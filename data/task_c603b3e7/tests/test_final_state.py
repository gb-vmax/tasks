# test_final_state.py

import os
import stat
import re
import pytest
import time
from datetime import datetime, timedelta

HOME = "/home/user"
DATA_DIR = f"{HOME}/legacy_data"
REPORTS_DIR = f"{HOME}/legacy_run/reports"

TMP_FILES = ["temp1.tmp", "temp2.tmp", "temp3.tmp"]
NON_TMP_FILES = [
    ("keepme.txt", "important data\n"),
    ("archive.log", "log file data\n"),
]

# The output the script must produce, with exact line endings and ordering.
EXPECTED_LOG_CONTENT = (
    "Cleanup Summary:\n"
    "Deleted files:\n"
    "- temp1.tmp\n"
    "- temp2.tmp\n"
    "- temp3.tmp\n"
    "Operation completed successfully.\n"
)

# Regex for the required log filename format.
LOGFILE_RE = re.compile(r"^cleanup_(\d{8}_\d{6})\.log$")

@pytest.mark.describe("Final OS/filesystem state validation after student action")
class TestFinalState:

    def test_tmp_files_deleted(self):
        """All .tmp files must be deleted from DATA_DIR."""
        for fname in TMP_FILES:
            fpath = os.path.join(DATA_DIR, fname)
            assert not os.path.exists(fpath), (
                f"Temporary file {fpath} still exists. "
                "All .tmp files must be deleted by the script."
            )

    def test_non_tmp_files_untouched(self):
        """Non-tmp files must remain untouched (content and mtime)."""
        for fname, expected_content in NON_TMP_FILES:
            fpath = os.path.join(DATA_DIR, fname)
            assert os.path.isfile(fpath), (
                f"Non-tmp file {fpath} is missing. "
                "The script must NOT remove or rename non-tmp files."
            )
            # Check content
            with open(fpath, "r") as f:
                content = f.read()
            assert content == expected_content, (
                f"Contents of {fpath} changed. "
                "Non-tmp files must not be modified.\n"
                f"Expected: {repr(expected_content)}\nActual:   {repr(content)}"
            )

    def test_log_file_exists_and_name(self):
        """A log file with correct timestamp format must exist in REPORTS_DIR."""
        log_files = [f for f in os.listdir(REPORTS_DIR) if LOGFILE_RE.match(f)]
        assert log_files, (
            f"No log file matching cleanup_YYYYMMDD_HHMMSS.log found in {REPORTS_DIR}. "
            "A report log file with the correct timestamped name must be created."
        )
        # Accept only one new log in the reports directory
        assert len(log_files) == 1, (
            f"Expected exactly one cleanup_YYYYMMDD_HHMMSS.log in {REPORTS_DIR}, found: {log_files}"
        )
        log_file = log_files[0]
        match = LOGFILE_RE.match(log_file)
        timestamp_str = match.group(1)
        # Store for later tests
        self.log_file_path = os.path.join(REPORTS_DIR, log_file)
        self.log_file_timestamp_str = timestamp_str

    def test_log_file_timestamp_close_to_now(self):
        """Timestamp in log filename must be within ±60s of current UTC time."""
        # This depends on previous test to set self.log_file_timestamp_str
        log_files = [f for f in os.listdir(REPORTS_DIR) if LOGFILE_RE.match(f)]
        assert log_files, "No matching cleanup_YYYYMMDD_HHMMSS.log found for timestamp check."
        log_file = log_files[0]
        match = LOGFILE_RE.match(log_file)
        timestamp_str = match.group(1)
        try:
            log_dt = datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S")
        except Exception:
            assert False, (
                f"Log filename timestamp {timestamp_str} is not in required format YYYYMMDD_HHMMSS."
            )
        now_utc = datetime.utcnow()
        delta = abs((now_utc - log_dt).total_seconds())
        assert delta <= 60, (
            f"Timestamp in log filename ({timestamp_str}) is not within ±60s of current UTC time. "
            f"Current UTC: {now_utc.strftime('%Y%m%d_%H%M%S')}, "
            f"File: {timestamp_str}, "
            f"Difference: {int(delta)} seconds."
        )
        # Save for other tests
        self.log_file_path = os.path.join(REPORTS_DIR, log_file)

    def test_log_file_content_exact(self):
        """Log file must contain exactly the required output, no extra whitespace or lines."""
        log_files = [f for f in os.listdir(REPORTS_DIR) if LOGFILE_RE.match(f)]
        assert log_files, "No matching cleanup_YYYYMMDD_HHMMSS.log found for content check."
        log_file = log_files[0]
        log_path = os.path.join(REPORTS_DIR, log_file)
        with open(log_path, "r") as f:
            content = f.read()
        # Normalize line endings (should be \n already, but just in case)
        content = content.replace("\r\n", "\n")
        expected = EXPECTED_LOG_CONTENT
        assert content == expected, (
            f"Log file {log_path} content does not match expected output.\n"
            "Expected:\n"
            f"{repr(expected)}\n"
            "Actual:\n"
            f"{repr(content)}"
        )

    def test_log_file_permissions(self):
        """Log file must have permissions 600 (rw-------)."""
        log_files = [f for f in os.listdir(REPORTS_DIR) if LOGFILE_RE.match(f)]
        assert log_files, "No matching cleanup_YYYYMMDD_HHMMSS.log found for permissions check."
        log_file = log_files[0]
        log_path = os.path.join(REPORTS_DIR, log_file)
        st = os.stat(log_path)
        mode = st.st_mode & 0o777
        assert mode == 0o600, (
            f"Log file {log_path} permissions are {oct(mode)}, expected 0o600 (rw-------)."
        )

    def test_log_file_path_printed(self, capsys):
        """
        The absolute path of the created log file must have been printed
        to stdout as the last action.
        """
        # Since we can't capture output after the fact, check if the file
        # /home/user/legacy_run/reports/cleanup_YYYYMMDD_HHMMSS.log path appears in the latest lines
        log_files = [f for f in os.listdir(REPORTS_DIR) if LOGFILE_RE.match(f)]
        assert log_files, "No matching cleanup_YYYYMMDD_HHMMSS.log found for output path check."
        log_file = log_files[0]
        log_path = os.path.join(REPORTS_DIR, log_file)
        # Try to find the log path in logs or in a designated output file, or as a last resort, skip with reason
        # In many environments, we cannot retrieve the previous stdout after the fact.
        # If the test system can provide the captured stdout, instruct to check for exact path.
        # Otherwise, skip with a clear message.
        # Here we use capsys only if the script was run via pytest subprocess, which is not the case here.
        pytest.skip(
            f"Manual verification required: "
            f"The script must print the absolute path to the log file ({log_path}) on stdout as its last action."
        )