# test_final_state.py

import os
import pytest

SECURITY_DIR = "/home/user/security"
API_CREDENTIALS_PATH = os.path.join(SECURITY_DIR, "api_credentials.csv")
ROTATION_LOG_PATH = os.path.join(SECURITY_DIR, "rotation_log.txt")

EXPECTED_CREDENTIALS = (
    "username,apikey\n"
    "alice,NEW_SECURE_API_KEY_8901\n"
    "bob,BOB_API_KEY_555\n"
    "carol,CAROL_KEY_6789\n"
)

EXPECTED_LOG_LINE = "alice's API key rotated to NEW_SECURE_API_KEY_8901\n"

def test_security_directory_exists():
    assert os.path.isdir(SECURITY_DIR), (
        f"Directory '{SECURITY_DIR}' does not exist. "
        f"The required security directory must be present after task completion."
    )

def test_api_credentials_file_exists():
    assert os.path.isfile(API_CREDENTIALS_PATH), (
        f"File '{API_CREDENTIALS_PATH}' does not exist. "
        f"The credentials file must exist after the API key rotation."
    )

def test_api_credentials_file_content():
    with open(API_CREDENTIALS_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_CREDENTIALS, (
        f"The credentials file '{API_CREDENTIALS_PATH}' does not have the expected content after rotation.\n"
        f"Expected:\n{EXPECTED_CREDENTIALS!r}\n\n"
        f"Found:\n{content!r}\n"
        "Make sure only alice's API key is replaced, all other data is unchanged, and the file format matches exactly."
    )

def test_rotation_log_exists():
    assert os.path.isfile(ROTATION_LOG_PATH), (
        f"Rotation log '{ROTATION_LOG_PATH}' does not exist. "
        f"You must create this log file after rotating the API key."
    )

def test_rotation_log_content():
    with open(ROTATION_LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) == 1, (
        f"The log file '{ROTATION_LOG_PATH}' should contain exactly one line, but it has {len(lines)} lines.\n"
        f"Log file content:\n{''.join(lines)!r}"
    )
    assert lines[0] == EXPECTED_LOG_LINE, (
        f"The log file '{ROTATION_LOG_PATH}' does not have the expected content.\n"
        f"Expected line:\n{EXPECTED_LOG_LINE!r}\n"
        f"Found line:\n{lines[0]!r}\n"
        "Ensure you use the exact required text, no extra spaces or newlines."
    )