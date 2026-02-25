# test_final_state.py

import os
import sqlite3
import pytest

ML_DATA_DIR = "/home/user/ml_data"
OLD_DB_PATH = os.path.join(ML_DATA_DIR, "old_training_data.db")
NEW_DB_PATH = os.path.join(ML_DATA_DIR, "new_training_data.db")
LOG_PATH = os.path.join(ML_DATA_DIR, "migration_validation.log")

EXPECTED_ROWS = [
    (1, "I love bananas.", 0),
    (2, "Hello, world!", 1),
    (3, "The sky is blue.", 0),
]
EXPECTED_ROW_COUNT = 3
EXPECTED_LOG_CONTENT = (
    "Record count in old_training_data.db: 3\n"
    "Record count in new_training_data.db: 3\n"
    "Migration successful: yes\n"
)

def get_train_samples_rows(db_path):
    """Return all rows from train_samples table, ordered by id."""
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT id, sentence, label FROM train_samples ORDER BY id;")
        rows = cur.fetchall()
        return rows
    finally:
        conn.close()

def get_train_samples_count(db_path):
    """Return the row count from train_samples table."""
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM train_samples;")
        count = cur.fetchone()[0]
        return count
    finally:
        conn.close()

def get_train_samples_schema(db_path):
    """Return list of (name, type) for columns in train_samples."""
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("PRAGMA table_info(train_samples);")
        columns = cur.fetchall()
        # columns: (cid, name, type, notnull, dflt_value, pk)
        return [(col[1], col[2]) for col in columns]
    finally:
        conn.close()

def has_table(db_path, table_name):
    """Check if a table exists in the database."""
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
            (table_name,),
        )
        return cur.fetchone() is not None
    finally:
        conn.close()

def read_file_exact(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def test_new_training_data_db_exists():
    assert os.path.isfile(NEW_DB_PATH), (
        f"Expected new database file {NEW_DB_PATH} does not exist after migration."
    )

def test_new_training_data_db_has_train_samples_table():
    assert has_table(NEW_DB_PATH, "train_samples"), (
        f"Table 'train_samples' does not exist in {NEW_DB_PATH} after migration."
    )

def test_new_training_data_db_schema_matches():
    schema = get_train_samples_schema(NEW_DB_PATH)
    expected_schema = [("id", "INTEGER"), ("sentence", "TEXT"), ("label", "INTEGER")]
    assert schema == expected_schema, (
        f"Schema of 'train_samples' in {NEW_DB_PATH} is {schema}, expected {expected_schema}."
    )

def test_new_training_data_db_content_matches():
    rows = get_train_samples_rows(NEW_DB_PATH)
    assert rows == EXPECTED_ROWS, (
        f"Rows in 'train_samples' in {NEW_DB_PATH} are {rows}, expected {EXPECTED_ROWS}."
    )

def test_new_training_data_db_row_count():
    count = get_train_samples_count(NEW_DB_PATH)
    assert count == EXPECTED_ROW_COUNT, (
        f"'train_samples' in {NEW_DB_PATH} has {count} rows, expected {EXPECTED_ROW_COUNT}."
    )

def test_log_file_exists():
    assert os.path.isfile(LOG_PATH), (
        f"Expected log file {LOG_PATH} does not exist after migration."
    )

def test_log_file_content_exact():
    actual = read_file_exact(LOG_PATH)
    assert actual == EXPECTED_LOG_CONTENT, (
        f"Log file {LOG_PATH} content is incorrect.\n"
        f"Expected:\n{EXPECTED_LOG_CONTENT!r}\n"
        f"Actual:\n{actual!r}\n"
        "The log file must match the required format exactly."
    )

def test_log_file_no_extra_content():
    """Ensure there is no extra content after the required lines."""
    lines = read_file_exact(LOG_PATH).splitlines()
    assert len(lines) == 3, (
        f"Log file {LOG_PATH} should have exactly 3 lines, but it has {len(lines)} lines: {lines!r}"
    )

def test_log_file_counts_and_success_line():
    """Parse the log and check the counts and migration status line."""
    lines = read_file_exact(LOG_PATH).splitlines()
    assert lines[0].startswith("Record count in old_training_data.db: "), (
        f"First line of log is incorrect: {lines[0]!r}"
    )
    assert lines[1].startswith("Record count in new_training_data.db: "), (
        f"Second line of log is incorrect: {lines[1]!r}"
    )
    assert lines[2].startswith("Migration successful: "), (
        f"Third line of log is incorrect: {lines[2]!r}"
    )
    old_count = int(lines[0].split(": ")[1])
    new_count = int(lines[1].split(": ")[1])
    success = lines[2].split(": ")[1]
    assert old_count == EXPECTED_ROW_COUNT, (
        f"Log file reports {old_count} rows in old_training_data.db, expected {EXPECTED_ROW_COUNT}."
    )
    assert new_count == EXPECTED_ROW_COUNT, (
        f"Log file reports {new_count} rows in new_training_data.db, expected {EXPECTED_ROW_COUNT}."
    )
    assert success == "yes", (
        f"Log file migration status is '{success}', expected 'yes' since counts match."
    )

def test_log_file_is_plain_text():
    content = read_file_exact(LOG_PATH)
    try:
        content.encode("ascii")
    except UnicodeEncodeError:
        pytest.fail(
            f"Log file {LOG_PATH} contains non-ASCII characters. It must be plain text."
        )