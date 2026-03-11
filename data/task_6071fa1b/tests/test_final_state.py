# test_final_state.py

import os
import pytest

CSV_PATH = "/home/user/ml_project/training_data.csv"
OUTPUT_PATH = "/home/user/ml_project/class_stats.txt"

EXPECTED_OUTPUT = """\
=== CLASS DISTRIBUTION REPORT ===

bird: 4 samples (26.67%), feature1 range [0.50, 3.20], feature2 range [1.10, 4.80]
cat: 6 samples (40.00%), feature1 range [1.20, 5.60], feature2 range [0.30, 3.90]
dog: 5 samples (33.33%), feature1 range [0.80, 4.40], feature2 range [1.50, 6.20]

Total samples: 15"""


def test_output_file_exists():
    assert os.path.isfile(OUTPUT_PATH), (
        f"Output file '{OUTPUT_PATH}' does not exist. "
        "The task requires writing the class distribution report to this file."
    )


def test_output_file_is_readable():
    assert os.access(OUTPUT_PATH, os.R_OK), (
        f"Output file '{OUTPUT_PATH}' exists but is not readable."
    )


def test_output_file_exact_content():
    with open(OUTPUT_PATH, "r") as f:
        actual = f.read().rstrip("\n")

    assert actual == EXPECTED_OUTPUT, (
        f"Content of '{OUTPUT_PATH}' does not match expected.\n\n"
        f"Expected:\n{repr(EXPECTED_OUTPUT)}\n\n"
        f"Actual:\n{repr(actual)}"
    )


def test_output_file_header():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 1, (
        f"'{OUTPUT_PATH}' is empty or has no lines."
    )
    first_line = lines[0].rstrip("\n")
    assert first_line == "=== CLASS DISTRIBUTION REPORT ===", (
        f"First line of '{OUTPUT_PATH}' is not the expected header.\n"
        f"Expected: '=== CLASS DISTRIBUTION REPORT ==='\n"
        f"Got:      '{first_line}'"
    )


def test_output_file_blank_line_after_header():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 2, (
        f"'{OUTPUT_PATH}' has fewer than 2 lines."
    )
    second_line = lines[1].rstrip("\n")
    assert second_line == "", (
        f"Second line of '{OUTPUT_PATH}' should be blank (between header and first class).\n"
        f"Got: '{second_line}'"
    )


def test_output_file_bird_line():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()

    expected_line = "bird: 4 samples (26.67%), feature1 range [0.50, 3.20], feature2 range [1.10, 4.80]"
    assert expected_line in content, (
        f"Expected bird line not found in '{OUTPUT_PATH}'.\n"
        f"Expected line: '{expected_line}'\n"
        f"File content:\n{content}"
    )


def test_output_file_cat_line():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()

    expected_line = "cat: 6 samples (40.00%), feature1 range [1.20, 5.60], feature2 range [0.30, 3.90]"
    assert expected_line in content, (
        f"Expected cat line not found in '{OUTPUT_PATH}'.\n"
        f"Expected line: '{expected_line}'\n"
        f"File content:\n{content}"
    )


def test_output_file_dog_line():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()

    expected_line = "dog: 5 samples (33.33%), feature1 range [0.80, 4.40], feature2 range [1.50, 6.20]"
    assert expected_line in content, (
        f"Expected dog line not found in '{OUTPUT_PATH}'.\n"
        f"Expected line: '{expected_line}'\n"
        f"File content:\n{content}"
    )


def test_output_file_total_samples_line():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()

    expected_line = "Total samples: 15"
    assert expected_line in content, (
        f"Expected total samples line not found in '{OUTPUT_PATH}'.\n"
        f"Expected line: '{expected_line}'\n"
        f"File content:\n{content}"
    )


def test_output_file_classes_in_alphabetical_order():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.readlines()

    class_lines = []
    for line in lines:
        stripped = line.rstrip("\n")
        for cls in ("bird", "cat", "dog"):
            if stripped.startswith(cls + ":"):
                class_lines.append(cls)
                break

    assert class_lines == ["bird", "cat", "dog"], (
        f"Classes in '{OUTPUT_PATH}' are not in alphabetical order.\n"
        f"Found order: {class_lines}\n"
        f"Expected order: ['bird', 'cat', 'dog']"
    )


def test_output_file_blank_line_before_total():
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    # Find the index of the "Total samples: 15" line
    total_idx = None
    for i, line in enumerate(lines):
        if line.startswith("Total samples:"):
            total_idx = i
            break

    assert total_idx is not None, (
        f"'Total samples:' line not found in '{OUTPUT_PATH}'."
    )
    assert total_idx >= 1, (
        f"'Total samples:' line is the first line, expected a blank line before it."
    )
    line_before_total = lines[total_idx - 1]
    assert line_before_total == "", (
        f"Expected a blank line before 'Total samples:' in '{OUTPUT_PATH}'.\n"
        f"Line before 'Total samples:': '{line_before_total}'"
    )


def test_output_file_structure_line_count():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read().rstrip("\n")
    lines = content.split("\n")

    # Expected structure:
    # Line 0: === CLASS DISTRIBUTION REPORT ===
    # Line 1: (blank)
    # Line 2: bird: ...
    # Line 3: cat: ...
    # Line 4: dog: ...
    # Line 5: (blank)
    # Line 6: Total samples: 15
    assert len(lines) == 7, (
        f"Expected exactly 7 lines in '{OUTPUT_PATH}' (after stripping trailing newline), "
        f"but got {len(lines)}.\n"
        f"Lines:\n" + "\n".join(repr(l) for l in lines)
    )


def test_csv_file_still_intact():
    """Ensure the original CSV file was not modified."""
    expected_csv = """\
1,2.30,1.50,cat
2,0.50,4.80,bird
3,4.40,6.20,dog
4,1.20,0.30,cat
5,3.20,1.10,bird
6,0.80,1.50,dog
7,5.60,3.90,cat
8,1.80,2.20,bird
9,2.10,3.70,dog
10,3.40,1.90,cat
11,1.50,4.10,bird
12,4.10,5.30,dog
13,2.90,2.60,cat
14,0.90,3.30,dog
15,3.80,2.80,cat"""

    assert os.path.isfile(CSV_PATH), (
        f"Original CSV file '{CSV_PATH}' is missing after task completion."
    )
    with open(CSV_PATH, "r") as f:
        actual = f.read().rstrip("\n")

    assert actual == expected_csv, (
        f"Original CSV file '{CSV_PATH}' was modified.\n"
        f"Expected:\n{expected_csv}\n\n"
        f"Actual:\n{actual}"
    )