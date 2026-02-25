# test_final_state.py

import os
import subprocess
import pytest

HOME = "/home/user"
PIPELINE_UTILS_DIR = os.path.join(HOME, "pipeline-utils")
BUILD_STATUS_FILE = os.path.join(PIPELINE_UTILS_DIR, "build_status.txt")
PIPELINE_VERIFICATION_LOG = os.path.join(HOME, "pipeline-verification.log")
EXPECTED_BUILD_STATUS = ["Pipeline: Android Release", "Status: Success"]
EXPECTED_COMMIT_MESSAGE = "Initial build status"
EXPECTED_TAG = "build-v1.0"


def run_git(args, cwd):
    """Run a git command and return stdout as string (stripped)."""
    result = subprocess.run(
        ["git"] + args,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Git command failed: git {' '.join(args)}\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )
    return result.stdout.strip()


def test_pipeline_utils_dir_exists_and_is_git_repo():
    assert os.path.isdir(PIPELINE_UTILS_DIR), (
        f"Directory {PIPELINE_UTILS_DIR} does not exist."
    )
    git_dir = os.path.join(PIPELINE_UTILS_DIR, ".git")
    assert os.path.isdir(git_dir), (
        f"Directory {PIPELINE_UTILS_DIR} exists but is not a git repository (.git missing)."
    )


def test_build_status_file_content_and_tracked():
    assert os.path.isfile(BUILD_STATUS_FILE), (
        f"File {BUILD_STATUS_FILE} does not exist."
    )
    with open(BUILD_STATUS_FILE, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]
    assert lines == EXPECTED_BUILD_STATUS, (
        f"{BUILD_STATUS_FILE} does not contain the expected content. "
        f"Expected lines: {EXPECTED_BUILD_STATUS!r}, got: {lines!r}"
    )

    # Check if build_status.txt is tracked and not changed
    tracked_files = run_git(["ls-files"], cwd=PIPELINE_UTILS_DIR).splitlines()
    assert "build_status.txt" in tracked_files, (
        f"{BUILD_STATUS_FILE} is not tracked in git."
    )
    status = run_git(["status", "--porcelain"], cwd=PIPELINE_UTILS_DIR)
    assert status == "", (
        f"Git repository has uncommitted changes:\n{status}"
    )


def test_single_commit_with_expected_message_and_file():
    # There should be exactly one commit, with the expected message
    log = run_git(
        ["log", "--pretty=format:%H%n%s", "--reverse"], cwd=PIPELINE_UTILS_DIR
    )
    log_lines = log.splitlines()
    assert len(log_lines) == 2, (
        f"Expected a single commit in the repository. Got log:\n{log}"
    )
    commit_hash, commit_msg = log_lines
    assert commit_msg == EXPECTED_COMMIT_MESSAGE, (
        f"Commit message is '{commit_msg}', expected '{EXPECTED_COMMIT_MESSAGE}'."
    )

    # Check build_status.txt is present in the tree for this commit
    files_in_commit = run_git(
        ["ls-tree", "--name-only", commit_hash], cwd=PIPELINE_UTILS_DIR
    ).splitlines()
    assert "build_status.txt" in files_in_commit, (
        f"'build_status.txt' is not present in the initial commit."
    )


def test_tag_exists_and_points_to_commit():
    # Get HEAD commit hash
    head_hash = run_git(["rev-parse", "HEAD"], cwd=PIPELINE_UTILS_DIR)
    # Get tag hash
    try:
        tag_hash = run_git(
            ["rev-list", "-n", "1", EXPECTED_TAG], cwd=PIPELINE_UTILS_DIR
        )
    except RuntimeError:
        pytest.fail(f"Tag '{EXPECTED_TAG}' does not exist in the repository.")

    assert tag_hash == head_hash, (
        f"Tag '{EXPECTED_TAG}' does not point to the most recent commit.\n"
        f"HEAD: {head_hash}\nTag points to: {tag_hash}"
    )


def test_pipeline_verification_log_content():
    assert os.path.isfile(PIPELINE_VERIFICATION_LOG), (
        f"Verification log file {PIPELINE_VERIFICATION_LOG} does not exist."
    )
    with open(PIPELINE_VERIFICATION_LOG, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]

    # Compose expected log (dynamically get commit hash and tag)
    head_hash = run_git(["rev-parse", "HEAD"], cwd=PIPELINE_UTILS_DIR)
    # Confirm tag points to HEAD
    tag_hash = run_git(["rev-list", "-n", "1", EXPECTED_TAG], cwd=PIPELINE_UTILS_DIR)
    assert tag_hash == head_hash, (
        f"Tag '{EXPECTED_TAG}' does not point to HEAD commit in verification step."
    )

    expected_log = [
        head_hash,
        EXPECTED_COMMIT_MESSAGE,
        EXPECTED_BUILD_STATUS[0],
        EXPECTED_BUILD_STATUS[1],
        EXPECTED_TAG,
    ]

    assert lines == expected_log, (
        f"Verification log {PIPELINE_VERIFICATION_LOG} has incorrect content.\n"
        f"Expected:\n{expected_log!r}\nGot:\n{lines!r}\n"
        "Check for extra lines, missing lines, or incorrect data."
    )