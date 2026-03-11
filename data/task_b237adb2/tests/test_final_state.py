# test_final_state.py

import os
import pytest

ENV_FILE = "/home/user/apps/staging/.env"
SUMMARY_FILE = "/home/user/apps/staging/env_summary.txt"

EXPECTED_ENV_CONTENT = (
    "APP_ENV=staging\n"
    "APP_PORT=8080\n"
    "DB_HOST=db-staging.internal.company.com\n"
    "DB_PORT=5432\n"
    "DB_USER=staginguser\n"
    "DB_PASSWORD=hunter2\n"
    "API_KEY=sk-staging-9f2a1c4e8b3d7f6a\n"
    "LOG_LEVEL=debug\n"
)

EXPECTED_SUMMARY_CONTENT = (
    "DB_HOST=db-staging.internal.company.com\n"
    "DB_PORT=5432\n"
    "API_KEY=sk-staging-9f2a1c4e8b3d7f6a\n"
    "APP_ENV=staging\n"
)


# ── .env file tests ──────────────────────────────────────────────────────────

def test_env_file_exists():
    assert os.path.isfile(ENV_FILE), (
        f"File '{ENV_FILE}' does not exist. "
        "The staging .env file must be present after the task is completed."
    )


def test_env_file_is_readable():
    assert os.access(ENV_FILE, os.R_OK), (
        f"File '{ENV_FILE}' is not readable."
    )


def test_env_file_exact_content():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_ENV_CONTENT, (
        f"File '{ENV_FILE}' does not have the expected final content.\n"
        f"Expected:\n{EXPECTED_ENV_CONTENT!r}\n"
        f"Got:\n{content!r}"
    )


def test_env_file_db_host_updated():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    assert "DB_HOST=db-staging.internal.company.com" in content, (
        f"'DB_HOST' was not updated to 'db-staging.internal.company.com' in '{ENV_FILE}'.\n"
        f"File content:\n{content}"
    )


def test_env_file_old_db_host_removed():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    assert "DB_HOST=db-prod.internal.company.com" not in content, (
        f"Old 'DB_HOST=db-prod.internal.company.com' still present in '{ENV_FILE}'. "
        "It must be replaced with the new value.\n"
        f"File content:\n{content}"
    )


def test_env_file_api_key_updated():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    assert "API_KEY=sk-staging-9f2a1c4e8b3d7f6a" in content, (
        f"'API_KEY' was not updated to 'sk-staging-9f2a1c4e8b3d7f6a' in '{ENV_FILE}'.\n"
        f"File content:\n{content}"
    )


def test_env_file_old_api_key_removed():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    assert "API_KEY=sk-old-key-deprecated-111111" not in content, (
        f"Old 'API_KEY=sk-old-key-deprecated-111111' still present in '{ENV_FILE}'. "
        "It must be replaced with the new value.\n"
        f"File content:\n{content}"
    )


def test_env_file_other_vars_unchanged():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    expected_unchanged = [
        "APP_ENV=staging",
        "APP_PORT=8080",
        "DB_PORT=5432",
        "DB_USER=staginguser",
        "DB_PASSWORD=hunter2",
        "LOG_LEVEL=debug",
    ]
    for var in expected_unchanged:
        assert var in content, (
            f"Variable '{var}' is missing or changed in '{ENV_FILE}'. "
            "Variables other than DB_HOST and API_KEY must remain exactly as they were.\n"
            f"File content:\n{content}"
        )


def test_env_file_line_count():
    with open(ENV_FILE, "r") as f:
        lines = f.readlines()
    non_empty_lines = [l for l in lines if l.strip()]
    assert len(non_empty_lines) == 8, (
        f"Expected exactly 8 non-empty lines in '{ENV_FILE}', "
        f"but found {len(non_empty_lines)}.\n"
        f"Lines: {lines}"
    )


def test_env_file_line_order():
    with open(ENV_FILE, "r") as f:
        lines = f.readlines()
    expected_lines = EXPECTED_ENV_CONTENT.splitlines(keepends=True)
    assert lines == expected_lines, (
        f"Lines in '{ENV_FILE}' are not in the expected order.\n"
        f"Expected lines: {expected_lines}\n"
        f"Got lines:      {lines}"
    )


def test_env_file_ends_with_newline():
    with open(ENV_FILE, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"File '{ENV_FILE}' does not end with a newline character."
    )


def test_env_file_no_trailing_spaces():
    with open(ENV_FILE, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} in '{ENV_FILE}' has trailing whitespace: {line!r}"
        )


# ── env_summary.txt tests ────────────────────────────────────────────────────

def test_summary_file_exists():
    assert os.path.isfile(SUMMARY_FILE), (
        f"Summary file '{SUMMARY_FILE}' does not exist. "
        "It must be created as part of the task."
    )


def test_summary_file_is_readable():
    assert os.access(SUMMARY_FILE, os.R_OK), (
        f"Summary file '{SUMMARY_FILE}' is not readable."
    )


def test_summary_file_exact_content():
    with open(SUMMARY_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_SUMMARY_CONTENT, (
        f"Summary file '{SUMMARY_FILE}' does not have the expected content.\n"
        f"Expected:\n{EXPECTED_SUMMARY_CONTENT!r}\n"
        f"Got:\n{content!r}"
    )


def test_summary_file_line_count():
    with open(SUMMARY_FILE, "r") as f:
        lines = f.readlines()
    non_empty_lines = [l for l in lines if l.strip()]
    assert len(non_empty_lines) == 4, (
        f"Expected exactly 4 non-empty lines in '{SUMMARY_FILE}', "
        f"but found {len(non_empty_lines)}.\n"
        f"Lines: {lines}"
    )


def test_summary_file_line_order():
    with open(SUMMARY_FILE, "r") as f:
        lines = f.readlines()
    expected_lines = EXPECTED_SUMMARY_CONTENT.splitlines(keepends=True)
    assert lines == expected_lines, (
        f"Lines in '{SUMMARY_FILE}' are not in the expected order.\n"
        f"Expected: {expected_lines}\n"
        f"Got:      {lines}"
    )


def test_summary_file_db_host_line():
    with open(SUMMARY_FILE, "r") as f:
        lines = f.readlines()
    assert lines[0].rstrip("\n") == "DB_HOST=db-staging.internal.company.com", (
        f"Line 1 of '{SUMMARY_FILE}' is incorrect.\n"
        f"Expected: 'DB_HOST=db-staging.internal.company.com'\n"
        f"Got:      {lines[0]!r}"
    )


def test_summary_file_db_port_line():
    with open(SUMMARY_FILE, "r") as f:
        lines = f.readlines()
    assert lines[1].rstrip("\n") == "DB_PORT=5432", (
        f"Line 2 of '{SUMMARY_FILE}' is incorrect.\n"
        f"Expected: 'DB_PORT=5432'\n"
        f"Got:      {lines[1]!r}"
    )


def test_summary_file_api_key_line():
    with open(SUMMARY_FILE, "r") as f:
        lines = f.readlines()
    assert lines[2].rstrip("\n") == "API_KEY=sk-staging-9f2a1c4e8b3d7f6a", (
        f"Line 3 of '{SUMMARY_FILE}' is incorrect.\n"
        f"Expected: 'API_KEY=sk-staging-9f2a1c4e8b3d7f6a'\n"
        f"Got:      {lines[2]!r}"
    )


def test_summary_file_app_env_line():
    with open(SUMMARY_FILE, "r") as f:
        lines = f.readlines()
    assert lines[3].rstrip("\n") == "APP_ENV=staging", (
        f"Line 4 of '{SUMMARY_FILE}' is incorrect.\n"
        f"Expected: 'APP_ENV=staging'\n"
        f"Got:      {lines[3]!r}"
    )


def test_summary_file_no_trailing_spaces():
    with open(SUMMARY_FILE, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} in '{SUMMARY_FILE}' has trailing whitespace: {line!r}"
        )


def test_summary_file_no_blank_lines():
    with open(SUMMARY_FILE, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"Line {i} in '{SUMMARY_FILE}' is blank. No blank lines are allowed."
        )


def test_summary_file_ends_with_newline():
    with open(SUMMARY_FILE, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"Summary file '{SUMMARY_FILE}' does not end with a newline character."
    )


def test_summary_file_no_spaces_around_equals():
    with open(SUMMARY_FILE, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        key_value = line.rstrip("\n")
        if "=" in key_value:
            key, _, value = key_value.partition("=")
            assert key == key.rstrip(), (
                f"Line {i} in '{SUMMARY_FILE}' has a space before '=': {line!r}"
            )
            assert value == value.lstrip(), (
                f"Line {i} in '{SUMMARY_FILE}' has a space after '=': {line!r}"
            )