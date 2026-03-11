# test_final_state.py

import os
import pytest

ERROR_COUNT_FILE = "/home/user/logs/error_count.txt"
ERRORS_ONLY_LOG = "/home/user/logs/errors_only.log"
SERVICE_LOG = "/home/user/logs/service.log"

EXPECTED_ERROR_COUNT = 6

EXPECTED_ERROR_LINES = [
    "[ERROR] 2024-06-01 08:02:34 - Failed to connect to database: connection refused",
    "[ERROR] 2024-06-01 08:02:52 - Retry limit exceeded, giving up on database connection",
    "[ERROR] 2024-06-01 08:10:15 - Null pointer exception in UserSessionHandler at line 42",
    "[ERROR] 2024-06-01 08:21:05 - Out of memory: failed to allocate 512MB for cache",
    "[ERROR] 2024-06-01 08:45:22 - Unhandled exception in RequestRouter: timeout after 30s",
    "[ERROR] 2024-06-01 09:15:44 - Authentication service unreachable: no route to host",
]

EXPECTED_ERRORS_ONLY_CONTENT = "\n".join(EXPECTED_ERROR_LINES) + "\n"

EXPECTED_ERROR_COUNT_CONTENT = f"{EXPECTED_ERROR_COUNT}\n"


# --- Tests for error_count.txt ---

def test_error_count_file_exists():
    assert os.path.isfile(ERROR_COUNT_FILE), (
        f"File '{ERROR_COUNT_FILE}' does not exist. "
        "The error count file must be created after completing the task."
    )


def test_error_count_file_is_readable():
    assert os.access(ERROR_COUNT_FILE, os.R_OK), (
        f"File '{ERROR_COUNT_FILE}' is not readable."
    )


def test_error_count_file_content_is_integer():
    with open(ERROR_COUNT_FILE, "r") as f:
        content = f.read()
    stripped = content.strip()
    assert stripped.isdigit(), (
        f"Content of '{ERROR_COUNT_FILE}' should be a plain integer, got: {repr(content)}"
    )


def test_error_count_file_correct_value():
    with open(ERROR_COUNT_FILE, "r") as f:
        content = f.read()
    stripped = content.strip()
    assert stripped.isdigit(), (
        f"Content of '{ERROR_COUNT_FILE}' is not a valid integer: {repr(content)}"
    )
    count = int(stripped)
    assert count == EXPECTED_ERROR_COUNT, (
        f"Expected error count to be {EXPECTED_ERROR_COUNT}, but got {count}. "
        f"File content: {repr(content)}"
    )


def test_error_count_file_exact_content():
    with open(ERROR_COUNT_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_ERROR_COUNT_CONTENT, (
        f"Exact content of '{ERROR_COUNT_FILE}' does not match.\n"
        f"Expected: {repr(EXPECTED_ERROR_COUNT_CONTENT)}\n"
        f"Actual:   {repr(content)}\n"
        "The file should contain exactly the integer followed by a newline, nothing else."
    )


def test_error_count_file_single_line():
    with open(ERROR_COUNT_FILE, "r") as f:
        lines = f.readlines()
    non_empty_lines = [l for l in lines if l.strip()]
    assert len(non_empty_lines) == 1, (
        f"'{ERROR_COUNT_FILE}' should contain exactly one non-empty line, "
        f"but found {len(non_empty_lines)} non-empty lines. Lines: {lines}"
    )


# --- Tests for errors_only.log ---

def test_errors_only_log_exists():
    assert os.path.isfile(ERRORS_ONLY_LOG), (
        f"File '{ERRORS_ONLY_LOG}' does not exist. "
        "The errors-only log file must be created after completing the task."
    )


def test_errors_only_log_is_readable():
    assert os.access(ERRORS_ONLY_LOG, os.R_OK), (
        f"File '{ERRORS_ONLY_LOG}' is not readable."
    )


def test_errors_only_log_line_count():
    with open(ERRORS_ONLY_LOG, "r") as f:
        lines = [line for line in f if line.strip()]
    assert len(lines) == EXPECTED_ERROR_COUNT, (
        f"Expected {EXPECTED_ERROR_COUNT} non-empty lines in '{ERRORS_ONLY_LOG}', "
        f"but found {len(lines)}."
    )


def test_errors_only_log_all_lines_are_error_level():
    with open(ERRORS_ONLY_LOG, "r") as f:
        lines = f.readlines()
    non_empty_lines = [line.rstrip("\n") for line in lines if line.strip()]
    for i, line in enumerate(non_empty_lines, start=1):
        assert line.startswith("[ERROR]"), (
            f"Line {i} in '{ERRORS_ONLY_LOG}' does not start with '[ERROR]': {repr(line)}\n"
            "Only ERROR-level lines should be present in this file."
        )


def test_errors_only_log_correct_lines():
    with open(ERRORS_ONLY_LOG, "r") as f:
        lines = f.readlines()
    actual_lines = [line.rstrip("\n") for line in lines if line.strip()]
    assert actual_lines == EXPECTED_ERROR_LINES, (
        f"Lines in '{ERRORS_ONLY_LOG}' do not match expected ERROR lines.\n"
        f"Expected ({len(EXPECTED_ERROR_LINES)} lines):\n"
        + "\n".join(EXPECTED_ERROR_LINES)
        + f"\n\nActual ({len(actual_lines)} lines):\n"
        + "\n".join(actual_lines)
    )


def test_errors_only_log_exact_content():
    with open(ERRORS_ONLY_LOG, "r") as f:
        content = f.read()
    assert content == EXPECTED_ERRORS_ONLY_CONTENT, (
        f"Exact content of '{ERRORS_ONLY_LOG}' does not match expected content.\n"
        f"Expected:\n{repr(EXPECTED_ERRORS_ONLY_CONTENT)}\n\n"
        f"Actual:\n{repr(content)}\n"
        "Ensure lines are in the same order as the source file with no extra blank lines or headers."
    )


def test_errors_only_log_preserves_order():
    with open(ERRORS_ONLY_LOG, "r") as f:
        actual_lines = [line.rstrip("\n") for line in f if line.strip()]
    for i, (actual, expected) in enumerate(zip(actual_lines, EXPECTED_ERROR_LINES), start=1):
        assert actual == expected, (
            f"Line {i} in '{ERRORS_ONLY_LOG}' does not match expected.\n"
            f"Expected: {repr(expected)}\n"
            f"Actual:   {repr(actual)}\n"
            "Lines must be in the same order as they appear in the source log file."
        )


def test_errors_only_log_no_extra_content():
    with open(ERRORS_ONLY_LOG, "r") as f:
        content = f.read()
    # Should not contain INFO or WARN lines
    for line in content.splitlines():
        assert not line.startswith("[INFO]"), (
            f"'{ERRORS_ONLY_LOG}' contains an INFO line that should not be there: {repr(line)}"
        )
        assert not line.startswith("[WARN]"), (
            f"'{ERRORS_ONLY_LOG}' contains a WARN line that should not be there: {repr(line)}"
        )


# --- Sanity check: source log file is unchanged ---

def test_service_log_still_exists_and_unchanged():
    assert os.path.isfile(SERVICE_LOG), (
        f"Source file '{SERVICE_LOG}' no longer exists. It must not be modified or deleted."
    )
    with open(SERVICE_LOG, "r") as f:
        lines = f.readlines()
    error_lines = [line.rstrip("\n") for line in lines if line.startswith("[ERROR]")]
    assert len(error_lines) == EXPECTED_ERROR_COUNT, (
        f"Source file '{SERVICE_LOG}' appears to have been modified. "
        f"Expected {EXPECTED_ERROR_COUNT} ERROR lines, found {len(error_lines)}."
    )