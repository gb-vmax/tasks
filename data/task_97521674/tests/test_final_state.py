# test_final_state.py
"""
Pytest suite to validate the FINAL state of the translation log filtering task.

Checks:
- /home/user/projects/translation_logs/filtered_update_20240612.log exists
- Its contents match the expected filtered entries and summary line exactly
- The original update_20240612.log is unaltered
- The number of filtered entries in the file and summary is exactly 7
"""

import os
import pytest

LOG_DIR = "/home/user/projects/translation_logs"
LOG_FILE = os.path.join(LOG_DIR, "update_20240612.log")
FILTERED_FILE = os.path.join(LOG_DIR, "filtered_update_20240612.log")

EXPECTED_FILTERED_CONTENT = (
    "2024-06-12 09:32:18 | locale:fr | key:homepage.header.title | status:updated | details:Translation updated for new campaign\n"
    "2024-06-12 09:35:02 | locale:de | key:account.email.body | status:failed | details:Plural form missing\n"
    "2024-06-12 10:02:11 | locale:fr | key:homepage.header.subtitle | status:failed | details:Missing variable in string\n"
    "2024-06-12 10:18:50 | locale:de | key:homepage.header.title | status:updated | details:Minor spelling correction\n"
    "2024-06-12 10:23:15 | locale:fr | key:settings.privacy | status:failed | details:Formatting tags invalid\n"
    "2024-06-12 10:31:55 | locale:de | key:footer.contact | status:updated | details:Formality level checked\n"
    "2024-06-12 11:04:22 | locale:fr | key:dashboard.welcome | status:failed | details:Variable mismatch\n"
    "SUMMARY: 7 entries matching (locale: fr|de, status: failed|updated)\n"
)

EXPECTED_LOG_CONTENT = (
    "2024-06-12 09:32:18 | locale:fr | key:homepage.header.title | status:updated | details:Translation updated for new campaign\n"
    "2024-06-12 09:32:18 | locale:es | key:homepage.header.title | status:added | details:New translation provided\n"
    "2024-06-12 09:35:02 | locale:de | key:account.email.body | status:failed | details:Plural form missing\n"
    "2024-06-12 09:36:44 | locale:fr | key:footer.contact | status:added | details:Contact info added\n"
    "2024-06-12 09:38:12 | locale:it | key:footer.contact | status:updated | details:Grammar fixed\n"
    "2024-06-12 10:02:11 | locale:fr | key:homepage.header.subtitle | status:failed | details:Missing variable in string\n"
    "2024-06-12 10:18:50 | locale:de | key:homepage.header.title | status:updated | details:Minor spelling correction\n"
    "2024-06-12 10:21:53 | locale:es | key:settings.privacy | status:updated | details:Translation improved\n"
    "2024-06-12 10:23:15 | locale:fr | key:settings.privacy | status:failed | details:Formatting tags invalid\n"
    "2024-06-12 10:25:22 | locale:pt | key:homepage.header.subtitle | status:added | details:New addition for PT\n"
    "2024-06-12 10:31:55 | locale:de | key:footer.contact | status:updated | details:Formality level checked\n"
    "2024-06-12 11:04:22 | locale:fr | key:dashboard.welcome | status:failed | details:Variable mismatch\n"
)

@pytest.mark.describe("Final OS/filesystem state after translation log filtering task")
class TestFinalState:

    def test_log_dir_still_exists(self):
        assert os.path.isdir(LOG_DIR), (
            f"Directory {LOG_DIR} is missing after task completion. "
            "It must not be removed."
        )

    def test_original_log_untouched(self):
        assert os.path.isfile(LOG_FILE), (
            f"Original log file {LOG_FILE} is missing after the task. "
            "Do not delete or move the original file."
        )
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            actual = f.read().rstrip('\n')
        expected = EXPECTED_LOG_CONTENT.rstrip('\n')
        assert actual == expected, (
            f"The contents of {LOG_FILE} have changed after the task. "
            "Do not modify the original log file.\n"
            f"Expected contents:\n{EXPECTED_LOG_CONTENT}"
        )

    def test_filtered_log_exists(self):
        assert os.path.isfile(FILTERED_FILE), (
            f"Filtered log file {FILTERED_FILE} does not exist. "
            "You must create this file with the filtered entries."
        )

    def test_filtered_log_contents_exact(self):
        with open(FILTERED_FILE, "r", encoding="utf-8") as f:
            actual = f.read()
        expected = EXPECTED_FILTERED_CONTENT
        # Compare exact content including newlines
        assert actual == expected, (
            f"The contents of {FILTERED_FILE} do not match the expected filtered output.\n"
            "Check that you have filtered the correct lines, preserved their order, "
            "and appended the summary in the exact required format.\n\n"
            f"Expected:\n{EXPECTED_FILTERED_CONTENT}\n\n"
            f"Actual:\n{actual}"
        )

    def test_filtered_log_entry_count_and_summary(self):
        with open(FILTERED_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # The summary is the last line
        assert lines, (
            f"{FILTERED_FILE} is empty. It must contain the filtered entries and a summary line."
        )
        summary_line = lines[-1].rstrip('\n')
        expected_summary = "SUMMARY: 7 entries matching (locale: fr|de, status: failed|updated)"
        assert summary_line == expected_summary, (
            f"The summary line at the end of {FILTERED_FILE} is incorrect.\n"
            f"Expected:\n{expected_summary}\n"
            f"Actual:\n{summary_line}"
        )
        # The number of filtered entries (excluding the summary) should be 7
        filtered_entries = lines[:-1]
        assert len(filtered_entries) == 7, (
            f"There should be exactly 7 filtered entries before the summary in {FILTERED_FILE}, "
            f"but found {len(filtered_entries)}."
        )

    def test_filtered_log_no_extra_lines(self):
        with open(FILTERED_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Check for trailing blank lines
        if lines:
            assert lines[-1].strip() != "", (
                f"{FILTERED_FILE} has a blank line at the end. "
                "The last line must be the summary, with no trailing blank lines."
            )
            # No extra blank lines between entries
            for i, line in enumerate(lines[:-1], 1):
                assert line.strip() != "", (
                    f"{FILTERED_FILE} has a blank line at line {i}. "
                    "There should be no blank lines between entries."
                )