# test_final_state.py

import os
import subprocess
import pytest

REPORT_FILE = "/home/user/disk_report.txt"
ARCHIVE_DIR = "/home/user/archive"

EXPECTED_LINES = [
    "40K\t/home/user/archive/videos",
    "20K\t/home/user/archive/docs",
    "8K\t/home/user/archive/logs",
    "4K\t/home/user/archive/configs",
]


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Expected report file {REPORT_FILE} to exist, but it does not. "
        "The disk usage report has not been generated yet."
    )


def test_report_file_is_not_empty():
    size = os.path.getsize(REPORT_FILE)
    assert size > 0, (
        f"Expected report file {REPORT_FILE} to be non-empty, but it is empty."
    )


def test_report_file_line_count():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    # Filter out any trailing empty lines
    non_empty_lines = [l for l in lines if l.strip() != ""]
    assert len(non_empty_lines) == 4, (
        f"Expected exactly 4 non-empty lines in {REPORT_FILE}, "
        f"but found {len(non_empty_lines)}. Lines: {non_empty_lines}"
    )


def test_report_file_exact_content():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    # Build expected content: lines joined by newline, with a trailing newline
    expected_content = "\n".join(EXPECTED_LINES) + "\n"

    assert content == expected_content, (
        f"Report file content does not match expected.\n"
        f"Expected:\n{repr(expected_content)}\n"
        f"Got:\n{repr(content)}"
    )


def test_report_first_line_videos():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    non_empty = [l for l in lines if l.strip()]
    assert len(non_empty) >= 1, "Report file has no lines."
    assert non_empty[0] == EXPECTED_LINES[0], (
        f"First line (largest directory) should be:\n  {repr(EXPECTED_LINES[0])}\n"
        f"But got:\n  {repr(non_empty[0])}\n"
        "The 'videos' directory (40K) should appear first."
    )


def test_report_second_line_docs():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    non_empty = [l for l in lines if l.strip()]
    assert len(non_empty) >= 2, "Report file has fewer than 2 lines."
    assert non_empty[1] == EXPECTED_LINES[1], (
        f"Second line should be:\n  {repr(EXPECTED_LINES[1])}\n"
        f"But got:\n  {repr(non_empty[1])}\n"
        "The 'docs' directory (20K) should appear second."
    )


def test_report_third_line_logs():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    non_empty = [l for l in lines if l.strip()]
    assert len(non_empty) >= 3, "Report file has fewer than 3 lines."
    assert non_empty[2] == EXPECTED_LINES[2], (
        f"Third line should be:\n  {repr(EXPECTED_LINES[2])}\n"
        f"But got:\n  {repr(non_empty[2])}\n"
        "The 'logs' directory (8K) should appear third."
    )


def test_report_fourth_line_configs():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    non_empty = [l for l in lines if l.strip()]
    assert len(non_empty) >= 4, "Report file has fewer than 4 lines."
    assert non_empty[3] == EXPECTED_LINES[3], (
        f"Fourth line should be:\n  {repr(EXPECTED_LINES[3])}\n"
        f"But got:\n  {repr(non_empty[3])}\n"
        "The 'configs' directory (4K) should appear fourth."
    )


def test_report_uses_tab_separator():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    non_empty = [l for l in lines if l.strip()]
    for i, line in enumerate(non_empty):
        assert "\t" in line, (
            f"Line {i+1} does not contain a tab character separator.\n"
            f"Line content: {repr(line)}\n"
            "Each line must use a tab (\\t) between the size and the path."
        )


def test_report_sizes_have_K_suffix():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    non_empty = [l for l in lines if l.strip()]
    for i, line in enumerate(non_empty):
        parts = line.split("\t")
        assert len(parts) >= 1, f"Line {i+1} is malformed: {repr(line)}"
        size_field = parts[0]
        assert size_field.endswith("K"), (
            f"Line {i+1}: size field {repr(size_field)} does not end with 'K'.\n"
            "Sizes must be expressed in kilobytes with a capital K suffix (e.g., 40K)."
        )
        # Check the numeric part is actually a number
        numeric_part = size_field[:-1]
        assert numeric_part.isdigit(), (
            f"Line {i+1}: size field {repr(size_field)} — the part before 'K' "
            f"({repr(numeric_part)}) is not a valid integer."
        )


def test_report_paths_are_absolute():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    non_empty = [l for l in lines if l.strip()]
    for i, line in enumerate(non_empty):
        parts = line.split("\t")
        assert len(parts) == 2, (
            f"Line {i+1} does not have exactly 2 tab-separated fields: {repr(line)}"
        )
        path_field = parts[1]
        assert path_field.startswith("/"), (
            f"Line {i+1}: path {repr(path_field)} is not an absolute path. "
            "Paths must start with '/'."
        )


def test_report_paths_reference_archive_subdirs():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    non_empty = [l for l in lines if l.strip()]
    expected_paths = {
        "/home/user/archive/videos",
        "/home/user/archive/docs",
        "/home/user/archive/logs",
        "/home/user/archive/configs",
    }
    actual_paths = set()
    for line in non_empty:
        parts = line.split("\t")
        if len(parts) == 2:
            actual_paths.add(parts[1])
    assert actual_paths == expected_paths, (
        f"Report paths do not match expected archive subdirectories.\n"
        f"Expected paths: {sorted(expected_paths)}\n"
        f"Got paths: {sorted(actual_paths)}"
    )


def test_report_sorted_descending_by_size():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    non_empty = [l for l in lines if l.strip()]
    sizes = []
    for i, line in enumerate(non_empty):
        parts = line.split("\t")
        assert len(parts) == 2, f"Line {i+1} malformed: {repr(line)}"
        size_field = parts[0]
        assert size_field.endswith("K"), f"Line {i+1} size field malformed: {repr(size_field)}"
        sizes.append(int(size_field[:-1]))
    assert sizes == sorted(sizes, reverse=True), (
        f"Lines are not sorted in descending order by size.\n"
        f"Got sizes in order: {sizes}\n"
        f"Expected descending order: {sorted(sizes, reverse=True)}"
    )


def test_report_no_trailing_spaces_on_lines():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    non_empty = [l for l in lines if l.strip()]
    for i, line in enumerate(non_empty):
        assert not line.endswith(" "), (
            f"Line {i+1} has trailing space(s): {repr(line)}"
        )


def test_report_no_blank_lines_between_data():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    lines = content.splitlines()
    # Allow a single trailing newline (standard), but no blank lines within data
    for i, line in enumerate(lines):
        if i < len(lines) - 1 or line.strip():
            # All lines except possibly the last should be non-empty
            pass
    blank_lines = [i + 1 for i, l in enumerate(lines) if l.strip() == ""]
    # If there's a trailing newline, the last element after splitlines won't be blank
    # but let's check for any blank lines in the middle
    if blank_lines:
        # Check if it's only the very last position
        assert blank_lines == [], (
            f"Report file contains blank lines at positions: {blank_lines}\n"
            "No blank lines are allowed in the report."
        )


def test_archive_subdirectories_unchanged():
    """Verify that the archive directory structure was not modified."""
    subdirs = sorted([
        entry.name
        for entry in os.scandir(ARCHIVE_DIR)
        if entry.is_dir()
    ])
    expected_subdirs = sorted(["videos", "docs", "logs", "configs"])
    assert subdirs == expected_subdirs, (
        f"Archive subdirectories have changed.\n"
        f"Expected: {expected_subdirs}\n"
        f"Got: {subdirs}"
    )


def test_source_files_still_intact():
    """Verify the original files in the archive are still present and correct size."""
    files_and_sizes = [
        ("/home/user/archive/videos/clip.bin", 40960),
        ("/home/user/archive/docs/manual.bin", 20480),
        ("/home/user/archive/logs/app.bin", 8192),
        ("/home/user/archive/configs/settings.bin", 4096),
    ]
    for filepath, expected_size in files_and_sizes:
        assert os.path.isfile(filepath), (
            f"Source file {filepath} is missing. It should not have been removed."
        )
        actual_size = os.path.getsize(filepath)
        assert actual_size == expected_size, (
            f"Source file {filepath} has wrong size: "
            f"expected {expected_size} bytes, got {actual_size} bytes."
        )