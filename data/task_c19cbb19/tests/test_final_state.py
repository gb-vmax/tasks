# test_final_state.py

import os
import pytest

SUMMARY_PATH = "/home/user/storage/threshold_summary.txt"

@pytest.mark.describe("Final OS state after student action")
class TestFinalState:

    def test_threshold_summary_file_exists(self):
        assert os.path.isfile(SUMMARY_PATH), (
            f"The summary file '{SUMMARY_PATH}' does not exist. "
            "You must create this file as specified in the task."
        )

    def test_threshold_summary_contents_exact(self):
        expected_lines = [
            "/data1: 80G",
            "/backup: 120G",
        ]
        try:
            with open(SUMMARY_PATH, "r") as f:
                contents = f.read().replace("\r\n", "\n").replace("\r", "\n")
        except Exception as e:
            pytest.fail(f"Could not read '{SUMMARY_PATH}': {e}")

        # Remove leading/trailing whitespace and split into lines
        actual_lines = [line.rstrip('\n').rstrip('\r') for line in contents.splitlines()]
        assert actual_lines == expected_lines, (
            f"The contents of '{SUMMARY_PATH}' do not match the expected format or values.\n"
            f"Expected lines (in order):\n{expected_lines}\n\n"
            f"Actual lines:\n{actual_lines}\n"
            "Check that:\n"
            "- Only the two specified lines are present, in the correct order.\n"
            "- There are no extra blank lines or whitespace.\n"
            "- The thresholds match those from the config file."
        )

    def test_threshold_summary_no_extra_content(self):
        """
        Ensure there are exactly two lines, and no extra whitespace or blank lines.
        """
        with open(SUMMARY_PATH, "rb") as f:
            raw = f.read()

        # Check for any trailing newlines beyond the end of the second line
        # There should be exactly one \n after the first line, and either none or one after the second (text files may or may not end with \n)
        # So: Accept either (b"/data1: 80G\n/backup: 120G") or (b"/data1: 80G\n/backup: 120G\n")
        expected1 = b"/data1: 80G\n/backup: 120G"
        expected2 = b"/data1: 80G\n/backup: 120G\n"
        assert raw == expected1 or raw == expected2, (
            f"The summary file '{SUMMARY_PATH}' contains extra content, whitespace, or lines.\n"
            f"Expected file bytes:\n{expected1!r} or {expected2!r}\n\n"
            f"Actual file bytes:\n{raw!r}\n"
            "Ensure there are no extra blank lines, spaces, or content in the file."
        )