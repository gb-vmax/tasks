# test_final_state.py

import os
import pytest

SUPPORT_DIR = "/home/user/support"
SUMMARY_REPORT_PATH = "/home/user/support/summary_report.txt"
TECHNICIAN_LOAD_PATH = "/home/user/support/technician_load.txt"

EXPECTED_SUMMARY_REPORT = """\
=== IT SUPPORT TICKET SUMMARY ===

--- Tickets by Category ---
7 network
7 software
6 hardware
5 access
5 email

--- Tickets by Technician ---
9 alice
7 bob
7 carol
7 dave

--- Tickets by Status ---
22 closed
5 open
3 pending

--- Top Error Codes ---
7 ERR_CRASH
7 ERR_TIMEOUT
6 ERR_DISK
5 ERR_AUTH
5 ERR_SMTP

--- Tickets by Priority ---
12 medium
9 high
9 low
"""

EXPECTED_TECHNICIAN_LOAD = """\
alice
bob
carol
dave
"""


# ── summary_report.txt ────────────────────────────────────────────────────────

def test_summary_report_exists():
    assert os.path.isfile(SUMMARY_REPORT_PATH), (
        f"Expected summary report to exist at {SUMMARY_REPORT_PATH}, but it does not."
    )


def test_summary_report_is_readable():
    assert os.access(SUMMARY_REPORT_PATH, os.R_OK), (
        f"Expected summary report at {SUMMARY_REPORT_PATH} to be readable, but it is not."
    )


def test_summary_report_exact_content():
    with open(SUMMARY_REPORT_PATH, "r", encoding="utf-8") as f:
        actual = f.read()
    assert actual == EXPECTED_SUMMARY_REPORT, (
        f"Content of {SUMMARY_REPORT_PATH} does not match expected.\n\n"
        f"--- EXPECTED (repr) ---\n{EXPECTED_SUMMARY_REPORT!r}\n\n"
        f"--- ACTUAL (repr) ---\n{actual!r}"
    )


def test_summary_report_header_line():
    with open(SUMMARY_REPORT_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert lines[0].rstrip("\n") == "=== IT SUPPORT TICKET SUMMARY ===", (
        f"First line of {SUMMARY_REPORT_PATH} is wrong.\n"
        f"Got: {lines[0]!r}"
    )


def test_summary_report_section_headers_present():
    with open(SUMMARY_REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    expected_headers = [
        "--- Tickets by Category ---",
        "--- Tickets by Technician ---",
        "--- Tickets by Status ---",
        "--- Top Error Codes ---",
        "--- Tickets by Priority ---",
    ]
    for header in expected_headers:
        assert header in content, (
            f"Section header {header!r} not found in {SUMMARY_REPORT_PATH}."
        )


def test_summary_report_category_section():
    with open(SUMMARY_REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    # Extract section
    start = content.find("--- Tickets by Category ---")
    end = content.find("--- Tickets by Technician ---")
    assert start != -1 and end != -1, "Could not locate 'Tickets by Category' section."
    section = content[start:end].strip()
    lines = section.splitlines()
    # Remove header line
    data_lines = lines[1:]
    expected = [
        "7 network",
        "7 software",
        "6 hardware",
        "5 access",
        "5 email",
    ]
    assert data_lines == expected, (
        f"'Tickets by Category' section data lines are wrong.\n"
        f"Expected: {expected}\n"
        f"Got:      {data_lines}"
    )


def test_summary_report_technician_section():
    with open(SUMMARY_REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    start = content.find("--- Tickets by Technician ---")
    end = content.find("--- Tickets by Status ---")
    assert start != -1 and end != -1, "Could not locate 'Tickets by Technician' section."
    section = content[start:end].strip()
    lines = section.splitlines()
    data_lines = lines[1:]
    expected = [
        "9 alice",
        "7 bob",
        "7 carol",
        "7 dave",
    ]
    assert data_lines == expected, (
        f"'Tickets by Technician' section data lines are wrong.\n"
        f"Expected: {expected}\n"
        f"Got:      {data_lines}"
    )


def test_summary_report_status_section():
    with open(SUMMARY_REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    start = content.find("--- Tickets by Status ---")
    end = content.find("--- Top Error Codes ---")
    assert start != -1 and end != -1, "Could not locate 'Tickets by Status' section."
    section = content[start:end].strip()
    lines = section.splitlines()
    data_lines = lines[1:]
    expected = [
        "22 closed",
        "5 open",
        "3 pending",
    ]
    assert data_lines == expected, (
        f"'Tickets by Status' section data lines are wrong.\n"
        f"Expected: {expected}\n"
        f"Got:      {data_lines}"
    )


def test_summary_report_error_codes_section():
    with open(SUMMARY_REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    start = content.find("--- Top Error Codes ---")
    end = content.find("--- Tickets by Priority ---")
    assert start != -1 and end != -1, "Could not locate 'Top Error Codes' section."
    section = content[start:end].strip()
    lines = section.splitlines()
    data_lines = lines[1:]
    expected = [
        "7 ERR_CRASH",
        "7 ERR_TIMEOUT",
        "6 ERR_DISK",
        "5 ERR_AUTH",
        "5 ERR_SMTP",
    ]
    assert data_lines == expected, (
        f"'Top Error Codes' section data lines are wrong.\n"
        f"Expected: {expected}\n"
        f"Got:      {data_lines}"
    )


def test_summary_report_priority_section():
    with open(SUMMARY_REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    start = content.find("--- Tickets by Priority ---")
    assert start != -1, "Could not locate 'Tickets by Priority' section."
    section = content[start:].strip()
    lines = section.splitlines()
    data_lines = lines[1:]
    expected = [
        "12 medium",
        "9 high",
        "9 low",
    ]
    assert data_lines == expected, (
        f"'Tickets by Priority' section data lines are wrong.\n"
        f"Expected: {expected}\n"
        f"Got:      {data_lines}"
    )


def test_summary_report_ends_with_newline():
    with open(SUMMARY_REPORT_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"{SUMMARY_REPORT_PATH} must end with a newline character."
    )


def test_summary_report_no_trailing_blank_line():
    with open(SUMMARY_REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    # After stripping the final newline, there should be no trailing blank line
    stripped = content.rstrip("\n")
    assert not stripped.endswith("\n"), (
        f"{SUMMARY_REPORT_PATH} must not have a trailing blank line before the final newline."
    )


def test_summary_report_blank_lines_between_sections():
    """Check that blank lines appear between sections as required."""
    with open(SUMMARY_REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    # After the main header there should be a blank line
    assert "\n\n--- Tickets by Category ---" in content, (
        "Expected a blank line between the main header and 'Tickets by Category' section."
    )
    assert "\n\n--- Tickets by Technician ---" in content, (
        "Expected a blank line between 'Tickets by Category' and 'Tickets by Technician' sections."
    )
    assert "\n\n--- Tickets by Status ---" in content, (
        "Expected a blank line between 'Tickets by Technician' and 'Tickets by Status' sections."
    )
    assert "\n\n--- Top Error Codes ---" in content, (
        "Expected a blank line between 'Tickets by Status' and 'Top Error Codes' sections."
    )
    assert "\n\n--- Tickets by Priority ---" in content, (
        "Expected a blank line between 'Top Error Codes' and 'Tickets by Priority' sections."
    )


# ── technician_load.txt ───────────────────────────────────────────────────────

def test_technician_load_exists():
    assert os.path.isfile(TECHNICIAN_LOAD_PATH), (
        f"Expected technician load file to exist at {TECHNICIAN_LOAD_PATH}, but it does not."
    )


def test_technician_load_is_readable():
    assert os.access(TECHNICIAN_LOAD_PATH, os.R_OK), (
        f"Expected technician load file at {TECHNICIAN_LOAD_PATH} to be readable, but it is not."
    )


def test_technician_load_exact_content():
    with open(TECHNICIAN_LOAD_PATH, "r", encoding="utf-8") as f:
        actual = f.read()
    assert actual == EXPECTED_TECHNICIAN_LOAD, (
        f"Content of {TECHNICIAN_LOAD_PATH} does not match expected.\n\n"
        f"--- EXPECTED (repr) ---\n{EXPECTED_TECHNICIAN_LOAD!r}\n\n"
        f"--- ACTUAL (repr) ---\n{actual!r}"
    )


def test_technician_load_order():
    with open(TECHNICIAN_LOAD_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines() if line.strip()]
    expected_order = ["alice", "bob", "carol", "dave"]
    assert lines == expected_order, (
        f"Technician order in {TECHNICIAN_LOAD_PATH} is wrong.\n"
        f"Expected: {expected_order}\n"
        f"Got:      {lines}"
    )


def test_technician_load_no_counts():
    with open(TECHNICIAN_LOAD_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines() if line.strip()]
    for line in lines:
        parts = line.split()
        assert len(parts) == 1, (
            f"Each line in {TECHNICIAN_LOAD_PATH} should contain only the technician name "
            f"(no counts), but found: {line!r}"
        )


def test_technician_load_ends_with_newline():
    with open(TECHNICIAN_LOAD_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"{TECHNICIAN_LOAD_PATH} must end with a final newline character."
    )


def test_technician_load_four_entries():
    with open(TECHNICIAN_LOAD_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines() if line.strip()]
    assert len(lines) == 4, (
        f"Expected 4 technician names in {TECHNICIAN_LOAD_PATH}, but found {len(lines)}.\n"
        f"Lines: {lines}"
    )