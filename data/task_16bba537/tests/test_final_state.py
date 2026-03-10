# test_final_state.py

import os
import re
import pytest

LOG_FILE = "/home/user/logs/fw_deny.log"
OUTPUT_FILE = "/home/user/logs/deny_count.txt"

EXPECTED_OUTPUT_LINES = [
    "6 192.168.1.45",
    "5 10.10.5.2",
    "4 172.16.8.99",
]


def test_output_file_exists():
    assert os.path.isfile(OUTPUT_FILE), (
        f"Output file '{OUTPUT_FILE}' does not exist. "
        "The task requires writing deny counts to this file."
    )


def test_output_file_is_readable():
    assert os.access(OUTPUT_FILE, os.R_OK), (
        f"Output file '{OUTPUT_FILE}' exists but is not readable."
    )


def test_output_file_line_count():
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()

    lines = content.rstrip("\n").splitlines()
    assert len(lines) == len(EXPECTED_OUTPUT_LINES), (
        f"Output file '{OUTPUT_FILE}' has {len(lines)} lines, "
        f"expected {len(EXPECTED_OUTPUT_LINES)} lines.\n"
        f"  File contents:\n{content!r}"
    )


def test_output_file_no_leading_spaces():
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()

    lines = content.rstrip("\n").splitlines()
    for i, line in enumerate(lines, start=1):
        assert not line.startswith(" "), (
            f"Line {i} of '{OUTPUT_FILE}' has a leading space, which is not allowed.\n"
            f"  Line content: {line!r}"
        )


def test_output_file_no_blank_lines():
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()

    lines = content.rstrip("\n").splitlines()
    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"Line {i} of '{OUTPUT_FILE}' is blank. No blank lines are allowed."
        )


def test_output_file_exact_content():
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()

    assert len(actual_lines) == len(EXPECTED_OUTPUT_LINES), (
        f"Output file '{OUTPUT_FILE}' has {len(actual_lines)} lines, "
        f"expected {len(EXPECTED_OUTPUT_LINES)} lines."
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, EXPECTED_OUTPUT_LINES), start=1):
        assert actual == expected, (
            f"Line {i} of '{OUTPUT_FILE}' does not match expected.\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}\n"
            f"  Hint: Lines must be in 'count ip_address' format, sorted by count "
            f"descending, then by IP descending lexicographically for ties."
        )


def test_output_counts_match_log():
    """Verify that the counts in the output file match what is actually in the log."""
    # Parse the log file to get ground-truth counts
    counts = {}
    with open(LOG_FILE, "r") as f:
        for line in f:
            m = re.search(r'src=(\S+)', line)
            if m:
                ip = m.group(1)
                counts[ip] = counts.get(ip, 0) + 1

    # Parse the output file
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()

    output_lines = content.rstrip("\n").splitlines()
    output_counts = {}
    for i, line in enumerate(output_lines, start=1):
        parts = line.split()
        assert len(parts) == 2, (
            f"Line {i} of '{OUTPUT_FILE}' does not have exactly 2 fields.\n"
            f"  Line content: {line!r}\n"
            f"  Expected format: '<count> <ip_address>'"
        )
        count_str, ip = parts
        assert count_str.isdigit(), (
            f"Line {i} of '{OUTPUT_FILE}': first field '{count_str}' is not a valid integer count."
        )
        output_counts[ip] = int(count_str)

    assert output_counts == counts, (
        f"Counts in '{OUTPUT_FILE}' do not match actual IP counts from '{LOG_FILE}'.\n"
        f"  Expected counts: {counts}\n"
        f"  Output counts:   {output_counts}"
    )


def test_output_sorted_by_count_descending():
    """Verify lines are sorted by count in descending order."""
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()

    output_lines = content.rstrip("\n").splitlines()
    counts_in_order = []
    for line in output_lines:
        parts = line.split()
        if len(parts) == 2 and parts[0].isdigit():
            counts_in_order.append(int(parts[0]))

    assert counts_in_order == sorted(counts_in_order, reverse=True), (
        f"Lines in '{OUTPUT_FILE}' are not sorted by count in descending order.\n"
        f"  Counts found: {counts_in_order}\n"
        f"  Expected order: {sorted(counts_in_order, reverse=True)}"
    )


def test_output_tie_breaking_reverse_alphabetical():
    """
    Verify that IPs with the same count are sorted in reverse alphabetical (descending
    lexicographic) order. In this specific dataset all counts are distinct, so this
    test verifies the structure is correct regardless.
    """
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()

    output_lines = content.rstrip("\n").splitlines()

    # Group lines by count
    from collections import defaultdict
    groups = defaultdict(list)
    for line in output_lines:
        parts = line.split()
        if len(parts) == 2 and parts[0].isdigit():
            count = int(parts[0])
            ip = parts[1]
            groups[count].append(ip)

    for count, ips in groups.items():
        expected_order = sorted(ips, reverse=True)
        assert ips == expected_order, (
            f"IPs with count={count} in '{OUTPUT_FILE}' are not in reverse alphabetical order.\n"
            f"  Found order:    {ips}\n"
            f"  Expected order: {expected_order}"
        )


def test_log_file_unchanged():
    """Ensure the original log file was not modified."""
    EXPECTED_LINES = [
        "2024-11-01T08:12:03 DENY src=192.168.1.45 dst=10.0.0.1 port=443 proto=TCP",
        "2024-11-01T08:12:11 DENY src=10.10.5.2 dst=10.0.0.1 port=22 proto=TCP",
        "2024-11-01T08:13:00 DENY src=192.168.1.45 dst=10.0.0.1 port=80 proto=TCP",
        "2024-11-01T08:13:45 DENY src=172.16.8.99 dst=10.0.0.2 port=8080 proto=TCP",
        "2024-11-01T08:14:02 DENY src=10.10.5.2 dst=10.0.0.1 port=22 proto=TCP",
        "2024-11-01T08:14:30 DENY src=192.168.1.45 dst=10.0.0.1 port=443 proto=TCP",
        "2024-11-01T08:15:01 DENY src=10.10.5.2 dst=10.0.0.3 port=3389 proto=TCP",
        "2024-11-01T08:15:22 DENY src=172.16.8.99 dst=10.0.0.2 port=443 proto=TCP",
        "2024-11-01T08:16:10 DENY src=192.168.1.45 dst=10.0.0.1 port=8443 proto=TCP",
        "2024-11-01T08:16:55 DENY src=10.10.5.2 dst=10.0.0.1 port=22 proto=TCP",
        "2024-11-01T08:17:03 DENY src=192.168.1.45 dst=10.0.0.2 port=80 proto=TCP",
        "2024-11-01T08:17:44 DENY src=172.16.8.99 dst=10.0.0.1 port=53 proto=UDP",
        "2024-11-01T08:18:05 DENY src=10.10.5.2 dst=10.0.0.1 port=22 proto=TCP",
        "2024-11-01T08:18:50 DENY src=192.168.1.45 dst=10.0.0.3 port=443 proto=TCP",
        "2024-11-01T08:19:12 DENY src=172.16.8.99 dst=10.0.0.1 port=80 proto=TCP",
    ]

    with open(LOG_FILE, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()

    assert len(actual_lines) == len(EXPECTED_LINES), (
        f"Log file '{LOG_FILE}' appears to have been modified: "
        f"expected {len(EXPECTED_LINES)} lines, found {len(actual_lines)}."
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, EXPECTED_LINES), start=1):
        assert actual == expected, (
            f"Log file '{LOG_FILE}' line {i} was modified.\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}"
        )