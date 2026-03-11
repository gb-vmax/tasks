# test_final_state.py

import os
import pytest

LOG_FILE = "/home/user/logs/uptime_monitor.log"
FAILED_CHECKS_FILE = "/home/user/logs/failed_checks.txt"
FAILED_COUNT_FILE = "/home/user/logs/failed_count.txt"

EXPECTED_FAILED_LINES = [
    "[2024-06-10T08:00:15Z] [ERROR] host=db.internal status=DOWN response_time_ms=5003 check_id=chk_002",
    "[2024-06-10T08:01:00Z] [ERROR] host=payments.example.com status=TIMEOUT response_time_ms=30001 check_id=chk_004",
    "[2024-06-10T08:01:30Z] [ERROR] host=auth.internal status=DOWN response_time_ms=9999 check_id=chk_006",
    "[2024-06-10T08:02:15Z] [ERROR] host=db.internal status=TIMEOUT response_time_ms=30001 check_id=chk_008",
]

EXPECTED_FAILED_COUNT = 4


# --- Tests for failed_checks.txt ---

def test_failed_checks_file_exists():
    assert os.path.isfile(FAILED_CHECKS_FILE), (
        f"Expected output file '{FAILED_CHECKS_FILE}' to exist, but it was not found. "
        "The task requires writing failed checks to this file."
    )


def test_failed_checks_file_is_readable():
    assert os.access(FAILED_CHECKS_FILE, os.R_OK), (
        f"File '{FAILED_CHECKS_FILE}' exists but is not readable."
    )


def test_failed_checks_file_has_correct_number_of_lines():
    with open(FAILED_CHECKS_FILE, "r") as f:
        lines = [line for line in f.read().splitlines() if line.strip()]
    assert len(lines) == EXPECTED_FAILED_COUNT, (
        f"Expected {EXPECTED_FAILED_COUNT} lines in '{FAILED_CHECKS_FILE}', "
        f"but found {len(lines)}.\nActual lines:\n" + "\n".join(lines)
    )


def test_failed_checks_file_contains_only_failed_statuses():
    with open(FAILED_CHECKS_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    for line in lines:
        assert "status=DOWN" in line or "status=TIMEOUT" in line, (
            f"Found a line in '{FAILED_CHECKS_FILE}' that does not have status=DOWN or status=TIMEOUT:\n"
            f"  {line!r}\n"
            "Only lines with status=DOWN or status=TIMEOUT should be included."
        )


def test_failed_checks_file_does_not_contain_up_lines():
    with open(FAILED_CHECKS_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    up_lines = [line for line in lines if "status=UP" in line]
    assert len(up_lines) == 0, (
        f"Found lines with status=UP in '{FAILED_CHECKS_FILE}' — these should not be included:\n"
        + "\n".join(up_lines)
    )


def test_failed_checks_file_lines_match_expected_exactly():
    with open(FAILED_CHECKS_FILE, "r") as f:
        content = f.read()
    actual_lines = [line for line in content.splitlines() if line.strip()]
    assert actual_lines == EXPECTED_FAILED_LINES, (
        f"Content of '{FAILED_CHECKS_FILE}' does not match expected.\n\n"
        f"Expected lines:\n" + "\n".join(EXPECTED_FAILED_LINES) + "\n\n"
        f"Actual lines:\n" + "\n".join(actual_lines)
    )


def test_failed_checks_file_lines_are_verbatim_from_source():
    """Each line in failed_checks.txt must appear verbatim in the original log."""
    with open(LOG_FILE, "r") as f:
        log_lines = set(line.rstrip("\n") for line in f if line.strip())
    with open(FAILED_CHECKS_FILE, "r") as f:
        failed_lines = [line.rstrip("\n") for line in f if line.strip()]
    for line in failed_lines:
        assert line in log_lines, (
            f"Line in '{FAILED_CHECKS_FILE}' was not found verbatim in '{LOG_FILE}':\n"
            f"  {line!r}\n"
            "Lines must be copied exactly as they appear in the source log."
        )


def test_failed_checks_file_preserves_order_from_source():
    """Lines in failed_checks.txt must appear in the same order as in the source log."""
    with open(LOG_FILE, "r") as f:
        log_lines = [line.rstrip("\n") for line in f if line.strip()]
    with open(FAILED_CHECKS_FILE, "r") as f:
        failed_lines = [line.rstrip("\n") for line in f if line.strip()]

    # Get indices of failed lines in the original log
    log_indices = []
    for line in failed_lines:
        try:
            idx = log_lines.index(line)
            log_indices.append(idx)
        except ValueError:
            pytest.fail(
                f"Line in '{FAILED_CHECKS_FILE}' not found in '{LOG_FILE}':\n  {line!r}"
            )

    assert log_indices == sorted(log_indices), (
        f"Lines in '{FAILED_CHECKS_FILE}' are not in the same order as they appear in '{LOG_FILE}'.\n"
        f"Expected order indices: {sorted(log_indices)}\n"
        f"Actual order indices:   {log_indices}"
    )


def test_failed_checks_file_no_extra_content():
    """failed_checks.txt should contain no headers, footers, or extra blank lines beyond content."""
    with open(FAILED_CHECKS_FILE, "r") as f:
        raw_content = f.read()
    # Strip trailing newline (acceptable), but check no extra blank lines in between
    lines = raw_content.rstrip("\n").splitlines()
    non_empty_lines = [l for l in lines if l.strip()]
    assert len(lines) == len(non_empty_lines), (
        f"'{FAILED_CHECKS_FILE}' contains unexpected blank lines. "
        f"All {len(lines)} lines should be non-empty log entries."
    )
    assert len(non_empty_lines) == EXPECTED_FAILED_COUNT, (
        f"Expected exactly {EXPECTED_FAILED_COUNT} non-empty lines in '{FAILED_CHECKS_FILE}', "
        f"but found {len(non_empty_lines)}."
    )


# --- Tests for failed_count.txt ---

def test_failed_count_file_exists():
    assert os.path.isfile(FAILED_COUNT_FILE), (
        f"Expected output file '{FAILED_COUNT_FILE}' to exist, but it was not found. "
        "The task requires writing the failed check count to this file."
    )


def test_failed_count_file_is_readable():
    assert os.access(FAILED_COUNT_FILE, os.R_OK), (
        f"File '{FAILED_COUNT_FILE}' exists but is not readable."
    )


def test_failed_count_file_contains_only_a_number():
    with open(FAILED_COUNT_FILE, "r") as f:
        content = f.read().strip()
    assert content.isdigit(), (
        f"'{FAILED_COUNT_FILE}' should contain only a single integer, "
        f"but got: {content!r}"
    )


def test_failed_count_file_correct_value():
    with open(FAILED_COUNT_FILE, "r") as f:
        content = f.read().strip()
    try:
        count = int(content)
    except ValueError:
        pytest.fail(
            f"Could not parse integer from '{FAILED_COUNT_FILE}'. Content was: {content!r}"
        )
    assert count == EXPECTED_FAILED_COUNT, (
        f"Expected the count in '{FAILED_COUNT_FILE}' to be {EXPECTED_FAILED_COUNT}, "
        f"but got {count}."
    )


def test_failed_count_file_has_exactly_one_line():
    with open(FAILED_COUNT_FILE, "r") as f:
        raw_content = f.read()
    # Allow a single trailing newline, but no more content
    stripped = raw_content.strip()
    lines = [l for l in raw_content.splitlines() if l.strip()]
    assert len(lines) == 1, (
        f"'{FAILED_COUNT_FILE}' should contain exactly one line (the count), "
        f"but found {len(lines)} non-empty lines. Content was: {raw_content!r}"
    )


def test_failed_count_matches_failed_checks_lines():
    """The count in failed_count.txt must equal the number of lines in failed_checks.txt."""
    with open(FAILED_COUNT_FILE, "r") as f:
        count_content = f.read().strip()
    with open(FAILED_CHECKS_FILE, "r") as f:
        failed_lines = [line for line in f.read().splitlines() if line.strip()]

    try:
        count = int(count_content)
    except ValueError:
        pytest.fail(
            f"Could not parse integer from '{FAILED_COUNT_FILE}'. Content was: {count_content!r}"
        )

    assert count == len(failed_lines), (
        f"The count in '{FAILED_COUNT_FILE}' ({count}) does not match "
        f"the number of lines in '{FAILED_CHECKS_FILE}' ({len(failed_lines)}). "
        "These two values must be consistent."
    )


# --- Sanity check: source log file still intact ---

def test_source_log_file_still_intact():
    """The original log file should not have been modified."""
    EXPECTED_LOG_CONTENT = """\
[2024-06-10T08:00:01Z] [INFO] host=api.example.com status=UP response_time_ms=98 check_id=chk_001
[2024-06-10T08:00:15Z] [ERROR] host=db.internal status=DOWN response_time_ms=5003 check_id=chk_002
[2024-06-10T08:00:30Z] [INFO] host=cache.internal status=UP response_time_ms=210 check_id=chk_003
[2024-06-10T08:01:00Z] [ERROR] host=payments.example.com status=TIMEOUT response_time_ms=30001 check_id=chk_004
[2024-06-10T08:01:15Z] [INFO] host=api.example.com status=UP response_time_ms=105 check_id=chk_005
[2024-06-10T08:01:30Z] [ERROR] host=auth.internal status=DOWN response_time_ms=9999 check_id=chk_006
[2024-06-10T08:02:00Z] [INFO] host=cache.internal status=UP response_time_ms=188 check_id=chk_007
[2024-06-10T08:02:15Z] [ERROR] host=db.internal status=TIMEOUT response_time_ms=30001 check_id=chk_008
[2024-06-10T08:02:45Z] [INFO] host=payments.example.com status=UP response_time_ms=312 check_id=chk_009
[2024-06-10T08:03:00Z] [INFO] host=api.example.com status=UP response_time_ms=99 check_id=chk_010"""

    assert os.path.isfile(LOG_FILE), (
        f"Source log file '{LOG_FILE}' is missing — it should not have been deleted."
    )
    with open(LOG_FILE, "r") as f:
        actual = f.read().rstrip("\n")
    assert actual == EXPECTED_LOG_CONTENT, (
        f"Source log file '{LOG_FILE}' has been modified. It must remain unchanged.\n\n"
        f"Expected:\n{EXPECTED_LOG_CONTENT}\n\nActual:\n{actual}"
    )