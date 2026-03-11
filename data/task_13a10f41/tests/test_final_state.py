# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/security/top_offenders.txt"
LOG_PATH = "/home/user/security/firewall_deny.log"
SECURITY_DIR = "/home/user/security"

EXPECTED_CONTENT = """\
7 10.0.0.5
5 172.16.0.3
5 192.168.1.20
3 10.0.1.8
TOTAL_DENIES: 20"""

EXPECTED_LINES = [
    "7 10.0.0.5",
    "5 172.16.0.3",
    "5 192.168.1.20",
    "3 10.0.1.8",
    "TOTAL_DENIES: 20",
]


def test_security_directory_exists():
    assert os.path.isdir(SECURITY_DIR), (
        f"Directory '{SECURITY_DIR}' does not exist. "
        "The security directory must be present."
    )


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The student must generate this file as part of the task."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file '{REPORT_PATH}' exists but is not readable."
    )


def test_report_file_has_exactly_5_lines():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    # Strip trailing blank lines
    while lines and lines[-1].strip() == "":
        lines.pop()
    assert len(lines) == 5, (
        f"Expected exactly 5 lines in '{REPORT_PATH}' "
        f"(4 IP lines + 1 TOTAL_DENIES line), but found {len(lines)}.\n"
        f"Actual content:\n{content!r}"
    )


def test_report_line_contents_match_exactly():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    actual_lines = content.splitlines()
    while actual_lines and actual_lines[-1].strip() == "":
        actual_lines.pop()

    assert len(actual_lines) == len(EXPECTED_LINES), (
        f"Line count mismatch: expected {len(EXPECTED_LINES)}, "
        f"got {len(actual_lines)}.\n"
        f"Actual content:\n{content!r}"
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, EXPECTED_LINES), start=1):
        assert actual == expected, (
            f"Line {i} mismatch.\n"
            f"  Expected: {expected!r}\n"
            f"  Got:      {actual!r}\n"
            f"Full file content:\n{content!r}"
        )


def test_report_no_trailing_whitespace_on_lines():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    while lines and lines[-1].strip() == "":
        lines.pop()

    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} has trailing whitespace: {line!r}"
        )


def test_report_no_blank_lines():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    # Exclude trailing blank lines (only check non-trailing blanks)
    while lines and lines[-1].strip() == "":
        lines.pop()

    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"Line {i} is blank, but no blank lines are allowed in '{REPORT_PATH}'."
        )


def test_ip_lines_format():
    """The first 4 lines must be in '<count> <ip>' format."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    while lines and lines[-1].strip() == "":
        lines.pop()

    ip_lines = lines[:4]
    for i, line in enumerate(ip_lines, start=1):
        parts = line.split()
        assert len(parts) == 2, (
            f"Line {i} does not have exactly 2 fields (count and IP): {line!r}"
        )
        count_str, ip_str = parts
        assert count_str.isdigit(), (
            f"Line {i}: count field is not a digit: {count_str!r}"
        )
        octets = ip_str.split(".")
        assert len(octets) == 4 and all(o.isdigit() for o in octets), (
            f"Line {i}: IP address format is invalid: {ip_str!r}"
        )


def test_ip_counts_are_correct():
    """Verify the count values for each IP are correct."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    while lines and lines[-1].strip() == "":
        lines.pop()

    ip_lines = lines[:4]
    ip_count_map = {}
    for line in ip_lines:
        parts = line.split()
        if len(parts) == 2:
            count, ip = parts
            ip_count_map[ip] = int(count)

    expected_counts = {
        "10.0.0.5": 7,
        "172.16.0.3": 5,
        "192.168.1.20": 5,
        "10.0.1.8": 3,
    }

    for ip, expected_count in expected_counts.items():
        assert ip in ip_count_map, (
            f"IP '{ip}' not found in report. Found IPs: {list(ip_count_map.keys())}"
        )
        assert ip_count_map[ip] == expected_count, (
            f"IP '{ip}': expected count {expected_count}, got {ip_count_map[ip]}."
        )

    assert set(ip_count_map.keys()) == set(expected_counts.keys()), (
        f"Unexpected IPs in report. Found: {set(ip_count_map.keys())}, "
        f"Expected: {set(expected_counts.keys())}"
    )


def test_sort_order_most_frequent_first():
    """Lines must be sorted by count descending."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    while lines and lines[-1].strip() == "":
        lines.pop()

    ip_lines = lines[:4]
    counts = []
    for line in ip_lines:
        parts = line.split()
        if len(parts) == 2:
            counts.append(int(parts[0]))

    assert counts == sorted(counts, reverse=True), (
        f"IP lines are not sorted by count descending. "
        f"Counts found: {counts}"
    )


def test_tie_broken_by_ip_numerically_ascending():
    """When counts are equal, IPs must be sorted numerically ascending."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    while lines and lines[-1].strip() == "":
        lines.pop()

    ip_lines = lines[:4]
    parsed = []
    for line in ip_lines:
        parts = line.split()
        if len(parts) == 2:
            count = int(parts[0])
            ip = parts[1]
            ip_tuple = tuple(int(o) for o in ip.split("."))
            parsed.append((count, ip_tuple, ip))

    # Group by count and check within each group IPs are ascending numerically
    from itertools import groupby
    for count, group in groupby(parsed, key=lambda x: x[0]):
        group_list = list(group)
        ip_tuples = [item[1] for item in group_list]
        assert ip_tuples == sorted(ip_tuples), (
            f"For count={count}, IPs are not sorted numerically ascending. "
            f"Found IPs: {[item[2] for item in group_list]}"
        )


def test_total_denies_line_is_last():
    """The TOTAL_DENIES line must be the last line."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    while lines and lines[-1].strip() == "":
        lines.pop()

    last_line = lines[-1]
    assert last_line == "TOTAL_DENIES: 20", (
        f"Last line must be 'TOTAL_DENIES: 20', but got: {last_line!r}"
    )


def test_total_denies_format():
    """The TOTAL_DENIES line must have the exact format 'TOTAL_DENIES: <number>'."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    while lines and lines[-1].strip() == "":
        lines.pop()

    total_line = lines[-1]
    assert total_line.startswith("TOTAL_DENIES: "), (
        f"TOTAL_DENIES line must start with 'TOTAL_DENIES: ', got: {total_line!r}"
    )
    total_str = total_line[len("TOTAL_DENIES: "):]
    assert total_str.isdigit(), (
        f"TOTAL_DENIES value must be a number, got: {total_str!r}"
    )
    assert int(total_str) == 20, (
        f"TOTAL_DENIES value must be 20 (total log entries), got: {total_str}"
    )


def test_exact_file_content():
    """The entire file content must match the expected content exactly."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    # Normalize: strip trailing newline for comparison
    normalized = content.rstrip("\n")
    assert normalized == EXPECTED_CONTENT, (
        f"File content does not match expected.\n"
        f"Expected:\n{EXPECTED_CONTENT!r}\n\n"
        f"Got:\n{normalized!r}"
    )


def test_log_file_still_intact():
    """The original log file must still exist and be unchanged."""
    assert os.path.isfile(LOG_PATH), (
        f"Original log file '{LOG_PATH}' is missing after task completion."
    )
    with open(LOG_PATH, "r") as f:
        lines = f.read().splitlines()
    while lines and lines[-1].strip() == "":
        lines.pop()
    assert len(lines) == 20, (
        f"Original log file '{LOG_PATH}' should still have 20 lines, "
        f"but found {len(lines)}."
    )