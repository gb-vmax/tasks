# test_final_state.py

import os
import pytest

TICKET_TITLES_PATH = "/home/user/ticket_titles.txt"
TICKET_FREQUENCY_REPORT_PATH = "/home/user/ticket_frequency_report.txt"

# The expected content of the ticket frequency report, as per the task description.
EXPECTED_REPORT_CONTENT = """3 Cannot connect to VPN
2 Printer not working
1 Forgot password
1 Software installation request
"""

@pytest.mark.describe("Final state: ticket_frequency_report.txt exists and is correct")
def test_ticket_frequency_report_exists():
    assert os.path.isfile(TICKET_FREQUENCY_REPORT_PATH), (
        f"Missing required report file: {TICKET_FREQUENCY_REPORT_PATH}. "
        "You must create this file as described in the task."
    )

@pytest.mark.describe("Final state: ticket_frequency_report.txt contents are exactly correct")
def test_ticket_frequency_report_content():
    if not os.path.isfile(TICKET_FREQUENCY_REPORT_PATH):
        pytest.skip(f"{TICKET_FREQUENCY_REPORT_PATH} does not exist, so content cannot be checked.")

    with open(TICKET_FREQUENCY_REPORT_PATH, "r", encoding="utf-8") as f:
        actual_content = f.read()

    # Compare lines, ignoring trailing newlines, but enforcing exact line order and content.
    expected_lines = EXPECTED_REPORT_CONTENT.strip().splitlines()
    actual_lines = actual_content.strip().splitlines()

    # Check number of lines
    assert len(actual_lines) == len(expected_lines), (
        f"The report at {TICKET_FREQUENCY_REPORT_PATH} has {len(actual_lines)} lines; "
        f"expected {len(expected_lines)} lines.\n"
        f"Expected lines:\n{EXPECTED_REPORT_CONTENT}\n\n"
        f"Actual lines:\n{actual_content}"
    )

    # Check each line for exact match
    for i, (expected, actual) in enumerate(zip(expected_lines, actual_lines), 1):
        assert actual == expected, (
            f"Line {i} in {TICKET_FREQUENCY_REPORT_PATH} is incorrect.\n"
            f"Expected: '{expected}'\n"
            f"Found:    '{actual}'\n"
            "Ensure counts and titles are correct, lines are sorted by count (descending), "
            "and ties are broken lexicographically (case sensitive)."
        )

@pytest.mark.describe("Final state: ticket_frequency_report.txt does not contain extra lines")
def test_ticket_frequency_report_no_extra_lines():
    with open(TICKET_FREQUENCY_REPORT_PATH, "r", encoding="utf-8") as f:
        actual_content = f.read()
    # Should match exactly, including no extra trailing lines
    expected = EXPECTED_REPORT_CONTENT.strip()
    actual = actual_content.strip()
    assert actual == expected, (
        f"The contents of {TICKET_FREQUENCY_REPORT_PATH} do not match the expected output.\n"
        f"Expected:\n{EXPECTED_REPORT_CONTENT}\n\n"
        f"Found:\n{actual_content}\n"
        "Ensure there are no extra blank lines or missing lines."
    )