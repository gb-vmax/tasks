# test_final_state.py

import os
import re
import pytest

REPORT_FILE = "/home/user/resource_usage_report.txt"

DATETIME_EDT_REGEX = (
    r"^\d{4}-\d{2}-\d{2} "         # YYYY-MM-DD
    r"\d{2}:\d{2}:\d{2} "          # HH:MM:SS
    r"EDT$"                        # EDT timezone abbreviation, must be at end
)

def read_report_file():
    """
    Reads the report file and returns its lines as a list (without newlines).
    """
    if not os.path.exists(REPORT_FILE):
        pytest.fail(
            f"The report file '{REPORT_FILE}' does not exist. "
            "You must create it at the specified absolute path."
        )
    with open(REPORT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Remove trailing newlines from each line
    lines = [line.rstrip('\n') for line in lines]
    return lines

def test_report_file_exists():
    """
    The report file must exist at the specified absolute path.
    """
    assert os.path.isfile(REPORT_FILE), (
        f"The report file '{REPORT_FILE}' was not found. "
        "It must exist at the specified absolute path."
    )

def test_report_file_is_single_line():
    """
    The report file must contain exactly one line (no blank or extra lines).
    """
    lines = read_report_file()
    assert len(lines) == 1, (
        f"The report file '{REPORT_FILE}' must contain exactly one line, "
        f"but found {len(lines)} lines."
    )

def test_report_file_content_format_and_timezone():
    """
    The report file must contain the current date and time in the format:
    YYYY-MM-DD HH:MM:SS EDT
    - The timezone abbreviation must be 'EDT'.
    - There must be no leading/trailing whitespace.
    - The line must match the strict format.
    """
    lines = read_report_file()
    content = lines[0]

    # Check for leading/trailing whitespace
    assert content == content.strip(), (
        f"The report file line must not have leading or trailing whitespace: '{content}'"
    )

    # Check strict format and that EDT is present at the end
    if not re.match(DATETIME_EDT_REGEX, content):
        pytest.fail(
            f"The report file line does not match the required format.\n"
            "Expected format: YYYY-MM-DD HH:MM:SS EDT\n"
            f"Actual content: '{content}'\n"
            "Make sure you use the TZ environment variable set to 'America/New_York' "
            "and print the date using the 'date' command in the exact format."
        )

def test_report_file_no_extra_content():
    """
    The report file must not contain any extra content (no blank lines, headers, or footers).
    """
    with open(REPORT_FILE, 'rb') as f:
        data = f.read()
    # The file should end with a single newline or no newline (POSIX allows last line without newline)
    # But since we splitlines in read_report_file, check that no extra data follows the line
    lines = data.splitlines()
    assert len(lines) == 1, (
        f"The report file '{REPORT_FILE}' must contain exactly one non-empty line."
    )