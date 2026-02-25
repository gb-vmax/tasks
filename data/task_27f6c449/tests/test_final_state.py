# test_final_state.py

import os
import stat
import pwd
import pytest
import sqlite3
import filecmp

HOME = '/home/user'
DB_PATH = os.path.join(HOME, 'data', 'customer_data.db')
BACKUP_PATH = os.path.join(HOME, 'backups', 'customer_data_backup.db')
BACKUPS_DIR = os.path.join(HOME, 'backups')
BACKUP_LOGS_DIR = os.path.join(HOME, 'backup_logs')
VERIFICATION_LOG = os.path.join(BACKUP_LOGS_DIR, 'backup_verification.log')

EXPECTED_TABLES = ['customers', 'orders']
EXPECTED_TABLES_ORDER = ['customers', 'orders']
EXPECTED_TABLES_DOTTABLES_OUTPUT = 'customers  orders'
EXPECTED_LOG_CONTENT = "Table: customers\nTable: orders\n"


def test_backup_file_exists():
    assert os.path.isfile(BACKUP_PATH), (
        f"Backup file does not exist at expected path: {BACKUP_PATH}"
    )


def test_backup_is_byte_for_byte_copy():
    # Compare the original and backup files byte-for-byte
    assert os.path.isfile(DB_PATH), (
        f"Reference database file is missing: {DB_PATH}"
    )
    # filecmp.cmp returns True if the files are identical
    identical = filecmp.cmp(DB_PATH, BACKUP_PATH, shallow=False)
    assert identical, (
        f"The backup file {BACKUP_PATH} is not a byte-for-byte copy of {DB_PATH}."
    )


def test_backup_db_contains_expected_tables():
    # Open the backup db and check tables
    try:
        conn = sqlite3.connect(BACKUP_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        )
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
    except Exception as e:
        pytest.fail(f"Could not open or query the backup database {BACKUP_PATH}: {e}")

    missing = [t for t in EXPECTED_TABLES_ORDER if t not in tables]
    assert not missing, (
        f"The backup database is missing tables: {', '.join(missing)}"
    )
    assert tables == EXPECTED_TABLES_ORDER, (
        f"The backup database tables are: {tables}, expected: {EXPECTED_TABLES_ORDER}"
    )


def test_backup_db_dot_tables_output():
    """
    Simulate the output of the `.tables` command.
    The .tables command lists table names in sorted order, space-separated, on one line.
    """
    try:
        conn = sqlite3.connect(BACKUP_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        )
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
    except Exception as e:
        pytest.fail(f"Could not open or query the backup database {BACKUP_PATH}: {e}")

    dot_tables_output = '  '.join(tables)
    assert dot_tables_output == EXPECTED_TABLES_DOTTABLES_OUTPUT, (
        f"'.tables' output for backup database is '{dot_tables_output}', "
        f"expected '{EXPECTED_TABLES_DOTTABLES_OUTPUT}'."
    )


def test_verification_log_exists():
    assert os.path.isfile(VERIFICATION_LOG), (
        f"Backup verification log file does not exist: {VERIFICATION_LOG}"
    )


def test_verification_log_content_exact():
    with open(VERIFICATION_LOG, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == EXPECTED_LOG_CONTENT, (
        f"Backup verification log file content is incorrect.\n"
        f"Expected:\n{EXPECTED_LOG_CONTENT!r}\n"
        f"Found:\n{content!r}\n"
        "The output must exactly match the specified format, including order and newlines."
    )


@pytest.mark.parametrize("dir_path", [BACKUPS_DIR, BACKUP_LOGS_DIR])
def test_required_directories_still_exist_and_writable(dir_path):
    assert os.path.isdir(dir_path), (
        f"Required directory does not exist: {dir_path}"
    )
    # Check ownership and writability
    stat_info = os.stat(dir_path)
    dir_uid = stat_info.st_uid
    user_uid = pwd.getpwnam('user').pw_uid
    assert dir_uid == user_uid, (
        f"Directory {dir_path} is not owned by 'user'."
    )
    assert os.access(dir_path, os.W_OK), (
        f"Directory {dir_path} is not writable by 'user'."
    )