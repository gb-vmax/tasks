# test_final_state.py

import os
import stat
import pytest
import subprocess

HOME = "/home/user"
DTUNE_DIR = os.path.join(HOME, ".dashboard_tune")
ENV_FILE = os.path.join(DTUNE_DIR, "dashboard.env")
LOG_FILE = os.path.join(DTUNE_DIR, "settings_merged.log")

ENV_VARS = [
    ("DASHBOARD_TITLE", "Staging Observability"),
    ("DEBUG_MODE", "true"),
    ("LOG_LEVEL", "info"),
    ("DATASOURCE_URL", "https://logs-staging.example.com/query"),
    ("REFRESH_INTERVAL", "30"),
]

SESSION_VARS = [
    ("SESSION_OWNER", "alice.smith"),
    ("SESSION_ID", "stag-20230501-001"),
]

MERGED_ORDER = [
    "DASHBOARD_TITLE",
    "DEBUG_MODE",
    "LOG_LEVEL",
    "DATASOURCE_URL",
    "REFRESH_INTERVAL",
    "SESSION_OWNER",
    "SESSION_ID",
]


def get_env_file_lines():
    """Read lines from the dashboard.env file, stripped of newlines."""
    with open(ENV_FILE, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def get_log_file_lines():
    """Read lines from the settings_merged.log file, stripped of newlines."""
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def get_shell_env_vars():
    """Get environment variables from printenv as a dict."""
    proc = subprocess.run(["printenv"], capture_output=True, text=True, env=os.environ)
    env_lines = proc.stdout.strip().split("\n")
    env_dict = {}
    for line in env_lines:
        if "=" in line:
            k, v = line.split("=", 1)
            env_dict[k] = v
    return env_dict


@pytest.mark.order(1)
def test_dashboard_tune_directory_exists_and_is_user_writable():
    assert os.path.isdir(DTUNE_DIR), (
        f"Directory '{DTUNE_DIR}' does not exist. "
        "You must create this hidden directory in your home directory."
    )
    mode = os.stat(DTUNE_DIR).st_mode
    assert mode & stat.S_IWUSR, (
        f"Directory '{DTUNE_DIR}' exists, but is not user-writable. "
        "Please ensure the directory permissions allow the user to write."
    )


@pytest.mark.order(2)
def test_dashboard_env_file_exists_content_and_permissions():
    assert os.path.isfile(ENV_FILE), (
        f"File '{ENV_FILE}' does not exist. "
        "You must create this file in the '.dashboard_tune' directory."
    )
    mode = os.stat(ENV_FILE).st_mode
    assert mode & stat.S_IWUSR, (
        f"File '{ENV_FILE}' exists, but is not user-writable. "
        "Please ensure the file permissions allow the user to write."
    )
    lines = get_env_file_lines()
    expected_lines = [f"{k}={v}" for k, v in ENV_VARS]
    assert lines == expected_lines, (
        f"File '{ENV_FILE}' does not have the correct content.\n"
        "Expected lines:\n"
        + "\n".join(expected_lines)
        + "\nActual lines:\n"
        + "\n".join(lines)
        + "\nEnsure there are no blank lines, extra whitespace, or missing/extra variables."
    )


@pytest.mark.order(3)
def test_session_environment_variables_are_exported():
    env = get_shell_env_vars()
    missing = []
    wrong = []
    for k, v in SESSION_VARS:
        if k not in env:
            missing.append(k)
        elif env[k] != v:
            wrong.append(f"{k} (expected '{v}', got '{env[k]}')")
    assert not missing, (
        f"Session environment variable(s) missing from shell environment: {', '.join(missing)}. "
        "You must export these variables (not just set in a file)."
    )
    assert not wrong, (
        f"Session environment variable(s) have incorrect value: {', '.join(wrong)}. "
        "Please export them with the correct value."
    )


@pytest.mark.order(4)
def test_settings_merged_log_exists_content_and_permissions():
    assert os.path.isfile(LOG_FILE), (
        f"Log file '{LOG_FILE}' does not exist. "
        "You must create this file in the '.dashboard_tune' directory."
    )
    mode = os.stat(LOG_FILE).st_mode
    assert mode & stat.S_IWUSR, (
        f"Log file '{LOG_FILE}' exists, but is not user-writable. "
        "Please ensure the file permissions allow the user to write."
    )
    lines = get_log_file_lines()
    var_dict = dict(ENV_VARS + SESSION_VARS)
    expected_lines = [f"{var}={var_dict[var]}" for var in MERGED_ORDER]
    assert lines == expected_lines, (
        f"Log file '{LOG_FILE}' does not have the correct content or order.\n"
        "Expected lines (in order):\n"
        + "\n".join(expected_lines)
        + "\nActual lines:\n"
        + "\n".join(lines)
        + "\nEnsure all 7 variables are present, in the correct order, with no blank lines or extra whitespace."
    )
    assert len(lines) == 7, (
        f"Log file '{LOG_FILE}' should have exactly 7 lines (one for each variable), but has {len(lines)}."
    )
    for i, line in enumerate(lines):
        assert line.strip(), (
            f"Log file '{LOG_FILE}' contains a blank or empty line at position {i+1}. "
            "There must be no blank or extra lines."
        )
    # Check for extra whitespace around '=' or at line ends
    for i, line in enumerate(lines):
        if "=" not in line:
            pytest.fail(
                f"Log file '{LOG_FILE}' line {i+1} ('{line}') does not contain '='. "
                "Each line must be in VARIABLE=VALUE format."
            )
        var, val = line.split("=", 1)
        expected_var = MERGED_ORDER[i]
        expected_val = var_dict[expected_var]
        assert var == expected_var, (
            f"Log file '{LOG_FILE}' line {i+1} variable is '{var}', expected '{expected_var}'."
        )
        assert val == expected_val, (
            f"Log file '{LOG_FILE}' line {i+1} value is '{val}', expected '{expected_val}'."
        )
        assert line == f"{var}={val}", (
            f"Log file '{LOG_FILE}' line {i+1} ('{line}') has extra whitespace. "
            "There must be no spaces before or after '='."
        )