# test_final_state.py

import os
import pytest

APP_PROFILE_CSV = "/home/user/app_profile.csv"
PROFILE_SUMMARY_CSV = "/home/user/profile_summary.csv"

EXPECTED_APP_PROFILE_CONTENT = (
    "ProcessID,Process,User,Threads,CPU%,MemoryMB\n"
    "1023,chrome,alice,14,32.5,450\n"
    "1057,firefox,bob,8,42.1,305\n"
    "1092,code,carol,10,15.7,210\n"
    "1107,slack,dan,6,21.0,190\n"
)

EXPECTED_PROFILE_SUMMARY_CONTENT = (
    "Process,CPU%\n"
    "chrome,32.5\n"
    "firefox,42.1\n"
    "code,15.7\n"
    "slack,21.0\n"
)

@pytest.mark.describe("Final OS/filesystem state after app profiling extraction task")
class TestFinalState:
    def test_app_profile_csv_untouched(self):
        """Check that the input CSV file still exists and is unmodified."""
        assert os.path.isfile(APP_PROFILE_CSV), (
            f"Required input file '{APP_PROFILE_CSV}' is missing after task completion. "
            "You must not remove or modify the original input file."
        )
        with open(APP_PROFILE_CSV, "rb") as f:
            content_bytes = f.read()
        try:
            content = content_bytes.decode("utf-8")
        except UnicodeDecodeError:
            pytest.fail(
                f"File '{APP_PROFILE_CSV}' is not valid UTF-8 text after task completion. "
                "You must not alter the encoding of the input file."
            )
        assert content == EXPECTED_APP_PROFILE_CONTENT, (
            f"File '{APP_PROFILE_CSV}' was modified during the task.\n"
            "Expected:\n"
            f"{EXPECTED_APP_PROFILE_CONTENT!r}\n"
            "Actual:\n"
            f"{content!r}\n"
            "You must not change the input file in any way."
        )

    def test_profile_summary_csv_exists(self):
        """Check that the output CSV file was created."""
        assert os.path.isfile(PROFILE_SUMMARY_CSV), (
            f"Output file '{PROFILE_SUMMARY_CSV}' is missing after task completion. "
            "You must create this file as part of the task."
        )

    def test_profile_summary_csv_content(self):
        """Check that the output CSV file has exactly the expected content and format."""
        with open(PROFILE_SUMMARY_CSV, "rb") as f:
            content_bytes = f.read()
        try:
            content = content_bytes.decode("utf-8")
        except UnicodeDecodeError:
            pytest.fail(
                f"File '{PROFILE_SUMMARY_CSV}' is not valid UTF-8 text. "
                "The output must be a plain text CSV file."
            )

        # Check for presence of carriage returns (CR) or CRLF line endings
        if "\r" in content:
            pytest.fail(
                f"File '{PROFILE_SUMMARY_CSV}' contains carriage return (CR) characters or CRLF line endings. "
                "Line endings must be UNIX style (LF only, '\\n')."
            )

        # Check for trailing whitespace on any line
        lines = content.split('\n')
        for idx, line in enumerate(lines):
            # Last line may be empty after split if file ends with \n
            if line != '' and (line.endswith(' ') or line.endswith('\t')):
                pytest.fail(
                    f"Line {idx+1} of '{PROFILE_SUMMARY_CSV}' has trailing whitespace. "
                    "All fields and lines must be trimmed, with no extra spaces."
                )

        # Check for extra spaces around comma
        for idx, line in enumerate(lines):
            if ',' in line and (', ' in line or ' ,' in line):
                pytest.fail(
                    f"Line {idx+1} of '{PROFILE_SUMMARY_CSV}' contains extra whitespace around comma. "
                    "All columns must be comma-separated with no surrounding spaces."
                )

        # Check for correct content and order
        assert content == EXPECTED_PROFILE_SUMMARY_CONTENT, (
            f"File '{PROFILE_SUMMARY_CSV}' does not have the expected content and format.\n"
            "Expected:\n"
            f"{EXPECTED_PROFILE_SUMMARY_CONTENT!r}\n"
            "Actual:\n"
            f"{content!r}\n"
            "Please ensure the file matches exactly, including header, column order, values, and UNIX line endings."
        )

    def test_profile_summary_csv_no_extra_lines(self):
        """Check there are no extra blank lines at the end of the output file."""
        with open(PROFILE_SUMMARY_CSV, "rb") as f:
            content_bytes = f.read()
        content = content_bytes.decode("utf-8")
        # The expected content ends with a single '\n', so the last line after split is empty
        lines = content.split('\n')
        # Remove the last empty line after split if present
        if lines and lines[-1] == '':
            lines = lines[:-1]
        # There should be exactly 5 lines: header + 4 data rows
        assert len(lines) == 5, (
            f"File '{PROFILE_SUMMARY_CSV}' has an unexpected number of lines. "
            f"Expected 5 (header + 4 rows), got {len(lines)}. "
            "Please ensure there are no extra blank lines at the end."
        )