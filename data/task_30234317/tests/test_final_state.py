# test_final_state.py

import os
import pytest

AUDIT_REPORT_PATH = "/home/user/cron_audit_report.txt"

# The exact, required content for the audit report (including line breaks and spacing)
EXPECTED_REPORT = (
    "==== CRON JOBS FOR USER: alice ====\n"
    "TIMING: 0 5 * * 1\n"
    "COMMAND: /home/alice/backup.sh\n"
    "TIMING: 15 14 1 * *\n"
    "COMMAND: /usr/bin/python3 /home/alice/scripts/cleanup.py\n"
    "==== CRON JOBS FOR USER: bob ====\n"
    "TIMING: */10 * * * *\n"
    "COMMAND: /home/bob/report.sh\n"
)


def test_audit_report_file_exists():
    """
    The audit report file must exist at the specified absolute path after task completion.
    """
    assert os.path.isfile(AUDIT_REPORT_PATH), (
        f"Expected audit report file at {AUDIT_REPORT_PATH}, but it does not exist. "
        "You must create this file after processing the user crontabs."
    )


def test_audit_report_file_content_exact():
    """
    The audit report file must have exactly the required content, with correct order,
    formatting, spacing, and line breaks. Any deviation is a failure.
    """
    if not os.path.isfile(AUDIT_REPORT_PATH):
        pytest.skip(f"Audit report file {AUDIT_REPORT_PATH} does not exist (skipped content check).")
    with open(AUDIT_REPORT_PATH, "r", encoding="utf-8") as f:
        actual = f.read()
    if actual != EXPECTED_REPORT:
        # Find the first difference for a helpful message
        import difflib
        diff = "\n".join(difflib.unified_diff(
            EXPECTED_REPORT.splitlines(),
            actual.splitlines(),
            fromfile="expected",
            tofile="found",
            lineterm=""
        ))
        pytest.fail(
            f"Audit report content does not match the required output format, order, or content.\n"
            f"Difference:\n{diff}\n\n"
            f"Expected:\n{EXPECTED_REPORT!r}\nFound:\n{actual!r}"
        )


def test_audit_report_file_permissions():
    """
    The audit report file should be readable by the owner. (Mode 600 or 644 are both acceptable.)
    """
    st = os.stat(AUDIT_REPORT_PATH)
    mode = st.st_mode & 0o777
    assert mode in (0o600, 0o644), (
        f"Audit report file {AUDIT_REPORT_PATH} should have mode 600 or 644, but has {oct(mode)}."
    )


def test_no_extra_audit_report_files():
    """
    There should be no extra audit report files in /home/user (only cron_audit_report.txt).
    """
    user_home = os.path.dirname(AUDIT_REPORT_PATH)
    files = [f for f in os.listdir(user_home) if os.path.isfile(os.path.join(user_home, f))]
    extras = [f for f in files if f.startswith("cron_audit_report") and f != "cron_audit_report.txt"]
    assert not extras, (
        f"Found unexpected extra audit report files in {user_home}: {', '.join(extras)}. "
        "Only cron_audit_report.txt should exist."
    )