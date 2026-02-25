# test_final_state.py

import os
import pytest

MICROSERVICE_LOGS_DIR = "/home/user/microservice_logs"
API_LOG = os.path.join(MICROSERVICE_LOGS_DIR, "api.log")
DB_LOG = os.path.join(MICROSERVICE_LOGS_DIR, "db.log")
CACHE_LOG = os.path.join(MICROSERVICE_LOGS_DIR, "cache.log")
ERROR_SUMMARY_LOG = os.path.join(MICROSERVICE_LOGS_DIR, "error_summary.log")

TRUTH_API_LOG = [
    "2024-06-18 14:02:07 INFO Connected to API Gateway.",
    "2024-06-18 14:03:01 ERROR Failed to fetch user data.",
    "2024-06-18 14:03:45 WARN Response time high.",
    "2024-06-18 14:04:00 ERROR Token expired.",
]
TRUTH_DB_LOG = [
    "2024-06-18 14:02:10 INFO Database connection established.",
    "2024-06-18 14:03:05 ERROR Connection timeout.",
    "2024-06-18 14:03:50 WARN Slow query detected.",
]
TRUTH_CACHE_LOG = [
    "2024-06-18 14:02:15 INFO Cache initialized.",
    "2024-06-18 14:03:10 ERROR Redis unreachable.",
    "2024-06-18 14:03:55 INFO Cache hit rate: 95%.",
]
TRUTH_ERROR_SUMMARY_LOG = [
    "API.LOG: 2024-06-18 14:03:01 ERROR Failed to fetch user data.",
    "API.LOG: 2024-06-18 14:04:00 ERROR Token expired.",
    "DB.LOG: 2024-06-18 14:03:05 ERROR Connection timeout.",
    "CACHE.LOG: 2024-06-18 14:03:10 ERROR Redis unreachable.",
]

@pytest.mark.parametrize("path", [
    MICROSERVICE_LOGS_DIR,
])
def test_logs_directory_exists(path):
    assert os.path.isdir(path), f"Required directory missing: {path}"

@pytest.mark.parametrize("path,expected_lines", [
    (API_LOG, TRUTH_API_LOG),
    (DB_LOG, TRUTH_DB_LOG),
    (CACHE_LOG, TRUTH_CACHE_LOG),
])
def test_log_file_untouched_and_contents(path, expected_lines):
    assert os.path.isfile(path), f"Required log file missing: {path}"
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    assert lines == expected_lines, (
        f"Contents of {path} do not match expected after task completion.\n"
        f"Expected:\n{expected_lines}\nActual:\n{lines}"
    )

def test_error_summary_log_exists():
    assert os.path.isfile(ERROR_SUMMARY_LOG), (
        f"{ERROR_SUMMARY_LOG} was not created. "
        f"Expected error summary file to exist at the absolute path."
    )

def test_error_summary_log_contents_exact():
    if not os.path.isfile(ERROR_SUMMARY_LOG):
        pytest.fail(f"{ERROR_SUMMARY_LOG} does not exist, so its contents cannot be validated.")

    with open(ERROR_SUMMARY_LOG, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    assert lines == TRUTH_ERROR_SUMMARY_LOG, (
        f"Contents of {ERROR_SUMMARY_LOG} do not match the required output.\n"
        f"Expected:\n" +
        "\n".join(TRUTH_ERROR_SUMMARY_LOG) +
        "\nActual:\n" +
        "\n".join(lines)
    )

def test_error_summary_log_formatting_and_order():
    """
    Double-checks the formatting and ordering of entries in error_summary.log.
    """
    if not os.path.isfile(ERROR_SUMMARY_LOG):
        pytest.fail(f"{ERROR_SUMMARY_LOG} does not exist, so its formatting cannot be validated.")

    with open(ERROR_SUMMARY_LOG, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    # Check number of lines
    assert len(lines) == 4, (
        f"error_summary.log must have exactly 4 lines (one for each ERROR entry). "
        f"Found {len(lines)} lines."
    )

    # Check prefixes and ordering
    expected_prefixes = [
        "API.LOG: ",
        "API.LOG: ",
        "DB.LOG: ",
        "CACHE.LOG: ",
    ]
    for idx, (line, prefix) in enumerate(zip(lines, expected_prefixes)):
        assert line.startswith(prefix), (
            f"Line {idx+1} of error_summary.log should start with '{prefix}' "
            f"but got: '{line}'"
        )

    # Check that the message after the prefix matches the original error line
    expected_error_lines = [
        "2024-06-18 14:03:01 ERROR Failed to fetch user data.",
        "2024-06-18 14:04:00 ERROR Token expired.",
        "2024-06-18 14:03:05 ERROR Connection timeout.",
        "2024-06-18 14:03:10 ERROR Redis unreachable.",
    ]
    for idx, (line, prefix, expected_error) in enumerate(zip(lines, expected_prefixes, expected_error_lines)):
        actual_error = line[len(prefix):]
        assert actual_error == expected_error, (
            f"Line {idx+1} of error_summary.log has incorrect error message.\n"
            f"Expected: '{expected_error}'\nActual:   '{actual_error}'"
        )

def test_no_extra_lines_in_error_summary():
    """
    Ensures there are no extra lines (blank or otherwise) at the end or between entries.
    """
    with open(ERROR_SUMMARY_LOG, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # All lines except possibly the last should end with \n
    for i, line in enumerate(lines[:-1]):
        assert line.endswith('\n'), (
            f"Line {i+1} of {ERROR_SUMMARY_LOG} does not end with a newline."
        )
    # The last line may or may not end with \n (POSIX does not require final newline)
    # Check that there are no blank lines
    stripped_lines = [l.rstrip('\n') for l in lines]
    assert all(l.strip() != "" for l in stripped_lines), (
        f"{ERROR_SUMMARY_LOG} contains blank lines, which is not allowed."
    )