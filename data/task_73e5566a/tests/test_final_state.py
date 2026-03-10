# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/data/dataset_report.txt"
CSV_PATH = "/home/user/data/training_samples.csv"

EXPECTED_REPORT_CONTENT = """\
=== DATASET DIAGNOSTIC REPORT ===

File: /home/user/data/training_samples.csv
Total rows (excluding header): 10
Total columns: 5

=== COLUMN STATS ===
sample_id: min=1, max=10, missing=0
age: min=23, max=52, missing=2
income: min=45000, max=91000, missing=1
score: min=72, max=95, missing=2
label: min=0, max=1, missing=0

=== MISSING VALUE SUMMARY ===
Total missing values: 5
Columns with missing data: 3"""


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The diagnostic report must be generated at this path."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file '{REPORT_PATH}' exists but is not readable."
    )


def test_report_exact_content():
    with open(REPORT_PATH, "r") as f:
        content = f.read().strip()
    expected = EXPECTED_REPORT_CONTENT.strip()
    assert content == expected, (
        f"Report file content does not match expected.\n\n"
        f"--- EXPECTED ---\n{expected}\n\n"
        f"--- ACTUAL ---\n{content}\n"
    )


def test_report_header_section():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert "=== DATASET DIAGNOSTIC REPORT ===" in content, (
        "Report is missing the header '=== DATASET DIAGNOSTIC REPORT ==='."
    )


def test_report_file_line():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_line = "File: /home/user/data/training_samples.csv"
    assert expected_line in content, (
        f"Report is missing the line: '{expected_line}'.\n"
        f"Actual content:\n{content}"
    )


def test_report_total_rows():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_line = "Total rows (excluding header): 10"
    assert expected_line in content, (
        f"Report is missing or has wrong value for total rows.\n"
        f"Expected line: '{expected_line}'\n"
        f"Actual content:\n{content}"
    )


def test_report_total_columns():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_line = "Total columns: 5"
    assert expected_line in content, (
        f"Report is missing or has wrong value for total columns.\n"
        f"Expected line: '{expected_line}'\n"
        f"Actual content:\n{content}"
    )


def test_report_column_stats_section():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert "=== COLUMN STATS ===" in content, (
        "Report is missing the section header '=== COLUMN STATS ==='."
    )


def test_report_sample_id_stats():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_line = "sample_id: min=1, max=10, missing=0"
    assert expected_line in content, (
        f"Report has wrong stats for 'sample_id'.\n"
        f"Expected line: '{expected_line}'\n"
        f"Actual content:\n{content}"
    )


def test_report_age_stats():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_line = "age: min=23, max=52, missing=2"
    assert expected_line in content, (
        f"Report has wrong stats for 'age'.\n"
        f"Expected line: '{expected_line}'\n"
        f"Actual content:\n{content}"
    )


def test_report_income_stats():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_line = "income: min=45000, max=91000, missing=1"
    assert expected_line in content, (
        f"Report has wrong stats for 'income'.\n"
        f"Expected line: '{expected_line}'\n"
        f"Actual content:\n{content}"
    )


def test_report_score_stats():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_line = "score: min=72, max=95, missing=2"
    assert expected_line in content, (
        f"Report has wrong stats for 'score'.\n"
        f"Expected line: '{expected_line}'\n"
        f"Actual content:\n{content}"
    )


def test_report_label_stats():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_line = "label: min=0, max=1, missing=0"
    assert expected_line in content, (
        f"Report has wrong stats for 'label'.\n"
        f"Expected line: '{expected_line}'\n"
        f"Actual content:\n{content}"
    )


def test_report_missing_value_summary_section():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert "=== MISSING VALUE SUMMARY ===" in content, (
        "Report is missing the section header '=== MISSING VALUE SUMMARY ==='."
    )


def test_report_total_missing_values():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_line = "Total missing values: 5"
    assert expected_line in content, (
        f"Report has wrong total missing values.\n"
        f"Expected line: '{expected_line}'\n"
        f"Actual content:\n{content}"
    )


def test_report_columns_with_missing_data():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_line = "Columns with missing data: 3"
    assert expected_line in content, (
        f"Report has wrong count for 'Columns with missing data'.\n"
        f"Expected line: '{expected_line}'\n"
        f"Actual content:\n{content}"
    )


def test_report_no_decimal_values():
    """Ensure min/max values are integers, not floats (e.g., '42' not '42.0')."""
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    for line in lines:
        if "min=" in line and "max=" in line:
            # Check that no numeric value has a decimal point
            # Extract the stats portion
            parts = line.strip().split(":")
            if len(parts) >= 2:
                stats_part = ":".join(parts[1:])
                # Look for patterns like =<number>. which would indicate floats
                import re
                # Find all numeric values after = sign
                numeric_values = re.findall(r'=(-?\d+\.?\d*)', stats_part)
                for val in numeric_values:
                    assert "." not in val, (
                        f"Found decimal value '{val}' in line: '{line.strip()}'. "
                        "All min/max values should be integers (no decimals)."
                    )


def test_report_column_order():
    """Ensure columns appear in the correct order in the COLUMN STATS section."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    expected_columns_in_order = [
        "sample_id",
        "age",
        "income",
        "score",
        "label",
    ]

    # Find the COLUMN STATS section
    stats_section_start = content.find("=== COLUMN STATS ===")
    summary_section_start = content.find("=== MISSING VALUE SUMMARY ===")

    assert stats_section_start != -1, "Could not find '=== COLUMN STATS ===' section."
    assert summary_section_start != -1, "Could not find '=== MISSING VALUE SUMMARY ===' section."

    stats_section = content[stats_section_start:summary_section_start]

    positions = []
    for col in expected_columns_in_order:
        pos = stats_section.find(col + ":")
        assert pos != -1, (
            f"Column '{col}' not found in the COLUMN STATS section.\n"
            f"Stats section content:\n{stats_section}"
        )
        positions.append(pos)

    assert positions == sorted(positions), (
        f"Columns are not listed in the correct order in COLUMN STATS section.\n"
        f"Expected order: {expected_columns_in_order}\n"
        f"Stats section:\n{stats_section}"
    )


def test_report_structure_blank_lines():
    """Check that the report has the correct blank line structure."""
    with open(REPORT_PATH, "r") as f:
        content = f.read().strip()

    lines = content.split("\n")

    # Line 0: === DATASET DIAGNOSTIC REPORT ===
    assert lines[0] == "=== DATASET DIAGNOSTIC REPORT ===", (
        f"First line should be '=== DATASET DIAGNOSTIC REPORT ===' but got: '{lines[0]}'"
    )

    # Line 1: blank
    assert lines[1] == "", (
        f"Second line should be blank but got: '{lines[1]}'"
    )

    # Line 2: File: ...
    assert lines[2].startswith("File:"), (
        f"Third line should start with 'File:' but got: '{lines[2]}'"
    )

    # Line 3: Total rows
    assert lines[3].startswith("Total rows"), (
        f"Fourth line should start with 'Total rows' but got: '{lines[3]}'"
    )

    # Line 4: Total columns
    assert lines[4].startswith("Total columns"), (
        f"Fifth line should start with 'Total columns' but got: '{lines[4]}'"
    )

    # Line 5: blank
    assert lines[5] == "", (
        f"Sixth line should be blank but got: '{lines[5]}'"
    )

    # Line 6: === COLUMN STATS ===
    assert lines[6] == "=== COLUMN STATS ===", (
        f"Seventh line should be '=== COLUMN STATS ===' but got: '{lines[6]}'"
    )

    # Lines 7-11: column stats (5 columns)
    for i in range(7, 12):
        assert lines[i] != "", (
            f"Line {i+1} should contain column stats but is blank."
        )

    # Line 12: blank
    assert lines[12] == "", (
        f"Line 13 should be blank but got: '{lines[12]}'"
    )

    # Line 13: === MISSING VALUE SUMMARY ===
    assert lines[13] == "=== MISSING VALUE SUMMARY ===", (
        f"Line 14 should be '=== MISSING VALUE SUMMARY ===' but got: '{lines[13]}'"
    )

    # Line 14: Total missing values
    assert lines[14].startswith("Total missing values:"), (
        f"Line 15 should start with 'Total missing values:' but got: '{lines[14]}'"
    )

    # Line 15: Columns with missing data
    assert lines[15].startswith("Columns with missing data:"), (
        f"Line 16 should start with 'Columns with missing data:' but got: '{lines[15]}'"
    )


def test_csv_file_unchanged():
    """Verify the original CSV file was not modified."""
    expected_csv_content = """\
sample_id,age,income,score,label
1,23,45000,88,1
2,35,62000,91,0
3,,54000,76,1
4,41,78000,,0
5,29,,83,1
6,52,91000,95,0
7,38,67000,72,1
8,,83000,84,0
9,31,59000,,1
10,44,72000,90,0"""

    assert os.path.isfile(CSV_PATH), (
        f"Original CSV file '{CSV_PATH}' is missing after the task."
    )

    with open(CSV_PATH, "r") as f:
        content = f.read().strip()

    assert content == expected_csv_content.strip(), (
        f"Original CSV file '{CSV_PATH}' was modified.\n"
        f"Expected:\n{expected_csv_content}\n\n"
        f"Got:\n{content}"
    )