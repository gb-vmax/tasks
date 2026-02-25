# test_final_state.py

import os
import pytest

DATA_ANALYSIS_DIR = "/home/user/data_analysis"
CSV_FILES = {
    "small_dataset.csv": 15000,
    "medium_dataset.csv": 52000,
    "large_dataset.csv": 105500,
}
REPORT_FILE = os.path.join(DATA_ANALYSIS_DIR, "csv_disk_usage_report.txt")
SUMMARY_FILE = os.path.join(DATA_ANALYSIS_DIR, "csv_disk_usage_summary.txt")

EXPECTED_REPORT_CONTENT = (
    "large_dataset.csv,105500\n"
    "medium_dataset.csv,52000\n"
    "small_dataset.csv,15000\n"
)

EXPECTED_SUMMARY_CONTENT = (
    "3\n"
    "172500\n"
    "57500\n"
)

@pytest.mark.parametrize("fname,expected_size", CSV_FILES.items())
def test_csv_file_exists_and_size_final(fname, expected_size):
    """Check that each expected CSV file still exists with the correct size."""
    fpath = os.path.join(DATA_ANALYSIS_DIR, fname)
    assert os.path.exists(fpath), f"Missing file after task: {fpath}"
    assert os.path.isfile(fpath), f"Not a file after task: {fpath}"
    actual_size = os.path.getsize(fpath)
    assert actual_size == expected_size, (
        f"File {fpath} has size {actual_size}, expected {expected_size} after task"
    )

def test_only_expected_csv_files_present_final():
    """Ensure only the expected CSV files are present (no extra .csv files) after task."""
    files_in_dir = set(
        f for f in os.listdir(DATA_ANALYSIS_DIR)
        if os.path.isfile(os.path.join(DATA_ANALYSIS_DIR, f))
    )
    csv_files_in_dir = {f for f in files_in_dir if f.lower().endswith('.csv')}
    expected_csvs = set(CSV_FILES.keys())
    missing = expected_csvs - csv_files_in_dir
    extra = csv_files_in_dir - expected_csvs
    assert not missing, (
        f"Missing expected CSV files after task: {', '.join(sorted(missing))}"
    )
    assert not extra, (
        f"Found unexpected CSV files after task: {', '.join(sorted(extra))}"
    )

def test_report_file_exists_and_content():
    """Check that the report file exists and has the exact expected content."""
    assert os.path.exists(REPORT_FILE), (
        f"Report file missing after task: {REPORT_FILE}"
    )
    assert os.path.isfile(REPORT_FILE), (
        f"Report file is not a file after task: {REPORT_FILE}"
    )
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_REPORT_CONTENT, (
        "csv_disk_usage_report.txt content is incorrect.\n"
        "Expected:\n"
        f"{EXPECTED_REPORT_CONTENT!r}\n"
        "Got:\n"
        f"{content!r}"
    )

def test_summary_file_exists_and_content():
    """Check that the summary file exists and has the exact expected content."""
    assert os.path.exists(SUMMARY_FILE), (
        f"Summary file missing after task: {SUMMARY_FILE}"
    )
    assert os.path.isfile(SUMMARY_FILE), (
        f"Summary file is not a file after task: {SUMMARY_FILE}"
    )
    with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_SUMMARY_CONTENT, (
        "csv_disk_usage_summary.txt content is incorrect.\n"
        "Expected:\n"
        f"{EXPECTED_SUMMARY_CONTENT!r}\n"
        "Got:\n"
        f"{content!r}"
    )

def test_no_extra_files_created():
    """
    Ensure that no additional files (other than the original .csv files, report, and summary)
    exist in /home/user/data_analysis after the task.
    """
    allowed_files = set(CSV_FILES.keys()) | {
        "csv_disk_usage_report.txt",
        "csv_disk_usage_summary.txt",
    }
    files_in_dir = set(
        f for f in os.listdir(DATA_ANALYSIS_DIR)
        if os.path.isfile(os.path.join(DATA_ANALYSIS_DIR, f))
    )
    extra = files_in_dir - allowed_files
    assert not extra, (
        f"Unexpected extra files found after task in {DATA_ANALYSIS_DIR}: {', '.join(sorted(extra))}"
    )

def test_no_report_or_summary_files_outside_target():
    """
    Ensure that no files named csv_disk_usage_report.txt or csv_disk_usage_summary.txt
    exist outside /home/user/data_analysis.
    """
    # Only check parent dir and root for safety, as full filesystem traversal is not allowed.
    parent_dir = os.path.dirname(DATA_ANALYSIS_DIR)
    forbidden_names = {"csv_disk_usage_report.txt", "csv_disk_usage_summary.txt"}
    for dirpath in ["/home/user", "/home"]:
        if not os.path.exists(dirpath):
            continue
        for fname in os.listdir(dirpath):
            if fname in forbidden_names:
                pytest.fail(
                    f"Forbidden file {fname} found outside {DATA_ANALYSIS_DIR} in {dirpath}"
                )

def test_data_analysis_is_still_directory():
    """Check that /home/user/data_analysis is still a directory after the task."""
    assert os.path.exists(DATA_ANALYSIS_DIR), f"Directory missing after task: {DATA_ANALYSIS_DIR}"
    assert os.path.isdir(DATA_ANALYSIS_DIR), f"Not a directory after task: {DATA_ANALYSIS_DIR}"

def test_no_csv_subdirectories_present():
    """Ensure there are no subdirectories named as .csv in /home/user/data_analysis after the task."""
    for entry in os.listdir(DATA_ANALYSIS_DIR):
        full_path = os.path.join(DATA_ANALYSIS_DIR, entry)
        if entry.lower().endswith('.csv') and os.path.isdir(full_path):
            pytest.fail(f"Unexpected subdirectory with .csv extension after task: {full_path}")