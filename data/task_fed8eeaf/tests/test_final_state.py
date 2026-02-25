# test_final_state.py

import os
import stat
import pytest

DB_DIR = '/home/user/db'
QUERY_LOG = '/home/user/db/query.log'
SLOW_QUERIES_LOG = '/home/user/db/slow_queries.log'

EXPECTED_QUERY_LOG_LINES = [
    "[2024-06-20 13:27:14] user:alice db:invoices duration:205ms query:SELECT * FROM payments WHERE amount > 1000;",
    "[2024-06-20 13:28:10] user:bob db:customers duration:98ms query:SELECT * FROM customers WHERE country='US';",
    "[2024-06-20 13:29:45] user:carol db:invoices duration:201ms query:UPDATE invoices SET status='paid' WHERE id=42;",
    "[2024-06-20 13:30:55] user:dave db:payments duration:199ms query:DELETE FROM payments WHERE amount < 10;",
    "[2024-06-20 13:31:16] user:alice db:accounts duration:305ms query:INSERT INTO accounts (user, balance) VALUES ('alice', 500);",
]

# Only lines with duration > 200ms (strictly greater than 200)
EXPECTED_SLOW_QUERIES_LOG_LINES = [
    "[2024-06-20 13:27:14] user:alice db:invoices duration:205ms query:SELECT * FROM payments WHERE amount > 1000;",
    "[2024-06-20 13:29:45] user:carol db:invoices duration:201ms query:UPDATE invoices SET status='paid' WHERE id=42;",
    "[2024-06-20 13:31:16] user:alice db:accounts duration:305ms query:INSERT INTO accounts (user, balance) VALUES ('alice', 500);",
]


@pytest.mark.describe("Final state: /home/user/db/ directory still exists and is writable")
def test_db_directory_exists_and_writable():
    assert os.path.isdir(DB_DIR), (
        f"Required directory '{DB_DIR}' does not exist after task completion."
    )
    mode = os.stat(DB_DIR).st_mode
    is_writable = bool(mode & stat.S_IWUSR)
    assert is_writable, (
        f"Directory '{DB_DIR}' exists but is not writable by the user after task completion."
    )


@pytest.mark.describe("Final state: /home/user/db/query.log exists and is unchanged")
def test_query_log_exists_and_unchanged():
    assert os.path.isfile(QUERY_LOG), (
        f"File '{QUERY_LOG}' is missing after the task. It must not be deleted or renamed."
    )
    with open(QUERY_LOG, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]
    assert lines == EXPECTED_QUERY_LOG_LINES, (
        f"File '{QUERY_LOG}' was modified. It must remain unchanged after the task.\n"
        "Expected lines:\n" +
        "\n".join(EXPECTED_QUERY_LOG_LINES) +
        "\nActual lines:\n" +
        "\n".join(lines)
    )


@pytest.mark.describe("Final state: /home/user/db/slow_queries.log exists with correct filtered lines")
def test_slow_queries_log_exists_and_contents():
    assert os.path.isfile(SLOW_QUERIES_LOG), (
        f"File '{SLOW_QUERIES_LOG}' does not exist. "
        "You must create this file with the correct filtered log lines."
    )
    with open(SLOW_QUERIES_LOG, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]
    assert lines == EXPECTED_SLOW_QUERIES_LOG_LINES, (
        f"File '{SLOW_QUERIES_LOG}' does not contain the correct slow query entries.\n"
        "Expected lines:\n" +
        "\n".join(EXPECTED_SLOW_QUERIES_LOG_LINES) +
        "\nActual lines:\n" +
        "\n".join(lines) +
        (
            "\n\nCheck for extra blank lines, missing lines, or incorrect order."
            if lines != EXPECTED_SLOW_QUERIES_LOG_LINES else ""
        )
    )

    # Check for blank lines before, between, or after entries
    for i, line in enumerate(lines):
        assert line.strip() != "", (
            f"File '{SLOW_QUERIES_LOG}' contains a blank line at position {i+1}. "
            "There should be no blank lines before, between, or after the log entries."
        )


@pytest.mark.describe("Final state: No extra files created in /home/user/db/")
def test_no_extra_files_in_db_dir():
    expected_files = {'query.log', 'slow_queries.log'}
    actual_files = set(
        f for f in os.listdir(DB_DIR)
        if os.path.isfile(os.path.join(DB_DIR, f))
    )
    extra_files = actual_files - expected_files
    assert not extra_files, (
        f"Extra files present in '{DB_DIR}': {sorted(list(extra_files))}. "
        f"Only 'query.log' and 'slow_queries.log' should exist after the task."
    )


@pytest.mark.describe("Final state: /home/user/db/slow_queries.log is owned and writable by the user")
def test_slow_queries_log_writable():
    st = os.stat(SLOW_QUERIES_LOG)
    # Check if user has write permission
    is_writable = bool(st.st_mode & stat.S_IWUSR)
    assert is_writable, (
        f"File '{SLOW_QUERIES_LOG}' is not writable by the user. "
        "Ensure the file permissions allow writing by the user."
    )
    # Optionally check ownership (if running as root or non-root, skip if not applicable)
    # Skipping UID check for portability