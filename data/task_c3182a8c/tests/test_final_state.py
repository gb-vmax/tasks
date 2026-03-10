# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/diagnostics/report.txt"
DIAGNOSTICS_DIR = "/home/user/diagnostics"

EXPECTED_LINES = [
    "=== DIAGNOSTICS REPORT ===",
    "Host: db.internal.example.com",
    "Port: 5432",
    "Log Level: WARNING",
    "Log File: /var/log/app/app.log",
    "Max Workers: 8",
    "Debug Mode: false",
]


def test_diagnostics_directory_exists():
    assert os.path.isdir(DIAGNOSTICS_DIR), (
        f"The diagnostics directory '{DIAGNOSTICS_DIR}' does not exist. "
        "The student must create this directory as part of the task."
    )


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"The report file '{REPORT_PATH}' does not exist. "
        "The student must create this file as part of the task."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"The report file '{REPORT_PATH}' exists but is not readable."
    )


def test_report_has_exactly_7_lines():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    # Split on newlines; file should end with a single newline giving 7 non-empty lines
    lines = content.splitlines()
    assert len(lines) == 7, (
        f"Expected exactly 7 lines in '{REPORT_PATH}', but found {len(lines)}. "
        f"Actual content:\n{content!r}"
    )


def test_report_is_newline_terminated():
    with open(REPORT_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"The report file '{REPORT_PATH}' must end with a newline character. "
        f"Last bytes: {content[-4:]!r}"
    )


def test_report_no_trailing_spaces():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} in '{REPORT_PATH}' has trailing whitespace: {line!r}"
        )


def test_report_line_1_header():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert lines[0] == EXPECTED_LINES[0], (
        f"Line 1 mismatch in '{REPORT_PATH}'.\n"
        f"  Expected: {EXPECTED_LINES[0]!r}\n"
        f"  Got:      {lines[0]!r}"
    )


def test_report_line_2_host():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert lines[1] == EXPECTED_LINES[1], (
        f"Line 2 mismatch in '{REPORT_PATH}'.\n"
        f"  Expected: {EXPECTED_LINES[1]!r}\n"
        f"  Got:      {lines[1]!r}\n"
        "Hint: 'Host' should come from the [database] section, "
        "not [server] or [cache]."
    )


def test_report_line_3_port():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert lines[2] == EXPECTED_LINES[2], (
        f"Line 3 mismatch in '{REPORT_PATH}'.\n"
        f"  Expected: {EXPECTED_LINES[2]!r}\n"
        f"  Got:      {lines[2]!r}\n"
        "Hint: 'Port' should come from the [database] section (5432), "
        "not [server] (8080) or [cache] (6379)."
    )


def test_report_line_4_log_level():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert lines[3] == EXPECTED_LINES[3], (
        f"Line 4 mismatch in '{REPORT_PATH}'.\n"
        f"  Expected: {EXPECTED_LINES[3]!r}\n"
        f"  Got:      {lines[3]!r}\n"
        "Hint: 'Log Level' should come from the 'level' key in [logging] section."
    )


def test_report_line_5_log_file():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert lines[4] == EXPECTED_LINES[4], (
        f"Line 5 mismatch in '{REPORT_PATH}'.\n"
        f"  Expected: {EXPECTED_LINES[4]!r}\n"
        f"  Got:      {lines[4]!r}\n"
        "Hint: 'Log File' should come from the 'file' key in [logging] section."
    )


def test_report_line_6_max_workers():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert lines[5] == EXPECTED_LINES[5], (
        f"Line 6 mismatch in '{REPORT_PATH}'.\n"
        f"  Expected: {EXPECTED_LINES[5]!r}\n"
        f"  Got:      {lines[5]!r}\n"
        "Hint: 'Max Workers' should come from the 'max_workers' key in [server] section."
    )


def test_report_line_7_debug_mode():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert lines[6] == EXPECTED_LINES[6], (
        f"Line 7 mismatch in '{REPORT_PATH}'.\n"
        f"  Expected: {EXPECTED_LINES[6]!r}\n"
        f"  Got:      {lines[6]!r}\n"
        "Hint: 'Debug Mode' should come from the 'debug' key in [server] section."
    )


def test_report_exact_full_content():
    expected_content = "\n".join(EXPECTED_LINES) + "\n"
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()
    assert actual_content == expected_content, (
        f"The full content of '{REPORT_PATH}' does not match expected.\n"
        f"  Expected: {expected_content!r}\n"
        f"  Got:      {actual_content!r}"
    )