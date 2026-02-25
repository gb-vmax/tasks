# test_final_state.py

import os
import stat
import pytest

LOGINS_LOG_PATH = "/home/user/backup/logins.log"
LOGIN_FREQUENCIES_PATH = "/home/user/backup/login_frequencies.txt"

EXPECTED_LOGINS_LOG_CONTENT = (
    "alice\n"
    "bob\n"
    "alice\n"
    "carol\n"
    "alice\n"
    "bob\n"
    "dan\n"
    "carol\n"
    "carol\n"
    "alice\n"
)

EXPECTED_LOGIN_FREQUENCIES_CONTENT = (
    "4 alice\n"
    "3 carol\n"
    "2 bob\n"
    "1 dan\n"
)

def test_backup_directory_exists():
    backup_dir = os.path.dirname(LOGINS_LOG_PATH)
    assert os.path.isdir(backup_dir), (
        f"Required directory '{backup_dir}' does not exist. "
        "Please ensure the backup directory is present."
    )

def test_logins_log_exists_and_is_file_and_unmodified():
    assert os.path.exists(LOGINS_LOG_PATH), (
        f"Required file '{LOGINS_LOG_PATH}' does not exist. "
        "It must remain present after the task."
    )
    assert os.path.isfile(LOGINS_LOG_PATH), (
        f"'{LOGINS_LOG_PATH}' exists but is not a regular file."
    )
    # Check content
    try:
        with open(LOGINS_LOG_PATH, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        pytest.fail(f"Could not read '{LOGINS_LOG_PATH}': {e}")
    assert content == EXPECTED_LOGINS_LOG_CONTENT, (
        f"The content of '{LOGINS_LOG_PATH}' was modified.\n"
        "Expected (should be unmodified):\n"
        f"{EXPECTED_LOGINS_LOG_CONTENT}\n"
        "Found:\n"
        f"{content}"
    )

def test_login_frequencies_txt_exists_and_is_file():
    assert os.path.exists(LOGIN_FREQUENCIES_PATH), (
        f"Output file '{LOGIN_FREQUENCIES_PATH}' does not exist. "
        "It must be created as output."
    )
    assert os.path.isfile(LOGIN_FREQUENCIES_PATH), (
        f"'{LOGIN_FREQUENCIES_PATH}' exists but is not a regular file."
    )

def test_login_frequencies_txt_content_exact():
    try:
        with open(LOGIN_FREQUENCIES_PATH, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        pytest.fail(f"Could not read '{LOGIN_FREQUENCIES_PATH}': {e}")

    # Check for exact match
    if content != EXPECTED_LOGIN_FREQUENCIES_CONTENT:
        # Provide helpful diagnostics
        exp_lines = EXPECTED_LOGIN_FREQUENCIES_CONTENT.splitlines(keepends=True)
        got_lines = content.splitlines(keepends=True)
        explanation = []
        explanation.append(
            f"The content of '{LOGIN_FREQUENCIES_PATH}' does not match the expected result."
        )
        explanation.append("Expected (exact, with newlines):")
        explanation.append(repr(EXPECTED_LOGIN_FREQUENCIES_CONTENT))
        explanation.append("Found:")
        explanation.append(repr(content))
        # Compare line by line for details
        for i, (exp, got) in enumerate(zip(exp_lines, got_lines), 1):
            if exp != got:
                explanation.append(
                    f"Line {i} mismatch:\n  Expected: {repr(exp)}\n  Got     : {repr(got)}"
                )
        if len(exp_lines) != len(got_lines):
            explanation.append(
                f"Expected {len(exp_lines)} lines, found {len(got_lines)} lines."
            )
        pytest.fail("\n".join(explanation))

def test_login_frequencies_txt_format_and_uniqueness():
    """
    Additional checks on output format:
    - Each line: <count> <user>
    - No blank lines, no trailing spaces, unique users, correct line count
    """
    lines = []
    try:
        with open(LOGIN_FREQUENCIES_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        pytest.fail(f"Could not read '{LOGIN_FREQUENCIES_PATH}': {e}")

    # Check for blank lines and trailing spaces
    for i, line in enumerate(lines, 1):
        assert line.strip() != "", (
            f"Blank line found at line {i} in '{LOGIN_FREQUENCIES_PATH}'. "
            "There should be no blank lines."
        )
        assert not line.endswith(" \n") and not line.endswith(" "), (
            f"Trailing spaces found at line {i} in '{LOGIN_FREQUENCIES_PATH}'. "
            "Lines must not have trailing spaces."
        )

    # Check format and uniqueness
    seen_users = set()
    for i, line in enumerate(lines, 1):
        if not line.endswith("\n"):
            pytest.fail(f"Line {i} does not end with a newline character.")
        line = line.rstrip("\n")
        parts = line.split(" ")
        assert len(parts) == 2, (
            f"Line {i} in '{LOGIN_FREQUENCIES_PATH}' is not in the format '<count> <user>':\n"
            f"  {repr(line)}"
        )
        count_str, user = parts
        assert count_str.isdigit(), (
            f"Line {i} in '{LOGIN_FREQUENCIES_PATH}' does not start with a number:\n"
            f"  {repr(line)}"
        )
        assert user not in seen_users, (
            f"Duplicate user '{user}' found in '{LOGIN_FREQUENCIES_PATH}' (line {i}). "
            "Each user must appear only once."
        )
        seen_users.add(user)

    # Check number of lines matches number of unique users in input
    input_users = set(EXPECTED_LOGINS_LOG_CONTENT.strip().split("\n"))
    assert len(lines) == len(input_users), (
        f"Expected {len(input_users)} unique users in the output, "
        f"but found {len(lines)} lines in '{LOGIN_FREQUENCIES_PATH}'."
    )

def test_login_frequencies_txt_sort_order():
    """
    Check that the lines are sorted by frequency desc, then user alphabetically.
    """
    try:
        with open(LOGIN_FREQUENCIES_PATH, "r", encoding="utf-8") as f:
            lines = [line.rstrip('\n') for line in f]
    except Exception as e:
        pytest.fail(f"Could not read '{LOGIN_FREQUENCIES_PATH}': {e}")

    entries = []
    for i, line in enumerate(lines, 1):
        parts = line.split(" ")
        if len(parts) != 2 or not parts[0].isdigit():
            pytest.fail(f"Line {i} is not in '<count> <user>' format: {repr(line)}")
        count = int(parts[0])
        user = parts[1]
        entries.append((count, user))

    # Check sort order: descending by count, then alpha by user
    for i in range(1, len(entries)):
        prev = entries[i-1]
        curr = entries[i]
        if curr[0] > prev[0]:
            pytest.fail(
                f"Line {i+1} ('{curr[0]} {curr[1]}') has a higher count than previous line "
                f"('{prev[0]} {prev[1]}'). Output should be sorted by count descending."
            )
        if curr[0] == prev[0] and curr[1] < prev[1]:
            pytest.fail(
                f"Line {i+1} ('{curr[0]} {curr[1]}') and line {i} ('{prev[0]} {prev[1]}') "
                "have the same count, but are not in alphabetical order by user."
            )