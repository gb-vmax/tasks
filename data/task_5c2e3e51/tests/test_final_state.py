# test_final_state.py

"""
Pytest suite to validate the final state after generating the PostgreSQL customer_data
backup status summary report.

This test checks:
- The report file exists at /home/user/backup_summary/backup_status_report.txt
- The report file contents exactly match the required format and truth data
- Only the correct 5 backup entries are included, with correct ordering, headers, and field separators
- No extra lines, no trailing whitespace, and correct field values

Assumes initial state as described in the task and that the 5 most recent logs are:
    /home/user/backup_logs/backup_20240618.log
    /home/user/backup_logs/backup_20240619.log
    /home/user/backup_logs/backup_20240620.log
    /home/user/backup_logs/backup_20240621.log
    /home/user/backup_logs/backup_20240622.log
"""

import os
import pytest

REPORT_PATH = "/home/user/backup_summary/backup_status_report.txt"

# The expected report content as per the truth value
EXPECTED_REPORT_LINES = [
    "DATE_TIME | STATUS | DURATION",
    "2024-06-18 01:43:00 | SUCCESS | 00:12:03",
    "2024-06-19 01:43:01 | FAILURE | 00:07:20",
    "2024-06-20 01:44:15 | SUCCESS | 00:13:55",
    "2024-06-21 01:44:28 | SUCCESS | 00:09:40",
    "2024-06-22 00:35:22 | FAILURE | 00:08:32",
]

def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Backup status report file {REPORT_PATH} does not exist. "
        "You must generate the report at this exact location."
    )

def test_report_file_contents_exact():
    assert os.path.isfile(REPORT_PATH), (
        f"Backup status report file {REPORT_PATH} does not exist."
    )
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # Check number of lines
    assert len(lines) == len(EXPECTED_REPORT_LINES), (
        f"Report file {REPORT_PATH} should have {len(EXPECTED_REPORT_LINES)} lines "
        f"(header + 5 entries), but has {len(lines)}.\n"
        f"Actual content:\n{lines}"
    )

    # Check header
    assert lines[0] == EXPECTED_REPORT_LINES[0], (
        f"Header line in report file is incorrect.\n"
        f"Expected: {EXPECTED_REPORT_LINES[0]!r}\n"
        f"Actual:   {lines[0]!r}"
    )

    # Check each entry line exactly
    for i, (actual, expected) in enumerate(zip(lines, EXPECTED_REPORT_LINES)):
        assert actual == expected, (
            f"Line {i+1} of report file is incorrect.\n"
            f"Expected: {expected!r}\n"
            f"Actual:   {actual!r}"
        )

def test_report_no_extra_lines_or_trailing_whitespace():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        raw_content = f.read()

    # Check for trailing whitespace on any line
    for idx, line in enumerate(raw_content.splitlines(), 1):
        assert line == line.rstrip(), (
            f"Line {idx} of report file has trailing whitespace: {line!r}"
        )

    # Check file does not end with extra blank lines
    assert raw_content.endswith('\n') is False or raw_content.endswith('\r\n') is False, (
        f"Report file {REPORT_PATH} should not have trailing blank lines."
    )

def test_report_lines_format_and_fields():
    """
    Ensure that every entry line matches the required format:
    DATE_TIME | STATUS | DURATION
    (with exact separators and correct field values)
    """
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # Skip header
    entry_lines = lines[1:]

    for i, line in enumerate(entry_lines, 2):
        # Each line must contain exactly two " | " separators
        parts = line.split(" | ")
        assert len(parts) == 3, (
            f"Line {i} of report must have exactly two ' | ' separators.\n"
            f"Got: {line!r}"
        )
        date_time, status, duration = parts

        # Check DATE_TIME is of the format YYYY-MM-DD HH:MM:SS
        assert len(date_time) == 19, (
            f"Line {i}: DATE_TIME field is not 19 characters (YYYY-MM-DD HH:MM:SS): {date_time!r}"
        )
        # Simple format check
        yyyy, mm, dd = date_time[:4], date_time[5:7], date_time[8:10]
        assert yyyy.isdigit() and mm.isdigit() and dd.isdigit(), (
            f"Line {i}: DATE_TIME does not start with a valid date: {date_time!r}"
        )
        assert date_time[4] == '-' and date_time[7] == '-', (
            f"Line {i}: DATE_TIME missing '-' separators in date: {date_time!r}"
        )
        assert date_time[10] == ' ', (
            f"Line {i}: DATE_TIME missing space between date and time: {date_time!r}"
        )
        hh, min_, ss = date_time[11:13], date_time[14:16], date_time[17:19]
        assert hh.isdigit() and min_.isdigit() and ss.isdigit(), (
            f"Line {i}: DATE_TIME does not have a valid time: {date_time!r}"
        )
        assert date_time[13] == ':' and date_time[16] == ':', (
            f"Line {i}: DATE_TIME missing ':' separators in time: {date_time!r}"
        )

        # STATUS must be SUCCESS or FAILURE
        assert status in ("SUCCESS", "FAILURE"), (
            f"Line {i}: STATUS field must be 'SUCCESS' or 'FAILURE', got: {status!r}"
        )

        # DURATION must be HH:MM:SS
        assert len(duration) == 8, (
            f"Line {i}: DURATION field is not of format HH:MM:SS: {duration!r}"
        )
        h, m, s = duration[:2], duration[3:5], duration[6:8]
        assert h.isdigit() and m.isdigit() and s.isdigit(), (
            f"Line {i}: DURATION does not contain valid digits: {duration!r}"
        )
        assert duration[2] == ':' and duration[5] == ':', (
            f"Line {i}: DURATION missing ':' separators: {duration!r}"
        )