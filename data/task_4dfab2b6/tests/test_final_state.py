# test_final_state.py

import os
import pytest

DOTENV_PATH = "/home/user/db_backup/.env"
LOG_PATH = "/home/user/db_backup/backup_env_check.log"
TRUTH_LINES = [
    "PGUSER=db_backup_user",
    "PGPASSWORD=S3cr3tP@ssw0rd2024",
]


def read_file_exact_lines(path):
    """
    Reads a file and returns a list of lines, preserving exact line endings.
    """
    with open(path, 'r', newline='') as f:
        content = f.read()
    # Split into lines, keeping all line endings for precise checking
    # But we want to check for *no* trailing newline at EOF, so we splitlines(False)
    lines = content.split('\n')
    return lines, content


def assert_file_content_exact(path, expected_lines, file_description):
    """
    Asserts that the file at path contains exactly the expected lines,
    in order, with no extra whitespace, blank lines, or trailing newline at EOF.
    """
    lines, content = read_file_exact_lines(path)

    # Check for trailing newline at EOF
    if content.endswith('\n'):
        pytest.fail(
            f"{file_description} at '{path}' ends with a trailing newline. "
            "It must have no trailing newline at the end."
        )

    # There should be exactly len(expected_lines) lines
    if len(lines) != len(expected_lines):
        pytest.fail(
            f"{file_description} at '{path}' should contain exactly {len(expected_lines)} lines, "
            f"but it has {len(lines)}. Content:\n{repr(content)}"
        )

    # Check each line for exact match and no leading/trailing whitespace
    for idx, (actual, expected) in enumerate(zip(lines, expected_lines), start=1):
        if actual != expected:
            pytest.fail(
                f"{file_description} at '{path}' line {idx} is incorrect.\n"
                f"Expected: {repr(expected)}\n"
                f"Actual:   {repr(actual)}\n"
                "Lines must match exactly, with no extra whitespace."
            )


def test_dotenv_file_exists_with_correct_content():
    """
    The dotenv file /home/user/db_backup/.env must exist
    and contain exactly the two required lines, in order,
    with no extra whitespace or trailing newline.
    """
    assert os.path.exists(DOTENV_PATH), (
        f"Dotenv file '{DOTENV_PATH}' does not exist. "
        "You must create this file."
    )
    assert os.path.isfile(DOTENV_PATH), (
        f"'{DOTENV_PATH}' exists but is not a file."
    )

    assert_file_content_exact(
        DOTENV_PATH,
        TRUTH_LINES,
        "Dotenv file"
    )


def test_env_variables_set_correctly(monkeypatch):
    """
    The environment variables PGUSER and PGPASSWORD must be set in the
    agent's shell session with the correct values.
    """
    # These values must be set in the environment at test time
    pguser = os.environ.get("PGUSER")
    pgpassword = os.environ.get("PGPASSWORD")
    assert pguser == "db_backup_user", (
        "Environment variable PGUSER is not set correctly.\n"
        f"Expected: 'db_backup_user'\nActual:   {repr(pguser)}\n"
        "Did you load the dotenv file into your shell session?"
    )
    assert pgpassword == "S3cr3tP@ssw0rd2024", (
        "Environment variable PGPASSWORD is not set correctly.\n"
        f"Expected: 'S3cr3tP@ssw0rd2024'\nActual:   {repr(pgpassword)}\n"
        "Did you load the dotenv file into your shell session?"
    )


def test_log_file_exists_and_correct():
    """
    The log file /home/user/db_backup/backup_env_check.log must exist,
    and contain exactly the two required lines, in order,
    with no extra whitespace or trailing newline.
    """
    assert os.path.exists(LOG_PATH), (
        f"Log file '{LOG_PATH}' does not exist. "
        "You must create this file as the final step."
    )
    assert os.path.isfile(LOG_PATH), (
        f"'{LOG_PATH}' exists but is not a file."
    )

    assert_file_content_exact(
        LOG_PATH,
        TRUTH_LINES,
        "Log file"
    )