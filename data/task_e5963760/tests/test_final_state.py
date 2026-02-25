# test_final_state.py

import os
import pytest

BUILD_DIR = "/home/user/builds"
BUILD_LOG = "/home/user/builds/build_output.log"
BUILD_ERRORS_SUMMARY = "/home/user/builds/build_errors_summary.txt"

EXPECTED_ERRORS_SUMMARY_LINES = [
    "ERROR: Failed to resolve dependency 'libfoo'",
    "ERROR: Timeout while connecting to repository",
    "ERROR: Insufficient disk space"
]

def test_builds_directory_still_exists_and_writable():
    assert os.path.isdir(BUILD_DIR), (
        f"Directory {BUILD_DIR} does not exist after the task. "
        "The builds directory must remain present."
    )
    assert os.access(BUILD_DIR, os.W_OK), (
        f"Directory {BUILD_DIR} is not writable after the task. "
        "Agent must retain write permissions to builds directory."
    )

def test_build_errors_summary_exists_and_content():
    assert os.path.isfile(BUILD_ERRORS_SUMMARY), (
        f"File {BUILD_ERRORS_SUMMARY} does not exist after the task. "
        "You must create this file containing the unique error messages."
    )
    with open(BUILD_ERRORS_SUMMARY, "r", encoding="utf-8") as f:
        summary_lines = [line.rstrip('\n') for line in f]

    assert summary_lines == EXPECTED_ERRORS_SUMMARY_LINES, (
        f"File {BUILD_ERRORS_SUMMARY} does not have the expected content.\n"
        f"Expected lines:\n{EXPECTED_ERRORS_SUMMARY_LINES!r}\n"
        f"Found lines:\n{summary_lines!r}\n"
        "Ensure you have written all and only the unique ERROR lines, in order, with no extra blank lines."
    )

def test_build_errors_summary_no_blank_lines():
    with open(BUILD_ERRORS_SUMMARY, "r", encoding="utf-8") as f:
        summary_lines = f.readlines()
    if summary_lines:
        assert summary_lines[0].strip() != "", (
            f"File {BUILD_ERRORS_SUMMARY} has a blank line at the beginning."
        )
        assert summary_lines[-1].strip() != "", (
            f"File {BUILD_ERRORS_SUMMARY} has a blank line at the end."
        )
        for i, line in enumerate(summary_lines):
            if i < len(summary_lines) - 1:
                assert line.endswith('\n'), (
                    f"Line {i+1} in {BUILD_ERRORS_SUMMARY!r} does not end with a newline."
                )

def test_build_errors_summary_contains_only_error_lines():
    with open(BUILD_ERRORS_SUMMARY, "r", encoding="utf-8") as f:
        summary_lines = [line.rstrip('\n') for line in f]
    for line in summary_lines:
        assert line.startswith("ERROR:"), (
            f"Line in {BUILD_ERRORS_SUMMARY!r} does not start with 'ERROR:': {line!r}"
        )

def test_build_output_log_untouched():
    # The build_output.log file should not be altered by this task
    expected_build_log_lines = [
        "INFO: Build started at 2024-05-22 09:00:01",
        "WARNING: Deprecated API used",
        "ERROR: Failed to resolve dependency 'libfoo'",
        "ERROR: Timeout while connecting to repository",
        "ERROR: Failed to resolve dependency 'libfoo'",
        "INFO: Build finished at 2024-05-22 09:00:34",
        "ERROR: Insufficient disk space",
    ]
    assert os.path.isfile(BUILD_LOG), (
        f"File {BUILD_LOG} is missing after the task. "
        "You must not delete or move the original build log."
    )
    with open(BUILD_LOG, "r", encoding="utf-8") as f:
        actual_lines = [line.rstrip('\n') for line in f]
    assert actual_lines == expected_build_log_lines, (
        f"File {BUILD_LOG} was modified during the task.\n"
        "You must not change the original build log file."
    )