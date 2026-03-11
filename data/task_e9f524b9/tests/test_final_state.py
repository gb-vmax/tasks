# test_final_state.py

import os
import pytest

CREDENTIALS_DIR = "/home/user/credentials"
ROTATION_REPORT = os.path.join(CREDENTIALS_DIR, "rotation_report.tsv")
ROTATION_SUMMARY = os.path.join(CREDENTIALS_DIR, "rotation_summary.txt")


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def read_lines(path):
    with open(path, "r") as f:
        return f.read().splitlines()


# ---------------------------------------------------------------------------
# rotation_report.tsv existence & basic structure
# ---------------------------------------------------------------------------

def test_rotation_report_exists():
    assert os.path.isfile(ROTATION_REPORT), (
        f"Output file {ROTATION_REPORT} does not exist. "
        "The task requires creating this file."
    )


def test_rotation_report_line_count():
    lines = read_lines(ROTATION_REPORT)
    assert len(lines) == 10, (
        f"{ROTATION_REPORT} should have exactly 10 lines (1 header + 9 data rows), "
        f"but found {len(lines)} lines."
    )


def test_rotation_report_header():
    lines = read_lines(ROTATION_REPORT)
    expected_header = "service\thost\tusername\tsecret\tport"
    assert lines[0] == expected_header, (
        f"Header of {ROTATION_REPORT} is wrong.\n"
        f"Expected: {repr(expected_header)}\n"
        f"Got:      {repr(lines[0])}"
    )


# ---------------------------------------------------------------------------
# rotation_report.tsv — exact data rows
# ---------------------------------------------------------------------------

EXPECTED_DATA_ROWS = [
    # DB rows
    "postgres\tdb1.internal\talice\ts3cr3tDB1\t5432",
    "postgres\tdb2.internal\tbob\thunter2\t5432",
    "mysql\tdb3.internal\tcarol\tp@ssw0rd\t3306",
    # API rows
    "payments\tapi.payments.io\tsvc_pay\ttok_abc123\tN/A",
    "analytics\tapi.analytics.io\tsvc_ana\ttok_xyz789\tN/A",
    "notifications\tapi.notify.io\tsvc_not\ttok_def456\tN/A",
    # SSH rows
    "bastion\tjump1.internal\tdeploy\tSHA256:aabbcc1\t22",
    "bastion\tjump2.internal\tdeploy\tSHA256:ddeeff2\t2222",
    "automation\tworker1.internal\tansible\tSHA256:112233a\t22",
]


def test_rotation_report_db_rows():
    lines = read_lines(ROTATION_REPORT)
    data_rows = lines[1:]
    for i, (expected, got) in enumerate(zip(EXPECTED_DATA_ROWS[:3], data_rows[:3]), start=2):
        assert got == expected, (
            f"{ROTATION_REPORT} DB row at line {i} is wrong.\n"
            f"Expected: {repr(expected)}\n"
            f"Got:      {repr(got)}"
        )


def test_rotation_report_api_rows():
    lines = read_lines(ROTATION_REPORT)
    data_rows = lines[1:]
    for i, (expected, got) in enumerate(zip(EXPECTED_DATA_ROWS[3:6], data_rows[3:6]), start=5):
        assert got == expected, (
            f"{ROTATION_REPORT} API row at line {i} is wrong.\n"
            f"Expected: {repr(expected)}\n"
            f"Got:      {repr(got)}"
        )


def test_rotation_report_ssh_rows():
    lines = read_lines(ROTATION_REPORT)
    data_rows = lines[1:]
    for i, (expected, got) in enumerate(zip(EXPECTED_DATA_ROWS[6:], data_rows[6:]), start=8):
        assert got == expected, (
            f"{ROTATION_REPORT} SSH row at line {i} is wrong.\n"
            f"Expected: {repr(expected)}\n"
            f"Got:      {repr(got)}"
        )


def test_rotation_report_all_rows_exact():
    lines = read_lines(ROTATION_REPORT)
    data_rows = lines[1:]
    assert data_rows == EXPECTED_DATA_ROWS, (
        f"{ROTATION_REPORT} data rows do not match expected.\n"
        f"Expected rows:\n" + "\n".join(repr(r) for r in EXPECTED_DATA_ROWS) + "\n"
        f"Got rows:\n" + "\n".join(repr(r) for r in data_rows)
    )


def test_rotation_report_uses_tab_delimiter():
    lines = read_lines(ROTATION_REPORT)
    for i, line in enumerate(lines, start=1):
        parts = line.split("\t")
        assert len(parts) == 5, (
            f"{ROTATION_REPORT} line {i} does not have exactly 5 tab-separated columns.\n"
            f"Line: {repr(line)}\n"
            f"Columns found: {len(parts)}"
        )


def test_rotation_report_api_rows_port_is_na():
    lines = read_lines(ROTATION_REPORT)
    data_rows = lines[1:]
    api_rows = data_rows[3:6]
    for i, row in enumerate(api_rows, start=5):
        parts = row.split("\t")
        assert parts[4] == "N/A", (
            f"{ROTATION_REPORT} API row at line {i}: port column should be 'N/A', "
            f"got {repr(parts[4])}.\nFull row: {repr(row)}"
        )


# ---------------------------------------------------------------------------
# rotation_summary.txt existence & structure
# ---------------------------------------------------------------------------

def test_rotation_summary_exists():
    assert os.path.isfile(ROTATION_SUMMARY), (
        f"Output file {ROTATION_SUMMARY} does not exist. "
        "The task requires creating this summary file."
    )


def test_rotation_summary_line_count():
    lines = read_lines(ROTATION_SUMMARY)
    assert len(lines) == 5, (
        f"{ROTATION_SUMMARY} should have exactly 5 lines, "
        f"but found {len(lines)} lines.\n"
        f"Content:\n" + "\n".join(repr(l) for l in lines)
    )


# ---------------------------------------------------------------------------
# rotation_summary.txt — exact content
# ---------------------------------------------------------------------------

EXPECTED_SUMMARY_LINES = [
    "Total credentials: 9",
    "DB credentials: 3",
    "API credentials: 3",
    "SSH credentials: 3",
    "Services: analytics, automation, bastion, mysql, notifications, payments, postgres",
]


def test_rotation_summary_total_credentials():
    lines = read_lines(ROTATION_SUMMARY)
    assert lines[0] == EXPECTED_SUMMARY_LINES[0], (
        f"{ROTATION_SUMMARY} line 1 (Total credentials) is wrong.\n"
        f"Expected: {repr(EXPECTED_SUMMARY_LINES[0])}\n"
        f"Got:      {repr(lines[0])}"
    )


def test_rotation_summary_db_credentials():
    lines = read_lines(ROTATION_SUMMARY)
    assert lines[1] == EXPECTED_SUMMARY_LINES[1], (
        f"{ROTATION_SUMMARY} line 2 (DB credentials) is wrong.\n"
        f"Expected: {repr(EXPECTED_SUMMARY_LINES[1])}\n"
        f"Got:      {repr(lines[1])}"
    )


def test_rotation_summary_api_credentials():
    lines = read_lines(ROTATION_SUMMARY)
    assert lines[2] == EXPECTED_SUMMARY_LINES[2], (
        f"{ROTATION_SUMMARY} line 3 (API credentials) is wrong.\n"
        f"Expected: {repr(EXPECTED_SUMMARY_LINES[2])}\n"
        f"Got:      {repr(lines[2])}"
    )


def test_rotation_summary_ssh_credentials():
    lines = read_lines(ROTATION_SUMMARY)
    assert lines[3] == EXPECTED_SUMMARY_LINES[3], (
        f"{ROTATION_SUMMARY} line 4 (SSH credentials) is wrong.\n"
        f"Expected: {repr(EXPECTED_SUMMARY_LINES[3])}\n"
        f"Got:      {repr(lines[3])}"
    )


def test_rotation_summary_services():
    lines = read_lines(ROTATION_SUMMARY)
    assert lines[4] == EXPECTED_SUMMARY_LINES[4], (
        f"{ROTATION_SUMMARY} line 5 (Services) is wrong.\n"
        f"Expected: {repr(EXPECTED_SUMMARY_LINES[4])}\n"
        f"Got:      {repr(lines[4])}"
    )


def test_rotation_summary_exact_content():
    lines = read_lines(ROTATION_SUMMARY)
    assert lines == EXPECTED_SUMMARY_LINES, (
        f"{ROTATION_SUMMARY} content does not match expected.\n"
        f"Expected:\n" + "\n".join(repr(l) for l in EXPECTED_SUMMARY_LINES) + "\n"
        f"Got:\n" + "\n".join(repr(l) for l in lines)
    )


# ---------------------------------------------------------------------------
# Cross-validation: summary counts match report contents
# ---------------------------------------------------------------------------

def test_summary_counts_match_report():
    report_lines = read_lines(ROTATION_REPORT)
    data_rows = report_lines[1:]  # skip header

    summary_lines = read_lines(ROTATION_SUMMARY)

    total = len(data_rows)
    assert summary_lines[0] == f"Total credentials: {total}", (
        f"Total credentials in summary ({summary_lines[0]}) does not match "
        f"actual data rows in report ({total})."
    )


def test_summary_services_match_report():
    report_lines = read_lines(ROTATION_REPORT)
    data_rows = report_lines[1:]

    services = sorted(set(row.split("\t")[0] for row in data_rows))
    expected_services_line = "Services: " + ", ".join(services)

    summary_lines = read_lines(ROTATION_SUMMARY)
    assert summary_lines[4] == expected_services_line, (
        f"Services line in summary does not match unique services from report.\n"
        f"Expected: {repr(expected_services_line)}\n"
        f"Got:      {repr(summary_lines[4])}"
    )


# ---------------------------------------------------------------------------
# Input files are untouched
# ---------------------------------------------------------------------------

def test_input_files_still_exist():
    for fname in ("db_creds.tsv", "api_creds.tsv", "ssh_creds.tsv"):
        path = os.path.join(CREDENTIALS_DIR, fname)
        assert os.path.isfile(path), (
            f"Input file {path} is missing after the task. "
            "Input files must not be deleted."
        )


def test_db_creds_unchanged():
    path = os.path.join(CREDENTIALS_DIR, "db_creds.tsv")
    lines = read_lines(path)
    expected = [
        "password\tusername\thost\tport\tservice",
        "s3cr3tDB1\talice\tdb1.internal\t5432\tpostgres",
        "hunter2\tbob\tdb2.internal\t5432\tpostgres",
        "p@ssw0rd\tcarol\tdb3.internal\t3306\tmysql",
    ]
    assert lines == expected, (
        f"{path} has been modified.\n"
        f"Expected:\n" + "\n".join(repr(l) for l in expected) + "\n"
        f"Got:\n" + "\n".join(repr(l) for l in lines)
    )


def test_api_creds_unchanged():
    path = os.path.join(CREDENTIALS_DIR, "api_creds.tsv")
    lines = read_lines(path)
    expected = [
        "service\thost\tusername\tapi_key\texpiry",
        "payments\tapi.payments.io\tsvc_pay\ttok_abc123\t2024-12-31",
        "analytics\tapi.analytics.io\tsvc_ana\ttok_xyz789\t2024-11-30",
        "notifications\tapi.notify.io\tsvc_not\ttok_def456\t2025-01-15",
    ]
    assert lines == expected, (
        f"{path} has been modified.\n"
        f"Expected:\n" + "\n".join(repr(l) for l in expected) + "\n"
        f"Got:\n" + "\n".join(repr(l) for l in lines)
    )


def test_ssh_creds_unchanged():
    path = os.path.join(CREDENTIALS_DIR, "ssh_creds.tsv")
    lines = read_lines(path)
    expected = [
        "host\tusername\tkey_fingerprint\tport\tservice",
        "jump1.internal\tdeploy\tSHA256:aabbcc1\t22\tbastion",
        "jump2.internal\tdeploy\tSHA256:ddeeff2\t2222\tbastion",
        "worker1.internal\tansible\tSHA256:112233a\t22\tautomation",
    ]
    assert lines == expected, (
        f"{path} has been modified.\n"
        f"Expected:\n" + "\n".join(repr(l) for l in expected) + "\n"
        f"Got:\n" + "\n".join(repr(l) for l in lines)
    )