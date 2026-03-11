# test_final_state.py

import os
import re
import subprocess
import pytest

REPORT_FILE = "/home/user/disk_report.txt"
DATA_DIR = "/home/user/data"

EXPECTED_RANK = {
    1: ("backups", 204800),
    2: ("logs", 51200),
    3: ("uploads", 30720),
}

TOLERANCE = 0.05  # 5%

LINE_PATTERN = re.compile(
    r'^(\d+)\.\s+(\d+)K\t(/home/user/data/(\S+))$'
)


@pytest.fixture(scope="module")
def report_lines():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file {REPORT_FILE} does not exist. "
        "The task requires creating this file."
    )
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    lines = content.splitlines()
    return lines


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file {REPORT_FILE} does not exist. "
        "Please create the disk usage report at this path."
    )


def test_report_has_exactly_four_lines(report_lines):
    assert len(report_lines) == 4, (
        f"Report file must have exactly 4 lines, but has {len(report_lines)} lines.\n"
        f"Content:\n" + "\n".join(repr(l) for l in report_lines)
    )


def test_report_header_line(report_lines):
    assert report_lines[0] == "=== Disk Usage Report ===", (
        f"First line must be exactly '=== Disk Usage Report ===' but got: {report_lines[0]!r}"
    )


def test_report_entry_lines_format(report_lines):
    for i in range(1, 4):
        line = report_lines[i]
        match = LINE_PATTERN.match(line)
        assert match is not None, (
            f"Line {i+1} does not match expected format 'N. <SIZE>K\\t/home/user/data/<dirname>'.\n"
            f"Got: {line!r}\n"
            f"Expected format example: '1. 204800K\\t/home/user/data/backups'"
        )


def test_report_numbering(report_lines):
    for i in range(1, 4):
        line = report_lines[i]
        match = LINE_PATTERN.match(line)
        assert match is not None, f"Line {i+1} does not match pattern: {line!r}"
        rank_num = int(match.group(1))
        assert rank_num == i, (
            f"Line {i+1} should start with rank number {i}, but got {rank_num}.\n"
            f"Line content: {line!r}"
        )


def test_report_sizes_descending(report_lines):
    sizes = []
    for i in range(1, 4):
        line = report_lines[i]
        match = LINE_PATTERN.match(line)
        assert match is not None, f"Line {i+1} does not match pattern: {line!r}"
        sizes.append(int(match.group(2)))

    for i in range(len(sizes) - 1):
        assert sizes[i] >= sizes[i + 1], (
            f"Sizes must be in descending order, but entry {i+1} ({sizes[i]}K) "
            f"is not >= entry {i+2} ({sizes[i+1]}K).\n"
            f"All sizes: {sizes}"
        )


def test_report_rank1_is_backups(report_lines):
    line = report_lines[1]
    match = LINE_PATTERN.match(line)
    assert match is not None, f"Line 2 does not match pattern: {line!r}"
    dirname = match.group(4)
    assert dirname == "backups", (
        f"Rank 1 entry should be 'backups' directory, but got '{dirname}'.\n"
        f"Line: {line!r}"
    )


def test_report_rank2_is_logs(report_lines):
    line = report_lines[2]
    match = LINE_PATTERN.match(line)
    assert match is not None, f"Line 3 does not match pattern: {line!r}"
    dirname = match.group(4)
    assert dirname == "logs", (
        f"Rank 2 entry should be 'logs' directory, but got '{dirname}'.\n"
        f"Line: {line!r}"
    )


def test_report_rank3_is_uploads(report_lines):
    line = report_lines[3]
    match = LINE_PATTERN.match(line)
    assert match is not None, f"Line 4 does not match pattern: {line!r}"
    dirname = match.group(4)
    assert dirname == "uploads", (
        f"Rank 3 entry should be 'uploads' directory, but got '{dirname}'.\n"
        f"Line: {line!r}"
    )


def test_report_sizes_within_tolerance(report_lines):
    for i in range(1, 4):
        line = report_lines[i]
        match = LINE_PATTERN.match(line)
        assert match is not None, f"Line {i+1} does not match pattern: {line!r}"
        actual_size = int(match.group(2))
        dirname = match.group(4)
        expected_name, expected_kb = EXPECTED_RANK[i]
        diff = abs(actual_size - expected_kb) / expected_kb
        assert diff < TOLERANCE, (
            f"Rank {i} entry '{dirname}' has size {actual_size}K, "
            f"expected ~{expected_kb}K for '{expected_name}' "
            f"(difference {diff*100:.1f}% exceeds {TOLERANCE*100:.0f}% tolerance).\n"
            f"Line: {line!r}"
        )


def test_report_paths_are_absolute(report_lines):
    for i in range(1, 4):
        line = report_lines[i]
        match = LINE_PATTERN.match(line)
        assert match is not None, f"Line {i+1} does not match pattern: {line!r}"
        path = match.group(3)
        assert os.path.isabs(path), (
            f"Path in rank {i} entry must be absolute, but got: {path!r}\n"
            f"Line: {line!r}"
        )
        assert path.startswith(DATA_DIR), (
            f"Path in rank {i} entry must start with '{DATA_DIR}', but got: {path!r}\n"
            f"Line: {line!r}"
        )


def test_report_tab_separator(report_lines):
    """Verify that there is exactly one tab character between the size and path."""
    for i in range(1, 4):
        line = report_lines[i]
        # After the "N. <SIZE>K" part, there must be a tab then the path
        # Check that the line contains a tab
        assert '\t' in line, (
            f"Line {i+1} must contain a tab character between the size and path.\n"
            f"Got: {line!r}"
        )
        # Verify the tab is in the right place: after the "K" and before the path
        # Pattern: "N. <SIZE>K\t<PATH>"
        parts_after_dot = line.split('. ', 1)
        assert len(parts_after_dot) == 2, f"Cannot parse line {i+1}: {line!r}"
        size_and_path = parts_after_dot[1]
        tab_parts = size_and_path.split('\t', 1)
        assert len(tab_parts) == 2, (
            f"Line {i+1} must have exactly one tab separating size from path.\n"
            f"Got: {line!r}"
        )
        size_part = tab_parts[0]
        assert size_part.endswith('K'), (
            f"Size part before tab must end with 'K', got: {size_part!r}\n"
            f"Line: {line!r}"
        )


def test_data_directory_not_modified():
    """Verify that the data directory contents have not been modified."""
    expected_files = {
        "/home/user/data/backups/backup.tar": 200 * 1024 * 1024,
        "/home/user/data/logs/access.log": 50 * 1024 * 1024,
        "/home/user/data/uploads/user_uploads.bin": 30 * 1024 * 1024,
        "/home/user/data/tmp/scratch.bin": 5 * 1024 * 1024,
        "/home/user/data/configs/settings.conf": 1 * 1024 * 1024,
    }
    for path, expected_size in expected_files.items():
        assert os.path.isfile(path), (
            f"File {path} is missing — the data directory should not be modified."
        )
        actual_size = os.path.getsize(path)
        diff = abs(actual_size - expected_size) / expected_size
        assert diff < TOLERANCE, (
            f"File {path} has size {actual_size} bytes, expected ~{expected_size} bytes. "
            f"The data directory should not be modified."
        )


def test_report_sizes_match_actual_du(report_lines):
    """
    Verify that the sizes in the report match what du -sk actually reports
    for those directories (within tolerance).
    """
    result = subprocess.run(
        ["du", "-sk",
         "/home/user/data/backups",
         "/home/user/data/logs",
         "/home/user/data/uploads"],
        capture_output=True,
        text=True,
        check=True
    )
    assert result.returncode == 0, f"du command failed: {result.stderr}"

    actual_du = {}
    for line in result.stdout.strip().splitlines():
        parts = line.split('\t', 1)
        assert len(parts) == 2, f"Unexpected du output: {line!r}"
        kb = int(parts[0])
        path = parts[1].rstrip('/')
        actual_du[path] = kb

    rank_to_path = {
        1: "/home/user/data/backups",
        2: "/home/user/data/logs",
        3: "/home/user/data/uploads",
    }

    for i in range(1, 4):
        line = report_lines[i]
        match = LINE_PATTERN.match(line)
        assert match is not None, f"Line {i+1} does not match pattern: {line!r}"
        reported_size = int(match.group(2))
        expected_path = rank_to_path[i]
        actual_size = actual_du.get(expected_path)
        assert actual_size is not None, (
            f"Could not get du size for {expected_path}"
        )
        diff = abs(reported_size - actual_size) / actual_size if actual_size else 1
        assert diff < TOLERANCE, (
            f"Rank {i} reported size {reported_size}K does not match "
            f"actual du size {actual_size}K for {expected_path} "
            f"(difference {diff*100:.1f}% exceeds {TOLERANCE*100:.0f}% tolerance)."
        )