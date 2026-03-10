# test_final_state.py

import os
import pytest

DEPLOY_INI_PATH = "/home/user/project/deploy.ini"
CONFIG_SUMMARY_PATH = "/home/user/project/config_summary.txt"

EXPECTED_SUMMARY_LINES = [
    "[development] host=localhost port=5000",
    "[staging] host=staging.myapp.io port=8080",
    "[production] host=prod.myapp.io port=443",
]

EXPECTED_DEPLOY_INI_CONTENT = """\
[development]
host = localhost
port = 5000
debug = true
db = dev_db

[staging]
host = staging.myapp.io
port = 8080
debug = false
db = staging_db

[production]
host = prod.myapp.io
port = 443
debug = false
db = prod_db
; summary generated"""


# --- config_summary.txt tests ---

def test_config_summary_exists():
    assert os.path.isfile(CONFIG_SUMMARY_PATH), (
        f"Summary file '{CONFIG_SUMMARY_PATH}' does not exist. "
        "The task requires creating this file."
    )


def test_config_summary_is_readable():
    assert os.access(CONFIG_SUMMARY_PATH, os.R_OK), (
        f"Summary file '{CONFIG_SUMMARY_PATH}' is not readable."
    )


def test_config_summary_has_exactly_3_lines():
    with open(CONFIG_SUMMARY_PATH, "r") as f:
        content = f.read()
    # Strip trailing newline for counting, but each line must be present
    lines = content.rstrip("\n").splitlines()
    assert len(lines) == 3, (
        f"Expected exactly 3 lines in '{CONFIG_SUMMARY_PATH}', "
        f"but found {len(lines)} line(s).\n"
        f"Actual content:\n{content}"
    )


def test_config_summary_line1_development():
    with open(CONFIG_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    assert len(lines) >= 1, (
        f"'{CONFIG_SUMMARY_PATH}' has fewer than 1 line."
    )
    assert lines[0] == EXPECTED_SUMMARY_LINES[0], (
        f"Line 1 of '{CONFIG_SUMMARY_PATH}' is wrong.\n"
        f"Expected: {EXPECTED_SUMMARY_LINES[0]!r}\n"
        f"Got:      {lines[0]!r}"
    )


def test_config_summary_line2_staging():
    with open(CONFIG_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    assert len(lines) >= 2, (
        f"'{CONFIG_SUMMARY_PATH}' has fewer than 2 lines."
    )
    assert lines[1] == EXPECTED_SUMMARY_LINES[1], (
        f"Line 2 of '{CONFIG_SUMMARY_PATH}' is wrong.\n"
        f"Expected: {EXPECTED_SUMMARY_LINES[1]!r}\n"
        f"Got:      {lines[1]!r}"
    )


def test_config_summary_line3_production():
    with open(CONFIG_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    assert len(lines) >= 3, (
        f"'{CONFIG_SUMMARY_PATH}' has fewer than 3 lines."
    )
    assert lines[2] == EXPECTED_SUMMARY_LINES[2], (
        f"Line 3 of '{CONFIG_SUMMARY_PATH}' is wrong.\n"
        f"Expected: {EXPECTED_SUMMARY_LINES[2]!r}\n"
        f"Got:      {lines[2]!r}"
    )


def test_config_summary_no_trailing_spaces():
    with open(CONFIG_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} of '{CONFIG_SUMMARY_PATH}' has trailing spaces.\n"
            f"Got: {line!r}"
        )


def test_config_summary_no_blank_lines():
    with open(CONFIG_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"Line {i} of '{CONFIG_SUMMARY_PATH}' is blank. "
            "No blank lines are allowed between entries."
        )


def test_config_summary_exact_content():
    expected_content = "\n".join(EXPECTED_SUMMARY_LINES) + "\n"
    with open(CONFIG_SUMMARY_PATH, "r") as f:
        actual_content = f.read()
    # Also allow without trailing newline
    actual_stripped = actual_content.rstrip("\n")
    expected_stripped = "\n".join(EXPECTED_SUMMARY_LINES)
    assert actual_stripped == expected_stripped, (
        f"Content of '{CONFIG_SUMMARY_PATH}' does not exactly match expected.\n"
        f"Expected:\n{expected_stripped!r}\n\n"
        f"Got:\n{actual_stripped!r}"
    )


# --- deploy.ini tests ---

def test_deploy_ini_exists():
    assert os.path.isfile(DEPLOY_INI_PATH), (
        f"Deploy config file '{DEPLOY_INI_PATH}' does not exist."
    )


def test_deploy_ini_last_line_is_summary_comment():
    with open(DEPLOY_INI_PATH, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").splitlines()
    assert lines, (
        f"'{DEPLOY_INI_PATH}' is empty."
    )
    last_line = lines[-1]
    assert last_line == "; summary generated", (
        f"Last line of '{DEPLOY_INI_PATH}' is not '; summary generated'.\n"
        f"Got: {last_line!r}"
    )


def test_deploy_ini_contains_summary_comment():
    with open(DEPLOY_INI_PATH, "r") as f:
        content = f.read()
    assert "; summary generated" in content, (
        f"'{DEPLOY_INI_PATH}' does not contain '; summary generated'."
    )


def test_deploy_ini_original_sections_preserved():
    import configparser
    config = configparser.ConfigParser()
    config.read(DEPLOY_INI_PATH)

    for section in ("development", "staging", "production"):
        assert section in config, (
            f"Section [{section}] not found in '{DEPLOY_INI_PATH}' after modification."
        )


def test_deploy_ini_development_values_preserved():
    import configparser
    config = configparser.ConfigParser()
    config.read(DEPLOY_INI_PATH)
    assert config["development"].get("host") == "localhost", (
        "Expected host=localhost in [development] section of deploy.ini."
    )
    assert config["development"].get("port") == "5000", (
        "Expected port=5000 in [development] section of deploy.ini."
    )
    assert config["development"].get("debug") == "true", (
        "Expected debug=true in [development] section of deploy.ini."
    )
    assert config["development"].get("db") == "dev_db", (
        "Expected db=dev_db in [development] section of deploy.ini."
    )


def test_deploy_ini_staging_values_preserved():
    import configparser
    config = configparser.ConfigParser()
    config.read(DEPLOY_INI_PATH)
    assert config["staging"].get("host") == "staging.myapp.io", (
        "Expected host=staging.myapp.io in [staging] section of deploy.ini."
    )
    assert config["staging"].get("port") == "8080", (
        "Expected port=8080 in [staging] section of deploy.ini."
    )
    assert config["staging"].get("debug") == "false", (
        "Expected debug=false in [staging] section of deploy.ini."
    )
    assert config["staging"].get("db") == "staging_db", (
        "Expected db=staging_db in [staging] section of deploy.ini."
    )


def test_deploy_ini_production_values_preserved():
    import configparser
    config = configparser.ConfigParser()
    config.read(DEPLOY_INI_PATH)
    assert config["production"].get("host") == "prod.myapp.io", (
        "Expected host=prod.myapp.io in [production] section of deploy.ini."
    )
    assert config["production"].get("port") == "443", (
        "Expected port=443 in [production] section of deploy.ini."
    )
    assert config["production"].get("debug") == "false", (
        "Expected debug=false in [production] section of deploy.ini."
    )
    assert config["production"].get("db") == "prod_db", (
        "Expected db=prod_db in [production] section of deploy.ini."
    )


def test_deploy_ini_exact_final_content():
    with open(DEPLOY_INI_PATH, "r") as f:
        actual_content = f.read()
    actual_stripped = actual_content.rstrip("\n")
    expected_stripped = EXPECTED_DEPLOY_INI_CONTENT.rstrip("\n")
    assert actual_stripped == expected_stripped, (
        f"Final content of '{DEPLOY_INI_PATH}' does not match expected.\n"
        f"Expected:\n{expected_stripped!r}\n\n"
        f"Got:\n{actual_stripped!r}"
    )


def test_deploy_ini_summary_comment_appears_only_once():
    with open(DEPLOY_INI_PATH, "r") as f:
        content = f.read()
    count = content.count("; summary generated")
    assert count == 1, (
        f"'; summary generated' appears {count} time(s) in '{DEPLOY_INI_PATH}', "
        "but it should appear exactly once."
    )