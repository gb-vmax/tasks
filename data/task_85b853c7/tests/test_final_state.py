# test_final_state.py

import os
import subprocess
import pytest


REPORT_FILE = "/home/user/disk_report.txt"
BASE_DIR = "/home/user/server_data"

EXPECTED_HEADER = "Disk Usage Report: /home/user/server_data"
EXPECTED_SEPARATOR = "=" * 42

# Expected data lines based on truth values (sorted largest first, >= 50K)
# backups: 200K, logs: 100K, cache: 64K
# tmp (8K) and sessions (32K) are excluded
EXPECTED_DATA_LINES = [
    f"200K\t/home/user/server_data/backups",
    f"100K\t/home/user/server_data/logs",
    f"64K\t/home/user/server_data/cache",
]

EXPECTED_LINES = [EXPECTED_HEADER, EXPECTED_SEPARATOR] + EXPECTED_DATA_LINES


def read_report_lines():
    """Read the report file and return lines stripped of trailing newline only."""
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    # Split into lines; handle optional trailing newline
    if content.endswith("\n"):
        content = content[:-1]
    return content.split("\n")


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file '{REPORT_FILE}' does not exist. "
        "The task requires generating this file."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_FILE, os.R_OK), (
        f"Report file '{REPORT_FILE}' exists but is not readable."
    )


def test_report_total_line_count():
    lines = read_report_lines()
    expected_count = len(EXPECTED_LINES)  # 5 lines
    assert len(lines) == expected_count, (
        f"Report file has {len(lines)} lines, but expected {expected_count} lines.\n"
        f"Actual lines:\n" + "\n".join(repr(l) for l in lines) + "\n"
        f"Expected lines:\n" + "\n".join(repr(l) for l in EXPECTED_LINES)
    )


def test_report_header_line():
    lines = read_report_lines()
    assert len(lines) >= 1, "Report file is empty."
    assert lines[0] == EXPECTED_HEADER, (
        f"Line 1 (header) is wrong.\n"
        f"  Got:      {repr(lines[0])}\n"
        f"  Expected: {repr(EXPECTED_HEADER)}"
    )


def test_report_separator_line():
    lines = read_report_lines()
    assert len(lines) >= 2, "Report file has fewer than 2 lines."
    assert lines[1] == EXPECTED_SEPARATOR, (
        f"Line 2 (separator) is wrong.\n"
        f"  Got:      {repr(lines[1])}\n"
        f"  Expected: {repr(EXPECTED_SEPARATOR)} (exactly 42 '=' characters)"
    )


def test_separator_is_exactly_42_equals():
    lines = read_report_lines()
    assert len(lines) >= 2, "Report file has fewer than 2 lines."
    sep = lines[1]
    assert len(sep) == 42 and all(c == "=" for c in sep), (
        f"Separator line must be exactly 42 '=' characters.\n"
        f"  Got: {repr(sep)} (length={len(sep)})"
    )


def test_report_backups_line():
    lines = read_report_lines()
    assert len(lines) >= 3, "Report file has fewer than 3 lines (missing data lines)."
    expected = EXPECTED_DATA_LINES[0]
    assert lines[2] == expected, (
        f"Line 3 (first data line) is wrong.\n"
        f"  Got:      {repr(lines[2])}\n"
        f"  Expected: {repr(expected)}\n"
        "  (backups should be 200K, listed first as largest)"
    )


def test_report_logs_line():
    lines = read_report_lines()
    assert len(lines) >= 4, "Report file has fewer than 4 lines (missing logs line)."
    expected = EXPECTED_DATA_LINES[1]
    assert lines[3] == expected, (
        f"Line 4 (second data line) is wrong.\n"
        f"  Got:      {repr(lines[3])}\n"
        f"  Expected: {repr(expected)}\n"
        "  (logs should be 100K, listed second)"
    )


def test_report_cache_line():
    lines = read_report_lines()
    assert len(lines) >= 5, "Report file has fewer than 5 lines (missing cache line)."
    expected = EXPECTED_DATA_LINES[2]
    assert lines[4] == expected, (
        f"Line 5 (third data line) is wrong.\n"
        f"  Got:      {repr(lines[4])}\n"
        f"  Expected: {repr(expected)}\n"
        "  (cache should be 64K, listed third)"
    )


def test_tmp_not_in_report():
    """tmp directory uses only 8K, so it must be excluded (< 50K threshold)."""
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "/home/user/server_data/tmp" not in content, (
        "The 'tmp' subdirectory (8K) should NOT appear in the report "
        "because it is below the 50K threshold."
    )


def test_sessions_not_in_report():
    """sessions directory uses only 32K, so it must be excluded (< 50K threshold)."""
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "/home/user/server_data/sessions" not in content, (
        "The 'sessions' subdirectory (32K) should NOT appear in the report "
        "because it is below the 50K threshold."
    )


def test_data_lines_use_tab_separator():
    """Each data line must use a literal tab between size and path."""
    lines = read_report_lines()
    data_lines = lines[2:]  # skip header and separator
    for i, line in enumerate(data_lines):
        assert "\t" in line, (
            f"Data line {i + 3} does not contain a tab character.\n"
            f"  Got: {repr(line)}\n"
            "  Each data line must be: <size>K<TAB><path>"
        )
        parts = line.split("\t")
        assert len(parts) == 2, (
            f"Data line {i + 3} should have exactly 2 tab-separated fields.\n"
            f"  Got: {repr(line)}"
        )


def test_data_lines_size_format():
    """Each data line's size field must end with 'K' and be a valid integer."""
    lines = read_report_lines()
    data_lines = lines[2:]
    for i, line in enumerate(data_lines):
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        size_field = parts[0]
        assert size_field.endswith("K"), (
            f"Data line {i + 3}: size field '{size_field}' must end with 'K'.\n"
            f"  Full line: {repr(line)}"
        )
        size_value = size_field[:-1]
        assert size_value.isdigit(), (
            f"Data line {i + 3}: size value '{size_value}' is not a valid integer.\n"
            f"  Full line: {repr(line)}"
        )


def test_data_lines_sorted_descending():
    """Data lines must be sorted from largest to smallest."""
    lines = read_report_lines()
    data_lines = lines[2:]
    sizes = []
    for line in data_lines:
        parts = line.split("\t")
        if len(parts) == 2 and parts[0].endswith("K"):
            sizes.append(int(parts[0][:-1]))
    assert sizes == sorted(sizes, reverse=True), (
        f"Data lines are not sorted in descending order by size.\n"
        f"  Sizes found: {sizes}\n"
        f"  Expected order: {sorted(sizes, reverse=True)}"
    )


def test_no_trailing_spaces_in_lines():
    """No line should have trailing spaces."""
    lines = read_report_lines()
    for i, line in enumerate(lines):
        assert line == line.rstrip(" "), (
            f"Line {i + 1} has trailing spaces: {repr(line)}"
        )


def test_no_blank_lines_between_entries():
    """There should be no blank lines anywhere in the report."""
    lines = read_report_lines()
    for i, line in enumerate(lines):
        assert line.strip() != "", (
            f"Line {i + 1} is blank or whitespace-only. "
            "No blank lines are allowed in the report."
        )


def test_data_lines_have_absolute_paths():
    """Each data line's path must be an absolute path under server_data."""
    lines = read_report_lines()
    data_lines = lines[2:]
    for i, line in enumerate(data_lines):
        parts = line.split("\t")
        if len(parts) == 2:
            path = parts[1]
            assert path.startswith("/home/user/server_data/"), (
                f"Data line {i + 3}: path '{path}' is not an absolute path "
                f"under '{BASE_DIR}'."
            )


def test_exact_file_content():
    """The entire file content must exactly match the expected report."""
    expected_content = "\n".join(EXPECTED_LINES) + "\n"
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()

    # Also accept without trailing newline
    if actual_content == expected_content or actual_content == expected_content.rstrip("\n"):
        return

    assert actual_content == expected_content, (
        f"Report file content does not match expected.\n"
        f"Expected:\n{repr(expected_content)}\n\n"
        f"Actual:\n{repr(actual_content)}"
    )