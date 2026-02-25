# test_final_state.py

import os
import pytest

DIRTY_DATA_PATH = "/home/user/data/dirty_data.csv"
CLEAN_DATA_PATH = "/home/user/data/clean_data.csv"
CLEANING_LOG_PATH = "/home/user/data/cleaning_log.txt"

EXPECTED_CLEAN_DATA = (
    "id,value,label\n"
    "1,12.5,A\n"
    "4,6.8,D\n"
    "5,7.2,E\n"
)

EXPECTED_LOG_LINES = [
    "Removed 2 rows due to invalid or missing values",
    "Remaining rows: 3",
    "Success"
]

@pytest.mark.describe("Final State Validation")
class TestFinalState:

    def test_clean_data_csv_exists(self):
        assert os.path.isfile(CLEAN_DATA_PATH), (
            f"Missing expected output file: {CLEAN_DATA_PATH}. "
            "The cleaned CSV must exist at the specified path after the task is completed."
        )

    def test_clean_data_csv_content(self):
        with open(CLEAN_DATA_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        assert content == EXPECTED_CLEAN_DATA, (
            f"The content of {CLEAN_DATA_PATH} does not match the expected cleaned data.\n"
            "Expected:\n"
            f"{EXPECTED_CLEAN_DATA}\n"
            "Found:\n"
            f"{content}\n"
            "Ensure the file contains only valid rows, with the header preserved and line endings correct."
        )

    def test_cleaning_log_txt_exists(self):
        assert os.path.isfile(CLEANING_LOG_PATH), (
            f"Missing expected log file: {CLEANING_LOG_PATH}. "
            "The log file must exist at the specified path after the task is completed."
        )

    def test_cleaning_log_txt_content(self):
        with open(CLEANING_LOG_PATH, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        assert len(lines) == 3, (
            f"The log file {CLEANING_LOG_PATH} must have exactly 3 lines.\n"
            f"Found {len(lines)} lines: {lines}"
        )
        for i, (actual, expected) in enumerate(zip(lines, EXPECTED_LOG_LINES), 1):
            assert actual == expected, (
                f"Line {i} of {CLEANING_LOG_PATH} is incorrect.\n"
                f"Expected: '{expected}'\n"
                f"Found:    '{actual}'"
            )

    def test_clean_data_csv_header_matches_dirty_data(self):
        """Ensure the header in clean_data.csv exactly matches the dirty_data.csv header."""
        with open(DIRTY_DATA_PATH, 'r', encoding='utf-8') as f:
            dirty_header = f.readline().rstrip('\n')
        with open(CLEAN_DATA_PATH, 'r', encoding='utf-8') as f:
            clean_header = f.readline().rstrip('\n')
        assert clean_header == dirty_header, (
            f"The header row in {CLEAN_DATA_PATH} does not match the original header in {DIRTY_DATA_PATH}.\n"
            f"Expected header: '{dirty_header}'\n"
            f"Found header:    '{clean_header}'"
        )

    def test_clean_data_csv_no_extra_rows(self):
        """Ensure clean_data.csv contains exactly the expected rows after the header."""
        with open(CLEAN_DATA_PATH, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        assert len(lines) == 4, (
            f"{CLEAN_DATA_PATH} should have exactly 1 header and 3 data rows (total 4 lines).\n"
            f"Found {len(lines)} lines: {lines}"
        )
        # Check that only the allowed IDs are present in the cleaned data
        valid_ids = {"1", "4", "5"}
        for i, line in enumerate(lines[1:], 2):  # skip header
            row_id = line.partition(',')[0]
            assert row_id in valid_ids, (
                f"Unexpected row at line {i} in {CLEAN_DATA_PATH}: '{line}'.\n"
                f"Only rows with id 1, 4, and 5 should remain after cleaning."
            )

    def test_dirty_data_csv_untouched(self):
        """Ensure the original dirty_data.csv is unchanged."""
        expected = (
            "id,value,label\n"
            "1,12.5,A\n"
            "2,,B\n"
            "3,not_a_number,C\n"
            "4,6.8,D\n"
            "5,7.2,E\n"
        )
        with open(DIRTY_DATA_PATH, 'r', encoding='utf-8') as f:
            actual = f.read()
        assert actual == expected, (
            f"The file {DIRTY_DATA_PATH} should not be modified during the cleaning process.\n"
            "If it was changed, restore it to its original state."
        )