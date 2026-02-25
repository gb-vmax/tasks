# test_final_state.py

import os
import pytest

APP_LOG = "/home/user/server/app.log"
AUTH_FAILURE_LOG = "/home/user/server/auth_failure.log"
AUTH_SUMMARY = "/home/user/server/auth_summary.txt"

# The expected lines that should appear in auth_failure.log, in order, verbatim
EXPECTED_AUTH_FAILURE_LINES = [
    "2024-05-01 09:32:14 ERROR authentication failed for user=smith\n",
    "2024-05-01 09:33:50 WARN Invalid Password for user=admin\n",
    "2024-05-01 09:35:02 ERROR authentication failed for user=alice\n",
]

EXPECTED_SUMMARY_LINE = "Total failures: 3\n"

def read_file_lines(path):
    """Helper to read lines from a file, preserving line endings, returns list of lines."""
    with open(path, "r", encoding="utf-8") as f:
        # Read lines with their original line endings preserved
        return f.readlines()

def test_auth_failure_log_exists():
    assert os.path.isfile(AUTH_FAILURE_LOG), (
        f"Expected {AUTH_FAILURE_LOG} to exist after task completion, but it does not."
    )

def test_auth_failure_log_content_and_order():
    assert os.path.isfile(AUTH_FAILURE_LOG), (
        f"{AUTH_FAILURE_LOG} does not exist."
    )
    actual_lines = read_file_lines(AUTH_FAILURE_LOG)
    # Normalize line endings to \n for comparison
    actual_lines = [l.replace('\r\n', '\n').replace('\r', '\n') for l in actual_lines]
    expected_lines = [l.replace('\r\n', '\n').replace('\r', '\n') for l in EXPECTED_AUTH_FAILURE_LINES]
    assert actual_lines == expected_lines, (
        f"{AUTH_FAILURE_LOG} does not contain the correct filtered lines in order.\n"
        f"Expected lines:\n{''.join(expected_lines)}\n"
        f"Actual lines:\n{''.join(actual_lines)}\n"
        f"Each line must match exactly, and only lines containing "
        f"'authentication failed' or 'invalid password' (case-insensitive) should be present."
    )

def test_auth_failure_log_no_extra_lines():
    lines = read_file_lines(AUTH_FAILURE_LOG)
    # Normalize line endings
    lines = [l.replace('\r\n', '\n').replace('\r', '\n') for l in lines]
    assert len(lines) == len(EXPECTED_AUTH_FAILURE_LINES), (
        f"{AUTH_FAILURE_LOG} contains {len(lines)} lines, but exactly {len(EXPECTED_AUTH_FAILURE_LINES)} are expected."
    )

def test_auth_failure_log_lines_are_verbatim_from_app_log():
    # This test ensures no extra whitespace or modifications were introduced
    app_log_lines = read_file_lines(APP_LOG)
    # Normalize line endings
    app_log_lines = [l.replace('\r\n', '\n').replace('\r', '\n') for l in app_log_lines]
    filtered_lines = []
    for line in app_log_lines:
        lwr = line.lower()
        if "authentication failed" in lwr or "invalid password" in lwr:
            filtered_lines.append(line.replace('\r\n', '\n').replace('\r', '\n'))
    actual_lines = read_file_lines(AUTH_FAILURE_LOG)
    actual_lines = [l.replace('\r\n', '\n').replace('\r', '\n') for l in actual_lines]
    assert actual_lines == filtered_lines, (
        f"The lines in {AUTH_FAILURE_LOG} are not copied verbatim from {APP_LOG}.\n"
        f"Expected (from app.log):\n{''.join(filtered_lines)}\n"
        f"Actual:\n{''.join(actual_lines)}"
    )

def test_auth_summary_exists():
    assert os.path.isfile(AUTH_SUMMARY), (
        f"Expected {AUTH_SUMMARY} to exist after task completion, but it does not."
    )

def test_auth_summary_content_exact():
    assert os.path.isfile(AUTH_SUMMARY), (
        f"{AUTH_SUMMARY} does not exist."
    )
    with open(AUTH_SUMMARY, "r", encoding="utf-8") as f:
        summary_content = f.read()
    # Normalize line endings to \n for comparison
    summary_content = summary_content.replace('\r\n', '\n').replace('\r', '\n')
    assert summary_content == EXPECTED_SUMMARY_LINE, (
        f"{AUTH_SUMMARY} must contain exactly one line: {EXPECTED_SUMMARY_LINE!r}\n"
        f"Actual content: {summary_content!r}\n"
        f"Do not include extra lines, spaces, or text."
    )

def test_auth_summary_count_matches_failure_log():
    with open(AUTH_SUMMARY, "r", encoding="utf-8") as f:
        line = f.readline()
    # Try to extract the count from the summary line
    prefix = "Total failures: "
    assert line.startswith(prefix), (
        f"{AUTH_SUMMARY} must start with '{prefix}', but got: {line!r}"
    )
    count_str = line[len(prefix):].strip()
    try:
        count = int(count_str)
    except ValueError:
        pytest.fail(
            f"The summary count in {AUTH_SUMMARY} is not a valid integer: {count_str!r}"
        )
    failure_lines = read_file_lines(AUTH_FAILURE_LOG)
    assert count == len(failure_lines), (
        f"The count in {AUTH_SUMMARY} is {count}, but {AUTH_FAILURE_LOG} contains {len(failure_lines)} lines.\n"
        f"These counts must match exactly."
    )

def test_auth_summary_is_single_line():
    with open(AUTH_SUMMARY, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Normalize line endings
    lines = [l.replace('\r\n', '\n').replace('\r', '\n') for l in lines]
    assert len(lines) == 1, (
        f"{AUTH_SUMMARY} must contain exactly one line. Found {len(lines)} lines."
    )