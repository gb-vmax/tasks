# test_final_state.py

import os
import pytest
from collections import Counter

ARTIFACT_LOG_PATH = "/home/user/mlops/artifact_log.txt"
ARTIFACT_COUNTS_PATH = "/home/user/mlops/artifact_counts.txt"
MLOPS_DIR = "/home/user/mlops"

EXPECTED_COUNTS_LINES = [
    "18 model_checkpoint",
    "10 confusion_matrix",
    "9 training_log",
    "7 roc_curve",
    "6 feature_importance",
]

EXPECTED_COUNTS = {
    "model_checkpoint": 18,
    "confusion_matrix": 10,
    "training_log": 9,
    "roc_curve": 7,
    "feature_importance": 6,
}


def test_mlops_directory_exists():
    assert os.path.isdir(MLOPS_DIR), (
        f"Directory {MLOPS_DIR} does not exist. "
        "The mlops working directory must be present."
    )


def test_artifact_log_still_exists():
    assert os.path.isfile(ARTIFACT_LOG_PATH), (
        f"Original artifact log {ARTIFACT_LOG_PATH} no longer exists. "
        "The input file must not be removed."
    )


def test_artifact_counts_file_exists():
    assert os.path.isfile(ARTIFACT_COUNTS_PATH), (
        f"Output file {ARTIFACT_COUNTS_PATH} does not exist. "
        "The task requires writing the frequency report to this path."
    )


def test_artifact_counts_file_is_readable():
    assert os.access(ARTIFACT_COUNTS_PATH, os.R_OK), (
        f"File {ARTIFACT_COUNTS_PATH} is not readable."
    )


def test_artifact_counts_no_blank_lines():
    with open(ARTIFACT_COUNTS_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines()
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"File {ARTIFACT_COUNTS_PATH} contains blank lines at line numbers: {blank_lines}. "
        "No blank lines are allowed."
    )


def test_artifact_counts_no_header_line():
    with open(ARTIFACT_COUNTS_PATH, "r") as f:
        content = f.read()

    lines = [line.strip() for line in content.splitlines() if line.strip()]
    assert len(lines) > 0, (
        f"File {ARTIFACT_COUNTS_PATH} is empty."
    )

    first_line = lines[0]
    parts = first_line.split()
    assert len(parts) == 2 and parts[0].isdigit(), (
        f"First line of {ARTIFACT_COUNTS_PATH} does not look like a data line "
        f"('<count> <artifact_type>'). Got: '{first_line}'. "
        "There should be no header line."
    )


def test_artifact_counts_line_format():
    with open(ARTIFACT_COUNTS_PATH, "r") as f:
        content = f.read()

    lines = [line for line in content.splitlines() if line.strip()]
    for i, line in enumerate(lines, start=1):
        parts = line.split(" ")
        assert len(parts) == 2, (
            f"Line {i} in {ARTIFACT_COUNTS_PATH} does not have exactly two space-separated fields. "
            f"Got: '{line}'. Expected format: '<count> <artifact_type>'."
        )
        count_str, artifact_type = parts
        assert count_str.isdigit(), (
            f"Line {i} in {ARTIFACT_COUNTS_PATH}: first field '{count_str}' is not a valid integer count. "
            f"Full line: '{line}'."
        )
        assert not line.startswith(" "), (
            f"Line {i} in {ARTIFACT_COUNTS_PATH} has a leading space: '{line}'. "
            "No leading spaces are allowed."
        )


def test_artifact_counts_correct_number_of_lines():
    with open(ARTIFACT_COUNTS_PATH, "r") as f:
        content = f.read()

    lines = [line for line in content.splitlines() if line.strip()]
    assert len(lines) == len(EXPECTED_COUNTS), (
        f"Expected {len(EXPECTED_COUNTS)} lines in {ARTIFACT_COUNTS_PATH}, "
        f"but found {len(lines)}. Lines found:\n" + "\n".join(lines)
    )


def test_artifact_counts_correct_counts():
    with open(ARTIFACT_COUNTS_PATH, "r") as f:
        content = f.read()

    lines = [line for line in content.splitlines() if line.strip()]
    actual_counts = {}
    for i, line in enumerate(lines, start=1):
        parts = line.split(" ")
        if len(parts) == 2 and parts[0].isdigit():
            count_str, artifact_type = parts
            actual_counts[artifact_type] = int(count_str)

    assert actual_counts == EXPECTED_COUNTS, (
        f"Counts in {ARTIFACT_COUNTS_PATH} do not match expected counts.\n"
        f"Expected: {EXPECTED_COUNTS}\n"
        f"Actual:   {actual_counts}"
    )


def test_artifact_counts_sorted_descending_by_count():
    with open(ARTIFACT_COUNTS_PATH, "r") as f:
        content = f.read()

    lines = [line for line in content.splitlines() if line.strip()]
    counts_in_order = []
    for line in lines:
        parts = line.split(" ")
        if len(parts) == 2 and parts[0].isdigit():
            counts_in_order.append(int(parts[0]))

    assert counts_in_order == sorted(counts_in_order, reverse=True), (
        f"Lines in {ARTIFACT_COUNTS_PATH} are not sorted by count in descending order. "
        f"Counts found in order: {counts_in_order}. "
        "Expected descending order (highest count first)."
    )


def test_artifact_counts_tiebreaker_alphabetical():
    with open(ARTIFACT_COUNTS_PATH, "r") as f:
        content = f.read()

    lines = [line for line in content.splitlines() if line.strip()]
    parsed = []
    for line in lines:
        parts = line.split(" ")
        if len(parts) == 2 and parts[0].isdigit():
            parsed.append((int(parts[0]), parts[1]))

    # Group by count and check alphabetical ordering within each group
    from itertools import groupby
    for count_val, group in groupby(parsed, key=lambda x: x[0]):
        artifact_types = [item[1] for item in group]
        assert artifact_types == sorted(artifact_types), (
            f"Artifact types with count {count_val} in {ARTIFACT_COUNTS_PATH} "
            f"are not sorted alphabetically. Found: {artifact_types}. "
            f"Expected: {sorted(artifact_types)}."
        )


def test_artifact_counts_exact_content():
    with open(ARTIFACT_COUNTS_PATH, "r") as f:
        content = f.read()

    actual_lines = [line for line in content.splitlines() if line.strip()]

    assert actual_lines == EXPECTED_COUNTS_LINES, (
        f"Content of {ARTIFACT_COUNTS_PATH} does not exactly match expected output.\n"
        f"Expected:\n" + "\n".join(EXPECTED_COUNTS_LINES) + "\n\n"
        f"Actual:\n" + "\n".join(actual_lines)
    )


def test_artifact_counts_only_known_artifact_types():
    known_types = set(EXPECTED_COUNTS.keys())

    with open(ARTIFACT_COUNTS_PATH, "r") as f:
        content = f.read()

    lines = [line for line in content.splitlines() if line.strip()]
    found_types = set()
    for line in lines:
        parts = line.split(" ")
        if len(parts) == 2:
            found_types.add(parts[1])

    unknown = found_types - known_types
    assert not unknown, (
        f"Unknown artifact types found in {ARTIFACT_COUNTS_PATH}: {unknown}. "
        f"Only these types are expected: {known_types}."
    )


def test_artifact_counts_all_expected_types_present():
    expected_types = set(EXPECTED_COUNTS.keys())

    with open(ARTIFACT_COUNTS_PATH, "r") as f:
        content = f.read()

    lines = [line for line in content.splitlines() if line.strip()]
    found_types = set()
    for line in lines:
        parts = line.split(" ")
        if len(parts) == 2:
            found_types.add(parts[1])

    missing = expected_types - found_types
    assert not missing, (
        f"Expected artifact types missing from {ARTIFACT_COUNTS_PATH}: {missing}. "
        f"All of these must appear: {expected_types}."
    )