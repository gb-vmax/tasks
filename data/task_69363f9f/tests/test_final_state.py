# test_final_state.py

import os
import pytest

OUTPUT_DIR = "/home/user/api_data/output"
NORMALIZED_USERS = "/home/user/api_data/output/normalized_users.tsv"
COMBINED_REPORT = "/home/user/api_data/output/combined_report.tsv"


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def read_lines(filepath):
    """Return non-empty lines stripped of trailing newline/whitespace."""
    with open(filepath, "r") as f:
        return [line.rstrip("\n") for line in f if line.strip()]


# ---------------------------------------------------------------------------
# Output directory
# ---------------------------------------------------------------------------

def test_output_directory_exists():
    assert os.path.isdir(OUTPUT_DIR), (
        f"Output directory '{OUTPUT_DIR}' does not exist. "
        "The task requires creating this directory."
    )


# ---------------------------------------------------------------------------
# normalized_users.tsv — existence and basic structure
# ---------------------------------------------------------------------------

def test_normalized_users_exists():
    assert os.path.isfile(NORMALIZED_USERS), (
        f"File '{NORMALIZED_USERS}' does not exist. "
        "The task requires producing this file."
    )


def test_normalized_users_line_count():
    lines = read_lines(NORMALIZED_USERS)
    assert len(lines) == 6, (
        f"'{NORMALIZED_USERS}' should have exactly 6 non-empty lines "
        f"(1 header + 5 data rows), but found {len(lines)}."
    )


def test_normalized_users_header():
    lines = read_lines(NORMALIZED_USERS)
    expected = "user_id\tfull_name\temail\tdepartment\tstatus"
    actual = lines[0]
    assert actual == expected, (
        f"Header of normalized_users.tsv is wrong.\n"
        f"Expected: {repr(expected)}\n"
        f"Got:      {repr(actual)}"
    )


def test_normalized_users_no_trailing_whitespace():
    with open(NORMALIZED_USERS, "r") as f:
        for i, line in enumerate(f, start=1):
            stripped = line.rstrip("\n")
            assert stripped == stripped.rstrip(), (
                f"normalized_users.tsv line {i} has trailing whitespace: {repr(stripped)}"
            )


def test_normalized_users_tab_separated():
    lines = read_lines(NORMALIZED_USERS)
    for i, line in enumerate(lines, start=1):
        fields = line.split("\t")
        assert len(fields) == 5, (
            f"normalized_users.tsv line {i} should have 5 tab-separated fields, "
            f"but found {len(fields)}. Line: {repr(line)}"
        )


def test_normalized_users_data_rows():
    lines = read_lines(NORMALIZED_USERS)
    expected_rows = [
        "user_id\tfull_name\temail\tdepartment\tstatus",
        "U001\tAlice Marsh\talice@example.com\tengineering\tactive",
        "U002\tBob Chen\tbob@example.com\tmarketing\tinactive",
        "U003\tCarol Singh\tcarol@example.com\tsales\tactive",
        "U004\tDan Okafor\tdan@example.com\tengineering\tsuspended",
        "U005\tEve Torres\teve@example.com\thr\tactive",
    ]
    assert len(lines) == len(expected_rows), (
        f"normalized_users.tsv has {len(lines)} lines but expected {len(expected_rows)}."
    )
    for i, (actual, expected) in enumerate(zip(lines, expected_rows), start=1):
        assert actual == expected, (
            f"normalized_users.tsv line {i} mismatch.\n"
            f"Expected: {repr(expected)}\n"
            f"Got:      {repr(actual)}"
        )


# ---------------------------------------------------------------------------
# combined_report.tsv — existence and basic structure
# ---------------------------------------------------------------------------

def test_combined_report_exists():
    assert os.path.isfile(COMBINED_REPORT), (
        f"File '{COMBINED_REPORT}' does not exist. "
        "The task requires producing this file."
    )


def test_combined_report_line_count():
    lines = read_lines(COMBINED_REPORT)
    assert len(lines) == 6, (
        f"'{COMBINED_REPORT}' should have exactly 6 non-empty lines "
        f"(1 header + 5 data rows), but found {len(lines)}."
    )


def test_combined_report_header():
    lines = read_lines(COMBINED_REPORT)
    expected = "user_id\tfull_name\temail\tengagement_score\tlogin_count\tcountry\tcity\tstatus"
    actual = lines[0]
    assert actual == expected, (
        f"Header of combined_report.tsv is wrong.\n"
        f"Expected: {repr(expected)}\n"
        f"Got:      {repr(actual)}"
    )


def test_combined_report_no_trailing_whitespace():
    with open(COMBINED_REPORT, "r") as f:
        for i, line in enumerate(f, start=1):
            stripped = line.rstrip("\n")
            assert stripped == stripped.rstrip(), (
                f"combined_report.tsv line {i} has trailing whitespace: {repr(stripped)}"
            )


def test_combined_report_tab_separated():
    lines = read_lines(COMBINED_REPORT)
    for i, line in enumerate(lines, start=1):
        fields = line.split("\t")
        assert len(fields) == 8, (
            f"combined_report.tsv line {i} should have 8 tab-separated fields, "
            f"but found {len(fields)}. Line: {repr(line)}"
        )


def test_combined_report_row2():
    """Row 2 (first data row) — U001."""
    lines = read_lines(COMBINED_REPORT)
    expected = "U001\tAlice Marsh\talice@example.com\t87\t142\tUSA\tNew York\tactive"
    actual = lines[1]
    assert actual == expected, (
        f"combined_report.tsv row 2 (U001) mismatch.\n"
        f"Expected: {repr(expected)}\n"
        f"Got:      {repr(actual)}"
    )


def test_combined_report_row5():
    """Row 5 (fourth data row) — U004."""
    lines = read_lines(COMBINED_REPORT)
    expected = "U004\tDan Okafor\tdan@example.com\t12\t5\tNigeria\tLagos\tsuspended"
    actual = lines[4]
    assert actual == expected, (
        f"combined_report.tsv row 5 (U004) mismatch.\n"
        f"Expected: {repr(expected)}\n"
        f"Got:      {repr(actual)}"
    )


def test_combined_report_all_data_rows():
    lines = read_lines(COMBINED_REPORT)
    expected_rows = [
        "user_id\tfull_name\temail\tengagement_score\tlogin_count\tcountry\tcity\tstatus",
        "U001\tAlice Marsh\talice@example.com\t87\t142\tUSA\tNew York\tactive",
        "U002\tBob Chen\tbob@example.com\t34\t23\tCanada\tToronto\tinactive",
        "U003\tCarol Singh\tcarol@example.com\t76\t98\tUK\tLondon\tactive",
        "U004\tDan Okafor\tdan@example.com\t12\t5\tNigeria\tLagos\tsuspended",
        "U005\tEve Torres\teve@example.com\t95\t211\tMexico\tMexico City\tactive",
    ]
    assert len(lines) == len(expected_rows), (
        f"combined_report.tsv has {len(lines)} lines but expected {len(expected_rows)}."
    )
    for i, (actual, expected) in enumerate(zip(lines, expected_rows), start=1):
        assert actual == expected, (
            f"combined_report.tsv line {i} mismatch.\n"
            f"Expected: {repr(expected)}\n"
            f"Got:      {repr(actual)}"
        )