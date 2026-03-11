# test_final_state.py

import os
import re
import pytest

REPORT_PATH = "/home/user/logs/triage_report.txt"
LOG_PATH = "/home/user/logs/production.log"

EXPECTED_CONTENT = """\
=== INCIDENT TRIAGE REPORT ===
Incident window: 2024-05-21T08:09:05 to 2024-05-21T09:03:55

--- Severity Breakdown ---
FATAL: 4
ERROR: 11
WARN: 6
INFO: 9

--- Affected Services (ERROR/FATAL only) ---
payment-service: 5
db-connector: 4
api-gateway: 3
auth-service: 3

--- Error Code Frequency ---
ERR-2201: 4
ERR-1042: 3
ERR-4031: 3
ERR-5001: 3
ERR-9900: 2

*** CRITICAL: payment-service has FATAL errors — escalate immediately ***
"""


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Triage report '{REPORT_PATH}' does not exist. "
        "The student must create this file as part of the task."
    )


def test_report_file_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Triage report '{REPORT_PATH}' is not readable."
    )


def test_report_exact_content():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        actual = f.read()

    assert actual == EXPECTED_CONTENT, (
        f"Triage report content does not match expected.\n"
        f"--- EXPECTED ---\n{EXPECTED_CONTENT!r}\n"
        f"--- ACTUAL ---\n{actual!r}"
    )


def test_report_ends_with_single_newline():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    assert content.endswith("\n"), (
        f"Triage report '{REPORT_PATH}' must end with a newline character."
    )
    assert not content.endswith("\n\n"), (
        f"Triage report '{REPORT_PATH}' must end with exactly ONE newline, not multiple."
    )


def test_report_no_trailing_spaces():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(" "), (
            f"Line {i} in '{REPORT_PATH}' has trailing spaces: {line!r}"
        )


def test_report_header_line():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    assert lines[0] == "=== INCIDENT TRIAGE REPORT ===", (
        f"First line of report is wrong.\n"
        f"  Expected: '=== INCIDENT TRIAGE REPORT ==='\n"
        f"  Actual:   {lines[0]!r}"
    )


def test_report_incident_window():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    assert lines[1] == "Incident window: 2024-05-21T08:09:05 to 2024-05-21T09:03:55", (
        f"Incident window line is wrong.\n"
        f"  Expected: 'Incident window: 2024-05-21T08:09:05 to 2024-05-21T09:03:55'\n"
        f"  Actual:   {lines[1]!r}"
    )


def test_report_severity_breakdown_section():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()

    # Find the severity breakdown section
    try:
        idx = lines.index("--- Severity Breakdown ---")
    except ValueError:
        pytest.fail("'--- Severity Breakdown ---' header not found in report.")

    expected_severity_lines = [
        "FATAL: 4",
        "ERROR: 11",
        "WARN: 6",
        "INFO: 9",
    ]

    for i, expected_line in enumerate(expected_severity_lines):
        actual_line = lines[idx + 1 + i]
        assert actual_line == expected_line, (
            f"Severity breakdown line {i+1} is wrong.\n"
            f"  Expected: {expected_line!r}\n"
            f"  Actual:   {actual_line!r}"
        )


def test_report_affected_services_section():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()

    try:
        idx = lines.index("--- Affected Services (ERROR/FATAL only) ---")
    except ValueError:
        pytest.fail("'--- Affected Services (ERROR/FATAL only) ---' header not found in report.")

    expected_service_lines = [
        "payment-service: 5",
        "db-connector: 4",
        "api-gateway: 3",
        "auth-service: 3",
    ]

    for i, expected_line in enumerate(expected_service_lines):
        actual_line = lines[idx + 1 + i]
        assert actual_line == expected_line, (
            f"Affected services line {i+1} is wrong.\n"
            f"  Expected: {expected_line!r}\n"
            f"  Actual:   {actual_line!r}"
        )


def test_report_error_code_frequency_section():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()

    try:
        idx = lines.index("--- Error Code Frequency ---")
    except ValueError:
        pytest.fail("'--- Error Code Frequency ---' header not found in report.")

    expected_error_lines = [
        "ERR-2201: 4",
        "ERR-1042: 3",
        "ERR-4031: 3",
        "ERR-5001: 3",
        "ERR-9900: 2",
    ]

    for i, expected_line in enumerate(expected_error_lines):
        actual_line = lines[idx + 1 + i]
        assert actual_line == expected_line, (
            f"Error code frequency line {i+1} is wrong.\n"
            f"  Expected: {expected_line!r}\n"
            f"  Actual:   {actual_line!r}"
        )


def test_report_critical_flag_section():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()

    expected_critical_line = (
        "*** CRITICAL: payment-service has FATAL errors \u2014 escalate immediately ***"
    )

    assert expected_critical_line in lines, (
        f"Critical flag line not found in report.\n"
        f"  Expected line: {expected_critical_line!r}\n"
        f"  Report lines: {lines}"
    )


def test_report_line_count():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    # Expected lines based on EXPECTED_CONTENT (without trailing empty line from splitlines)
    expected_lines = EXPECTED_CONTENT.splitlines()

    assert len(lines) == len(expected_lines), (
        f"Report has {len(lines)} lines, expected {len(expected_lines)} lines.\n"
        f"Actual lines: {lines}"
    )


def test_report_blank_lines_between_sections():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()

    # Line index 2 should be blank (after incident window line)
    assert lines[2] == "", (
        f"Expected blank line at position 3 (index 2), got: {lines[2]!r}"
    )

    # Find severity section and check blank line before it
    try:
        sev_idx = lines.index("--- Severity Breakdown ---")
        assert lines[sev_idx - 1] == "", (
            f"Expected blank line before '--- Severity Breakdown ---', "
            f"got: {lines[sev_idx - 1]!r}"
        )
    except ValueError:
        pytest.fail("'--- Severity Breakdown ---' not found.")

    # Find affected services section and check blank line before it
    try:
        svc_idx = lines.index("--- Affected Services (ERROR/FATAL only) ---")
        assert lines[svc_idx - 1] == "", (
            f"Expected blank line before '--- Affected Services (ERROR/FATAL only) ---', "
            f"got: {lines[svc_idx - 1]!r}"
        )
    except ValueError:
        pytest.fail("'--- Affected Services (ERROR/FATAL only) ---' not found.")

    # Find error code section and check blank line before it
    try:
        err_idx = lines.index("--- Error Code Frequency ---")
        assert lines[err_idx - 1] == "", (
            f"Expected blank line before '--- Error Code Frequency ---', "
            f"got: {lines[err_idx - 1]!r}"
        )
    except ValueError:
        pytest.fail("'--- Error Code Frequency ---' not found.")

    # Check blank line before critical flag
    critical_line = "*** CRITICAL: payment-service has FATAL errors \u2014 escalate immediately ***"
    try:
        crit_idx = lines.index(critical_line)
        assert lines[crit_idx - 1] == "", (
            f"Expected blank line before critical flag line, "
            f"got: {lines[crit_idx - 1]!r}"
        )
    except ValueError:
        pytest.fail(f"Critical flag line not found: {critical_line!r}")


def test_log_file_still_intact():
    """Ensure the original log file was not modified."""
    assert os.path.isfile(LOG_PATH), (
        f"Original log file '{LOG_PATH}' is missing — it must not be deleted."
    )

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    if lines and lines[-1] == "":
        lines = lines[:-1]

    assert len(lines) == 30, (
        f"Original log file '{LOG_PATH}' should have 30 lines, found {len(lines)}."
    )