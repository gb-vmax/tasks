# test_final_state.py

import os
import pytest

CHARGES_CSV_PATH = "/home/user/finops/charges.csv"
REPORT_PATH = "/home/user/finops/team_charge_counts.txt"

EXPECTED_LINES = [
    "12 platform",
    "7 analytics",
    "7 data",
    "4 infra",
]


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The task requires producing this file with team charge counts."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file '{REPORT_PATH}' exists but is not readable. "
        "Ensure the file has appropriate read permissions."
    )


def test_report_line_count():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    actual_lines = [line for line in content.splitlines() if line.strip()]
    assert len(actual_lines) == len(EXPECTED_LINES), (
        f"Report file has {len(actual_lines)} non-empty line(s), "
        f"expected {len(EXPECTED_LINES)}.\n"
        f"Actual content:\n{content!r}"
    )


def test_report_content_exact():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    actual_lines = [line for line in content.splitlines() if line.strip()]

    for i, (actual, expected) in enumerate(zip(actual_lines, EXPECTED_LINES), start=1):
        assert actual == expected, (
            f"Line {i} of '{REPORT_PATH}' does not match.\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}\n"
            f"Hint: format is '<count> <team>' with a single space, "
            f"sorted by count descending then team name alphabetically."
        )


def test_report_no_trailing_spaces():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        stripped_right = line.rstrip("\n")
        assert stripped_right == stripped_right.rstrip(), (
            f"Line {i} of '{REPORT_PATH}' has trailing whitespace: {line!r}"
        )


def test_report_no_header():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    actual_lines = [line for line in content.splitlines() if line.strip()]
    if actual_lines:
        first_line = actual_lines[0]
        parts = first_line.split()
        assert len(parts) == 2 and parts[0].isdigit(), (
            f"First line of '{REPORT_PATH}' does not look like a data row "
            f"(expected '<count> <team>', got {first_line!r}). "
            "Make sure there is no header line."
        )


def test_report_format_each_line():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    actual_lines = [line for line in content.splitlines() if line.strip()]
    for i, line in enumerate(actual_lines, start=1):
        parts = line.split(" ")
        assert len(parts) == 2, (
            f"Line {i} of '{REPORT_PATH}' does not have exactly two fields "
            f"separated by a single space: {line!r}"
        )
        count_str, team_name = parts
        assert count_str.isdigit(), (
            f"Line {i} of '{REPORT_PATH}': first field '{count_str}' is not an integer."
        )
        assert team_name.strip() == team_name and len(team_name) > 0, (
            f"Line {i} of '{REPORT_PATH}': team name '{team_name}' is invalid."
        )


def test_report_sorted_by_count_descending_then_alpha():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    actual_lines = [line for line in content.splitlines() if line.strip()]
    parsed = []
    for line in actual_lines:
        parts = line.split(" ", 1)
        count = int(parts[0])
        team = parts[1]
        parsed.append((count, team))

    # Verify sorted: descending count, then ascending team name for ties
    for i in range(len(parsed) - 1):
        curr_count, curr_team = parsed[i]
        next_count, next_team = parsed[i + 1]
        assert curr_count > next_count or (curr_count == next_count and curr_team <= next_team), (
            f"Lines {i + 1} and {i + 2} of '{REPORT_PATH}' are not in the correct order.\n"
            f"  Line {i + 1}: {curr_count} {curr_team}\n"
            f"  Line {i + 2}: {next_count} {next_team}\n"
            "Expected: sorted by count descending, then alphabetically by team name for ties."
        )


def test_report_counts_match_csv():
    """Cross-check the report counts against the source charges.csv."""
    from collections import Counter

    assert os.path.isfile(CHARGES_CSV_PATH), (
        f"Cannot cross-check: source file '{CHARGES_CSV_PATH}' does not exist."
    )

    with open(CHARGES_CSV_PATH, "r") as f:
        csv_lines = [line.strip() for line in f if line.strip()]

    team_counter = Counter()
    for line in csv_lines:
        parts = line.split(",")
        assert len(parts) == 5, (
            f"Malformed line in charges.csv (expected 5 fields): {line!r}"
        )
        team = parts[3]
        team_counter[team] += 1

    with open(REPORT_PATH, "r") as f:
        report_lines = [line for line in f.read().splitlines() if line.strip()]

    report_counts = {}
    for line in report_lines:
        parts = line.split(" ", 1)
        count = int(parts[0])
        team = parts[1]
        report_counts[team] = count

    # Every team in CSV must appear in report with correct count
    for team, expected_count in team_counter.items():
        assert team in report_counts, (
            f"Team '{team}' from charges.csv is missing from '{REPORT_PATH}'."
        )
        assert report_counts[team] == expected_count, (
            f"Team '{team}' has count {report_counts[team]} in report, "
            f"but {expected_count} line items in charges.csv."
        )

    # No extra teams in report
    for team in report_counts:
        assert team in team_counter, (
            f"Team '{team}' appears in report but not in charges.csv."
        )


def test_report_exact_expected_content():
    """Final definitive check against the known expected output."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    actual_lines = [line for line in content.splitlines() if line.strip()]
    expected_content = "\n".join(EXPECTED_LINES)
    actual_content = "\n".join(actual_lines)

    assert actual_lines == EXPECTED_LINES, (
        f"Report content does not match expected output.\n"
        f"Expected:\n{expected_content}\n\n"
        f"Actual:\n{actual_content}"
    )