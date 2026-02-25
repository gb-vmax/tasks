# test_final_state.py

import os
import re
import pytest

REPORT_PATH = "/home/user/capacity_report.txt"


def read_report_lines():
    """Read lines from the report file, stripping trailing newlines only."""
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    return [line.rstrip('\n') for line in lines]


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Expected report file {REPORT_PATH} was not found. "
        "Please ensure the file is created at the correct absolute path."
    )


def test_report_file_permissions():
    parent_dir = os.path.dirname(REPORT_PATH)
    assert os.access(parent_dir, os.W_OK), (
        f"Directory {parent_dir} is not writable by the user. "
        "Ensure the user has sufficient permissions to write the report file."
    )
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file {REPORT_PATH} is not readable. "
        "Check file permissions."
    )


def test_report_format_and_content():
    """
    Validate the exact format and value ranges of the report file.
    """
    lines = read_report_lines()
    assert len(lines) == 2, (
        f"Report file must contain exactly 2 lines, found {len(lines)} line(s). "
        "Do not include any extra lines or blank lines."
    )

    cpu_line, mem_line = lines

    # Validate CPU Usage line
    cpu_pattern = r"^CPU Usage: (\d+)%$"
    cpu_match = re.fullmatch(cpu_pattern, cpu_line)
    assert cpu_match, (
        f"First line must be in the format 'CPU Usage: X%', "
        f"but got: '{cpu_line}'"
    )
    cpu_percent = int(cpu_match.group(1))
    assert 0 <= cpu_percent <= 100, (
        f"CPU percentage {cpu_percent}% is out of range (0-100)."
    )

    # Validate Memory Usage line
    mem_pattern = r"^Memory Usage: (\d+)% \((\d+) MiB / (\d+) MiB\)$"
    mem_match = re.fullmatch(mem_pattern, mem_line)
    assert mem_match, (
        f"Second line must be in the format "
        "'Memory Usage: Y% (Z MiB / W MiB)', "
        f"but got: '{mem_line}'"
    )
    mem_percent = int(mem_match.group(1))
    mem_used = int(mem_match.group(2))
    mem_total = int(mem_match.group(3))

    assert 0 <= mem_percent <= 100, (
        f"Memory usage percentage {mem_percent}% is out of range (0-100)."
    )
    assert mem_total > 0, (
        f"Total memory (W) must be positive, got {mem_total} MiB."
    )
    assert 0 <= mem_used <= mem_total, (
        f"Used memory (Z) {mem_used} MiB is out of range (0-{mem_total} MiB)."
    )

    # Recompute percentage and compare to reported value (allow max 1% rounding difference)
    if mem_total > 0:
        calculated_percent = round((mem_used / mem_total) * 100)
        assert abs(calculated_percent - mem_percent) <= 1, (
            f"Reported memory usage {mem_percent}% does not match calculated value "
            f"{calculated_percent}% (from {mem_used} / {mem_total})."
        )

def test_report_no_extra_whitespace():
    """
    Ensure lines have no leading/trailing spaces and no extra blank lines.
    """
    with open(REPORT_PATH, "r") as f:
        raw = f.read()

    # File should end with a single newline, not multiple
    assert raw.endswith('\n'), (
        "Report file must end with a single newline character."
    )

    lines = raw.splitlines()
    for idx, line in enumerate(lines):
        assert line == line.strip(), (
            f"Line {idx+1} in report has leading or trailing spaces: '{line}'"
        )