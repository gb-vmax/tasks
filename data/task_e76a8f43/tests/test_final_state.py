# test_final_state.py

import os
import pytest
import re

RAW_DATA_PATH = "/home/user/raw_data.csv"
CLEANED_DATA_PATH = "/home/user/cleaned_data.csv"
LOG_PATH = "/home/user/processing.log"

RAW_DATA_EXPECTED = (
    "id,name,age,department,salary,hire_date\n"
    "1,Jane Doe,34,Engineering,92000,2018-06-21\n"
    "2,John Smith,29,Marketing,67000,2019-12-01\n"
    "3,Amy Adams,41,Engineering,105000,2016-03-17\n"
    "4,Mark Lee,52,Human Resources,98000,2010-09-06\n"
    "5,Leila Chan,37,Finance,88000,2015-11-23\n"
)

CLEANED_DATA_EXPECTED = (
    "department,name,salary\n"
    "Engineering,Jane Doe,92000\n"
    "Marketing,John Smith,67000\n"
    "Engineering,Amy Adams,105000\n"
    "Human Resources,Mark Lee,98000\n"
    "Finance,Leila Chan,88000\n"
)

LOG_ENTRY_REGEX = re.compile(
    r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] Cleaned data written to /home/user/cleaned_data\.csv\n?$"
)

@pytest.mark.describe("Final OS/filesystem state after data cleaning")
class TestFinalState:

    def test_raw_data_csv_untouched(self):
        """Check that /home/user/raw_data.csv still exists and is unchanged."""
        assert os.path.isfile(RAW_DATA_PATH), (
            f"Expected original data file {RAW_DATA_PATH} to still exist after processing."
        )
        with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        if content != RAW_DATA_EXPECTED:
            import difflib
            diff = "\n".join(
                difflib.unified_diff(
                    RAW_DATA_EXPECTED.splitlines(),
                    content.splitlines(),
                    fromfile="expected",
                    tofile="actual",
                    lineterm=""
                )
            )
            pytest.fail(
                f"{RAW_DATA_PATH} was modified during processing. It must remain unchanged.\nDiff:\n{diff}"
            )

    def test_cleaned_data_csv_exists(self):
        """Check that /home/user/cleaned_data.csv exists."""
        assert os.path.isfile(CLEANED_DATA_PATH), (
            f"Expected output file {CLEANED_DATA_PATH} does not exist. "
            "The cleaned dataset must be created at the specified path."
        )

    def test_cleaned_data_csv_content(self):
        """Check the content of /home/user/cleaned_data.csv matches the expected cleaned output."""
        try:
            with open(CLEANED_DATA_PATH, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            pytest.fail(f"Cleaned dataset file {CLEANED_DATA_PATH} does not exist.")

        # No extra whitespace, blank lines, or altered data
        if content != CLEANED_DATA_EXPECTED:
            import difflib
            diff = "\n".join(
                difflib.unified_diff(
                    CLEANED_DATA_EXPECTED.splitlines(),
                    content.splitlines(),
                    fromfile="expected",
                    tofile="actual",
                    lineterm=""
                )
            )
            pytest.fail(
                f"{CLEANED_DATA_PATH} does not match the expected cleaned output.\nDiff:\n{diff}"
            )

    def test_cleaned_data_csv_no_extra_lines(self):
        """Ensure there are no extra blank lines at the end of cleaned_data.csv."""
        with open(CLEANED_DATA_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Should be exactly 6 lines: 1 header, 5 data rows
        assert len(lines) == 6, (
            f"{CLEANED_DATA_PATH} should have exactly 6 lines (1 header + 5 data rows), "
            f"but found {len(lines)} lines."
        )
        # No trailing blank lines
        assert all(line.strip() for line in lines), (
            f"{CLEANED_DATA_PATH} contains blank lines. There should be no blank lines."
        )

    def test_cleaned_data_csv_format(self):
        """Ensure the CSV is comma-delimited and columns are in correct order."""
        with open(CLEANED_DATA_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        header = lines[0].strip()
        assert header == "department,name,salary", (
            f"CSV header is '{header}', but expected 'department,name,salary'."
        )
        for i, line in enumerate(lines[1:], 2):
            fields = line.strip().split(",")
            assert len(fields) == 3, (
                f"Row {i} of {CLEANED_DATA_PATH} does not have exactly 3 columns: {line.strip()}"
            )

    def test_processing_log_entry_appended(self):
        """Check that the processing log contains a valid entry for cleaned_data.csv at the end."""
        assert os.path.isfile(LOG_PATH), (
            f"Processing log file {LOG_PATH} does not exist. "
            "A log entry must be appended after processing."
        )
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        assert lines, (
            f"{LOG_PATH} is empty. It should contain at least one log entry."
        )
        last_line = lines[-1]
        if not LOG_ENTRY_REGEX.match(last_line):
            pytest.fail(
                f"The last line of {LOG_PATH} does not match the expected log entry format.\n"
                f"Expected format: '[YYYY-MM-DD HH:MM:SS] Cleaned data written to /home/user/cleaned_data.csv'\n"
                f"Actual last line: {last_line!r}"
            )

    def test_processing_log_entry_not_overwritten(self):
        """Ensure that the log file preserves previous entries and only appends."""
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # The log entry must be ONLY at the end, not anywhere else
        entry_count = sum(
            1 for line in lines if "Cleaned data written to /home/user/cleaned_data.csv" in line
        )
        assert entry_count == 1, (
            f"{LOG_PATH} should contain exactly one occurrence of the cleaned data log entry at the end, "
            f"but found {entry_count} occurrences."
        )

    def test_log_entry_datetime_format(self):
        """Check that the log entry has a valid timestamp in the correct format."""
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            last_line = f.readlines()[-1]
        m = LOG_ENTRY_REGEX.match(last_line)
        assert m is not None, (
            f"The last line of {LOG_PATH} does not match the expected log entry format."
        )
        datetime_str = m.group(1)
        from datetime import datetime
        try:
            dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            pytest.fail(
                f"The timestamp '{datetime_str}' in the log entry is not in the required YYYY-MM-DD HH:MM:SS format."
            )