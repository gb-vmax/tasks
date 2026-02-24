# test_final_state.py

import os
import pytest
import re
from datetime import datetime

UPTIME_AUDIT_DIR = "/home/user/uptime_audit"
SSH_STATUS_LOG = "/home/user/uptime_audit/ssh_status.log"

TIMESTAMP_LINE_REGEX = r"^Timestamp: (\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$"
STATUS_LINE_RUNNING = "sshd status: running"
STATUS_LINE_NOT_RUNNING = "sshd status: not running"

@pytest.fixture(scope="module")
def log_lines():
    """Read the ssh_status.log lines, stripping line endings."""
    if not os.path.exists(SSH_STATUS_LOG):
        pytest.fail(f"Log file '{SSH_STATUS_LOG}' does not exist after task completion.")
    with open(SSH_STATUS_LOG, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n\r") for line in f.readlines()]
    return lines

def test_uptime_audit_dir_exists():
    """The /home/user/uptime_audit directory must exist after the task is completed."""
    assert os.path.isdir(UPTIME_AUDIT_DIR), (
        f"Directory '{UPTIME_AUDIT_DIR}' does not exist after the task is completed."
    )

def test_ssh_status_log_exists():
    """The /home/user/uptime_audit/ssh_status.log file must exist after the task is completed."""
    assert os.path.isfile(SSH_STATUS_LOG), (
        f"Log file '{SSH_STATUS_LOG}' does not exist after the task is completed."
    )

def test_ssh_status_log_format_and_content(log_lines):
    """
    The log file must:
      - Be exactly two lines, no blank lines.
      - First line: Timestamp in form 'Timestamp: YYYY-MM-DD HH:MM:SS'
      - Second line: 'sshd status: running' OR 'sshd status: not running'
    """
    assert len(log_lines) == 2, (
        f"Log file '{SSH_STATUS_LOG}' must have exactly 2 lines, but has {len(log_lines)}."
    )

    # Check timestamp line format
    ts_line = log_lines[0]
    m = re.match(TIMESTAMP_LINE_REGEX, ts_line)
    assert m, (
        f"First line of '{SSH_STATUS_LOG}' must be in the form 'Timestamp: YYYY-MM-DD HH:MM:SS'. "
        f"Got: '{ts_line}'"
    )
    try:
        # Parse to datetime to check for validity
        timestamp = datetime.strptime(ts_line[len("Timestamp: "):], "%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        pytest.fail(
            f"First line of '{SSH_STATUS_LOG}' does not contain a valid timestamp: {e}"
        )

    # Check status line
    status_line = log_lines[1]
    assert status_line in (STATUS_LINE_RUNNING, STATUS_LINE_NOT_RUNNING), (
        f"Second line of '{SSH_STATUS_LOG}' must be either '{STATUS_LINE_RUNNING}' or '{STATUS_LINE_NOT_RUNNING}'. "
        f"Got: '{status_line}'"
    )

def test_ssh_status_log_status_matches_system(log_lines):
    """
    The status in the log file must match the actual current status of sshd process.
    """
    # Determine actual status of sshd (running or not)
    sshd_running = False
    try:
        with os.popen("ps -eo comm") as psout:
            for line in psout:
                if line.strip() == "sshd":
                    sshd_running = True
                    break
    except Exception as e:
        pytest.fail(f"Failed to check sshd status: {e}")

    expected_status_line = STATUS_LINE_RUNNING if sshd_running else STATUS_LINE_NOT_RUNNING
    actual_status_line = log_lines[1]
    assert actual_status_line == expected_status_line, (
        f"Second line of '{SSH_STATUS_LOG}' does not match actual sshd status.\n"
        f"Expected: '{expected_status_line}'\n"
        f"Found:    '{actual_status_line}'"
    )

def test_ssh_status_log_no_blank_lines(log_lines):
    """There must be no blank lines in the log file."""
    for idx, line in enumerate(log_lines):
        assert line.strip() != "", (
            f"Line {idx+1} of '{SSH_STATUS_LOG}' is blank; there should be no blank lines."
        )