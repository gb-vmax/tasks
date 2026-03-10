# test_final_state.py

import os
import re
import subprocess
from datetime import datetime
import pytest

CONFIG_PATH = "/home/user/app/config.env"
LOG_PATH = "/home/user/app/rotation_log.txt"

OLD_API_KEY = "a3f8c2e1b7d94f0612345678abcdef90"
OLD_API_KEY_PREFIX = "a3f8c2e1"

EXPECTED_LOG_LINE_1 = "ROTATED DB_PASSWORD on 2024-11-01 old=hunter24 new=9f2a3b1c"
EXPECTED_LOG_LINE_2 = "ROTATED API_KEY on 2024-12-15 old=ccf01234 new=ab987654"

EXPECTED_NON_APIKEY_LINES = [
    "APP_ENV=production",
    "DB_HOST=db.internal.example.com",
    "DB_PORT=5432",
    "LOG_LEVEL=warn",
    "MAX_CONNECTIONS=50",
]

EXPECTED_CONFIG_LINE_ORDER = [
    "APP_ENV=production",
    "DB_HOST=db.internal.example.com",
    "DB_PORT=5432",
    # API_KEY line will be at index 3
    "LOG_LEVEL=warn",
    "MAX_CONNECTIONS=50",
]


def get_today_date():
    """Return today's date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")


def compute_new_api_key():
    """
    Compute the new API key using:
    echo -n "rotate-$(date +%Y-%m-%d)-secret" | openssl dgst -sha256 -hmac "prod-salt"
    Returns the hex digest portion (after '= ').
    """
    today = get_today_date()
    input_string = f"rotate-{today}-secret"
    result = subprocess.run(
        ["openssl", "dgst", "-sha256", "-hmac", "prod-salt"],
        input=input_string.encode(),
        capture_output=True,
    )
    assert result.returncode == 0, (
        f"openssl command failed with returncode {result.returncode}. "
        f"stderr: {result.stderr.decode()}"
    )
    output = result.stdout.decode().strip()
    # Output format: "HMAC-SHA256(stdin)= <hex_digest>" or similar
    # Extract the part after '= '
    match = re.search(r'=\s+([0-9a-f]+)$', output)
    assert match is not None, (
        f"Could not parse hex digest from openssl output: '{output}'"
    )
    return match.group(1)


@pytest.fixture(scope="module")
def new_api_key():
    """Compute and cache the expected new API key for this test run."""
    return compute_new_api_key()


@pytest.fixture(scope="module")
def today():
    return get_today_date()


@pytest.fixture(scope="module")
def config_lines():
    with open(CONFIG_PATH, "r") as f:
        content = f.read()
    return content.splitlines()


@pytest.fixture(scope="module")
def log_lines():
    with open(LOG_PATH, "r") as f:
        content = f.read()
    return content.splitlines()


# ── Config file tests ─────────────────────────────────────────────────────────

def test_config_file_exists():
    assert os.path.isfile(CONFIG_PATH), (
        f"Config file not found at {CONFIG_PATH}. "
        "The file must exist after the rotation."
    )


def test_config_file_has_exactly_one_api_key_line(config_lines):
    api_key_lines = [l for l in config_lines if l.startswith("API_KEY=")]
    assert len(api_key_lines) == 1, (
        f"Expected exactly 1 line starting with 'API_KEY=' in {CONFIG_PATH}, "
        f"found {len(api_key_lines)}. Lines: {api_key_lines}"
    )


def test_config_file_api_key_value_equals_new_key(config_lines, new_api_key):
    api_key_lines = [l for l in config_lines if l.startswith("API_KEY=")]
    assert len(api_key_lines) == 1, (
        f"Expected exactly 1 API_KEY= line in {CONFIG_PATH}, "
        f"found {len(api_key_lines)}."
    )
    value = api_key_lines[0][len("API_KEY="):]
    assert value == new_api_key, (
        f"API_KEY value in {CONFIG_PATH} does not match the expected new key.\n"
        f"Expected: '{new_api_key}'\n"
        f"Got:      '{value}'\n"
        "The new key should be computed as: "
        "echo -n 'rotate-$(date +%Y-%m-%d)-secret' | openssl dgst -sha256 -hmac 'prod-salt' | awk '{print $2}'"
    )


def test_config_file_api_key_not_old_value(config_lines):
    api_key_lines = [l for l in config_lines if l.startswith("API_KEY=")]
    assert len(api_key_lines) == 1, (
        f"Expected exactly 1 API_KEY= line in {CONFIG_PATH}."
    )
    value = api_key_lines[0][len("API_KEY="):]
    assert value != OLD_API_KEY, (
        f"API_KEY in {CONFIG_PATH} still has the old value '{OLD_API_KEY}'. "
        "The rotation does not appear to have been performed."
    )


def test_config_file_api_key_no_quotes_or_spaces(config_lines):
    api_key_lines = [l for l in config_lines if l.startswith("API_KEY=")]
    assert len(api_key_lines) == 1
    line = api_key_lines[0]
    value = line[len("API_KEY="):]
    assert '"' not in value and "'" not in value, (
        f"API_KEY value in {CONFIG_PATH} must not contain quotes. "
        f"Got: '{value}'"
    )
    assert ' ' not in value, (
        f"API_KEY value in {CONFIG_PATH} must not contain spaces. "
        f"Got: '{value}'"
    )
    assert value == value.strip(), (
        f"API_KEY value in {CONFIG_PATH} must not have leading/trailing whitespace. "
        f"Got: '{value}'"
    )


def test_config_file_non_apikey_lines_unchanged(config_lines):
    non_api_lines = [l for l in config_lines if not l.startswith("API_KEY=")]
    assert non_api_lines == EXPECTED_NON_APIKEY_LINES, (
        f"Non-API_KEY lines in {CONFIG_PATH} were modified (must remain unchanged).\n"
        f"Expected: {EXPECTED_NON_APIKEY_LINES}\n"
        f"Got:      {non_api_lines}"
    )


def test_config_file_line_count(config_lines):
    assert len(config_lines) == 6, (
        f"Expected exactly 6 lines in {CONFIG_PATH}, found {len(config_lines)}.\n"
        f"Lines: {config_lines}"
    )


def test_config_file_line_order(config_lines, new_api_key):
    expected_lines = [
        "APP_ENV=production",
        "DB_HOST=db.internal.example.com",
        "DB_PORT=5432",
        f"API_KEY={new_api_key}",
        "LOG_LEVEL=warn",
        "MAX_CONNECTIONS=50",
    ]
    assert config_lines == expected_lines, (
        f"Config file lines do not match expected order/content.\n"
        f"Expected: {expected_lines}\n"
        f"Got:      {config_lines}"
    )


def test_config_file_api_key_line_format(config_lines, new_api_key):
    """The API_KEY line must be exactly 'API_KEY=<new_value>' with no extra chars."""
    api_key_lines = [l for l in config_lines if l.startswith("API_KEY=")]
    assert len(api_key_lines) == 1
    expected_line = f"API_KEY={new_api_key}"
    assert api_key_lines[0] == expected_line, (
        f"API_KEY line format is incorrect.\n"
        f"Expected: '{expected_line}'\n"
        f"Got:      '{api_key_lines[0]}'"
    )


# ── Rotation log tests ────────────────────────────────────────────────────────

def test_rotation_log_exists():
    assert os.path.isfile(LOG_PATH), (
        f"Rotation log not found at {LOG_PATH}. "
        "The file must exist after the rotation."
    )


def test_rotation_log_has_exactly_three_lines(log_lines):
    non_empty = [l for l in log_lines if l.strip()]
    assert len(non_empty) == 3, (
        f"Expected exactly 3 non-empty lines in {LOG_PATH}, "
        f"found {len(non_empty)}.\nContent:\n" + "\n".join(log_lines)
    )


def test_rotation_log_line1_unchanged(log_lines):
    assert len(log_lines) >= 1, f"{LOG_PATH} is empty."
    assert log_lines[0].rstrip() == EXPECTED_LOG_LINE_1, (
        f"Line 1 of {LOG_PATH} was modified (must remain unchanged).\n"
        f"Expected: '{EXPECTED_LOG_LINE_1}'\n"
        f"Got:      '{log_lines[0].rstrip()}'"
    )


def test_rotation_log_line2_unchanged(log_lines):
    assert len(log_lines) >= 2, (
        f"{LOG_PATH} has fewer than 2 lines."
    )
    assert log_lines[1].rstrip() == EXPECTED_LOG_LINE_2, (
        f"Line 2 of {LOG_PATH} was modified (must remain unchanged).\n"
        f"Expected: '{EXPECTED_LOG_LINE_2}'\n"
        f"Got:      '{log_lines[1].rstrip()}'"
    )


def test_rotation_log_line3_exists(log_lines):
    assert len(log_lines) >= 3, (
        f"Expected a 3rd line in {LOG_PATH} recording the new rotation, "
        f"but only {len(log_lines)} line(s) found.\nContent:\n" + "\n".join(log_lines)
    )


def test_rotation_log_line3_format(log_lines, today, new_api_key):
    assert len(log_lines) >= 3, (
        f"Line 3 is missing from {LOG_PATH}."
    )
    line3 = log_lines[2].rstrip()
    new_key_prefix = new_api_key[:8]
    expected_line3 = (
        f"ROTATED API_KEY on {today} "
        f"old={OLD_API_KEY_PREFIX} "
        f"new={new_key_prefix}"
    )
    assert line3 == expected_line3, (
        f"Line 3 of {LOG_PATH} does not match expected format.\n"
        f"Expected: '{expected_line3}'\n"
        f"Got:      '{line3}'\n"
        f"Note: today's date is '{today}', "
        f"old key prefix is '{OLD_API_KEY_PREFIX}', "
        f"new key prefix is '{new_key_prefix}'."
    )


def test_rotation_log_line3_date_is_today(log_lines, today):
    assert len(log_lines) >= 3, f"Line 3 is missing from {LOG_PATH}."
    line3 = log_lines[2].rstrip()
    assert today in line3, (
        f"Line 3 of {LOG_PATH} does not contain today's date '{today}'.\n"
        f"Got: '{line3}'"
    )


def test_rotation_log_line3_old_key_prefix(log_lines):
    assert len(log_lines) >= 3, f"Line 3 is missing from {LOG_PATH}."
    line3 = log_lines[2].rstrip()
    assert f"old={OLD_API_KEY_PREFIX}" in line3, (
        f"Line 3 of {LOG_PATH} does not contain the correct old key prefix.\n"
        f"Expected 'old={OLD_API_KEY_PREFIX}' in line.\n"
        f"Got: '{line3}'"
    )


def test_rotation_log_line3_new_key_prefix(log_lines, new_api_key):
    assert len(log_lines) >= 3, f"Line 3 is missing from {LOG_PATH}."
    line3 = log_lines[2].rstrip()
    new_key_prefix = new_api_key[:8]
    assert f"new={new_key_prefix}" in line3, (
        f"Line 3 of {LOG_PATH} does not contain the correct new key prefix.\n"
        f"Expected 'new={new_key_prefix}' in line.\n"
        f"Got: '{line3}'"
    )


def test_rotation_log_line3_starts_with_rotated_api_key(log_lines):
    assert len(log_lines) >= 3, f"Line 3 is missing from {LOG_PATH}."
    line3 = log_lines[2].rstrip()
    assert line3.startswith("ROTATED API_KEY on "), (
        f"Line 3 of {LOG_PATH} must start with 'ROTATED API_KEY on '.\n"
        f"Got: '{line3}'"
    )


def test_rotation_log_file_ends_with_newline():
    """The log file should end with a newline so wc -l counts correctly."""
    with open(LOG_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"The rotation log {LOG_PATH} does not end with a newline character. "
        "Please ensure the appended line ends with '\\n'."
    )


def test_config_file_ends_with_newline():
    """The config file should end with a newline."""
    with open(CONFIG_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"The config file {CONFIG_PATH} does not end with a newline character."
    )