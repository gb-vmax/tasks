# test_final_state.py

import os
import pytest

REPORT_FILE = "/home/user/config_report.txt"

EXPECTED_CONTENT = (
    "CONFIG CHANGE REPORT\n"
    "====================\n"
    "Total changes: 15\n"
    "Successful changes: 10\n"
    "Failed changes: 5\n"
    "\n"
    "Changes by user:\n"
    "  alice: 6\n"
    "  bob: 5\n"
    "  carol: 4\n"
    "\n"
    "Changes by component:\n"
    "  database: 4\n"
    "  firewall: 3\n"
    "  network: 4\n"
    "  webserver: 4"
)


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file not found: {REPORT_FILE}. "
        "The student must generate the config report at this path."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_FILE, os.R_OK), (
        f"Report file is not readable: {REPORT_FILE}"
    )


def test_report_exact_content():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()

    assert actual_content == EXPECTED_CONTENT, (
        f"Report file content does not match expected.\n"
        f"Expected:\n{EXPECTED_CONTENT!r}\n\n"
        f"Actual:\n{actual_content!r}"
    )


def test_report_no_trailing_newline():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()

    assert not actual_content.endswith("\n"), (
        f"Report file must not have a trailing newline, but it does.\n"
        f"Last 10 chars: {actual_content[-10:]!r}"
    )


def test_report_header():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 2, (
        f"Report file has fewer than 2 lines; cannot check header."
    )
    assert lines[0] == "CONFIG CHANGE REPORT", (
        f"First line (header title) is wrong.\n"
        f"Expected: 'CONFIG CHANGE REPORT'\n"
        f"Actual:   {lines[0]!r}"
    )
    assert lines[1] == "====================", (
        f"Second line (header separator) is wrong.\n"
        f"Expected: '===================='\n"
        f"Actual:   {lines[1]!r}"
    )


def test_report_total_changes():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    total_line = None
    for line in lines:
        if line.startswith("Total changes:"):
            total_line = line
            break

    assert total_line is not None, (
        "Could not find a line starting with 'Total changes:' in the report."
    )
    assert total_line == "Total changes: 15", (
        f"Total changes line is wrong.\n"
        f"Expected: 'Total changes: 15'\n"
        f"Actual:   {total_line!r}"
    )


def test_report_successful_changes():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    success_line = None
    for line in lines:
        if line.startswith("Successful changes:"):
            success_line = line
            break

    assert success_line is not None, (
        "Could not find a line starting with 'Successful changes:' in the report."
    )
    assert success_line == "Successful changes: 10", (
        f"Successful changes line is wrong.\n"
        f"Expected: 'Successful changes: 10'\n"
        f"Actual:   {success_line!r}"
    )


def test_report_failed_changes():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    failed_line = None
    for line in lines:
        if line.startswith("Failed changes:"):
            failed_line = line
            break

    assert failed_line is not None, (
        "Could not find a line starting with 'Failed changes:' in the report."
    )
    assert failed_line == "Failed changes: 5", (
        f"Failed changes line is wrong.\n"
        f"Expected: 'Failed changes: 5'\n"
        f"Actual:   {failed_line!r}"
    )


def test_report_changes_by_user_section_header():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert "Changes by user:" in lines, (
        "Could not find 'Changes by user:' section header in the report."
    )


def test_report_user_alice():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert "  alice: 6" in lines, (
        f"Expected '  alice: 6' in the report (with exactly two leading spaces).\n"
        f"Lines in report:\n" + "\n".join(repr(l) for l in lines)
    )


def test_report_user_bob():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert "  bob: 5" in lines, (
        f"Expected '  bob: 5' in the report (with exactly two leading spaces).\n"
        f"Lines in report:\n" + "\n".join(repr(l) for l in lines)
    )


def test_report_user_carol():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert "  carol: 4" in lines, (
        f"Expected '  carol: 4' in the report (with exactly two leading spaces).\n"
        f"Lines in report:\n" + "\n".join(repr(l) for l in lines)
    )


def test_report_users_alphabetical_order():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    # Find the "Changes by user:" section and extract user lines
    in_user_section = False
    user_lines = []
    for line in lines:
        if line == "Changes by user:":
            in_user_section = True
            continue
        if in_user_section:
            if line.startswith("  ") and ":" in line:
                user_lines.append(line)
            else:
                break

    assert len(user_lines) == 3, (
        f"Expected 3 user lines in 'Changes by user:' section, got {len(user_lines)}.\n"
        f"User lines found: {user_lines!r}"
    )

    expected_user_lines = ["  alice: 6", "  bob: 5", "  carol: 4"]
    assert user_lines == expected_user_lines, (
        f"User lines are not in alphabetical order or have wrong counts.\n"
        f"Expected: {expected_user_lines!r}\n"
        f"Actual:   {user_lines!r}"
    )


def test_report_changes_by_component_section_header():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert "Changes by component:" in lines, (
        "Could not find 'Changes by component:' section header in the report."
    )


def test_report_component_database():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert "  database: 4" in lines, (
        f"Expected '  database: 4' in the report (with exactly two leading spaces).\n"
        f"Lines in report:\n" + "\n".join(repr(l) for l in lines)
    )


def test_report_component_firewall():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert "  firewall: 3" in lines, (
        f"Expected '  firewall: 3' in the report (with exactly two leading spaces).\n"
        f"Lines in report:\n" + "\n".join(repr(l) for l in lines)
    )


def test_report_component_network():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert "  network: 4" in lines, (
        f"Expected '  network: 4' in the report (with exactly two leading spaces).\n"
        f"Lines in report:\n" + "\n".join(repr(l) for l in lines)
    )


def test_report_component_webserver():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert "  webserver: 4" in lines, (
        f"Expected '  webserver: 4' in the report (with exactly two leading spaces).\n"
        f"Lines in report:\n" + "\n".join(repr(l) for l in lines)
    )


def test_report_components_alphabetical_order():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    # Find the "Changes by component:" section and extract component lines
    in_component_section = False
    component_lines = []
    for line in lines:
        if line == "Changes by component:":
            in_component_section = True
            continue
        if in_component_section:
            if line.startswith("  ") and ":" in line:
                component_lines.append(line)
            else:
                break

    assert len(component_lines) == 4, (
        f"Expected 4 component lines in 'Changes by component:' section, got {len(component_lines)}.\n"
        f"Component lines found: {component_lines!r}"
    )

    expected_component_lines = [
        "  database: 4",
        "  firewall: 3",
        "  network: 4",
        "  webserver: 4",
    ]
    assert component_lines == expected_component_lines, (
        f"Component lines are not in alphabetical order or have wrong counts.\n"
        f"Expected: {expected_component_lines!r}\n"
        f"Actual:   {component_lines!r}"
    )


def test_report_blank_line_between_sections():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    # There should be a blank line between the summary and "Changes by user:"
    # and between "Changes by user:" section and "Changes by component:"
    # Check blank line after "Failed changes: 5"
    failed_idx = None
    for i, line in enumerate(lines):
        if line.startswith("Failed changes:"):
            failed_idx = i
            break

    assert failed_idx is not None, "Could not find 'Failed changes:' line."
    assert failed_idx + 1 < len(lines) and lines[failed_idx + 1] == "", (
        f"Expected a blank line after 'Failed changes: 5' (line index {failed_idx}), "
        f"but got: {lines[failed_idx + 1]!r}"
    )

    # Check blank line between user section and component section
    user_section_idx = None
    for i, line in enumerate(lines):
        if line == "Changes by user:":
            user_section_idx = i
            break

    assert user_section_idx is not None, "Could not find 'Changes by user:' line."

    # Find end of user entries
    end_of_users = user_section_idx + 1
    while end_of_users < len(lines) and lines[end_of_users].startswith("  "):
        end_of_users += 1

    assert end_of_users < len(lines) and lines[end_of_users] == "", (
        f"Expected a blank line after the user entries, "
        f"but got: {lines[end_of_users]!r}"
    )


def test_log_file_unchanged():
    """Ensure the original log file was not modified."""
    log_file = "/home/user/config_changes.log"
    expected_lines = [
        "[2024-06-10 08:14:02] USER=alice COMPONENT=database ACTION=update STATUS=success",
        "[2024-06-10 08:45:17] USER=bob COMPONENT=webserver ACTION=update STATUS=success",
        "[2024-06-10 09:02:33] USER=alice COMPONENT=network ACTION=update STATUS=failure",
        "[2024-06-10 09:30:55] USER=bob COMPONENT=network ACTION=rollback STATUS=failure",
        "[2024-06-10 10:11:08] USER=carol COMPONENT=database ACTION=update STATUS=success",
        "[2024-06-10 10:45:22] USER=alice COMPONENT=firewall ACTION=update STATUS=success",
        "[2024-06-10 11:03:41] USER=carol COMPONENT=webserver ACTION=update STATUS=success",
        "[2024-06-10 11:28:59] USER=bob COMPONENT=database ACTION=rollback STATUS=success",
        "[2024-06-10 12:00:05] USER=alice COMPONENT=webserver ACTION=update STATUS=success",
        "[2024-06-10 13:15:44] USER=carol COMPONENT=firewall ACTION=update STATUS=failure",
        "[2024-06-10 14:02:30] USER=alice COMPONENT=database ACTION=update STATUS=success",
        "[2024-06-10 14:55:13] USER=bob COMPONENT=firewall ACTION=update STATUS=success",
        "[2024-06-10 15:30:27] USER=carol COMPONENT=network ACTION=update STATUS=success",
        "[2024-06-10 16:10:09] USER=alice COMPONENT=network ACTION=rollback STATUS=failure",
        "[2024-06-10 16:48:52] USER=bob COMPONENT=webserver ACTION=update STATUS=failure",
    ]

    assert os.path.isfile(log_file), (
        f"Original log file not found: {log_file}"
    )

    with open(log_file, "r") as f:
        actual_lines = [line.rstrip("\n") for line in f if line.strip()]

    assert len(actual_lines) == len(expected_lines), (
        f"Log file line count changed: expected {len(expected_lines)}, got {len(actual_lines)}."
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, expected_lines), start=1):
        assert actual == expected, (
            f"Log file line {i} was modified.\n"
            f"Expected: {expected!r}\n"
            f"Actual:   {actual!r}"
        )