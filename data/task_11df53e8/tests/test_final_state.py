# test_final_state.py

import os
import re
import pytest

FILTERED_CSV_PATH = "/home/user/data/filtered_sales.csv"
SALES_CSV_PATH = "/home/user/data/sales.csv"

EXPECTED_CONTENT = (
    "transaction_id,date,amount,status\n"
    "T001,2024-01-05,150.00,completed\n"
    "T004,2024-01-08,310.75,completed\n"
    "T006,2024-01-10,99.99,refunded\n"
    "T010,2024-01-14,60.00,refunded\n"
    "T011,2024-01-15,130.00,completed\n"
    "T013,2024-01-17,250.00,completed\n"
    "T015,2024-01-19,75.00,refunded\n"
)

EXPECTED_LINES = EXPECTED_CONTENT.splitlines()  # 8 elements (no trailing empty)


def test_filtered_csv_exists():
    assert os.path.isfile(FILTERED_CSV_PATH), (
        f"Output file does not exist: {FILTERED_CSV_PATH}\n"
        "The task requires creating this filtered CSV file."
    )


def test_filtered_csv_is_readable():
    assert os.access(FILTERED_CSV_PATH, os.R_OK), (
        f"Output file exists but is not readable: {FILTERED_CSV_PATH}"
    )


def test_filtered_csv_exact_content():
    with open(FILTERED_CSV_PATH, "rb") as f:
        raw_bytes = f.read()

    # Check Unix line endings (no carriage returns)
    assert b"\r" not in raw_bytes, (
        f"File {FILTERED_CSV_PATH} contains carriage return characters (\\r).\n"
        "The file must use Unix line endings (LF only)."
    )

    actual_content = raw_bytes.decode("utf-8")
    assert actual_content == EXPECTED_CONTENT, (
        f"Content of {FILTERED_CSV_PATH} does not match expected.\n"
        f"Expected:\n{EXPECTED_CONTENT!r}\n\n"
        f"Actual:\n{actual_content!r}"
    )


def test_filtered_csv_ends_with_newline():
    with open(FILTERED_CSV_PATH, "rb") as f:
        raw_bytes = f.read()
    assert raw_bytes.endswith(b"\n"), (
        f"File {FILTERED_CSV_PATH} does not end with a newline character.\n"
        "The file must end with a Unix newline after the last data row."
    )


def test_filtered_csv_header():
    with open(FILTERED_CSV_PATH, "r", newline="") as f:
        first_line = f.readline().rstrip("\n")
    expected_header = "transaction_id,date,amount,status"
    assert first_line == expected_header, (
        f"Header line mismatch in {FILTERED_CSV_PATH}.\n"
        f"Expected: {expected_header!r}\n"
        f"Got:      {first_line!r}"
    )


def test_filtered_csv_line_count():
    with open(FILTERED_CSV_PATH, "r", newline="") as f:
        content = f.read()
    lines = content.split("\n")
    # File ends with \n so split produces a trailing empty string
    non_empty_lines = [l for l in lines if l.strip() != ""]
    assert len(non_empty_lines) == 8, (
        f"Expected 8 non-blank lines (1 header + 7 data rows) in {FILTERED_CSV_PATH}.\n"
        f"Got {len(non_empty_lines)} non-blank lines.\n"
        f"Lines found: {non_empty_lines}"
    )


def test_filtered_csv_no_blank_lines():
    with open(FILTERED_CSV_PATH, "r", newline="") as f:
        content = f.read()
    # Strip trailing newline before checking for blank lines
    interior = content.rstrip("\n")
    lines = interior.split("\n")
    blank_lines = [i + 1 for i, l in enumerate(lines) if l.strip() == ""]
    assert not blank_lines, (
        f"File {FILTERED_CSV_PATH} contains blank lines at positions: {blank_lines}.\n"
        "The output file must have no blank lines."
    )


def test_filtered_csv_no_trailing_whitespace():
    with open(FILTERED_CSV_PATH, "r", newline="") as f:
        lines = f.readlines()
    offending = []
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        if stripped != stripped.rstrip():
            offending.append((i, repr(line)))
    assert not offending, (
        f"File {FILTERED_CSV_PATH} has trailing whitespace on the following lines:\n"
        + "\n".join(f"  Line {ln}: {content}" for ln, content in offending)
    )


def test_filtered_csv_columns_order():
    with open(FILTERED_CSV_PATH, "r", newline="") as f:
        header = f.readline().rstrip("\n")
    columns = header.split(",")
    expected_columns = ["transaction_id", "date", "amount", "status"]
    assert columns == expected_columns, (
        f"Column order/names mismatch in {FILTERED_CSV_PATH}.\n"
        f"Expected columns: {expected_columns}\n"
        f"Got columns:      {columns}"
    )


def test_filtered_csv_no_region_or_product_code_columns():
    with open(FILTERED_CSV_PATH, "r", newline="") as f:
        header = f.readline().rstrip("\n")
    columns = header.split(",")
    assert "region" not in columns, (
        f"Column 'region' should have been dropped but is present in {FILTERED_CSV_PATH}.\n"
        f"Header: {header!r}"
    )
    assert "product_code" not in columns, (
        f"Column 'product_code' should have been dropped but is present in {FILTERED_CSV_PATH}.\n"
        f"Header: {header!r}"
    )


def test_filtered_csv_data_rows():
    with open(FILTERED_CSV_PATH, "r", newline="") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    # lines[0] is header, lines[1..7] are data rows
    expected_data_rows = [
        "T001,2024-01-05,150.00,completed",
        "T004,2024-01-08,310.75,completed",
        "T006,2024-01-10,99.99,refunded",
        "T010,2024-01-14,60.00,refunded",
        "T011,2024-01-15,130.00,completed",
        "T013,2024-01-17,250.00,completed",
        "T015,2024-01-19,75.00,refunded",
    ]

    data_lines = [l for l in lines if l.strip() and l != "transaction_id,date,amount,status"]

    assert len(data_lines) == len(expected_data_rows), (
        f"Expected {len(expected_data_rows)} data rows in {FILTERED_CSV_PATH}, "
        f"got {len(data_lines)}.\n"
        f"Data rows found: {data_lines}"
    )

    for i, (actual, expected) in enumerate(zip(data_lines, expected_data_rows), start=1):
        assert actual == expected, (
            f"Data row {i} mismatch in {FILTERED_CSV_PATH}.\n"
            f"Expected: {expected!r}\n"
            f"Got:      {actual!r}"
        )


def test_filtered_csv_row_order():
    """Ensure rows appear in the same order as in the original file."""
    with open(FILTERED_CSV_PATH, "r", newline="") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    data_lines = [l for l in lines[1:] if l.strip()]
    transaction_ids = [row.split(",")[0] for row in data_lines]
    expected_order = ["T001", "T004", "T006", "T010", "T011", "T013", "T015"]

    assert transaction_ids == expected_order, (
        f"Row order mismatch in {FILTERED_CSV_PATH}.\n"
        f"Expected transaction_id order: {expected_order}\n"
        f"Got:                           {transaction_ids}"
    )


def test_filtered_csv_excludes_wrong_product_codes():
    """Verify that rows with invalid product codes are excluded."""
    with open(FILTERED_CSV_PATH, "r", newline="") as f:
        content = f.read()

    # These transaction IDs should NOT appear (wrong product code format)
    excluded_ids = ["T002", "T005", "T008", "T014"]
    for tid in excluded_ids:
        assert tid not in content, (
            f"Transaction {tid} should be excluded (invalid product_code format) "
            f"but was found in {FILTERED_CSV_PATH}."
        )


def test_filtered_csv_excludes_wrong_status():
    """Verify that rows with non-matching status are excluded."""
    with open(FILTERED_CSV_PATH, "r", newline="") as f:
        content = f.read()

    # These transaction IDs should NOT appear (wrong status)
    excluded_ids = ["T003", "T007", "T009", "T012"]
    for tid in excluded_ids:
        assert tid not in content, (
            f"Transaction {tid} should be excluded (status not 'completed' or 'refunded') "
            f"but was found in {FILTERED_CSV_PATH}.\n"
            "Note: 'Completed' (capital C) should be excluded - status match is case-sensitive."
        )


def test_filtered_csv_t009_excluded_case_sensitive():
    """T009 has 'Completed' (capital C) which must NOT match - case-sensitive filter."""
    with open(FILTERED_CSV_PATH, "r", newline="") as f:
        content = f.read()
    assert "T009" not in content, (
        f"Transaction T009 has status 'Completed' (capital C) which should be excluded "
        f"by the case-sensitive filter, but it was found in {FILTERED_CSV_PATH}.\n"
        "The status filter must be case-sensitive: only 'completed' and 'refunded' (lowercase)."
    )


def test_original_sales_csv_unchanged():
    """The original sales.csv file must not be modified."""
    expected_original = (
        "transaction_id,date,region,product_code,amount,status\n"
        "T001,2024-01-05,north,PRD-001,150.00,completed\n"
        "T002,2024-01-06,south,PRD-10,89.50,completed\n"
        "T003,2024-01-07,east,PRD-042,200.00,pending\n"
        "T004,2024-01-08,west,PRD-007,310.75,completed\n"
        "T005,2024-01-09,north,PRD-1234,45.00,completed\n"
        "T006,2024-01-10,south,PRD-099,99.99,refunded\n"
        "T007,2024-01-11,east,PRD-003,55.25,cancelled\n"
        "T008,2024-01-12,west,PRD-88,175.00,refunded\n"
        "T009,2024-01-13,north,PRD-056,420.00,Completed\n"
        "T010,2024-01-14,south,PRD-002,60.00,refunded\n"
        "T011,2024-01-15,east,PRD-777,130.00,completed\n"
        "T012,2024-01-16,west,PRD-019,88.40,pending\n"
        "T013,2024-01-17,north,PRD-500,250.00,completed\n"
        "T014,2024-01-18,south,PRD-AB1,190.00,completed\n"
        "T015,2024-01-19,east,PRD-011,75.00,refunded\n"
    )
    assert os.path.isfile(SALES_CSV_PATH), (
        f"Original file {SALES_CSV_PATH} is missing - it should not have been deleted."
    )
    with open(SALES_CSV_PATH, "r", newline="") as f:
        actual = f.read()
    # Normalize: allow file to not have trailing newline
    actual_normalized = actual if actual.endswith("\n") else actual + "\n"
    assert actual_normalized == expected_original, (
        f"Original file {SALES_CSV_PATH} appears to have been modified.\n"
        f"Expected content matches the original 15-row sales CSV."
    )