# test_final_state.py
"""
Pytest suite to validate the FINAL state after extracting permission change lines
from /home/user/logs/auth_sample.log into /home/user/logs/perm_audit.log.

Checks:
- /home/user/logs/perm_audit.log exists.
- It contains ONLY the lines from auth_sample.log that include 'chmod' or 'chown' (case-sensitive, exact match).
- The order and spacing of lines are preserved.
- No extra or missing lines.

Fails with clear messages if the state is not as expected.
"""

import os
import pytest

AUTH_SAMPLE_LOG = "/home/user/logs/auth_sample.log"
PERM_AUDIT_LOG = "/home/user/logs/perm_audit.log"

# "Truth" contents for validation
TRUTH_AUTH_SAMPLE = [
    "Jun 15 10:05:13 server1 sshd[531]: Accepted password for admin from 192.168.56.21 port 62420 ssh2\n",
    "Jun 15 10:05:15 server1 chmod: mode of '/var/tmp/testfile.log' changed from 0644 to 0600\n",
    "Jun 15 10:05:16 server1 su[540]: Successful su for root by admin\n",
    "Jun 15 10:05:19 server1 chown: changing ownership of '/srv/www/html/index.html' from root to webuser\n",
    "Jun 15 10:05:25 server1 sshd[531]: Session closed for admin\n",
    "Jun 15 10:05:30 server1 passwd[550]: password for user 'bob' changed by admin\n"
]

TRUTH_PERM_AUDIT = [
    "Jun 15 10:05:15 server1 chmod: mode of '/var/tmp/testfile.log' changed from 0644 to 0600\n",
    "Jun 15 10:05:19 server1 chown: changing ownership of '/srv/www/html/index.html' from root to webuser\n"
]

@pytest.mark.final_state
def test_perm_audit_log_exists():
    assert os.path.isfile(PERM_AUDIT_LOG), (
        f"Expected '{PERM_AUDIT_LOG}' to exist, but it does not. "
        "You must create this file with the filtered results."
    )

@pytest.mark.final_state
def test_perm_audit_log_content_exact():
    try:
        with open(PERM_AUDIT_LOG, "r") as f:
            actual_lines = f.readlines()
    except Exception as e:
        pytest.fail(f"Could not read '{PERM_AUDIT_LOG}': {e}")

    # Check for exact match
    if actual_lines != TRUTH_PERM_AUDIT:
        # Prepare a detailed diff message
        expected = "".join(TRUTH_PERM_AUDIT)
        actual = "".join(actual_lines)
        pytest.fail(
            f"'{PERM_AUDIT_LOG}' does not have the exact expected content.\n"
            "Expected lines:\n"
            f"{expected}\n"
            "Actual lines:\n"
            f"{actual}\n"
            "Ensure ONLY lines containing the full word 'chmod' or 'chown' (case-sensitive) from "
            f"'{AUTH_SAMPLE_LOG}' are present, in order, and with no extra/missing lines."
        )

@pytest.mark.final_state
def test_perm_audit_log_no_extra_lines():
    # This is a redundancy check, but it will explicitly check that only the right lines are included.
    try:
        with open(PERM_AUDIT_LOG, "r") as f:
            lines = f.readlines()
    except Exception as e:
        pytest.fail(f"Could not read '{PERM_AUDIT_LOG}': {e}")

    for idx, line in enumerate(lines):
        if "chmod" not in line and "chown" not in line:
            pytest.fail(
                f"Line {idx+1} in '{PERM_AUDIT_LOG}' does not contain 'chmod' or 'chown':\n"
                f"  {line}"
            )

@pytest.mark.final_state
def test_perm_audit_log_preserves_order_and_spacing():
    # Ensure the lines are in the same order as in the source log.
    try:
        with open(PERM_AUDIT_LOG, "r") as f:
            audit_lines = f.readlines()
        with open(AUTH_SAMPLE_LOG, "r") as f:
            auth_lines = f.readlines()
    except Exception as e:
        pytest.fail(f"Could not read one of the log files: {e}")

    # Get expected filtered lines from the original log
    expected_filtered = [line for line in auth_lines if "chmod" in line or "chown" in line]

    assert audit_lines == expected_filtered, (
        f"The lines in '{PERM_AUDIT_LOG}' do not preserve the original order/spacing "
        f"from '{AUTH_SAMPLE_LOG}'.\n"
        f"Expected filtered lines:\n{''.join(expected_filtered)}"
        f"Actual lines:\n{''.join(audit_lines)}"
    )