# test_final_state.py

import os
import pytest

HOME = "/home/user"
CONFIG_DIR = os.path.join(HOME, "config_logs")
LOG_FILE = os.path.join(CONFIG_DIR, "env_setting.log")
ENV_VAR = "MICROSERVICE_ENV"
ENV_EXPECTED_VALUE = "staging"
LOG_EXPECTED_LINE = f"{ENV_VAR}={ENV_EXPECTED_VALUE}"

def test_MICROSERVICE_ENV_set_to_staging():
    value = os.environ.get(ENV_VAR)
    assert value == ENV_EXPECTED_VALUE, (
        f"Environment variable '{ENV_VAR}' is not set to '{ENV_EXPECTED_VALUE}'. "
        f"Current value: '{value}'. You must set it for the current session."
    )

def test_config_logs_directory_exists():
    assert os.path.isdir(CONFIG_DIR), (
        f"Directory '{CONFIG_DIR}' does not exist. "
        "You must create it if missing."
    )

def test_config_logs_directory_writable():
    assert os.access(CONFIG_DIR, os.W_OK), (
        f"Directory '{CONFIG_DIR}' is not writable by the user. "
        "Ensure the directory has the correct permissions."
    )

def test_env_setting_log_file_exists():
    assert os.path.isfile(LOG_FILE), (
        f"The log file '{LOG_FILE}' does not exist. "
        "You must create this file after setting the environment variable."
    )

def test_env_setting_log_file_content_exact():
    assert os.path.isfile(LOG_FILE), (
        f"Cannot check contents: '{LOG_FILE}' does not exist."
    )
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # File must contain exactly one line, with exact content, no extra whitespace or blank lines.
    assert len(lines) == 1, (
        f"'{LOG_FILE}' must contain exactly one line. "
        f"Found {len(lines)} lines."
    )
    line = lines[0]
    # Remove only the trailing newline to check for other whitespace
    if line.endswith('\n'):
        line_content = line[:-1]
        trailing = '\n'
    else:
        line_content = line
        trailing = ''
    assert line_content == LOG_EXPECTED_LINE, (
        f"'{LOG_FILE}' must contain exactly '{LOG_EXPECTED_LINE}'. "
        f"Found: '{line_content}'"
    )
    # Check that there are no leading/trailing spaces
    assert line_content.strip() == LOG_EXPECTED_LINE, (
        f"'{LOG_FILE}' contains leading/trailing whitespace. "
        f"Found: '{line_content}'"
    )
    # No extra trailing blank lines
    assert trailing == '\n', (
        f"'{LOG_FILE}' does not end with a newline character as expected."
    )

def test_MICROSERVICE_ENV_echo_matches(monkeypatch):
    """
    Simulate what would happen if the user ran: echo $MICROSERVICE_ENV
    in the current environment.
    """
    # This simulates the shell output after export
    value = os.environ.get(ENV_VAR)
    assert value == ENV_EXPECTED_VALUE, (
        f"After setting the variable, 'echo $MICROSERVICE_ENV' should output '{ENV_EXPECTED_VALUE}'. "
        f"Current value: '{value}'."
    )