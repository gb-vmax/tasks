# test_final_state.py

import os
import subprocess
import re
import pytest

REPORT_FILE = "/home/user/disk_report.txt"
NET_DATA = "/home/user/net_data"
CAPTURES = "/home/user/net_data/captures"
LOGS = "/home/user/net_data/logs"
CONFIGS = "/home/user/net_data/configs"


def get_du_size(path):
    """Run du -sh on a path and return the human-readable size string."""
    result = subprocess.run(
        ["du", "-sh", path],
        capture_output=True, text=True, check=True
    )
    # Output format: "<size>\t<path>"
    size = result.stdout.split("\t")[0].strip()
    return size


def get_du_bytes(path):
    """Run du -sb on a path and return the size in bytes as an integer."""
    result = subprocess.run(
        ["du", "-sb", path],
        capture_output=True, text=True, check=True
    )
    size = int(result.stdout.split()[0])
    return size


@pytest.fixture(scope="module")
def report_lines():
    """Read the report file and return its lines (without trailing newline on each)."""
    assert os.path.isfile(REPORT_FILE), (
        f"Report file {REPORT_FILE} does not exist. The task has not been completed."
    )
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    # Split into lines; we want to preserve empty lines
    lines = content.splitlines()
    return lines


def test_report_file_exists():
    """The report file must exist at /home/user/disk_report.txt."""
    assert os.path.isfile(REPORT_FILE), (
        f"Report file {REPORT_FILE} does not exist. "
        "Please create the disk usage report as described in the task."
    )


def test_report_has_exactly_7_lines(report_lines):
    """The report must have exactly 7 lines."""
    assert len(report_lines) == 7, (
        f"Expected exactly 7 lines in {REPORT_FILE}, but found {len(report_lines)}. "
        f"Lines: {report_lines}"
    )


def test_line1_header(report_lines):
    """Line 1 must be the exact header string."""
    expected = "Disk Usage Report: /home/user/net_data"
    assert report_lines[0] == expected, (
        f"Line 1 should be '{expected}' but got '{report_lines[0]}'"
    )


def test_line2_blank(report_lines):
    """Line 2 must be blank."""
    assert report_lines[1] == "", (
        f"Line 2 should be empty but got '{report_lines[1]}'"
    )


def test_line6_blank(report_lines):
    """Line 6 must be blank."""
    assert report_lines[5] == "", (
        f"Line 6 should be empty but got '{report_lines[5]}'"
    )


def test_subdirectory_lines_format(report_lines):
    """Lines 3-5 must be in 'du -sh' tab-separated format: <size>\t<path>."""
    for i in range(2, 5):
        line = report_lines[i]
        parts = line.split("\t")
        assert len(parts) == 2, (
            f"Line {i+1} should have exactly one tab character separating size and path, "
            f"but got: '{line}'"
        )
        size_part, path_part = parts
        # Size should match a human-readable du format like 4.0K, 12M, 1.1G, 276K, etc.
        assert re.match(r'^\d+(\.\d+)?[KMGTP]?$', size_part), (
            f"Line {i+1} size '{size_part}' does not look like a du -sh human-readable size. "
            f"Full line: '{line}'"
        )
        # Path should be a valid absolute path
        assert path_part.startswith("/"), (
            f"Line {i+1} path '{path_part}' should be an absolute path. "
            f"Full line: '{line}'"
        )


def test_subdirectory_lines_contain_correct_paths(report_lines):
    """Lines 3-5 must contain the three expected subdirectory paths."""
    paths_in_report = set()
    for i in range(2, 5):
        line = report_lines[i]
        parts = line.split("\t")
        assert len(parts) == 2, (
            f"Line {i+1} is malformed (no tab): '{line}'"
        )
        path_part = parts[1].strip()
        paths_in_report.add(path_part)

    expected_paths = {CAPTURES, LOGS, CONFIGS}
    assert paths_in_report == expected_paths, (
        f"Expected subdirectory paths {expected_paths} in lines 3-5, "
        f"but found {paths_in_report}"
    )


def test_subdirectory_lines_sorted_descending_by_size(report_lines):
    """Lines 3-5 must be sorted in descending order by actual disk usage (largest first)."""
    # Get actual byte sizes
    actual_sizes = {
        CAPTURES: get_du_bytes(CAPTURES),
        LOGS: get_du_bytes(LOGS),
        CONFIGS: get_du_bytes(CONFIGS),
    }

    # Extract paths from lines 3-5 in order
    ordered_paths = []
    for i in range(2, 5):
        line = report_lines[i]
        parts = line.split("\t")
        assert len(parts) == 2, f"Line {i+1} is malformed: '{line}'"
        path_part = parts[1].strip()
        ordered_paths.append(path_part)

    # Verify descending order
    for j in range(len(ordered_paths) - 1):
        path_a = ordered_paths[j]
        path_b = ordered_paths[j + 1]
        size_a = actual_sizes.get(path_a)
        size_b = actual_sizes.get(path_b)
        assert size_a is not None, (
            f"Path '{path_a}' from report line {j+3} is not a recognized subdirectory."
        )
        assert size_b is not None, (
            f"Path '{path_b}' from report line {j+4} is not a recognized subdirectory."
        )
        assert size_a >= size_b, (
            f"Subdirectory order is wrong: '{path_a}' ({size_a} bytes) should come before "
            f"'{path_b}' ({size_b} bytes), but sizes are not in descending order. "
            f"Report lines 3-5: {report_lines[2:5]}"
        )


def test_captures_before_logs(report_lines):
    """captures must appear before logs in the report (captures is larger)."""
    captures_line_idx = None
    logs_line_idx = None
    for i in range(2, 5):
        line = report_lines[i]
        parts = line.split("\t")
        if len(parts) == 2:
            path = parts[1].strip()
            if path == CAPTURES:
                captures_line_idx = i
            elif path == LOGS:
                logs_line_idx = i

    assert captures_line_idx is not None, (
        f"Could not find captures path '{CAPTURES}' in lines 3-5 of the report."
    )
    assert logs_line_idx is not None, (
        f"Could not find logs path '{LOGS}' in lines 3-5 of the report."
    )
    assert captures_line_idx < logs_line_idx, (
        f"captures (line {captures_line_idx+1}) should come before "
        f"logs (line {logs_line_idx+1}) since captures is larger."
    )


def test_logs_before_configs(report_lines):
    """logs must appear before configs in the report (logs is larger)."""
    logs_line_idx = None
    configs_line_idx = None
    for i in range(2, 5):
        line = report_lines[i]
        parts = line.split("\t")
        if len(parts) == 2:
            path = parts[1].strip()
            if path == LOGS:
                logs_line_idx = i
            elif path == CONFIGS:
                configs_line_idx = i

    assert logs_line_idx is not None, (
        f"Could not find logs path '{LOGS}' in lines 3-5 of the report."
    )
    assert configs_line_idx is not None, (
        f"Could not find configs path '{CONFIGS}' in lines 3-5 of the report."
    )
    assert logs_line_idx < configs_line_idx, (
        f"logs (line {logs_line_idx+1}) should come before "
        f"configs (line {configs_line_idx+1}) since logs is larger."
    )


def test_subdirectory_sizes_match_du(report_lines):
    """The sizes reported for each subdirectory must match what du -sh actually reports."""
    for i in range(2, 5):
        line = report_lines[i]
        parts = line.split("\t")
        assert len(parts) == 2, f"Line {i+1} is malformed: '{line}'"
        reported_size = parts[0].strip()
        path = parts[1].strip()

        actual_size = get_du_size(path)
        assert reported_size == actual_size, (
            f"Line {i+1}: reported size '{reported_size}' for '{path}' "
            f"does not match actual du -sh output '{actual_size}'. "
            f"The sizes in the report must match the current du -sh values."
        )


def test_line7_total_format(report_lines):
    """Line 7 must start with 'Total: ' followed by the du -sh size of /home/user/net_data."""
    line7 = report_lines[6]
    assert line7.startswith("Total: "), (
        f"Line 7 should start with 'Total: ' but got '{line7}'"
    )


def test_line7_total_size_matches_du(report_lines):
    """The total size on line 7 must match the actual du -sh output for /home/user/net_data."""
    line7 = report_lines[6]
    assert line7.startswith("Total: "), (
        f"Line 7 should start with 'Total: ' but got '{line7}'"
    )
    reported_total = line7[len("Total: "):].strip()

    actual_total = get_du_size(NET_DATA)
    assert reported_total == actual_total, (
        f"Line 7 total size '{reported_total}' does not match "
        f"actual du -sh {NET_DATA} output '{actual_total}'. "
        f"The total must reflect the current disk usage of {NET_DATA}."
    )


def test_no_trailing_blank_lines(report_lines):
    """The file should have exactly 7 lines with no extra trailing blank lines."""
    # We already check for exactly 7 lines in test_report_has_exactly_7_lines,
    # but also verify the last line is not blank
    assert report_lines[6] != "", (
        f"Line 7 (the last line) should not be blank. Got '{report_lines[6]}'. "
        f"The file should end with the Total line."
    )