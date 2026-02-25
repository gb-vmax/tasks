# test_final_state.py

"""
Pytest suite to validate the FINAL state of the OS/container
after processing /home/user/data/sales.csv as described.

Checks:
- /home/user/data/clean_sales.csv exists, is correct, and contains only well-formed rows (with header).
- /home/user/data/sales_errors.log exists, is correct, and contains one line per malformed row (in order).
- Only these two files are changed or created (no other new files in /home/user/data).
"""

import os
import pytest

DATA_DIR = "/home/user/data"
SALES_CSV = os.path.join(DATA_DIR, "sales.csv")
CLEAN_SALES_CSV = os.path.join(DATA_DIR, "clean_sales.csv")
SALES_ERRORS_LOG = os.path.join(DATA_DIR, "sales_errors.log")

# The expected contents, including newlines, as per the privileged truth data
EXPECTED_CLEAN_SALES_CSV = (
    "ID,Date,Customer,Amount\n"
    "1001,2023-01-01,Smith,500\n"
    "1002,2023-01-02,Williams,300\n"
    "1003,2023-01-03,\"O'Reilly, Jr.\",700\n"
    "1004,2023-01-04,Evans,200\n"
    "1005,2023-01-05,\"Miller, Anna\",missing_amount\n"
    "1006,2023-01-06,Patel,800\n"
    "1007,2023-01-07,Chen,600\n"
)

EXPECTED_SALES_ERRORS_LOG = (
    "BADLINE_MISSING_COLUMN\n"
    "BROKEN,\"2023-01-08,Lee\n"
    ",\n"
)

@pytest.mark.describe("Final OS/filesystem state for sales.csv cleaning task")
class TestFinalState:

    def test_clean_sales_csv_exists_and_contents(self):
        """Check that clean_sales.csv exists and contains the correct, well-formed rows only."""
        assert os.path.isfile(CLEAN_SALES_CSV), (
            f"Expected output file '{CLEAN_SALES_CSV}' was not created."
        )
        with open(CLEAN_SALES_CSV, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == EXPECTED_CLEAN_SALES_CSV, (
            f"File '{CLEAN_SALES_CSV}' does not have the expected contents.\n"
            "If there are missing or extra lines, malformed rows, or wrong formatting, fix your output.\n"
            "Expected:\n"
            f"{EXPECTED_CLEAN_SALES_CSV!r}\nGot:\n{content!r}"
        )

    def test_sales_errors_log_exists_and_contents(self):
        """Check that sales_errors.log exists and contains only the malformed lines (one per line, in order)."""
        assert os.path.isfile(SALES_ERRORS_LOG), (
            f"Expected log file '{SALES_ERRORS_LOG}' was not created."
        )
        with open(SALES_ERRORS_LOG, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == EXPECTED_SALES_ERRORS_LOG, (
            f"File '{SALES_ERRORS_LOG}' does not have the expected contents.\n"
            "Each malformed row must be logged on its own line, in the order encountered.\n"
            "Expected:\n"
            f"{EXPECTED_SALES_ERRORS_LOG!r}\nGot:\n{content!r}"
        )

    def test_no_other_files_changed_or_created(self):
        """Ensure only clean_sales.csv and sales_errors.log were created/changed in /home/user/data."""
        allowed = {"sales.csv", "clean_sales.csv", "sales_errors.log"}
        found = set(os.listdir(DATA_DIR))
        extra = found - allowed
        assert not extra, (
            f"Unexpected files or directories found in '{DATA_DIR}': {sorted(extra)}.\n"
            "Only 'clean_sales.csv' and 'sales_errors.log' should be created or changed."
        )

    def test_sales_csv_unmodified(self):
        """Ensure that the original sales.csv is unchanged (not overwritten or truncated)."""
        expected_lines = [
            "ID,Date,Customer,Amount\n",
            "1001,2023-01-01,Smith,500\n",
            "1002,2023-01-02,Williams,300\n",
            "BADLINE_MISSING_COLUMN\n",
            "1003,2023-01-03,\"O'Reilly, Jr.\",700\n",
            "1004,2023-01-04,Evans,200\n",
            "1005,2023-01-05,\"Miller, Anna\",missing_amount\n",
            "1006,2023-01-06,Patel,800\n",
            "1007,2023-01-07,Chen,600\n",
            "BROKEN,\"2023-01-08,Lee\n",
            ",\n",
        ]
        assert os.path.isfile(SALES_CSV), (
            f"Original input file '{SALES_CSV}' is missing after processing. Do not delete or overwrite it."
        )
        with open(SALES_CSV, "r", encoding="utf-8") as f:
            content = f.readlines()
        assert content == expected_lines, (
            f"File '{SALES_CSV}' was modified during processing. "
            "You must not alter the original input file."
        )