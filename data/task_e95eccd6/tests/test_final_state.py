# test_final_state.py

import os
import sqlite3
import pytest

DB_DIR = "/home/user/db-migration"
SOURCE_DB = os.path.join(DB_DIR, "source.db")
TARGET_DB = os.path.join(DB_DIR, "target.db")
EXPORT_CSV = os.path.join(DB_DIR, "customers_export.csv")
VALIDATION_LOG = os.path.join(DB_DIR, "validation.log")

EXPECTED_ROWS = [
    (1, "Alice Smith", "alice.smith@example.com"),
    (2, "Bob Johnson", "bob.johnson@example.com"),
    (3, "Carol Williams", "carol.williams@example.com"),
]
EXPECTED_CSV = (
    "id,name,email\n"
    "1,Alice Smith,alice.smith@example.com\n"
    "2,Bob Johnson,bob.johnson@example.com\n"
    "3,Carol Williams,carol.williams@example.com\n"
)
EXPECTED_LOG = (
    "Migrated 3 records to target.db\n"
    "First customer: id=1, name=Alice Smith, email=alice.smith@example.com\n"
)

def test_db_migration_directory_unchanged():
    """Ensure /home/user/db-migration exists, is writable, and only contains the 4 expected files."""
    assert os.path.isdir(DB_DIR), f"Directory {DB_DIR} does not exist."
    assert os.access(DB_DIR, os.W_OK), f"Directory {DB_DIR} is not writable by user."
    expected_files = {"source.db", "target.db", "customers_export.csv", "validation.log"}
    actual_files = set(f for f in os.listdir(DB_DIR) if not f.startswith('.'))
    missing = expected_files - actual_files
    extra = actual_files - expected_files
    assert not missing, (
        f"Missing expected files in {DB_DIR}: {', '.join(sorted(missing))}. "
        "After the migration, only source.db, target.db, customers_export.csv, and validation.log should be present."
    )
    assert not extra, (
        f"Unexpected extra files in {DB_DIR}: {', '.join(sorted(extra))}. "
        "No files other than source.db, target.db, customers_export.csv, and validation.log should exist."
    )

def test_customers_export_csv_exists_and_correct():
    """Validate that the export CSV exists and its contents match the expected export."""
    assert os.path.isfile(EXPORT_CSV), (
        f"File {EXPORT_CSV} does not exist. "
        "The export CSV must be present after migration."
    )
    with open(EXPORT_CSV, "r", encoding="utf-8") as f:
        content = f.read()
    # Must match exactly, including newlines, no extra whitespace or quotes
    assert content == EXPECTED_CSV, (
        f"customers_export.csv does not match expected contents.\n"
        "Expected:\n"
        f"{EXPECTED_CSV!r}\n"
        "Found:\n"
        f"{content!r}\n"
        "Ensure the CSV has exactly the correct header and rows, with no extra whitespace, quotes, or lines."
    )

def test_target_db_customers_table_migrated():
    """Check that the target.db customers table contains the correct migrated data."""
    assert os.path.isfile(TARGET_DB), f"Target database {TARGET_DB} does not exist."
    try:
        conn = sqlite3.connect(TARGET_DB)
        cursor = conn.cursor()
        # Table exists
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='customers'"
        )
        assert cursor.fetchone(), (
            "Table 'customers' does not exist in target.db after migration."
        )
        # Schema is correct
        cursor.execute("PRAGMA table_info(customers)")
        columns = cursor.fetchall()
        expected_columns = [("id", "INTEGER"), ("name", "TEXT"), ("email", "TEXT")]
        actual_columns = [(col[1], col[2]) for col in columns]
        for (exp_name, exp_type), (act_name, act_type) in zip(expected_columns, actual_columns):
            assert exp_name == act_name, (
                f"Expected column '{exp_name}' in 'customers' table of target.db, found '{act_name}'."
            )
            assert exp_type.upper() in act_type.upper(), (
                f"Expected column '{exp_name}' to have type '{exp_type}' in target.db, found '{act_type}'."
            )
        # Data is correct
        cursor.execute("SELECT id, name, email FROM customers ORDER BY id ASC")
        rows = cursor.fetchall()
        assert rows == EXPECTED_ROWS, (
            "target.db 'customers' table does not contain the expected 3 migrated records.\n"
            "Expected:\n" +
            "\n".join(str(r) for r in EXPECTED_ROWS) +
            "\nFound:\n" +
            "\n".join(str(r) for r in rows) +
            "\nEnsure all 3 records are inserted, in order, and no extra or missing rows."
        )
    finally:
        conn.close()

def test_validation_log_correct():
    """Check that the validation.log exists and its contents are exactly as specified."""
    assert os.path.isfile(VALIDATION_LOG), (
        f"Validation log {VALIDATION_LOG} does not exist. "
        "It must be created after migration."
    )
    with open(VALIDATION_LOG, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_LOG, (
        f"validation.log contents are incorrect.\n"
        "Expected:\n"
        f"{EXPECTED_LOG!r}\n"
        "Found:\n"
        f"{content!r}\n"
        "The log file must have exactly two lines, no extra whitespace or lines, "
        "and the values must be correct and in the specified format."
    )

def test_source_db_unchanged():
    """Ensure that source.db is unmodified (still contains the initial 3 records, unchanged)."""
    assert os.path.isfile(SOURCE_DB), f"Source database {SOURCE_DB} does not exist."
    try:
        conn = sqlite3.connect(SOURCE_DB)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='customers'"
        )
        assert cursor.fetchone(), (
            "Table 'customers' does not exist in source.db after migration."
        )
        cursor.execute("SELECT id, name, email FROM customers ORDER BY id ASC")
        rows = cursor.fetchall()
        assert rows == EXPECTED_ROWS, (
            "source.db 'customers' table contents were modified during migration.\n"
            "Expected:\n" +
            "\n".join(str(r) for r in EXPECTED_ROWS) +
            "\nFound:\n" +
            "\n".join(str(r) for r in rows) +
            "\nThe source database must remain unchanged."
        )
    finally:
        conn.close()