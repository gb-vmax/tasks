# test_final_state.py

import os
import sqlite3
import pytest

DB_PATH = "/home/user/capacity_resources.db"
LOG_PATH = "/home/user/resource_stats.log"

EXPECTED_ROWS = [
    (1, "CPU", "Server01", 63.5, "2024-06-01"),
    (2, "Memory", "Server01", 74.2, "2024-06-01"),
    (3, "Disk", "DBStorage", 87.9, "2024-06-01"),
    (4, "CPU", "Server02", 41.0, "2024-06-01"),
]

EXPECTED_LOG_LINES = {
    "CPU 52.25 63.5",
    "Memory 74.2 74.2",
    "Disk 87.9 87.9",
}


def test_db_file_exists():
    """
    The SQLite database file must exist at the expected absolute path.
    """
    assert os.path.isfile(DB_PATH), f"Database file {DB_PATH} does not exist."


def test_resources_table_schema_and_rows():
    """
    The 'resources' table must exist with the correct schema and rows.
    """
    assert os.path.isfile(DB_PATH), f"Database file {DB_PATH} does not exist."

    conn = sqlite3.connect(DB_PATH)
    try:
        # Check that the 'resources' table exists
        cursor = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='resources';"
        )
        table = cursor.fetchone()
        assert table is not None, (
            "Table 'resources' does not exist in the database."
        )

        # Check schema (column names and types)
        cursor = conn.execute("PRAGMA table_info(resources);")
        schema = cursor.fetchall()
        expected_schema = [
            # cid, name, type, notnull, dflt_value, pk
            (0, "id", "INTEGER", 0, None, 1),
            (1, "resource_type", "TEXT", 0, None, 0),
            (2, "resource_name", "TEXT", 0, None, 0),
            (3, "usage_percent", "REAL", 0, None, 0),
            (4, "analysis_date", "TEXT", 0, None, 0),
        ]
        actual_schema = [(cid, name, coltype, notnull, dflt_value, pk) for cid, name, coltype, notnull, dflt_value, pk in schema]
        for expected, actual in zip(expected_schema, actual_schema):
            assert expected == actual, (
                f"Schema mismatch for column {expected[1]}: expected {expected}, got {actual}"
            )

        # Check AUTOINCREMENT is present in the table definition
        cursor = conn.execute(
            "SELECT sql FROM sqlite_master WHERE type='table' AND name='resources';"
        )
        create_sql = cursor.fetchone()
        assert create_sql is not None and "AUTOINCREMENT" in create_sql[0].upper(), (
            "Column 'id' is not defined as AUTOINCREMENT."
        )

        # Check the rows
        cursor = conn.execute(
            "SELECT id, resource_type, resource_name, usage_percent, analysis_date FROM resources ORDER BY id ASC;"
        )
        rows = cursor.fetchall()
        assert rows == EXPECTED_ROWS, (
            f"Table 'resources' contents are incorrect.\n"
            f"Expected rows:\n{EXPECTED_ROWS}\n"
            f"Actual rows:\n{rows}"
        )

    finally:
        conn.close()


def test_resource_stats_log_exists():
    """
    The log file /home/user/resource_stats.log must exist.
    """
    assert os.path.isfile(LOG_PATH), f"Log file {LOG_PATH} does not exist."


def test_resource_stats_log_contents():
    """
    The log file must contain exactly one correctly-formatted line per resource_type,
    with the correct values, no extra output, and the correct number of lines.
    """
    assert os.path.isfile(LOG_PATH), f"Log file {LOG_PATH} does not exist."
    with open(LOG_PATH, "rt", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    # Remove empty lines and check line count
    lines = [line for line in lines if line.strip()]
    assert len(lines) == 3, (
        f"resource_stats.log must contain exactly 3 lines (one per resource_type), "
        f"but found {len(lines)} lines: {lines}"
    )

    # Check each line format and values
    actual_lines_set = set(lines)
    missing = EXPECTED_LOG_LINES - actual_lines_set
    unexpected = actual_lines_set - EXPECTED_LOG_LINES

    assert not missing, (
        f"resource_stats.log is missing the following expected lines: {missing}"
    )
    assert not unexpected, (
        f"resource_stats.log contains unexpected lines: {unexpected}"
    )

    # Check that each line has exactly three fields: type avg max, and that floats are rounded correctly
    for line in lines:
        parts = line.split(" ")
        assert len(parts) == 3, (
            f"Line '{line}' does not have exactly three fields separated by spaces."
        )
        rtype, avg, mx = parts
        # Check float formatting
        try:
            avg_val = float(avg)
            mx_val = float(mx)
        except Exception:
            pytest.fail(f"Line '{line}' does not have valid float values for average or maximum usage percent.")

        # Check rounding
        if rtype == "CPU":
            assert avg == "52.25", f"CPU average usage_percent should be 52.25, got {avg}"
            assert mx == "63.5", f"CPU max usage_percent should be 63.5, got {mx}"
        elif rtype == "Disk":
            assert avg == "87.9", f"Disk average usage_percent should be 87.9, got {avg}"
            assert mx == "87.9", f"Disk max usage_percent should be 87.9, got {mx}"
        elif rtype == "Memory":
            assert avg == "74.2", f"Memory average usage_percent should be 74.2, got {avg}"
            assert mx == "74.2", f"Memory max usage_percent should be 74.2, got {mx}"
        else:
            pytest.fail(f"Unexpected resource_type '{rtype}' in line: '{line}'")