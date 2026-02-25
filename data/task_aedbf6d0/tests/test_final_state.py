# test_final_state.py

import os
import csv
import json
import pytest

SALES_DATA_DIR = "/home/user/sales_data"

# ---- Truth Data ----

TRUTH_SUMMARY_CSV = [
    ["Region", "TotalOrders", "TotalSaleAmount", "AverageSaleAmount"],
    ["North", "3", "855.50", "285.17"],
    ["South", "2", "430.00", "215.00"],
    ["West",  "4", "795.00", "198.75"],
]

TRUTH_SUMMARY_JSON = [
    {
        "Region": "North",
        "TotalOrders": 3,
        "TotalSaleAmount": 855.50,
        "AverageSaleAmount": 285.17
    },
    {
        "Region": "South",
        "TotalOrders": 2,
        "TotalSaleAmount": 430.00,
        "AverageSaleAmount": 215.00
    },
    {
        "Region": "West",
        "TotalOrders": 4,
        "TotalSaleAmount": 795.00,
        "AverageSaleAmount": 198.75
    },
]

TRUTH_PROCESS_LOG_LINES = [
    "north.csv | Region: North | TotalOrders: 3 | TotalSaleAmount: 855.50 | AverageSaleAmount: 285.17",
    "south.csv | Region: South | TotalOrders: 2 | TotalSaleAmount: 430.00 | AverageSaleAmount: 215.00",
    "west.csv | Region: West | TotalOrders: 4 | TotalSaleAmount: 795.00 | AverageSaleAmount: 198.75",
]

SUMMARY_CSV_PATH = os.path.join(SALES_DATA_DIR, "summary.csv")
SUMMARY_JSON_PATH = os.path.join(SALES_DATA_DIR, "summary.json")
PROCESS_LOG_PATH = os.path.join(SALES_DATA_DIR, "process.log")

# ---- Tests ----

def test_summary_csv_exists_and_correct():
    """Check summary.csv exists and matches the truth, including headers, row order, values, and formatting."""
    assert os.path.isfile(SUMMARY_CSV_PATH), f"Missing required file: {SUMMARY_CSV_PATH}"

    with open(SUMMARY_CSV_PATH, newline="") as f:
        reader = csv.reader(f)
        actual_rows = list(reader)

    # Check number of rows
    assert len(actual_rows) == len(TRUTH_SUMMARY_CSV), (
        f"{SUMMARY_CSV_PATH} should have {len(TRUTH_SUMMARY_CSV)} rows (including header), but found {len(actual_rows)}."
    )

    # Check header exactly
    assert actual_rows[0] == TRUTH_SUMMARY_CSV[0], (
        f"{SUMMARY_CSV_PATH} header is incorrect.\nExpected: {TRUTH_SUMMARY_CSV[0]}\nFound:    {actual_rows[0]}"
    )

    # Check each data row for exact match (values and order, as str)
    for i, (expected, found) in enumerate(zip(TRUTH_SUMMARY_CSV[1:], actual_rows[1:]), start=1):
        assert found == expected, (
            f"{SUMMARY_CSV_PATH} row {i} is incorrect.\nExpected: {expected}\nFound:    {found}"
        )

def test_summary_json_exists_and_correct():
    """Check summary.json exists, is valid JSON, is an array of 3 objects with exact keys and values/types."""
    assert os.path.isfile(SUMMARY_JSON_PATH), f"Missing required file: {SUMMARY_JSON_PATH}"

    with open(SUMMARY_JSON_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            pytest.fail(f"{SUMMARY_JSON_PATH} is not valid JSON: {e}")

    # Must be list of 3 dicts
    assert isinstance(data, list), f"{SUMMARY_JSON_PATH} must be a JSON array."
    assert len(data) == 3, f"{SUMMARY_JSON_PATH} must have 3 objects (one per region), found {len(data)}."

    # Check each object for keys (order not enforced, but keys must match)
    for i, (expected, actual) in enumerate(zip(TRUTH_SUMMARY_JSON, data)):
        assert isinstance(actual, dict), (
            f"{SUMMARY_JSON_PATH} entry {i} is not an object."
        )
        assert set(actual.keys()) == set(expected.keys()), (
            f"{SUMMARY_JSON_PATH} entry {i} keys incorrect.\nExpected: {sorted(expected.keys())}\nFound:    {sorted(actual.keys())}"
        )
        # Value checks
        for key in expected:
            exp_val = expected[key]
            act_val = actual[key]
            # Numeric checks
            if key in ("TotalOrders",):
                assert isinstance(act_val, int), (
                    f"{SUMMARY_JSON_PATH} entry {i} '{key}' should be int, found {type(act_val).__name__}."
                )
                assert act_val == exp_val, (
                    f"{SUMMARY_JSON_PATH} entry {i} '{key}' value incorrect. Expected: {exp_val}, Found: {act_val}"
                )
            elif key in ("TotalSaleAmount", "AverageSaleAmount"):
                assert isinstance(act_val, (float, int)), (
                    f"{SUMMARY_JSON_PATH} entry {i} '{key}' should be a number (float), found {type(act_val).__name__}."
                )
                # Check for exact value and rounding
                assert round(float(act_val), 2) == float(f"{exp_val:.2f}"), (
                    f"{SUMMARY_JSON_PATH} entry {i} '{key}' value incorrect or not rounded to two decimals. "
                    f"Expected: {exp_val}, Found: {act_val}"
                )
            else:
                assert act_val == exp_val, (
                    f"{SUMMARY_JSON_PATH} entry {i} '{key}' value incorrect. Expected: {exp_val}, Found: {act_val}"
                )

def test_process_log_exists_and_correct():
    """Check process.log exists and has exactly the expected lines, in order, with exact formatting."""
    assert os.path.isfile(PROCESS_LOG_PATH), f"Missing required file: {PROCESS_LOG_PATH}"

    with open(PROCESS_LOG_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n\r") for line in f]

    # Remove any blank lines at end (shouldn't be, but robust)
    lines = [line for line in lines if line.strip() != ""]

    assert lines == TRUTH_PROCESS_LOG_LINES, (
        f"{PROCESS_LOG_PATH} contents are incorrect.\n"
        f"Expected lines:\n" +
        "\n".join(TRUTH_PROCESS_LOG_LINES) +
        "\nFound lines:\n" +
        "\n".join(lines)
    )

def test_no_extra_output_files():
    """Ensure that only the expected output files exist in /home/user/sales_data/."""
    expected_files = {
        "north.csv", "south.csv", "west.csv",
        "summary.csv", "summary.json", "process.log"
    }
    found_files = set(os.listdir(SALES_DATA_DIR))
    extra = found_files - expected_files
    missing = expected_files - found_files
    assert not missing, (
        f"Missing expected files in {SALES_DATA_DIR}: {sorted(missing)}"
    )
    assert not extra, (
        f"Unexpected extra files found in {SALES_DATA_DIR}: {sorted(extra)}"
    )