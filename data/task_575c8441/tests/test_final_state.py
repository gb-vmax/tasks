# test_final_state.py

import os
import pytest

AUDIT_DIR = "/home/user/audit"
ACCESS_LOG = "/home/user/audit/access_log.tsv"
COMPLIANCE_REPORT = "/home/user/audit/compliance_report.tsv"
USERNAMES_FILE = "/home/user/audit/usernames.txt"

EXPECTED_COMPLIANCE_HEADER = ["username", "system", "action", "timestamp"]

EXPECTED_COMPLIANCE_ROWS = [
    ["alice", "payroll", "LOGIN", "2024-06-01T08:12:34Z"],
    ["bob", "hr_portal", "VIEW", "2024-06-01T08:45:00Z"],
    ["alice", "finance", "EXPORT", "2024-06-01T09:03:11Z"],
    ["charlie", "payroll", "LOGIN", "2024-06-01T09:17:55Z"],
    ["bob", "payroll", "VIEW", "2024-06-01T10:01:22Z"],
    ["diana", "hr_portal", "LOGIN", "2024-06-01T10:34:09Z"],
    ["alice", "hr_portal", "DELETE", "2024-06-01T11:00:00Z"],
    ["charlie", "finance", "VIEW", "2024-06-01T11:22:47Z"],
]

EXPECTED_USERNAMES = ["alice", "bob", "charlie", "diana"]


# ── compliance_report.tsv tests ──────────────────────────────────────────────

def test_compliance_report_exists():
    assert os.path.isfile(COMPLIANCE_REPORT), (
        f"Output file '{COMPLIANCE_REPORT}' does not exist. "
        "The compliance report must be produced by the task."
    )


def test_compliance_report_is_tab_separated():
    with open(COMPLIANCE_REPORT, "r", encoding="utf-8") as f:
        first_line = f.readline().rstrip("\n")
    assert "\t" in first_line, (
        f"The header line of '{COMPLIANCE_REPORT}' does not contain tab characters. "
        f"Header found: {first_line!r}"
    )


def test_compliance_report_header():
    with open(COMPLIANCE_REPORT, "r", encoding="utf-8") as f:
        first_line = f.readline().rstrip("\n")
    columns = first_line.split("\t")
    assert columns == EXPECTED_COMPLIANCE_HEADER, (
        f"Header of '{COMPLIANCE_REPORT}' is incorrect.\n"
        f"Expected: {EXPECTED_COMPLIANCE_HEADER}\n"
        f"Got:      {columns}"
    )


def test_compliance_report_row_count():
    with open(COMPLIANCE_REPORT, "r", encoding="utf-8") as f:
        lines = f.read().rstrip("\n").splitlines()
    # lines[0] is header
    data_lines = lines[1:]
    assert len(data_lines) == len(EXPECTED_COMPLIANCE_ROWS), (
        f"'{COMPLIANCE_REPORT}' has {len(data_lines)} data rows, "
        f"expected {len(EXPECTED_COMPLIANCE_ROWS)}."
    )


def test_compliance_report_data_rows():
    with open(COMPLIANCE_REPORT, "r", encoding="utf-8") as f:
        lines = f.read().rstrip("\n").splitlines()
    data_lines = lines[1:]  # skip header

    for i, (line, expected) in enumerate(zip(data_lines, EXPECTED_COMPLIANCE_ROWS), start=2):
        row = line.split("\t")
        assert row == expected, (
            f"Row {i} of '{COMPLIANCE_REPORT}' is incorrect.\n"
            f"Expected: {expected}\n"
            f"Got:      {row}"
        )


def test_compliance_report_column_count():
    with open(COMPLIANCE_REPORT, "r", encoding="utf-8") as f:
        lines = f.read().rstrip("\n").splitlines()

    for i, line in enumerate(lines, start=1):
        cols = line.split("\t")
        assert len(cols) == 4, (
            f"Line {i} of '{COMPLIANCE_REPORT}' has {len(cols)} columns, expected 4.\n"
            f"Line content: {line!r}"
        )


def test_compliance_report_no_ip_address_column():
    with open(COMPLIANCE_REPORT, "r", encoding="utf-8") as f:
        header_line = f.readline().rstrip("\n")
    columns = header_line.split("\t")
    assert "ip_address" not in columns, (
        f"'{COMPLIANCE_REPORT}' must NOT contain the 'ip_address' column, "
        f"but it was found in the header: {columns}"
    )


def test_compliance_report_no_status_column():
    with open(COMPLIANCE_REPORT, "r", encoding="utf-8") as f:
        header_line = f.readline().rstrip("\n")
    columns = header_line.split("\t")
    assert "status" not in columns, (
        f"'{COMPLIANCE_REPORT}' must NOT contain the 'status' column, "
        f"but it was found in the header: {columns}"
    )


def test_compliance_report_column_order():
    with open(COMPLIANCE_REPORT, "r", encoding="utf-8") as f:
        header_line = f.readline().rstrip("\n")
    columns = header_line.split("\t")
    assert columns == EXPECTED_COMPLIANCE_HEADER, (
        f"Column order in '{COMPLIANCE_REPORT}' is wrong.\n"
        f"Expected order: {EXPECTED_COMPLIANCE_HEADER}\n"
        f"Got:            {columns}"
    )


def test_compliance_report_no_extra_rows():
    with open(COMPLIANCE_REPORT, "r", encoding="utf-8") as f:
        lines = f.read().rstrip("\n").splitlines()
    # header + 8 data rows
    assert len(lines) == 1 + len(EXPECTED_COMPLIANCE_ROWS), (
        f"'{COMPLIANCE_REPORT}' has {len(lines)} total lines "
        f"(including header), expected {1 + len(EXPECTED_COMPLIANCE_ROWS)}."
    )


# ── usernames.txt tests ──────────────────────────────────────────────────────

def test_usernames_file_exists():
    assert os.path.isfile(USERNAMES_FILE), (
        f"Output file '{USERNAMES_FILE}' does not exist. "
        "The usernames file must be produced by the task."
    )


def test_usernames_file_content():
    with open(USERNAMES_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.rstrip("\n").splitlines()
    assert lines == EXPECTED_USERNAMES, (
        f"'{USERNAMES_FILE}' content is incorrect.\n"
        f"Expected (one per line): {EXPECTED_USERNAMES}\n"
        f"Got:                     {lines}"
    )


def test_usernames_file_sorted():
    with open(USERNAMES_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.rstrip("\n").splitlines()
    assert lines == sorted(lines), (
        f"Usernames in '{USERNAMES_FILE}' are not sorted alphabetically.\n"
        f"Got:      {lines}\n"
        f"Expected: {sorted(lines)}"
    )


def test_usernames_file_unique():
    with open(USERNAMES_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.rstrip("\n").splitlines()
    assert len(lines) == len(set(lines)), (
        f"'{USERNAMES_FILE}' contains duplicate usernames.\n"
        f"Lines: {lines}"
    )


def test_usernames_file_no_header():
    with open(USERNAMES_FILE, "r", encoding="utf-8") as f:
        first_line = f.readline().rstrip("\n")
    assert first_line != "username", (
        f"'{USERNAMES_FILE}' must NOT contain a header row, "
        f"but the first line is 'username'."
    )


def test_usernames_file_exact_count():
    with open(USERNAMES_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.rstrip("\n").splitlines()
    assert len(lines) == len(EXPECTED_USERNAMES), (
        f"'{USERNAMES_FILE}' has {len(lines)} lines, "
        f"expected {len(EXPECTED_USERNAMES)} unique usernames."
    )


def test_usernames_file_exact_values():
    with open(USERNAMES_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.rstrip("\n").splitlines()
    assert set(lines) == set(EXPECTED_USERNAMES), (
        f"'{USERNAMES_FILE}' does not contain the expected usernames.\n"
        f"Expected: {set(EXPECTED_USERNAMES)}\n"
        f"Got:      {set(lines)}"
    )


# ── source file integrity check ──────────────────────────────────────────────

def test_access_log_still_intact():
    """Ensure the original access log was not modified."""
    EXPECTED_HEADER = ["timestamp", "username", "ip_address", "system", "action", "status"]
    EXPECTED_ROWS = [
        ["2024-06-01T08:12:34Z", "alice", "10.0.1.5", "payroll", "LOGIN", "SUCCESS"],
        ["2024-06-01T08:45:00Z", "bob", "10.0.1.8", "hr_portal", "VIEW", "SUCCESS"],
        ["2024-06-01T09:03:11Z", "alice", "10.0.1.5", "finance", "EXPORT", "DENIED"],
        ["2024-06-01T09:17:55Z", "charlie", "10.0.2.1", "payroll", "LOGIN", "SUCCESS"],
        ["2024-06-01T10:01:22Z", "bob", "10.0.1.8", "payroll", "VIEW", "SUCCESS"],
        ["2024-06-01T10:34:09Z", "diana", "10.0.3.4", "hr_portal", "LOGIN", "SUCCESS"],
        ["2024-06-01T11:00:00Z", "alice", "10.0.1.5", "hr_portal", "DELETE", "DENIED"],
        ["2024-06-01T11:22:47Z", "charlie", "10.0.2.1", "finance", "VIEW", "SUCCESS"],
    ]

    assert os.path.isfile(ACCESS_LOG), (
        f"Source file '{ACCESS_LOG}' is missing — it must not be deleted."
    )

    with open(ACCESS_LOG, "r", encoding="utf-8") as f:
        lines = f.read().rstrip("\n").splitlines()

    header = lines[0].split("\t")
    assert header == EXPECTED_HEADER, (
        f"Header of '{ACCESS_LOG}' was modified.\n"
        f"Expected: {EXPECTED_HEADER}\n"
        f"Got:      {header}"
    )

    data_lines = lines[1:]
    assert len(data_lines) == len(EXPECTED_ROWS), (
        f"'{ACCESS_LOG}' has {len(data_lines)} data rows, expected {len(EXPECTED_ROWS)}."
    )

    for i, (line, expected) in enumerate(zip(data_lines, EXPECTED_ROWS), start=2):
        row = line.split("\t")
        assert row == expected, (
            f"Row {i} of '{ACCESS_LOG}' was modified.\n"
            f"Expected: {expected}\n"
            f"Got:      {row}"
        )