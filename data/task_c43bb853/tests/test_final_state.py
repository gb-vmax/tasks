# test_final_state.py

import os
import pytest

SSHD_CONFIG_PATH = "/home/user/sshd_config"
REPORT_PATH = "/home/user/sshd_hardening_report.txt"

EXPECTED_SSHD_CONFIG = """# This is the sshd server system-wide configuration file.
Protocol 2
HostKey /etc/ssh/ssh_host_rsa_key
PermitRootLogin no
MaxAuthTries 4
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
X11Forwarding no
PrintMotd no
AcceptEnv LANG LC_*
Subsystem sftp /usr/lib/openssh/sftp-server
"""

EXPECTED_REPORT = (
    "SSH Hardening Report\n"
    "====================\n"
    "PermitRootLogin: yes -> no\n"
    "PasswordAuthentication: yes -> no\n"
    "X11Forwarding: yes -> no\n"
)


# ── sshd_config tests ──────────────────────────────────────────────────────────

def test_sshd_config_exists():
    assert os.path.isfile(SSHD_CONFIG_PATH), (
        f"sshd_config file does not exist at {SSHD_CONFIG_PATH}"
    )


def test_sshd_config_full_content():
    with open(SSHD_CONFIG_PATH, "r") as f:
        content = f.read()
    assert content == EXPECTED_SSHD_CONFIG, (
        f"sshd_config content does not match expected.\n"
        f"Expected:\n{EXPECTED_SSHD_CONFIG!r}\n\n"
        f"Actual:\n{content!r}"
    )


def test_permit_root_login_no():
    with open(SSHD_CONFIG_PATH, "r") as f:
        lines = f.readlines()
    matching = [l.rstrip("\n") for l in lines if l.startswith("PermitRootLogin")]
    assert len(matching) >= 1, (
        "No 'PermitRootLogin' directive found in sshd_config"
    )
    assert matching[0] == "PermitRootLogin no", (
        f"Expected 'PermitRootLogin no', got: {matching[0]!r} — "
        "PermitRootLogin must be set to 'no'"
    )


def test_password_authentication_no():
    with open(SSHD_CONFIG_PATH, "r") as f:
        lines = f.readlines()
    matching = [l.rstrip("\n") for l in lines if l.startswith("PasswordAuthentication")]
    assert len(matching) >= 1, (
        "No 'PasswordAuthentication' directive found in sshd_config"
    )
    assert matching[0] == "PasswordAuthentication no", (
        f"Expected 'PasswordAuthentication no', got: {matching[0]!r} — "
        "PasswordAuthentication must be set to 'no'"
    )


def test_x11_forwarding_no():
    with open(SSHD_CONFIG_PATH, "r") as f:
        lines = f.readlines()
    matching = [l.rstrip("\n") for l in lines if l.startswith("X11Forwarding")]
    assert len(matching) >= 1, (
        "No 'X11Forwarding' directive found in sshd_config"
    )
    assert matching[0] == "X11Forwarding no", (
        f"Expected 'X11Forwarding no', got: {matching[0]!r} — "
        "X11Forwarding must be set to 'no'"
    )


def test_sshd_config_unchanged_lines():
    """Verify that lines not subject to hardening are untouched."""
    with open(SSHD_CONFIG_PATH, "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines()]

    expected_unchanged = [
        "# This is the sshd server system-wide configuration file.",
        "Protocol 2",
        "HostKey /etc/ssh/ssh_host_rsa_key",
        "MaxAuthTries 4",
        "PubkeyAuthentication yes",
        "PermitEmptyPasswords no",
        "PrintMotd no",
        "AcceptEnv LANG LC_*",
        "Subsystem sftp /usr/lib/openssh/sftp-server",
    ]
    for expected_line in expected_unchanged:
        assert expected_line in lines, (
            f"Expected unchanged line not found in sshd_config: {expected_line!r}"
        )


def test_sshd_config_line_count():
    with open(SSHD_CONFIG_PATH, "r") as f:
        lines = f.readlines()
    # 12 content lines + trailing newline means 12 lines when split
    assert len(lines) == 12, (
        f"Expected 12 lines in sshd_config, got {len(lines)}. "
        "Ensure no lines were added or removed."
    )


# ── report file tests ──────────────────────────────────────────────────────────

def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Hardening report file does not exist at {REPORT_PATH}"
    )


def test_report_file_exact_content():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert content == EXPECTED_REPORT, (
        f"Report file content does not match expected.\n"
        f"Expected bytes: {EXPECTED_REPORT!r}\n"
        f"Actual bytes:   {content!r}"
    )


def test_report_file_line_count():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    # 5 lines of text + trailing newline → split gives 6 elements, last empty
    assert content.endswith("\n"), (
        "Report file must end with a trailing newline character."
    )
    non_empty_lines = content.rstrip("\n").split("\n")
    assert len(non_empty_lines) == 5, (
        f"Expected 5 lines in the report, got {len(non_empty_lines)}. "
        f"Content: {content!r}"
    )


def test_report_header_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[0] == "SSH Hardening Report", (
        f"First line of report must be 'SSH Hardening Report', got: {lines[0]!r}"
    )


def test_report_separator_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[1] == "====================", (
        f"Second line of report must be '====================', got: {lines[1]!r}"
    )


def test_report_permit_root_login_entry():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[2] == "PermitRootLogin: yes -> no", (
        f"Third line of report must be 'PermitRootLogin: yes -> no', got: {lines[2]!r}"
    )


def test_report_password_authentication_entry():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[3] == "PasswordAuthentication: yes -> no", (
        f"Fourth line of report must be 'PasswordAuthentication: yes -> no', got: {lines[3]!r}"
    )


def test_report_x11_forwarding_entry():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[4] == "X11Forwarding: yes -> no", (
        f"Fifth line of report must be 'X11Forwarding: yes -> no', got: {lines[4]!r}"
    )


def test_report_no_trailing_spaces():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} of report has trailing whitespace: {line!r}"
        )


def test_report_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file is not readable: {REPORT_PATH}"
    )