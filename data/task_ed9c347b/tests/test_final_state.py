# test_final_state.py

import os
import re
import pytest

WARNINGS_PATH = "/home/user/project/warnings.txt"
BUILD_LOG_PATH = "/home/user/project/build.log"
PROJECT_DIR = "/home/user/project"

EXPECTED_WARNINGS = (
    "src/main.c:14:3: warning: implicit declaration of function 'printf'\n"
    "src/auth.c:42:8: warning: unused variable 'token'\n"
    "src/utils.c:88:1: warning: comparison between signed and unsigned integer expressions\n"
    "src/utils.c:102:15: warning: format '%d' expects argument of type 'int'\n"
    "src/config.c:19:22: warning: unused parameter 'opts'\n"
)

EXPECTED_WARNING_LINES = [
    "src/main.c:14:3: warning: implicit declaration of function 'printf'",
    "src/auth.c:42:8: warning: unused variable 'token'",
    "src/utils.c:88:1: warning: comparison between signed and unsigned integer expressions",
    "src/utils.c:102:15: warning: format '%d' expects argument of type 'int'",
    "src/config.c:19:22: warning: unused parameter 'opts'",
]

NON_WARNING_LINES = [
    "[INFO] Build started at 2024-03-15 09:00:00",
    "[INFO] Compiling src/main.c",
    "src/main.c:10:5: error: undeclared identifier 'x'",
    "[INFO] Compiling src/auth.c",
    "src/auth.c:57:12: note: variable declared here",
    "src/auth.c:61:1: error: expected ';' before '}' token",
    "[INFO] Compiling src/utils.c",
    "[INFO] Compiling src/config.c",
    "src/config.c:7:4: note: initialized here",
    "[INFO] Build failed with 2 errors and 5 warnings",
]


def test_project_directory_exists():
    assert os.path.isdir(PROJECT_DIR), (
        f"Project directory '{PROJECT_DIR}' does not exist."
    )


def test_build_log_unchanged():
    """The original build.log should not have been modified."""
    assert os.path.isfile(BUILD_LOG_PATH), (
        f"Build log '{BUILD_LOG_PATH}' is missing — it should not have been deleted."
    )


def test_warnings_file_exists():
    assert os.path.isfile(WARNINGS_PATH), (
        f"Expected warnings file '{WARNINGS_PATH}' does not exist. "
        "The task requires extracting warning lines and writing them to this file."
    )


def test_warnings_file_is_readable():
    assert os.access(WARNINGS_PATH, os.R_OK), (
        f"Warnings file '{WARNINGS_PATH}' exists but is not readable."
    )


def test_warnings_file_exact_content():
    """The warnings file must match the expected content byte-for-byte."""
    with open(WARNINGS_PATH, "r") as f:
        actual = f.read()

    assert actual == EXPECTED_WARNINGS, (
        f"Content of '{WARNINGS_PATH}' does not match expected.\n\n"
        f"Expected (repr):\n{repr(EXPECTED_WARNINGS)}\n\n"
        f"Actual (repr):\n{repr(actual)}"
    )


def test_warnings_file_ends_with_newline():
    """File should end with a newline (standard grep output behaviour)."""
    with open(WARNINGS_PATH, "rb") as f:
        content = f.read()

    assert content.endswith(b"\n"), (
        f"'{WARNINGS_PATH}' does not end with a newline character. "
        "Standard grep output ends each matched line with a newline."
    )


def test_warnings_file_line_count():
    with open(WARNINGS_PATH, "r") as f:
        lines = f.readlines()

    # Strip trailing empty line that may result from a trailing newline
    non_empty_lines = [l for l in lines if l.strip()]
    assert len(non_empty_lines) == 5, (
        f"Expected exactly 5 warning lines in '{WARNINGS_PATH}', "
        f"but found {len(non_empty_lines)}.\n"
        f"Lines found:\n" + "".join(f"  {l}" for l in lines)
    )


def test_warnings_file_contains_all_expected_warnings():
    with open(WARNINGS_PATH, "r") as f:
        content = f.read()
        lines = [l.rstrip("\n") for l in content.splitlines()]

    for expected in EXPECTED_WARNING_LINES:
        assert expected in lines, (
            f"Expected warning line not found in '{WARNINGS_PATH}':\n"
            f"  Missing: {expected!r}\n"
            f"  Lines present: {lines}"
        )


def test_warnings_file_preserves_order():
    """Warning lines must appear in the same order as in the build log."""
    with open(WARNINGS_PATH, "r") as f:
        actual_lines = [l.rstrip("\n") for l in f.readlines() if l.strip()]

    assert actual_lines == EXPECTED_WARNING_LINES, (
        f"Warning lines in '{WARNINGS_PATH}' are not in the correct order.\n"
        f"Expected order:\n" + "\n".join(f"  {l}" for l in EXPECTED_WARNING_LINES) + "\n\n"
        f"Actual order:\n" + "\n".join(f"  {l}" for l in actual_lines)
    )


def test_warnings_file_contains_no_non_warning_lines():
    """The warnings file must not contain info, error, or note lines."""
    with open(WARNINGS_PATH, "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines() if l.strip()]

    for line in lines:
        assert line not in NON_WARNING_LINES, (
            f"Non-warning line found in '{WARNINGS_PATH}':\n"
            f"  Unexpected line: {line!r}\n"
            "Only lines matching the compiler warning pattern should be included."
        )


def test_warnings_file_all_lines_match_warning_pattern():
    """Every line in the warnings file must match the compiler warning pattern."""
    warning_pattern = re.compile(r'^src/\S+\.c:\d+:\d+: warning: .+$')

    with open(WARNINGS_PATH, "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines() if l.strip()]

    for line in lines:
        assert warning_pattern.match(line), (
            f"Line in '{WARNINGS_PATH}' does not match the expected warning pattern:\n"
            f"  Offending line: {line!r}\n"
            r"  Expected pattern: src/<file>.c:<line>:<col>: warning: <message>"
        )


def test_warnings_file_no_extra_whitespace_or_headers():
    """The file should contain only the raw warning lines with no headers or extra blank lines."""
    with open(WARNINGS_PATH, "r") as f:
        raw = f.read()

    # Should not start with a blank line
    assert not raw.startswith("\n"), (
        f"'{WARNINGS_PATH}' starts with a blank line. "
        "No headers or extra blank lines should be present."
    )

    # Should not have consecutive blank lines
    assert "\n\n" not in raw, (
        f"'{WARNINGS_PATH}' contains blank lines between entries. "
        "Only the raw warning lines should be present."
    )