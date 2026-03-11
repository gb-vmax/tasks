# test_final_state.py

import os
import pytest

FREQUENCY_FILE = "/home/user/automation/workflow_frequency.txt"
LOG_FILE = "/home/user/automation/workflow_runs.log"
AUTOMATION_DIR = "/home/user/automation"

EXPECTED_LINES = [
    "9 deploy_prod",
    "9 sync_users",
    "5 notify_slack",
    "4 backup_db",
    "3 run_tests",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES)


def test_automation_directory_exists():
    assert os.path.isdir(AUTOMATION_DIR), (
        f"Directory '{AUTOMATION_DIR}' does not exist. "
        "The automation directory is missing."
    )


def test_log_file_still_exists():
    assert os.path.isfile(LOG_FILE), (
        f"Log file '{LOG_FILE}' no longer exists. "
        "The original log file should not have been removed."
    )


def test_frequency_file_exists():
    assert os.path.isfile(FREQUENCY_FILE), (
        f"Frequency report '{FREQUENCY_FILE}' does not exist. "
        "Please generate the workflow_frequency.txt report."
    )


def test_frequency_file_is_readable():
    assert os.access(FREQUENCY_FILE, os.R_OK), (
        f"Frequency report '{FREQUENCY_FILE}' is not readable."
    )


def test_frequency_file_line_count():
    with open(FREQUENCY_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    assert len(lines) == 5, (
        f"Expected exactly 5 non-empty lines in '{FREQUENCY_FILE}', "
        f"but found {len(lines)}.\n"
        f"Lines found:\n" + "\n".join(repr(l) for l in lines)
    )


def test_frequency_file_no_blank_lines():
    with open(FREQUENCY_FILE, "r") as f:
        raw_lines = f.readlines()

    blank_lines = [i + 1 for i, line in enumerate(raw_lines) if line.strip() == ""]
    assert not blank_lines, (
        f"Found blank lines in '{FREQUENCY_FILE}' at line numbers: {blank_lines}. "
        "The report must have no blank lines."
    )


def test_frequency_file_no_header():
    with open(FREQUENCY_FILE, "r") as f:
        first_line = f.readline().rstrip("\n")

    # First line should match the expected first data line
    assert first_line == EXPECTED_LINES[0], (
        f"First line of '{FREQUENCY_FILE}' is {repr(first_line)}, "
        f"but expected {repr(EXPECTED_LINES[0])}. "
        "There should be no header line — just data rows."
    )


def test_frequency_file_line_format():
    with open(FREQUENCY_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines, start=1):
        parts = line.split(" ")
        assert len(parts) == 2, (
            f"Line {i} in '{FREQUENCY_FILE}' does not have exactly 2 parts "
            f"(count and workflow name separated by a single space).\n"
            f"Line: {repr(line)}"
        )
        count_str, workflow_name = parts
        assert count_str.isdigit(), (
            f"Line {i} in '{FREQUENCY_FILE}': the first part {repr(count_str)} "
            f"is not a valid integer count.\nLine: {repr(line)}"
        )
        assert workflow_name.strip() == workflow_name and workflow_name != "", (
            f"Line {i} in '{FREQUENCY_FILE}': workflow name {repr(workflow_name)} "
            f"has leading/trailing spaces or is empty.\nLine: {repr(line)}"
        )


def test_frequency_file_no_leading_trailing_spaces():
    with open(FREQUENCY_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines, start=1):
        assert line == line.strip(), (
            f"Line {i} in '{FREQUENCY_FILE}' has leading or trailing spaces.\n"
            f"Line: {repr(line)}"
        )


def test_frequency_file_exact_content():
    with open(FREQUENCY_FILE, "r") as f:
        content = f.read()

    actual = content.strip()
    assert actual == EXPECTED_CONTENT, (
        f"Content of '{FREQUENCY_FILE}' does not match expected output.\n\n"
        f"Expected:\n{EXPECTED_CONTENT}\n\n"
        f"Actual:\n{actual}"
    )


def test_frequency_file_correct_counts():
    with open(FREQUENCY_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    expected_counts = {
        "deploy_prod": 9,
        "sync_users": 9,
        "notify_slack": 5,
        "backup_db": 4,
        "run_tests": 3,
    }

    found_workflows = {}
    for line in lines:
        parts = line.split(" ", 1)
        if len(parts) == 2:
            count_str, workflow = parts
            if count_str.isdigit():
                found_workflows[workflow] = int(count_str)

    for workflow, expected_count in expected_counts.items():
        actual_count = found_workflows.get(workflow)
        assert actual_count is not None, (
            f"Workflow '{workflow}' is missing from '{FREQUENCY_FILE}'."
        )
        assert actual_count == expected_count, (
            f"Workflow '{workflow}' has count {actual_count} in '{FREQUENCY_FILE}', "
            f"but expected {expected_count}."
        )

    assert set(found_workflows.keys()) == set(expected_counts.keys()), (
        f"Unexpected workflows in '{FREQUENCY_FILE}'.\n"
        f"Expected workflows: {sorted(expected_counts.keys())}\n"
        f"Found workflows: {sorted(found_workflows.keys())}"
    )


def test_frequency_file_sorted_descending_by_count_then_alphabetical():
    with open(FREQUENCY_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    parsed = []
    for i, line in enumerate(lines, start=1):
        parts = line.split(" ", 1)
        assert len(parts) == 2 and parts[0].isdigit(), (
            f"Line {i} cannot be parsed as '<count> <workflow>': {repr(line)}"
        )
        count, workflow = int(parts[0]), parts[1]
        parsed.append((count, workflow))

    # Verify sorting: descending count, then ascending name
    for i in range(len(parsed) - 1):
        curr_count, curr_name = parsed[i]
        next_count, next_name = parsed[i + 1]

        assert curr_count >= next_count, (
            f"Line {i + 1} has count {curr_count} and line {i + 2} has count {next_count}. "
            f"Counts must be in descending order.\n"
            f"Line {i + 1}: {repr(lines[i])}\n"
            f"Line {i + 2}: {repr(lines[i + 1])}"
        )

        if curr_count == next_count:
            assert curr_name <= next_name, (
                f"Workflows '{curr_name}' and '{next_name}' have the same count ({curr_count}), "
                f"but '{curr_name}' should come before '{next_name}' alphabetically.\n"
                f"Line {i + 1}: {repr(lines[i])}\n"
                f"Line {i + 2}: {repr(lines[i + 1])}"
            )


def test_frequency_file_exact_line_by_line():
    with open(FREQUENCY_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    assert len(lines) == len(EXPECTED_LINES), (
        f"Expected {len(EXPECTED_LINES)} lines, got {len(lines)}."
    )

    for i, (actual_line, expected_line) in enumerate(zip(lines, EXPECTED_LINES), start=1):
        assert actual_line == expected_line, (
            f"Line {i} of '{FREQUENCY_FILE}' is incorrect.\n"
            f"Expected: {repr(expected_line)}\n"
            f"Actual:   {repr(actual_line)}"
        )