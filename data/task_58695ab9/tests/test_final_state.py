# test_final_state.py

import os
import re
import pytest

REPORT_FILE = "/home/user/pipeline/failure_report.txt"
LOG_FILE = "/home/user/pipeline/build_failures.log"

EXPECTED_LINES = [
    "6 Gradle sync failed",
    "5 Unit tests failed",
    "4 Code signing error",
    "3 Provisioning profile expired",
    "2 NDK version mismatch",
]

EXPECTED_COUNTS = {
    "Gradle sync failed": 6,
    "Unit tests failed": 5,
    "Code signing error": 4,
    "Provisioning profile expired": 3,
    "NDK version mismatch": 2,
}


def read_report_lines():
    """Read the report file and return non-empty lines."""
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    return content, [line for line in content.splitlines() if line.strip()]


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Failure report file does not exist: {REPORT_FILE}. "
        "The task requires generating this file from the build_failures.log."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_FILE, os.R_OK), (
        f"Failure report file exists but is not readable: {REPORT_FILE}"
    )


def test_report_has_exactly_five_lines():
    _, lines = read_report_lines()
    assert len(lines) == 5, (
        f"Expected exactly 5 lines in the report (one per unique failure reason), "
        f"but found {len(lines)} lines. Lines found:\n" + "\n".join(lines)
    )


def test_report_no_blank_lines():
    content, _ = read_report_lines()
    raw_lines = content.splitlines()
    blank_lines = [i + 1 for i, line in enumerate(raw_lines) if line.strip() == ""]
    assert not blank_lines, (
        f"Report contains blank lines at line numbers: {blank_lines}. "
        "The report must have no blank lines."
    )


def test_report_no_trailing_whitespace_on_lines():
    content, lines = read_report_lines()
    bad_lines = [(i + 1, repr(line)) for i, line in enumerate(content.splitlines()) if line != line.rstrip()]
    assert not bad_lines, (
        f"Report has lines with trailing whitespace:\n"
        + "\n".join(f"  Line {lineno}: {repr_line}" for lineno, repr_line in bad_lines)
    )


def test_report_line_format():
    """Each line must match the pattern: ^[0-9]+ .+$ (count, space, failure reason)."""
    _, lines = read_report_lines()
    pattern = re.compile(r"^\d+ .+$")
    bad_lines = [(i + 1, line) for i, line in enumerate(lines) if not pattern.match(line)]
    assert not bad_lines, (
        f"The following lines do not match the required format '<count> <failure reason>':\n"
        + "\n".join(f"  Line {lineno}: {repr(line)}" for lineno, line in bad_lines)
    )


def test_report_no_leading_spaces_on_count():
    """Count must be a plain number with no leading spaces or zero-padding."""
    _, lines = read_report_lines()
    for i, line in enumerate(lines, 1):
        parts = line.split(" ", 1)
        assert len(parts) == 2, (
            f"Line {i} does not have the expected format '<count> <failure reason>': {repr(line)}"
        )
        count_str = parts[0]
        assert count_str == str(int(count_str)), (
            f"Line {i} has a count with leading zeros or invalid format: {repr(count_str)}. "
            "Count must be a plain integer with no padding."
        )


def test_report_exact_content():
    """The report must exactly match the expected lines in order."""
    _, lines = read_report_lines()
    assert lines == EXPECTED_LINES, (
        f"Report content does not match expected.\n"
        f"Expected:\n" + "\n".join(EXPECTED_LINES) + "\n\n"
        f"Actual:\n" + "\n".join(lines)
    )


def test_report_counts_are_correct():
    """Each failure reason must have the correct count."""
    _, lines = read_report_lines()
    for line in lines:
        parts = line.split(" ", 1)
        if len(parts) != 2:
            pytest.fail(f"Line does not have expected format: {repr(line)}")
        count_str, reason = parts
        count = int(count_str)
        if reason in EXPECTED_COUNTS:
            expected_count = EXPECTED_COUNTS[reason]
            assert count == expected_count, (
                f"Failure reason '{reason}' has count {count}, "
                f"but expected count is {expected_count}."
            )


def test_report_contains_all_expected_failure_reasons():
    """All five unique failure reasons must appear in the report."""
    _, lines = read_report_lines()
    reasons_in_report = set()
    for line in lines:
        parts = line.split(" ", 1)
        if len(parts) == 2:
            reasons_in_report.add(parts[1])

    for expected_reason in EXPECTED_COUNTS:
        assert expected_reason in reasons_in_report, (
            f"Expected failure reason '{expected_reason}' is missing from the report. "
            f"Reasons found: {sorted(reasons_in_report)}"
        )


def test_report_sorted_by_count_descending():
    """Lines must be sorted from most frequent to least frequent."""
    _, lines = read_report_lines()
    counts = []
    for line in lines:
        parts = line.split(" ", 1)
        if len(parts) == 2:
            counts.append(int(parts[0]))

    assert counts == sorted(counts, reverse=True), (
        f"Report is not sorted by count in descending order. "
        f"Counts found: {counts}. Expected order: {sorted(counts, reverse=True)}"
    )


def test_report_alphabetical_tiebreak():
    """When counts are equal, failure reasons must be sorted alphabetically (ascending)."""
    _, lines = read_report_lines()
    # Group lines by count
    from collections import defaultdict
    count_groups = defaultdict(list)
    for line in lines:
        parts = line.split(" ", 1)
        if len(parts) == 2:
            count_groups[int(parts[0])].append(parts[1])

    for count, reasons in count_groups.items():
        if len(reasons) > 1:
            assert reasons == sorted(reasons), (
                f"For count={count}, failure reasons are not sorted alphabetically. "
                f"Found order: {reasons}. Expected: {sorted(reasons)}"
            )


def test_report_no_extra_failure_reasons():
    """The report must not contain any failure reasons beyond the expected five."""
    _, lines = read_report_lines()
    reasons_in_report = set()
    for line in lines:
        parts = line.split(" ", 1)
        if len(parts) == 2:
            reasons_in_report.add(parts[1])

    expected_reasons = set(EXPECTED_COUNTS.keys())
    unexpected = reasons_in_report - expected_reasons
    assert not unexpected, (
        f"Report contains unexpected failure reasons: {unexpected}. "
        f"Only these reasons should appear: {expected_reasons}"
    )


def test_log_file_unchanged():
    """The source log file must not have been modified."""
    expected_log_lines = [
        "Gradle sync failed",
        "Code signing error",
        "Unit tests failed",
        "Gradle sync failed",
        "Provisioning profile expired",
        "Unit tests failed",
        "Gradle sync failed",
        "Code signing error",
        "NDK version mismatch",
        "Gradle sync failed",
        "Unit tests failed",
        "Provisioning profile expired",
        "Gradle sync failed",
        "Code signing error",
        "NDK version mismatch",
        "Unit tests failed",
        "Gradle sync failed",
        "Provisioning profile expired",
        "Code signing error",
        "Unit tests failed",
    ]
    assert os.path.isfile(LOG_FILE), (
        f"Source log file is missing: {LOG_FILE}"
    )
    with open(LOG_FILE, "r") as f:
        content = f.read()
    actual_lines = content.strip().splitlines()
    assert actual_lines == expected_log_lines, (
        f"Source log file has been modified! It should remain unchanged.\n"
        f"Expected {len(expected_log_lines)} lines, got {len(actual_lines)} lines."
    )