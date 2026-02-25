# test_final_state.py

import os
import stat
import pytest

INTEGRATION_TESTS_DIR = "/home/user/integration_tests"
LEGACY_TEST_PATH = os.path.join(INTEGRATION_TESTS_DIR, "legacy_api_test.py")
LOG_PATH = os.path.join(INTEGRATION_TESTS_DIR, "test_run.log")

# The exact output that should be in the log file after running the script
EXPECTED_LOG = (
    "=== Starting Legacy API Integration Test ===\n"
    "Connecting to API endpoint http://localhost:7000/api/v1/check ...\n"
    "Status: 200 OK\n"
    "Payload: {'result':'success','service':'auth'}\n"
    "=== Test Passed ===\n"
)

def test_log_file_exists():
    assert os.path.isfile(LOG_PATH), (
        f"Expected log file {LOG_PATH} not found.\n"
        "You must create this file by running the script and capturing all output."
    )

def test_log_file_permissions():
    st = os.stat(LOG_PATH)
    user_readable = bool(st.st_mode & stat.S_IRUSR)
    user_writable = bool(st.st_mode & stat.S_IWUSR)
    assert user_readable and user_writable, (
        f"Log file {LOG_PATH} must be readable and writable by the user."
    )

def test_log_file_content_exact_match():
    """
    Checks that the log file contains the exact expected output, including line
    endings, order, blank lines, and that stderr is captured if present.
    """
    try:
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            log_contents = f.read()
    except Exception as e:
        pytest.fail(f"Could not read {LOG_PATH}: {e}")

    # Accept both Unix and Windows line endings, but require output as it would appear on the terminal
    # Normalize both to \n for comparison
    norm_actual = log_contents.replace('\r\n', '\n')
    norm_expected = EXPECTED_LOG.replace('\r\n', '\n')

    assert norm_actual == norm_expected, (
        f"The contents of {LOG_PATH} do not match the expected output.\n\n"
        "Expected output:\n"
        "-------------------\n"
        f"{norm_expected}\n"
        "-------------------\n"
        "Actual output:\n"
        "-------------------\n"
        f"{norm_actual}\n"
        "-------------------\n"
        "If there are extra/missing lines, wrong order, or missing error output, "
        "the script was not run or output was not captured exactly."
    )

def test_log_file_is_not_empty():
    size = os.path.getsize(LOG_PATH)
    assert size > 0, (
        f"The log file {LOG_PATH} is empty. "
        "You must capture the script's output in this file."
    )

def test_legacy_script_still_exists():
    assert os.path.isfile(LEGACY_TEST_PATH), (
        f"Legacy script {LEGACY_TEST_PATH} is missing after the task. "
        "Do not remove or modify the original script."
    )

def test_log_file_is_newer_than_script():
    log_stat = os.stat(LOG_PATH)
    script_stat = os.stat(LEGACY_TEST_PATH)
    assert log_stat.st_mtime >= script_stat.st_mtime, (
        f"The log file {LOG_PATH} appears older than the script {LEGACY_TEST_PATH}.\n"
        "You must re-run the script after any changes, and ensure the log is up to date."
    )