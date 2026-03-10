# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/reports/audit_report.txt"
REPORTS_DIR = "/home/user/reports"
AUTH_LOG_PATH = "/home/user/logs/auth.log"

EXPECTED_CONTENT = """\
=== FAILED LOGIN AUDIT REPORT ===
Log file: /home/user/logs/auth.log
Total failed attempts: 12

Failed attempts per user (descending):
  root: 4
  alice: 3
  admin: 2
  bob: 2
  carol: 1

Users with 3 or more failed attempts (HIGH RISK):
  alice
  root"""


def test_reports_directory_exists():
    assert os.path.isdir(REPORTS_DIR), (
        f"Directory '{REPORTS_DIR}' does not exist. "
        "The student must create the reports directory as part of the task."
    )


def test_audit_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Audit report file '{REPORT_PATH}' does not exist. "
        "The student must generate the report at this path."
    )


def test_audit_report_file_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Audit report file '{REPORT_PATH}' is not readable."
    )


def test_audit_report_exact_content():
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    # Normalize: strip trailing newline for comparison if present
    actual_stripped = actual_content.rstrip("\n")
    expected_stripped = EXPECTED_CONTENT.rstrip("\n")

    assert actual_stripped == expected_stripped, (
        f"Audit report content does not match expected.\n"
        f"Expected:\n{expected_stripped!r}\n\n"
        f"Actual:\n{actual_stripped!r}"
    )


def test_audit_report_header_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, "Report file is empty."
    assert lines[0] == "=== FAILED LOGIN AUDIT REPORT ===", (
        f"First line of report is wrong.\n"
        f"  Expected: '=== FAILED LOGIN AUDIT REPORT ==='\n"
        f"  Actual:   {lines[0]!r}"
    )


def test_audit_report_log_file_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 2, "Report file has fewer than 2 lines."
    assert lines[1] == f"Log file: {AUTH_LOG_PATH}", (
        f"Second line of report is wrong.\n"
        f"  Expected: 'Log file: {AUTH_LOG_PATH}'\n"
        f"  Actual:   {lines[1]!r}"
    )


def test_audit_report_total_failed_attempts():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 3, "Report file has fewer than 3 lines."
    assert lines[2] == "Total failed attempts: 12", (
        f"Third line of report is wrong.\n"
        f"  Expected: 'Total failed attempts: 12'\n"
        f"  Actual:   {lines[2]!r}"
    )


def test_audit_report_blank_line_after_total():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 4, "Report file has fewer than 4 lines."
    assert lines[3] == "", (
        f"Line 4 of report should be blank.\n"
        f"  Actual: {lines[3]!r}"
    )


def test_audit_report_failed_attempts_section_header():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 5, "Report file has fewer than 5 lines."
    assert lines[4] == "Failed attempts per user (descending):", (
        f"Line 5 of report is wrong.\n"
        f"  Expected: 'Failed attempts per user (descending):'\n"
        f"  Actual:   {lines[4]!r}"
    )


def test_audit_report_per_user_entries():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    expected_entries = [
        "  root: 4",
        "  alice: 3",
        "  admin: 2",
        "  bob: 2",
        "  carol: 1",
    ]

    # Lines 5 through 9 (0-indexed) should be the per-user entries
    assert len(lines) >= 10, (
        f"Report file has fewer than 10 lines, cannot check per-user entries."
    )

    for i, expected in enumerate(expected_entries):
        actual = lines[5 + i]
        assert actual == expected, (
            f"Per-user entry at line {6 + i} is wrong.\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}"
        )


def test_audit_report_blank_line_before_high_risk():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    # After 5 user entries (lines 5-9), line 10 should be blank
    assert len(lines) >= 11, "Report file has fewer than 11 lines."
    assert lines[10] == "", (
        f"Line 11 of report should be blank (before HIGH RISK section).\n"
        f"  Actual: {lines[10]!r}"
    )


def test_audit_report_high_risk_section_header():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 12, "Report file has fewer than 12 lines."
    assert lines[11] == "Users with 3 or more failed attempts (HIGH RISK):", (
        f"Line 12 of report is wrong.\n"
        f"  Expected: 'Users with 3 or more failed attempts (HIGH RISK):'\n"
        f"  Actual:   {lines[11]!r}"
    )


def test_audit_report_high_risk_users():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    expected_high_risk = [
        "  alice",
        "  root",
    ]

    assert len(lines) >= 14, (
        f"Report file has fewer than 14 lines, cannot check HIGH RISK users."
    )

    for i, expected in enumerate(expected_high_risk):
        actual = lines[12 + i]
        assert actual == expected, (
            f"HIGH RISK entry at line {13 + i} is wrong.\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}"
        )


def test_audit_report_line_count():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines()
    # Remove trailing empty lines for count check
    while lines and lines[-1] == "":
        lines.pop()

    # Expected: 14 lines total (0-indexed 0..13)
    # Line 0: header
    # Line 1: log file
    # Line 2: total
    # Line 3: blank
    # Line 4: section header
    # Lines 5-9: 5 user entries
    # Line 10: blank
    # Line 11: HIGH RISK header
    # Lines 12-13: alice, root
    assert len(lines) == 14, (
        f"Report file should have 14 non-trailing-blank lines, "
        f"but has {len(lines)}.\n"
        f"Lines found:\n" + "\n".join(f"  {i}: {l!r}" for i, l in enumerate(lines))
    )


def test_auth_log_file_unchanged():
    """Verify the original auth.log file was not modified."""
    expected_lines = [
        "Mar 15 09:01:12 webserver sshd[10001]: Accepted password for deploy from 10.0.0.1 port 22 ssh2",
        "Mar 15 09:03:44 webserver sshd[10002]: Failed password for alice from 192.168.1.10 port 54321 ssh2",
        "Mar 15 09:05:21 webserver sshd[10003]: Failed password for invalid user bob from 10.0.0.5 port 43210 ssh2",
        "Mar 15 09:07:33 webserver sshd[10004]: Failed password for alice from 192.168.1.10 port 54400 ssh2",
        "Mar 15 09:08:55 webserver sshd[10005]: Failed password for root from 203.0.113.5 port 12345 ssh2",
        "Mar 15 09:10:02 webserver sshd[10006]: Failed password for root from 203.0.113.5 port 12346 ssh2",
        "Mar 15 09:11:18 webserver sshd[10007]: Failed password for alice from 192.168.1.10 port 54500 ssh2",
        "Mar 15 09:13:45 webserver sshd[10008]: Accepted password for alice from 192.168.1.10 port 54600 ssh2",
        "Mar 15 09:15:00 webserver sshd[10009]: Failed password for invalid user admin from 198.51.100.2 port 9922 ssh2",
        "Mar 15 09:16:12 webserver sshd[10010]: Failed password for root from 203.0.113.5 port 12347 ssh2",
        "Mar 15 09:18:30 webserver sshd[10011]: Failed password for invalid user bob from 10.0.0.5 port 43300 ssh2",
        "Mar 15 09:20:05 webserver sshd[10012]: Failed password for root from 203.0.113.5 port 12348 ssh2",
        "Mar 15 09:22:44 webserver sshd[10013]: Failed password for invalid user admin from 198.51.100.2 port 9923 ssh2",
        "Mar 15 09:25:10 webserver sshd[10014]: Accepted password for deploy from 10.0.0.1 port 22 ssh2",
        "Mar 15 09:27:33 webserver sshd[10015]: Failed password for carol from 172.16.0.5 port 11111 ssh2",
    ]

    assert os.path.isfile(AUTH_LOG_PATH), (
        f"Auth log file '{AUTH_LOG_PATH}' no longer exists after the task."
    )

    with open(AUTH_LOG_PATH, "r") as f:
        actual_lines = [line.rstrip("\n") for line in f.readlines()]

    while actual_lines and actual_lines[-1] == "":
        actual_lines.pop()

    assert len(actual_lines) == len(expected_lines), (
        f"Auth log file has {len(actual_lines)} lines, expected {len(expected_lines)}. "
        "The log file should not have been modified."
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, expected_lines), start=1):
        assert actual == expected, (
            f"Auth log line {i} was modified.\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}"
        )