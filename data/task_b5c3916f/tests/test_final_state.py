# test_final_state.py

import os
import pytest

AUDIT_LOG_PATH = "/home/user/output/audit_user_access.log"

EXPECTED_AUDIT_LOG_CONTENT = """[SSH]
alice
felix
[FTP]
carol
[HTTP]
bob
"""

def test_audit_log_exists():
    assert os.path.isfile(AUDIT_LOG_PATH), (
        f"Required audit log file is missing: {AUDIT_LOG_PATH}"
    )

def test_audit_log_content_exact():
    """
    Ensure the audit log has the exact required content (format, order, and users).
    """
    assert os.path.isfile(AUDIT_LOG_PATH), (
        f"Required audit log file is missing: {AUDIT_LOG_PATH}"
    )
    with open(AUDIT_LOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    # Normalize line endings for robust comparison
    actual = content.replace('\r\n', '\n').strip()
    expected = EXPECTED_AUDIT_LOG_CONTENT.strip()
    assert actual == expected, (
        f"{AUDIT_LOG_PATH} does not match the required audit log format and content.\n"
        f"--- Expected content ---\n{expected}\n"
        f"--- Actual content ---\n{actual}\n"
        "Check for:\n"
        "- Correct section headers ([SSH], [FTP], [HTTP]) in order\n"
        "- Each allowed user listed under their service, lexicographically sorted\n"
        "- No extra or missing lines, blank lines, or users\n"
        "- Exact format as shown above"
    )