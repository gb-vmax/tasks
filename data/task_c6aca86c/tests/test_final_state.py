# test_final_state.py

import os
import pytest

BOTTLENECK_FILE = "/home/user/ci/bottleneck.txt"
PIPELINE_LOG = "/home/user/ci/pipeline_timings.log"
CI_DIR = "/home/user/ci"

EXPECTED_LINE_1 = "bottleneck: unit_tests (143s)"
EXPECTED_LINE_2 = "total_duration: 527s"


def test_ci_directory_exists():
    assert os.path.isdir(CI_DIR), (
        f"Directory '{CI_DIR}' does not exist. "
        "The CI directory must be present."
    )


def test_pipeline_log_still_intact():
    """Ensure the original pipeline log was not modified."""
    assert os.path.isfile(PIPELINE_LOG), (
        f"File '{PIPELINE_LOG}' no longer exists. "
        "The pipeline timings log must not be removed."
    )


def test_bottleneck_file_exists():
    assert os.path.isfile(BOTTLENECK_FILE), (
        f"File '{BOTTLENECK_FILE}' does not exist. "
        "The bottleneck summary file must be created by the task."
    )


def test_bottleneck_file_is_readable():
    assert os.access(BOTTLENECK_FILE, os.R_OK), (
        f"File '{BOTTLENECK_FILE}' is not readable."
    )


def test_bottleneck_file_has_exactly_two_lines():
    with open(BOTTLENECK_FILE, "r") as f:
        content = f.read()

    lines = content.splitlines()
    # Filter to non-empty lines for a better error message, but we want exactly 2 total
    non_empty = [l for l in lines if l.strip()]

    assert len(lines) == 2, (
        f"Expected exactly 2 lines in '{BOTTLENECK_FILE}', "
        f"but found {len(lines)} lines.\n"
        f"Full content repr: {repr(content)}"
    )


def test_bottleneck_first_line_content():
    with open(BOTTLENECK_FILE, "r") as f:
        content = f.read()

    lines = content.splitlines()
    assert len(lines) >= 1, (
        f"'{BOTTLENECK_FILE}' is empty or has no lines."
    )

    first_line = lines[0]
    assert first_line == EXPECTED_LINE_1, (
        f"First line of '{BOTTLENECK_FILE}' is incorrect.\n"
        f"  Expected: '{EXPECTED_LINE_1}'\n"
        f"  Actual:   '{first_line}'\n"
        "Make sure the format is exactly: bottleneck: <stage_name> (<duration_seconds>s)"
    )


def test_bottleneck_second_line_content():
    with open(BOTTLENECK_FILE, "r") as f:
        content = f.read()

    lines = content.splitlines()
    assert len(lines) >= 2, (
        f"'{BOTTLENECK_FILE}' does not have a second line.\n"
        f"Full content repr: {repr(content)}"
    )

    second_line = lines[1]
    assert second_line == EXPECTED_LINE_2, (
        f"Second line of '{BOTTLENECK_FILE}' is incorrect.\n"
        f"  Expected: '{EXPECTED_LINE_2}'\n"
        f"  Actual:   '{second_line}'\n"
        "Make sure the format is exactly: total_duration: <sum>s"
    )


def test_bottleneck_file_exact_content():
    """Check the complete file content matches exactly."""
    with open(BOTTLENECK_FILE, "r") as f:
        content = f.read()

    expected_content = f"{EXPECTED_LINE_1}\n{EXPECTED_LINE_2}\n"
    # Also accept without trailing newline
    expected_content_no_trailing = f"{EXPECTED_LINE_1}\n{EXPECTED_LINE_2}"

    assert content in (expected_content, expected_content_no_trailing), (
        f"The full content of '{BOTTLENECK_FILE}' does not match expected.\n"
        f"  Expected (with trailing newline): {repr(expected_content)}\n"
        f"  Expected (without trailing newline): {repr(expected_content_no_trailing)}\n"
        f"  Actual: {repr(content)}"
    )


def test_bottleneck_stage_name_correct():
    """Specifically verify the bottleneck stage name is unit_tests."""
    with open(BOTTLENECK_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, f"'{BOTTLENECK_FILE}' has no lines."
    first_line = lines[0]

    assert "unit_tests" in first_line, (
        f"The bottleneck stage 'unit_tests' is not mentioned in the first line.\n"
        f"  First line: '{first_line}'\n"
        "The stage with the highest duration (143s) should be 'unit_tests'."
    )


def test_bottleneck_duration_value_correct():
    """Specifically verify the bottleneck duration is 143s."""
    with open(BOTTLENECK_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, f"'{BOTTLENECK_FILE}' has no lines."
    first_line = lines[0]

    assert "143s" in first_line, (
        f"The bottleneck duration '143s' is not present in the first line.\n"
        f"  First line: '{first_line}'\n"
        "The maximum duration stage 'unit_tests' took 143 seconds."
    )


def test_total_duration_value_correct():
    """Specifically verify the total duration is 527s."""
    with open(BOTTLENECK_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 2, (
        f"'{BOTTLENECK_FILE}' does not have a second line for total_duration."
    )
    second_line = lines[1]

    assert "527s" in second_line, (
        f"The total duration '527s' is not present in the second line.\n"
        f"  Second line: '{second_line}'\n"
        "The sum of all stage durations (18+47+31+143+112+98+23+55) should be 527."
    )


def test_bottleneck_format_has_parentheses():
    """Verify parentheses are present around duration in first line."""
    with open(BOTTLENECK_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, f"'{BOTTLENECK_FILE}' has no lines."
    first_line = lines[0]

    assert "(" in first_line and ")" in first_line, (
        f"First line of '{BOTTLENECK_FILE}' is missing parentheses around duration.\n"
        f"  First line: '{first_line}'\n"
        f"  Expected format: bottleneck: <stage_name> (<duration_seconds>s)"
    )


def test_bottleneck_format_has_colon_space():
    """Verify 'bottleneck: ' prefix with colon and space is present."""
    with open(BOTTLENECK_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, f"'{BOTTLENECK_FILE}' has no lines."
    first_line = lines[0]

    assert first_line.startswith("bottleneck: "), (
        f"First line of '{BOTTLENECK_FILE}' does not start with 'bottleneck: '.\n"
        f"  First line: '{first_line}'\n"
        "The format must be: bottleneck: <stage_name> (<duration_seconds>s)"
    )


def test_total_duration_format_has_colon_space():
    """Verify 'total_duration: ' prefix with colon and space is present."""
    with open(BOTTLENECK_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 2, (
        f"'{BOTTLENECK_FILE}' does not have a second line."
    )
    second_line = lines[1]

    assert second_line.startswith("total_duration: "), (
        f"Second line of '{BOTTLENECK_FILE}' does not start with 'total_duration: '.\n"
        f"  Second line: '{second_line}'\n"
        "The format must be: total_duration: <sum>s"
    )


def test_no_extra_whitespace_in_lines():
    """Verify there is no leading/trailing whitespace on either line."""
    with open(BOTTLENECK_FILE, "r") as f:
        content = f.read()

    lines = content.splitlines()
    assert len(lines) >= 2, (
        f"'{BOTTLENECK_FILE}' does not have 2 lines. Content: {repr(content)}"
    )

    for i, line in enumerate(lines[:2]):
        assert line == line.strip(), (
            f"Line {i + 1} of '{BOTTLENECK_FILE}' has leading or trailing whitespace.\n"
            f"  Line repr: {repr(line)}"
        )