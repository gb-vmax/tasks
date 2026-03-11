# test_final_state.py

import os
import stat
import pytest

SERVICES_DIR = "/home/user/services"
AUDIT_REPORT_PATH = "/home/user/services/audit_report.txt"

EXPECTED_PERMISSIONS = {
    "db_credentials.env": 0o600,
    "api_secret.key": 0o600,
    "auth_token.txt": 0o600,
    "app_config.yaml": 0o640,
    "nginx_config.conf": 0o640,
    "README.md": 0o644,
}

EXPECTED_FILE_CONTENTS = {
    "db_credentials.env": "DB_PASSWORD=supersecret\n",
    "api_secret.key": "API_SECRET=abc123xyz\n",
    "auth_token.txt": "TOKEN=eyJhbGci\n",
    "app_config.yaml": "port: 8080\nhost: localhost\n",
    "nginx_config.conf": "worker_processes 1;\n",
    "README.md": "# Services\n",
}

EXPECTED_AUDIT_REPORT = (
    "PERMISSION AUDIT REPORT\n"
    "=======================\n"
    "FILE: README.md\n"
    "  BEFORE: 777\n"
    "  AFTER: 644\n"
    "FILE: api_secret.key\n"
    "  BEFORE: 777\n"
    "  AFTER: 600\n"
    "FILE: app_config.yaml\n"
    "  BEFORE: 777\n"
    "  AFTER: 640\n"
    "FILE: auth_token.txt\n"
    "  BEFORE: 755\n"
    "  AFTER: 600\n"
    "FILE: db_credentials.env\n"
    "  BEFORE: 777\n"
    "  AFTER: 600\n"
    "FILE: nginx_config.conf\n"
    "  BEFORE: 755\n"
    "  AFTER: 640\n"
    "=======================\n"
    "TOTAL FILES REMEDIATED: 6\n"
)


# ---------------------------------------------------------------------------
# Directory / structure checks
# ---------------------------------------------------------------------------

def test_services_directory_exists():
    assert os.path.isdir(SERVICES_DIR), (
        f"Directory '{SERVICES_DIR}' does not exist."
    )


def test_audit_report_exists():
    assert os.path.isfile(AUDIT_REPORT_PATH), (
        f"Audit report '{AUDIT_REPORT_PATH}' does not exist. "
        "The student must create this file as part of the task."
    )


# ---------------------------------------------------------------------------
# File existence checks
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filename", EXPECTED_PERMISSIONS.keys())
def test_service_file_exists(filename):
    filepath = os.path.join(SERVICES_DIR, filename)
    assert os.path.isfile(filepath), (
        f"Expected service file '{filepath}' does not exist. "
        "Service files must not be removed during the task."
    )


# ---------------------------------------------------------------------------
# Permission checks
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filename,expected_mode", EXPECTED_PERMISSIONS.items())
def test_service_file_permissions(filename, expected_mode):
    filepath = os.path.join(SERVICES_DIR, filename)
    assert os.path.isfile(filepath), f"File '{filepath}' does not exist."

    file_stat = os.stat(filepath)
    actual_mode = stat.S_IMODE(file_stat.st_mode)

    assert actual_mode == expected_mode, (
        f"File '{filepath}' has permissions {oct(actual_mode)} "
        f"but expected {oct(expected_mode)}. "
        "Permissions were not set correctly according to the remediation rules."
    )


# ---------------------------------------------------------------------------
# Content integrity checks (files should not be modified)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filename,expected_content", EXPECTED_FILE_CONTENTS.items())
def test_service_file_content_unchanged(filename, expected_content):
    filepath = os.path.join(SERVICES_DIR, filename)
    assert os.path.isfile(filepath), f"File '{filepath}' does not exist."

    with open(filepath, "r") as f:
        actual_content = f.read()

    assert actual_content == expected_content, (
        f"File '{filepath}' content was unexpectedly modified.\n"
        f"Expected: {repr(expected_content)}\n"
        f"Actual:   {repr(actual_content)}"
    )


# ---------------------------------------------------------------------------
# Audit report content checks
# ---------------------------------------------------------------------------

def test_audit_report_exact_content():
    assert os.path.isfile(AUDIT_REPORT_PATH), (
        f"Audit report '{AUDIT_REPORT_PATH}' does not exist."
    )

    with open(AUDIT_REPORT_PATH, "r") as f:
        actual_content = f.read()

    assert actual_content == EXPECTED_AUDIT_REPORT, (
        f"Audit report content does not match expected.\n"
        f"Expected:\n{repr(EXPECTED_AUDIT_REPORT)}\n\n"
        f"Actual:\n{repr(actual_content)}"
    )


def test_audit_report_header_line():
    with open(AUDIT_REPORT_PATH, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 1, "Audit report is empty."
    assert lines[0].rstrip("\n") == "PERMISSION AUDIT REPORT", (
        f"First line of audit report is incorrect.\n"
        f"Expected: 'PERMISSION AUDIT REPORT'\n"
        f"Actual:   {repr(lines[0].rstrip(chr(10)))}"
    )


def test_audit_report_separator_lines():
    """Both separator lines must be exactly 23 '=' characters."""
    with open(AUDIT_REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    separator = "=" * 23
    separator_lines = [i for i, line in enumerate(lines) if line == separator]

    assert len(separator_lines) == 2, (
        f"Expected exactly 2 separator lines of 23 '=' characters, "
        f"but found {len(separator_lines)}. "
        f"Lines matching: {separator_lines}"
    )

    # First separator should be line index 1 (second line)
    assert separator_lines[0] == 1, (
        f"First separator line should be at line 2 (index 1), "
        f"but found at index {separator_lines[0]}."
    )

    # Second separator should be the second-to-last line (before TOTAL FILES line)
    assert separator_lines[1] == len(lines) - 2, (
        f"Second separator line should be second-to-last line (index {len(lines) - 2}), "
        f"but found at index {separator_lines[1]}."
    )


def test_audit_report_total_files_remediated():
    with open(AUDIT_REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    last_line = lines[-1]
    assert last_line == "TOTAL FILES REMEDIATED: 6", (
        f"Last line of audit report is incorrect.\n"
        f"Expected: 'TOTAL FILES REMEDIATED: 6'\n"
        f"Actual:   {repr(last_line)}"
    )


def test_audit_report_file_entries_count():
    with open(AUDIT_REPORT_PATH, "r") as f:
        content = f.read()

    file_entries = [line for line in content.splitlines() if line.startswith("FILE: ")]
    assert len(file_entries) == 6, (
        f"Expected 6 FILE entries in audit report, but found {len(file_entries)}.\n"
        f"Entries found: {file_entries}"
    )


def test_audit_report_file_entries_alphabetical_order():
    with open(AUDIT_REPORT_PATH, "r") as f:
        content = f.read()

    file_entries = [
        line[len("FILE: "):].strip()
        for line in content.splitlines()
        if line.startswith("FILE: ")
    ]

    assert file_entries == sorted(file_entries), (
        f"FILE entries in audit report are not in alphabetical order.\n"
        f"Actual order:    {file_entries}\n"
        f"Expected order:  {sorted(file_entries)}"
    )


def test_audit_report_does_not_include_itself():
    with open(AUDIT_REPORT_PATH, "r") as f:
        content = f.read()

    assert "audit_report.txt" not in content, (
        "The audit report must NOT include 'audit_report.txt' as one of the FILE entries."
    )


def test_audit_report_before_values():
    """Verify BEFORE values match original insecure permissions."""
    expected_before = {
        "README.md": "777",
        "api_secret.key": "777",
        "app_config.yaml": "777",
        "auth_token.txt": "755",
        "db_credentials.env": "777",
        "nginx_config.conf": "755",
    }

    with open(AUDIT_REPORT_PATH, "r") as f:
        lines = f.readlines()

    # Parse FILE blocks
    current_file = None
    parsed = {}
    for line in lines:
        line_stripped = line.rstrip("\n")
        if line_stripped.startswith("FILE: "):
            current_file = line_stripped[len("FILE: "):]
            parsed[current_file] = {}
        elif line_stripped.strip().startswith("BEFORE: ") and current_file:
            parsed[current_file]["before"] = line_stripped.strip()[len("BEFORE: "):]
        elif line_stripped.strip().startswith("AFTER: ") and current_file:
            parsed[current_file]["after"] = line_stripped.strip()[len("AFTER: "):]

    for filename, expected_val in expected_before.items():
        assert filename in parsed, (
            f"FILE entry for '{filename}' not found in audit report."
        )
        actual_before = parsed[filename].get("before", "MISSING")
        assert actual_before == expected_val, (
            f"BEFORE value for '{filename}' is incorrect.\n"
            f"Expected: '{expected_val}'\n"
            f"Actual:   '{actual_before}'"
        )


def test_audit_report_after_values():
    """Verify AFTER values match the applied chmod rules."""
    expected_after = {
        "README.md": "644",
        "api_secret.key": "600",
        "app_config.yaml": "640",
        "auth_token.txt": "600",
        "db_credentials.env": "600",
        "nginx_config.conf": "640",
    }

    with open(AUDIT_REPORT_PATH, "r") as f:
        lines = f.readlines()

    current_file = None
    parsed = {}
    for line in lines:
        line_stripped = line.rstrip("\n")
        if line_stripped.startswith("FILE: "):
            current_file = line_stripped[len("FILE: "):]
            parsed[current_file] = {}
        elif line_stripped.strip().startswith("BEFORE: ") and current_file:
            parsed[current_file]["before"] = line_stripped.strip()[len("BEFORE: "):]
        elif line_stripped.strip().startswith("AFTER: ") and current_file:
            parsed[current_file]["after"] = line_stripped.strip()[len("AFTER: "):]

    for filename, expected_val in expected_after.items():
        assert filename in parsed, (
            f"FILE entry for '{filename}' not found in audit report."
        )
        actual_after = parsed[filename].get("after", "MISSING")
        assert actual_after == expected_val, (
            f"AFTER value for '{filename}' is incorrect.\n"
            f"Expected: '{expected_val}'\n"
            f"Actual:   '{actual_after}'"
        )


# ---------------------------------------------------------------------------
# Ensure no unexpected files were added (besides audit_report.txt)
# ---------------------------------------------------------------------------

def test_no_unexpected_files_in_services_dir():
    entries = os.listdir(SERVICES_DIR)
    files_in_dir = {
        entry for entry in entries
        if os.path.isfile(os.path.join(SERVICES_DIR, entry))
    }

    allowed_files = set(EXPECTED_PERMISSIONS.keys()) | {"audit_report.txt"}
    unexpected = files_in_dir - allowed_files

    assert not unexpected, (
        f"Unexpected files found in '{SERVICES_DIR}': {unexpected}. "
        "Only the original service files and 'audit_report.txt' should be present."
    )


def test_exact_file_count_including_audit_report():
    entries = os.listdir(SERVICES_DIR)
    files_in_dir = [
        entry for entry in entries
        if os.path.isfile(os.path.join(SERVICES_DIR, entry))
    ]
    # 6 service files + 1 audit report = 7
    assert len(files_in_dir) == 7, (
        f"Expected exactly 7 files in '{SERVICES_DIR}' (6 service files + audit_report.txt), "
        f"but found {len(files_in_dir)}: {sorted(files_in_dir)}"
    )