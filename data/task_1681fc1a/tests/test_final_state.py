# test_final_state.py

import os
import pytest

SALES_CSV_PATH = "/home/user/data/sales.csv"
SALES_CLEAN_PATH = "/home/user/data/sales_clean.csv"
SALES_SUMMARY_PATH = "/home/user/data/sales_summary.txt"

EXPECTED_CLEAN_CONTENT = """transaction_id,product,quantity,unit_price,region
T001,widget,5,12.50,north
T003,widget,3,8.00,east
T004,doohickey,2,15.00,west
T007,thingamajig,4,20.00,south
T009,widget,10,12.50,east
T011,gadget,3,9.99,north
T013,doohickey,6,15.00,west
T015,gadget,7,9.99,south"""

EXPECTED_SUMMARY_CONTENT = (
    "Sales Summary\n"
    "=============\n"
    "\n"
    "east: 149.00\n"
    "north: 92.47\n"
    "south: 149.93\n"
    "west: 120.00\n"
    "Total: 511.40"
)


# ---------------------------------------------------------------------------
# sales_clean.csv tests
# ---------------------------------------------------------------------------

def test_sales_clean_exists():
    assert os.path.isfile(SALES_CLEAN_PATH), (
        f"File '{SALES_CLEAN_PATH}' does not exist. "
        "The cleaned CSV file must be created after processing."
    )


def test_sales_clean_is_readable():
    assert os.access(SALES_CLEAN_PATH, os.R_OK), (
        f"File '{SALES_CLEAN_PATH}' is not readable."
    )


def test_sales_clean_header():
    with open(SALES_CLEAN_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")
    expected_header = "transaction_id,product,quantity,unit_price,region"
    assert first_line == expected_header, (
        f"Header of '{SALES_CLEAN_PATH}' is incorrect.\n"
        f"Expected: {repr(expected_header)}\n"
        f"Actual:   {repr(first_line)}"
    )


def test_sales_clean_row_count():
    with open(SALES_CLEAN_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    # 1 header + 8 valid data rows = 9 lines
    assert len(lines) == 9, (
        f"Expected 9 non-empty lines (1 header + 8 valid data rows) in '{SALES_CLEAN_PATH}', "
        f"but found {len(lines)} non-empty lines."
    )


def test_sales_clean_content_exact():
    with open(SALES_CLEAN_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()
    expected_lines = EXPECTED_CLEAN_CONTENT.strip().splitlines()

    assert len(actual_lines) == len(expected_lines), (
        f"Expected {len(expected_lines)} lines in '{SALES_CLEAN_PATH}', "
        f"but found {len(actual_lines)} lines.\n"
        f"Actual content:\n{content}"
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, expected_lines), start=1):
        assert actual == expected, (
            f"Line {i} of '{SALES_CLEAN_PATH}' does not match.\n"
            f"Expected: {repr(expected)}\n"
            f"Actual:   {repr(actual)}"
        )


def test_sales_clean_contains_valid_rows():
    with open(SALES_CLEAN_PATH, "r") as f:
        content = f.read()

    valid_rows = [
        "T001,widget,5,12.50,north",
        "T003,widget,3,8.00,east",
        "T004,doohickey,2,15.00,west",
        "T007,thingamajig,4,20.00,south",
        "T009,widget,10,12.50,east",
        "T011,gadget,3,9.99,north",
        "T013,doohickey,6,15.00,west",
        "T015,gadget,7,9.99,south",
    ]
    for row in valid_rows:
        assert row in content, (
            f"Expected valid row '{row}' to be present in '{SALES_CLEAN_PATH}'."
        )


def test_sales_clean_excludes_invalid_rows():
    with open(SALES_CLEAN_PATH, "r") as f:
        content = f.read()

    invalid_rows = [
        "T002,gadget,abc,9.99,south",   # non-numeric quantity
        "T005,gadget,1,9.99,",           # empty region
        "T006,widget,0,12.50,north",     # zero quantity
        "T008,gadget,2,9.99,midwest",    # invalid region
        "T010,doohickey,,15.00,west",    # empty quantity
        "T012,thingamajig,1,-5.00,south",# negative price
        "T014,widget,2,8.00",            # missing field
    ]
    for row in invalid_rows:
        assert row not in content, (
            f"Invalid row '{row}' should NOT be present in '{SALES_CLEAN_PATH}', "
            "but it was found."
        )


def test_sales_clean_column_order():
    """Verify that the columns appear in the correct order."""
    with open(SALES_CLEAN_PATH, "r") as f:
        lines = f.readlines()

    header = lines[0].rstrip("\n")
    assert header == "transaction_id,product,quantity,unit_price,region", (
        f"Column order in '{SALES_CLEAN_PATH}' is incorrect.\n"
        f"Expected: 'transaction_id,product,quantity,unit_price,region'\n"
        f"Actual:   '{header}'"
    )

    # Spot-check a data row for correct field order
    # T001,widget,5,12.50,north
    data_rows = [line.rstrip("\n") for line in lines[1:] if line.strip()]
    t001_row = next((r for r in data_rows if r.startswith("T001,")), None)
    assert t001_row is not None, (
        f"Row T001 not found in '{SALES_CLEAN_PATH}'."
    )
    fields = t001_row.split(",")
    assert len(fields) == 5, (
        f"Row T001 in '{SALES_CLEAN_PATH}' does not have exactly 5 fields: {t001_row}"
    )
    assert fields[0] == "T001", f"Field 0 (transaction_id) of T001 incorrect: {fields[0]}"
    assert fields[1] == "widget", f"Field 1 (product) of T001 incorrect: {fields[1]}"
    assert fields[2] == "5", f"Field 2 (quantity) of T001 incorrect: {fields[2]}"
    assert fields[3] == "12.50", f"Field 3 (unit_price) of T001 incorrect: {fields[3]}"
    assert fields[4] == "north", f"Field 4 (region) of T001 incorrect: {fields[4]}"


# ---------------------------------------------------------------------------
# sales_summary.txt tests
# ---------------------------------------------------------------------------

def test_sales_summary_exists():
    assert os.path.isfile(SALES_SUMMARY_PATH), (
        f"File '{SALES_SUMMARY_PATH}' does not exist. "
        "The summary file must be created after processing."
    )


def test_sales_summary_is_readable():
    assert os.access(SALES_SUMMARY_PATH, os.R_OK), (
        f"File '{SALES_SUMMARY_PATH}' is not readable."
    )


def test_sales_summary_content_exact():
    with open(SALES_SUMMARY_PATH, "r") as f:
        content = f.read()

    assert content == EXPECTED_SUMMARY_CONTENT, (
        f"Content of '{SALES_SUMMARY_PATH}' does not match expected.\n"
        f"Expected:\n{repr(EXPECTED_SUMMARY_CONTENT)}\n"
        f"Actual:\n{repr(content)}"
    )


def test_sales_summary_header_lines():
    with open(SALES_SUMMARY_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 2, (
        f"'{SALES_SUMMARY_PATH}' has fewer than 2 lines."
    )
    assert lines[0] == "Sales Summary", (
        f"First line of '{SALES_SUMMARY_PATH}' should be 'Sales Summary'.\n"
        f"Actual: {repr(lines[0])}"
    )
    assert lines[1] == "=============", (
        f"Second line of '{SALES_SUMMARY_PATH}' should be '=============`.\n"
        f"Actual: {repr(lines[1])}"
    )


def test_sales_summary_blank_line_after_separator():
    with open(SALES_SUMMARY_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 3, (
        f"'{SALES_SUMMARY_PATH}' has fewer than 3 lines; expected blank line after separator."
    )
    assert lines[2] == "", (
        f"Line 3 of '{SALES_SUMMARY_PATH}' should be blank (empty line after '=============').\n"
        f"Actual: {repr(lines[2])}"
    )


def test_sales_summary_region_values():
    with open(SALES_SUMMARY_PATH, "r") as f:
        content = f.read()

    expected_regions = {
        "east": "149.00",
        "north": "92.47",
        "south": "149.93",
        "west": "120.00",
    }

    for region, total in expected_regions.items():
        expected_line = f"{region}: {total}"
        assert expected_line in content, (
            f"Expected line '{expected_line}' not found in '{SALES_SUMMARY_PATH}'.\n"
            f"Actual content:\n{content}"
        )


def test_sales_summary_grand_total():
    with open(SALES_SUMMARY_PATH, "r") as f:
        content = f.read()

    expected_total_line = "Total: 511.40"
    assert expected_total_line in content, (
        f"Expected grand total line '{expected_total_line}' not found in '{SALES_SUMMARY_PATH}'.\n"
        f"Actual content:\n{content}"
    )


def test_sales_summary_regions_alphabetical_order():
    with open(SALES_SUMMARY_PATH, "r") as f:
        lines = f.read().splitlines()

    # Regions start after the blank line (index 3 onward)
    # lines[0] = "Sales Summary"
    # lines[1] = "============="
    # lines[2] = ""
    # lines[3..6] = region lines
    # lines[7] = "Total: ..."
    region_lines = [l for l in lines[3:] if l and not l.startswith("Total:")]

    regions_found = []
    for line in region_lines:
        parts = line.split(":")
        if parts:
            regions_found.append(parts[0].strip())

    assert regions_found == sorted(regions_found), (
        f"Regions in '{SALES_SUMMARY_PATH}' are not in alphabetical order.\n"
        f"Found order: {regions_found}\n"
        f"Expected order: {sorted(regions_found)}"
    )

    expected_region_order = ["east", "north", "south", "west"]
    assert regions_found == expected_region_order, (
        f"Region order in '{SALES_SUMMARY_PATH}' is incorrect.\n"
        f"Expected: {expected_region_order}\n"
        f"Actual:   {regions_found}"
    )


def test_sales_summary_no_trailing_newline():
    with open(SALES_SUMMARY_PATH, "rb") as f:
        raw = f.read()

    assert not raw.endswith(b"\n"), (
        f"'{SALES_SUMMARY_PATH}' should not end with a trailing newline, but it does.\n"
        f"Last 20 bytes: {repr(raw[-20:])}"
    )


def test_sales_summary_total_line_is_last():
    with open(SALES_SUMMARY_PATH, "r") as f:
        lines = f.read().splitlines()

    assert lines[-1].startswith("Total:"), (
        f"The last line of '{SALES_SUMMARY_PATH}' should start with 'Total:', "
        f"but found: {repr(lines[-1])}"
    )


# ---------------------------------------------------------------------------
# Original sales.csv must remain unchanged
# ---------------------------------------------------------------------------

EXPECTED_ORIGINAL_CONTENT = """transaction_id,product,quantity,unit_price,region
T001,widget,5,12.50,north
T002,gadget,abc,9.99,south
T003,widget,3,8.00,east
T004,doohickey,2,15.00,west
T005,gadget,1,9.99,
T006,widget,0,12.50,north
T007,thingamajig,4,20.00,south
T008,gadget,2,9.99,midwest
T009,widget,10,12.50,east
T010,doohickey,,15.00,west
T011,gadget,3,9.99,north
T012,thingamajig,1,-5.00,south
T013,doohickey,6,15.00,west
T014,widget,2,8.00
T015,gadget,7,9.99,south"""


def test_original_sales_csv_unchanged():
    with open(SALES_CSV_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()
    expected_lines = EXPECTED_ORIGINAL_CONTENT.strip().splitlines()

    assert len(actual_lines) == len(expected_lines), (
        f"Original '{SALES_CSV_PATH}' appears to have been modified: "
        f"expected {len(expected_lines)} lines, found {len(actual_lines)} lines."
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, expected_lines), start=1):
        assert actual == expected, (
            f"Line {i} of original '{SALES_CSV_PATH}' was modified.\n"
            f"Expected: {repr(expected)}\n"
            f"Actual:   {repr(actual)}"
        )