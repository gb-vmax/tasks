# test_final_state.py

import os
import stat
import sqlite3
import csv
import pytest

EMPLOYEES_CSV_PATH = "/home/user/data/employees.csv"
ETL_DIR = "/home/user/etl"
EMPLOYEE_DB_PATH = os.path.join(ETL_DIR, "employee_data.db")
ENGINEERING_CSV_PATH = os.path.join(ETL_DIR, "engineering_employees.csv")

# Truth data for validation
EMPLOYEES_CSV_CONTENT = [
    ["id", "name", "department", "salary"],
    ["1", "Alice", "Engineering", "95000"],
    ["2", "Bob", "Sales", "70000"],
    ["3", "Charlie", "Engineering", "99000"],
    ["4", "David", "HR", "60000"],
]

ENGINEERING_CSV_EXPECTED = [
    ["id", "name", "department", "salary"],
    ["1", "Alice", "Engineering", "95000"],
    ["3", "Charlie", "Engineering", "99000"],
]


def test_etl_directory_exists_and_writable():
    """Check that /home/user/etl directory exists and is writable."""
    assert os.path.isdir(ETL_DIR), (
        f"Directory {ETL_DIR} does not exist. "
        "It must be created as part of the ETL process."
    )
    assert os.access(ETL_DIR, os.W_OK), (
        f"Directory {ETL_DIR} is not writable by the current user."
    )


def test_employee_db_exists():
    """Check that /home/user/etl/employee_data.db exists and is a file."""
    assert os.path.isfile(EMPLOYEE_DB_PATH), (
        f"Database file {EMPLOYEE_DB_PATH} does not exist. "
        "It must be created as part of the ETL process."
    )
    assert os.access(EMPLOYEE_DB_PATH, os.W_OK), (
        f"Database file {EMPLOYEE_DB_PATH} is not writable by the current user."
    )


def test_employee_db_schema_and_data():
    """Check that the database has the correct schema and data in the employees table."""
    conn = sqlite3.connect(EMPLOYEE_DB_PATH)
    try:
        cursor = conn.cursor()
        # Check table existence
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='employees';"
        )
        table = cursor.fetchone()
        assert table is not None, (
            "Table 'employees' does not exist in the database. "
            "Please create it with the correct schema."
        )

        # Check columns and types
        cursor.execute("PRAGMA table_info(employees);")
        schema = cursor.fetchall()
        expected_schema = [
            (0, "id", "INTEGER", 0, None, 0),
            (1, "name", "TEXT", 0, None, 0),
            (2, "department", "TEXT", 0, None, 0),
            (3, "salary", "INTEGER", 0, None, 0),
        ]
        # Only check name and type in order
        actual_columns = [(col[1], col[2]) for col in schema]
        expected_columns = [(col[1], col[2]) for col in expected_schema]
        assert actual_columns == expected_columns, (
            f"Schema of 'employees' table is incorrect.\n"
            f"Expected columns: {expected_columns}\n"
            f"Found columns:    {actual_columns}\n"
            "Columns and types must match exactly."
        )

        # Check row count and content
        cursor.execute("SELECT id, name, department, salary FROM employees ORDER BY id ASC;")
        rows = cursor.fetchall()
        expected_rows = [
            (1, "Alice", "Engineering", 95000),
            (2, "Bob", "Sales", 70000),
            (3, "Charlie", "Engineering", 99000),
            (4, "David", "HR", 60000),
        ]
        assert rows == expected_rows, (
            "Data in 'employees' table does not match the CSV input.\n"
            f"Expected rows:\n{expected_rows}\n"
            f"Found rows:\n{rows}\n"
        )

    finally:
        conn.close()


def test_engineering_employees_csv_exists_and_content():
    """Check that /home/user/etl/engineering_employees.csv exists and has exact required content."""
    assert os.path.isfile(ENGINEERING_CSV_PATH), (
        f"Output CSV file {ENGINEERING_CSV_PATH} does not exist. "
        "It must be created as part of the ETL process."
    )

    with open(ENGINEERING_CSV_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        actual_rows = list(reader)

    # Remove trailing empty lines, if any
    while actual_rows and all(not cell.strip() for cell in actual_rows[-1]):
        actual_rows.pop()

    assert actual_rows == ENGINEERING_CSV_EXPECTED, (
        f"Content of {ENGINEERING_CSV_PATH} does not match the expected output.\n"
        "Expected:\n"
        + "\n".join([",".join(row) for row in ENGINEERING_CSV_EXPECTED])
        + "\nFound:\n"
        + "\n".join([",".join(row) for row in actual_rows])
        + "\nPlease ensure the file contains only the specified rows and columns, with no extra whitespace or lines."
    )


def test_engineering_employees_csv_no_extra_rows_or_columns():
    """Ensure there are no extra rows or columns in the output CSV."""
    with open(ENGINEERING_CSV_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Check number of rows
    expected_num_rows = len(ENGINEERING_CSV_EXPECTED)
    assert len(rows) == expected_num_rows, (
        f"The output CSV {ENGINEERING_CSV_PATH} contains {len(rows)} rows, "
        f"but exactly {expected_num_rows} rows (including header) are expected."
    )

    # Check number of columns in each row
    expected_num_columns = len(ENGINEERING_CSV_EXPECTED[0])
    for i, row in enumerate(rows):
        assert len(row) == expected_num_columns, (
            f"Row {i+1} of {ENGINEERING_CSV_PATH} has {len(row)} columns, "
            f"but {expected_num_columns} columns are expected.\n"
            f"Row content: {row}"
        )


def test_engineering_employees_csv_header_exact():
    """Ensure the header of the output CSV matches exactly."""
    with open(ENGINEERING_CSV_PATH, "r", encoding="utf-8", newline="") as f:
        header = f.readline().rstrip('\r\n')
    expected_header = ",".join(ENGINEERING_CSV_EXPECTED[0])
    assert header == expected_header, (
        f"Header of {ENGINEERING_CSV_PATH} does not match expected header.\n"
        f"Expected: {expected_header}\n"
        f"Found:    {header}\n"
        "Ensure there are no extra spaces, columns, or missing fields."
    )