# test_final_state.py

import os
import pwd
import stat
import pytest
import re

HOME = '/home/user'
DEPLOY_DIR = os.path.join(HOME, 'deployments', 'analytics-app')
ENV_FILE = os.path.join(DEPLOY_DIR, '.env')
LOG_FILE = os.path.join(DEPLOY_DIR, 'deploy.log')
USER = 'user'

ENV_KEYS = [
    "APP_VERSION",
    "DATABASE_URL",
    "ENABLE_CACHE",
    "LOG_LEVEL",
    "DEPLOY_TIMESTAMP",
]

ENV_EXPECTED = {
    "APP_VERSION": "3.8.2",
    "DATABASE_URL": "postgresql://analytics:Password123@db.internal:5432/analyticsdb",
    "ENABLE_CACHE": "true",
    "LOG_LEVEL": "info",
    # DEPLOY_TIMESTAMP checked for ISO8601 value, not hardcoded
}

LOG_LINE_TEMPLATE = r"^\[DEPLOYED\] ({iso8601}) - version 3.8.2 deployed by user$"
ISO8601_REGEX = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z"


def get_uid_gid_for_user(username):
    try:
        pw = pwd.getpwnam(username)
        return pw.pw_uid, pw.pw_gid
    except KeyError:
        pytest.skip(f"User '{username}' does not exist on this system.")


def file_owner(path):
    statinfo = os.stat(path)
    uid, gid = statinfo.st_uid, statinfo.st_gid
    return uid, gid


def is_readable_writable_by_user(path, username):
    uid, gid = get_uid_gid_for_user(username)
    st = os.stat(path)
    # Check user permissions
    if st.st_uid == uid:
        return bool(st.st_mode & stat.S_IRUSR) and bool(st.st_mode & stat.S_IWUSR)
    # Check group permissions
    if st.st_gid == gid:
        return bool(st.st_mode & stat.S_IRGRP) and bool(st.st_mode & stat.S_IWGRP)
    # Otherwise, check others
    return bool(st.st_mode & stat.S_IROTH) and bool(st.st_mode & stat.S_IWOTH)


def is_executable_by_anyone(path):
    st = os.stat(path)
    return bool(st.st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))


def read_file_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f.readlines()]


def read_file_content(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def parse_env_file(lines):
    result = {}
    for line in lines:
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        result[k.strip()] = v.strip()
    return result


def test_deploy_dir_exists_and_owned_by_user():
    assert os.path.isdir(DEPLOY_DIR), (
        f"Directory {DEPLOY_DIR} does not exist or is not a directory."
    )
    uid, gid = file_owner(DEPLOY_DIR)
    user_uid, user_gid = get_uid_gid_for_user(USER)
    assert uid == user_uid, (
        f"Directory {DEPLOY_DIR} is not owned by user '{USER}' (uid={user_uid})."
    )


def test_env_file_exists_and_content():
    assert os.path.isfile(ENV_FILE), (
        f".env file does not exist at {ENV_FILE}."
    )
    lines = read_file_lines(ENV_FILE)
    assert len(lines) == 5, (
        f".env file at {ENV_FILE} should have exactly 5 lines, found {len(lines)}"
    )
    env = parse_env_file(lines)
    for k in ENV_KEYS:
        assert k in env, (
            f"Key '{k}' missing from {ENV_FILE}."
        )
    for k in ENV_EXPECTED:
        assert env[k] == ENV_EXPECTED[k], (
            f"Key '{k}' in {ENV_FILE} has value '{env[k]}', expected '{ENV_EXPECTED[k]}'."
        )

    dep_ts = env["DEPLOY_TIMESTAMP"]
    assert re.fullmatch(ISO8601_REGEX, dep_ts), (
        f"DEPLOY_TIMESTAMP '{dep_ts}' in {ENV_FILE} is not in ISO8601 UTC format (e.g. 2024-06-12T12:15:00Z)."
    )


def test_env_file_permissions():
    assert is_readable_writable_by_user(ENV_FILE, USER), (
        f".env file at {ENV_FILE} is not readable and writable by user '{USER}'."
    )
    assert not is_executable_by_anyone(ENV_FILE), (
        f".env file at {ENV_FILE} must not be executable by anyone."
    )


def test_deploy_log_exists_and_content():
    assert os.path.isfile(LOG_FILE), (
        f"deploy.log file does not exist at {LOG_FILE}."
    )
    log_lines = read_file_lines(LOG_FILE)
    assert len(log_lines) == 1, (
        f"deploy.log at {LOG_FILE} must contain exactly one line, found {len(log_lines)}."
    )
    log_line = log_lines[0]

    # Extract DEPLOY_TIMESTAMP from .env for matching
    env_lines = read_file_lines(ENV_FILE)
    env = parse_env_file(env_lines)
    dep_ts = env["DEPLOY_TIMESTAMP"]

    expected_log_line = f"[DEPLOYED] {dep_ts} - version 3.8.2 deployed by user"
    assert log_line == expected_log_line, (
        f"deploy.log line mismatch.\nExpected: {expected_log_line}\nFound:    {log_line}"
    )


def test_deploy_log_permissions():
    assert is_readable_writable_by_user(LOG_FILE, USER), (
        f"deploy.log at {LOG_FILE} is not readable and writable by user '{USER}'."
    )
    assert not is_executable_by_anyone(LOG_FILE), (
        f"deploy.log at {LOG_FILE} must not be executable by anyone."
    )


def test_terminal_output_exact(monkeypatch):
    """
    The agent must print, in order:
      1. The .env file content (with each variable on a new line, in the correct order and with DEPLOY_TIMESTAMP value).
      2. The full path: /home/user/deployments/analytics-app/deploy.log
      3. The content of deploy.log (the correct single line).
    No extra lines or messages.
    """
    # The agent should have written the output to stdout.
    # We'll assume the agent's output is logged to a file for testability,
    # e.g., /tmp/agent_terminal_output.txt (since pytest can't capture the agent's prior output).
    # If not, this test must be adapted to your environment.
    # Here, we check the output as if it is in os.environ["AGENT_OUTPUT"]
    output_path = os.environ.get("AGENT_OUTPUT_PATH", "/tmp/agent_terminal_output.txt")
    if not os.path.isfile(output_path):
        pytest.skip("No agent terminal output found to verify (expected at /tmp/agent_terminal_output.txt or $AGENT_OUTPUT_PATH).")

    with open(output_path, "r", encoding="utf-8") as f:
        output = f.read()
    actual_lines = [line.rstrip("\n") for line in output.splitlines()]

    # Compose expected lines
    env_lines = read_file_lines(ENV_FILE)
    log_lines = read_file_lines(LOG_FILE)
    expected_lines = env_lines + [LOG_FILE] + log_lines

    assert actual_lines == expected_lines, (
        "Terminal output does not match the required format.\n"
        "Expected output:\n"
        f"{chr(10).join(expected_lines)}\n"
        "Actual output:\n"
        f"{chr(10).join(actual_lines)}"
    )