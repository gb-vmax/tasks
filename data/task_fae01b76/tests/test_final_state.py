# test_final_state.py

import pytest
import os


AUDIT_FILE = "/home/user/audit/user_accounts.txt"
AUDIT_DIR = "/home/user/audit"

EXPECTED_LINES = [
    "=== USER ACCOUNT AUDIT REPORT ===",
    "Generated from: /etc/passwd",
    "",
    "Non-system accounts (UID >= 1000):",
    "  user | UID: 1000 | Home: /home/user | Shell: /bin/bash",
    "  alice | UID: 1001 | Home: /home/alice | Shell: /bin/bash",
    "  bob | UID: 1002 | Home: /home/bob | Shell: /bin/sh",
    "  charlie | UID: 1500 | Home: /home/charlie | Shell: /usr/sbin/nologin",
    "",
    "Total non-system accounts: 4",
]


def test_audit_directory_exists():
    """The /home/user/audit/ directory must have been created by the agent."""
    assert os.path.isdir(AUDIT_DIR), (
        f"Directory '{AUDIT_DIR}' does not exist. "
        "The agent must create this directory as part of the task."
    )


def test_audit_file_exists():
    """The audit report file must exist at /home/user/audit/user_accounts.txt."""
    assert os.path.isfile(AUDIT_FILE), (
        f"Audit report file '{AUDIT_FILE}' does not exist. "
        "The agent must create this file as part of the task."
    )


def test_audit_file_is_readable():
    """The audit report file must be readable."""
    assert os.access(AUDIT_FILE, os.R_OK), (
        f"Audit report file '{AUDIT_FILE}' exists but is not readable."
    )


@pytest.fixture
def audit_lines():
    """Read the audit file and return its lines (without trailing newline on last line)."""
    with open(AUDIT_FILE, "r") as f:
        content = f.read()
    # Split into lines; preserve empty lines
    lines = content.splitlines()
    return lines


def test_audit_file_has_trailing_newline():
    """The audit file must end with a trailing newline."""
    with open(AUDIT_FILE, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"'{AUDIT_FILE}' does not end with a trailing newline. "
        "The file must have a newline after the last line."
    )


def test_audit_file_line_count(audit_lines):
    """The audit file must have exactly 10 lines."""
    assert len(audit_lines) == 10, (
        f"Expected exactly 10 lines in '{AUDIT_FILE}', but got {len(audit_lines)}.\n"
        f"Actual lines:\n" + "\n".join(f"  [{i+1}]: {repr(line)}" for i, line in enumerate(audit_lines))
    )


def test_line_1_header(audit_lines):
    """Line 1 must be the report header."""
    expected = "=== USER ACCOUNT AUDIT REPORT ==="
    actual = audit_lines[0] if len(audit_lines) >= 1 else None
    assert actual == expected, (
        f"Line 1 is wrong.\n"
        f"  Expected: {repr(expected)}\n"
        f"  Got:      {repr(actual)}"
    )


def test_line_2_source(audit_lines):
    """Line 2 must indicate the source file."""
    expected = "Generated from: /etc/passwd"
    actual = audit_lines[1] if len(audit_lines) >= 2 else None
    assert actual == expected, (
        f"Line 2 is wrong.\n"
        f"  Expected: {repr(expected)}\n"
        f"  Got:      {repr(actual)}"
    )


def test_line_3_blank(audit_lines):
    """Line 3 must be an empty line."""
    expected = ""
    actual = audit_lines[2] if len(audit_lines) >= 3 else None
    assert actual == expected, (
        f"Line 3 must be blank.\n"
        f"  Expected: {repr(expected)}\n"
        f"  Got:      {repr(actual)}"
    )


def test_line_4_section_header(audit_lines):
    """Line 4 must be the section header for non-system accounts."""
    expected = "Non-system accounts (UID >= 1000):"
    actual = audit_lines[3] if len(audit_lines) >= 4 else None
    assert actual == expected, (
        f"Line 4 is wrong.\n"
        f"  Expected: {repr(expected)}\n"
        f"  Got:      {repr(actual)}"
    )


def test_line_5_user_entry(audit_lines):
    """Line 5 must be the 'user' account entry (UID 1000)."""
    expected = "  user | UID: 1000 | Home: /home/user | Shell: /bin/bash"
    actual = audit_lines[4] if len(audit_lines) >= 5 else None
    assert actual == expected, (
        f"Line 5 (user entry) is wrong.\n"
        f"  Expected: {repr(expected)}\n"
        f"  Got:      {repr(actual)}\n"
        "Check: 2-space indent, correct UID/home/shell, ' | ' separators."
    )


def test_line_6_alice_entry(audit_lines):
    """Line 6 must be the 'alice' account entry (UID 1001)."""
    expected = "  alice | UID: 1001 | Home: /home/alice | Shell: /bin/bash"
    actual = audit_lines[5] if len(audit_lines) >= 6 else None
    assert actual == expected, (
        f"Line 6 (alice entry) is wrong.\n"
        f"  Expected: {repr(expected)}\n"
        f"  Got:      {repr(actual)}\n"
        "Check: 2-space indent, correct UID/home/shell, ' | ' separators."
    )


def test_line_7_bob_entry(audit_lines):
    """Line 7 must be the 'bob' account entry (UID 1002)."""
    expected = "  bob | UID: 1002 | Home: /home/bob | Shell: /bin/sh"
    actual = audit_lines[6] if len(audit_lines) >= 7 else None
    assert actual == expected, (
        f"Line 7 (bob entry) is wrong.\n"
        f"  Expected: {repr(expected)}\n"
        f"  Got:      {repr(actual)}\n"
        "Check: 2-space indent, correct UID/home/shell, ' | ' separators."
    )


def test_line_8_charlie_entry(audit_lines):
    """Line 8 must be the 'charlie' account entry (UID 1500)."""
    expected = "  charlie | UID: 1500 | Home: /home/charlie | Shell: /usr/sbin/nologin"
    actual = audit_lines[7] if len(audit_lines) >= 8 else None
    assert actual == expected, (
        f"Line 8 (charlie entry) is wrong.\n"
        f"  Expected: {repr(expected)}\n"
        f"  Got:      {repr(actual)}\n"
        "Check: 2-space indent, correct UID/home/shell, ' | ' separators."
    )


def test_line_9_blank(audit_lines):
    """Line 9 must be an empty line (before the total)."""
    expected = ""
    actual = audit_lines[8] if len(audit_lines) >= 9 else None
    assert actual == expected, (
        f"Line 9 must be blank.\n"
        f"  Expected: {repr(expected)}\n"
        f"  Got:      {repr(actual)}"
    )


def test_line_10_total(audit_lines):
    """Line 10 must show the total count of non-system accounts."""
    expected = "Total non-system accounts: 4"
    actual = audit_lines[9] if len(audit_lines) >= 10 else None
    assert actual == expected, (
        f"Line 10 (total line) is wrong.\n"
        f"  Expected: {repr(expected)}\n"
        f"  Got:      {repr(actual)}\n"
        "There should be exactly 4 non-system accounts (user, alice, bob, charlie)."
    )


def test_full_file_content(audit_lines):
    """The entire file content must match the expected report exactly."""
    assert audit_lines == EXPECTED_LINES, (
        f"Full file content does not match expected.\n"
        f"Expected lines:\n" +
        "\n".join(f"  [{i+1}]: {repr(line)}" for i, line in enumerate(EXPECTED_LINES)) +
        f"\n\nActual lines:\n" +
        "\n".join(f"  [{i+1}]: {repr(line)}" for i, line in enumerate(audit_lines))
    )


def test_no_nobody_account_in_report(audit_lines):
    """The 'nobody' account (UID 65534) must not appear in the report."""
    for i, line in enumerate(audit_lines, 1):
        assert "nobody" not in line, (
            f"Line {i} contains 'nobody', which should be excluded from the report.\n"
            f"  Line content: {repr(line)}"
        )


def test_no_system_accounts_in_report(audit_lines):
    """No system accounts (UID < 1000) should appear in the report entries."""
    # Parse /etc/passwd to get system account names
    system_usernames = set()
    with open("/etc/passwd", "r") as f:
        for line in f:
            parts = line.strip().split(":")
            if len(parts) >= 3:
                try:
                    uid = int(parts[2])
                    if uid < 1000:
                        system_usernames.add(parts[0])
                except ValueError:
                    pass

    # Check that none of the account entry lines (lines 5-8, index 4-7) contain system usernames
    entry_lines = audit_lines[4:8] if len(audit_lines) >= 8 else audit_lines[4:]
    for entry_line in entry_lines:
        # Extract username (first field before ' | ')
        if " | " in entry_line:
            username = entry_line.strip().split(" | ")[0]
            assert username not in system_usernames, (
                f"System account '{username}' (UID < 1000) found in report entries. "
                "Only non-system accounts (UID >= 1000) should be listed."
            )


def test_entries_sorted_by_uid(audit_lines):
    """Account entries must be sorted in ascending order by UID."""
    entry_lines = audit_lines[4:8] if len(audit_lines) >= 8 else audit_lines[4:]
    uids = []
    for line in entry_lines:
        # Parse UID from format: "  username | UID: <uid> | ..."
        if "UID: " in line:
            try:
                uid_part = line.split("UID: ")[1].split(" |")[0].strip()
                uids.append(int(uid_part))
            except (IndexError, ValueError):
                pass

    assert uids == sorted(uids), (
        f"Account entries are not sorted by UID in ascending order.\n"
        f"UIDs found: {uids}\n"
        f"Expected order: {sorted(uids)}"
    )


def test_entry_indentation(audit_lines):
    """Each account entry line must be indented with exactly two spaces."""
    entry_lines = audit_lines[4:8] if len(audit_lines) >= 8 else audit_lines[4:]
    for i, line in enumerate(entry_lines, 5):
        assert line.startswith("  "), (
            f"Line {i} does not start with exactly two spaces.\n"
            f"  Line content: {repr(line)}"
        )
        assert not line.startswith("   "), (
            f"Line {i} starts with more than two spaces (over-indented).\n"
            f"  Line content: {repr(line)}"
        )


def test_entry_separator_format(audit_lines):
    """Each account entry must use ' | ' (space-pipe-space) as field separator."""
    entry_lines = audit_lines[4:8] if len(audit_lines) >= 8 else audit_lines[4:]
    for i, line in enumerate(entry_lines, 5):
        assert " | " in line, (
            f"Line {i} does not contain ' | ' separator.\n"
            f"  Line content: {repr(line)}\n"
            "Fields must be separated by ' | ' (space, pipe, space)."
        )
        # Each entry should have exactly 3 separators (4 fields)
        parts = line.strip().split(" | ")
        assert len(parts) == 4, (
            f"Line {i} does not have exactly 4 fields separated by ' | '.\n"
            f"  Line content: {repr(line)}\n"
            f"  Fields found: {parts}"
        )