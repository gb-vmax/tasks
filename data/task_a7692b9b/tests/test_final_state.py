# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/capacity/usage_report.txt"
CSV_PATH = "/home/user/capacity/server_metrics.csv"

EXPECTED_CONTENT = """\
=== SERVER CAPACITY REPORT ===
Server: srv-01
Report timezone: America/New_York

--- CPU ANALYSIS ---
Overall average CPU: 52.34%
Peak CPU hour: 2024-03-10 00:00 EST
High CPU intervals (>75%): 4

--- MEMORY ANALYSIS ---
Overall average memory: 68.84%
Peak memory hour: 2024-03-10 01:00 EST
High memory intervals (>80%): 4

--- DST NOTE ---
First EDT interval: 2024-03-10 03:00 EDT
"""


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The task requires writing the report to this path."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file '{REPORT_PATH}' is not readable."
    )


def test_report_exact_content():
    with open(REPORT_PATH, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_CONTENT, (
        f"Content of '{REPORT_PATH}' does not match expected.\n"
        f"Expected repr:\n{repr(EXPECTED_CONTENT)}\n\n"
        f"Actual repr:\n{repr(actual)}"
    )


def test_report_ends_with_newline():
    with open(REPORT_PATH, "r") as f:
        actual = f.read()
    assert actual.endswith("\n"), (
        f"Report file '{REPORT_PATH}' must end with a newline character. "
        f"Last 10 chars repr: {repr(actual[-10:])}"
    )


def test_report_no_trailing_spaces():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} in '{REPORT_PATH}' has trailing whitespace: {repr(line)}"
        )


def test_report_line_count():
    with open(REPORT_PATH, "r") as f:
        actual = f.read()
    lines = actual.split("\n")
    # The expected content has 17 lines of text + 1 empty string after final newline = 18 parts
    # Let's count non-empty lines and the structure
    expected_lines = EXPECTED_CONTENT.split("\n")
    actual_lines = actual.split("\n")
    assert len(actual_lines) == len(expected_lines), (
        f"Report file '{REPORT_PATH}' has {len(actual_lines)} lines (when split by '\\n') "
        f"but expected {len(expected_lines)} lines.\n"
        f"Expected split repr: {expected_lines}\n"
        f"Actual split repr: {actual_lines}"
    )


def test_report_header_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[0] == "=== SERVER CAPACITY REPORT ===", (
        f"Line 1 of report is wrong.\nExpected: '=== SERVER CAPACITY REPORT ==='\nActual: {repr(lines[0])}"
    )


def test_report_server_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[1] == "Server: srv-01", (
        f"Line 2 of report is wrong.\nExpected: 'Server: srv-01'\nActual: {repr(lines[1])}"
    )


def test_report_timezone_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[2] == "Report timezone: America/New_York", (
        f"Line 3 of report is wrong.\nExpected: 'Report timezone: America/New_York'\nActual: {repr(lines[2])}"
    )


def test_report_blank_line_after_header():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[3] == "", (
        f"Line 4 of report should be blank.\nActual: {repr(lines[3])}"
    )


def test_report_cpu_section_header():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[4] == "--- CPU ANALYSIS ---", (
        f"Line 5 of report is wrong.\nExpected: '--- CPU ANALYSIS ---'\nActual: {repr(lines[4])}"
    )


def test_report_overall_average_cpu():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[5] == "Overall average CPU: 52.34%", (
        f"Overall average CPU line is wrong.\nExpected: 'Overall average CPU: 52.34%'\nActual: {repr(lines[5])}"
    )


def test_report_peak_cpu_hour():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[6] == "Peak CPU hour: 2024-03-10 00:00 EST", (
        f"Peak CPU hour line is wrong.\nExpected: 'Peak CPU hour: 2024-03-10 00:00 EST'\nActual: {repr(lines[6])}"
    )


def test_report_high_cpu_intervals():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[7] == "High CPU intervals (>75%): 4", (
        f"High CPU intervals line is wrong.\nExpected: 'High CPU intervals (>75%): 4'\nActual: {repr(lines[7])}"
    )


def test_report_blank_line_before_memory_section():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[8] == "", (
        f"Line 9 of report should be blank.\nActual: {repr(lines[8])}"
    )


def test_report_memory_section_header():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[9] == "--- MEMORY ANALYSIS ---", (
        f"Line 10 of report is wrong.\nExpected: '--- MEMORY ANALYSIS ---'\nActual: {repr(lines[9])}"
    )


def test_report_overall_average_memory():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[10] == "Overall average memory: 68.84%", (
        f"Overall average memory line is wrong.\nExpected: 'Overall average memory: 68.84%'\nActual: {repr(lines[10])}"
    )


def test_report_peak_memory_hour():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[11] == "Peak memory hour: 2024-03-10 01:00 EST", (
        f"Peak memory hour line is wrong.\nExpected: 'Peak memory hour: 2024-03-10 01:00 EST'\nActual: {repr(lines[11])}"
    )


def test_report_high_memory_intervals():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[12] == "High memory intervals (>80%): 4", (
        f"High memory intervals line is wrong.\nExpected: 'High memory intervals (>80%): 4'\nActual: {repr(lines[12])}"
    )


def test_report_blank_line_before_dst_section():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[13] == "", (
        f"Line 14 of report should be blank.\nActual: {repr(lines[13])}"
    )


def test_report_dst_section_header():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[14] == "--- DST NOTE ---", (
        f"Line 15 of report is wrong.\nExpected: '--- DST NOTE ---'\nActual: {repr(lines[14])}"
    )


def test_report_first_edt_interval():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[15] == "First EDT interval: 2024-03-10 03:00 EDT", (
        f"First EDT interval line is wrong.\nExpected: 'First EDT interval: 2024-03-10 03:00 EDT'\nActual: {repr(lines[15])}"
    )


def test_report_final_newline_only():
    """The file should end with exactly one newline after the last content line."""
    with open(REPORT_PATH, "r") as f:
        actual = f.read()
    assert not actual.endswith("\n\n"), (
        f"Report file '{REPORT_PATH}' ends with more than one newline. "
        f"Last 5 chars repr: {repr(actual[-5:])}"
    )
    assert actual.endswith("\n"), (
        f"Report file '{REPORT_PATH}' must end with a newline."
    )


def test_csv_file_still_intact():
    """Ensure the original CSV file was not modified."""
    assert os.path.isfile(CSV_PATH), (
        f"Original CSV file '{CSV_PATH}' is missing after task completion."
    )
    with open(CSV_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    assert len(lines) == 17, (
        f"CSV file '{CSV_PATH}' should have 17 lines (1 header + 16 data rows), "
        f"but found {len(lines)}."
    )
    assert lines[0] == "timestamp,cpu_percent,mem_percent,server_id", (
        f"CSV header has been modified. Found: {repr(lines[0])}"
    )