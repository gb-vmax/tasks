# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/audit/trail_report.txt"

EXPECTED_CONTENT = """\
AUDIT TRAIL - FAILED LOGIN ATTEMPTS
------------------------------------
[15/01/2024 10:05] alice @ 192.168.1.10
[18/01/2024 09:22] alice @ 192.168.1.10
[15/01/2024 08:45] bob @ 10.0.0.5
[16/01/2024 11:30] bob @ 10.0.0.5
[15/01/2024 09:12] carol @ 192.168.1.22
[18/01/2024 13:15] dave @ 10.0.0.8
[17/01/2024 16:47] eve @ 172.16.0.3
------------------------------------
Total failed attempts: 7
"""

SEPARATOR = "-" * 36


def read_report():
    with open(REPORT_PATH, "r") as f:
        return f.read()


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The student must generate this file to complete the task."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file '{REPORT_PATH}' exists but is not readable. "
        "Check file permissions."
    )


def test_report_exact_content():
    content = read_report()
    assert content == EXPECTED_CONTENT, (
        f"Report file '{REPORT_PATH}' does not match the expected content exactly.\n"
        f"Expected:\n{repr(EXPECTED_CONTENT)}\n\n"
        f"Actual:\n{repr(content)}"
    )


def test_report_header_line():
    content = read_report()
    lines = content.splitlines()
    assert lines[0] == "AUDIT TRAIL - FAILED LOGIN ATTEMPTS", (
        f"First line of report is incorrect.\n"
        f"Expected: 'AUDIT TRAIL - FAILED LOGIN ATTEMPTS'\n"
        f"Actual:   '{lines[0]}'"
    )


def test_report_first_separator():
    content = read_report()
    lines = content.splitlines()
    assert len(lines) >= 2, "Report has fewer than 2 lines."
    assert lines[1] == SEPARATOR, (
        f"Second line (first separator) of report is incorrect.\n"
        f"Expected: '{SEPARATOR}' (36 hyphens)\n"
        f"Actual:   '{lines[1]}' (length {len(lines[1])})"
    )


def test_report_second_separator():
    content = read_report()
    lines = content.splitlines()
    # The second separator should be the second-to-last line
    assert len(lines) >= 2, "Report has too few lines."
    second_sep_line = lines[-2]
    assert second_sep_line == SEPARATOR, (
        f"Second separator line of report is incorrect.\n"
        f"Expected: '{SEPARATOR}' (36 hyphens)\n"
        f"Actual:   '{second_sep_line}' (length {len(second_sep_line)})"
    )


def test_report_summary_line():
    content = read_report()
    lines = content.splitlines()
    summary_line = lines[-1]
    assert summary_line == "Total failed attempts: 7", (
        f"Summary (last) line of report is incorrect.\n"
        f"Expected: 'Total failed attempts: 7'\n"
        f"Actual:   '{summary_line}'"
    )


def test_report_ends_with_newline():
    content = read_report()
    assert content.endswith("\n"), (
        f"Report file '{REPORT_PATH}' does not end with a newline character. "
        "The file must end with a newline after the summary line."
    )


def test_report_entry_count():
    content = read_report()
    lines = content.splitlines()
    # Entries are between line index 2 and the second separator (second-to-last line)
    entry_lines = lines[2:-2]
    assert len(entry_lines) == 7, (
        f"Expected 7 entry lines in the report, but found {len(entry_lines)}.\n"
        f"Entry lines found:\n" + "\n".join(entry_lines)
    )


def test_report_entry_format():
    content = read_report()
    lines = content.splitlines()
    entry_lines = lines[2:-2]
    import re
    pattern = re.compile(
        r'^\[\d{2}/\d{2}/\d{4} \d{2}:\d{2}\] \S+ @ \d+\.\d+\.\d+\.\d+$'
    )
    for line in entry_lines:
        assert pattern.match(line), (
            f"Entry line does not match expected format "
            f"'[DD/MM/YYYY HH:MM] <username> @ <source_ip>'.\n"
            f"Offending line: '{line}'"
        )


def test_report_no_success_entries():
    content = read_report()
    lines = content.splitlines()
    entry_lines = lines[2:-2]
    # None of the entries should correspond to SUCCESS rows from the CSV
    # We verify by checking none of the known SUCCESS entries appear
    success_entries_substrings = [
        "alice @ 192.168.1.10",  # only SUCCESS for alice is 2024-01-15 08:23:41
        "dave @ 10.0.0.8",       # only SUCCESS for dave is 2024-01-16 07:58:09
        "carol @ 192.168.1.22",  # only SUCCESS for carol is 2024-01-17 14:02:44
    ]
    # More precisely, check that the SUCCESS timestamps do not appear
    success_timestamps_reformatted = [
        "15/01/2024 08:23",  # alice SUCCESS
        "16/01/2024 07:58",  # dave SUCCESS
        "17/01/2024 14:02",  # carol SUCCESS
    ]
    for ts in success_timestamps_reformatted:
        for line in entry_lines:
            assert ts not in line, (
                f"A SUCCESS row entry appears in the report (timestamp {ts}). "
                f"Only FAILURE rows should be included.\n"
                f"Offending line: '{line}'"
            )


def test_report_entries_sorted_by_username_then_timestamp():
    content = read_report()
    lines = content.splitlines()
    entry_lines = lines[2:-2]

    import re
    pattern = re.compile(
        r'^\[(\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2})\] (\S+) @ '
    )

    parsed = []
    for line in entry_lines:
        m = pattern.match(line)
        assert m, f"Could not parse entry line: '{line}'"
        day, month, year, hour, minute, username = m.groups()
        # Reconstruct sortable timestamp
        sortable_ts = f"{year}-{month}-{day} {hour}:{minute}"
        parsed.append((username, sortable_ts, line))

    sorted_parsed = sorted(parsed, key=lambda x: (x[0], x[1]))

    for i, (actual, expected) in enumerate(zip(parsed, sorted_parsed)):
        assert actual == expected, (
            f"Entry at position {i + 1} is out of order.\n"
            f"Found:    '{actual[2]}'\n"
            f"Expected: '{expected[2]}'\n"
            "Entries must be sorted by username (A-Z), then by timestamp (ascending)."
        )


def test_report_specific_entries_present():
    content = read_report()
    expected_entries = [
        "[15/01/2024 10:05] alice @ 192.168.1.10",
        "[18/01/2024 09:22] alice @ 192.168.1.10",
        "[15/01/2024 08:45] bob @ 10.0.0.5",
        "[16/01/2024 11:30] bob @ 10.0.0.5",
        "[15/01/2024 09:12] carol @ 192.168.1.22",
        "[18/01/2024 13:15] dave @ 10.0.0.8",
        "[17/01/2024 16:47] eve @ 172.16.0.3",
    ]
    for entry in expected_entries:
        assert entry in content, (
            f"Expected entry not found in report.\n"
            f"Missing entry: '{entry}'\n"
            f"Report content:\n{content}"
        )


def test_report_separator_length():
    assert len(SEPARATOR) == 36, (
        f"Internal test error: SEPARATOR should be 36 hyphens, got {len(SEPARATOR)}."
    )
    content = read_report()
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("-"):
            assert line == SEPARATOR, (
                f"Separator line at index {i} has incorrect length or content.\n"
                f"Expected: '{SEPARATOR}' (36 hyphens)\n"
                f"Actual:   '{line}' (length {len(line)})"
            )


def test_report_no_blank_lines_before_second_separator():
    content = read_report()
    lines = content.splitlines()
    # The line just before the second separator (lines[-2]) should be an entry, not blank
    line_before_second_sep = lines[-3]
    assert line_before_second_sep.strip() != "", (
        f"There is a blank line between the last entry and the second separator.\n"
        f"Line before second separator: '{line_before_second_sep}'"
    )


def test_report_timestamp_format_no_seconds():
    """Timestamps in entries must be DD/MM/YYYY HH:MM (no seconds)."""
    content = read_report()
    lines = content.splitlines()
    entry_lines = lines[2:-2]
    import re
    # Ensure no seconds appear in timestamps (format would be HH:MM:SS)
    seconds_pattern = re.compile(r'\[\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}\]')
    for line in entry_lines:
        assert not seconds_pattern.search(line), (
            f"Entry line contains seconds in the timestamp, but seconds should be dropped.\n"
            f"Offending line: '{line}'"
        )