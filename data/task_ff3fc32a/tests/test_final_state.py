# test_final_state.py

import os
import stat
import pytest

TEST_ENV_PATH = "/home/user/configs/test_env.sh"
APP_INI_PATH = "/home/user/configs/app.ini"

EXPECTED_LINES = [
    "export TEST_DATABASE_HOST=db.internal.example.com",
    "export TEST_DATABASE_PORT=5432",
    "export TEST_DATABASE_NAME=appdb_production",
    "export TEST_SERVER_TIMEOUT=30",
    "export TEST_SERVER_DEBUG=false",
    "export TEST_AUTH_SECRET_KEY=s3cr3t!k3y#2024",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES) + "\n"


def test_test_env_sh_exists():
    assert os.path.isfile(TEST_ENV_PATH), (
        f"File '{TEST_ENV_PATH}' does not exist. "
        "The task requires creating this file."
    )


def test_test_env_sh_is_readable():
    assert os.access(TEST_ENV_PATH, os.R_OK), (
        f"File '{TEST_ENV_PATH}' is not readable."
    )


def test_test_env_sh_line_count():
    with open(TEST_ENV_PATH, "r") as f:
        content = f.read()
    # Strip trailing newline for counting, but the file should have exactly 6 lines
    lines = content.splitlines()
    assert len(lines) == 6, (
        f"File '{TEST_ENV_PATH}' should contain exactly 6 lines, "
        f"but found {len(lines)} lines.\n"
        f"Actual content:\n{content}"
    )


def test_test_env_sh_no_blank_lines():
    with open(TEST_ENV_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"File '{TEST_ENV_PATH}' contains blank lines at positions: {blank_lines}. "
        "The file must contain no blank lines."
    )


def test_test_env_sh_no_comments():
    with open(TEST_ENV_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    comment_lines = [i + 1 for i, line in enumerate(lines) if line.strip().startswith("#")]
    assert not comment_lines, (
        f"File '{TEST_ENV_PATH}' contains comment lines at positions: {comment_lines}. "
        "The file must contain no comments."
    )


def test_test_env_sh_no_shebang():
    with open(TEST_ENV_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    shebang_lines = [i + 1 for i, line in enumerate(lines) if line.strip().startswith("!")]
    assert not shebang_lines, (
        f"File '{TEST_ENV_PATH}' contains a shebang or '!' line. "
        "The file must not have a shebang header."
    )


def test_test_env_sh_line1():
    with open(TEST_ENV_PATH, "r") as f:
        lines = f.read().splitlines()
    assert len(lines) >= 1, f"File '{TEST_ENV_PATH}' has fewer than 1 line."
    assert lines[0] == EXPECTED_LINES[0], (
        f"Line 1 of '{TEST_ENV_PATH}' is wrong.\n"
        f"Expected: {EXPECTED_LINES[0]!r}\n"
        f"Got:      {lines[0]!r}"
    )


def test_test_env_sh_line2():
    with open(TEST_ENV_PATH, "r") as f:
        lines = f.read().splitlines()
    assert len(lines) >= 2, f"File '{TEST_ENV_PATH}' has fewer than 2 lines."
    assert lines[1] == EXPECTED_LINES[1], (
        f"Line 2 of '{TEST_ENV_PATH}' is wrong.\n"
        f"Expected: {EXPECTED_LINES[1]!r}\n"
        f"Got:      {lines[1]!r}"
    )


def test_test_env_sh_line3():
    with open(TEST_ENV_PATH, "r") as f:
        lines = f.read().splitlines()
    assert len(lines) >= 3, f"File '{TEST_ENV_PATH}' has fewer than 3 lines."
    assert lines[2] == EXPECTED_LINES[2], (
        f"Line 3 of '{TEST_ENV_PATH}' is wrong.\n"
        f"Expected: {EXPECTED_LINES[2]!r}\n"
        f"Got:      {lines[2]!r}"
    )


def test_test_env_sh_line4():
    with open(TEST_ENV_PATH, "r") as f:
        lines = f.read().splitlines()
    assert len(lines) >= 4, f"File '{TEST_ENV_PATH}' has fewer than 4 lines."
    assert lines[3] == EXPECTED_LINES[3], (
        f"Line 4 of '{TEST_ENV_PATH}' is wrong.\n"
        f"Expected: {EXPECTED_LINES[3]!r}\n"
        f"Got:      {lines[3]!r}"
    )


def test_test_env_sh_line5():
    with open(TEST_ENV_PATH, "r") as f:
        lines = f.read().splitlines()
    assert len(lines) >= 5, f"File '{TEST_ENV_PATH}' has fewer than 5 lines."
    assert lines[4] == EXPECTED_LINES[4], (
        f"Line 5 of '{TEST_ENV_PATH}' is wrong.\n"
        f"Expected: {EXPECTED_LINES[4]!r}\n"
        f"Got:      {lines[4]!r}"
    )


def test_test_env_sh_line6():
    with open(TEST_ENV_PATH, "r") as f:
        lines = f.read().splitlines()
    assert len(lines) >= 6, f"File '{TEST_ENV_PATH}' has fewer than 6 lines."
    assert lines[5] == EXPECTED_LINES[5], (
        f"Line 6 of '{TEST_ENV_PATH}' is wrong.\n"
        f"Expected: {EXPECTED_LINES[5]!r}\n"
        f"Got:      {lines[5]!r}"
    )


def test_test_env_sh_exact_content():
    with open(TEST_ENV_PATH, "r") as f:
        content = f.read()
    # Allow trailing newline at end of file (POSIX standard), but nothing else extra
    normalized = content if content.endswith("\n") else content + "\n"
    assert normalized == EXPECTED_CONTENT, (
        f"File '{TEST_ENV_PATH}' does not have the exact expected content.\n"
        f"Expected:\n{EXPECTED_CONTENT!r}\n"
        f"Got:\n{content!r}"
    )


def test_test_env_sh_permissions_755():
    file_stat = os.stat(TEST_ENV_PATH)
    mode = stat.S_IMODE(file_stat.st_mode)
    expected_mode = 0o755
    assert mode == expected_mode, (
        f"File '{TEST_ENV_PATH}' has permissions {oct(mode)}, "
        f"but expected {oct(expected_mode)} (755 / -rwxr-xr-x). "
        "Run: chmod 755 /home/user/configs/test_env.sh"
    )


def test_test_env_sh_is_executable_by_owner():
    file_stat = os.stat(TEST_ENV_PATH)
    mode = stat.S_IMODE(file_stat.st_mode)
    assert mode & stat.S_IXUSR, (
        f"File '{TEST_ENV_PATH}' is not executable by owner. "
        f"Current permissions: {oct(mode)}"
    )


def test_test_env_sh_is_executable_by_group():
    file_stat = os.stat(TEST_ENV_PATH)
    mode = stat.S_IMODE(file_stat.st_mode)
    assert mode & stat.S_IXGRP, (
        f"File '{TEST_ENV_PATH}' is not executable by group. "
        f"Current permissions: {oct(mode)}"
    )


def test_test_env_sh_is_executable_by_others():
    file_stat = os.stat(TEST_ENV_PATH)
    mode = stat.S_IMODE(file_stat.st_mode)
    assert mode & stat.S_IXOTH, (
        f"File '{TEST_ENV_PATH}' is not executable by others. "
        f"Current permissions: {oct(mode)}"
    )


def test_test_env_sh_all_lines_start_with_export():
    with open(TEST_ENV_PATH, "r") as f:
        lines = f.read().splitlines()
    for i, line in enumerate(lines, start=1):
        assert line.startswith("export "), (
            f"Line {i} of '{TEST_ENV_PATH}' does not start with 'export ': {line!r}"
        )


def test_test_env_sh_values_have_no_surrounding_whitespace():
    with open(TEST_ENV_PATH, "r") as f:
        lines = f.read().splitlines()
    for i, line in enumerate(lines, start=1):
        # Each line should be: export KEY=VALUE
        assert line.startswith("export "), (
            f"Line {i} does not start with 'export ': {line!r}"
        )
        rest = line[len("export "):]
        assert "=" in rest, (
            f"Line {i} does not contain '=': {line!r}"
        )
        key, value = rest.split("=", 1)
        assert key == key.strip(), (
            f"Line {i} key has surrounding whitespace: {key!r}"
        )
        assert value == value.strip(), (
            f"Line {i} value has surrounding whitespace: {value!r}"
        )


def test_app_ini_still_intact():
    """Ensure the original app.ini was not modified."""
    assert os.path.isfile(APP_INI_PATH), (
        f"Original file '{APP_INI_PATH}' no longer exists after the task. "
        "It should not have been deleted or moved."
    )
    import configparser
    config = configparser.ConfigParser()
    config.read(APP_INI_PATH)
    assert config["database"].get("host", "").strip() == "db.internal.example.com"
    assert config["database"].get("port", "").strip() == "5432"
    assert config["database"].get("name", "").strip() == "appdb_production"
    assert config["server"].get("timeout", "").strip() == "30"
    assert config["server"].get("debug", "").strip() == "false"
    assert config["auth"].get("secret_key", "").strip() == "s3cr3t!k3y#2024"