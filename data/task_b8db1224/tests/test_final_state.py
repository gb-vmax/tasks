# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/mlops/artifact_report.txt"
TSV_PATH = "/home/user/mlops/experiments.tsv"
MLOPS_DIR = "/home/user/mlops"

EXPECTED_LINES = [
    "exp_001 | resnet50 | 92.3% | ckpt_final",
    "exp_003 | vgg16 | 87.5% | ckpt_best",
    "exp_005 | bert_large | 95.1% | ckpt_final",
    "exp_007 | mobilenet | 81.0% | ckpt_best",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES) + "\n"


def test_mlops_directory_exists():
    assert os.path.isdir(MLOPS_DIR), (
        f"Directory '{MLOPS_DIR}' does not exist. "
        "The /home/user/mlops directory must be present."
    )


def test_tsv_file_still_intact():
    """Ensure the input TSV file has not been modified or deleted."""
    assert os.path.isfile(TSV_PATH), (
        f"Input file '{TSV_PATH}' no longer exists. "
        "The source TSV file should not have been removed."
    )


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Output report file '{REPORT_PATH}' does not exist. "
        "The task requires creating this file with the processed experiment data."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Output report file '{REPORT_PATH}' exists but is not readable."
    )


def test_report_line_count():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    # Strip trailing newline before splitting to get actual data lines
    lines = content.rstrip("\n").split("\n") if content.strip() else []

    assert len(lines) == len(EXPECTED_LINES), (
        f"Expected {len(EXPECTED_LINES)} lines in '{REPORT_PATH}', "
        f"but found {len(lines)} lines.\n"
        f"Actual content:\n{repr(content)}"
    )


def test_report_no_blank_lines():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    lines = content.split("\n")
    # The last element after split may be empty due to trailing newline — that's acceptable
    # but there should be no blank lines within the data
    data_lines = lines[:-1] if lines and lines[-1] == "" else lines

    for i, line in enumerate(data_lines, start=1):
        assert line.strip() != "", (
            f"Line {i} in '{REPORT_PATH}' is blank. "
            "The report should contain no blank lines."
        )


def test_report_no_trailing_spaces():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    lines = content.split("\n")
    data_lines = lines[:-1] if lines and lines[-1] == "" else lines

    for i, line in enumerate(data_lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} in '{REPORT_PATH}' has trailing whitespace.\n"
            f"Line content: {repr(line)}"
        )


def test_report_no_header():
    with open(REPORT_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")

    # Header would typically contain column names like 'experiment_id' or 'model_name'
    header_keywords = ["experiment_id", "model_name", "status", "accuracy", "checkpoint"]
    for keyword in header_keywords:
        assert keyword.lower() not in first_line.lower(), (
            f"The first line of '{REPORT_PATH}' appears to be a header containing '{keyword}'. "
            "The report should contain only data lines, no header.\n"
            f"First line: {repr(first_line)}"
        )


def test_report_excludes_failed_experiments():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    failed_ids = ["exp_002", "exp_006"]
    for exp_id in failed_ids:
        assert exp_id not in content, (
            f"FAILED experiment '{exp_id}' should NOT appear in '{REPORT_PATH}', "
            f"but it was found.\nActual content:\n{content}"
        )


def test_report_excludes_running_experiments():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    assert "exp_004" not in content, (
        f"RUNNING experiment 'exp_004' should NOT appear in '{REPORT_PATH}', "
        f"but it was found.\nActual content:\n{content}"
    )


def test_report_contains_completed_experiment_ids():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    completed_ids = ["exp_001", "exp_003", "exp_005", "exp_007"]
    for exp_id in completed_ids:
        assert exp_id in content, (
            f"COMPLETED experiment '{exp_id}' should appear in '{REPORT_PATH}', "
            f"but it was not found.\nActual content:\n{content}"
        )


def test_report_each_line_exact_content():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").split("\n")

    assert len(actual_lines) == len(EXPECTED_LINES), (
        f"Expected {len(EXPECTED_LINES)} lines but got {len(actual_lines)}.\n"
        f"Actual content:\n{repr(content)}"
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, EXPECTED_LINES), start=1):
        assert actual == expected, (
            f"Line {i} of '{REPORT_PATH}' does not match expected output.\n"
            f"Expected: {repr(expected)}\n"
            f"Actual:   {repr(actual)}\n\n"
            "Check: status filtering (COMPLETED only), accuracy conversion to percentage "
            "(1 decimal place), checkpoint filename extraction with .pt stripped, "
            "and correct pipe-separated format."
        )


def test_report_accuracy_format():
    """Verify accuracy values are formatted as percentages with one decimal place."""
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    import re
    percentage_pattern = re.compile(r'\d+\.\d%')

    for i, line in enumerate(lines, start=1):
        assert percentage_pattern.search(line), (
            f"Line {i} of '{REPORT_PATH}' does not contain a properly formatted percentage "
            f"(e.g., '92.3%').\nLine content: {repr(line)}"
        )


def test_report_pipe_separator_format():
    """Verify each line uses ' | ' as separator between fields."""
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines, start=1):
        parts = line.split(" | ")
        assert len(parts) == 4, (
            f"Line {i} of '{REPORT_PATH}' should have exactly 4 fields separated by ' | ', "
            f"but splitting by ' | ' gives {len(parts)} parts.\n"
            f"Line content: {repr(line)}"
        )


def test_report_checkpoint_no_pt_extension():
    """Verify checkpoint names do not have the .pt extension."""
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines, start=1):
        parts = line.split(" | ")
        if len(parts) == 4:
            checkpoint_name = parts[3]
            assert not checkpoint_name.endswith(".pt"), (
                f"Line {i} of '{REPORT_PATH}': checkpoint name '{checkpoint_name}' "
                "should not have the '.pt' extension stripped."
            )
            assert "/" not in checkpoint_name, (
                f"Line {i} of '{REPORT_PATH}': checkpoint name '{checkpoint_name}' "
                "should be just the filename (no directory path)."
            )


def test_report_order_matches_input():
    """Verify that completed experiments appear in the same order as in the TSV."""
    with open(REPORT_PATH, "r") as f:
        actual_lines = [line.rstrip("\n") for line in f if line.strip()]

    expected_order = ["exp_001", "exp_003", "exp_005", "exp_007"]

    actual_ids = []
    for line in actual_lines:
        parts = line.split(" | ")
        if parts:
            actual_ids.append(parts[0].strip())

    assert actual_ids == expected_order, (
        f"Experiment IDs in '{REPORT_PATH}' are not in the correct order.\n"
        f"Expected order: {expected_order}\n"
        f"Actual order:   {actual_ids}\n"
        "Lines should appear in the same order as in the input TSV file."
    )


def test_report_exact_full_content():
    """Final comprehensive check: the entire file content matches exactly."""
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    assert actual_content == EXPECTED_CONTENT, (
        f"The content of '{REPORT_PATH}' does not exactly match the expected output.\n"
        f"Expected:\n{repr(EXPECTED_CONTENT)}\n"
        f"Actual:\n{repr(actual_content)}"
    )