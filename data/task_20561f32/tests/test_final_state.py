# test_final_state.py

import os
import stat
import pytest

UTILS_DIR = "/home/user/utils"
SCRIPT_PATH = "/home/user/utils/word_freq.py"
SAMPLE_PATH = "/home/user/utils/sample.txt"
REPORT_PATH = "/home/user/utils/report.txt"

EXPECTED_REPORT_CONTENTS = (
    "and: 1\n"
    "at: 1\n"
    "away: 1\n"
    "barked: 1\n"
    "brown: 1\n"
    "dog: 2\n"
    "fox: 3\n"
    "jumps: 1\n"
    "lazy: 1\n"
    "over: 1\n"
    "quick: 1\n"
    "ran: 1\n"
    "the: 5\n"
    "\n"
    "total unique words: 13\n"
)


def test_utils_directory_exists():
    assert os.path.isdir(UTILS_DIR), (
        f"Directory {UTILS_DIR} does not exist. "
        "The utils directory should be present."
    )


def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), (
        f"Script {SCRIPT_PATH} does not exist. "
        "The word_freq.py script must be present."
    )


def test_script_is_executable():
    """The script must be executable (chmod +x) after the task."""
    mode = os.stat(SCRIPT_PATH).st_mode
    is_executable = bool(mode & stat.S_IXUSR)
    assert is_executable, (
        f"Script {SCRIPT_PATH} is NOT executable (mode {oct(stat.S_IMODE(mode))}). "
        "The task requires making it executable with chmod +x."
    )


def test_script_has_user_execute_bit():
    """Specifically check that the user execute bit (S_IXUSR) is set."""
    mode = os.stat(SCRIPT_PATH).st_mode
    perms = stat.S_IMODE(mode)
    assert perms & stat.S_IXUSR, (
        f"Script {SCRIPT_PATH} is missing the user execute bit. "
        f"Current permissions: {oct(perms)}. "
        "Run: chmod +x /home/user/utils/word_freq.py"
    )


def test_sample_file_exists():
    assert os.path.isfile(SAMPLE_PATH), (
        f"Sample file {SAMPLE_PATH} does not exist. "
        "The sample input file must be present."
    )


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file {REPORT_PATH} does not exist. "
        "The task requires running word_freq.py against sample.txt and "
        "redirecting output to report.txt. "
        "Run: /home/user/utils/word_freq.py /home/user/utils/sample.txt > /home/user/utils/report.txt"
    )


def test_report_file_is_not_empty():
    assert os.path.getsize(REPORT_PATH) > 0, (
        f"Report file {REPORT_PATH} exists but is empty. "
        "The report must contain the word frequency output from word_freq.py."
    )


def test_report_file_exact_contents():
    with open(REPORT_PATH, "r") as f:
        actual_contents = f.read()

    assert actual_contents == EXPECTED_REPORT_CONTENTS, (
        f"Report file {REPORT_PATH} does not have the expected contents.\n"
        f"Expected:\n{EXPECTED_REPORT_CONTENTS!r}\n"
        f"Actual:\n{actual_contents!r}\n"
        "Make sure you ran the script correctly: "
        "/home/user/utils/word_freq.py /home/user/utils/sample.txt > /home/user/utils/report.txt"
    )


def test_report_contains_word_frequencies():
    with open(REPORT_PATH, "r") as f:
        contents = f.read()

    expected_entries = [
        "and: 1",
        "at: 1",
        "away: 1",
        "barked: 1",
        "brown: 1",
        "dog: 2",
        "fox: 3",
        "jumps: 1",
        "lazy: 1",
        "over: 1",
        "quick: 1",
        "ran: 1",
        "the: 5",
    ]

    for entry in expected_entries:
        assert entry in contents, (
            f"Report file {REPORT_PATH} is missing expected entry: {entry!r}\n"
            f"Actual contents:\n{contents}"
        )


def test_report_contains_summary_line():
    with open(REPORT_PATH, "r") as f:
        contents = f.read()

    assert "total unique words: 13" in contents, (
        f"Report file {REPORT_PATH} is missing the summary line 'total unique words: 13'.\n"
        f"Actual contents:\n{contents}"
    )


def test_report_has_blank_line_before_summary():
    with open(REPORT_PATH, "r") as f:
        contents = f.read()

    assert "\n\ntotal unique words: 13\n" in contents, (
        f"Report file {REPORT_PATH} is missing the blank line before the summary.\n"
        "Expected a blank line between the last word entry and 'total unique words: 13'.\n"
        f"Actual contents:\n{contents!r}"
    )


def test_report_ends_with_newline():
    with open(REPORT_PATH, "r") as f:
        contents = f.read()

    assert contents.endswith("\n"), (
        f"Report file {REPORT_PATH} does not end with a newline character.\n"
        f"Last 20 characters: {contents[-20:]!r}"
    )


def test_report_lines_are_alphabetically_sorted():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    # Extract word frequency lines (before the blank line)
    word_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            break
        word_lines.append(stripped)

    words = [line.split(":")[0] for line in word_lines]
    assert words == sorted(words), (
        f"Words in report file {REPORT_PATH} are not sorted alphabetically.\n"
        f"Actual order: {words}\n"
        f"Expected order: {sorted(words)}"
    )


def test_report_word_count_is_correct():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    # Count word frequency lines (before the blank line)
    word_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            break
        word_lines.append(stripped)

    assert len(word_lines) == 13, (
        f"Report file {REPORT_PATH} contains {len(word_lines)} word entries, "
        f"expected 13.\n"
        f"Word lines found: {word_lines}"
    )