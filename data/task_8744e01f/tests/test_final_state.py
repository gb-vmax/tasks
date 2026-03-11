# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/metrics/capacity_report.txt"

EXPECTED_CONTENT = """\
=== CAPACITY PLANNING REPORT ===

[CPU]
Average Usage: 73.6%
Peak Usage: 94.7%
Busiest Host: db01

[MEMORY]
Overall Utilization: 68.5%
Total Used: 50504 MB
Most Loaded Host: db01 (88.5%)

[DISK]
Overall Utilization: 65.1%
Total Capacity: 9700 GB
Fullest Mount: /data/postgres (90.0%)

[SUMMARY]
CPU Status: OK
Memory Status: OK
Disk Status: OK"""


def test_capacity_report_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file {REPORT_PATH} does not exist. "
        "The task requires creating this file with the capacity planning report."
    )


def test_capacity_report_not_empty():
    assert os.path.getsize(REPORT_PATH) > 0, (
        f"Report file {REPORT_PATH} is empty. "
        "The file must contain the capacity planning report."
    )


def read_report():
    with open(REPORT_PATH, "r") as f:
        return f.read()


def test_capacity_report_no_trailing_spaces():
    content = read_report()
    lines = content.splitlines()
    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} in {REPORT_PATH} has trailing whitespace: {repr(line)}"
        )


def test_capacity_report_exact_content():
    content = read_report()
    # Normalize: strip trailing newline for comparison
    actual = content.rstrip("\n")
    expected = EXPECTED_CONTENT.rstrip("\n")
    assert actual == expected, (
        f"Report content does not match expected.\n"
        f"--- EXPECTED ---\n{expected}\n"
        f"--- ACTUAL ---\n{actual}\n"
        f"--- DIFF (expected vs actual) ---\n"
        + _diff(expected, actual)
    )


def _diff(expected, actual):
    """Simple line-by-line diff for error messages."""
    exp_lines = expected.splitlines()
    act_lines = actual.splitlines()
    diff_lines = []
    max_len = max(len(exp_lines), len(act_lines))
    for i in range(max_len):
        e = exp_lines[i] if i < len(exp_lines) else "<MISSING>"
        a = act_lines[i] if i < len(act_lines) else "<MISSING>"
        if e != a:
            diff_lines.append(f"  Line {i+1}:")
            diff_lines.append(f"    Expected: {repr(e)}")
            diff_lines.append(f"    Actual:   {repr(a)}")
    return "\n".join(diff_lines) if diff_lines else "(no line-level differences found)"


def test_report_header():
    content = read_report()
    lines = content.splitlines()
    assert lines[0] == "=== CAPACITY PLANNING REPORT ===", (
        f"First line of report is incorrect.\n"
        f"Expected: '=== CAPACITY PLANNING REPORT ==='\n"
        f"Actual:   {repr(lines[0])}"
    )


def test_report_cpu_section():
    content = read_report()
    lines = content.splitlines()
    assert "[CPU]" in lines, (
        f"'[CPU]' section header not found in {REPORT_PATH}."
    )
    cpu_idx = lines.index("[CPU]")
    assert lines[cpu_idx + 1] == "Average Usage: 73.6%", (
        f"CPU Average Usage line incorrect.\n"
        f"Expected: 'Average Usage: 73.6%'\n"
        f"Actual:   {repr(lines[cpu_idx + 1])}"
    )
    assert lines[cpu_idx + 2] == "Peak Usage: 94.7%", (
        f"CPU Peak Usage line incorrect.\n"
        f"Expected: 'Peak Usage: 94.7%'\n"
        f"Actual:   {repr(lines[cpu_idx + 2])}"
    )
    assert lines[cpu_idx + 3] == "Busiest Host: db01", (
        f"CPU Busiest Host line incorrect.\n"
        f"Expected: 'Busiest Host: db01'\n"
        f"Actual:   {repr(lines[cpu_idx + 3])}"
    )


def test_report_memory_section():
    content = read_report()
    lines = content.splitlines()
    assert "[MEMORY]" in lines, (
        f"'[MEMORY]' section header not found in {REPORT_PATH}."
    )
    mem_idx = lines.index("[MEMORY]")
    assert lines[mem_idx + 1] == "Overall Utilization: 68.5%", (
        f"Memory Overall Utilization line incorrect.\n"
        f"Expected: 'Overall Utilization: 68.5%'\n"
        f"Actual:   {repr(lines[mem_idx + 1])}"
    )
    assert lines[mem_idx + 2] == "Total Used: 50504 MB", (
        f"Memory Total Used line incorrect.\n"
        f"Expected: 'Total Used: 50504 MB'\n"
        f"Actual:   {repr(lines[mem_idx + 2])}"
    )
    assert lines[mem_idx + 3] == "Most Loaded Host: db01 (88.5%)", (
        f"Memory Most Loaded Host line incorrect.\n"
        f"Expected: 'Most Loaded Host: db01 (88.5%)'\n"
        f"Actual:   {repr(lines[mem_idx + 3])}"
    )


def test_report_disk_section():
    content = read_report()
    lines = content.splitlines()
    assert "[DISK]" in lines, (
        f"'[DISK]' section header not found in {REPORT_PATH}."
    )
    disk_idx = lines.index("[DISK]")
    assert lines[disk_idx + 1] == "Overall Utilization: 65.1%", (
        f"Disk Overall Utilization line incorrect.\n"
        f"Expected: 'Overall Utilization: 65.1%'\n"
        f"Actual:   {repr(lines[disk_idx + 1])}"
    )
    assert lines[disk_idx + 2] == "Total Capacity: 9700 GB", (
        f"Disk Total Capacity line incorrect.\n"
        f"Expected: 'Total Capacity: 9700 GB'\n"
        f"Actual:   {repr(lines[disk_idx + 2])}"
    )
    assert lines[disk_idx + 3] == "Fullest Mount: /data/postgres (90.0%)", (
        f"Disk Fullest Mount line incorrect.\n"
        f"Expected: 'Fullest Mount: /data/postgres (90.0%)'\n"
        f"Actual:   {repr(lines[disk_idx + 3])}"
    )


def test_report_summary_section():
    content = read_report()
    lines = content.splitlines()
    assert "[SUMMARY]" in lines, (
        f"'[SUMMARY]' section header not found in {REPORT_PATH}."
    )
    sum_idx = lines.index("[SUMMARY]")
    assert lines[sum_idx + 1] == "CPU Status: OK", (
        f"Summary CPU Status line incorrect.\n"
        f"Expected: 'CPU Status: OK'\n"
        f"Actual:   {repr(lines[sum_idx + 1])}"
    )
    assert lines[sum_idx + 2] == "Memory Status: OK", (
        f"Summary Memory Status line incorrect.\n"
        f"Expected: 'Memory Status: OK'\n"
        f"Actual:   {repr(lines[sum_idx + 2])}"
    )
    assert lines[sum_idx + 3] == "Disk Status: OK", (
        f"Summary Disk Status line incorrect.\n"
        f"Expected: 'Disk Status: OK'\n"
        f"Actual:   {repr(lines[sum_idx + 3])}"
    )


def test_report_blank_lines_between_sections():
    content = read_report()
    lines = content.splitlines()

    # After header line (index 0), there should be a blank line at index 1
    assert lines[1] == "", (
        f"Expected blank line after header (line 2), got: {repr(lines[1])}"
    )

    # Find section indices
    section_headers = ["[CPU]", "[MEMORY]", "[DISK]", "[SUMMARY]"]
    for i, header in enumerate(section_headers):
        assert header in lines, f"Section '{header}' not found in report."

    cpu_idx = lines.index("[CPU]")
    mem_idx = lines.index("[MEMORY]")
    disk_idx = lines.index("[DISK]")
    sum_idx = lines.index("[SUMMARY]")

    # There should be a blank line before each section (except the first after header)
    # [CPU] is at cpu_idx, the line before it should be blank (already checked line 1)
    assert lines[cpu_idx - 1] == "", (
        f"Expected blank line before '[CPU]' (line {cpu_idx}), "
        f"got: {repr(lines[cpu_idx - 1])}"
    )
    assert lines[mem_idx - 1] == "", (
        f"Expected blank line before '[MEMORY]' (line {mem_idx + 1}), "
        f"got: {repr(lines[mem_idx - 1])}"
    )
    assert lines[disk_idx - 1] == "", (
        f"Expected blank line before '[DISK]' (line {disk_idx + 1}), "
        f"got: {repr(lines[disk_idx - 1])}"
    )
    assert lines[sum_idx - 1] == "", (
        f"Expected blank line before '[SUMMARY]' (line {sum_idx + 1}), "
        f"got: {repr(lines[sum_idx - 1])}"
    )


def test_report_line_count():
    content = read_report()
    # Strip trailing newline before counting
    lines = content.rstrip("\n").splitlines()
    expected_lines = EXPECTED_CONTENT.rstrip("\n").splitlines()
    assert len(lines) == len(expected_lines), (
        f"Report has {len(lines)} lines, expected {len(expected_lines)} lines.\n"
        f"Actual lines:\n" + "\n".join(f"  {i+1}: {repr(l)}" for i, l in enumerate(lines))
    )


def test_source_files_unchanged():
    """Verify the source metric files still exist and weren't deleted."""
    for path in [
        "/home/user/metrics/cpu_usage.log",
        "/home/user/metrics/memory_usage.log",
        "/home/user/metrics/disk_usage.log",
    ]:
        assert os.path.isfile(path), (
            f"Source file {path} is missing after task completion. "
            "Source files should not be deleted."
        )