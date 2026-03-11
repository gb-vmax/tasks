# test_final_state.py

import os
import pytest

COST_REPORTS_DIR = "/home/user/cost_reports"
SUBDIR = "/home/user/cost_reports/subdir"
SAVINGS_REPORT = "/home/user/cost_reports/savings_report.txt"

# Files that must have been DELETED (large daily CSVs > 10KB)
DELETED_FILES = [
    "/home/user/cost_reports/daily_2024_01_15.csv",
    "/home/user/cost_reports/daily_2024_01_16.csv",
    "/home/user/cost_reports/subdir/daily_2024_01_17.csv",
]

# Files that must still EXIST after the task
SURVIVING_FILES = [
    ("/home/user/cost_reports/savings_report.txt", None),       # size checked separately
    ("/home/user/cost_reports/daily_2024_01_14.csv", 8000),
    ("/home/user/cost_reports/monthly_2024_01.csv", 25000),
    ("/home/user/cost_reports/subdir/monthly_2024_02.csv", 12000),
]

EXPECTED_TOTAL_BYTES = 55500
EXPECTED_SAVINGS_CONTENT = "55500\n"


# ---------------------------------------------------------------------------
# Directory structure
# ---------------------------------------------------------------------------

def test_cost_reports_directory_still_exists():
    assert os.path.isdir(COST_REPORTS_DIR), (
        f"Directory {COST_REPORTS_DIR} no longer exists. "
        "The base cost_reports directory must not be removed."
    )


def test_subdir_still_exists():
    assert os.path.isdir(SUBDIR), (
        f"Subdirectory {SUBDIR} no longer exists. "
        "The subdir must not be removed."
    )


# ---------------------------------------------------------------------------
# Large daily CSV files must be GONE
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filepath", DELETED_FILES)
def test_large_daily_file_deleted(filepath):
    assert not os.path.exists(filepath), (
        f"File {filepath} still exists but should have been deleted. "
        "All daily_*.csv files larger than 10KB must be removed."
    )


# ---------------------------------------------------------------------------
# Surviving files must still EXIST with correct sizes
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filepath,expected_size", SURVIVING_FILES)
def test_surviving_file_exists(filepath, expected_size):
    assert os.path.isfile(filepath), (
        f"File {filepath} does not exist but should have been preserved. "
        "Only large daily_*.csv files (>10KB) should be deleted."
    )


@pytest.mark.parametrize("filepath,expected_size", [
    (fp, sz) for fp, sz in SURVIVING_FILES if sz is not None
])
def test_surviving_file_size(filepath, expected_size):
    assert os.path.isfile(filepath), (
        f"File {filepath} does not exist, cannot check size."
    )
    actual_size = os.path.getsize(filepath)
    assert actual_size == expected_size, (
        f"File {filepath} has size {actual_size} bytes, "
        f"expected {expected_size} bytes. "
        "The file content must not have been modified."
    )


# ---------------------------------------------------------------------------
# savings_report.txt content
# ---------------------------------------------------------------------------

def test_savings_report_exists():
    assert os.path.isfile(SAVINGS_REPORT), (
        f"File {SAVINGS_REPORT} does not exist. "
        "The savings report must be created before deleting the large files."
    )


def test_savings_report_content_exact():
    assert os.path.isfile(SAVINGS_REPORT), (
        f"File {SAVINGS_REPORT} does not exist, cannot check content."
    )
    with open(SAVINGS_REPORT, "r") as f:
        content = f.read()
    assert content == EXPECTED_SAVINGS_CONTENT, (
        f"savings_report.txt contains {content!r}, "
        f"expected {EXPECTED_SAVINGS_CONTENT!r}. "
        f"The file must contain exactly the integer {EXPECTED_TOTAL_BYTES} "
        "followed by a newline."
    )


def test_savings_report_integer_value():
    assert os.path.isfile(SAVINGS_REPORT), (
        f"File {SAVINGS_REPORT} does not exist, cannot check integer value."
    )
    with open(SAVINGS_REPORT, "r") as f:
        content = f.read().strip()
    try:
        value = int(content)
    except ValueError:
        pytest.fail(
            f"savings_report.txt content {content!r} is not a valid integer. "
            "The file must contain only the total byte count as an integer."
        )
    assert value == EXPECTED_TOTAL_BYTES, (
        f"savings_report.txt contains the value {value}, "
        f"expected {EXPECTED_TOTAL_BYTES} "
        f"(15000 + 22000 + 18500 = {EXPECTED_TOTAL_BYTES}). "
        "The byte count must reflect the total size of all daily_*.csv files "
        "that were larger than 10KB."
    )


def test_savings_report_single_line():
    assert os.path.isfile(SAVINGS_REPORT), (
        f"File {SAVINGS_REPORT} does not exist, cannot check line count."
    )
    with open(SAVINGS_REPORT, "r") as f:
        lines = f.readlines()
    # Allow exactly one line with optional trailing newline
    non_empty_lines = [ln for ln in lines if ln.strip()]
    assert len(non_empty_lines) == 1, (
        f"savings_report.txt has {len(non_empty_lines)} non-empty line(s), "
        "expected exactly 1. "
        "The file must contain only the total byte count on a single line."
    )


# ---------------------------------------------------------------------------
# No unexpected daily_*.csv files larger than 10KB remain anywhere
# ---------------------------------------------------------------------------

def test_no_large_daily_csvs_remain():
    """Walk the entire cost_reports tree and ensure no daily_*.csv > 10KB exists."""
    found = []
    for root, dirs, files in os.walk(COST_REPORTS_DIR):
        for fname in files:
            if fname.startswith("daily_") and fname.endswith(".csv"):
                fpath = os.path.join(root, fname)
                size = os.path.getsize(fpath)
                if size > 10240:  # strictly greater than 10KB
                    found.append((fpath, size))
    assert not found, (
        "The following daily_*.csv files larger than 10KB still exist and "
        "should have been deleted:\n"
        + "\n".join(f"  {fp} ({sz} bytes)" for fp, sz in found)
    )


def test_small_daily_csv_untouched():
    """The 8000-byte daily CSV must still exist and be unmodified."""
    filepath = "/home/user/cost_reports/daily_2024_01_14.csv"
    assert os.path.isfile(filepath), (
        f"File {filepath} does not exist. "
        "Small daily_*.csv files (<=10KB) must NOT be deleted."
    )
    actual_size = os.path.getsize(filepath)
    assert actual_size == 8000, (
        f"File {filepath} has size {actual_size} bytes, expected 8000 bytes. "
        "The small daily CSV must remain completely untouched."
    )
    with open(filepath, "r") as f:
        content = f.read()
    assert content == "B" * 8000, (
        f"File {filepath} content has been modified. "
        "Expected 8000 'B' characters."
    )


def test_monthly_csv_root_untouched():
    """The monthly_2024_01.csv must still exist and be unmodified."""
    filepath = "/home/user/cost_reports/monthly_2024_01.csv"
    assert os.path.isfile(filepath), (
        f"File {filepath} does not exist. "
        "Non-daily CSV files must NOT be deleted."
    )
    actual_size = os.path.getsize(filepath)
    assert actual_size == 25000, (
        f"File {filepath} has size {actual_size} bytes, expected 25000 bytes."
    )


def test_monthly_csv_subdir_untouched():
    """The subdir/monthly_2024_02.csv must still exist and be unmodified."""
    filepath = "/home/user/cost_reports/subdir/monthly_2024_02.csv"
    assert os.path.isfile(filepath), (
        f"File {filepath} does not exist. "
        "Non-daily CSV files in subdirectories must NOT be deleted."
    )
    actual_size = os.path.getsize(filepath)
    assert actual_size == 12000, (
        f"File {filepath} has size {actual_size} bytes, expected 12000 bytes."
    )