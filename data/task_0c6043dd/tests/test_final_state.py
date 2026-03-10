# test_final_state.py

import os
import pytest

OUTPUT_PATH = "/home/user/data/category_revenue.txt"
SALES_CSV_PATH = "/home/user/data/sales.csv"

EXPECTED_LINES = [
    "Clothing: 1670",
    "Electronics: 11930",
    "Furniture: 2490",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES)


def test_output_file_exists():
    assert os.path.isfile(OUTPUT_PATH), (
        f"Output file '{OUTPUT_PATH}' does not exist. "
        "The task requires creating this file with category revenue data."
    )


def test_output_file_is_readable():
    assert os.access(OUTPUT_PATH, os.R_OK), (
        f"Output file '{OUTPUT_PATH}' exists but is not readable."
    )


def test_output_file_has_exactly_three_lines():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 3, (
        f"Expected exactly 3 lines in '{OUTPUT_PATH}', but found {len(lines)}.\n"
        f"File content:\n{content!r}"
    )


def test_output_file_no_blank_lines():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"Output file '{OUTPUT_PATH}' contains blank lines at line numbers: {blank_lines}.\n"
        "The file should contain only category lines with no blank lines."
    )


def test_output_file_no_trailing_whitespace_per_line():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    offending = [(i + 1, repr(line)) for i, line in enumerate(lines) if line != line.rstrip()]
    assert not offending, (
        f"Output file '{OUTPUT_PATH}' has lines with trailing whitespace:\n"
        + "\n".join(f"  Line {ln}: {val}" for ln, val in offending)
    )


def test_output_file_clothing_line():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert lines[0] == "Clothing: 1670", (
        f"First line of '{OUTPUT_PATH}' is incorrect.\n"
        f"Expected: 'Clothing: 1670'\n"
        f"Got:      {lines[0]!r}"
    )


def test_output_file_electronics_line():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert lines[1] == "Electronics: 11930", (
        f"Second line of '{OUTPUT_PATH}' is incorrect.\n"
        f"Expected: 'Electronics: 11930'\n"
        f"Got:      {lines[1]!r}"
    )


def test_output_file_furniture_line():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert lines[2] == "Furniture: 2490", (
        f"Third line of '{OUTPUT_PATH}' is incorrect.\n"
        f"Expected: 'Furniture: 2490'\n"
        f"Got:      {lines[2]!r}"
    )


def test_output_file_sorted_alphabetically():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.read().splitlines()
    categories = []
    for line in lines:
        if ": " in line:
            category = line.split(": ")[0]
            categories.append(category)
    assert categories == sorted(categories), (
        f"Categories in '{OUTPUT_PATH}' are not sorted alphabetically.\n"
        f"Expected order: {sorted(categories)}\n"
        f"Got order:      {categories}"
    )


def test_output_file_exact_content():
    with open(OUTPUT_PATH, "r") as f:
        actual_content = f.read()
    # Strip trailing newline for comparison but ensure content matches exactly
    actual_stripped = actual_content.strip()
    assert actual_stripped == EXPECTED_CONTENT, (
        f"Content of '{OUTPUT_PATH}' does not match expected.\n"
        f"Expected:\n{EXPECTED_CONTENT!r}\n\n"
        f"Got:\n{actual_stripped!r}"
    )


def test_output_file_revenue_values_are_integers():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.read().splitlines()
    for line in lines:
        assert ": " in line, (
            f"Line {line!r} in '{OUTPUT_PATH}' does not match expected format '<category>: <revenue>'."
        )
        parts = line.split(": ", 1)
        revenue_str = parts[1]
        assert revenue_str.isdigit(), (
            f"Revenue value {revenue_str!r} in line {line!r} is not a plain integer. "
            "No decimal point or dollar sign should be present."
        )


def test_output_file_no_header():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.read().splitlines()
    # Ensure no line looks like a header (e.g., "category,revenue" or "Category Revenue")
    for line in lines:
        assert "," not in line, (
            f"Line {line!r} in '{OUTPUT_PATH}' contains a comma, which suggests a CSV header or wrong format."
        )
        assert "category" not in line.lower() or ": " in line, (
            f"Line {line!r} in '{OUTPUT_PATH}' looks like a header line, which is not allowed."
        )


def test_clothing_revenue_correct_value():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.read().splitlines()
    clothing_lines = [l for l in lines if l.startswith("Clothing:")]
    assert len(clothing_lines) == 1, (
        f"Expected exactly one 'Clothing' line in '{OUTPUT_PATH}', found {len(clothing_lines)}."
    )
    assert clothing_lines[0] == "Clothing: 1670", (
        f"Clothing revenue is incorrect.\n"
        f"Expected: 'Clothing: 1670'\n"
        f"Got:      {clothing_lines[0]!r}\n"
        "Clothing revenue = (5×90) + (12×60) + (20×25) = 450 + 720 + 500 = 1670"
    )


def test_electronics_revenue_correct_value():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.read().splitlines()
    electronics_lines = [l for l in lines if l.startswith("Electronics:")]
    assert len(electronics_lines) == 1, (
        f"Expected exactly one 'Electronics' line in '{OUTPUT_PATH}', found {len(electronics_lines)}."
    )
    assert electronics_lines[0] == "Electronics: 11930", (
        f"Electronics revenue is incorrect.\n"
        f"Expected: 'Electronics: 11930'\n"
        f"Got:      {electronics_lines[0]!r}\n"
        "Electronics revenue = (3×1200) + (7×650) + (6×430) + (15×80) = 3600 + 4550 + 2580 + 1200 = 11930"
    )


def test_furniture_revenue_correct_value():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.read().splitlines()
    furniture_lines = [l for l in lines if l.startswith("Furniture:")]
    assert len(furniture_lines) == 1, (
        f"Expected exactly one 'Furniture' line in '{OUTPUT_PATH}', found {len(furniture_lines)}."
    )
    assert furniture_lines[0] == "Furniture: 2490", (
        f"Furniture revenue is incorrect.\n"
        f"Expected: 'Furniture: 2490'\n"
        f"Got:      {furniture_lines[0]!r}\n"
        "Furniture revenue = (10×85) + (4×320) + (8×45) = 850 + 1280 + 360 = 2490"
    )


def test_sales_csv_still_intact():
    """Ensure the original sales.csv file was not modified or deleted."""
    assert os.path.isfile(SALES_CSV_PATH), (
        f"Original file '{SALES_CSV_PATH}' no longer exists. "
        "The task should not delete or move the source CSV file."
    )
    with open(SALES_CSV_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")
    expected_header = "date,category,product,units_sold,unit_price"
    assert first_line == expected_header, (
        f"The header of '{SALES_CSV_PATH}' appears to have been modified.\n"
        f"Expected: {expected_header!r}\n"
        f"Got:      {first_line!r}"
    )