# test_final_state.py

import os
import sqlite3
import pytest

SOURCE_DB = "/home/user/source.db"
DEST_DB = "/home/user/destination.db"
LOG_FILE = "/home/user/migration_validation.log"

EXPECTED_ROWS = [
    (1, "Alice Smith", "alice@example.com"),
    (2, "Bob Jones", "bob@example.com"),
    (3, "Carol White", "carol@example.com"),
]

EXPECTED_LOG_LINES = [
    "Total rows in source: 3",
    "Total rows in destination: 3",
    "Row count matches",
    "Row contents match",
]

@pytest.mark.describe("Final OS/filesystem state after migration and validation")
class TestFinalState:

    def test_destination_db_exists(self):
        assert os.path.isfile(DEST_DB), (
            f"Destination database file {DEST_DB} does not exist. "
            f"Migration did not create the database."
        )

    def test_destination_db_schema_and_rows(self):
        # Check destination DB schema
        try:
            conn = sqlite3.connect(DEST_DB)
            cur = conn.cursor()
            cur.execute("PRAGMA table_info(customers)")
            columns = cur.fetchall()
            assert len(columns) == 3, (
                f"'customers' table in destination database should have 3 columns, found {len(columns)}."
            )
            # Check column names, types, and constraints
            col_checks = [
                (columns[0][1] == 'id' and columns[0][2] == 'INTEGER' and columns[0][5] == 1),
                (columns[1][1] == 'name' and columns[1][2] == 'TEXT' and columns[1][3] == 1),
                (columns[2][1] == 'email' and columns[2][2] == 'TEXT' and columns[2][3] == 1),
            ]
            assert all(col_checks), (
                f"'customers' table schema in {DEST_DB} is incorrect: {columns}."
            )
            # Check table rows
            cur.execute("SELECT id, name, email FROM customers ORDER BY id")
            rows = cur.fetchall()
            assert rows == EXPECTED_ROWS, (
                f"'customers' table in {DEST_DB} does not have the expected rows after migration.\n"
                f"Expected: {EXPECTED_ROWS}\nFound: {rows}"
            )
        except sqlite3.DatabaseError as e:
            pytest.fail(f"Cannot open/query {DEST_DB} as a valid SQLite3 database: {e}")
        finally:
            if 'conn' in locals():
                conn.close()

    def test_source_db_unchanged(self):
        # Ensure the source DB still exists and is unchanged
        assert os.path.isfile(SOURCE_DB), (
            f"Source database file {SOURCE_DB} is missing after migration."
        )
        try:
            conn = sqlite3.connect(SOURCE_DB)
            cur = conn.cursor()
            cur.execute("PRAGMA table_info(customers)")
            columns = cur.fetchall()
            assert len(columns) == 3, (
                f"'customers' table in source database should have 3 columns, found {len(columns)}."
            )
            cur.execute("SELECT id, name, email FROM customers ORDER BY id")
            rows = cur.fetchall()
            assert rows == EXPECTED_ROWS, (
                f"'customers' table in {SOURCE_DB} does not have the expected rows after migration.\n"
                f"Expected: {EXPECTED_ROWS}\nFound: {rows}"
            )
        except sqlite3.DatabaseError as e:
            pytest.fail(f"Cannot open/query {SOURCE_DB} as a valid SQLite3 database: {e}")
        finally:
            if 'conn' in locals():
                conn.close()

    def test_log_file_exists_and_contents(self):
        assert os.path.isfile(LOG_FILE), (
            f"Log file {LOG_FILE} does not exist after migration and validation."
        )
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            log_lines = [line.rstrip('\n') for line in f]

        # Check the number of lines is exactly 4
        assert len(log_lines) == 4, (
            f"Log file {LOG_FILE} should contain exactly 4 lines, found {len(log_lines)}.\n"
            f"Log contents:\n{chr(10).join(log_lines)}"
        )

        # Check each line matches the expected line, in order
        for i, (expected, actual) in enumerate(zip(EXPECTED_LOG_LINES, log_lines), 1):
            assert expected == actual, (
                f"Log file {LOG_FILE}, line {i} incorrect.\n"
                f"Expected: '{expected}'\nFound:    '{actual}'"
            )

    def test_log_file_has_no_discrepancies(self):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = [line.rstrip('\n') for line in f]
        # There should be no line starting with "Discrepancy:"
        discrepancies = [line for line in lines if line.startswith("Discrepancy:")]
        assert not discrepancies, (
            f"Log file {LOG_FILE} should not contain any 'Discrepancy:' lines, "
            f"but found: {discrepancies}"
        )