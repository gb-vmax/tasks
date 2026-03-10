# test_final_state.py

import os
import pytest

ETL_DIR = "/home/user/etl"
PIPELINE_LOG = "/home/user/etl/pipeline.log"
ERRORS_LOG = "/home/user/etl/errors.log"
ERROR_COUNT_TXT = "/home/user/etl/error_count.txt"

EXPECTED_ERRORS_LOG_CONTENTS = """\
2024-11-01 03:12:45 | ERROR | [TRANSFORM] | null value in non-nullable column "user_id"
2024-11-01 03:14:02 | ERROR | [LOAD] | deadlock detected on table "events", retrying
2024-11-01 03:15:12 | ERROR | [TRANSFORM] | division by zero in metric "conversion_rate"
2024-11-01 03:15:44 | ERROR | [LOAD] | disk quota exceeded on target warehouse"""

EXPECTED_ERROR_COUNT = 4

EXPECTED_MATCHED_LINES = [
    '2024-11-01 03:12:45 | ERROR | [TRANSFORM] | null value in non-nullable column "user_id"',
    '2024-11-01 03:14:02 | ERROR | [LOAD] | deadlock detected on table "events", retrying',
    '2024-11-01 03:15:12 | ERROR | [TRANSFORM] | division by zero in metric "conversion_rate"',
    '2024-11-01 03:15:44 | ERROR | [LOAD] | disk quota exceeded on target warehouse',
]


# ── Directory / source file still intact ─────────────────────────────────────

def test_etl_directory_still_exists():
    assert os.path.isdir(ETL_DIR), (
        f"Directory '{ETL_DIR}' does not exist. "
        "The ETL working directory must be present after the task."
    )


def test_pipeline_log_still_exists():
    assert os.path.isfile(PIPELINE_LOG), (
        f"Source file '{PIPELINE_LOG}' no longer exists. "
        "The original pipeline.log must not be deleted or moved."
    )


# ── errors.log existence and readability ─────────────────────────────────────

def test_errors_log_exists():
    assert os.path.isfile(ERRORS_LOG), (
        f"Output file '{ERRORS_LOG}' does not exist. "
        "The filtering step must create errors.log."
    )


def test_errors_log_is_readable():
    assert os.access(ERRORS_LOG, os.R_OK), (
        f"File '{ERRORS_LOG}' exists but is not readable."
    )


# ── errors.log content ────────────────────────────────────────────────────────

def test_errors_log_exact_contents():
    with open(ERRORS_LOG, "r") as f:
        actual = f.read()

    # Strip a single trailing newline for comparison (both forms are acceptable)
    actual_stripped = actual.rstrip("\n")
    assert actual_stripped == EXPECTED_ERRORS_LOG_CONTENTS, (
        f"Contents of '{ERRORS_LOG}' do not match expected.\n\n"
        f"Expected:\n{EXPECTED_ERRORS_LOG_CONTENTS}\n\n"
        f"Actual:\n{actual_stripped}"
    )


def test_errors_log_line_count():
    with open(ERRORS_LOG, "r") as f:
        lines = [l for l in f.read().splitlines() if l.strip()]
    assert len(lines) == EXPECTED_ERROR_COUNT, (
        f"Expected {EXPECTED_ERROR_COUNT} non-empty lines in '{ERRORS_LOG}', "
        f"but found {len(lines)}.\nLines found:\n" + "\n".join(lines)
    )


def test_errors_log_no_trailing_blank_lines():
    with open(ERRORS_LOG, "r") as f:
        raw = f.read()
    # At most one trailing newline is fine; two or more means a blank line
    assert not raw.endswith("\n\n"), (
        f"'{ERRORS_LOG}' has trailing blank line(s). "
        "The file must end after the last matched line (optionally one newline)."
    )


def test_errors_log_contains_only_transform_and_load_errors():
    with open(ERRORS_LOG, "r") as f:
        lines = [l for l in f.read().splitlines() if l.strip()]

    for line in lines:
        assert "ERROR" in line, (
            f"Non-ERROR line found in '{ERRORS_LOG}':\n  {line}"
        )
        assert ("[TRANSFORM]" in line or "[LOAD]" in line), (
            f"Line in '{ERRORS_LOG}' is not from [TRANSFORM] or [LOAD] stage:\n  {line}"
        )


def test_errors_log_excludes_extract_errors():
    with open(ERRORS_LOG, "r") as f:
        contents = f.read()
    assert "[EXTRACT]" not in contents, (
        f"'{ERRORS_LOG}' contains [EXTRACT] lines, which must be excluded.\n"
        f"File contents:\n{contents}"
    )


def test_errors_log_excludes_validate_errors():
    with open(ERRORS_LOG, "r") as f:
        contents = f.read()
    assert "[VALIDATE]" not in contents, (
        f"'{ERRORS_LOG}' contains [VALIDATE] lines, which must be excluded.\n"
        f"File contents:\n{contents}"
    )


def test_errors_log_excludes_warn_lines():
    with open(ERRORS_LOG, "r") as f:
        contents = f.read()
    assert "WARN" not in contents, (
        f"'{ERRORS_LOG}' contains WARN lines, which must be excluded.\n"
        f"File contents:\n{contents}"
    )


def test_errors_log_excludes_info_lines():
    with open(ERRORS_LOG, "r") as f:
        contents = f.read()
    assert "INFO" not in contents, (
        f"'{ERRORS_LOG}' contains INFO lines, which must be excluded.\n"
        f"File contents:\n{contents}"
    )


def test_errors_log_excludes_debug_lines():
    with open(ERRORS_LOG, "r") as f:
        contents = f.read()
    assert "DEBUG" not in contents, (
        f"'{ERRORS_LOG}' contains DEBUG lines, which must be excluded.\n"
        f"File contents:\n{contents}"
    )


def test_errors_log_preserves_order():
    with open(ERRORS_LOG, "r") as f:
        actual_lines = [l for l in f.read().splitlines() if l.strip()]
    assert actual_lines == EXPECTED_MATCHED_LINES, (
        f"Lines in '{ERRORS_LOG}' are not in the correct order.\n\n"
        f"Expected order:\n" + "\n".join(EXPECTED_MATCHED_LINES) + "\n\n"
        f"Actual order:\n" + "\n".join(actual_lines)
    )


def test_errors_log_lines_unmodified():
    with open(ERRORS_LOG, "r") as f:
        actual_lines = [l for l in f.read().splitlines() if l.strip()]
    for expected, actual in zip(EXPECTED_MATCHED_LINES, actual_lines):
        assert actual == expected, (
            f"Line content was modified in '{ERRORS_LOG}'.\n"
            f"  Expected : {expected!r}\n"
            f"  Actual   : {actual!r}"
        )


# ── error_count.txt existence and readability ─────────────────────────────────

def test_error_count_txt_exists():
    assert os.path.isfile(ERROR_COUNT_TXT), (
        f"Output file '{ERROR_COUNT_TXT}' does not exist. "
        "The count step must create error_count.txt."
    )


def test_error_count_txt_is_readable():
    assert os.access(ERROR_COUNT_TXT, os.R_OK), (
        f"File '{ERROR_COUNT_TXT}' exists but is not readable."
    )


# ── error_count.txt content ───────────────────────────────────────────────────

def test_error_count_txt_exact_contents():
    with open(ERROR_COUNT_TXT, "r") as f:
        raw = f.read()

    expected_raw = f"{EXPECTED_ERROR_COUNT}\n"
    assert raw == expected_raw, (
        f"Contents of '{ERROR_COUNT_TXT}' do not match expected.\n"
        f"Expected repr : {expected_raw!r}\n"
        f"Actual repr   : {raw!r}"
    )


def test_error_count_txt_is_integer():
    with open(ERROR_COUNT_TXT, "r") as f:
        raw = f.read().strip()
    assert raw.isdigit(), (
        f"'{ERROR_COUNT_TXT}' does not contain a plain integer. "
        f"Got: {raw!r}"
    )


def test_error_count_txt_value():
    with open(ERROR_COUNT_TXT, "r") as f:
        raw = f.read().strip()
    try:
        count = int(raw)
    except ValueError:
        pytest.fail(
            f"'{ERROR_COUNT_TXT}' cannot be parsed as an integer. Got: {raw!r}"
        )
    assert count == EXPECTED_ERROR_COUNT, (
        f"Count in '{ERROR_COUNT_TXT}' is {count}, expected {EXPECTED_ERROR_COUNT}."
    )


def test_error_count_txt_no_extra_whitespace():
    with open(ERROR_COUNT_TXT, "r") as f:
        raw = f.read()
    # Must be exactly "<digit(s)>\n" — no spaces, no extra newlines
    assert raw == raw.strip() + "\n", (
        f"'{ERROR_COUNT_TXT}' contains extra whitespace beyond the trailing newline.\n"
        f"Got repr: {raw!r}"
    )


def test_error_count_matches_errors_log_line_count():
    """Cross-check: the integer in error_count.txt must equal the line count in errors.log."""
    with open(ERROR_COUNT_TXT, "r") as f:
        count_from_file = int(f.read().strip())

    with open(ERRORS_LOG, "r") as f:
        lines_in_errors_log = [l for l in f.read().splitlines() if l.strip()]

    assert count_from_file == len(lines_in_errors_log), (
        f"Mismatch: '{ERROR_COUNT_TXT}' says {count_from_file} errors, "
        f"but '{ERRORS_LOG}' has {len(lines_in_errors_log)} non-empty lines."
    )