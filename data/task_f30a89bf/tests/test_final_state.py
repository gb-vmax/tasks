# test_final_state.py

import os
import pytest

COMPLIANCE_REPORT_PATH = "/home/user/audit/compliance_report.tsv"
AUDIT_DIR = "/home/user/audit"

EXPECTED_HEADER = "username\tserver_id\taccess_level\ttimestamp"

EXPECTED_DATA_ROWS = [
    "jsmith\tSRV-01\tadmin\t2024-06-01T08:12:00Z",
    "ajones\tSRV-02\tread-only\t2024-06-01T08:45:00Z",
    "bwilliams\tSRV-01\tread-write\t2024-06-01T09:03:00Z",
    "jsmith\tSRV-03\tadmin\t2024-06-01T09:17:00Z",
    "mchen\tSRV-02\tread-only\t2024-06-01T10:02:00Z",
    "rdavis\tSRV-01\tread-write\t2024-06-01T10:45:00Z",
    "ajones\tSRV-03\tadmin\t2024-06-01T11:30:00Z",
]

EXPECTED_FULL_CONTENT = "\n".join([EXPECTED_HEADER] + EXPECTED_DATA_ROWS) + "\n"


def test_audit_directory_exists():
    assert os.path.isdir(AUDIT_DIR), (
        f"Audit directory '{AUDIT_DIR}' does not exist."
    )


def test_compliance_report_exists():
    assert os.path.isfile(COMPLIANCE_REPORT_PATH), (
        f"Compliance report file '{COMPLIANCE_REPORT_PATH}' does not exist. "
        "The task requires creating this file."
    )


def test_compliance_report_is_readable():
    assert os.access(COMPLIANCE_REPORT_PATH, os.R_OK), (
        f"Compliance report file '{COMPLIANCE_REPORT_PATH}' is not readable."
    )


def test_compliance_report_ends_with_newline():
    with open(COMPLIANCE_REPORT_PATH, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        f"Compliance report '{COMPLIANCE_REPORT_PATH}' does not end with a newline. "
        f"Last 10 characters: {content[-10:]!r}"
    )


def test_compliance_report_header():
    with open(COMPLIANCE_REPORT_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")
    assert first_line == EXPECTED_HEADER, (
        f"Header line mismatch in '{COMPLIANCE_REPORT_PATH}'.\n"
        f"Expected: {EXPECTED_HEADER!r}\n"
        f"Got:      {first_line!r}"
    )


def test_compliance_report_header_no_original_columns():
    """Ensure the original header columns (ip_address, session_duration_mins) are not present."""
    with open(COMPLIANCE_REPORT_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")
    assert "ip_address" not in first_line, (
        f"Header in '{COMPLIANCE_REPORT_PATH}' still contains 'ip_address', "
        f"which should have been excluded. Header: {first_line!r}"
    )
    assert "session_duration_mins" not in first_line, (
        f"Header in '{COMPLIANCE_REPORT_PATH}' still contains 'session_duration_mins', "
        f"which should have been excluded. Header: {first_line!r}"
    )


def test_compliance_report_total_line_count():
    with open(COMPLIANCE_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 8, (
        f"Expected 8 lines (1 header + 7 data rows) in '{COMPLIANCE_REPORT_PATH}', "
        f"but found {len(lines)} lines."
    )


def test_compliance_report_data_rows():
    with open(COMPLIANCE_REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    # lines[0] is the header, lines[1:] are data rows
    data_rows = lines[1:]

    assert len(data_rows) == len(EXPECTED_DATA_ROWS), (
        f"Expected {len(EXPECTED_DATA_ROWS)} data rows in '{COMPLIANCE_REPORT_PATH}', "
        f"but found {len(data_rows)}."
    )

    for i, (actual, expected) in enumerate(zip(data_rows, EXPECTED_DATA_ROWS), start=1):
        assert actual == expected, (
            f"Data row {i} mismatch in '{COMPLIANCE_REPORT_PATH}'.\n"
            f"Expected: {expected!r}\n"
            f"Got:      {actual!r}"
        )


def test_compliance_report_tab_separated():
    with open(COMPLIANCE_REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    for i, line in enumerate(lines):
        fields = line.split("\t")
        assert len(fields) == 4, (
            f"Line {i+1} in '{COMPLIANCE_REPORT_PATH}' does not have exactly 4 tab-separated fields.\n"
            f"Line content: {line!r}\n"
            f"Fields found: {fields}"
        )


def test_compliance_report_column_order():
    """Verify that columns appear in the correct order: username, server_id, access_level, timestamp."""
    with open(COMPLIANCE_REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    header_fields = lines[0].split("\t")
    assert header_fields == ["username", "server_id", "access_level", "timestamp"], (
        f"Column order in header is incorrect.\n"
        f"Expected: ['username', 'server_id', 'access_level', 'timestamp']\n"
        f"Got:      {header_fields}"
    )


def test_compliance_report_exact_content():
    """Validate the entire file content matches the expected output exactly."""
    with open(COMPLIANCE_REPORT_PATH, "r") as f:
        actual_content = f.read()

    assert actual_content == EXPECTED_FULL_CONTENT, (
        f"Full content of '{COMPLIANCE_REPORT_PATH}' does not match expected.\n"
        f"Expected:\n{EXPECTED_FULL_CONTENT!r}\n\n"
        f"Got:\n{actual_content!r}"
    )


def test_compliance_report_no_ip_addresses_in_data():
    """Ensure no IP address patterns appear in the data rows."""
    import re
    ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')

    with open(COMPLIANCE_REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    data_rows = lines[1:]
    for i, row in enumerate(data_rows, start=1):
        match = ip_pattern.search(row)
        assert match is None, (
            f"Data row {i} in '{COMPLIANCE_REPORT_PATH}' contains an IP address "
            f"({match.group()!r}), which should have been excluded.\n"
            f"Row content: {row!r}"
        )


def test_compliance_report_no_session_durations_in_data():
    """Ensure no standalone numeric-only fields appear at the end of data rows (session durations)."""
    with open(COMPLIANCE_REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    data_rows = lines[1:]
    for i, row in enumerate(data_rows, start=1):
        fields = row.split("\t")
        # The last field should be a timestamp (ISO format), not a plain number
        last_field = fields[-1]
        assert not last_field.isdigit(), (
            f"Data row {i} in '{COMPLIANCE_REPORT_PATH}' appears to end with a numeric value "
            f"({last_field!r}), which suggests session_duration_mins was not removed.\n"
            f"Row content: {row!r}"
        )