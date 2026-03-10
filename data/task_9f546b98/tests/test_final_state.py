# test_final_state.py

import os
import re
import pytest

HIGH_REVENUE_CSV_PATH = "/home/user/data/high_revenue.csv"
REPORT_TXT_PATH = "/home/user/data/report.txt"

EXPECTED_HIGH_REVENUE_LINES = [
    "region,category,month,units_sold,revenue",
    "North,Electronics,January,120,8400",
    "East,Electronics,January,98,6860",
    "North,Furniture,February,15,7500",
    "South,Electronics,February,80,5600",
    "West,Electronics,February,110,7700",
    "East,Furniture,March,18,9000",
]

EXPECTED_REPORT_LINES = [
    "REGION,CATEGORY,MONTH,UNITS_SOLD,REVENUE",
    "Northern,Electronics,January,120,8400",
    "East,Electronics,January,98,6860",
    "Northern,Furniture,February,15,7500",
    "Southern,Electronics,February,80,5600",
    "West,Electronics,February,110,7700",
    "East,Furniture,March,18,9000",
]


# ---------------------------------------------------------------------------
# high_revenue.csv tests
# ---------------------------------------------------------------------------

def test_high_revenue_csv_exists():
    assert os.path.isfile(HIGH_REVENUE_CSV_PATH), (
        f"File '{HIGH_REVENUE_CSV_PATH}' does not exist. "
        "The awk step must create this file."
    )


def test_high_revenue_csv_is_readable():
    assert os.access(HIGH_REVENUE_CSV_PATH, os.R_OK), (
        f"File '{HIGH_REVENUE_CSV_PATH}' is not readable."
    )


def test_high_revenue_csv_line_count():
    with open(HIGH_REVENUE_CSV_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    assert len(lines) == 7, (
        f"'{HIGH_REVENUE_CSV_PATH}' should have exactly 7 lines "
        f"(1 header + 6 data rows), but has {len(lines)} lines.\n"
        f"Actual lines:\n" + "\n".join(lines)
    )


def test_high_revenue_csv_header():
    with open(HIGH_REVENUE_CSV_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    expected_header = "region,category,month,units_sold,revenue"
    assert lines[0] == expected_header, (
        f"First line of '{HIGH_REVENUE_CSV_PATH}' is not the expected header.\n"
        f"Expected: '{expected_header}'\n"
        f"Actual:   '{lines[0]}'"
    )


def test_high_revenue_csv_exact_content():
    with open(HIGH_REVENUE_CSV_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    assert lines == EXPECTED_HIGH_REVENUE_LINES, (
        f"Content of '{HIGH_REVENUE_CSV_PATH}' does not match expected.\n"
        f"Expected:\n" + "\n".join(EXPECTED_HIGH_REVENUE_LINES) +
        f"\n\nActual:\n" + "\n".join(lines)
    )


def test_high_revenue_csv_all_revenues_above_5000():
    with open(HIGH_REVENUE_CSV_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    # Skip header
    for i, line in enumerate(lines[1:], start=2):
        parts = line.split(",")
        assert len(parts) == 5, (
            f"Line {i} in '{HIGH_REVENUE_CSV_PATH}' does not have 5 columns: '{line}'"
        )
        try:
            revenue = float(parts[4])
        except ValueError:
            pytest.fail(
                f"Line {i} in '{HIGH_REVENUE_CSV_PATH}' has non-numeric revenue: '{parts[4]}'"
            )
        assert revenue > 5000, (
            f"Line {i} in '{HIGH_REVENUE_CSV_PATH}' has revenue {revenue} which is not > 5000: '{line}'"
        )


def test_high_revenue_csv_no_dollar_signs():
    with open(HIGH_REVENUE_CSV_PATH, "r") as f:
        content = f.read()
    assert "$" not in content, (
        f"'{HIGH_REVENUE_CSV_PATH}' contains a dollar sign '$', "
        "which should not be present — raw CSV data only."
    )


def test_high_revenue_csv_preserves_original_order():
    with open(HIGH_REVENUE_CSV_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    data_lines = lines[1:]
    expected_data = EXPECTED_HIGH_REVENUE_LINES[1:]
    assert data_lines == expected_data, (
        f"Data rows in '{HIGH_REVENUE_CSV_PATH}' are not in the expected original order.\n"
        f"Expected:\n" + "\n".join(expected_data) +
        f"\n\nActual:\n" + "\n".join(data_lines)
    )


# ---------------------------------------------------------------------------
# report.txt tests
# ---------------------------------------------------------------------------

def test_report_txt_exists():
    assert os.path.isfile(REPORT_TXT_PATH), (
        f"File '{REPORT_TXT_PATH}' does not exist. "
        "The sed step must create this file."
    )


def test_report_txt_is_readable():
    assert os.access(REPORT_TXT_PATH, os.R_OK), (
        f"File '{REPORT_TXT_PATH}' is not readable."
    )


def test_report_txt_line_count():
    with open(REPORT_TXT_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    assert len(lines) == 7, (
        f"'{REPORT_TXT_PATH}' should have exactly 7 lines "
        f"(1 header + 6 data rows), but has {len(lines)} lines.\n"
        f"Actual lines:\n" + "\n".join(lines)
    )


def test_report_txt_line1_uppercase_header():
    with open(REPORT_TXT_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    expected = "REGION,CATEGORY,MONTH,UNITS_SOLD,REVENUE"
    assert lines[0] == expected, (
        f"Line 1 of '{REPORT_TXT_PATH}' is not the expected uppercase header.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[0]}'"
    )


def test_report_txt_line2_northern():
    with open(REPORT_TXT_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    expected = "Northern,Electronics,January,120,8400"
    assert lines[1] == expected, (
        f"Line 2 of '{REPORT_TXT_PATH}' is not as expected.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[1]}'"
    )


def test_report_txt_line3_east():
    with open(REPORT_TXT_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    expected = "East,Electronics,January,98,6860"
    assert lines[2] == expected, (
        f"Line 3 of '{REPORT_TXT_PATH}' is not as expected.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[2]}'"
    )


def test_report_txt_line4_northern_furniture():
    with open(REPORT_TXT_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    expected = "Northern,Furniture,February,15,7500"
    assert lines[3] == expected, (
        f"Line 4 of '{REPORT_TXT_PATH}' is not as expected.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[3]}'"
    )


def test_report_txt_line5_southern():
    with open(REPORT_TXT_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    expected = "Southern,Electronics,February,80,5600"
    assert lines[4] == expected, (
        f"Line 5 of '{REPORT_TXT_PATH}' is not as expected.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[4]}'"
    )


def test_report_txt_exact_content():
    with open(REPORT_TXT_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    assert lines == EXPECTED_REPORT_LINES, (
        f"Content of '{REPORT_TXT_PATH}' does not match expected.\n"
        f"Expected:\n" + "\n".join(EXPECTED_REPORT_LINES) +
        f"\n\nActual:\n" + "\n".join(lines)
    )


def test_report_txt_no_bare_north():
    """No line in report.txt should contain the bare word 'North' (only 'Northern' is allowed)."""
    with open(REPORT_TXT_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    # 'North' not followed by 'ern' — i.e., bare 'North' as a standalone region token
    pattern = re.compile(r'\bNorth\b(?!ern)')
    offending = [line for line in lines if pattern.search(line)]
    assert not offending, (
        f"The following lines in '{REPORT_TXT_PATH}' still contain bare 'North' "
        f"instead of 'Northern':\n" + "\n".join(offending)
    )


def test_report_txt_no_bare_south():
    """No line in report.txt should contain the bare word 'South' (only 'Southern' is allowed)."""
    with open(REPORT_TXT_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    pattern = re.compile(r'\bSouth\b(?!ern)')
    offending = [line for line in lines if pattern.search(line)]
    assert not offending, (
        f"The following lines in '{REPORT_TXT_PATH}' still contain bare 'South' "
        f"instead of 'Southern':\n" + "\n".join(offending)
    )


def test_report_txt_contains_northern():
    with open(REPORT_TXT_PATH, "r") as f:
        content = f.read()
    assert "Northern" in content, (
        f"'{REPORT_TXT_PATH}' does not contain 'Northern'. "
        "The sed substitution of 'North' -> 'Northern' was not applied."
    )


def test_report_txt_contains_southern():
    with open(REPORT_TXT_PATH, "r") as f:
        content = f.read()
    assert "Southern" in content, (
        f"'{REPORT_TXT_PATH}' does not contain 'Southern'. "
        "The sed substitution of 'South' -> 'Southern' was not applied."
    )


def test_report_txt_no_lowercase_header():
    with open(REPORT_TXT_PATH, "r") as f:
        lines = f.read().strip().splitlines()
    lowercase_header = "region,category,month,units_sold,revenue"
    assert lines[0] != lowercase_header, (
        f"Line 1 of '{REPORT_TXT_PATH}' is still the lowercase header '{lowercase_header}'. "
        "It should have been replaced with the uppercase version."
    )


def test_report_txt_no_trailing_newline_issues():
    """File should not have excessive trailing blank lines."""
    with open(REPORT_TXT_PATH, "r") as f:
        raw = f.read()
    # Strip only right side to check for trailing blank lines
    stripped = raw.rstrip("\n")
    lines = stripped.splitlines()
    assert len(lines) == 7, (
        f"After stripping trailing newlines, '{REPORT_TXT_PATH}' should have 7 lines, "
        f"but has {len(lines)}. Possible trailing newline issue."
    )