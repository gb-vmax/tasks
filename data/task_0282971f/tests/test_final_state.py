# test_final_state.py

import os
import pytest

LOG_DIR = "/home/user/logs"
LOG_FILE = "/home/user/logs/nginx-service.log"
ERRORS_ONLY_FILE = "/home/user/logs/errors_only.log"
ERROR_SUMMARY_FILE = "/home/user/logs/error_summary.txt"

EXPECTED_ERROR_LINES = [
    "2024-05-10T08:13:45 [ERROR] Failed to bind to port 8080: address already in use",
    "2024-05-10T08:15:33 [ERROR] Timeout reading from upstream: connection timed out",
    "2024-05-10T08:17:45 [ERROR] Worker process 4821 exited with code 1",
    "2024-05-10T08:20:55 [ERROR] SSL certificate validation failed: certificate expired",
]

EXPECTED_ERRORS_ONLY_CONTENT = "\n".join(EXPECTED_ERROR_LINES) + "\n"

EXPECTED_SUMMARY_CONTENT = "Total errors: 4\n"


# --- Precondition checks (input file still intact) ---

def test_nginx_log_file_still_exists():
    assert os.path.isfile(LOG_FILE), (
        f"Input log file '{LOG_FILE}' no longer exists. "
        "It should not have been removed or renamed."
    )


# --- errors_only.log checks ---

def test_errors_only_log_exists():
    assert os.path.isfile(ERRORS_ONLY_FILE), (
        f"Output file '{ERRORS_ONLY_FILE}' does not exist. "
        "The solution must create this file containing only the [ERROR] lines."
    )


def test_errors_only_log_has_four_lines():
    with open(ERRORS_ONLY_FILE, "r") as f:
        lines = f.readlines()
    # Strip trailing blank lines to count meaningful lines
    non_empty_lines = [l for l in lines if l.strip()]
    assert len(non_empty_lines) == 4, (
        f"'{ERRORS_ONLY_FILE}' should contain exactly 4 error lines, "
        f"but found {len(non_empty_lines)} non-empty lines.\n"
        f"File contents:\n{''.join(lines)}"
    )


def test_errors_only_log_contains_correct_lines():
    with open(ERRORS_ONLY_FILE, "r") as f:
        content = f.read()
    actual_lines = [line for line in content.splitlines() if line.strip()]
    assert actual_lines == EXPECTED_ERROR_LINES, (
        f"'{ERRORS_ONLY_FILE}' does not contain the expected error lines.\n"
        f"Expected lines:\n" + "\n".join(EXPECTED_ERROR_LINES) + "\n\n"
        f"Actual lines:\n" + "\n".join(actual_lines)
    )


def test_errors_only_log_preserves_original_order():
    with open(ERRORS_ONLY_FILE, "r") as f:
        actual_lines = [line.rstrip("\n") for line in f if line.strip()]
    for i, (expected, actual) in enumerate(zip(EXPECTED_ERROR_LINES, actual_lines)):
        assert actual == expected, (
            f"'{ERRORS_ONLY_FILE}' line {i + 1} is out of order or incorrect.\n"
            f"Expected: {expected!r}\n"
            f"Got:      {actual!r}"
        )


def test_errors_only_log_no_non_error_lines():
    with open(ERRORS_ONLY_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    for line in lines:
        assert "[ERROR]" in line, (
            f"'{ERRORS_ONLY_FILE}' contains a line without '[ERROR]':\n{line!r}\n"
            "Only [ERROR] lines should be present in this file."
        )


def test_errors_only_log_no_trailing_blank_line():
    with open(ERRORS_ONLY_FILE, "rb") as f:
        raw = f.read()
    # The file should end with exactly one newline after the last error line
    assert not raw.endswith(b"\n\n"), (
        f"'{ERRORS_ONLY_FILE}' ends with a trailing blank line. "
        "The file should have no trailing blank line after the last error entry."
    )


def test_errors_only_log_exact_content():
    with open(ERRORS_ONLY_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_ERRORS_ONLY_CONTENT, (
        f"'{ERRORS_ONLY_FILE}' does not match the expected exact content.\n"
        f"Expected (repr): {EXPECTED_ERRORS_ONLY_CONTENT!r}\n"
        f"Got      (repr): {content!r}"
    )


# --- error_summary.txt checks ---

def test_error_summary_exists():
    assert os.path.isfile(ERROR_SUMMARY_FILE), (
        f"Output file '{ERROR_SUMMARY_FILE}' does not exist. "
        "The solution must create this file with a one-line summary of error count."
    )


def test_error_summary_exact_content():
    with open(ERROR_SUMMARY_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_SUMMARY_CONTENT, (
        f"'{ERROR_SUMMARY_FILE}' does not match the expected content.\n"
        f"Expected (repr): {EXPECTED_SUMMARY_CONTENT!r}\n"
        f"Got      (repr): {content!r}"
    )


def test_error_summary_exactly_one_line():
    with open(ERROR_SUMMARY_FILE, "r") as f:
        lines = f.readlines()
    non_empty_lines = [l for l in lines if l.strip()]
    assert len(non_empty_lines) == 1, (
        f"'{ERROR_SUMMARY_FILE}' should contain exactly one line, "
        f"but found {len(non_empty_lines)} non-empty lines.\n"
        f"File contents:\n{''.join(lines)}"
    )


def test_error_summary_correct_format():
    with open(ERROR_SUMMARY_FILE, "r") as f:
        line = f.readline().rstrip("\n")
    assert line == "Total errors: 4", (
        f"'{ERROR_SUMMARY_FILE}' summary line has incorrect format or count.\n"
        f"Expected: 'Total errors: 4'\n"
        f"Got:      {line!r}"
    )


def test_error_summary_no_trailing_blank_line():
    with open(ERROR_SUMMARY_FILE, "rb") as f:
        raw = f.read()
    assert not raw.endswith(b"\n\n"), (
        f"'{ERROR_SUMMARY_FILE}' ends with a trailing blank line. "
        "The file should contain exactly one line followed by a single newline."
    )