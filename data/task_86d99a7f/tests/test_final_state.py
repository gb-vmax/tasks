# test_final_state.py

import os
import pytest

SECURITY_DIR = "/home/user/security"
ACCESS_LOG = "/home/user/security/access.log"
OLD_CREDENTIALS_LOG = "/home/user/security/old-credentials.log"
SUMMARY_TXT = "/home/user/security/old-credentials-summary.txt"

# The expected filtered log content (must match exactly, including order and newlines)
EXPECTED_OLD_CREDENTIALS_LOG = (
    "2024-06-05 12:21:11 - user:alice - action:login - status:success - ip:192.168.1.15\n"
    "2024-06-05 12:22:18 - user:bob - action:failed - status:invalid_password - ip:192.168.1.33\n"
    "2024-06-05 12:26:00 - user:alice - action:token_refresh - status:success - ip:192.168.1.15\n"
    "2024-06-05 12:28:01 - user:bob - action:login - status:success - ip:192.168.1.33\n"
    "2024-06-05 12:28:17 - user:alice - action:failed - status:invalid_password - ip:192.168.1.15\n"
    "2024-06-05 12:30:11 - user:alice - action:login - status:success - ip:192.168.1.15\n"
)

EXPECTED_SUMMARY_TXT = "Old credential entries: 6\n"

@pytest.mark.parametrize("path", [OLD_CREDENTIALS_LOG, SUMMARY_TXT])
def test_output_files_exist(path):
    assert os.path.isfile(path), (
        f"Expected file '{path}' does not exist. "
        f"Did you forget to create or write to it?"
    )
    # Check readable and writable
    if not os.access(path, os.R_OK):
        raise AssertionError(f"File '{path}' exists but is not readable by the user.")
    if not os.access(path, os.W_OK):
        raise AssertionError(f"File '{path}' exists but is not writable by the user.")

def test_old_credentials_log_content_exact():
    """Check that old-credentials.log exists and matches the expected content exactly."""
    assert os.path.isfile(OLD_CREDENTIALS_LOG), (
        f"Filtered log file '{OLD_CREDENTIALS_LOG}' does not exist."
    )
    with open(OLD_CREDENTIALS_LOG, "r", encoding="utf-8") as f:
        content = f.read()
    # Normalize line endings for comparison
    content_norm = content.replace('\r\n', '\n')
    expected_norm = EXPECTED_OLD_CREDENTIALS_LOG.replace('\r\n', '\n')
    assert content_norm == expected_norm, (
        f"File '{OLD_CREDENTIALS_LOG}' does not match the expected filtered log entries.\n"
        f"--- Expected ---\n{expected_norm}\n"
        f"--- Found ---\n{content_norm}"
    )
    # Check for trailing blank lines
    with open(OLD_CREDENTIALS_LOG, "rb") as fbin:
        raw = fbin.read()
    if raw.endswith(b"\n\n"):
        raise AssertionError(
            f"File '{OLD_CREDENTIALS_LOG}' contains extra blank lines at the end."
        )

def test_old_credentials_log_no_extra_lines():
    """Ensure there are exactly 6 non-blank lines and no extra content."""
    with open(OLD_CREDENTIALS_LOG, "r", encoding="utf-8") as f:
        lines = f.readlines()
    nonblank = [line for line in lines if line.strip()]
    assert len(nonblank) == 6, (
        f"File '{OLD_CREDENTIALS_LOG}' should contain exactly 6 non-blank lines, found {len(nonblank)}."
    )
    # Each line must match one of the expected lines (order matters)
    expected_lines = EXPECTED_OLD_CREDENTIALS_LOG.strip('\n').split('\n')
    file_lines = [line.rstrip('\n') for line in lines]
    assert file_lines == expected_lines, (
        f"File '{OLD_CREDENTIALS_LOG}' lines do not match expected lines.\n"
        f"--- Expected ---\n{expected_lines}\n"
        f"--- Found ---\n{file_lines}"
    )

def test_summary_txt_content_exact():
    """Check that summary file exists and contains the precise summary."""
    assert os.path.isfile(SUMMARY_TXT), (
        f"Summary file '{SUMMARY_TXT}' does not exist."
    )
    with open(SUMMARY_TXT, "r", encoding="utf-8") as f:
        content = f.read()
    # Normalize line endings
    content_norm = content.replace('\r\n', '\n')
    expected_norm = EXPECTED_SUMMARY_TXT.replace('\r\n', '\n')
    assert content_norm == expected_norm, (
        f"File '{SUMMARY_TXT}' does not match the expected summary content.\n"
        f"--- Expected ---\n{expected_norm}\n"
        f"--- Found ---\n{content_norm}"
    )
    # Should be exactly one line, no extra blank lines or spaces
    lines = content.splitlines()
    assert len(lines) == 1, (
        f"File '{SUMMARY_TXT}' should contain exactly one line, found {len(lines)} lines."
    )
    assert lines[0] == "Old credential entries: 6", (
        f"Summary line in '{SUMMARY_TXT}' is incorrect. "
        f"Expected 'Old credential entries: 6', found: '{lines[0]}'"
    )

def test_access_log_untouched():
    """Verify the original access.log is unchanged."""
    expected_access_log = (
        "2024-06-05 12:21:11 - user:alice - action:login - status:success - ip:192.168.1.15\n"
        "2024-06-05 12:22:18 - user:bob - action:failed - status:invalid_password - ip:192.168.1.33\n"
        "2024-06-05 12:25:41 - user:charlie - action:login - status:success - ip:10.0.0.5\n"
        "2024-06-05 12:26:00 - user:alice - action:token_refresh - status:success - ip:192.168.1.15\n"
        "2024-06-05 12:27:14 - user:dave - action:logout - status:success - ip:172.16.0.18\n"
        "2024-06-05 12:28:01 - user:bob - action:login - status:success - ip:192.168.1.33\n"
        "2024-06-05 12:28:17 - user:alice - action:failed - status:invalid_password - ip:192.168.1.15\n"
        "2024-06-05 12:29:05 - user:charlie - action:token_refresh - status:success - ip:10.0.0.5\n"
        "2024-06-05 12:30:11 - user:alice - action:login - status:success - ip:192.168.1.15\n"
    )
    assert os.path.isfile(ACCESS_LOG), (
        f"Original log file '{ACCESS_LOG}' does not exist."
    )
    with open(ACCESS_LOG, "r", encoding="utf-8") as f:
        content = f.read()
    # Normalize line endings
    content_norm = content.replace('\r\n', '\n')
    expected_norm = expected_access_log.replace('\r\n', '\n')
    assert content_norm == expected_norm, (
        f"File '{ACCESS_LOG}' was modified during the task. It must remain unchanged.\n"
        f"--- Expected ---\n{expected_norm}\n"
        f"--- Found ---\n{content_norm}"
    )

def test_no_extra_files_created():
    """Ensure no extra files exist in the security directory."""
    allowed = {
        "access.log",
        "old-credentials.log",
        "old-credentials-summary.txt",
    }
    files = set(os.listdir(SECURITY_DIR))
    extras = files - allowed
    assert not extras, (
        f"Unexpected files found in '{SECURITY_DIR}': {sorted(extras)}. "
        f"Only these should exist: {sorted(allowed)}"
    )