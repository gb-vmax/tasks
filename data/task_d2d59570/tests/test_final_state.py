# test_final_state.py

import os
import pytest

VERIFICATION_OUTPUT = "/home/user/backup/verification_output.csv"

EXPECTED_OUTPUT = (
    "status,checksum\n"
    "SUCCESS,ad328d766fbe\n"
    "FAILURE,09842dbeff92\n"
    "SUCCESS,ff33aabb2200\n"
)

def test_verification_output_exists():
    assert os.path.isfile(VERIFICATION_OUTPUT), (
        f"File '{VERIFICATION_OUTPUT}' does not exist.\n"
        "You must create this file with the extracted columns from backup_report.csv."
    )

def test_verification_output_content():
    try:
        with open(VERIFICATION_OUTPUT, "r", encoding="utf-8") as f:
            output = f.read()
    except Exception as e:
        pytest.fail(f"Could not read '{VERIFICATION_OUTPUT}': {e}")

    if output != EXPECTED_OUTPUT:
        # Provide a detailed difference
        import difflib
        diff = "\n".join(
            difflib.unified_diff(
                EXPECTED_OUTPUT.splitlines(keepends=True),
                output.splitlines(keepends=True),
                fromfile="expected",
                tofile="found",
            )
        )
        pytest.fail(
            f"The content of '{VERIFICATION_OUTPUT}' does not match the expected output.\n"
            "Differences (expected vs found):\n"
            f"{diff}\n"
            "Ensure you extract only the 3rd and 4th columns (status,checksum), "
            "keep the correct header, no extra columns or spaces, "
            "and preserve the order and formatting (including final newline)."
        )

def test_verification_output_has_only_two_columns():
    # Check that there are exactly two columns in every line and no extra/empty fields
    with open(VERIFICATION_OUTPUT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    for i, line in enumerate(lines, 1):
        fields = line.split(",")
        assert len(fields) == 2, (
            f"Line {i} of '{VERIFICATION_OUTPUT}' does not have exactly 2 columns: '{line}'\n"
            "Each line must contain only the 'status' and 'checksum' columns, separated by a single comma."
        )
        # Check for leading/trailing spaces in header and data
        for j, val in enumerate(fields):
            assert val == val.strip(), (
                f"Line {i}, column {j+1} ('{val}') in '{VERIFICATION_OUTPUT}' contains leading/trailing spaces.\n"
                "No extra spaces are allowed in the output CSV."
            )