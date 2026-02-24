# test_final_state.py

import os
import sqlite3
import pytest

DB_PATH = "/home/user/resource_usage.db"
SUMMARY_PATH = "/home/user/usage_summary.txt"

EXPECTED_COLUMNS = [
    ("server_name", "TEXT"),
    ("cpu_percent", "REAL"),
    ("memory_mb", "INTEGER"),
    ("timestamp", "TEXT"),
]

EXPECTED_ROWS = [
    ("Alpha01", 43.0, 6084, "2024-04-30T11:58:00Z"),
    ("Beta02", 85.2, 9560, "2024-04-30T11:58:00Z"),
    ("Gamma03", 22.7, 4032, "2024-04-30T11:58:00Z"),
]

EXPECTED_SUMMARY = "50.3|9560"

def test_resource_usage_db_exists():
    assert os.path.exists(DB_PATH), (
        f"Database file {DB_PATH} does not exist. "
        "You must create the database at the specified absolute path."
    )

def test_usage_stats_table_schema():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Check that the usage_stats table exists
        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='usage_stats';
        """)
        table = cursor.fetchone()
        assert table is not None, (
            "Table 'usage_stats' does not exist in the database. "
            "You must create the table with the exact name and structure."
        )
        # Check table columns and types
        cursor.execute("PRAGMA table_info(usage_stats);")
        columns = cursor.fetchall()
        found_columns = [(col[1], col[2].upper()) for col in columns]
        expected_columns = [(name, typ.upper()) for name, typ in EXPECTED_COLUMNS]
        assert found_columns == expected_columns, (
            f"Table 'usage_stats' does not have the correct columns or types.\n"
            f"Expected: {expected_columns}\n"
            f"Found:    {found_columns}\n"
            "Check column names, order, and data types."
        )

def test_usage_stats_table_rows():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT server_name, cpu_percent, memory_mb, timestamp FROM usage_stats;")
        rows = cursor.fetchall()
        # Convert to set of tuples for unordered comparison
        expected_set = set(EXPECTED_ROWS)
        rows_set = set(rows)
        assert rows_set == expected_set, (
            "Table 'usage_stats' does not contain the exact expected records.\n"
            f"Expected rows (order does not matter):\n{sorted(expected_set)}\n"
            f"Found rows:\n{sorted(rows_set)}\n"
            "Check for missing, extra, or incorrect records."
        )
        assert len(rows) == 3, (
            f"Table 'usage_stats' should contain exactly 3 rows, found {len(rows)}."
        )

def test_usage_summary_txt_exists():
    assert os.path.exists(SUMMARY_PATH), (
        f"Summary file {SUMMARY_PATH} does not exist. "
        "You must output the query result to the specified absolute path."
    )

def test_usage_summary_txt_content():
    with open(SUMMARY_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Remove any trailing newlines/whitespace from the lines
    lines = [line.rstrip('\r\n') for line in lines]

    assert len(lines) == 1, (
        f"{SUMMARY_PATH} should contain exactly one line (no headers, no extra blank lines), "
        f"but found {len(lines)} line(s).\n"
        f"Content:\n{lines}"
    )
    actual = lines[0]
    assert actual == EXPECTED_SUMMARY, (
        f"{SUMMARY_PATH} does not contain the correct summary line.\n"
        f"Expected: {EXPECTED_SUMMARY!r}\n"
        f"Found:    {actual!r}\n"
        "Ensure you used the correct SQL, formatting, and no trailing whitespace or headers."
    )

def test_summary_matches_query_result():
    """Double-check the summary file matches the actual database query."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ROUND(AVG(cpu_percent), 1) as avg_cpu_percent, MAX(memory_mb) as max_memory_mb
            FROM usage_stats;
        """)
        row = cursor.fetchone()
    summary_line = f"{row[0]}|{row[1]}"
    with open(SUMMARY_PATH, "r", encoding="utf-8") as f:
        file_line = f.read().strip()
    assert file_line == summary_line, (
        f"Summary in {SUMMARY_PATH!r} does not match the result of the required SQL query.\n"
        f"Expected: {summary_line!r}\n"
        f"Found:    {file_line!r}\n"
        "Ensure you saved the precise query result to the file."
    )