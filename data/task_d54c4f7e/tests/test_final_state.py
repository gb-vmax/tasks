# test_final_state.py

import os
import stat
import pytest

DATABASE_CONF = "/home/user/configs/database.conf"
AUDIT_LOG = "/home/user/configs/audit.log"

EXPECTED_SECOND_LINE = "PERMISSION_CHANGE: /home/user/configs/database.conf 664->640 by user"
EXPECTED_FIRST_LINE = "PERMISSION_CHANGE: /home/user/configs/nginx.conf 666->644 by user"


def test_database_conf_exists():
    assert os.path.isfile(DATABASE_CONF), (
        f"File {DATABASE_CONF} does not exist. "
        "The configuration file must be present after the task."
    )


def test_database_conf_permissions_are_640():
    file_stat = os.stat(DATABASE_CONF)
    actual_mode = stat.S_IMODE(file_stat.st_mode)
    expected_mode = 0o640
    assert actual_mode == expected_mode, (
        f"Permissions of {DATABASE_CONF} are wrong. "
        f"Expected 640 (octal), but got {oct(actual_mode).replace('0o', '')}. "
        "Owner should have read+write, group should have read-only, others should have no access."
    )


def test_database_conf_content_unchanged():
    with open(DATABASE_CONF, "r") as f:
        content = f.read()
    expected = "host=localhost\nport=5432\ndbname=production\nuser=admin\npassword=s3cr3t\n"
    assert content == expected, (
        f"Content of {DATABASE_CONF} was modified unexpectedly.\n"
        f"Expected: {repr(expected)}\n"
        f"Got: {repr(content)}"
    )


def test_audit_log_exists():
    assert os.path.isfile(AUDIT_LOG), (
        f"Audit log {AUDIT_LOG} does not exist. "
        "The audit log must be present after the task."
    )


def test_audit_log_has_exactly_two_lines():
    with open(AUDIT_LOG, "r") as f:
        content = f.read()
    lines = [line for line in content.rstrip("\n").split("\n") if line.strip()]
    assert len(lines) == 2, (
        f"Audit log {AUDIT_LOG} should have exactly 2 non-empty lines, "
        f"but found {len(lines)}.\n"
        f"Full content:\n{repr(content)}"
    )


def test_audit_log_first_line_preserved():
    with open(AUDIT_LOG, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    assert len(lines) >= 1, (
        f"Audit log {AUDIT_LOG} is empty or has no lines."
    )
    assert lines[0] == EXPECTED_FIRST_LINE, (
        f"First line of {AUDIT_LOG} was modified or is incorrect.\n"
        f"Expected: {repr(EXPECTED_FIRST_LINE)}\n"
        f"Got: {repr(lines[0])}\n"
        "The pre-existing entry must not be overwritten."
    )


def test_audit_log_second_line_is_correct():
    with open(AUDIT_LOG, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    assert len(lines) >= 2, (
        f"Audit log {AUDIT_LOG} does not have a second line. "
        f"Full content:\n{repr(content)}"
    )
    assert lines[1] == EXPECTED_SECOND_LINE, (
        f"Second line of {AUDIT_LOG} is incorrect.\n"
        f"Expected: {repr(EXPECTED_SECOND_LINE)}\n"
        f"Got: {repr(lines[1])}\n"
        "The appended audit entry must exactly match the required format."
    )


def test_audit_log_second_line_no_trailing_whitespace():
    with open(AUDIT_LOG, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    if len(lines) >= 2:
        line = lines[1]
        assert line == line.rstrip(), (
            f"Second line of {AUDIT_LOG} has trailing whitespace.\n"
            f"Got: {repr(line)}"
        )


def test_audit_log_ends_with_newline():
    with open(AUDIT_LOG, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"Audit log {AUDIT_LOG} does not end with a newline character. "
        f"Last bytes: {repr(content[-10:])}"
    )


def test_audit_log_full_content():
    with open(AUDIT_LOG, "r") as f:
        content = f.read()
    expected_content = (
        "PERMISSION_CHANGE: /home/user/configs/nginx.conf 666->644 by user\n"
        "PERMISSION_CHANGE: /home/user/configs/database.conf 664->640 by user\n"
    )
    assert content == expected_content, (
        f"Full content of {AUDIT_LOG} does not match expected.\n"
        f"Expected: {repr(expected_content)}\n"
        f"Got: {repr(content)}"
    )