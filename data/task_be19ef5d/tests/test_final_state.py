# test_final_state.py

"""
Pytest suite to validate the final state of the OS/container after extracting 404 errors
from /home/user/logs/webserver_access.log to /home/user/logs/404_errors.log.

This suite ensures:
- The output file exists.
- It contains only the exact lines from the access log that match ' 404 ' (space-404-space).
- The lines are in the same order and unmodified.
- No extra or missing lines.
- No other files in /home/user/logs/ are changed.
"""

import os
import pytest
import hashlib

LOGS_DIR = "/home/user/logs"
ACCESS_LOG = "/home/user/logs/webserver_access.log"
ERRORS_LOG = "/home/user/logs/404_errors.log"

@pytest.mark.final_state
def test_404_errors_log_exists():
    assert os.path.isfile(ERRORS_LOG), (
        f"Expected output file '{ERRORS_LOG}' does not exist. "
        "You must create this file containing all lines with ' 404 ' from the access log."
    )

@pytest.mark.final_state
def test_404_errors_log_contents_exact():
    """
    Ensure that /home/user/logs/404_errors.log contains only the lines from
    /home/user/logs/webserver_access.log that include ' 404 ' (space-404-space),
    in the original order and formatting. No extra or modified lines.
    """
    try:
        with open(ACCESS_LOG, "r", encoding="utf-8") as f:
            access_lines = f.readlines()
    except Exception as e:
        pytest.fail(f"Could not read '{ACCESS_LOG}': {e}")

    expected_404_lines = [line for line in access_lines if " 404 " in line]

    try:
        with open(ERRORS_LOG, "r", encoding="utf-8") as f:
            actual_404_lines = f.readlines()
    except Exception as e:
        pytest.fail(f"Could not read '{ERRORS_LOG}': {e}")

    if actual_404_lines != expected_404_lines:
        # Provide detailed error message
        missing = [line for line in expected_404_lines if line not in actual_404_lines]
        extra = [line for line in actual_404_lines if line not in expected_404_lines]
        msg = []
        if missing:
            msg.append(f"Missing expected 404 lines in '{ERRORS_LOG}':\n" +
                       "".join(missing))
        if extra:
            msg.append(f"Unexpected extra lines in '{ERRORS_LOG}':\n" +
                       "".join(extra))
        if len(actual_404_lines) == len(expected_404_lines) and actual_404_lines != expected_404_lines:
            msg.append("Lines in output file are not in the same order or have been modified.")
        pytest.fail(
            f"'{ERRORS_LOG}' does not contain exactly the expected 404 lines from '{ACCESS_LOG}'.\n"
            + "\n".join(msg)
        )

@pytest.mark.final_state
def test_404_errors_log_no_extra_lines():
    """
    Ensure that no lines are present in 404_errors.log except those that match ' 404 ' in the access log.
    """
    with open(ACCESS_LOG, "r", encoding="utf-8") as f:
        access_lines = f.readlines()
    expected_404_lines = [line for line in access_lines if " 404 " in line]
    with open(ERRORS_LOG, "r", encoding="utf-8") as f:
        output_lines = f.readlines()
    non_matching_lines = [line for line in output_lines if " 404 " not in line]
    assert not non_matching_lines, (
        f"'{ERRORS_LOG}' contains lines that do not have ' 404 ':\n" +
        "".join(non_matching_lines)
    )
    assert len(output_lines) == len(expected_404_lines), (
        f"'{ERRORS_LOG}' contains {len(output_lines)} lines, but {len(expected_404_lines)} expected. "
        "There may be extra or missing lines."
    )

@pytest.mark.final_state
def test_access_log_unmodified():
    """
    Ensure the original access log file has not been modified (content and order preserved).
    """
    # To robustly check that the file is unmodified, we hash its contents.
    try:
        with open(ACCESS_LOG, "rb") as f:
            access_log_bytes = f.read()
    except Exception as e:
        pytest.fail(f"Could not read '{ACCESS_LOG}' for hash check: {e}")
    access_log_hash = hashlib.sha256(access_log_bytes).hexdigest()

    # For this test, we assume the initial sample for /home/user/logs/webserver_access.log is:
    TRUTH_SAMPLE = (
        b'127.0.0.1 - - [10/Jun/2024:10:15:32 +0000] "GET /index.html HTTP/1.1" 200 1024\n'
        b'127.0.0.1 - - [10/Jun/2024:10:16:03 +0000] "GET /nonexistent.jpg HTTP/1.1" 404 512\n'
        b'127.0.0.1 - - [10/Jun/2024:10:16:45 +0000] "POST /api/v1/users HTTP/1.1" 201 2048\n'
        b'127.0.0.1 - - [10/Jun/2024:10:17:10 +0000] "GET /not_found.html HTTP/1.1" 404 256\n'
        b'127.0.0.1 - - [10/Jun/2024:10:17:45 +0000] "GET /favicon.ico HTTP/1.1" 200 150\n'
    )
    truth_hash = hashlib.sha256(TRUTH_SAMPLE).hexdigest()

    assert access_log_hash == truth_hash, (
        f"'{ACCESS_LOG}' appears to have been modified. "
        "The original access log content must not be altered by this task."
    )

@pytest.mark.final_state
def test_no_other_logs_modified():
    """
    Ensure that no other files in /home/user/logs/ (besides 404_errors.log) have been modified or created.
    """
    # List all files in the logs directory
    try:
        all_files = [
            os.path.join(LOGS_DIR, f)
            for f in os.listdir(LOGS_DIR)
            if os.path.isfile(os.path.join(LOGS_DIR, f))
        ]
    except Exception as e:
        pytest.fail(f"Could not list files in '{LOGS_DIR}': {e}")

    # Only expected files: webserver_access.log and 404_errors.log
    expected_files = {ACCESS_LOG, ERRORS_LOG}
    found_files = set(all_files)

    unexpected_files = found_files - expected_files
    missing_files = {ACCESS_LOG} - found_files

    assert not missing_files, (
        f"Required log file(s) missing after task: {missing_files}. "
        "No files should be deleted from the logs directory."
    )
    assert not unexpected_files, (
        f"Unexpected file(s) present in '{LOGS_DIR}': {unexpected_files}. "
        "No new files should be created in the logs directory except 404_errors.log."
    )