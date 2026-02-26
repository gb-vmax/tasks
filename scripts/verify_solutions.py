#!/usr/bin/env python3
"""
Build Docker images, run solutions, and verify they pass tests.

Tracks which tasks have been successfully verified via a checksum file,
so each task only needs to be verified once (re-verified if changed).

Usage:
    # Verify all unverified/changed tasks
    python scripts/verify_solutions.py data/

    # Verify specific tasks (ignores checksum cache)
    python scripts/verify_solutions.py --force data/task_abc123

    # Dry run — show what would be verified without running anything
    python scripts/verify_solutions.py --dry-run data/

    # Set concurrency for parallel Docker builds
    python scripts/verify_solutions.py --jobs 4 data/
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

CHECKSUM_FILE = ".validated-solutions.json"


def compute_task_hash(task_dir: str) -> str:
    """Compute a stable hash of all files in a task directory.

    This is used to detect when a task has changed and needs re-verification.
    """
    h = hashlib.sha256()
    task_path = Path(task_dir)
    for filepath in sorted(task_path.rglob("*")):
        if filepath.is_file():
            rel = filepath.relative_to(task_path)
            h.update(str(rel).encode())
            h.update(filepath.read_bytes())
    return h.hexdigest()[:16]


def load_checksums(repo_root: str) -> dict:
    """Load the validated solutions checksum file."""
    path = os.path.join(repo_root, CHECKSUM_FILE)
    if os.path.isfile(path):
        with open(path) as f:
            return json.load(f)
    return {}


def save_checksums(repo_root: str, checksums: dict):
    """Save the validated solutions checksum file."""
    path = os.path.join(repo_root, CHECKSUM_FILE)
    with open(path, "w") as f:
        json.dump(checksums, f, indent=2, sort_keys=True)
        f.write("\n")


def find_task_dirs(path: str) -> list[str]:
    """Find all task directories under a path."""
    tasks = []
    if os.path.isfile(os.path.join(path, "task.toml")):
        tasks.append(os.path.abspath(path))
    else:
        for entry in sorted(os.listdir(path)):
            candidate = os.path.join(path, entry)
            if os.path.isdir(candidate) and os.path.isfile(os.path.join(candidate, "task.toml")):
                tasks.append(os.path.abspath(candidate))
    return tasks


def verify_task(task_dir: str, timeout: int = 600, platform: str = "") -> tuple[str, bool, str]:
    """Build a task's Docker image, run the solution, and check the test.

    Returns (task_id, success, message).
    """
    task_id = os.path.basename(task_dir)
    # Docker tags: [a-z0-9] with single separators, no slashes (local image)
    safe_tag = re.sub(r'[^a-z0-9]', '-', task_id.lower())
    safe_tag = re.sub(r'-+', '-', safe_tag).strip('-')[:120]
    image_tag = f"hci-{safe_tag}"

    try:
        # Step 1: Build Docker image
        env_dir = os.path.join(task_dir, "environment")
        build_cmd = ["docker", "build"]
        if platform:
            build_cmd += ["--platform", platform]
        build_cmd += ["-t", image_tag, env_dir]
        result = subprocess.run(
            build_cmd,
            capture_output=True, text=True, timeout=300,
        )
        if result.returncode != 0:
            return (task_id, False, f"Docker build failed:\n{result.stderr[-500:]}")

        # Step 2: Run solution inside the container
        solve_sh = os.path.join(task_dir, "solution", "solve.sh")
        test_sh = os.path.join(task_dir, "tests", "test.sh")

        # Create a runner script that:
        # 1. Runs the solution
        # 2. Runs the test
        # 3. Checks the reward
        runner = """#!/bin/bash
set -euo pipefail

# Create required directories
mkdir -p /logs/verifier

# Run solution
echo "=== Running solution ==="
bash /solution/solve.sh
echo "=== Solution complete ==="

# Run tests
echo "=== Running tests ==="
bash /tests/test.sh
echo "=== Tests complete ==="

# Check reward
if [ -f /logs/verifier/reward.txt ]; then
    reward=$(cat /logs/verifier/reward.txt | tr -d '[:space:]')
    if [ "$reward" = "1" ] || [ "$reward" = "1.0" ]; then
        echo "REWARD_CHECK_PASSED"
        exit 0
    else
        echo "REWARD_CHECK_FAILED: reward=$reward"
        exit 1
    fi
else
    echo "REWARD_CHECK_FAILED: /logs/verifier/reward.txt not found"
    exit 1
fi
"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".sh", delete=False) as f:
            f.write(runner)
            runner_path = f.name

        try:
            # Mount solution, tests, and runner into the container
            solution_dir = os.path.join(task_dir, "solution")
            tests_dir = os.path.join(task_dir, "tests")
            run_cmd = [
                "docker", "run", "--rm",
            ]
            if platform:
                run_cmd += ["--platform", platform]
            run_cmd += [
                "-v", f"{solution_dir}:/solution:ro",
                "-v", f"{tests_dir}:/tests:ro",
                "-v", f"{runner_path}:/runner.sh:ro",
                image_tag,
                "bash", "/runner.sh",
            ]
            result = subprocess.run(
                run_cmd,
                capture_output=True, text=True, timeout=timeout,
            )
        finally:
            os.unlink(runner_path)

        if result.returncode != 0:
            output = (result.stdout + result.stderr)[-1000:]
            return (task_id, False, f"Solution verification failed:\n{output}")

        if "REWARD_CHECK_PASSED" in result.stdout:
            return (task_id, True, "Solution verified successfully")
        else:
            return (task_id, False, f"Unexpected output:\n{result.stdout[-500:]}")

    except subprocess.TimeoutExpired:
        return (task_id, False, f"Timed out after {timeout}s")
    except Exception as e:
        return (task_id, False, f"Error: {e}")
    finally:
        # Clean up Docker image
        subprocess.run(
            ["docker", "rmi", "-f", image_tag],
            capture_output=True, timeout=30,
        )


def main():
    parser = argparse.ArgumentParser(description="Verify harbor task solutions")
    parser.add_argument("paths", nargs="+", help="Task directories or parent directories to scan")
    parser.add_argument("--force", action="store_true", help="Re-verify even if checksum matches")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be verified")
    parser.add_argument("--jobs", type=int, default=2, help="Parallel verification jobs (default: 2)")
    parser.add_argument("--timeout", type=int, default=600, help="Per-task timeout in seconds (default: 600)")
    parser.add_argument("--platform", type=str, default="", help="Docker platform (e.g. linux/amd64)")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    args = parser.parse_args()

    # Determine repo root (parent of scripts/)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Find all task directories
    all_task_dirs = []
    for p in args.paths:
        all_task_dirs.extend(find_task_dirs(p))

    if not all_task_dirs:
        print("No task directories found.", file=sys.stderr)
        sys.exit(1)

    # Load existing checksums
    checksums = load_checksums(repo_root)

    # Determine which tasks need verification
    tasks_to_verify = []
    tasks_already_verified = []

    for task_dir in all_task_dirs:
        task_id = os.path.basename(task_dir)
        current_hash = compute_task_hash(task_dir)

        if not args.force and checksums.get(task_id) == current_hash:
            tasks_already_verified.append(task_id)
        else:
            tasks_to_verify.append((task_dir, task_id, current_hash))

    print(f"Tasks found: {len(all_task_dirs)}")
    print(f"Already verified (unchanged): {len(tasks_already_verified)}")
    print(f"Need verification: {len(tasks_to_verify)}")

    if args.dry_run:
        if tasks_to_verify:
            print("\nWould verify:")
            for _, task_id, _ in tasks_to_verify:
                print(f"  {task_id}")
        sys.exit(0)

    if not tasks_to_verify:
        print("\nAll tasks are already verified!")
        sys.exit(0)

    # Run verifications
    print(f"\nVerifying {len(tasks_to_verify)} tasks (jobs={args.jobs})...\n")

    results = {"passed": [], "failed": []}

    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = {}
        for task_dir, task_id, current_hash in tasks_to_verify:
            future = executor.submit(verify_task, task_dir, args.timeout, args.platform)
            futures[future] = (task_id, current_hash)

        for future in as_completed(futures):
            task_id, current_hash = futures[future]
            tid, success, message = future.result()

            if success:
                results["passed"].append(tid)
                checksums[tid] = current_hash
                # Save after each success so we don't lose progress
                save_checksums(repo_root, checksums)
                print(f"  PASS: {tid}")
            else:
                results["failed"].append({"task_id": tid, "message": message})
                print(f"  FAIL: {tid}")
                print(f"        {message[:200]}")

    # Summary
    print(f"\n{'='*60}")
    print(f"Passed: {len(results['passed'])}")
    print(f"Failed: {len(results['failed'])}")
    print(f"Previously verified: {len(tasks_already_verified)}")

    if args.json:
        print(json.dumps(results, indent=2))

    if results["failed"]:
        print("\nFailed tasks:")
        for item in results["failed"]:
            print(f"  {item['task_id']}: {item['message'][:100]}")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
