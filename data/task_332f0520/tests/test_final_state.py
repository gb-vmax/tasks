# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/capacity/report.txt"

EXPECTED_CONTENT = """\
=== Capacity Report ===
Hosts analyzed: 8
CPU avg: 65.8%
MEM avg: 67.7%
DISK avg: 46.4%
High CPU hosts (>80%): cache02, db01, web02
High MEM hosts (>80%): db01, web03, worker01"""


def get_report_lines():
    """Helper to read and return stripped lines from the report file."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    return content


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file {REPORT_PATH} does not exist. "
        "The task requires producing this file."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file {REPORT_PATH} exists but is not readable."
    )


def test_report_file_not_empty():
    size = os.path.getsize(REPORT_PATH)
    assert size > 0, (
        f"Report file {REPORT_PATH} is empty. It must contain the capacity report."
    )


def test_report_header_line():
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert len(lines) >= 1, (
        f"Report file {REPORT_PATH} has no lines."
    )
    assert lines[0] == "=== Capacity Report ===", (
        f"First line of report is wrong.\n"
        f"Expected: '=== Capacity Report ==='\n"
        f"Got:      {lines[0]!r}"
    )


def test_report_hosts_analyzed_line():
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert len(lines) >= 2, (
        f"Report file {REPORT_PATH} has fewer than 2 lines."
    )
    assert lines[1] == "Hosts analyzed: 8", (
        f"Second line of report is wrong.\n"
        f"Expected: 'Hosts analyzed: 8'\n"
        f"Got:      {lines[1]!r}"
    )


def test_report_cpu_avg_line():
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert len(lines) >= 3, (
        f"Report file {REPORT_PATH} has fewer than 3 lines."
    )
    assert lines[2] == "CPU avg: 65.8%", (
        f"Third line of report is wrong.\n"
        f"Expected: 'CPU avg: 65.8%'\n"
        f"Got:      {lines[2]!r}"
    )


def test_report_mem_avg_line():
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert len(lines) >= 4, (
        f"Report file {REPORT_PATH} has fewer than 4 lines."
    )
    assert lines[3] == "MEM avg: 67.7%", (
        f"Fourth line of report is wrong.\n"
        f"Expected: 'MEM avg: 67.7%'\n"
        f"Got:      {lines[3]!r}"
    )


def test_report_disk_avg_line():
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert len(lines) >= 5, (
        f"Report file {REPORT_PATH} has fewer than 5 lines."
    )
    assert lines[4] == "DISK avg: 46.4%", (
        f"Fifth line of report is wrong.\n"
        f"Expected: 'DISK avg: 46.4%'\n"
        f"Got:      {lines[4]!r}"
    )


def test_report_high_cpu_hosts_line():
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert len(lines) >= 6, (
        f"Report file {REPORT_PATH} has fewer than 6 lines."
    )
    assert lines[5] == "High CPU hosts (>80%): cache02, db01, web02", (
        f"Sixth line of report is wrong.\n"
        f"Expected: 'High CPU hosts (>80%): cache02, db01, web02'\n"
        f"Got:      {lines[5]!r}\n"
        "Note: hostnames must be sorted alphabetically and joined with ', '"
    )


def test_report_high_mem_hosts_line():
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert len(lines) >= 7, (
        f"Report file {REPORT_PATH} has fewer than 7 lines."
    )
    assert lines[6] == "High MEM hosts (>80%): db01, web03, worker01", (
        f"Seventh line of report is wrong.\n"
        f"Expected: 'High MEM hosts (>80%): db01, web03, worker01'\n"
        f"Got:      {lines[6]!r}\n"
        "Note: hostnames must be sorted alphabetically and joined with ', '"
    )


def test_report_exact_line_count():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    # Strip trailing newline(s) for counting
    lines = content.rstrip("\n").splitlines()
    assert len(lines) == 7, (
        f"Report file {REPORT_PATH} has {len(lines)} non-empty lines, expected exactly 7.\n"
        f"Content:\n{content!r}"
    )


def test_report_no_extra_blank_lines():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").splitlines()
    for i, line in enumerate(lines):
        assert line.strip() != "" or False, (
            f"Report file {REPORT_PATH} has an unexpected blank line at line {i+1}.\n"
            f"Content:\n{content!r}"
        )
        # Actually check for blank lines explicitly
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"Report file {REPORT_PATH} has blank lines at positions: {blank_lines}.\n"
        f"No extra blank lines are allowed.\n"
        f"Content:\n{content!r}"
    )


def test_report_no_leading_or_trailing_spaces_per_line():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").splitlines()
    for i, line in enumerate(lines):
        assert line == line.strip() or line.startswith("=== "), (
            f"Line {i+1} has unexpected leading/trailing whitespace: {line!r}"
        )
        # More precise check
        assert line == line.rstrip(), (
            f"Line {i+1} has trailing whitespace: {line!r}"
        )


def test_report_full_content_matches_expected():
    """Final comprehensive check: the entire file content matches expected."""
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    # Normalize: strip trailing newline for comparison (a single trailing newline is acceptable)
    actual_normalized = actual_content.rstrip("\n")
    expected_normalized = EXPECTED_CONTENT.rstrip("\n")

    assert actual_normalized == expected_normalized, (
        f"Report file {REPORT_PATH} content does not match expected.\n\n"
        f"Expected content:\n{EXPECTED_CONTENT!r}\n\n"
        f"Actual content:\n{actual_content!r}\n\n"
        "Check each line carefully for spacing, punctuation, and values."
    )