# test_final_state.py

import os
import pytest

PROJECT_DIR = "/home/user/my_python_project"
SETTINGS_YAML = os.path.join(PROJECT_DIR, "settings.yaml")
CONFIG_TOML = os.path.join(PROJECT_DIR, "config.toml")
CONFIG_UPDATE_LOG = os.path.join(PROJECT_DIR, "config_update.log")

EXPECTED_SETTINGS_YAML = """database:
  host: localhost
  port: 5432
  user: admin
  password: secret123
"""

EXPECTED_CONFIG_TOML = """[project]
name = "my_python_project"
version = "1.0.0"
"""

EXPECTED_CONFIG_UPDATE_LOG = (
    "=== settings.yaml ===\n"
    "database:\n"
    "  host: localhost\n"
    "  port: 5432\n"
    "  user: admin\n"
    "  password: secret123\n"
    "=== config.toml ===\n"
    "[project]\n"
    "name = \"my_python_project\"\n"
    "version = \"1.0.0\"\n"
)

def read_file(path):
    """Read file contents, returning a string. If file does not exist, return None."""
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def test_project_directory_still_exists():
    assert os.path.isdir(PROJECT_DIR), (
        f"Project directory '{PROJECT_DIR}' is missing after completion. "
        "It must exist."
    )

def test_settings_yaml_final_content():
    actual = read_file(SETTINGS_YAML)
    assert actual is not None, (
        f"File '{SETTINGS_YAML}' does not exist after completion. "
        "It must exist with the correct content."
    )
    # Allow a trailing newline, but content must match exactly otherwise.
    if not (actual == EXPECTED_SETTINGS_YAML or actual == EXPECTED_SETTINGS_YAML.rstrip("\n")):
        # Show diff-like error
        msg = (
            f"File '{SETTINGS_YAML}' does not contain the exact expected YAML content.\n"
            "Expected:\n"
            f"{EXPECTED_SETTINGS_YAML!r}\n"
            "Actual:\n"
            f"{actual!r}\n"
            "Check indentation, spelling, and formatting (2 spaces per indent, correct keys)."
        )
        assert False, msg

def test_config_toml_final_content():
    actual = read_file(CONFIG_TOML)
    assert actual is not None, (
        f"File '{CONFIG_TOML}' does not exist after completion. "
        "It must exist with the correct content."
    )
    # Allow a trailing newline, but content must match exactly otherwise.
    if not (actual == EXPECTED_CONFIG_TOML or actual == EXPECTED_CONFIG_TOML.rstrip("\n")):
        msg = (
            f"File '{CONFIG_TOML}' does not contain the exact expected TOML content.\n"
            "Expected:\n"
            f"{EXPECTED_CONFIG_TOML!r}\n"
            "Actual:\n"
            f"{actual!r}\n"
            "Check section header, key names, values, and line formatting."
        )
        assert False, msg

def test_config_update_log_exists():
    assert os.path.isfile(CONFIG_UPDATE_LOG), (
        f"Log file '{CONFIG_UPDATE_LOG}' does not exist after completion. "
        "You must create this log file listing the exact contents of both config files."
    )

def test_config_update_log_content():
    actual = read_file(CONFIG_UPDATE_LOG)
    assert actual is not None, (
        f"Log file '{CONFIG_UPDATE_LOG}' does not exist after completion. "
        "You must create this log file."
    )
    # The log must match exactly (including newlines, section headers, and file content).
    if actual != EXPECTED_CONFIG_UPDATE_LOG:
        msg = (
            f"Log file '{CONFIG_UPDATE_LOG}' does not match the required format/content.\n"
            "Expected:\n"
            f"{EXPECTED_CONFIG_UPDATE_LOG!r}\n"
            "Actual:\n"
            f"{actual!r}\n"
            "Check section headers, newlines, and that the config file contents are listed exactly as specified."
        )
        assert False, msg

def test_no_extra_content_in_settings_yaml():
    """Ensure no extra keys or sections are present in settings.yaml."""
    actual = read_file(SETTINGS_YAML)
    assert actual is not None  # Already checked elsewhere
    # Split and check lines
    expected_lines = EXPECTED_SETTINGS_YAML.strip().splitlines()
    actual_lines = actual.strip().splitlines()
    assert actual_lines == expected_lines, (
        f"File '{SETTINGS_YAML}' contains unexpected extra lines or formatting issues.\n"
        "Expected lines:\n"
        f"{expected_lines}\n"
        "Actual lines:\n"
        f"{actual_lines}\n"
        "Remove any extra sections, comments, or whitespace."
    )

def test_no_extra_content_in_config_toml():
    """Ensure no extra keys or sections are present in config.toml."""
    actual = read_file(CONFIG_TOML)
    assert actual is not None  # Already checked elsewhere
    expected_lines = EXPECTED_CONFIG_TOML.strip().splitlines()
    actual_lines = actual.strip().splitlines()
    assert actual_lines == expected_lines, (
        f"File '{CONFIG_TOML}' contains unexpected extra lines or formatting issues.\n"
        "Expected lines:\n"
        f"{expected_lines}\n"
        "Actual lines:\n"
        f"{actual_lines}\n"
        "Remove any extra sections, comments, or whitespace."
    )

def test_no_extra_content_in_config_update_log():
    """Ensure log file contains only the required content, no extra lines before or after."""
    actual = read_file(CONFIG_UPDATE_LOG)
    assert actual is not None
    expected = EXPECTED_CONFIG_UPDATE_LOG
    # There must be no extra blank lines or whitespace at the start/end
    assert actual == expected, (
        f"Log file '{CONFIG_UPDATE_LOG}' contains extra or missing content/blank lines.\n"
        "Expected:\n"
        f"{expected!r}\n"
        "Actual:\n"
        f"{actual!r}\n"
        "Remove any extra newlines or whitespace."
    )