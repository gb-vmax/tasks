# test_final_state.py

import os
import stat
import subprocess
import pytest


def test_alice_in_devteam():
    """alice must be a member of the devteam group."""
    result = subprocess.run(
        ["groups", "alice"],
        capture_output=True,
        text=True,
        check=True
    )
    groups_output = result.stdout.strip()
    assert "devteam" in groups_output, (
        f"alice is NOT in the devteam group. "
        f"Current groups for alice: {groups_output}"
    )


def test_alice_in_devteam_via_etc_group():
    """Verify alice is in devteam via /etc/group as a secondary check."""
    with open("/etc/group", "r") as f:
        group_contents = f.read()

    # Find the devteam line
    devteam_line = None
    for line in group_contents.splitlines():
        if line.startswith("devteam:"):
            devteam_line = line
            break

    assert devteam_line is not None, (
        "Group 'devteam' not found in /etc/group."
    )
    assert "alice" in devteam_line, (
        f"alice is not listed in the devteam group entry in /etc/group. "
        f"devteam line: {devteam_line}"
    )


def test_config_cfg_exists():
    """File /home/user/projects/webapp/config.cfg must exist."""
    path = "/home/user/projects/webapp/config.cfg"
    assert os.path.isfile(path), (
        f"File '{path}' does not exist."
    )


def test_config_cfg_mode_is_0640():
    """config.cfg must have mode 0640 (fixed permissions)."""
    path = "/home/user/projects/webapp/config.cfg"
    result = subprocess.run(
        ["stat", "-c", "%a", path],
        capture_output=True,
        text=True,
        check=True
    )
    mode = result.stdout.strip()
    assert mode == "640", (
        f"File '{path}' should have mode 640, but currently has mode {mode}. "
        "The permissions have not been fixed correctly."
    )


def test_config_cfg_content_preserved():
    """config.cfg content should still contain 'db_password=secret'."""
    path = "/home/user/projects/webapp/config.cfg"
    with open(path, "r") as f:
        content = f.read()
    assert "db_password=secret" in content, (
        f"File '{path}' no longer contains expected content 'db_password=secret'. "
        f"Actual content: {repr(content)}"
    )


def test_ticket_042_exists():
    """File /home/user/tickets/ticket_042.txt must exist."""
    path = "/home/user/tickets/ticket_042.txt"
    assert os.path.isfile(path), (
        f"File '{path}' does not exist. The resolution log was not created."
    )


def test_ticket_042_exact_content():
    """ticket_042.txt must have the exact required content."""
    path = "/home/user/tickets/ticket_042.txt"
    expected_content = (
        "Ticket: 042\n"
        "Status: resolved\n"
        "User: alice\n"
        "Group added: devteam\n"
        "Config file: /home/user/projects/webapp/config.cfg\n"
        "Config permissions: 640\n"
    )
    with open(path, "r") as f:
        actual_content = f.read()

    assert actual_content == expected_content, (
        f"File '{path}' does not have the exact required content.\n"
        f"Expected: {repr(expected_content)}\n"
        f"Actual:   {repr(actual_content)}"
    )


def test_ticket_042_line_count():
    """ticket_042.txt must have exactly 6 lines."""
    path = "/home/user/tickets/ticket_042.txt"
    result = subprocess.run(
        ["wc", "-l", path],
        capture_output=True,
        text=True,
        check=True
    )
    # wc -l output is like "6 /path/to/file"
    line_count = int(result.stdout.strip().split()[0])
    assert line_count == 6, (
        f"File '{path}' should have exactly 6 lines, but has {line_count} lines."
    )


def test_ticket_042_no_trailing_spaces():
    """ticket_042.txt must have no trailing spaces on any line."""
    path = "/home/user/tickets/ticket_042.txt"
    with open(path, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        # Strip the newline, then check for trailing spaces
        line_without_newline = line.rstrip("\n")
        assert line_without_newline == line_without_newline.rstrip(), (
            f"Line {i} in '{path}' has trailing spaces: {repr(line)}"
        )


def test_ticket_042_ends_with_newline():
    """ticket_042.txt must end with a newline character."""
    path = "/home/user/tickets/ticket_042.txt"
    with open(path, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"File '{path}' does not end with a newline. "
        f"Last bytes: {repr(content[-10:])}"
    )


def test_ticket_042_no_extra_blank_lines():
    """ticket_042.txt must not have any extra blank lines."""
    path = "/home/user/tickets/ticket_042.txt"
    with open(path, "r") as f:
        content = f.read()

    # Split by newline - after stripping trailing newline, there should be exactly 6 parts
    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 6, (
        f"File '{path}' should have exactly 6 non-empty lines (no extra blank lines), "
        f"but splitting gives {len(lines)} parts: {lines}"
    )

    for i, line in enumerate(lines, start=1):
        assert line != "", (
            f"Line {i} in '{path}' is blank, which is not allowed."
        )


def test_ticket_042_individual_lines():
    """Each line in ticket_042.txt must match the expected value exactly."""
    path = "/home/user/tickets/ticket_042.txt"
    expected_lines = [
        "Ticket: 042",
        "Status: resolved",
        "User: alice",
        "Group added: devteam",
        "Config file: /home/user/projects/webapp/config.cfg",
        "Config permissions: 640",
    ]
    with open(path, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").split("\n")

    assert len(actual_lines) == len(expected_lines), (
        f"Expected {len(expected_lines)} lines, but got {len(actual_lines)} lines."
    )

    for i, (expected, actual) in enumerate(zip(expected_lines, actual_lines), start=1):
        assert actual == expected, (
            f"Line {i} mismatch in '{path}'.\n"
            f"  Expected: {repr(expected)}\n"
            f"  Actual:   {repr(actual)}"
        )