# test_final_state.py

import os
import pytest

VULN_SUMMARY_PATH = "/home/user/pentest/vuln_summary.txt"
SCAN_RESULTS_PATH = "/home/user/pentest/scan_results.txt"
PENTEST_DIR = "/home/user/pentest"

EXPECTED_LINES = [
    "6 SSL_WEAK_CIPHER",
    "5 DEFAULT_CREDENTIALS",
    "5 SMB_SIGNING_DISABLED",
    "4 OPEN_REDIRECT",
    "4 XSS_REFLECTED",
    "2 SSL_SELF_SIGNED_CERT",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES) + "\n"


def test_pentest_directory_exists():
    assert os.path.isdir(PENTEST_DIR), (
        f"Directory '{PENTEST_DIR}' does not exist. "
        "The pentest working directory must be present."
    )


def test_scan_results_file_still_exists():
    """The original input file must not have been removed."""
    assert os.path.isfile(SCAN_RESULTS_PATH), (
        f"Original scan results file '{SCAN_RESULTS_PATH}' no longer exists. "
        "The input file must not be deleted or moved."
    )


def test_vuln_summary_file_exists():
    assert os.path.isfile(VULN_SUMMARY_PATH), (
        f"Output file '{VULN_SUMMARY_PATH}' does not exist. "
        "The vulnerability summary file must be created at this exact path."
    )


def test_vuln_summary_file_readable():
    assert os.access(VULN_SUMMARY_PATH, os.R_OK), (
        f"File '{VULN_SUMMARY_PATH}' is not readable. "
        "The summary file must be readable."
    )


def test_vuln_summary_line_count():
    with open(VULN_SUMMARY_PATH, "r") as f:
        content = f.read()

    # Strip trailing newline before splitting so a single trailing newline
    # doesn't produce a spurious empty entry.
    actual_lines = content.rstrip("\n").splitlines()

    assert len(actual_lines) == 6, (
        f"Expected exactly 6 lines in '{VULN_SUMMARY_PATH}', "
        f"but found {len(actual_lines)} lines.\n"
        f"Actual content:\n{content}"
    )


def test_vuln_summary_no_blank_lines():
    with open(VULN_SUMMARY_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()
    blank_lines = [i + 1 for i, line in enumerate(actual_lines) if line.strip() == ""]

    assert not blank_lines, (
        f"Found blank lines in '{VULN_SUMMARY_PATH}' at line numbers: {blank_lines}. "
        "The summary file must contain no blank lines."
    )


def test_vuln_summary_no_leading_whitespace():
    with open(VULN_SUMMARY_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()
    bad_lines = [
        (i + 1, repr(line))
        for i, line in enumerate(actual_lines)
        if line != line.lstrip()
    ]

    assert not bad_lines, (
        f"Found lines with leading whitespace in '{VULN_SUMMARY_PATH}':\n"
        + "\n".join(f"  Line {lineno}: {line}" for lineno, line in bad_lines)
        + "\nEach line must start with the count digit(s) immediately — no leading spaces."
    )


def test_vuln_summary_no_trailing_whitespace():
    with open(VULN_SUMMARY_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()
    bad_lines = [
        (i + 1, repr(line))
        for i, line in enumerate(actual_lines)
        if line != line.rstrip()
    ]

    assert not bad_lines, (
        f"Found lines with trailing whitespace in '{VULN_SUMMARY_PATH}':\n"
        + "\n".join(f"  Line {lineno}: {line}" for lineno, line in bad_lines)
        + "\nEach line must have no trailing whitespace."
    )


def test_vuln_summary_line_format():
    """Every line must match '<integer> <VULN_NAME>' with exactly one space."""
    import re
    pattern = re.compile(r'^\d+ \S+$')

    with open(VULN_SUMMARY_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()
    bad_lines = [
        (i + 1, repr(line))
        for i, line in enumerate(actual_lines)
        if not pattern.match(line)
    ]

    assert not bad_lines, (
        f"Lines in '{VULN_SUMMARY_PATH}' do not match the required format "
        "'<count> <vulnerability_name>':\n"
        + "\n".join(f"  Line {lineno}: {line}" for lineno, line in bad_lines)
    )


def test_vuln_summary_exact_lines():
    """Each line must exactly match the expected output."""
    with open(VULN_SUMMARY_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()

    assert actual_lines == EXPECTED_LINES, (
        f"Contents of '{VULN_SUMMARY_PATH}' do not match expected.\n\n"
        f"Expected ({len(EXPECTED_LINES)} lines):\n"
        + "\n".join(EXPECTED_LINES)
        + f"\n\nActual ({len(actual_lines)} lines):\n"
        + "\n".join(actual_lines)
        + "\n\nDiff (expected vs actual):\n"
        + _diff(EXPECTED_LINES, actual_lines)
    )


def test_vuln_summary_sorted_by_count_descending():
    """Counts must be in non-increasing order."""
    with open(VULN_SUMMARY_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()
    counts = []
    for line in actual_lines:
        parts = line.split(" ", 1)
        assert len(parts) == 2, (
            f"Cannot parse count from line: {repr(line)}"
        )
        counts.append(int(parts[0]))

    for i in range(len(counts) - 1):
        assert counts[i] >= counts[i + 1], (
            f"Counts are not sorted in descending order in '{VULN_SUMMARY_PATH}'.\n"
            f"Line {i + 1} has count {counts[i]} but line {i + 2} has count {counts[i + 1]}.\n"
            f"All lines:\n" + "\n".join(actual_lines)
        )


def test_vuln_summary_tiebreaker_alphabetical():
    """When counts are equal, vulnerability names must be sorted alphabetically."""
    with open(VULN_SUMMARY_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()

    parsed = []
    for line in actual_lines:
        parts = line.split(" ", 1)
        parsed.append((int(parts[0]), parts[1]))

    # Group by count and check alphabetical order within each group
    from itertools import groupby
    for count, group in groupby(parsed, key=lambda x: x[0]):
        names = [item[1] for item in group]
        assert names == sorted(names), (
            f"Vulnerability names with count {count} are not in alphabetical order "
            f"in '{VULN_SUMMARY_PATH}'.\n"
            f"Expected alphabetical order: {sorted(names)}\n"
            f"Actual order: {names}"
        )


def test_vuln_summary_correct_counts():
    """Each vulnerability must have the correct count."""
    with open(VULN_SUMMARY_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()

    actual_counts = {}
    for line in actual_lines:
        parts = line.split(" ", 1)
        assert len(parts) == 2, f"Cannot parse line: {repr(line)}"
        count, name = int(parts[0]), parts[1]
        actual_counts[name] = count

    expected_counts = {
        "SSL_WEAK_CIPHER": 6,
        "SMB_SIGNING_DISABLED": 5,
        "DEFAULT_CREDENTIALS": 5,
        "OPEN_REDIRECT": 4,
        "XSS_REFLECTED": 4,
        "SSL_SELF_SIGNED_CERT": 2,
    }

    for vuln, expected_count in expected_counts.items():
        assert vuln in actual_counts, (
            f"Vulnerability '{vuln}' is missing from '{VULN_SUMMARY_PATH}'."
        )
        assert actual_counts[vuln] == expected_count, (
            f"Vulnerability '{vuln}' should have count {expected_count} "
            f"in '{VULN_SUMMARY_PATH}', but found {actual_counts[vuln]}."
        )

    extra = set(actual_counts.keys()) - set(expected_counts.keys())
    assert not extra, (
        f"Unexpected vulnerability types found in '{VULN_SUMMARY_PATH}': {sorted(extra)}. "
        f"Only these types should appear: {sorted(expected_counts.keys())}"
    )


def test_vuln_summary_no_header():
    """The first line must be a data line, not a header."""
    with open(VULN_SUMMARY_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")

    # A header would typically start with a non-digit character
    assert first_line and first_line[0].isdigit(), (
        f"The first line of '{VULN_SUMMARY_PATH}' does not look like a data line "
        f"(expected to start with a digit). Got: {repr(first_line)}. "
        "The file must contain no header — only data lines."
    )


def test_vuln_summary_exact_content():
    """The entire file content must match exactly (including line endings)."""
    with open(VULN_SUMMARY_PATH, "r") as f:
        content = f.read()

    # Accept files that end with exactly one newline or no trailing newline.
    # The canonical expected content ends with a single newline.
    normalized_actual = content if content.endswith("\n") else content + "\n"

    assert normalized_actual == EXPECTED_CONTENT, (
        f"File '{VULN_SUMMARY_PATH}' content does not match expected.\n\n"
        f"Expected:\n{EXPECTED_CONTENT}\n"
        f"Actual:\n{content}"
    )


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _diff(expected_lines, actual_lines):
    """Return a simple unified-style diff string for display in failure messages."""
    import difflib
    diff = difflib.unified_diff(
        expected_lines,
        actual_lines,
        fromfile="expected",
        tofile="actual",
        lineterm="",
    )
    return "\n".join(diff)