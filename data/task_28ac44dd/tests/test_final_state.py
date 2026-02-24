# test_final_state.py

import os
import pytest

POSTGRESQL_LOG_PATH = "/home/user/db/postgresql.log"
SLOW_QUERIES_LOG_PATH = "/home/user/db/slow_queries.log"
FILTER_LOG_PATH = "/home/user/db/filter_log.txt"

EXPECTED_LOG_LINES = [
    "[2024-05-22 14:23:11] user=alice db=inventory duration=145ms statement: SELECT * FROM products;",
    "[2024-05-22 14:25:42] user=bob db=sales duration=384ms statement: UPDATE orders SET status='shipped' WHERE id=1492;",
    "[2024-05-22 14:26:00] user=carol db=inventory duration=92ms statement: DELETE FROM products WHERE id=3482;",
    "[2024-05-22 14:27:03] user=dan db=inventory duration=518ms statement: INSERT INTO products VALUES (1023, 'pen', 1.20);",
    "[2024-05-22 14:30:14] user=alice db=sales duration=215ms statement: SELECT * FROM orders WHERE status='shipped';",
    "[2024-05-22 14:31:22] user=dan db=inventory duration=301ms statement: SELECT COUNT(*) FROM products;",
    "[2024-05-22 14:32:45] user=bob db=sales duration=44ms statement: SELECT * FROM customers;",
]

SLOW_QUERIES_EXPECTED_LINES = [
    "[2024-05-22 14:25:42] user=bob db=sales duration=384ms statement: UPDATE orders SET status='shipped' WHERE id=1492;",
    "[2024-05-22 14:27:03] user=dan db=inventory duration=518ms statement: INSERT INTO products VALUES (1023, 'pen', 1.20);",
    "[2024-05-22 14:31:22] user=dan db=inventory duration=301ms statement: SELECT COUNT(*) FROM products;",
]

FILTERED_COUNT = len(SLOW_QUERIES_EXPECTED_LINES)
EXPECTED_FILTER_LOG_LINE = f"Filtered {FILTERED_COUNT} slow queries into slow_queries.log"

@pytest.mark.describe("Final OS/Filesystem state after student action")
def test_postgresql_log_unmodified():
    """
    The original log file must still exist and be unmodified.
    """
    assert os.path.isfile(POSTGRESQL_LOG_PATH), (
        f"{POSTGRESQL_LOG_PATH} is missing after task completion. It must not be deleted or moved."
    )
    with open(POSTGRESQL_LOG_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]
    assert lines == EXPECTED_LOG_LINES, (
        f"{POSTGRESQL_LOG_PATH} has been changed. It must remain unmodified after the task.\n"
        "Expected lines:\n"
        + "\n".join(EXPECTED_LOG_LINES)
        + "\n\nActual lines:\n"
        + "\n".join(lines)
    )

@pytest.mark.describe("Final OS/Filesystem state after student action")
def test_slow_queries_log_exists_and_correct():
    """
    The slow_queries.log must exist and contain only lines from postgresql.log
    where duration >= 300ms, preserving order and format.
    """
    assert os.path.isfile(SLOW_QUERIES_LOG_PATH), (
        f"Expected output file missing: {SLOW_QUERIES_LOG_PATH}.\n"
        "You must create this file with the filtered slow queries."
    )
    with open(SLOW_QUERIES_LOG_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]
    assert lines == SLOW_QUERIES_EXPECTED_LINES, (
        f"{SLOW_QUERIES_LOG_PATH} does not contain the correct filtered slow queries.\n"
        "Expected lines:\n"
        + "\n".join(SLOW_QUERIES_EXPECTED_LINES)
        + "\n\nActual lines:\n"
        + "\n".join(lines)
    )
    # Check that no extra lines are present
    assert len(lines) == FILTERED_COUNT, (
        f"{SLOW_QUERIES_LOG_PATH} contains an unexpected number of lines.\n"
        f"Expected {FILTERED_COUNT}, found {len(lines)}."
    )

@pytest.mark.describe("Final OS/Filesystem state after student action")
def test_filter_log_exists_and_correct():
    """
    The filter_log.txt must exist and contain exactly one line
    in the correct format.
    """
    assert os.path.isfile(FILTER_LOG_PATH), (
        f"Expected status file missing: {FILTER_LOG_PATH}.\n"
        "You must create this file after filtering."
    )
    with open(FILTER_LOG_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]
    assert len(lines) == 1, (
        f"{FILTER_LOG_PATH} should contain exactly one line. "
        f"Found {len(lines)} lines."
    )
    assert lines[0] == EXPECTED_FILTER_LOG_LINE, (
        f"{FILTER_LOG_PATH} does not have the correct status message.\n"
        f"Expected: {EXPECTED_FILTER_LOG_LINE!r}\n"
        f"Actual:   {lines[0]!r}"
    )

@pytest.mark.describe("Final OS/Filesystem state after student action")
def test_no_extra_files_created():
    """
    Ensure that no extra files were created in /home/user/db.
    Only postgresql.log, slow_queries.log, and filter_log.txt should exist.
    """
    expected_files = {
        "postgresql.log",
        "slow_queries.log",
        "filter_log.txt",
    }
    db_dir = "/home/user/db"
    assert os.path.isdir(db_dir), (
        f"Directory {db_dir} does not exist."
    )
    actual_files = set(
        f for f in os.listdir(db_dir)
        if os.path.isfile(os.path.join(db_dir, f))
    )
    extra_files = actual_files - expected_files
    missing_files = expected_files - actual_files
    assert not missing_files, (
        f"Missing expected file(s) in {db_dir}: {', '.join(sorted(missing_files))}"
    )
    assert not extra_files, (
        f"Unexpected extra file(s) found in {db_dir}: {', '.join(sorted(extra_files))}\n"
        "Only postgresql.log, slow_queries.log, and filter_log.txt should exist after the task."
    )