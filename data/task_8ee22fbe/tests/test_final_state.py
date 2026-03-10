# test_final_state.py

import os
import stat
import pytest

MONITORING_DIR = "/home/user/monitoring"
CONFIG_DIR = "/home/user/monitoring/config"
HEALTHCHECK = "/home/user/monitoring/healthcheck.sh"
CREDENTIALS = "/home/user/monitoring/config/api_credentials.conf"
AUDIT_REPORT = "/home/user/monitoring/audit_report.txt"

EXPECTED_AUDIT_REPORT_CONTENTS = """\
=== SECURITY AUDIT REPORT ===
Date: 2024-01-15
Auditor: sre-bot

VULNERABILITIES FIXED:

[1] healthcheck.sh
    Previous permissions: 0777
    Fixed permissions: 0750
    Risk: World-writable script executed by cron - arbitrary code injection

[2] api_credentials.conf
    Previous permissions: 0644
    Fixed permissions: 0600
    Risk: World-readable credentials file - API key exposure

STATUS: RESOLVED
"""


def get_octal_permissions(path):
    """Return the permission bits of a file as an octal integer."""
    return stat.S_IMODE(os.stat(path).st_mode)


# --- Directory existence and permissions ---

def test_monitoring_dir_exists():
    assert os.path.isdir(MONITORING_DIR), (
        f"Directory '{MONITORING_DIR}' does not exist. "
        "The monitoring directory must be present."
    )


def test_config_dir_exists():
    assert os.path.isdir(CONFIG_DIR), (
        f"Directory '{CONFIG_DIR}' does not exist. "
        "The config subdirectory must be present."
    )


def test_monitoring_dir_permissions():
    perms = get_octal_permissions(MONITORING_DIR)
    assert perms == 0o755, (
        f"Directory '{MONITORING_DIR}' has permissions {oct(perms)}, "
        f"expected 0o755 (0755). The directory permissions should not have changed."
    )


def test_config_dir_permissions():
    perms = get_octal_permissions(CONFIG_DIR)
    assert perms == 0o755, (
        f"Directory '{CONFIG_DIR}' has permissions {oct(perms)}, "
        f"expected 0o755 (0755). The config directory permissions should not have changed."
    )


# --- healthcheck.sh final state ---

def test_healthcheck_exists():
    assert os.path.isfile(HEALTHCHECK), (
        f"File '{HEALTHCHECK}' does not exist. "
        "The healthcheck script must still be present after fixing permissions."
    )


def test_healthcheck_permissions_are_0750():
    perms = get_octal_permissions(HEALTHCHECK)
    assert perms == 0o750, (
        f"File '{HEALTHCHECK}' has permissions {oct(perms)}, "
        f"expected 0o750 (0750). "
        "The healthcheck script must be changed from 0777 to 0750 to prevent "
        "world-writable access while allowing owner full access and group read/execute."
    )


def test_healthcheck_contents_unchanged():
    expected = (
        "#!/bin/bash\n"
        "curl -s https://example.com/health | grep -q \"ok\" && echo \"UP\" || echo \"DOWN\"\n"
    )
    assert os.path.isfile(HEALTHCHECK), (
        f"File '{HEALTHCHECK}' does not exist, cannot check contents."
    )
    with open(HEALTHCHECK, "r") as f:
        contents = f.read()
    assert contents.strip() == expected.strip(), (
        f"File '{HEALTHCHECK}' has unexpected contents after permission fix.\n"
        f"Expected:\n{expected}\n"
        f"Got:\n{contents}\n"
        "Only permissions should have been changed, not the file contents."
    )


# --- api_credentials.conf final state ---

def test_credentials_exists():
    assert os.path.isfile(CREDENTIALS), (
        f"File '{CREDENTIALS}' does not exist. "
        "The credentials file must still be present after fixing permissions."
    )


def test_credentials_permissions_are_0600():
    perms = get_octal_permissions(CREDENTIALS)
    assert perms == 0o600, (
        f"File '{CREDENTIALS}' has permissions {oct(perms)}, "
        f"expected 0o600 (0600). "
        "The credentials file must be changed from 0644 to 0600 so that only "
        "the owner can read/write it, protecting sensitive API keys."
    )


def test_credentials_contents_unchanged():
    expected = (
        "API_KEY=supersecret123\n"
        "API_SECRET=topsecretvalue456\n"
        "ENDPOINT=https://monitoring.example.com/api\n"
    )
    assert os.path.isfile(CREDENTIALS), (
        f"File '{CREDENTIALS}' does not exist, cannot check contents."
    )
    with open(CREDENTIALS, "r") as f:
        contents = f.read()
    assert contents.strip() == expected.strip(), (
        f"File '{CREDENTIALS}' has unexpected contents after permission fix.\n"
        f"Expected:\n{expected}\n"
        f"Got:\n{contents}\n"
        "Only permissions should have been changed, not the file contents."
    )


# --- audit_report.txt existence, permissions, and contents ---

def test_audit_report_exists():
    assert os.path.isfile(AUDIT_REPORT), (
        f"File '{AUDIT_REPORT}' does not exist. "
        "The security audit report must be created as part of completing the task."
    )


def test_audit_report_permissions_are_0640():
    assert os.path.isfile(AUDIT_REPORT), (
        f"File '{AUDIT_REPORT}' does not exist, cannot check permissions."
    )
    perms = get_octal_permissions(AUDIT_REPORT)
    assert perms == 0o640, (
        f"File '{AUDIT_REPORT}' has permissions {oct(perms)}, "
        f"expected 0o640 (0640). "
        "The audit report must be readable by owner (rw) and group (r), "
        "with no access for others."
    )


def test_audit_report_contents_exact():
    assert os.path.isfile(AUDIT_REPORT), (
        f"File '{AUDIT_REPORT}' does not exist, cannot check contents."
    )
    with open(AUDIT_REPORT, "r") as f:
        contents = f.read()

    assert contents == EXPECTED_AUDIT_REPORT_CONTENTS, (
        f"File '{AUDIT_REPORT}' does not have the exact expected contents.\n"
        f"--- EXPECTED ---\n{EXPECTED_AUDIT_REPORT_CONTENTS!r}\n"
        f"--- GOT ---\n{contents!r}\n"
        "The audit report must match the required format exactly, including "
        "spacing, indentation, and a trailing newline after 'STATUS: RESOLVED'."
    )


def test_audit_report_ends_with_newline():
    assert os.path.isfile(AUDIT_REPORT), (
        f"File '{AUDIT_REPORT}' does not exist, cannot check trailing newline."
    )
    with open(AUDIT_REPORT, "r") as f:
        contents = f.read()
    assert contents.endswith("\n"), (
        f"File '{AUDIT_REPORT}' does not end with a newline character. "
        "The file must end with a newline after 'STATUS: RESOLVED'."
    )


def test_audit_report_no_extra_trailing_content():
    assert os.path.isfile(AUDIT_REPORT), (
        f"File '{AUDIT_REPORT}' does not exist, cannot check for extra trailing content."
    )
    with open(AUDIT_REPORT, "r") as f:
        contents = f.read()
    # Strip the single trailing newline and ensure no extra blank lines at the end
    stripped = contents.rstrip("\n")
    assert stripped.endswith("STATUS: RESOLVED"), (
        f"File '{AUDIT_REPORT}' does not end with 'STATUS: RESOLVED' (ignoring trailing newline). "
        f"Last characters found: {contents[-50:]!r}"
    )


def test_audit_report_contains_healthcheck_section():
    assert os.path.isfile(AUDIT_REPORT), (
        f"File '{AUDIT_REPORT}' does not exist."
    )
    with open(AUDIT_REPORT, "r") as f:
        contents = f.read()
    assert "[1] healthcheck.sh" in contents, (
        f"Audit report is missing the '[1] healthcheck.sh' section."
    )
    assert "Previous permissions: 0777" in contents, (
        f"Audit report is missing 'Previous permissions: 0777' for healthcheck.sh."
    )
    assert "Fixed permissions: 0750" in contents, (
        f"Audit report is missing 'Fixed permissions: 0750' for healthcheck.sh."
    )
    assert "Risk: World-writable script executed by cron - arbitrary code injection" in contents, (
        f"Audit report is missing the risk description for healthcheck.sh."
    )


def test_audit_report_contains_credentials_section():
    assert os.path.isfile(AUDIT_REPORT), (
        f"File '{AUDIT_REPORT}' does not exist."
    )
    with open(AUDIT_REPORT, "r") as f:
        contents = f.read()
    assert "[2] api_credentials.conf" in contents, (
        f"Audit report is missing the '[2] api_credentials.conf' section."
    )
    assert "Previous permissions: 0644" in contents, (
        f"Audit report is missing 'Previous permissions: 0644' for api_credentials.conf."
    )
    assert "Fixed permissions: 0600" in contents, (
        f"Audit report is missing 'Fixed permissions: 0600' for api_credentials.conf."
    )
    assert "Risk: World-readable credentials file - API key exposure" in contents, (
        f"Audit report is missing the risk description for api_credentials.conf."
    )


def test_audit_report_header_and_status():
    assert os.path.isfile(AUDIT_REPORT), (
        f"File '{AUDIT_REPORT}' does not exist."
    )
    with open(AUDIT_REPORT, "r") as f:
        contents = f.read()
    assert "=== SECURITY AUDIT REPORT ===" in contents, (
        f"Audit report is missing the header '=== SECURITY AUDIT REPORT ==='."
    )
    assert "Date: 2024-01-15" in contents, (
        f"Audit report is missing 'Date: 2024-01-15'."
    )
    assert "Auditor: sre-bot" in contents, (
        f"Audit report is missing 'Auditor: sre-bot'."
    )
    assert "STATUS: RESOLVED" in contents, (
        f"Audit report is missing 'STATUS: RESOLVED'."
    )