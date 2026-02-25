# test_final_state.py

import os
import tarfile
import pytest
import re
from datetime import datetime

HOME = "/home/user"
ETL_DATA_DIR = os.path.join(HOME, "etl_data")
CSV_FILES = ["data1.csv", "data2.csv", "data3.csv"]
ARCHIVE_PATH = os.path.join(HOME, "etl_backup_2024_06_15.tar.gz")
LOG_PATH = os.path.join(HOME, "etl_backup_log.txt")

@pytest.mark.describe("Final state: Backup archive exists with correct contents")
def test_archive_exists_and_contents():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Backup archive '{ARCHIVE_PATH}' does not exist. "
        "You must create the archive at the specified path."
    )
    # Check that it's a valid gzip-compressed tar archive and has correct files
    try:
        with tarfile.open(ARCHIVE_PATH, mode='r:gz') as tf:
            tar_members = tf.getnames()
    except Exception as exc:
        pytest.fail(f"Could not open '{ARCHIVE_PATH}' as a gzip-compressed tar archive: {exc}")

    # All files should be inside etl_data/, not nested further, and all must be present
    expected_members = [f"etl_data/{fname}" for fname in CSV_FILES]
    tar_members_set = set(tar_members)
    expected_set = set(expected_members)

    missing = expected_set - tar_members_set
    extra = tar_members_set - expected_set

    assert not missing, (
        f"Archive '{ARCHIVE_PATH}' is missing required file(s): {', '.join(sorted(missing))}.\n"
        "Ensure all three CSV files are included as 'etl_data/data1.csv', etc."
    )
    # Accept only the three files (no extra files or directories)
    # Allow possible directory entry for etl_data/ itself, but nothing else
    allowed = set(expected_members)
    allowed.add("etl_data")  # directory entry may be present
    unexpected = tar_members_set - allowed
    assert not unexpected, (
        f"Archive '{ARCHIVE_PATH}' contains unexpected file(s): {', '.join(sorted(unexpected))}.\n"
        "It should only contain 'etl_data/data1.csv', 'etl_data/data2.csv', and 'etl_data/data3.csv'."
    )

@pytest.mark.describe("Final state: Log file exists and matches required format")
def test_log_file_exists_and_format():
    assert os.path.isfile(LOG_PATH), (
        f"Log file '{LOG_PATH}' does not exist. "
        "You must produce the log file at the specified path."
    )

    with open(LOG_PATH, "rt", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]

    # There must be exactly 5 lines: 1 (timestamp), 1 (header), 3 (csv filenames)
    assert len(lines) == 5, (
        f"Log file '{LOG_PATH}' should contain exactly 5 lines, but has {len(lines)}.\n"
        "Format should be:\n"
        "Backup completed on: <YYYY-MM-DD HH:MM:SS>\n"
        "Files in archive:\n"
        "data1.csv\n"
        "data2.csv\n"
        "data3.csv"
    )

    # Check first line: Backup completed on: <YYYY-MM-DD HH:MM:SS>
    ts_line = lines[0]
    ts_regex = r"^Backup completed on: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})$"
    match = re.match(ts_regex, ts_line)
    assert match, (
        f"First line of '{LOG_PATH}' is invalid: '{ts_line}'.\n"
        "It must be exactly: 'Backup completed on: <YYYY-MM-DD HH:MM:SS>'"
    )
    # Validate date/time format (should be a real date/time)
    timestamp_str = match.group(1)
    try:
        datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        pytest.fail(
            f"Timestamp in first line of '{LOG_PATH}' is not a valid date/time: '{timestamp_str}'.\n"
            "Expected format is 'YYYY-MM-DD HH:MM:SS'."
        )

    # Check second line
    assert lines[1] == "Files in archive:", (
        f"Second line of '{LOG_PATH}' must be exactly 'Files in archive:'.\n"
        f"Found: '{lines[1]}'"
    )

    # Check file list: alphabetical order, no path, no extra spaces
    log_csvs = lines[2:]
    assert log_csvs == sorted(CSV_FILES), (
        f"The CSV file list in '{LOG_PATH}' must be exactly:\n"
        "data1.csv\ndata2.csv\ndata3.csv\n"
        f"But found:\n{chr(10).join(log_csvs)}"
    )

    # Ensure no paths or extra spaces in file names
    for fname in log_csvs:
        assert fname in CSV_FILES, (
            f"Log file '{LOG_PATH}' lists unexpected file '{fname}'. "
            "Only data1.csv, data2.csv, and data3.csv should be listed, with no paths or extra spaces."
        )
        assert "/" not in fname and "\\" not in fname, (
            f"Log file '{LOG_PATH}' entry '{fname}' must not contain any path components."
        )
        assert fname == fname.strip(), (
            f"Log file '{LOG_PATH}' entry '{fname}' should not have leading/trailing spaces."
        )

@pytest.mark.describe("Final state: Output files are writable")
@pytest.mark.parametrize("output_path", [ARCHIVE_PATH, LOG_PATH])
def test_output_files_are_writable(output_path):
    assert os.access(output_path, os.W_OK), (
        f"Output file '{output_path}' is not writable. "
        "Ensure you have write permissions to the output files."
    )