# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/logs/error_report.txt"

EXPECTED_REPORT = """\
=== SERVICE ERROR REPORT ===

[ERROR COUNTS BY SERVICE]
auth: 8 errors (61.5%)
inventory: 6 errors (75.0%)
payments: 6 errors (60.0%)
gateway: 5 errors (55.6%)

[TOP ERROR CODES]
5001: 4 occurrences
6002: 3 occurrences
7001: 3 occurrences

[RESPONSE TIME BY REGION]
eu-central: avg 397ms, max 670ms
us-east: avg 414ms, max 880ms
us-west: avg 729ms, max 1200ms

[HOURLY ERROR RATE]
08:00 - 3 errors
09:00 - 3 errors
10:00 - 3 errors
11:00 - 5 errors
12:00 - 2 errors
13:00 - 3 errors
14:00 - 3 errors
15:00 - 3 errors

[CRITICAL SERVICES]
auth - 3 unique error codes, worst code: 5001
gateway - 3 unique error codes, worst code: 7001
inventory - 3 unique error codes, worst code: 8001
payments - 3 unique error codes, worst code: 6002"""


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The analysis script must create this file."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file '{REPORT_PATH}' is not readable."
    )


def test_report_file_not_empty():
    size = os.path.getsize(REPORT_PATH)
    assert size > 0, (
        f"Report file '{REPORT_PATH}' is empty. It must contain the analysis report."
    )


def test_report_exact_content():
    with open(REPORT_PATH, "r") as f:
        actual = f.read()

    # Strip trailing newline(s) for comparison, but preserve internal structure
    actual_stripped = actual.rstrip("\n")
    expected_stripped = EXPECTED_REPORT.rstrip("\n")

    assert actual_stripped == expected_stripped, (
        f"Report content does not match expected.\n\n"
        f"=== EXPECTED ===\n{expected_stripped}\n\n"
        f"=== ACTUAL ===\n{actual_stripped}\n\n"
        f"=== DIFF (line by line) ===\n"
        + _line_diff(expected_stripped, actual_stripped)
    )


def _line_diff(expected: str, actual: str) -> str:
    """Helper to produce a simple line-by-line diff for failure messages."""
    exp_lines = expected.splitlines()
    act_lines = actual.splitlines()
    diff_lines = []
    max_lines = max(len(exp_lines), len(act_lines))
    for i in range(max_lines):
        exp_line = exp_lines[i] if i < len(exp_lines) else "<MISSING>"
        act_line = act_lines[i] if i < len(act_lines) else "<MISSING>"
        if exp_line != act_line:
            diff_lines.append(f"  Line {i+1}:")
            diff_lines.append(f"    Expected: {exp_line!r}")
            diff_lines.append(f"    Actual:   {act_line!r}")
    return "\n".join(diff_lines) if diff_lines else "(no differences found in line-by-line check)"


def test_report_header():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert lines[0] == "=== SERVICE ERROR REPORT ===", (
        f"First line of report must be '=== SERVICE ERROR REPORT ===' but got: {lines[0]!r}"
    )


def test_report_section_error_counts_by_service():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    expected_section = (
        "[ERROR COUNTS BY SERVICE]\n"
        "auth: 8 errors (61.5%)\n"
        "inventory: 6 errors (75.0%)\n"
        "payments: 6 errors (60.0%)\n"
        "gateway: 5 errors (55.6%)"
    )
    assert expected_section in content, (
        f"[ERROR COUNTS BY SERVICE] section is missing or incorrect.\n"
        f"Expected to find:\n{expected_section}\n\n"
        f"Actual report content:\n{content}"
    )


def test_report_section_top_error_codes():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    expected_section = (
        "[TOP ERROR CODES]\n"
        "5001: 4 occurrences\n"
        "6002: 3 occurrences\n"
        "7001: 3 occurrences"
    )
    assert expected_section in content, (
        f"[TOP ERROR CODES] section is missing or incorrect.\n"
        f"Expected to find:\n{expected_section}\n\n"
        f"Actual report content:\n{content}"
    )


def test_report_section_response_time_by_region():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    expected_section = (
        "[RESPONSE TIME BY REGION]\n"
        "eu-central: avg 397ms, max 670ms\n"
        "us-east: avg 414ms, max 880ms\n"
        "us-west: avg 729ms, max 1200ms"
    )
    assert expected_section in content, (
        f"[RESPONSE TIME BY REGION] section is missing or incorrect.\n"
        f"Expected to find:\n{expected_section}\n\n"
        f"Actual report content:\n{content}"
    )


def test_report_section_hourly_error_rate():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    expected_section = (
        "[HOURLY ERROR RATE]\n"
        "08:00 - 3 errors\n"
        "09:00 - 3 errors\n"
        "10:00 - 3 errors\n"
        "11:00 - 5 errors\n"
        "12:00 - 2 errors\n"
        "13:00 - 3 errors\n"
        "14:00 - 3 errors\n"
        "15:00 - 3 errors"
    )
    assert expected_section in content, (
        f"[HOURLY ERROR RATE] section is missing or incorrect.\n"
        f"Expected to find:\n{expected_section}\n\n"
        f"Actual report content:\n{content}"
    )


def test_report_section_critical_services():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    expected_section = (
        "[CRITICAL SERVICES]\n"
        "auth - 3 unique error codes, worst code: 5001\n"
        "gateway - 3 unique error codes, worst code: 7001\n"
        "inventory - 3 unique error codes, worst code: 8001\n"
        "payments - 3 unique error codes, worst code: 6002"
    )
    assert expected_section in content, (
        f"[CRITICAL SERVICES] section is missing or incorrect.\n"
        f"Expected to find:\n{expected_section}\n\n"
        f"Actual report content:\n{content}"
    )


def test_report_no_trailing_spaces():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    trailing_space_lines = [
        (i + 1, repr(line)) for i, line in enumerate(lines) if line != line.rstrip(" ")
    ]
    assert not trailing_space_lines, (
        f"Report has trailing spaces on the following lines:\n"
        + "\n".join(f"  Line {ln}: {lr}" for ln, lr in trailing_space_lines)
    )


def test_report_sections_present():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    required_sections = [
        "[ERROR COUNTS BY SERVICE]",
        "[TOP ERROR CODES]",
        "[RESPONSE TIME BY REGION]",
        "[HOURLY ERROR RATE]",
        "[CRITICAL SERVICES]",
    ]
    for section in required_sections:
        assert section in content, (
            f"Required section '{section}' is missing from the report.\n"
            f"Actual report content:\n{content}"
        )


def test_report_section_order():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    sections = [
        "[ERROR COUNTS BY SERVICE]",
        "[TOP ERROR CODES]",
        "[RESPONSE TIME BY REGION]",
        "[HOURLY ERROR RATE]",
        "[CRITICAL SERVICES]",
    ]
    positions = []
    for section in sections:
        pos = content.find(section)
        assert pos != -1, f"Section '{section}' not found in report."
        positions.append((pos, section))

    for i in range(len(positions) - 1):
        assert positions[i][0] < positions[i + 1][0], (
            f"Section order is wrong: '{positions[i][1]}' should come before "
            f"'{positions[i+1][1]}' but positions are {positions[i][0]} and {positions[i+1][0]}."
        )