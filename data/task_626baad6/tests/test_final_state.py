# test_final_state.py

import os
import stat
import pytest

TRAINING_TEXT_PATH = "/home/user/data/training_text.txt"
REPORT_PATH = "/home/user/data/word_frequency_report.txt"
DATA_DIR = "/home/user/data"

EXPECTED_REPORT_LINES = [
    "1 bird\n",
    "2 cat\n",
    "1 dog\n"
]

@pytest.mark.describe("Final state validation for word frequency report task")
class TestFinalState:

    def test_data_directory_still_exists(self):
        assert os.path.isdir(DATA_DIR), (
            f"Directory '{DATA_DIR}' is missing after task completion. "
            "It must not be removed."
        )

    def test_training_text_file_still_exists(self):
        assert os.path.isfile(TRAINING_TEXT_PATH), (
            f"Original training file '{TRAINING_TEXT_PATH}' is missing after task completion. "
            "Do not delete or move the input file."
        )

    def test_training_text_file_permissions(self):
        st = os.stat(TRAINING_TEXT_PATH)
        assert bool(st.st_mode & stat.S_IRUSR), (
            f"File '{TRAINING_TEXT_PATH}' is not readable by the user after task completion."
        )
        assert bool(st.st_mode & stat.S_IWUSR), (
            f"File '{TRAINING_TEXT_PATH}' is not writable by the user after task completion."
        )

    def test_data_directory_permissions(self):
        st = os.stat(DATA_DIR)
        assert bool(st.st_mode & stat.S_IRUSR), (
            f"Directory '{DATA_DIR}' is not readable by the user after task completion."
        )
        assert bool(st.st_mode & stat.S_IWUSR), (
            f"Directory '{DATA_DIR}' is not writable by the user after task completion."
        )

    def test_training_text_file_contents_unchanged(self):
        expected_lines = ["cat\n", "dog\n", "cat\n", "bird\n"]
        with open(TRAINING_TEXT_PATH, "r", encoding="utf-8") as f:
            contents = f.readlines()
        assert contents == expected_lines, (
            f"Contents of '{TRAINING_TEXT_PATH}' have changed after task completion.\n"
            f"Expected: {repr(expected_lines)}\n"
            f"Found: {repr(contents)}\n"
            "You must not modify the original input file."
        )

    def test_report_file_exists(self):
        assert os.path.isfile(REPORT_PATH), (
            f"Report file '{REPORT_PATH}' was not created."
        )

    def test_report_file_permissions(self):
        st = os.stat(REPORT_PATH)
        assert bool(st.st_mode & stat.S_IRUSR), (
            f"File '{REPORT_PATH}' is not readable by the user."
        )
        assert bool(st.st_mode & stat.S_IWUSR), (
            f"File '{REPORT_PATH}' is not writable by the user."
        )

    def test_report_file_contents_exact(self):
        with open(REPORT_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        assert lines == EXPECTED_REPORT_LINES, (
            f"Report file '{REPORT_PATH}' contents are incorrect.\n"
            "Expected lines (order and format must match exactly):\n"
            f"{''.join(EXPECTED_REPORT_LINES)}\n"
            "Found lines:\n"
            f"{''.join(lines)}\n"
            "Check that:\n"
            "- Each line is in 'frequency_count word' format, exactly one space between number and word\n"
            "- Words are sorted lexicographically\n"
            "- Each line ends with a single newline '\\n', and there are no blank lines or trailing newlines after the last word\n"
            "- Frequencies are correct for each word"
        )

    def test_report_file_no_extra_blank_lines(self):
        with open(REPORT_PATH, "rb") as f:
            content = f.read()
        if not content:
            pytest.fail(
                f"Report file '{REPORT_PATH}' is empty. It must contain the word frequencies."
            )
        # Check that the file does not end with a blank line (i.e., no extra newlines at the end)
        if content.endswith(b"\n\n"):
            pytest.fail(
                f"Report file '{REPORT_PATH}' has extra blank lines at the end. "
                "There must be no blank lines or extra newlines after the last word."
            )

    def test_report_file_no_leading_trailing_whitespace(self):
        with open(REPORT_PATH, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                if line != line.strip() + '\n':
                    pytest.fail(
                        f"Line {i} of '{REPORT_PATH}' has leading or trailing whitespace: {repr(line)}. "
                        "Each line must be in the format 'frequency_count word' with no extra spaces."
                    )