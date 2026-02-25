# test_final_state.py

import os
import pytest

INI_PATH = "/home/user/artifact_manager/repos.ini"
LOG_PATH = "/home/user/artifact_manager/enabled_repos.log"

EXPECTED_INI_CONTENT = (
    "[core]\n"
    "base_url = https://artifacts.example.org/core\n"
    "enabled = yes\n\n"
    "[testing]\n"
    "base_url = https://artifacts.example.org/testing\n"
    "enabled = no\n\n"
    "[extra]\n"
    "base_url = https://artifacts.example.org/extra\n"
    "enabled = yes\n\n"
    "[legacy]\n"
    "base_url = https://artifacts.example.org/legacy\n"
    "enabled = no\n"
)

EXPECTED_LOG_CONTENT = (
    "core: https://artifacts.example.org/core\n"
    "extra: https://artifacts.example.org/extra\n"
)

def test_repos_ini_still_exists():
    assert os.path.isfile(INI_PATH), (
        f"Expected {INI_PATH} to exist after task completion, but it does not. "
        "Do not remove or rename the original INI file."
    )

def test_repos_ini_unchanged():
    with open(INI_PATH, encoding="utf-8") as f:
        actual = f.read()
    actual_n = actual.replace("\r\n", "\n").strip()
    expected_n = EXPECTED_INI_CONTENT.strip()
    assert actual_n == expected_n, (
        f"The content of {INI_PATH} has changed after the task was completed.\n"
        "You must NOT modify this file. Restore it to its original state.\n"
        "Expected content:\n"
        f"{EXPECTED_INI_CONTENT}\n"
        "Actual content:\n"
        f"{actual}\n"
    )

def test_enabled_repos_log_exists():
    assert os.path.isfile(LOG_PATH), (
        f"The output file {LOG_PATH} does not exist after task completion.\n"
        "You must create this file with the enabled repositories."
    )

def test_enabled_repos_log_content_exact():
    with open(LOG_PATH, encoding="utf-8") as f:
        actual = f.read()
    actual_n = actual.replace("\r\n", "\n")
    expected_n = EXPECTED_LOG_CONTENT
    assert actual_n == expected_n, (
        f"The content of {LOG_PATH} is not exactly as required.\n"
        "Expected content:\n"
        f"{EXPECTED_LOG_CONTENT}\n"
        "Actual content:\n"
        f"{actual}\n"
        "Make sure:\n"
        "- Only enabled repositories are listed\n"
        "- The format is <repo>: <url> exactly, with no extra whitespace\n"
        "- The order matches the INI file\n"
        "- No blank lines or extra lines are present"
    )

def test_enabled_repos_log_no_extra_lines():
    """Ensure there are no extra blank lines or repositories in the log file."""
    with open(LOG_PATH, encoding="utf-8") as f:
        lines = f.read().replace("\r\n", "\n").split("\n")
    # Remove final empty string if file ends with \n
    if lines and lines[-1] == '':
        lines.pop()
    expected_lines = [
        "core: https://artifacts.example.org/core",
        "extra: https://artifacts.example.org/extra",
    ]
    assert lines == expected_lines, (
        f"{LOG_PATH} contains unexpected lines or formatting.\n"
        f"Expected lines:\n{expected_lines}\n"
        f"Actual lines:\n{lines}\n"
        "Check for blank lines, extra whitespace, or extra repositories."
    )