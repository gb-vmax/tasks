# test_final_state.py

import os
import pytest
import re

SAMPLE_LOG_PATH = "/home/user/sample_data.log"
FILTERED_LOG_PATH = "/home/user/filtered_errors_warnings.log"

EXPECTED_FILTERED_LINES = [
    "[2023-03-11 09:10:07] ERROR - File not found\n",
    "[2023-03-11 09:11:01] WARNING - Deprecated API usage\n",
    "[2023-03-11 09:12:02] ERROR - Connection reset by peer\n",
]

def _read_file_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()

def _extract_error_warning_lines(lines):
    """
    Returns only lines where STATUS is exactly 'ERROR' or 'WARNING'
    in the format: [YYYY-MM-DD HH:MM:SS] STATUS - message
    """
    pattern = re.compile(
        r"^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] (ERROR|WARNING) - .+\n$"
    )
    return [line for line in lines if pattern.match(line)]

def test_filtered_log_file_exists():
    assert os.path.isfile(FILTERED_LOG_PATH), (
        f"Expected output file '{FILTERED_LOG_PATH}' does not exist. "
        "You must create this file as part of the task."
    )

def test_filtered_log_content_exact():
    filtered_lines = _read_file_lines(FILTERED_LOG_PATH)
    assert filtered_lines == EXPECTED_FILTERED_LINES, (
        f"The contents of '{FILTERED_LOG_PATH}' are incorrect.\n"
        "Expected lines (order and formatting must match exactly):\n"
        f"{''.join(EXPECTED_FILTERED_LINES)}\n"
        "Actual lines:\n"
        f"{''.join(filtered_lines)}"
    )

def test_filtered_log_contains_only_error_warning_lines_from_sample():
    sample_lines = _read_file_lines(SAMPLE_LOG_PATH)
    expected_lines = _extract_error_warning_lines(sample_lines)
    filtered_lines = _read_file_lines(FILTERED_LOG_PATH)

    assert filtered_lines == expected_lines, (
        f"The output file '{FILTERED_LOG_PATH}' must contain only those lines from "
        f"'{SAMPLE_LOG_PATH}' where the STATUS is exactly 'ERROR' or 'WARNING', "
        "in the same order and with no formatting changes.\n"
        "Expected extracted lines:\n"
        f"{''.join(expected_lines)}\n"
        "Actual lines:\n"
        f"{''.join(filtered_lines)}"
    )

def test_filtered_log_no_extra_or_missing_lines():
    filtered_lines = _read_file_lines(FILTERED_LOG_PATH)
    # Check that there are no duplicate, missing, or extra lines
    assert len(filtered_lines) == len(EXPECTED_FILTERED_LINES), (
        f"'{FILTERED_LOG_PATH}' should have exactly {len(EXPECTED_FILTERED_LINES)} lines, "
        f"but it has {len(filtered_lines)} lines."
    )
    for idx, (actual, expected) in enumerate(zip(filtered_lines, EXPECTED_FILTERED_LINES)):
        assert actual == expected, (
            f"Line {idx+1} in '{FILTERED_LOG_PATH}' does not match expected value.\n"
            f"Expected: {expected!r}\n"
            f"Actual:   {actual!r}"
        )

def test_filtered_log_no_extra_blank_lines_or_trailing_spaces():
    filtered_lines = _read_file_lines(FILTERED_LOG_PATH)
    for idx, line in enumerate(filtered_lines):
        assert line.endswith('\n'), (
            f"Line {idx+1} in '{FILTERED_LOG_PATH}' is missing a trailing newline."
        )
        assert line.rstrip('\n') == line.strip('\n'), (
            f"Line {idx+1} in '{FILTERED_LOG_PATH}' contains trailing spaces or tabs. "
            "No extra whitespace is allowed."
        )