# test_final_state.py

import os
import pytest

BUILD_SUMMARY_PATH = "/home/user/pipeline/build_summary.txt"
PIPELINE_DIR = "/home/user/pipeline"

EXPECTED_LINES = [
    "app_name=FluxMobile",
    "version_name=3.7.2",
    "version_code=4109",
    "build_type=release",
    "min_sdk=24",
    "target_sdk=34",
    "scheme=FluxMobile-Prod",
    "deployment_target=15.0",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES) + "\n"


def test_pipeline_directory_exists():
    assert os.path.isdir(PIPELINE_DIR), (
        f"Pipeline directory does not exist: {PIPELINE_DIR}"
    )


def test_build_summary_exists():
    assert os.path.isfile(BUILD_SUMMARY_PATH), (
        f"Summary file does not exist: {BUILD_SUMMARY_PATH}. "
        "The task requires creating this file."
    )


def test_build_summary_is_readable():
    assert os.access(BUILD_SUMMARY_PATH, os.R_OK), (
        f"Summary file is not readable: {BUILD_SUMMARY_PATH}"
    )


def test_build_summary_exact_content():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        actual_content = f.read()
    assert actual_content == EXPECTED_CONTENT, (
        f"Content of {BUILD_SUMMARY_PATH} does not match expected.\n"
        f"Expected (repr): {repr(EXPECTED_CONTENT)}\n"
        f"Actual   (repr): {repr(actual_content)}"
    )


def test_build_summary_ends_with_newline():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        actual_content = f.read()
    assert actual_content.endswith("\n"), (
        f"File {BUILD_SUMMARY_PATH} does not end with a trailing newline. "
        f"Last char repr: {repr(actual_content[-1]) if actual_content else 'file is empty'}"
    )


def test_build_summary_line_count():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        actual_content = f.read()
    # Strip trailing newline and split to count non-empty lines
    lines = actual_content.rstrip("\n").split("\n")
    assert len(lines) == 8, (
        f"Expected exactly 8 lines in {BUILD_SUMMARY_PATH}, got {len(lines)}.\n"
        f"Lines found: {lines}"
    )


def test_build_summary_no_blank_lines():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        actual_content = f.read()
    lines = actual_content.split("\n")
    # The last element after split on trailing newline should be empty string; ignore it
    # but any other blank lines are errors
    non_trailing = lines[:-1] if lines[-1] == "" else lines
    blank_lines = [i + 1 for i, line in enumerate(non_trailing) if line.strip() == ""]
    assert not blank_lines, (
        f"Found blank lines at line numbers {blank_lines} in {BUILD_SUMMARY_PATH}. "
        "No blank lines are allowed."
    )


def test_build_summary_no_section_headers():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        lines = f.readlines()
    section_lines = [line.strip() for line in lines if line.strip().startswith("[")]
    assert not section_lines, (
        f"Found INI section headers in {BUILD_SUMMARY_PATH}: {section_lines}. "
        "No section headers should be present."
    )


def test_build_summary_no_comments():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        lines = f.readlines()
    comment_lines = [
        line.strip() for line in lines
        if line.strip().startswith(";") or line.strip().startswith("#")
    ]
    assert not comment_lines, (
        f"Found comment lines in {BUILD_SUMMARY_PATH}: {comment_lines}. "
        "No comments should be present."
    )


def test_build_summary_line_1_app_name():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 1, f"File {BUILD_SUMMARY_PATH} has fewer than 1 line."
    assert lines[0] == "app_name=FluxMobile", (
        f"Line 1 of {BUILD_SUMMARY_PATH}: expected 'app_name=FluxMobile', got '{lines[0]}'"
    )


def test_build_summary_line_2_version_name():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 2, f"File {BUILD_SUMMARY_PATH} has fewer than 2 lines."
    assert lines[1] == "version_name=3.7.2", (
        f"Line 2 of {BUILD_SUMMARY_PATH}: expected 'version_name=3.7.2', got '{lines[1]}'"
    )


def test_build_summary_line_3_version_code():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 3, f"File {BUILD_SUMMARY_PATH} has fewer than 3 lines."
    assert lines[2] == "version_code=4109", (
        f"Line 3 of {BUILD_SUMMARY_PATH}: expected 'version_code=4109', got '{lines[2]}'"
    )


def test_build_summary_line_4_build_type():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 4, f"File {BUILD_SUMMARY_PATH} has fewer than 4 lines."
    assert lines[3] == "build_type=release", (
        f"Line 4 of {BUILD_SUMMARY_PATH}: expected 'build_type=release', got '{lines[3]}'"
    )


def test_build_summary_line_5_min_sdk():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 5, f"File {BUILD_SUMMARY_PATH} has fewer than 5 lines."
    assert lines[4] == "min_sdk=24", (
        f"Line 5 of {BUILD_SUMMARY_PATH}: expected 'min_sdk=24', got '{lines[4]}'"
    )


def test_build_summary_line_6_target_sdk():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 6, f"File {BUILD_SUMMARY_PATH} has fewer than 6 lines."
    assert lines[5] == "target_sdk=34", (
        f"Line 6 of {BUILD_SUMMARY_PATH}: expected 'target_sdk=34', got '{lines[5]}'"
    )


def test_build_summary_line_7_scheme():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 7, f"File {BUILD_SUMMARY_PATH} has fewer than 7 lines."
    assert lines[6] == "scheme=FluxMobile-Prod", (
        f"Line 7 of {BUILD_SUMMARY_PATH}: expected 'scheme=FluxMobile-Prod', got '{lines[6]}'"
    )


def test_build_summary_line_8_deployment_target():
    with open(BUILD_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 8, f"File {BUILD_SUMMARY_PATH} has fewer than 8 lines."
    assert lines[7] == "deployment_target=15.0", (
        f"Line 8 of {BUILD_SUMMARY_PATH}: expected 'deployment_target=15.0', got '{lines[7]}'"
    )


def test_build_summary_byte_for_byte():
    """Verify the exact byte content of the summary file."""
    expected_bytes = EXPECTED_CONTENT.encode("utf-8")
    with open(BUILD_SUMMARY_PATH, "rb") as f:
        actual_bytes = f.read()
    assert actual_bytes == expected_bytes, (
        f"Byte-for-byte content mismatch in {BUILD_SUMMARY_PATH}.\n"
        f"Expected bytes (repr): {repr(expected_bytes)}\n"
        f"Actual bytes   (repr): {repr(actual_bytes)}"
    )