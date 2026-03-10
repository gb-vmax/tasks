# test_final_state.py

import os
import pytest

REPORT_FILE = "/home/user/reports/traffic_report.txt"
REPORTS_DIR = "/home/user/reports"

EXPECTED_CONTENT = """\
=== TRAFFIC REPORT ===

--- Top 5 IPs by Request Count ---
9\t172.16.0.8
9\t203.0.113.5
8\t198.51.100.2
7\t10.0.0.1
7\t192.168.1.99

--- Status Code Summary ---
200: 23 requests
201: 1 requests
204: 1 requests
401: 3 requests
403: 5 requests
404: 6 requests
500: 1 requests

--- Total Bytes Transferred by Method ---
DELETE: 0 bytes
GET: 27476 bytes
HEAD: 0 bytes
POST: 1664 bytes

--- Suspicious IPs (error rate > 50%) ---
172.16.0.8 errors=9 total=9
"""


def test_reports_directory_exists():
    assert os.path.isdir(REPORTS_DIR), (
        f"Reports directory does not exist: {REPORTS_DIR}. "
        "The task requires creating this directory before writing the report."
    )


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file does not exist: {REPORT_FILE}. "
        "The task requires generating this file."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_FILE, os.R_OK), (
        f"Report file exists but is not readable: {REPORT_FILE}"
    )


def test_report_file_not_empty():
    size = os.path.getsize(REPORT_FILE)
    assert size > 0, (
        f"Report file is empty: {REPORT_FILE}. "
        "Expected a non-empty traffic report."
    )


def test_report_ends_with_newline():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        f"Report file does not end with a trailing newline: {REPORT_FILE}"
    )


def test_report_exact_content():
    with open(REPORT_FILE, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_CONTENT, (
        f"Report file content does not match expected.\n"
        f"Expected:\n{EXPECTED_CONTENT!r}\n\n"
        f"Actual:\n{actual!r}"
    )


def test_report_header():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert content.startswith("=== TRAFFIC REPORT ===\n"), (
        "Report does not start with '=== TRAFFIC REPORT ===\\n'. "
        f"Actual start: {content[:50]!r}"
    )


def test_report_top5_section_header():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "--- Top 5 IPs by Request Count ---\n" in content, (
        "Report is missing the '--- Top 5 IPs by Request Count ---' section header."
    )


def test_report_top5_ips():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    # Find the section
    start_idx = None
    for i, line in enumerate(lines):
        if line == "--- Top 5 IPs by Request Count ---":
            start_idx = i + 1
            break

    assert start_idx is not None, "Could not find '--- Top 5 IPs by Request Count ---' header."

    # Collect next 5 non-empty lines
    ip_lines = []
    for line in lines[start_idx:]:
        if line == "":
            break
        ip_lines.append(line)

    assert len(ip_lines) == 5, (
        f"Expected 5 lines in Top 5 IPs section, found {len(ip_lines)}.\n"
        f"Lines found: {ip_lines}"
    )

    expected_ip_lines = [
        "9\t172.16.0.8",
        "9\t203.0.113.5",
        "8\t198.51.100.2",
        "7\t10.0.0.1",
        "7\t192.168.1.99",
    ]

    for i, (actual_line, expected_line) in enumerate(zip(ip_lines, expected_ip_lines), start=1):
        assert actual_line == expected_line, (
            f"Top 5 IPs line {i} mismatch:\n"
            f"  Expected: {expected_line!r}\n"
            f"  Actual:   {actual_line!r}\n"
            "Note: count and IP must be separated by a TAB character."
        )


def test_report_top5_uses_tab_separator():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    start_idx = None
    for i, line in enumerate(lines):
        if line == "--- Top 5 IPs by Request Count ---":
            start_idx = i + 1
            break

    assert start_idx is not None, "Could not find Top 5 IPs section."

    ip_lines = []
    for line in lines[start_idx:]:
        if line == "":
            break
        ip_lines.append(line)

    for line in ip_lines:
        assert "\t" in line, (
            f"Top 5 IPs line does not contain a TAB separator: {line!r}\n"
            "Each line must be '<count><TAB><ip>'."
        )


def test_report_status_code_section_header():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "--- Status Code Summary ---\n" in content, (
        "Report is missing the '--- Status Code Summary ---' section header."
    )


def test_report_status_codes():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    start_idx = None
    for i, line in enumerate(lines):
        if line == "--- Status Code Summary ---":
            start_idx = i + 1
            break

    assert start_idx is not None, "Could not find '--- Status Code Summary ---' header."

    status_lines = []
    for line in lines[start_idx:]:
        if line == "":
            break
        status_lines.append(line)

    expected_status_lines = [
        "200: 23 requests",
        "201: 1 requests",
        "204: 1 requests",
        "401: 3 requests",
        "403: 5 requests",
        "404: 6 requests",
        "500: 1 requests",
    ]

    assert len(status_lines) == len(expected_status_lines), (
        f"Expected {len(expected_status_lines)} status code lines, found {len(status_lines)}.\n"
        f"Lines found: {status_lines}"
    )

    for i, (actual_line, expected_line) in enumerate(zip(status_lines, expected_status_lines), start=1):
        assert actual_line == expected_line, (
            f"Status Code Summary line {i} mismatch:\n"
            f"  Expected: {expected_line!r}\n"
            f"  Actual:   {actual_line!r}"
        )


def test_report_bytes_section_header():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "--- Total Bytes Transferred by Method ---\n" in content, (
        "Report is missing the '--- Total Bytes Transferred by Method ---' section header."
    )


def test_report_bytes_by_method():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    start_idx = None
    for i, line in enumerate(lines):
        if line == "--- Total Bytes Transferred by Method ---":
            start_idx = i + 1
            break

    assert start_idx is not None, "Could not find '--- Total Bytes Transferred by Method ---' header."

    method_lines = []
    for line in lines[start_idx:]:
        if line == "":
            break
        method_lines.append(line)

    expected_method_lines = [
        "DELETE: 0 bytes",
        "GET: 27476 bytes",
        "HEAD: 0 bytes",
        "POST: 1664 bytes",
    ]

    assert len(method_lines) == len(expected_method_lines), (
        f"Expected {len(expected_method_lines)} method lines, found {len(method_lines)}.\n"
        f"Lines found: {method_lines}"
    )

    for i, (actual_line, expected_line) in enumerate(zip(method_lines, expected_method_lines), start=1):
        assert actual_line == expected_line, (
            f"Bytes by Method line {i} mismatch:\n"
            f"  Expected: {expected_line!r}\n"
            f"  Actual:   {actual_line!r}"
        )


def test_report_suspicious_section_header():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "--- Suspicious IPs (error rate > 50%) ---\n" in content, (
        "Report is missing the '--- Suspicious IPs (error rate > 50%) ---' section header."
    )


def test_report_suspicious_ips():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    start_idx = None
    for i, line in enumerate(lines):
        if line == "--- Suspicious IPs (error rate > 50%) ---":
            start_idx = i + 1
            break

    assert start_idx is not None, "Could not find '--- Suspicious IPs (error rate > 50%) ---' header."

    suspicious_lines = []
    for line in lines[start_idx:]:
        if line == "":
            break
        suspicious_lines.append(line)

    expected_suspicious_lines = [
        "172.16.0.8 errors=9 total=9",
    ]

    assert len(suspicious_lines) == len(expected_suspicious_lines), (
        f"Expected {len(expected_suspicious_lines)} suspicious IP line(s), found {len(suspicious_lines)}.\n"
        f"Lines found: {suspicious_lines}\n"
        "Only IPs with >50% error rate AND at least 3 total requests should appear here."
    )

    for i, (actual_line, expected_line) in enumerate(zip(suspicious_lines, expected_suspicious_lines), start=1):
        assert actual_line == expected_line, (
            f"Suspicious IPs line {i} mismatch:\n"
            f"  Expected: {expected_line!r}\n"
            f"  Actual:   {actual_line!r}"
        )


def test_report_section_order():
    """Verify sections appear in the correct order."""
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    sections = [
        "=== TRAFFIC REPORT ===",
        "--- Top 5 IPs by Request Count ---",
        "--- Status Code Summary ---",
        "--- Total Bytes Transferred by Method ---",
        "--- Suspicious IPs (error rate > 50%) ---",
    ]

    positions = []
    for section in sections:
        pos = content.find(section)
        assert pos != -1, f"Section not found in report: {section!r}"
        positions.append(pos)

    for i in range(len(positions) - 1):
        assert positions[i] < positions[i + 1], (
            f"Section order is wrong: '{sections[i]}' should come before '{sections[i+1]}', "
            f"but found at positions {positions[i]} and {positions[i+1]} respectively."
        )


def test_report_blank_line_after_header():
    """Verify there is a blank line after the main header."""
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 2, "Report has fewer than 2 lines."
    assert lines[0] == "=== TRAFFIC REPORT ===", (
        f"First line should be '=== TRAFFIC REPORT ===', got: {lines[0]!r}"
    )
    assert lines[1] == "", (
        f"Second line should be blank (after header), got: {lines[1]!r}"
    )


def test_report_blank_lines_between_sections():
    """Verify blank lines separate each section."""
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    section_headers = [
        "--- Top 5 IPs by Request Count ---",
        "--- Status Code Summary ---",
        "--- Total Bytes Transferred by Method ---",
        "--- Suspicious IPs (error rate > 50%) ---",
    ]

    for header in section_headers:
        try:
            idx = lines.index(header)
        except ValueError:
            pytest.fail(f"Section header not found: {header!r}")

        # There should be a blank line before each section header (except possibly the first)
        if idx > 0:
            assert lines[idx - 1] == "", (
                f"Expected a blank line before section '{header}', "
                f"but line {idx} (0-indexed) is: {lines[idx - 1]!r}"
            )