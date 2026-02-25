# test_final_state.py

import os
import pytest

CSV_PATH = "/home/user/server_config/active_servers.csv"

# The exact expected contents for the CSV file, as per the truth data
EXPECTED_CSV_LINES = [
    "hostname,ip,interval",
    "web01,192.168.10.10,60",
    "db01,192.168.10.20,120",
    "cache01,192.168.10.40,45",
]

def test_active_servers_csv_exists():
    """Check that the active_servers.csv file exists at the correct location."""
    assert os.path.isfile(CSV_PATH), (
        f"The required report file was not found: {CSV_PATH}\n"
        "The summary report must be generated at this exact path."
    )

def test_active_servers_csv_contents_exact():
    """
    Check that the contents of the CSV file match the required output exactly:
    - Correct header
    - Three data lines (web01, db01, cache01) in the correct order
    - No extra or missing lines
    - No trailing spaces on any line
    """
    with open(CSV_PATH, encoding="utf-8") as f:
        lines = [line.rstrip() for line in f.readlines()]

    assert lines == EXPECTED_CSV_LINES, (
        f"The contents of {CSV_PATH} are incorrect.\n"
        f"--- Expected ---\n"
        f"{chr(10).join(EXPECTED_CSV_LINES)}\n"
        f"--- Actual ---\n"
        f"{chr(10).join(lines)}\n"
        "The report must:\n"
        "- Have exactly four lines: a header and three data rows (web01, db01, cache01),\n"
        "- Be in this order,\n"
        "- Contain no extra or missing lines,\n"
        "- Have no trailing spaces on any line."
    )

def test_active_servers_csv_no_trailing_blank_lines():
    """Ensure the CSV does not have any trailing blank lines."""
    with open(CSV_PATH, encoding="utf-8") as f:
        raw = f.read()
    assert not raw.endswith('\n\n'), (
        f"{CSV_PATH} has trailing blank lines at the end of the file.\n"
        "There must be exactly four lines (header + 3 data lines) with no blank lines at the end."
    )

def test_active_servers_csv_no_extra_columns():
    """Ensure there are exactly three columns in each row."""
    with open(CSV_PATH, encoding="utf-8") as f:
        lines = [line.rstrip() for line in f.readlines()]
    for idx, line in enumerate(lines):
        cols = line.split(',')
        assert len(cols) == 3, (
            f"Row {idx+1} of {CSV_PATH} does not have exactly three columns.\n"
            f"Row content: {line}\n"
            "Each row must have exactly: hostname,ip,interval"
        )

def test_active_servers_csv_header():
    """Ensure the header row is correct and appears only as the first line."""
    with open(CSV_PATH, encoding="utf-8") as f:
        lines = [line.rstrip() for line in f.readlines()]
    assert lines[0] == "hostname,ip,interval", (
        f"The first row of {CSV_PATH} must be the header: 'hostname,ip,interval'.\n"
        f"Actual first row: '{lines[0]}'"
    )
    for i, line in enumerate(lines[1:], 2):
        assert line != "hostname,ip,interval", (
            f"The header row 'hostname,ip,interval' appears again at line {i} in {CSV_PATH}.\n"
            "It must only be the first row."
        )