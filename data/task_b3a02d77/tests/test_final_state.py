# test_final_state.py

import os
import stat
import pytest

SECRETS_FILE = "/home/user/config/secrets.env"
AUDIT_DIR = "/home/user/audit"
AUDIT_LOG = "/home/user/audit/permissions.log"
EXPECTED_LOG_LINE = "ENFORCED 600 /home/user/config/secrets.env"


def test_secrets_file_exists():
    """The secrets file must still exist after the task."""
    assert os.path.isfile(SECRETS_FILE), (
        f"Expected file {SECRETS_FILE} to exist, but it does not. "
        "The file may have been accidentally deleted."
    )


def test_secrets_file_permissions_are_600():
    """The secrets file must have permissions 600 (owner rw, group none, others none)."""
    assert os.path.isfile(SECRETS_FILE), (
        f"{SECRETS_FILE} does not exist — cannot check permissions."
    )
    file_stat = os.stat(SECRETS_FILE)
    mode = stat.S_IMODE(file_stat.st_mode)
    assert mode == 0o600, (
        f"Expected {SECRETS_FILE} to have permissions 0600 (-rw-------), "
        f"but got {oct(mode)}. "
        "Run: chmod 600 /home/user/config/secrets.env"
    )


def test_secrets_file_contents_unchanged():
    """The secrets file contents must remain unchanged after permission enforcement."""
    assert os.path.isfile(SECRETS_FILE), (
        f"{SECRETS_FILE} does not exist — cannot check contents."
    )
    with open(SECRETS_FILE, "r") as f:
        contents = f.read()
    expected_lines = {"DB_PASSWORD=supersecret", "API_KEY=abc123"}
    actual_lines = set(
        line.strip() for line in contents.strip().splitlines() if line.strip()
    )
    assert expected_lines == actual_lines, (
        f"Expected {SECRETS_FILE} to contain lines {expected_lines}, "
        f"but got {actual_lines}. The file contents should not have been modified."
    )


def test_audit_directory_exists():
    """The audit directory /home/user/audit/ must exist."""
    assert os.path.isdir(AUDIT_DIR), (
        f"Expected directory {AUDIT_DIR} to exist, but it does not. "
        "Run: mkdir -p /home/user/audit"
    )


def test_audit_log_exists():
    """The audit log file must exist."""
    assert os.path.isfile(AUDIT_LOG), (
        f"Expected audit log file {AUDIT_LOG} to exist, but it does not. "
        f"Create it with the required content: '{EXPECTED_LOG_LINE}'"
    )


def test_audit_log_exact_content():
    """The audit log must contain exactly one line with the correct format."""
    assert os.path.isfile(AUDIT_LOG), (
        f"{AUDIT_LOG} does not exist — cannot check contents."
    )
    with open(AUDIT_LOG, "r") as f:
        contents = f.read()

    # Must be newline-terminated, one line
    lines = contents.splitlines()
    assert len(lines) == 1, (
        f"Expected {AUDIT_LOG} to contain exactly 1 line, "
        f"but found {len(lines)} lines. Contents: {repr(contents)}"
    )

    actual_line = lines[0]
    assert actual_line == EXPECTED_LOG_LINE, (
        f"Expected {AUDIT_LOG} to contain exactly:\n"
        f"  '{EXPECTED_LOG_LINE}'\n"
        f"But got:\n"
        f"  '{actual_line}'\n"
        "Check for extra spaces, wrong mode value, or incorrect file path."
    )


def test_audit_log_no_trailing_whitespace():
    """The audit log line must not have trailing whitespace."""
    assert os.path.isfile(AUDIT_LOG), (
        f"{AUDIT_LOG} does not exist — cannot check for trailing whitespace."
    )
    with open(AUDIT_LOG, "r") as f:
        contents = f.read()

    lines = contents.splitlines()
    if lines:
        line = lines[0]
        assert line == line.rstrip(), (
            f"The line in {AUDIT_LOG} has trailing whitespace. "
            f"Got: {repr(line)}"
        )


def test_audit_log_newline_terminated():
    """The audit log file should be newline-terminated (standard UNIX text file)."""
    assert os.path.isfile(AUDIT_LOG), (
        f"{AUDIT_LOG} does not exist — cannot check newline termination."
    )
    with open(AUDIT_LOG, "rb") as f:
        raw = f.read()

    assert raw.endswith(b"\n"), (
        f"Expected {AUDIT_LOG} to end with a newline character, "
        f"but it does not. Raw bytes at end: {repr(raw[-10:])}"
    )


def test_audit_log_no_blank_lines():
    """The audit log must not contain blank lines."""
    assert os.path.isfile(AUDIT_LOG), (
        f"{AUDIT_LOG} does not exist — cannot check for blank lines."
    )
    with open(AUDIT_LOG, "r") as f:
        contents = f.read()

    blank_lines = [i + 1 for i, line in enumerate(contents.splitlines()) if line.strip() == ""]
    assert not blank_lines, (
        f"Found blank lines in {AUDIT_LOG} at line numbers: {blank_lines}. "
        "The file must contain exactly one non-blank line."
    )


def test_stat_command_output():
    """Verify the permissions via stat module match what 'stat -c \"%a\"' would report."""
    assert os.path.isfile(SECRETS_FILE), (
        f"{SECRETS_FILE} does not exist — cannot verify stat output."
    )
    file_stat = os.stat(SECRETS_FILE)
    mode = stat.S_IMODE(file_stat.st_mode)
    octal_str = format(mode, "o")
    assert octal_str == "600", (
        f"Expected 'stat -c \"%a\" {SECRETS_FILE}' to output '600', "
        f"but the equivalent Python stat gives '{octal_str}'. "
        f"Current permissions: {oct(mode)}"
    )