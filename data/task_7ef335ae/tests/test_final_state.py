# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/diagnostics/report.txt"
DIAGNOSTICS_DIR = "/home/user/diagnostics"

EXPECTED_CONTENT = """\
=== DIAGNOSTIC REPORT ===

[SERVICE]
name: auth-service
version: 2.4.1
environment: production

[DATABASE]
host: db-primary.internal
port: 5432

[SERVER]
host: 0.0.0.0
port: 8080
timeout: 30

[LOGGING]
level: warn
file: /var/log/app/app.log
"""

EXPECTED_LINES = [
    "=== DIAGNOSTIC REPORT ===",  # line 1
    "",                            # line 2 (blank)
    "[SERVICE]",                   # line 3
    "name: auth-service",          # line 4
    "version: 2.4.1",              # line 5
    "environment: production",     # line 6
    "",                            # line 7 (blank)
    "[DATABASE]",                  # line 8
    "host: db-primary.internal",   # line 9
    "port: 5432",                  # line 10
    "",                            # line 11 (blank)
    "[SERVER]",                    # line 12
    "host: 0.0.0.0",               # line 13
    "port: 8080",                  # line 14
    "timeout: 30",                 # line 15
    "",                            # line 16 (blank)
    "[LOGGING]",                   # line 17
    "level: warn",                 # line 18
    "file: /var/log/app/app.log",  # line 19
]


def test_diagnostics_directory_exists():
    assert os.path.isdir(DIAGNOSTICS_DIR), (
        f"Directory '{DIAGNOSTICS_DIR}' does not exist. "
        "The diagnostics directory must be created as part of the task."
    )


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The diagnostics report must be created as part of the task."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file '{REPORT_PATH}' is not readable."
    )


def test_report_exact_content():
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    assert actual_content == EXPECTED_CONTENT, (
        f"Report file content does not match expected.\n"
        f"Expected:\n{repr(EXPECTED_CONTENT)}\n"
        f"Actual:\n{repr(actual_content)}"
    )


def test_report_ends_with_single_newline():
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    assert actual_content.endswith("\n"), (
        f"Report file '{REPORT_PATH}' must end with a newline character."
    )
    assert not actual_content.endswith("\n\n"), (
        f"Report file '{REPORT_PATH}' must end with exactly one newline, "
        "not multiple trailing newlines."
    )


def test_report_line_count():
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    # Split by lines; the trailing newline means splitlines gives 19 lines
    lines = actual_content.splitlines()
    assert len(lines) == 19, (
        f"Expected 19 lines (excluding the trailing newline), "
        f"but got {len(lines)} lines.\n"
        f"Actual content:\n{repr(actual_content)}"
    )


def test_report_line_by_line():
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    actual_lines = actual_content.splitlines()

    assert len(actual_lines) == len(EXPECTED_LINES), (
        f"Expected {len(EXPECTED_LINES)} lines but got {len(actual_lines)}.\n"
        f"Actual lines: {actual_lines}"
    )

    for i, (expected_line, actual_line) in enumerate(zip(EXPECTED_LINES, actual_lines), start=1):
        assert actual_line == expected_line, (
            f"Line {i} mismatch.\n"
            f"Expected: {repr(expected_line)}\n"
            f"Actual:   {repr(actual_line)}"
        )


def test_no_trailing_spaces_on_any_line():
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    lines = actual_content.splitlines()
    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} has trailing whitespace: {repr(line)}"
        )


def test_header_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert lines[0] == "=== DIAGNOSTIC REPORT ===", (
        f"Line 1 should be '=== DIAGNOSTIC REPORT ===' but got: {repr(lines[0])}"
    )


def test_blank_line_after_header():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert lines[1] == "", (
        f"Line 2 should be blank but got: {repr(lines[1])}"
    )


def test_service_section():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert lines[2] == "[SERVICE]", (
        f"Line 3 should be '[SERVICE]' but got: {repr(lines[2])}"
    )
    assert lines[3] == "name: auth-service", (
        f"Line 4 should be 'name: auth-service' but got: {repr(lines[3])}"
    )
    assert lines[4] == "version: 2.4.1", (
        f"Line 5 should be 'version: 2.4.1' but got: {repr(lines[4])}"
    )
    assert lines[5] == "environment: production", (
        f"Line 6 should be 'environment: production' but got: {repr(lines[5])}"
    )


def test_database_section():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert lines[6] == "", (
        f"Line 7 should be blank but got: {repr(lines[6])}"
    )
    assert lines[7] == "[DATABASE]", (
        f"Line 8 should be '[DATABASE]' but got: {repr(lines[7])}"
    )
    assert lines[8] == "host: db-primary.internal", (
        f"Line 9 should be 'host: db-primary.internal' but got: {repr(lines[8])}"
    )
    assert lines[9] == "port: 5432", (
        f"Line 10 should be 'port: 5432' but got: {repr(lines[9])}"
    )


def test_server_section():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert lines[10] == "", (
        f"Line 11 should be blank but got: {repr(lines[10])}"
    )
    assert lines[11] == "[SERVER]", (
        f"Line 12 should be '[SERVER]' but got: {repr(lines[11])}"
    )
    assert lines[12] == "host: 0.0.0.0", (
        f"Line 13 should be 'host: 0.0.0.0' (no quotes) but got: {repr(lines[12])}"
    )
    assert lines[13] == "port: 8080", (
        f"Line 14 should be 'port: 8080' but got: {repr(lines[13])}"
    )
    assert lines[14] == "timeout: 30", (
        f"Line 15 should be 'timeout: 30' but got: {repr(lines[14])}"
    )


def test_logging_section():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert lines[15] == "", (
        f"Line 16 should be blank but got: {repr(lines[15])}"
    )
    assert lines[16] == "[LOGGING]", (
        f"Line 17 should be '[LOGGING]' but got: {repr(lines[16])}"
    )
    assert lines[17] == "level: warn", (
        f"Line 18 should be 'level: warn' (no quotes) but got: {repr(lines[17])}"
    )
    assert lines[18] == "file: /var/log/app/app.log", (
        f"Line 19 should be 'file: /var/log/app/app.log' (no quotes) but got: {repr(lines[18])}"
    )


def test_no_quoted_values():
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    # Ensure no quoted values appear in the report
    assert '"0.0.0.0"' not in actual_content, (
        "Value '0.0.0.0' should not be quoted in the report."
    )
    assert '"warn"' not in actual_content, (
        "Value 'warn' should not be quoted in the report."
    )
    assert '"/var/log/app/app.log"' not in actual_content, (
        "Value '/var/log/app/app.log' should not be quoted in the report."
    )


def test_section_separators_are_single_blank_lines():
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    # There should be no double blank lines (two consecutive blank lines)
    assert "\n\n\n" not in actual_content, (
        "There should be no double blank lines (more than one consecutive blank line) "
        "in the report file."
    )