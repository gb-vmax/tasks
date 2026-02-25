# test_final_state.py

import os
import pytest

DATA_PIPELINE_DIR = "/home/user/data_pipeline"
RAW_CSV = os.path.join(DATA_PIPELINE_DIR, "raw_customers.csv")
CLEANED_CSV = os.path.join(DATA_PIPELINE_DIR, "cleaned_customers.csv")
ERROR_LOG = os.path.join(DATA_PIPELINE_DIR, "error_rows.log")

EXPECTED_CLEANED_CSV_LINES = [
    "first_name,last_name,age,city\n",
    "Alice,Smith,29,San Francisco\n",
    "Charlie,Brown,34,New York\n",
    "Edward,Jones,43,Boston\n",
    ",Martinez,28,Miami\n",
]

EXPECTED_ERROR_LOG_LINES = [
    "Bob,,twenty five,Los Angeles\n",
    "\n",
    ",,,\n",
    "Dana,Lee,,Seattle\n",
    "\n",
]

@pytest.mark.describe("Final OS/filesystem state after data cleaning")
class TestFinalState:
    def test_cleaned_customers_csv_exists(self):
        assert os.path.isfile(CLEANED_CSV), (
            f"Expected output file '{CLEANED_CSV}' does not exist. "
            "You must create this file as part of the data cleaning step."
        )

    def test_error_rows_log_exists(self):
        assert os.path.isfile(ERROR_LOG), (
            f"Expected error log file '{ERROR_LOG}' does not exist. "
            "You must create this file to log all skipped lines."
        )

    def test_cleaned_customers_csv_contents(self):
        try:
            with open(CLEANED_CSV, "r", encoding="utf-8") as f:
                actual_lines = f.readlines()
        except Exception as e:
            pytest.fail(f"Could not read '{CLEANED_CSV}': {e}")

        # Normalize line endings to '\n'
        def normalize(lines):
            return [l if l == "\n" else l.rstrip('\r\n') + "\n" for l in lines]

        actual_norm = normalize(actual_lines)
        expected_norm = normalize(EXPECTED_CLEANED_CSV_LINES)
        assert actual_norm == expected_norm, (
            f"'{CLEANED_CSV}' does not have the expected contents.\n"
            f"--- Expected ---\n{''.join(expected_norm)}\n"
            f"--- Actual ---\n{''.join(actual_norm)}"
        )

    def test_cleaned_customers_csv_header(self):
        """Header must be present and exactly as in the original file."""
        try:
            with open(CLEANED_CSV, "r", encoding="utf-8") as f:
                header = f.readline()
        except Exception as e:
            pytest.fail(f"Could not read header from '{CLEANED_CSV}': {e}")

        expected_header = "first_name,last_name,age,city\n"
        assert header == expected_header, (
            f"Header of '{CLEANED_CSV}' is incorrect.\n"
            f"Expected: {repr(expected_header)}\n"
            f"Actual:   {repr(header)}"
        )

    def test_cleaned_customers_csv_row_count(self):
        """Should contain header plus exactly 4 valid data rows."""
        try:
            with open(CLEANED_CSV, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            pytest.fail(f"Could not read '{CLEANED_CSV}': {e}")

        assert len(lines) == 5, (
            f"'{CLEANED_CSV}' should have 5 lines (1 header + 4 valid rows), found {len(lines)} lines."
        )

    def test_no_blank_lines_in_cleaned_customers_csv(self):
        """No blank lines (i.e., lines that are only '\\n') should appear in cleaned CSV."""
        try:
            with open(CLEANED_CSV, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            pytest.fail(f"Could not read '{CLEANED_CSV}': {e}")

        blank_lines = [i+1 for i, l in enumerate(lines) if l == "\n"]
        assert not blank_lines, (
            f"Blank line(s) found in '{CLEANED_CSV}' at line(s): {blank_lines}. "
            "There should be no blank lines in the cleaned output."
        )

    def test_cleaned_customers_csv_fields_and_order(self):
        """Each data row must have exactly 4 comma-separated fields, preserving column order."""
        try:
            with open(CLEANED_CSV, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            pytest.fail(f"Could not read '{CLEANED_CSV}': {e}")

        header = lines[0]
        expected_header = "first_name,last_name,age,city\n"
        assert header == expected_header, (
            f"Header mismatch in '{CLEANED_CSV}':\nExpected: {repr(expected_header)}\nActual:   {repr(header)}"
        )

        for i, row in enumerate(lines[1:], start=2):
            fields = row.rstrip('\r\n').split(",")
            assert len(fields) == 4, (
                f"Row {i} in '{CLEANED_CSV}' does not have 4 fields as expected: {repr(row)}"
            )

    def test_error_rows_log_contents(self):
        try:
            with open(ERROR_LOG, "r", encoding="utf-8") as f:
                actual_lines = f.readlines()
        except Exception as e:
            pytest.fail(f"Could not read '{ERROR_LOG}': {e}")

        # Normalize line endings to '\n'
        def normalize(lines):
            return [l if l == "\n" else l.rstrip('\r\n') + "\n" for l in lines]

        actual_norm = normalize(actual_lines)
        expected_norm = normalize(EXPECTED_ERROR_LOG_LINES)
        assert actual_norm == expected_norm, (
            f"'{ERROR_LOG}' does not have the expected contents.\n"
            f"--- Expected ---\n{''.join(expected_norm)}\n"
            f"--- Actual ---\n{''.join(actual_norm)}"
        )

    def test_error_rows_log_no_header(self):
        """The error log should not contain the header line from the original CSV."""
        try:
            with open(ERROR_LOG, "r", encoding="utf-8") as f:
                contents = f.read()
        except Exception as e:
            pytest.fail(f"Could not read '{ERROR_LOG}': {e}")

        assert "first_name,last_name,age,city" not in contents, (
            f"The header line must NOT be present in '{ERROR_LOG}'."
        )

    def test_error_rows_log_includes_blank_lines(self):
        """Blank lines from the input must be present in the error log exactly as-is."""
        try:
            with open(ERROR_LOG, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            pytest.fail(f"Could not read '{ERROR_LOG}': {e}")

        blank_line_indices = [i for i, l in enumerate(EXPECTED_ERROR_LOG_LINES) if l == "\n"]
        for idx in blank_line_indices:
            assert lines[idx] == "\n", (
                f"Expected blank line at position {idx+1} in '{ERROR_LOG}' but got: {repr(lines[idx])}"
            )

    def test_only_expected_files_exist(self):
        """No unexpected files (e.g., extra output files) should be present in the data_pipeline directory."""
        expected_files = {"raw_customers.csv", "cleaned_customers.csv", "error_rows.log"}
        actual_files = set(os.listdir(DATA_PIPELINE_DIR))
        extra_files = actual_files - expected_files
        assert not extra_files, (
            f"Unexpected file(s) found in '{DATA_PIPELINE_DIR}': {sorted(extra_files)}. "
            f"Only {sorted(expected_files)} should be present after the cleaning task."
        )