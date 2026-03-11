# test_final_state.py

import os
import configparser
import pytest

DB_CONFIG_PATH = "/home/user/db_config.ini"
DB_SUMMARY_PATH = "/home/user/db_summary.txt"

EXPECTED_LINES = [
    "host=db.internal.example.com",
    "port=5432",
    "max_connections=150",
    "query_timeout=30",
    "slow_query_log=enabled",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES) + "\n"


def test_summary_file_exists():
    assert os.path.isfile(DB_SUMMARY_PATH), (
        f"Summary file not found at {DB_SUMMARY_PATH}. "
        "The file must be created as part of the task."
    )


def test_summary_file_is_readable():
    assert os.access(DB_SUMMARY_PATH, os.R_OK), (
        f"Summary file at {DB_SUMMARY_PATH} exists but is not readable."
    )


def test_summary_file_exact_content():
    with open(DB_SUMMARY_PATH, "r") as f:
        actual_content = f.read()
    assert actual_content == EXPECTED_CONTENT, (
        f"Summary file content does not match expected.\n"
        f"Expected (repr): {EXPECTED_CONTENT!r}\n"
        f"Actual   (repr): {actual_content!r}"
    )


def test_summary_file_line_count():
    with open(DB_SUMMARY_PATH, "r") as f:
        lines = f.readlines()
    assert len(lines) == 5, (
        f"Expected exactly 5 lines in {DB_SUMMARY_PATH}, "
        f"but found {len(lines)} lines. Lines: {lines!r}"
    )


def test_summary_file_no_blank_lines():
    with open(DB_SUMMARY_PATH, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped != "", (
            f"Line {i} in {DB_SUMMARY_PATH} is blank. No blank lines are allowed."
        )


def test_summary_file_no_spaces_around_equals():
    with open(DB_SUMMARY_PATH, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert " = " not in stripped, (
            f"Line {i} contains ' = ' (spaces around equals): {stripped!r}. "
            "The format must be 'key=value' with no spaces around '='."
        )
        assert "= " not in stripped and " =" not in stripped, (
            f"Line {i} contains spaces around '=': {stripped!r}. "
            "The format must be 'key=value' with no spaces around '='."
        )


def test_summary_file_no_trailing_spaces():
    with open(DB_SUMMARY_PATH, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} has trailing whitespace: {stripped!r}. "
            "No trailing spaces are allowed."
        )


def test_summary_line_1_host():
    with open(DB_SUMMARY_PATH, "r") as f:
        lines = f.readlines()
    line = lines[0].rstrip("\n")
    assert line == "host=db.internal.example.com", (
        f"Line 1 (host) is incorrect.\n"
        f"Expected: 'host=db.internal.example.com'\n"
        f"Actual:   {line!r}"
    )


def test_summary_line_2_port():
    with open(DB_SUMMARY_PATH, "r") as f:
        lines = f.readlines()
    line = lines[1].rstrip("\n")
    assert line == "port=5432", (
        f"Line 2 (port) is incorrect.\n"
        f"Expected: 'port=5432'\n"
        f"Actual:   {line!r}"
    )


def test_summary_line_3_max_connections():
    with open(DB_SUMMARY_PATH, "r") as f:
        lines = f.readlines()
    line = lines[2].rstrip("\n")
    assert line == "max_connections=150", (
        f"Line 3 (max_connections) is incorrect.\n"
        f"Expected: 'max_connections=150'\n"
        f"Actual:   {line!r}"
    )


def test_summary_line_4_query_timeout():
    with open(DB_SUMMARY_PATH, "r") as f:
        lines = f.readlines()
    line = lines[3].rstrip("\n")
    assert line == "query_timeout=30", (
        f"Line 4 (query_timeout) is incorrect.\n"
        f"Expected: 'query_timeout=30'\n"
        f"Actual:   {line!r}"
    )


def test_summary_line_5_slow_query_log():
    with open(DB_SUMMARY_PATH, "r") as f:
        lines = f.readlines()
    line = lines[4].rstrip("\n")
    assert line == "slow_query_log=enabled", (
        f"Line 5 (slow_query_log) is incorrect.\n"
        f"Expected: 'slow_query_log=enabled'\n"
        f"Actual:   {line!r}"
    )


def test_summary_values_match_ini_config():
    """Cross-check: values in summary must match what's in the INI config file."""
    assert os.path.isfile(DB_CONFIG_PATH), (
        f"Cannot cross-check: source config file {DB_CONFIG_PATH} not found."
    )

    config = configparser.ConfigParser()
    config.read(DB_CONFIG_PATH)

    with open(DB_SUMMARY_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    expected_pairs = [
        ("connection", "host", lines[0] if len(lines) > 0 else ""),
        ("connection", "port", lines[1] if len(lines) > 1 else ""),
        ("performance", "max_connections", lines[2] if len(lines) > 2 else ""),
        ("performance", "query_timeout", lines[3] if len(lines) > 3 else ""),
        ("logging", "slow_query_log", lines[4] if len(lines) > 4 else ""),
    ]

    for section, key, summary_line in expected_pairs:
        assert section in config, (
            f"Section [{section}] missing from {DB_CONFIG_PATH}."
        )
        assert key in config[section], (
            f"Key '{key}' missing from [{section}] in {DB_CONFIG_PATH}."
        )
        ini_value = config[section][key].strip()
        expected_line = f"{key}={ini_value}"
        assert summary_line == expected_line, (
            f"Summary line for '{key}' does not match INI value.\n"
            f"Expected: {expected_line!r}\n"
            f"Actual:   {summary_line!r}"
        )


def test_summary_file_ends_with_newline():
    with open(DB_SUMMARY_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"The summary file {DB_SUMMARY_PATH} does not end with a newline character. "
        f"Last bytes: {content[-5:]!r}"
    )


def test_summary_file_no_windows_line_endings():
    with open(DB_SUMMARY_PATH, "rb") as f:
        content = f.read()
    assert b"\r\n" not in content, (
        f"The summary file {DB_SUMMARY_PATH} contains Windows-style line endings (\\r\\n). "
        "Only Unix-style line endings (\\n) are expected."
    )


def test_db_config_file_still_exists_and_unchanged():
    """Ensure the original config file was not modified or deleted."""
    assert os.path.isfile(DB_CONFIG_PATH), (
        f"The original database config file {DB_CONFIG_PATH} is missing. "
        "It should not have been deleted or moved."
    )

    config = configparser.ConfigParser()
    config.read(DB_CONFIG_PATH)

    checks = [
        ("connection", "host", "db.internal.example.com"),
        ("connection", "port", "5432"),
        ("performance", "max_connections", "150"),
        ("performance", "query_timeout", "30"),
        ("logging", "slow_query_log", "enabled"),
    ]

    for section, key, expected_value in checks:
        assert section in config, (
            f"Section [{section}] missing from {DB_CONFIG_PATH} after task completion."
        )
        assert key in config[section], (
            f"Key '{key}' missing from [{section}] in {DB_CONFIG_PATH} after task completion."
        )
        actual = config[section][key].strip()
        assert actual == expected_value, (
            f"Original config file may have been modified: "
            f"[{section}] {key} expected '{expected_value}', got '{actual}'."
        )