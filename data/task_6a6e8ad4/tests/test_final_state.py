# test_final_state.py

import os
import stat
import pytest

SCRIPT_PATH = "/home/user/admin/gen_report.sh"
REPORT_PATH = "/home/user/admin/report.txt"
CSV_PATH = "/home/user/admin/users.csv"

EXPECTED_REPORT = """\
=== USER ACCOUNT REPORT ===
Total users: 10
Active: 6
Inactive: 4

Active admins:
  alice (alice@example.com)
  frank (frank@example.com)

Active editors:
  eve (eve@example.com)
  heidi (heidi@example.com)"""


def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), (
        f"Script '{SCRIPT_PATH}' does not exist. "
        "The student must create the gen_report.sh script."
    )


def test_script_is_executable():
    st = os.stat(SCRIPT_PATH)
    is_executable = bool(st.st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
    assert is_executable, (
        f"Script '{SCRIPT_PATH}' is not executable. "
        "Run 'chmod +x /home/user/admin/gen_report.sh' to fix this."
    )


def test_script_is_readable():
    assert os.access(SCRIPT_PATH, os.R_OK), (
        f"Script '{SCRIPT_PATH}' is not readable."
    )


def test_report_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report '{REPORT_PATH}' does not exist. "
        "The student must run the gen_report.sh script to produce report.txt."
    )


def test_report_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report '{REPORT_PATH}' is not readable."
    )


def test_report_exact_content():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    # Strip trailing newline for comparison but allow it
    content_stripped = content.rstrip("\n")
    assert content_stripped == EXPECTED_REPORT, (
        f"Report '{REPORT_PATH}' does not have the expected content.\n\n"
        f"Expected:\n{EXPECTED_REPORT}\n\n"
        f"Got:\n{content_stripped}"
    )


def test_report_header_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 1, f"Report '{REPORT_PATH}' is empty."
    first_line = lines[0].rstrip("\n")
    assert first_line == "=== USER ACCOUNT REPORT ===", (
        f"First line of report is incorrect.\n"
        f"Expected: '=== USER ACCOUNT REPORT ==='\n"
        f"Got:      '{first_line}'"
    )


def test_report_total_users():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    total_line = None
    for line in lines:
        if line.startswith("Total users:"):
            total_line = line.rstrip("\n")
            break
    assert total_line is not None, (
        f"Report '{REPORT_PATH}' does not contain a 'Total users:' line."
    )
    assert total_line == "Total users: 10", (
        f"'Total users' line is incorrect.\n"
        f"Expected: 'Total users: 10'\n"
        f"Got:      '{total_line}'"
    )


def test_report_active_count():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    active_line = None
    for line in lines:
        stripped = line.rstrip("\n")
        if stripped.startswith("Active:"):
            active_line = stripped
            break
    assert active_line is not None, (
        f"Report '{REPORT_PATH}' does not contain an 'Active:' line."
    )
    assert active_line == "Active: 6", (
        f"'Active' count line is incorrect.\n"
        f"Expected: 'Active: 6'\n"
        f"Got:      '{active_line}'"
    )


def test_report_inactive_count():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    inactive_line = None
    for line in lines:
        stripped = line.rstrip("\n")
        if stripped.startswith("Inactive:"):
            inactive_line = stripped
            break
    assert inactive_line is not None, (
        f"Report '{REPORT_PATH}' does not contain an 'Inactive:' line."
    )
    assert inactive_line == "Inactive: 4", (
        f"'Inactive' count line is incorrect.\n"
        f"Expected: 'Inactive: 4'\n"
        f"Got:      '{inactive_line}'"
    )


def test_report_active_admins_section_header():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert "Active admins:" in content, (
        f"Report '{REPORT_PATH}' does not contain 'Active admins:' section header."
    )


def test_report_active_editors_section_header():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert "Active editors:" in content, (
        f"Report '{REPORT_PATH}' does not contain 'Active editors:' section header."
    )


def test_report_no_viewers_section():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert "Active viewers:" not in content, (
        f"Report '{REPORT_PATH}' should NOT contain an 'Active viewers:' section."
    )


def test_report_active_admins_entries():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    # Find the "Active admins:" section and collect entries
    in_section = False
    entries = []
    for line in lines:
        stripped = line.rstrip("\n")
        if stripped == "Active admins:":
            in_section = True
            continue
        if in_section:
            if stripped.startswith("  "):
                entries.append(stripped)
            else:
                break

    assert entries == [
        "  alice (alice@example.com)",
        "  frank (frank@example.com)",
    ], (
        f"Active admins entries are incorrect.\n"
        f"Expected:\n  alice (alice@example.com)\n  frank (frank@example.com)\n"
        f"Got:\n" + "\n".join(entries)
    )


def test_report_active_editors_entries():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    # Find the "Active editors:" section and collect entries
    in_section = False
    entries = []
    for line in lines:
        stripped = line.rstrip("\n")
        if stripped == "Active editors:":
            in_section = True
            continue
        if in_section:
            if stripped.startswith("  "):
                entries.append(stripped)
            else:
                break

    assert entries == [
        "  eve (eve@example.com)",
        "  heidi (heidi@example.com)",
    ], (
        f"Active editors entries are incorrect.\n"
        f"Expected:\n  eve (eve@example.com)\n  heidi (heidi@example.com)\n"
        f"Got:\n" + "\n".join(entries)
    )


def test_report_admins_sorted_alphabetically():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    in_section = False
    usernames = []
    for line in lines:
        stripped = line.rstrip("\n")
        if stripped == "Active admins:":
            in_section = True
            continue
        if in_section:
            if stripped.startswith("  "):
                # Extract username from "  username (email)"
                username = stripped.strip().split(" ")[0]
                usernames.append(username)
            else:
                break

    assert usernames == sorted(usernames), (
        f"Active admins are not sorted alphabetically.\n"
        f"Got: {usernames}\n"
        f"Expected sorted: {sorted(usernames)}"
    )


def test_report_editors_sorted_alphabetically():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    in_section = False
    usernames = []
    for line in lines:
        stripped = line.rstrip("\n")
        if stripped == "Active editors:":
            in_section = True
            continue
        if in_section:
            if stripped.startswith("  "):
                username = stripped.strip().split(" ")[0]
                usernames.append(username)
            else:
                break

    assert usernames == sorted(usernames), (
        f"Active editors are not sorted alphabetically.\n"
        f"Got: {usernames}\n"
        f"Expected sorted: {sorted(usernames)}"
    )


def test_report_blank_line_before_active_admins():
    """There should be a blank line between the counts and 'Active admins:' section."""
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    admins_idx = None
    for i, line in enumerate(lines):
        if line == "Active admins:":
            admins_idx = i
            break

    assert admins_idx is not None, (
        f"'Active admins:' section not found in report."
    )
    assert admins_idx > 0 and lines[admins_idx - 1] == "", (
        f"Expected a blank line before 'Active admins:' section.\n"
        f"Line before 'Active admins:' is: '{lines[admins_idx - 1]}'"
    )


def test_report_blank_line_between_sections():
    """There should be a blank line between 'Active admins:' entries and 'Active editors:'."""
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    editors_idx = None
    for i, line in enumerate(lines):
        if line == "Active editors:":
            editors_idx = i
            break

    assert editors_idx is not None, (
        f"'Active editors:' section not found in report."
    )
    assert editors_idx > 0 and lines[editors_idx - 1] == "", (
        f"Expected a blank line before 'Active editors:' section.\n"
        f"Line before 'Active editors:' is: '{lines[editors_idx - 1]}'"
    )


def test_csv_file_unchanged():
    """The original CSV file should remain unchanged after running the script."""
    expected_csv = (
        "username,email,role,status\n"
        "alice,alice@example.com,admin,active\n"
        "bob,bob@example.com,editor,inactive\n"
        "carol,carol@example.com,viewer,active\n"
        "dave,dave@example.com,admin,inactive\n"
        "eve,eve@example.com,editor,active\n"
        "frank,frank@example.com,admin,active\n"
        "grace,grace@example.com,viewer,inactive\n"
        "heidi,heidi@example.com,editor,active\n"
        "ivan,ivan@example.com,viewer,active\n"
        "judy,judy@example.com,admin,inactive"
    )
    with open(CSV_PATH, "r") as f:
        content = f.read().strip()
    assert content == expected_csv.strip(), (
        f"CSV file '{CSV_PATH}' has been modified.\n"
        f"Expected:\n{expected_csv.strip()}\n\n"
        f"Got:\n{content}"
    )