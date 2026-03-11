# test_final_state.py

import os
import pytest

REPORT_CSV_PATH = "/home/user/data/sales_report.csv"
SALES_CSV_PATH = "/home/user/data/sales.csv"

EXPECTED_HEADER = "date,salesperson,total"

EXPECTED_ROWS = [
    "2024-01-15,Alice,59.90",
    "2024-01-16,Bob,74.97",
    "2024-01-17,Alice,41.93",
    "2024-01-18,Carol,99.98",
    "2024-01-19,Bob,89.85",
]

EXPECTED_CONTENT = "\n".join([EXPECTED_HEADER] + EXPECTED_ROWS) + "\n"


def test_report_csv_exists():
    assert os.path.exists(REPORT_CSV_PATH), (
        f"Output file not found: {REPORT_CSV_PATH}. "
        "The task requires creating this file."
    )


def test_report_csv_is_file():
    assert os.path.isfile(REPORT_CSV_PATH), (
        f"Path exists but is not a regular file: {REPORT_CSV_PATH}"
    )


def test_report_csv_is_readable():
    assert os.access(REPORT_CSV_PATH, os.R_OK), (
        f"File is not readable: {REPORT_CSV_PATH}"
    )


def test_report_csv_header():
    with open(REPORT_CSV_PATH, "r", newline="") as f:
        first_line = f.readline().rstrip("\n").rstrip("\r")
    assert first_line == EXPECTED_HEADER, (
        f"Header row mismatch in {REPORT_CSV_PATH}.\n"
        f"Expected: '{EXPECTED_HEADER}'\n"
        f"Got:      '{first_line}'"
    )


def test_report_csv_line_count():
    with open(REPORT_CSV_PATH, "r", newline="") as f:
        content = f.read()
    # Count non-empty lines
    lines = [line for line in content.splitlines() if line.strip()]
    assert len(lines) == 6, (
        f"Expected exactly 6 lines (1 header + 5 data rows) in {REPORT_CSV_PATH}, "
        f"but found {len(lines)} non-empty lines."
    )


def test_report_csv_has_trailing_newline():
    with open(REPORT_CSV_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"File {REPORT_CSV_PATH} must end with a trailing newline character."
    )


def test_report_csv_no_extra_blank_lines():
    with open(REPORT_CSV_PATH, "r", newline="") as f:
        content = f.read()
    lines = content.splitlines()
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert len(blank_lines) == 0, (
        f"File {REPORT_CSV_PATH} contains blank lines at line numbers: {blank_lines}. "
        "No extra blank lines are allowed."
    )


def test_report_csv_columns_in_header():
    with open(REPORT_CSV_PATH, "r", newline="") as f:
        first_line = f.readline().rstrip("\n").rstrip("\r")
    columns = first_line.split(",")
    assert len(columns) == 3, (
        f"Header row should have exactly 3 columns, got {len(columns)}: {columns}"
    )
    assert columns[0] == "date", (
        f"First column should be 'date', got '{columns[0]}'"
    )
    assert columns[1] == "salesperson", (
        f"Second column should be 'salesperson', got '{columns[1]}'"
    )
    assert columns[2] == "total", (
        f"Third column should be 'total', got '{columns[2]}'"
    )


def test_report_csv_data_rows():
    with open(REPORT_CSV_PATH, "r", newline="") as f:
        lines = [line.rstrip("\n").rstrip("\r") for line in f]
    # Remove trailing empty line if present
    if lines and lines[-1] == "":
        lines = lines[:-1]

    data_lines = lines[1:]  # skip header

    assert len(data_lines) == 5, (
        f"Expected 5 data rows in {REPORT_CSV_PATH}, got {len(data_lines)}."
    )

    for i, (actual_line, expected_line) in enumerate(zip(data_lines, EXPECTED_ROWS), start=1):
        assert actual_line == expected_line, (
            f"Data row {i} mismatch in {REPORT_CSV_PATH}.\n"
            f"Expected: '{expected_line}'\n"
            f"Got:      '{actual_line}'"
        )


def test_report_csv_exact_content():
    with open(REPORT_CSV_PATH, "r", newline="") as f:
        actual_content = f.read()
    assert actual_content == EXPECTED_CONTENT, (
        f"Exact content mismatch in {REPORT_CSV_PATH}.\n"
        f"Expected (repr): {repr(EXPECTED_CONTENT)}\n"
        f"Got (repr):      {repr(actual_content)}"
    )


def test_report_csv_only_three_columns_per_row():
    with open(REPORT_CSV_PATH, "r", newline="") as f:
        lines = [line.rstrip("\n").rstrip("\r") for line in f if line.strip()]

    for i, line in enumerate(lines):
        columns = line.split(",")
        assert len(columns) == 3, (
            f"Line {i + 1} in {REPORT_CSV_PATH} should have exactly 3 comma-separated values, "
            f"but got {len(columns)}: '{line}'"
        )


def test_report_csv_no_extra_spaces():
    with open(REPORT_CSV_PATH, "r", newline="") as f:
        lines = [line.rstrip("\n").rstrip("\r") for line in f if line.strip()]

    for i, line in enumerate(lines):
        columns = line.split(",")
        for j, col in enumerate(columns):
            assert col == col.strip(), (
                f"Line {i + 1}, column {j + 1} in {REPORT_CSV_PATH} has extra whitespace: '{col}'"
            )


def test_report_csv_date_column_values():
    expected_dates = ["2024-01-15", "2024-01-16", "2024-01-17", "2024-01-18", "2024-01-19"]
    with open(REPORT_CSV_PATH, "r", newline="") as f:
        lines = [line.rstrip("\n").rstrip("\r") for line in f if line.strip()]

    data_lines = lines[1:]
    for i, (line, expected_date) in enumerate(zip(data_lines, expected_dates), start=1):
        actual_date = line.split(",")[0]
        assert actual_date == expected_date, (
            f"Row {i}: expected date '{expected_date}', got '{actual_date}' in {REPORT_CSV_PATH}"
        )


def test_report_csv_salesperson_column_values():
    expected_salespersons = ["Alice", "Bob", "Alice", "Carol", "Bob"]
    with open(REPORT_CSV_PATH, "r", newline="") as f:
        lines = [line.rstrip("\n").rstrip("\r") for line in f if line.strip()]

    data_lines = lines[1:]
    for i, (line, expected_sp) in enumerate(zip(data_lines, expected_salespersons), start=1):
        actual_sp = line.split(",")[1]
        assert actual_sp == expected_sp, (
            f"Row {i}: expected salesperson '{expected_sp}', got '{actual_sp}' in {REPORT_CSV_PATH}"
        )


def test_report_csv_total_column_values():
    expected_totals = ["59.90", "74.97", "41.93", "99.98", "89.85"]
    with open(REPORT_CSV_PATH, "r", newline="") as f:
        lines = [line.rstrip("\n").rstrip("\r") for line in f if line.strip()]

    data_lines = lines[1:]
    for i, (line, expected_total) in enumerate(zip(data_lines, expected_totals), start=1):
        actual_total = line.split(",")[2]
        assert actual_total == expected_total, (
            f"Row {i}: expected total '{expected_total}', got '{actual_total}' in {REPORT_CSV_PATH}"
        )


def test_original_sales_csv_unchanged():
    """Verify the original sales.csv was not modified."""
    expected_original = (
        "transaction_id,date,salesperson,region,product,quantity,unit_price,total\n"
        "1001,2024-01-15,Alice,North,Widget,10,5.99,59.90\n"
        "1002,2024-01-16,Bob,South,Gadget,3,24.99,74.97\n"
        "1003,2024-01-17,Alice,North,Widget,7,5.99,41.93\n"
        "1004,2024-01-18,Carol,East,Doohickey,2,49.99,99.98\n"
        "1005,2024-01-19,Bob,South,Widget,15,5.99,89.85\n"
    )
    assert os.path.exists(SALES_CSV_PATH), (
        f"Original file {SALES_CSV_PATH} should still exist but was not found."
    )
    with open(SALES_CSV_PATH, "r", newline="") as f:
        actual = f.read()
    # Normalize line endings for comparison
    actual_normalized = actual.replace("\r\n", "\n").replace("\r", "\n")
    expected_normalized = expected_original.replace("\r\n", "\n")
    # Allow for missing trailing newline in original
    assert actual_normalized.rstrip("\n") == expected_normalized.rstrip("\n"), (
        f"Original file {SALES_CSV_PATH} appears to have been modified.\n"
        f"Expected content matches original sales data."
    )