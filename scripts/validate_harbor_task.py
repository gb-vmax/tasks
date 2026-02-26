#!/usr/bin/env python3
"""
Validate that task directories conform to the harbor specification.

Usage:
    # Validate all tasks in data/
    python scripts/validate_harbor_task.py data/

    # Validate specific task directories
    python scripts/validate_harbor_task.py data/task_abc123 data/task_def456

    # Validate with verbose output
    python scripts/validate_harbor_task.py -v data/

Exit codes:
    0 - All tasks valid
    1 - Validation errors found
"""

import argparse
import os
import sys

try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        tomllib = None


def validate_task(task_dir: str, verbose: bool = False) -> list[str]:
    """Validate a single task directory. Returns list of error strings."""
    errors = []
    task_id = os.path.basename(task_dir)

    def err(msg: str):
        errors.append(f"{task_id}: {msg}")

    def info(msg: str):
        if verbose:
            print(f"  [ok] {msg}")

    # ── Required files ──────────────────────────────────────────────
    required_files = {
        "task.toml": "task configuration",
        "instruction.md": "task instructions",
        "environment/Dockerfile": "Docker environment",
        "solution/solve.sh": "solution script",
        "tests/test.sh": "test script",
    }

    for rel_path, desc in required_files.items():
        full_path = os.path.join(task_dir, rel_path)
        if not os.path.isfile(full_path):
            err(f"missing required file: {rel_path} ({desc})")
        else:
            info(f"{rel_path} exists")

    # ── task.toml validation ────────────────────────────────────────
    toml_path = os.path.join(task_dir, "task.toml")
    if os.path.isfile(toml_path):
        if tomllib is None:
            # Python < 3.11 and no tomli installed — do basic text checks
            with open(toml_path) as f:
                content = f.read()
            if not content.strip():
                err("task.toml is empty")
            else:
                # Check for required sections
                for section in ["[verifier]", "[agent]", "[environment]"]:
                    if section not in content:
                        err(f"task.toml missing section: {section}")
                    else:
                        info(f"task.toml has {section}")
        else:
            try:
                with open(toml_path, "rb") as f:
                    toml_data = tomllib.load(f)
            except Exception as e:
                err(f"task.toml parse error: {e}")
                toml_data = None

            if toml_data is not None:
                # Required sections
                for section in ["verifier", "agent", "environment"]:
                    if section not in toml_data:
                        err(f"task.toml missing section: [{section}]")
                    else:
                        info(f"task.toml has [{section}]")

                # Verifier checks
                verifier = toml_data.get("verifier", {})
                if "timeout_sec" not in verifier:
                    err("task.toml [verifier] missing timeout_sec")
                elif not isinstance(verifier["timeout_sec"], (int, float)):
                    err("task.toml [verifier].timeout_sec must be a number")
                elif verifier["timeout_sec"] <= 0:
                    err("task.toml [verifier].timeout_sec must be positive")
                else:
                    info(f"verifier.timeout_sec = {verifier['timeout_sec']}")

                # Agent checks
                agent = toml_data.get("agent", {})
                if "timeout_sec" not in agent:
                    err("task.toml [agent] missing timeout_sec")
                elif not isinstance(agent["timeout_sec"], (int, float)):
                    err("task.toml [agent].timeout_sec must be a number")
                elif agent["timeout_sec"] <= 0:
                    err("task.toml [agent].timeout_sec must be positive")
                else:
                    info(f"agent.timeout_sec = {agent['timeout_sec']}")

                # Environment checks
                env = toml_data.get("environment", {})
                if "cpus" not in env:
                    err("task.toml [environment] missing cpus")
                if "memory" not in env and "memory_mb" not in env:
                    err("task.toml [environment] missing memory or memory_mb")

    # ── instruction.md validation ───────────────────────────────────
    instr_path = os.path.join(task_dir, "instruction.md")
    if os.path.isfile(instr_path):
        size = os.path.getsize(instr_path)
        if size == 0:
            err("instruction.md is empty")
        elif size < 20:
            err(f"instruction.md suspiciously short ({size} bytes)")
        else:
            info(f"instruction.md is {size} bytes")

    # ── Dockerfile validation ───────────────────────────────────────
    dockerfile_path = os.path.join(task_dir, "environment", "Dockerfile")
    if os.path.isfile(dockerfile_path):
        with open(dockerfile_path) as f:
            dockerfile = f.read()
        if not dockerfile.strip():
            err("Dockerfile is empty")
        else:
            lines = [l.strip() for l in dockerfile.splitlines() if l.strip() and not l.strip().startswith("#")]
            if not lines:
                err("Dockerfile has no instructions (only comments/blanks)")
            elif not lines[0].startswith("FROM "):
                err(f"Dockerfile first instruction must be FROM, got: {lines[0][:60]}")
            else:
                info(f"Dockerfile starts with {lines[0][:60]}")

    # ── solve.sh validation ─────────────────────────────────────────
    solve_path = os.path.join(task_dir, "solution", "solve.sh")
    if os.path.isfile(solve_path):
        with open(solve_path) as f:
            solve_content = f.read()
        if not solve_content.strip():
            err("solution/solve.sh is empty")
        elif not solve_content.startswith("#!/"):
            err("solution/solve.sh missing shebang (#!/bin/bash or similar)")
        else:
            info("solution/solve.sh has shebang")

    # ── test.sh validation ──────────────────────────────────────────
    test_path = os.path.join(task_dir, "tests", "test.sh")
    if os.path.isfile(test_path):
        with open(test_path) as f:
            # Read just the first 1KB to check the header (test.sh can be huge with embedded tarballs)
            test_header = f.read(1024)
        if not test_header.strip():
            err("tests/test.sh is empty")
        elif not test_header.startswith("#!/"):
            err("tests/test.sh missing shebang")
        else:
            info("tests/test.sh has shebang")

    return errors


def find_task_dirs(path: str) -> list[str]:
    """Find all task directories under a path.

    A task directory is identified by containing a task.toml file.
    """
    tasks = []
    if os.path.isfile(os.path.join(path, "task.toml")):
        # path itself is a task directory
        tasks.append(path)
    else:
        # Scan one level deep (data/<task_id>/task.toml)
        for entry in sorted(os.listdir(path)):
            candidate = os.path.join(path, entry)
            if os.path.isdir(candidate) and os.path.isfile(os.path.join(candidate, "task.toml")):
                tasks.append(candidate)
    return tasks


def main():
    parser = argparse.ArgumentParser(description="Validate harbor task directories")
    parser.add_argument("paths", nargs="+", help="Task directories or parent directories to scan")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show passing checks too")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    args = parser.parse_args()

    all_task_dirs = []
    for p in args.paths:
        all_task_dirs.extend(find_task_dirs(p))

    if not all_task_dirs:
        print("No task directories found.", file=sys.stderr)
        sys.exit(1)

    all_errors = {}
    passed = 0
    failed = 0

    for task_dir in all_task_dirs:
        task_id = os.path.basename(task_dir)
        if args.verbose:
            print(f"\nValidating {task_id}...")
        errors = validate_task(task_dir, verbose=args.verbose)
        if errors:
            all_errors[task_id] = errors
            failed += 1
        else:
            passed += 1

    if args.json:
        import json
        result = {
            "passed": passed,
            "failed": failed,
            "total": passed + failed,
            "errors": all_errors,
        }
        print(json.dumps(result, indent=2))
    else:
        if all_errors:
            print(f"\n{'='*60}")
            print(f"VALIDATION FAILED: {failed}/{passed+failed} tasks have errors\n")
            for task_id, errors in all_errors.items():
                for e in errors:
                    print(f"  ERROR: {e}")
            print()
        else:
            print(f"\nAll {passed} tasks passed validation.")

    sys.exit(1 if all_errors else 0)


if __name__ == "__main__":
    main()
