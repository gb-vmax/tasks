# test_final_state.py

import os
import re
import socket
import subprocess
import pytest

REPORT_FILE = "/home/user/disk_report.txt"
APPDATA_DIR = "/home/user/appdata"


def get_hostname():
    result = subprocess.run(["hostname"], capture_output=True, text=True, check=True)
    return result.stdout.strip()


def get_du_sk(path):
    result = subprocess.run(["du", "-sk", path], capture_output=True, text=True, check=True)
    return int(result.stdout.split()[0])


def get_df_available(path):
    result = subprocess.run(["df", "-k", path], capture_output=True, text=True, check=True)
    lines = result.stdout.strip().splitlines()
    # Header line: Filesystem 1K-blocks Used Available Use% Mounted on
    # Data line follows
    header = lines[0].split()
    data = lines[1].split()
    avail_idx = None
    for i, col in enumerate(header):
        if col.lower() == "available":
            avail_idx = i
            break
    if avail_idx is None:
        # fallback: Available is typically the 4th column (index 3)
        avail_idx = 3
    return int(data[avail_idx])


def get_top5_subdirs():
    subdirs = [
        os.path.join(APPDATA_DIR, d)
        for d in os.listdir(APPDATA_DIR)
        if os.path.isdir(os.path.join(APPDATA_DIR, d))
    ]
    sizes = {}
    for d in subdirs:
        sizes[d] = get_du_sk(d)
    sorted_dirs = sorted(sizes.items(), key=lambda x: x[1], reverse=True)
    return sorted_dirs[:5]


@pytest.fixture(scope="module")
def report_lines():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file {REPORT_FILE} does not exist. The task has not been completed."
    )
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    lines = content.splitlines()
    return lines


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file {REPORT_FILE} does not exist. The task has not been completed."
    )


def test_line1_header(report_lines):
    assert len(report_lines) >= 1, "Report file is empty"
    assert report_lines[0] == "=== DISK USAGE REPORT ===", (
        f"Line 1 should be '=== DISK USAGE REPORT ===' but got: {report_lines[0]!r}"
    )


def test_line2_generated(report_lines):
    assert len(report_lines) >= 2, "Report file has fewer than 2 lines"
    hostname = get_hostname()
    expected = f"Generated: {hostname}"
    assert report_lines[1] == expected, (
        f"Line 2 should be {expected!r} but got: {report_lines[1]!r}"
    )


def test_line3_empty(report_lines):
    assert len(report_lines) >= 3, "Report file has fewer than 3 lines"
    assert report_lines[2] == "", (
        f"Line 3 should be empty but got: {report_lines[2]!r}"
    )


def test_line4_top_directories_header(report_lines):
    assert len(report_lines) >= 4, "Report file has fewer than 4 lines"
    assert report_lines[3] == "Top directories by size:", (
        f"Line 4 should be 'Top directories by size:' but got: {report_lines[3]!r}"
    )


def test_lines5_to_9_format(report_lines):
    assert len(report_lines) >= 9, (
        f"Report file should have at least 9 lines, but has {len(report_lines)}"
    )
    pattern = re.compile(r"^  [0-9]+K  /home/user/appdata/[a-z]+$")
    for i in range(4, 9):
        line = report_lines[i]
        assert pattern.match(line), (
            f"Line {i+1} does not match expected format '^  [0-9]+K  /home/user/appdata/[a-z]+$'. "
            f"Got: {line!r}"
        )


def test_lines5_to_9_sorted_descending(report_lines):
    assert len(report_lines) >= 9, (
        f"Report file should have at least 9 lines, but has {len(report_lines)}"
    )
    sizes = []
    for i in range(4, 9):
        line = report_lines[i]
        match = re.match(r"^  ([0-9]+)K  /home/user/appdata/([a-z]+)$", line)
        assert match, f"Line {i+1} does not match expected format: {line!r}"
        sizes.append(int(match.group(1)))
    for j in range(len(sizes) - 1):
        assert sizes[j] >= sizes[j + 1], (
            f"Lines 5-9 are not sorted in descending order by size. "
            f"Got sizes: {sizes}"
        )


def test_config_not_in_top5(report_lines):
    assert len(report_lines) >= 9, (
        f"Report file should have at least 9 lines, but has {len(report_lines)}"
    )
    for i in range(4, 9):
        line = report_lines[i]
        assert "/home/user/appdata/config" not in line, (
            f"Line {i+1} should not contain '/home/user/appdata/config' (config is the smallest directory). "
            f"Got: {line!r}"
        )


def test_line10_empty(report_lines):
    assert len(report_lines) >= 10, (
        f"Report file should have at least 10 lines, but has {len(report_lines)}"
    )
    assert report_lines[9] == "", (
        f"Line 10 should be empty but got: {report_lines[9]!r}"
    )


def test_line11_total_usage_format(report_lines):
    assert len(report_lines) >= 11, (
        f"Report file should have at least 11 lines, but has {len(report_lines)}"
    )
    pattern = re.compile(r"^Total usage: [0-9]+K$")
    assert pattern.match(report_lines[10]), (
        f"Line 11 should match 'Total usage: <number>K' but got: {report_lines[10]!r}"
    )


def test_line12_available_format(report_lines):
    assert len(report_lines) >= 12, (
        f"Report file should have at least 12 lines, but has {len(report_lines)}"
    )
    pattern = re.compile(r"^Available: [0-9]+K$")
    assert pattern.match(report_lines[11]), (
        f"Line 12 should match 'Available: <number>K' but got: {report_lines[11]!r}"
    )


def test_line11_total_usage_value(report_lines):
    assert len(report_lines) >= 11, (
        f"Report file should have at least 11 lines, but has {len(report_lines)}"
    )
    match = re.match(r"^Total usage: ([0-9]+)K$", report_lines[10])
    assert match, f"Line 11 format is wrong: {report_lines[10]!r}"
    reported_total = int(match.group(1))

    actual_total = get_du_sk(APPDATA_DIR)

    # Allow a small tolerance (e.g., 5%) since disk usage can fluctuate slightly
    # but in practice they should be very close or identical
    tolerance = max(10, int(actual_total * 0.05))
    assert abs(reported_total - actual_total) <= tolerance, (
        f"Line 11 total usage value {reported_total}K does not match "
        f"current 'du -sk {APPDATA_DIR}' output of {actual_total}K "
        f"(tolerance: {tolerance}K)"
    )


def test_line12_available_value(report_lines):
    assert len(report_lines) >= 12, (
        f"Report file should have at least 12 lines, but has {len(report_lines)}"
    )
    match = re.match(r"^Available: ([0-9]+)K$", report_lines[11])
    assert match, f"Line 12 format is wrong: {report_lines[11]!r}"
    reported_available = int(match.group(1))

    actual_available = get_df_available(APPDATA_DIR)

    # Allow a reasonable tolerance since available space can change between reads
    tolerance = max(1024, int(actual_available * 0.05))
    assert abs(reported_available - actual_available) <= tolerance, (
        f"Line 12 available value {reported_available}K does not match "
        f"current 'df -k' available of {actual_available}K "
        f"(tolerance: {tolerance}K)"
    )


def test_top5_directories_match_actual(report_lines):
    """Verify that the 5 directories listed are actually the top 5 by du -sk."""
    assert len(report_lines) >= 9, (
        f"Report file should have at least 9 lines, but has {len(report_lines)}"
    )
    top5 = get_top5_subdirs()
    top5_paths = {path for path, _ in top5}

    reported_paths = []
    for i in range(4, 9):
        line = report_lines[i]
        match = re.match(r"^  [0-9]+K  (/home/user/appdata/[a-z]+)$", line)
        assert match, f"Line {i+1} does not match expected format: {line!r}"
        reported_paths.append(match.group(1))

    reported_paths_set = set(reported_paths)
    assert reported_paths_set == top5_paths, (
        f"The reported top 5 directories {sorted(reported_paths_set)} "
        f"do not match the actual top 5 directories {sorted(top5_paths)}"
    )


def test_directory_sizes_in_report_match_actual(report_lines):
    """Verify that the KB values in the report match actual du -sk output for each directory."""
    assert len(report_lines) >= 9, (
        f"Report file should have at least 9 lines, but has {len(report_lines)}"
    )
    for i in range(4, 9):
        line = report_lines[i]
        match = re.match(r"^  ([0-9]+)K  (/home/user/appdata/[a-z]+)$", line)
        assert match, f"Line {i+1} does not match expected format: {line!r}"
        reported_size = int(match.group(1))
        path = match.group(2)

        actual_size = get_du_sk(path)
        tolerance = max(4, int(actual_size * 0.05))
        assert abs(reported_size - actual_size) <= tolerance, (
            f"Line {i+1}: reported size {reported_size}K for {path} does not match "
            f"actual 'du -sk' value of {actual_size}K (tolerance: {tolerance}K)"
        )


def test_report_has_exactly_12_lines(report_lines):
    """The report should have exactly 12 lines (no trailing content)."""
    # Allow for a possible trailing newline resulting in an empty last element
    effective_lines = report_lines
    if effective_lines and effective_lines[-1] == "":
        effective_lines = effective_lines[:-1]
    assert len(effective_lines) == 12, (
        f"Report should have exactly 12 lines but has {len(effective_lines)}. "
        f"Lines: {effective_lines}"
    )