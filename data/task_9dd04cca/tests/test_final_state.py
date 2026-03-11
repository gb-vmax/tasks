# test_final_state.py

import os
import pytest

ACTIVE_SERVERS_PATH = "/home/user/servers/active_servers.txt"
SERVERS_DIR = "/home/user/servers"

EXPECTED_LINES = [
    "[webserver01] 10.0.1.5 (web)",
    "[appserver01] 10.0.3.15 (application)",
    "[webserver02] 10.0.1.6 (web)",
    "[dbserver02] 10.0.2.11 (database)",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES) + "\n"

EXCLUDED_HOSTNAMES = ["dbserver01", "cacheserver01", "monserver01"]


def test_servers_directory_exists():
    assert os.path.isdir(SERVERS_DIR), (
        f"Directory '{SERVERS_DIR}' does not exist. "
        "The servers directory must be present."
    )


def test_active_servers_file_exists():
    assert os.path.isfile(ACTIVE_SERVERS_PATH), (
        f"File '{ACTIVE_SERVERS_PATH}' does not exist. "
        "The output file must be created by the task."
    )


def test_active_servers_file_is_readable():
    assert os.access(ACTIVE_SERVERS_PATH, os.R_OK), (
        f"File '{ACTIVE_SERVERS_PATH}' is not readable."
    )


def test_active_servers_exact_content():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        content = f.read()

    assert content == EXPECTED_CONTENT, (
        f"File '{ACTIVE_SERVERS_PATH}' does not have the expected content.\n"
        f"Expected (repr):\n{repr(EXPECTED_CONTENT)}\n\n"
        f"Got (repr):\n{repr(content)}"
    )


def test_active_servers_line_count():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        lines = [line for line in f.read().splitlines() if line.strip()]

    assert len(lines) == 4, (
        f"Expected exactly 4 non-empty lines in '{ACTIVE_SERVERS_PATH}', "
        f"but found {len(lines)} lines.\nLines found:\n" + "\n".join(lines)
    )


def test_active_servers_no_header():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")

    assert first_line != "hostname,ip_address,role,status,os", (
        f"The first line of '{ACTIVE_SERVERS_PATH}' should NOT be a header line, "
        f"but got: '{first_line}'"
    )

    # Also check it doesn't start with 'hostname'
    assert not first_line.startswith("hostname"), (
        f"The first line of '{ACTIVE_SERVERS_PATH}' looks like a header: '{first_line}'. "
        "No header should be present in the output file."
    )


def test_active_servers_correct_order():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    assert lines == EXPECTED_LINES, (
        f"Lines in '{ACTIVE_SERVERS_PATH}' are not in the correct order.\n"
        f"Expected:\n" + "\n".join(EXPECTED_LINES) + "\n\n"
        f"Got:\n" + "\n".join(lines)
    )


def test_active_servers_line_format():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    import re
    pattern = re.compile(r'^\[.+\] \S+ \(.+\)$')

    for i, line in enumerate(lines, 1):
        assert pattern.match(line), (
            f"Line {i} in '{ACTIVE_SERVERS_PATH}' does not match the expected format "
            f"'[<hostname>] <ip_address> (<role>)'.\n"
            f"Got: '{line}'"
        )


def test_active_servers_contains_webserver01():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        content = f.read()

    expected_line = "[webserver01] 10.0.1.5 (web)"
    assert expected_line in content, (
        f"Expected line '{expected_line}' not found in '{ACTIVE_SERVERS_PATH}'.\n"
        f"File contents:\n{content}"
    )


def test_active_servers_contains_appserver01():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        content = f.read()

    expected_line = "[appserver01] 10.0.3.15 (application)"
    assert expected_line in content, (
        f"Expected line '{expected_line}' not found in '{ACTIVE_SERVERS_PATH}'.\n"
        f"File contents:\n{content}"
    )


def test_active_servers_contains_webserver02():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        content = f.read()

    expected_line = "[webserver02] 10.0.1.6 (web)"
    assert expected_line in content, (
        f"Expected line '{expected_line}' not found in '{ACTIVE_SERVERS_PATH}'.\n"
        f"File contents:\n{content}"
    )


def test_active_servers_contains_dbserver02():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        content = f.read()

    expected_line = "[dbserver02] 10.0.2.11 (database)"
    assert expected_line in content, (
        f"Expected line '{expected_line}' not found in '{ACTIVE_SERVERS_PATH}'.\n"
        f"File contents:\n{content}"
    )


def test_excluded_servers_not_present():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        content = f.read()

    for hostname in EXCLUDED_HOSTNAMES:
        assert hostname not in content, (
            f"Server '{hostname}' should NOT appear in '{ACTIVE_SERVERS_PATH}' "
            f"(it is not active), but it was found in the file.\n"
            f"File contents:\n{content}"
        )


def test_no_os_column_in_output():
    os_values = ["Ubuntu", "CentOS", "Debian"]

    with open(ACTIVE_SERVERS_PATH, "r") as f:
        content = f.read()

    for os_val in os_values:
        assert os_val not in content, (
            f"OS value '{os_val}' should NOT appear in '{ACTIVE_SERVERS_PATH}' "
            f"(the os column must be omitted), but it was found.\n"
            f"File contents:\n{content}"
        )


def test_no_status_column_in_output():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        content = f.read()

    # The word 'active' as a standalone CSV field should not appear
    # Check that lines don't contain comma-separated fields
    lines = [line.rstrip("\n") for line in content.splitlines() if line.strip()]
    for i, line in enumerate(lines, 1):
        assert "," not in line, (
            f"Line {i} in '{ACTIVE_SERVERS_PATH}' contains a comma, which suggests "
            f"CSV formatting rather than the required plain-text format.\n"
            f"Got: '{line}'"
        )


def test_no_trailing_blank_lines():
    with open(ACTIVE_SERVERS_PATH, "r") as f:
        content = f.read()

    # The file should end with exactly one newline after the last line
    assert not content.endswith("\n\n"), (
        f"File '{ACTIVE_SERVERS_PATH}' has trailing blank lines. "
        f"It should end with a single newline after the last data line.\n"
        f"File ends with (repr): {repr(content[-10:])}"
    )

    assert content.endswith("\n"), (
        f"File '{ACTIVE_SERVERS_PATH}' should end with a newline character.\n"
        f"File ends with (repr): {repr(content[-10:])}"
    )