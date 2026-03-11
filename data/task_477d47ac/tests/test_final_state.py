# test_final_state.py

import os
import pytest

LOG_DIR = "/home/user/logs"
APP_LOG = "/home/user/logs/app.log"
ERRORS_ONLY_LOG = "/home/user/logs/errors_only.log"
ERROR_SUMMARY_TXT = "/home/user/logs/error_summary.txt"

EXPECTED_ERROR_LINES = [
    "2024-04-01T08:01:12Z ERROR Failed to load config file: missing key 'timeout'",
    "2024-04-01T08:02:10Z ERROR Null pointer exception in UserService.getById()",
    "2024-04-01T08:04:01Z ERROR Disk write failed: /var/data/session_store",
    "2024-04-01T08:05:45Z ERROR Connection timeout to upstream service: payments-svc",
    "2024-04-01T08:07:55Z ERROR Unhandled exception in request pipeline: NullReferenceException",
    "2024-04-01T08:09:00Z ERROR Authentication service unavailable",
]

EXPECTED_ERRORS_ONLY_CONTENT = "\n".join(EXPECTED_ERROR_LINES) + "\n"

EXPECTED_SUMMARY_CONTENT = "Total ERROR lines: 6"


def test_errors_only_log_exists():
    assert os.path.isfile(ERRORS_ONLY_LOG), (
        f"File '{ERRORS_ONLY_LOG}' does not exist. "
        "It should have been created by filtering ERROR lines from app.log."
    )


def test_error_summary_txt_exists():
    assert os.path.isfile(ERROR_SUMMARY_TXT), (
        f"File '{ERROR_SUMMARY_TXT}' does not exist. "
        "It should have been created with the error count summary."
    )


def test_errors_only_log_line_count():
    with open(ERRORS_ONLY_LOG, "r") as f:
        lines = [line for line in f if line.strip()]
    assert len(lines) == 6, (
        f"Expected 6 lines in '{ERRORS_ONLY_LOG}', but found {len(lines)}. "
        "The file should contain exactly the 6 ERROR lines from app.log."
    )


def test_errors_only_log_contains_only_error_lines():
    with open(ERRORS_ONLY_LOG, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    for line in lines:
        assert "ERROR" in line, (
            f"Line in '{ERRORS_ONLY_LOG}' does not contain 'ERROR': {repr(line)}. "
            "Only lines containing 'ERROR' should be present."
        )


def test_errors_only_log_exact_content():
    with open(ERRORS_ONLY_LOG, "r") as f:
        actual_content = f.read()
    # Normalize: strip trailing whitespace/newlines for comparison of lines
    actual_lines = [line.rstrip("\n") for line in actual_content.splitlines() if line.strip()]
    assert actual_lines == EXPECTED_ERROR_LINES, (
        f"Content of '{ERRORS_ONLY_LOG}' does not match expected.\n"
        f"Expected lines:\n" + "\n".join(EXPECTED_ERROR_LINES) + "\n\n"
        f"Actual lines:\n" + "\n".join(actual_lines)
    )


def test_errors_only_log_order():
    with open(ERRORS_ONLY_LOG, "r") as f:
        actual_lines = [line.rstrip("\n") for line in f if line.strip()]
    for i, (actual, expected) in enumerate(zip(actual_lines, EXPECTED_ERROR_LINES)):
        assert actual == expected, (
            f"Line {i + 1} of '{ERRORS_ONLY_LOG}' is incorrect.\n"
            f"Expected: {repr(expected)}\n"
            f"Actual:   {repr(actual)}"
        )


def test_error_summary_exact_content():
    with open(ERROR_SUMMARY_TXT, "r") as f:
        actual_content = f.read()
    # Strip trailing newline(s) for comparison — the summary should be exactly one line
    actual_stripped = actual_content.rstrip("\n")
    assert actual_stripped == EXPECTED_SUMMARY_CONTENT, (
        f"Content of '{ERROR_SUMMARY_TXT}' does not match expected.\n"
        f"Expected: {repr(EXPECTED_SUMMARY_CONTENT)}\n"
        f"Actual:   {repr(actual_stripped)}"
    )


def test_error_summary_no_extra_lines():
    with open(ERROR_SUMMARY_TXT, "r") as f:
        actual_content = f.read()
    lines = actual_content.rstrip("\n").splitlines()
    assert len(lines) == 1, (
        f"'{ERROR_SUMMARY_TXT}' should contain exactly 1 line, but found {len(lines)} lines.\n"
        f"Content: {repr(actual_content)}"
    )


def test_error_summary_correct_count_value():
    with open(ERROR_SUMMARY_TXT, "r") as f:
        actual_content = f.read().strip()
    assert actual_content == "Total ERROR lines: 6", (
        f"'{ERROR_SUMMARY_TXT}' has incorrect content.\n"
        f"Expected: 'Total ERROR lines: 6'\n"
        f"Actual:   {repr(actual_content)}"
    )


def test_app_log_unchanged():
    """Ensure the original app.log was not modified."""
    expected_app_log_content = """\
2024-04-01T08:00:01Z INFO  Server started on port 8080
2024-04-01T08:00:45Z INFO  Connected to database
2024-04-01T08:01:12Z ERROR Failed to load config file: missing key 'timeout'
2024-04-01T08:01:30Z WARN  Retrying database connection (attempt 1)
2024-04-01T08:01:55Z INFO  Request received: GET /api/status
2024-04-01T08:02:10Z ERROR Null pointer exception in UserService.getById()
2024-04-01T08:02:11Z INFO  Request received: POST /api/login
2024-04-01T08:03:00Z INFO  Cache warmed up successfully
2024-04-01T08:03:45Z WARN  High memory usage detected: 82%
2024-04-01T08:04:01Z ERROR Disk write failed: /var/data/session_store
2024-04-01T08:04:02Z INFO  Fallback to in-memory store activated
2024-04-01T08:05:15Z INFO  Request received: GET /api/users
2024-04-01T08:05:45Z ERROR Connection timeout to upstream service: payments-svc
2024-04-01T08:06:00Z INFO  Scheduled job 'cleanup' started
2024-04-01T08:06:30Z INFO  Scheduled job 'cleanup' completed
2024-04-01T08:07:10Z WARN  Rate limit threshold approaching for client 10.0.0.5
2024-04-01T08:07:55Z ERROR Unhandled exception in request pipeline: NullReferenceException
2024-04-01T08:08:30Z INFO  Health check passed
2024-04-01T08:09:00Z ERROR Authentication service unavailable
2024-04-01T08:09:45Z INFO  Request received: DELETE /api/session/4892
2024-04-01T08:10:20Z WARN  Deprecated API endpoint called: /api/v1/users
2024-04-01T08:11:00Z INFO  Graceful shutdown initiated"""

    assert os.path.isfile(APP_LOG), (
        f"Original log file '{APP_LOG}' is missing."
    )
    with open(APP_LOG, "r") as f:
        actual_content = f.read().rstrip("\n")
    assert actual_content == expected_app_log_content, (
        f"The original '{APP_LOG}' was modified. It should remain unchanged.\n"
        f"Expected content matches the original 22-line log file."
    )


def test_log_dir_contains_expected_files():
    entries = set(os.listdir(LOG_DIR))
    expected_files = {"app.log", "errors_only.log", "error_summary.txt"}
    missing = expected_files - entries
    assert not missing, (
        f"The following expected files are missing from '{LOG_DIR}': {missing}"
    )