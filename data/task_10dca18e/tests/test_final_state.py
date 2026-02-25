# test_final_state.py

import os
import stat
import pytest

HOME = "/home/user"
LOGS_DIR = os.path.join(HOME, "logs")
SCRIPTS_DIR = os.path.join(HOME, "scripts")
ERRORS_DIR = os.path.join(HOME, "errors")

SCRIPT_PATH = os.path.join(SCRIPTS_DIR, "extract_errors.sh")

EXPECTED_ERRORS_FILES = {
    os.path.join(ERRORS_DIR, "app_backend.errors"): [
        "ERROR Database connection failed",
        "ERROR Timeout occurred",
        "ERROR Failed to handle request",
    ],
    os.path.join(ERRORS_DIR, "app_frontend.errors"): [
        # empty file; no ERROR lines
    ],
    os.path.join(ERRORS_DIR, "app_worker.errors"): [
        "ERROR Task execution error: OutOfMemory",
        "ERROR Unexpected shutdown",
    ],
    os.path.join(ERRORS_DIR, "app_scheduler.errors"): [
        "ERROR Failed to load schedule configuration",
        "ERROR Invalid cron pattern detected",
    ],
}

SUMMARY_PATH = os.path.join(ERRORS_DIR, "error_summary.log")
EXPECTED_SUMMARY = [
    "app_backend.log: 3 errors",
    "app_frontend.log: 0 errors",
    "app_scheduler.log: 2 errors",
    "app_worker.log: 2 errors",
]

REQUIRED_DIRS = [LOGS_DIR, SCRIPTS_DIR, ERRORS_DIR]

@pytest.mark.parametrize("directory", REQUIRED_DIRS)
def test_required_directories_exist_and_writable(directory):
    assert os.path.isdir(directory), f"Required directory missing: {directory}"
    assert os.access(directory, os.W_OK), f"Directory not writable: {directory}"

def test_extract_errors_script_exists_and_executable():
    assert os.path.isfile(SCRIPT_PATH), (
        f"Shell script not found at {SCRIPT_PATH}. "
        "You must create /home/user/scripts/extract_errors.sh."
    )
    st = os.stat(SCRIPT_PATH)
    mode = st.st_mode
    # Check executable by user, group, others (755)
    is_executable = bool(mode & stat.S_IXUSR and mode & stat.S_IXGRP and mode & stat.S_IXOTH)
    assert is_executable, (
        f"{SCRIPT_PATH} exists but is not executable by user/group/others. "
        "Set its mode to 755."
    )

def test_extract_errors_script_uses_background_jobs():
    with open(SCRIPT_PATH, "r") as f:
        script_text = f.read()
    # Check for use of '&' (background process) and 'wait'
    # Accept either 'wait' or 'wait\n' or 'wait $!'
    has_background = any(
        line.strip().endswith("&") for line in script_text.splitlines()
        if line.strip() and not line.strip().startswith("#")
    )
    has_wait = any(
        line.strip().startswith("wait") for line in script_text.splitlines()
        if line.strip() and not line.strip().startswith("#")
    )
    assert has_background, (
        f"{SCRIPT_PATH} does not use background jobs ('&'). "
        "Each extraction must run in parallel as a background process."
    )
    assert has_wait, (
        f"{SCRIPT_PATH} does not use 'wait' after spawning background jobs. "
        "You must wait for all background jobs to finish before the script exits."
    )

@pytest.mark.parametrize("errors_path,expected_lines", EXPECTED_ERRORS_FILES.items())
def test_error_files_exist_and_content(errors_path, expected_lines):
    assert os.path.isfile(errors_path), (
        f"Expected extracted error file missing: {errors_path}"
    )
    with open(errors_path, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    assert lines == expected_lines, (
        f"File {errors_path} does not have the expected ERROR lines.\n"
        f"Expected ({len(expected_lines)} lines):\n{expected_lines}\n"
        f"Found ({len(lines)} lines):\n{lines}"
    )

def test_no_extra_errors_files():
    errors_files = [f for f in os.listdir(ERRORS_DIR) if f.endswith(".errors")]
    expected_files = sorted([
        "app_backend.errors",
        "app_frontend.errors",
        "app_worker.errors",
        "app_scheduler.errors",
    ])
    assert sorted(errors_files) == expected_files, (
        f"Unexpected .errors files in {ERRORS_DIR}. "
        f"Expected only: {expected_files}. Found: {sorted(errors_files)}"
    )

def test_error_summary_log_exists_and_content():
    assert os.path.isfile(SUMMARY_PATH), (
        f"Summary file missing: {SUMMARY_PATH}"
    )
    with open(SUMMARY_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    assert lines == EXPECTED_SUMMARY, (
        f"error_summary.log does not match expected format or content.\n"
        f"Expected ({len(EXPECTED_SUMMARY)} lines):\n{EXPECTED_SUMMARY}\n"
        f"Found ({len(lines)} lines):\n{lines}\n"
        "Check for exact order, no extra whitespace, and correct error counts."
    )

def test_error_summary_log_order_and_format():
    # This test ensures alphabetical order and strict format
    with open(SUMMARY_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    # Check order is strictly as specified
    basenames = [line.split(":")[0] for line in lines]
    expected_basenames = [
        "app_backend.log",
        "app_frontend.log",
        "app_scheduler.log",
        "app_worker.log",
    ]
    assert basenames == expected_basenames, (
        f"Log filenames in error_summary.log are not in strict alphabetical order.\n"
        f"Expected order: {expected_basenames}\nFound: {basenames}"
    )
    # Check format for each line
    for idx, line in enumerate(lines):
        parts = line.split(": ")
        assert len(parts) == 2 and parts[1].endswith("errors"), (
            f"Line {idx+1} of error_summary.log is not in the required format '<LOG_FILENAME>: <ERROR_COUNT> errors':\n"
            f"Found: {line!r}"
        )
        count_part = parts[1][:-7]  # Remove trailing ' errors'
        try:
            count = int(count_part)
        except ValueError:
            assert False, (
                f"Line {idx+1} of error_summary.log does not provide a valid integer error count:\n"
                f"Found: {line!r}"
            )

def test_no_extra_files_in_errors_dir():
    allowed = set([
        "app_backend.errors",
        "app_frontend.errors",
        "app_worker.errors",
        "app_scheduler.errors",
        "error_summary.log",
    ])
    found = set(os.listdir(ERRORS_DIR))
    extra = found - allowed
    assert not extra, (
        f"Unexpected extra files found in {ERRORS_DIR}: {extra}. "
        f"Only these should exist: {sorted(allowed)}"
    )