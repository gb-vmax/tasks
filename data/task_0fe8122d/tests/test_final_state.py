# test_final_state.py

import os
import re
import subprocess
import pytest

REPORT_PATH = "/home/user/disk_report.txt"
PIPELINE_DIR = "/home/user/pipeline_data"

EXPECTED_ORDER = [
    "/home/user/pipeline_data/archives",
    "/home/user/pipeline_data/processed",
    "/home/user/pipeline_data/raw_inputs",
    "/home/user/pipeline_data/tmp_scratch",
    "/home/user/pipeline_data/logs",
]

LINE_PATTERN = re.compile(r"^\S+\t/home/user/pipeline_data/\w+$")


@pytest.fixture(scope="module")
def report_lines():
    """Read and return non-empty lines from the report file."""
    assert os.path.isfile(REPORT_PATH), (
        f"Report file {REPORT_PATH} does not exist. "
        "The task has not been completed yet."
    )
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    return lines


def test_report_file_exists():
    """The report file must exist."""
    assert os.path.isfile(REPORT_PATH), (
        f"Report file {REPORT_PATH} does not exist. "
        "Please run the disk usage analysis and write the report."
    )


def test_report_has_exactly_5_lines(report_lines):
    """The report must contain exactly 5 lines (one per subdirectory)."""
    assert len(report_lines) == 5, (
        f"Expected exactly 5 lines in {REPORT_PATH}, "
        f"but found {len(report_lines)} lines. "
        f"Content:\n" + "\n".join(repr(l) for l in report_lines)
    )


def test_no_blank_lines(report_lines):
    """There must be no blank lines in the report."""
    blank_indices = [i for i, line in enumerate(report_lines) if line.strip() == ""]
    assert not blank_indices, (
        f"Found blank lines at positions (0-indexed): {blank_indices} "
        f"in {REPORT_PATH}. No blank lines are allowed."
    )


def test_each_line_matches_format(report_lines):
    """Each line must match the pattern: <size>\\t<absolute_path>."""
    for i, line in enumerate(report_lines):
        assert LINE_PATTERN.match(line), (
            f"Line {i + 1} does not match expected format "
            f"'<size>\\t/home/user/pipeline_data/<subdir>'.\n"
            f"Actual line: {line!r}\n"
            f"Expected pattern: {LINE_PATTERN.pattern}"
        )


def test_first_line_is_archives(report_lines):
    """The first line must refer to the archives subdirectory (largest)."""
    assert "/home/user/pipeline_data/archives" in report_lines[0], (
        f"Expected the first line to contain '/home/user/pipeline_data/archives' "
        f"(largest directory), but got: {report_lines[0]!r}"
    )


def test_second_line_is_processed(report_lines):
    """The second line must refer to the processed subdirectory."""
    assert "/home/user/pipeline_data/processed" in report_lines[1], (
        f"Expected the second line to contain '/home/user/pipeline_data/processed', "
        f"but got: {report_lines[1]!r}"
    )


def test_third_line_is_raw_inputs(report_lines):
    """The third line must refer to the raw_inputs subdirectory."""
    assert "/home/user/pipeline_data/raw_inputs" in report_lines[2], (
        f"Expected the third line to contain '/home/user/pipeline_data/raw_inputs', "
        f"but got: {report_lines[2]!r}"
    )


def test_last_line_is_logs(report_lines):
    """The last line must refer to the logs subdirectory (smallest)."""
    assert "/home/user/pipeline_data/logs" in report_lines[-1], (
        f"Expected the last line to contain '/home/user/pipeline_data/logs' "
        f"(smallest directory), but got: {report_lines[-1]!r}"
    )


def test_all_five_subdirectories_present(report_lines):
    """All five expected subdirectories must appear in the report."""
    expected_subdirs = {
        "/home/user/pipeline_data/archives",
        "/home/user/pipeline_data/processed",
        "/home/user/pipeline_data/raw_inputs",
        "/home/user/pipeline_data/tmp_scratch",
        "/home/user/pipeline_data/logs",
    }
    found = set()
    for line in report_lines:
        for subdir in expected_subdirs:
            if subdir in line:
                found.add(subdir)
    missing = expected_subdirs - found
    assert not missing, (
        f"The following subdirectories are missing from {REPORT_PATH}: {missing}\n"
        f"Report content:\n" + "\n".join(report_lines)
    )


def test_order_archives_before_processed(report_lines):
    """archives must appear before processed in the report."""
    indices = {}
    for i, line in enumerate(report_lines):
        if "/home/user/pipeline_data/archives" in line:
            indices["archives"] = i
        if "/home/user/pipeline_data/processed" in line:
            indices["processed"] = i
    assert "archives" in indices, "archives not found in report"
    assert "processed" in indices, "processed not found in report"
    assert indices["archives"] < indices["processed"], (
        f"'archives' (line {indices['archives'] + 1}) must appear before "
        f"'processed' (line {indices['processed'] + 1}) in {REPORT_PATH}."
    )


def test_order_processed_before_raw_inputs(report_lines):
    """processed must appear before raw_inputs in the report."""
    indices = {}
    for i, line in enumerate(report_lines):
        if "/home/user/pipeline_data/processed" in line:
            indices["processed"] = i
        if "/home/user/pipeline_data/raw_inputs" in line:
            indices["raw_inputs"] = i
    assert "processed" in indices, "processed not found in report"
    assert "raw_inputs" in indices, "raw_inputs not found in report"
    assert indices["processed"] < indices["raw_inputs"], (
        f"'processed' (line {indices['processed'] + 1}) must appear before "
        f"'raw_inputs' (line {indices['raw_inputs'] + 1}) in {REPORT_PATH}."
    )


def test_order_raw_inputs_before_tmp_scratch(report_lines):
    """raw_inputs must appear before tmp_scratch in the report."""
    indices = {}
    for i, line in enumerate(report_lines):
        if "/home/user/pipeline_data/raw_inputs" in line:
            indices["raw_inputs"] = i
        if "/home/user/pipeline_data/tmp_scratch" in line:
            indices["tmp_scratch"] = i
    assert "raw_inputs" in indices, "raw_inputs not found in report"
    assert "tmp_scratch" in indices, "tmp_scratch not found in report"
    assert indices["raw_inputs"] < indices["tmp_scratch"], (
        f"'raw_inputs' (line {indices['raw_inputs'] + 1}) must appear before "
        f"'tmp_scratch' (line {indices['tmp_scratch'] + 1}) in {REPORT_PATH}."
    )


def test_order_tmp_scratch_before_logs(report_lines):
    """tmp_scratch must appear before logs in the report."""
    indices = {}
    for i, line in enumerate(report_lines):
        if "/home/user/pipeline_data/tmp_scratch" in line:
            indices["tmp_scratch"] = i
        if "/home/user/pipeline_data/logs" in line:
            indices["logs"] = i
    assert "tmp_scratch" in indices, "tmp_scratch not found in report"
    assert "logs" in indices, "logs not found in report"
    assert indices["tmp_scratch"] < indices["logs"], (
        f"'tmp_scratch' (line {indices['tmp_scratch'] + 1}) must appear before "
        f"'logs' (line {indices['logs'] + 1}) in {REPORT_PATH}."
    )


def test_each_line_has_tab_separator(report_lines):
    """Each line must use a tab character to separate size from path."""
    for i, line in enumerate(report_lines):
        assert "\t" in line, (
            f"Line {i + 1} does not contain a tab separator between size and path.\n"
            f"Actual line: {line!r}\n"
            "Expected format: '<size>\\t<path>'"
        )


def test_each_line_path_is_immediate_subdir(report_lines):
    """Each line's path must be a direct child of the pipeline directory."""
    for i, line in enumerate(report_lines):
        parts = line.split("\t", 1)
        assert len(parts) == 2, (
            f"Line {i + 1} could not be split into size and path: {line!r}"
        )
        path = parts[1].strip()
        parent = os.path.dirname(path)
        assert parent == PIPELINE_DIR, (
            f"Line {i + 1}: path {path!r} is not an immediate subdirectory of "
            f"{PIPELINE_DIR!r}. Parent was {parent!r}."
        )


def test_report_sizes_are_human_readable(report_lines):
    """Each size field must be in human-readable format (e.g., 1.0M, 500K, 20K)."""
    human_readable_pattern = re.compile(r"^\d+(\.\d+)?[KMGTP]?$")
    for i, line in enumerate(report_lines):
        parts = line.split("\t", 1)
        if len(parts) < 2:
            continue
        size_str = parts[0].strip()
        assert human_readable_pattern.match(size_str), (
            f"Line {i + 1}: size field {size_str!r} does not look like a "
            f"human-readable size (e.g., '1.0M', '500K', '20K'). "
            f"Full line: {line!r}"
        )


def test_report_no_pipeline_dir_itself(report_lines):
    """The report must not contain a line for the pipeline_data directory itself."""
    for i, line in enumerate(report_lines):
        parts = line.split("\t", 1)
        if len(parts) == 2:
            path = parts[1].strip()
            assert path != PIPELINE_DIR, (
                f"Line {i + 1} refers to the pipeline_data directory itself "
                f"({PIPELINE_DIR!r}), which should not be included. "
                "Only immediate subdirectories should be listed."
            )


def test_report_is_sorted_largest_to_smallest(report_lines):
    """
    Verify the sort order is correct by comparing actual du byte sizes
    against the order in the report.
    """
    # Get actual byte sizes for each subdir
    subdir_paths = [
        "/home/user/pipeline_data/archives",
        "/home/user/pipeline_data/processed",
        "/home/user/pipeline_data/raw_inputs",
        "/home/user/pipeline_data/tmp_scratch",
        "/home/user/pipeline_data/logs",
    ]
    result = subprocess.run(
        ["du", "-s", "--block-size=1"] + subdir_paths,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"du command failed: {result.stderr}"
    )
    byte_sizes = {}
    for line in result.stdout.strip().splitlines():
        parts = line.split("\t", 1)
        if len(parts) == 2:
            byte_sizes[parts[1].strip()] = int(parts[0])

    # Extract paths from report lines in order
    report_paths = []
    for line in report_lines:
        parts = line.split("\t", 1)
        if len(parts) == 2:
            report_paths.append(parts[1].strip())

    # Check that sizes are non-increasing
    for i in range(len(report_paths) - 1):
        path_a = report_paths[i]
        path_b = report_paths[i + 1]
        if path_a in byte_sizes and path_b in byte_sizes:
            assert byte_sizes[path_a] >= byte_sizes[path_b], (
                f"Report is not sorted largest-to-smallest: "
                f"{path_a!r} ({byte_sizes[path_a]} bytes) appears before "
                f"{path_b!r} ({byte_sizes[path_b]} bytes), but the latter is larger."
            )