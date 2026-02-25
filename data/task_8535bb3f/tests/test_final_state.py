# test_final_state.py

import os
import sqlite3
import pytest

SOURCE_DB = '/home/user/source_data.db'
DEST_DB = '/home/user/destination_data.db'
REPORT_FILE = '/home/user/migration_report.txt'

EXPECTED_EMPLOYEE_SCHEMA = [
    {'cid': 0, 'name': 'id', 'type': 'INTEGER', 'notnull': 0, 'dflt_value': None, 'pk': 1},
    {'cid': 1, 'name': 'name', 'type': 'TEXT', 'notnull': 0, 'dflt_value': None, 'pk': 0},
    {'cid': 2, 'name': 'salary', 'type': 'INTEGER', 'notnull': 0, 'dflt_value': None, 'pk': 0},
]

EXPECTED_EMPLOYEE_ROWS = [
    (1, 'Alice', 60000),
    (2, 'Bob', 70000),
    (3, 'Carol', 65000),
]

EXPECTED_REPORT_LINES = [
    "TOTAL ROWS MATCH: YES",
    "DATA INTEGRITY: PASSED",
    "source_row={'id': 1, 'name': 'Alice', 'salary': 60000} destination_row={'id': 1, 'name': 'Alice', 'salary': 60000}",
    "source_row={'id': 2, 'name': 'Bob', 'salary': 70000} destination_row={'id': 2, 'name': 'Bob', 'salary': 70000}",
    "source_row={'id': 3, 'name': 'Carol', 'salary': 65000} destination_row={'id': 3, 'name': 'Carol', 'salary': 65000}",
]


def get_table_schema(conn, table_name):
    cur = conn.execute(f"PRAGMA table_info({table_name})")
    schema = []
    for row in cur.fetchall():
        schema.append({
            'cid': row[0],
            'name': row[1],
            'type': row[2],
            'notnull': row[3],
            'dflt_value': row[4],
            'pk': row[5],
        })
    return schema


def get_employee_rows(conn):
    cur = conn.execute("SELECT id, name, salary FROM employee ORDER BY id ASC")
    return cur.fetchall()


@pytest.mark.dependency()
def test_source_db_still_exists():
    assert os.path.isfile(SOURCE_DB), (
        f"Source database '{SOURCE_DB}' is missing after migration. "
        "The original data source should remain intact."
    )


@pytest.mark.dependency()
def test_destination_db_exists():
    assert os.path.isfile(DEST_DB), (
        f"Destination database '{DEST_DB}' does not exist. "
        "You must create this file as the target of the migration."
    )


@pytest.mark.dependency(depends=["test_destination_db_exists"])
def test_destination_db_employee_table_exists_and_schema():
    with sqlite3.connect(DEST_DB) as conn:
        # Check table existence
        cur = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='employee'"
        )
        table = cur.fetchone()
        assert table is not None, (
            f"Table 'employee' does not exist in '{DEST_DB}'. "
            "You must create the table in the destination database."
        )
        # Check schema
        schema = get_table_schema(conn, 'employee')
        assert len(schema) == len(EXPECTED_EMPLOYEE_SCHEMA), (
            f"Schema of 'employee' table in '{DEST_DB}' has {len(schema)} columns, "
            f"expected {len(EXPECTED_EMPLOYEE_SCHEMA)}."
        )
        for i, expected_col in enumerate(EXPECTED_EMPLOYEE_SCHEMA):
            for key in expected_col:
                assert schema[i][key] == expected_col[key], (
                    f"Schema mismatch in 'employee' table of '{DEST_DB}', "
                    f"column {i}.\n"
                    f"Expected: {expected_col}\n"
                    f"Found: {schema[i]}\n"
                    "The schema must match the source exactly."
                )


@pytest.mark.dependency(depends=["test_destination_db_exists"])
def test_destination_db_employee_table_data():
    with sqlite3.connect(DEST_DB) as conn:
        rows = get_employee_rows(conn)
    assert rows == EXPECTED_EMPLOYEE_ROWS, (
        f"Data mismatch in 'employee' table of '{DEST_DB}'.\n"
        f"Expected rows: {EXPECTED_EMPLOYEE_ROWS}\n"
        f"Found rows: {rows}\n"
        "The destination must contain exactly the same rows, in the same order, as the source."
    )


@pytest.mark.dependency()
def test_migration_report_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Migration report '{REPORT_FILE}' does not exist. "
        "You must create the report file after migration."
    )


@pytest.mark.dependency(depends=["test_migration_report_exists", "test_source_db_still_exists", "test_destination_db_exists"])
def test_migration_report_content_exact():
    with open(REPORT_FILE, "rt", encoding="utf-8") as f:
        lines = [line.rstrip('\r\n') for line in f]
    assert len(lines) == len(EXPECTED_REPORT_LINES), (
        f"Migration report '{REPORT_FILE}' has {len(lines)} lines, expected {len(EXPECTED_REPORT_LINES)}.\n"
        "Expected report format:\n" +
        "\n".join(EXPECTED_REPORT_LINES) +
        "\nActual report contents:\n" +
        "\n".join(lines)
    )
    for i, (expected, actual) in enumerate(zip(EXPECTED_REPORT_LINES, lines)):
        assert expected == actual, (
            f"Line {i+1} of migration report is incorrect.\n"
            f"Expected: {expected!r}\n"
            f"Found:    {actual!r}\n"
            "The report must match the required format exactly."
        )


@pytest.mark.dependency(depends=["test_migration_report_content_exact"])
def test_migration_report_matches_actual_db_state():
    """
    Cross-validate that the report matches the actual state of both databases.
    """
    # Load DBs
    with sqlite3.connect(SOURCE_DB) as src_conn, sqlite3.connect(DEST_DB) as dst_conn:
        src_rows = get_employee_rows(src_conn)
        dst_rows = get_employee_rows(dst_conn)
    # Load report
    with open(REPORT_FILE, "rt", encoding="utf-8") as f:
        lines = [line.rstrip('\r\n') for line in f]
    # Check first two lines
    row_count_match = "YES" if len(src_rows) == len(dst_rows) else "NO"
    assert lines[0] == f"TOTAL ROWS MATCH: {row_count_match}", (
        f"First line of report should indicate row count match as '{row_count_match}'.\n"
        f"Found: {lines[0]}"
    )
    data_integrity = "PASSED" if src_rows == dst_rows else "FAILED"
    assert lines[1] == f"DATA INTEGRITY: {data_integrity}", (
        f"Second line of report should indicate data integrity as '{data_integrity}'.\n"
        f"Found: {lines[1]}"
    )
    # Check row lines
    for idx, (src_row, dst_row) in enumerate(zip(src_rows, dst_rows)):
        src_dict = {'id': src_row[0], 'name': src_row[1], 'salary': src_row[2]}
        dst_dict = {'id': dst_row[0], 'name': dst_row[1], 'salary': dst_row[2]}
        expected_line = f"source_row={src_dict} destination_row={dst_dict}"
        actual_line = lines[2 + idx]
        assert actual_line == expected_line, (
            f"Report line {2+idx+1} does not match actual DB data.\n"
            f"Expected: {expected_line}\n"
            f"Found:    {actual_line}"
        )
    # If extra lines exist, fail
    assert len(lines) == 2 + len(src_rows), (
        f"Report has extra lines beyond expected {2 + len(src_rows)}."
    )