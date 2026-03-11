# test_final_state.py

import os
import pytest

SUMMARY_PATH = "/home/user/data/sales_summary.txt"

EXPECTED_CONTENT = """\
=== SALES DATA SUMMARY ===
Total records: 10
Total units sold: 430
Total revenue: 22650

=== REVENUE BY REGION ===
  South: 8300
  North: 7650
  West: 3950
  East: 2750

=== TOP PRODUCT BY UNITS SOLD ===
  Widget: 200
"""


def test_summary_file_exists():
    assert os.path.isfile(SUMMARY_PATH), (
        f"Summary file '{SUMMARY_PATH}' does not exist. "
        "The task requires creating this file."
    )


def test_summary_file_is_readable():
    assert os.access(SUMMARY_PATH, os.R_OK), (
        f"Summary file '{SUMMARY_PATH}' exists but is not readable."
    )


def test_summary_file_exact_content():
    with open(SUMMARY_PATH, "r") as f:
        actual = f.read()

    assert actual == EXPECTED_CONTENT, (
        f"Content of '{SUMMARY_PATH}' does not match expected.\n\n"
        f"--- EXPECTED (repr) ---\n{repr(EXPECTED_CONTENT)}\n\n"
        f"--- ACTUAL (repr) ---\n{repr(actual)}"
    )


def test_summary_ends_with_single_newline():
    with open(SUMMARY_PATH, "r") as f:
        actual = f.read()

    assert actual.endswith("\n"), (
        f"'{SUMMARY_PATH}' must end with a newline character."
    )
    assert not actual.endswith("\n\n"), (
        f"'{SUMMARY_PATH}' must end with exactly one trailing newline, "
        "but it ends with more than one."
    )


def test_summary_header_line():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    assert lines[0].rstrip("\n") == "=== SALES DATA SUMMARY ===", (
        f"First line of '{SUMMARY_PATH}' should be '=== SALES DATA SUMMARY ===', "
        f"but got: {repr(lines[0].rstrip(chr(10)))}"
    )


def test_summary_total_records():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "Total records: 10" in content, (
        f"'{SUMMARY_PATH}' should contain 'Total records: 10', "
        f"but it was not found.\nActual content:\n{content}"
    )


def test_summary_total_units_sold():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "Total units sold: 430" in content, (
        f"'{SUMMARY_PATH}' should contain 'Total units sold: 430', "
        f"but it was not found.\nActual content:\n{content}"
    )


def test_summary_total_revenue():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "Total revenue: 22650" in content, (
        f"'{SUMMARY_PATH}' should contain 'Total revenue: 22650', "
        f"but it was not found.\nActual content:\n{content}"
    )


def test_summary_revenue_by_region_header():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "=== REVENUE BY REGION ===" in content, (
        f"'{SUMMARY_PATH}' should contain '=== REVENUE BY REGION ===', "
        f"but it was not found.\nActual content:\n{content}"
    )


def test_summary_revenue_by_region_values():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    expected_region_lines = [
        "  South: 8300",
        "  North: 7650",
        "  West: 3950",
        "  East: 2750",
    ]
    for line in expected_region_lines:
        assert line in content, (
            f"'{SUMMARY_PATH}' should contain the line {repr(line)}, "
            f"but it was not found.\nActual content:\n{content}"
        )


def test_summary_revenue_by_region_order():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    # Find the REVENUE BY REGION section
    region_section_start = None
    for i, line in enumerate(lines):
        if line.strip() == "=== REVENUE BY REGION ===":
            region_section_start = i
            break

    assert region_section_start is not None, (
        f"Could not find '=== REVENUE BY REGION ===' in '{SUMMARY_PATH}'."
    )

    # Collect region lines (lines with two leading spaces after the header)
    region_lines = []
    for line in lines[region_section_start + 1:]:
        stripped = line.rstrip("\n")
        if stripped == "":
            break
        if stripped.startswith("  "):
            region_lines.append(stripped)

    expected_order = [
        "  South: 8300",
        "  North: 7650",
        "  West: 3950",
        "  East: 2750",
    ]

    assert region_lines == expected_order, (
        f"Revenue by region lines are not in the correct order.\n"
        f"Expected: {expected_order}\n"
        f"Actual:   {region_lines}"
    )


def test_summary_top_product_header():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "=== TOP PRODUCT BY UNITS SOLD ===" in content, (
        f"'{SUMMARY_PATH}' should contain '=== TOP PRODUCT BY UNITS SOLD ===', "
        f"but it was not found.\nActual content:\n{content}"
    )


def test_summary_top_product_value():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "  Widget: 200" in content, (
        f"'{SUMMARY_PATH}' should contain '  Widget: 200' (with two leading spaces), "
        f"but it was not found.\nActual content:\n{content}"
    )


def test_summary_no_decimal_points():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    import re
    # Check that no numeric values have decimal points
    decimal_matches = re.findall(r'\d+\.\d+', content)
    assert not decimal_matches, (
        f"'{SUMMARY_PATH}' contains decimal numbers {decimal_matches}, "
        "but all numeric values should be plain integers."
    )


def test_summary_no_commas_in_numbers():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    import re
    # Check for numbers formatted with commas like 1,000
    comma_number_matches = re.findall(r'\d{1,3}(?:,\d{3})+', content)
    assert not comma_number_matches, (
        f"'{SUMMARY_PATH}' contains comma-formatted numbers {comma_number_matches}, "
        "but all numeric values should be plain integers without commas."
    )


def test_summary_no_dollar_signs():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "$" not in content, (
        f"'{SUMMARY_PATH}' contains dollar signs, "
        "but all numeric values should be plain integers without dollar signs."
    )


def test_summary_blank_line_between_sections():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    # Strip newlines for comparison
    stripped_lines = [line.rstrip("\n") for line in lines]

    # Find section header indices
    section_headers = [
        "=== SALES DATA SUMMARY ===",
        "=== REVENUE BY REGION ===",
        "=== TOP PRODUCT BY UNITS SOLD ===",
    ]

    header_indices = {}
    for i, line in enumerate(stripped_lines):
        if line in section_headers:
            header_indices[line] = i

    assert len(header_indices) == 3, (
        f"Expected to find all 3 section headers in '{SUMMARY_PATH}', "
        f"but found: {list(header_indices.keys())}"
    )

    idx1 = header_indices["=== SALES DATA SUMMARY ==="]
    idx2 = header_indices["=== REVENUE BY REGION ==="]
    idx3 = header_indices["=== TOP PRODUCT BY UNITS SOLD ==="]

    # There should be a blank line immediately before each subsequent section header
    assert stripped_lines[idx2 - 1] == "", (
        f"There should be a blank line before '=== REVENUE BY REGION ===', "
        f"but line {idx2} (0-indexed) is: {repr(stripped_lines[idx2 - 1])}"
    )

    assert stripped_lines[idx3 - 1] == "", (
        f"There should be a blank line before '=== TOP PRODUCT BY UNITS SOLD ===', "
        f"but line {idx3} (0-indexed) is: {repr(stripped_lines[idx3 - 1])}"
    )


def test_summary_section_order():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    pos_summary = content.find("=== SALES DATA SUMMARY ===")
    pos_region = content.find("=== REVENUE BY REGION ===")
    pos_top = content.find("=== TOP PRODUCT BY UNITS SOLD ===")

    assert pos_summary != -1, (
        f"'=== SALES DATA SUMMARY ===' not found in '{SUMMARY_PATH}'."
    )
    assert pos_region != -1, (
        f"'=== REVENUE BY REGION ===' not found in '{SUMMARY_PATH}'."
    )
    assert pos_top != -1, (
        f"'=== TOP PRODUCT BY UNITS SOLD ===' not found in '{SUMMARY_PATH}'."
    )

    assert pos_summary < pos_region < pos_top, (
        f"Sections are not in the correct order in '{SUMMARY_PATH}'.\n"
        f"SALES DATA SUMMARY at pos {pos_summary}, "
        f"REVENUE BY REGION at pos {pos_region}, "
        f"TOP PRODUCT BY UNITS SOLD at pos {pos_top}."
    )