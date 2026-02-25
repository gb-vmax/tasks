# test_final_state.py

import os
import pytest

LOGS_DIR = "/home/user/logs"
APP_LOG = os.path.join(LOGS_DIR, "app.log")
ERROR_LINES_LOG = os.path.join(LOGS_DIR, "error_lines.log")
IP_LINES_LOG = os.path.join(LOGS_DIR, "ip_lines.log")
SUMMARY_LOG = os.path.join(LOGS_DIR, "regex_summary.log")

EXPECTED_ERROR_LINES = [
    "ERROR Could not connect to database at 192.168.1.10:5432",
    "ERROR Failed to bind to 0.0.0.0:8080 - port in use",
    "ERROR Unexpected exception occurred",
    "ERROR Invalid input from user at 2001:0db8:85a3:0000:0000:8a2e:0370:7334",
]

EXPECTED_IP_LINES = [
    "ERROR Could not connect to database at 192.168.1.10:5432",
    "User 10.20.30.40 accessed the admin console",
    "ERROR Failed to bind to 0.0.0.0:8080 - port in use",
    "DEBUG Sent payload to 172.16.254.1 for user sync",
    "INFO Connection from 127.0.0.1 succeeded",
]

EXPECTED_SUMMARY = "error_lines.log: 4 lines\nip_lines.log: 5 lines\n"


def read_file_lines(path):
    """Read a file and return its lines with trailing newlines stripped."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip('\r\n') for line in f]


@pytest.mark.describe("Final state: Output log files exist with exactly correct content and summary.")
class TestFinalState:

    def test_error_lines_log_exists(self):
        assert os.path.isfile(ERROR_LINES_LOG), (
            f"Expected output file '{ERROR_LINES_LOG}' does not exist. "
            "You must create this file containing all log lines starting with 'ERROR'."
        )

    def test_error_lines_log_content(self):
        lines = read_file_lines(ERROR_LINES_LOG)
        assert lines == EXPECTED_ERROR_LINES, (
            f"The content of '{ERROR_LINES_LOG}' is incorrect.\n"
            f"Expected lines:\n{EXPECTED_ERROR_LINES}\n"
            f"Actual lines:\n{lines}\n"
            "Ensure it contains only and ALL log lines from '/home/user/logs/app.log' that start with 'ERROR', "
            "in the original order, with no extra or missing lines."
        )

    def test_ip_lines_log_exists(self):
        assert os.path.isfile(IP_LINES_LOG), (
            f"Expected output file '{IP_LINES_LOG}' does not exist. "
            "You must create this file containing all log lines with an IPv4 address."
        )

    def test_ip_lines_log_content(self):
        lines = read_file_lines(IP_LINES_LOG)
        assert lines == EXPECTED_IP_LINES, (
            f"The content of '{IP_LINES_LOG}' is incorrect.\n"
            f"Expected lines:\n{EXPECTED_IP_LINES}\n"
            f"Actual lines:\n{lines}\n"
            "Ensure it contains only and ALL log lines from '/home/user/logs/app.log' that contain an IPv4 address, "
            "in the original order, with no extra or missing lines."
        )

    def test_regex_summary_log_exists(self):
        assert os.path.isfile(SUMMARY_LOG), (
            f"Expected output summary file '{SUMMARY_LOG}' does not exist. "
            "You must create this file summarizing the number of lines in the other two output files."
        )

    def test_regex_summary_log_content(self):
        with open(SUMMARY_LOG, "r", encoding="utf-8") as f:
            content = f.read()
        # Normalize line endings for comparison
        actual = content.replace('\r\n', '\n')
        expected = EXPECTED_SUMMARY
        assert actual == expected, (
            f"The content of '{SUMMARY_LOG}' is incorrect.\n"
            f"Expected content:\n{repr(expected)}\n"
            f"Actual content:\n{repr(actual)}\n"
            "Ensure the summary format matches exactly, including spacing, punctuation, and newlines."
        )

    def test_no_extra_output_files(self):
        """Check that only the expected output files exist in the logs directory (no leftovers)."""
        expected_files = {
            "app.log",
            "error_lines.log",
            "ip_lines.log",
            "regex_summary.log",
        }
        actual_files = set(os.listdir(LOGS_DIR))
        extra = actual_files - expected_files
        missing = expected_files - actual_files
        assert not missing, (
            f"The following expected files are missing from '{LOGS_DIR}': {missing}."
        )
        assert not extra, (
            f"The following unexpected files are present in '{LOGS_DIR}': {extra}.\n"
            "Remove any extra files created during your task."
        )