# test_final_state.py

import os
import pytest

USERS_CSV_PATH = "/home/user/data/users.csv"
EMAILS_TXT_PATH = "/home/user/data/emails.txt"

EXPECTED_USERS_CSV_CONTENT = (
    "username,email,registration_date\n"
    "john_doe,john@example.com,2021-01-10\n"
    "jane_smith,jane.smith@example.net,2022-11-02\n"
    "bob,bob77@webmail.com,2023-03-15\n"
)

EXPECTED_EMAILS = [
    "john@example.com",
    "jane.smith@example.net",
    "bob77@webmail.com"
]

def test_data_directory_exists():
    data_dir = "/home/user/data"
    assert os.path.isdir(data_dir), (
        f"Required directory '{data_dir}' does not exist. "
        "The data directory must remain present after task completion."
    )

def test_users_csv_intact():
    assert os.path.isfile(USERS_CSV_PATH), (
        f"Input file '{USERS_CSV_PATH}' is missing after the task. "
        "Do not remove or rename the input CSV file."
    )
    with open(USERS_CSV_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_USERS_CSV_CONTENT, (
        f"The file '{USERS_CSV_PATH}' has been modified. "
        "Input CSV content must remain unchanged after the task.\n"
        "Expected content:\n"
        f"{EXPECTED_USERS_CSV_CONTENT!r}\n"
        "Actual content:\n"
        f"{content!r}"
    )

def test_emails_txt_exists():
    assert os.path.isfile(EMAILS_TXT_PATH), (
        f"Output file '{EMAILS_TXT_PATH}' does not exist. "
        "You must create this file with the extracted email addresses."
    )

def test_emails_txt_content():
    with open(EMAILS_TXT_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Strip only trailing newlines (not other whitespace) for robust check
    stripped_lines = [line.rstrip('\n') for line in lines]

    # Check for leading/trailing blank lines
    if stripped_lines and (stripped_lines[0] == '' or stripped_lines[-1] == ''):
        pytest.fail(
            f"'{EMAILS_TXT_PATH}' must not have leading or trailing blank lines."
        )

    # Check for number of lines
    assert len(stripped_lines) == len(EXPECTED_EMAILS), (
        f"'{EMAILS_TXT_PATH}' must contain exactly {len(EXPECTED_EMAILS)} lines "
        f"with one email address per line, but found {len(stripped_lines)} lines."
    )

    # Check for exact email match and no surrounding whitespace
    for i, (actual, expected) in enumerate(zip(stripped_lines, EXPECTED_EMAILS), start=1):
        if actual != expected:
            pytest.fail(
                f"Line {i} of '{EMAILS_TXT_PATH}' is incorrect.\n"
                f"Expected: {expected!r}\n"
                f"Found:    {actual!r}\n"
                "Ensure there is no extra whitespace and only the email address is present per line."
            )

    # Check for extra whitespace (should not exist)
    for i, line in enumerate(lines, start=1):
        if line != line.strip() + '\n' and line != line.strip():
            pytest.fail(
                f"Line {i} of '{EMAILS_TXT_PATH}' contains leading/trailing whitespace.\n"
                f"Offending line: {line!r}\n"
                "Each line must contain only the email address, with no extra spaces."
            )

    # Check for extra blank lines anywhere
    for i, line in enumerate(stripped_lines, start=1):
        if line == '':
            pytest.fail(
                f"Line {i} of '{EMAILS_TXT_PATH}' is blank. "
                "There must be no empty lines in the output file."
            )