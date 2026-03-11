# test_final_state.py

import os
import pytest

LOG_PATH = "/home/user/builds/nightly.log"
FAILED_ARTIFACTS_PATH = "/home/user/builds/failed_artifacts.txt"
BUILDS_DIR = "/home/user/builds"

EXPECTED_FAILED_ARTIFACTS = [
    "libui-3.0.1.tar.gz",
    "libgfx-5.2.0.tar.gz",
    "libauth-0.9.1.tar.gz",
    "libparse-4.0.0.tar.gz",
]

EXPECTED_FILE_CONTENT = (
    "libui-3.0.1.tar.gz\n"
    "libgfx-5.2.0.tar.gz\n"
    "libauth-0.9.1.tar.gz\n"
    "libparse-4.0.0.tar.gz\n"
)


def test_builds_directory_exists():
    assert os.path.isdir(BUILDS_DIR), (
        f"Builds directory does not exist: {BUILDS_DIR}"
    )


def test_failed_artifacts_file_exists():
    assert os.path.isfile(FAILED_ARTIFACTS_PATH), (
        f"Expected output file does not exist: {FAILED_ARTIFACTS_PATH}\n"
        "The task requires creating this file with the failed artifact names."
    )


def test_failed_artifacts_file_is_readable():
    assert os.access(FAILED_ARTIFACTS_PATH, os.R_OK), (
        f"File exists but is not readable: {FAILED_ARTIFACTS_PATH}"
    )


def test_failed_artifacts_file_exact_content():
    with open(FAILED_ARTIFACTS_PATH, "r") as f:
        content = f.read()
    assert content == EXPECTED_FILE_CONTENT, (
        f"File content does not exactly match expected.\n"
        f"Expected (repr): {repr(EXPECTED_FILE_CONTENT)}\n"
        f"Got (repr):      {repr(content)}\n\n"
        f"Expected:\n{EXPECTED_FILE_CONTENT}\n"
        f"Got:\n{content}"
    )


def test_failed_artifacts_file_has_four_lines():
    with open(FAILED_ARTIFACTS_PATH, "r") as f:
        content = f.read()
    # Split on newlines; trailing newline means last element is empty string
    lines = content.split("\n")
    # Remove the trailing empty string caused by the final newline
    if lines and lines[-1] == "":
        lines = lines[:-1]
    assert len(lines) == 4, (
        f"Expected exactly 4 artifact lines in {FAILED_ARTIFACTS_PATH}, "
        f"got {len(lines)}.\nLines found: {lines}"
    )


def test_failed_artifacts_file_correct_artifact_names():
    with open(FAILED_ARTIFACTS_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    assert lines == EXPECTED_FAILED_ARTIFACTS, (
        f"Artifact names in file do not match expected.\n"
        f"Expected: {EXPECTED_FAILED_ARTIFACTS}\n"
        f"Got:      {lines}"
    )


def test_failed_artifacts_file_correct_order():
    with open(FAILED_ARTIFACTS_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    for i, (actual, expected) in enumerate(zip(lines, EXPECTED_FAILED_ARTIFACTS)):
        assert actual == expected, (
            f"Line {i + 1} in {FAILED_ARTIFACTS_PATH} is incorrect.\n"
            f"Expected: '{expected}'\n"
            f"Got:      '{actual}'"
        )


def test_failed_artifacts_file_ends_with_newline():
    with open(FAILED_ARTIFACTS_PATH, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        f"File {FAILED_ARTIFACTS_PATH} does not end with a trailing newline.\n"
        f"Last character (repr): {repr(content[-1]) if content else 'file is empty'}"
    )


def test_failed_artifacts_file_no_blank_lines():
    with open(FAILED_ARTIFACTS_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    # The last element after split will be '' due to trailing newline — that's acceptable
    # Check that no other blank lines exist
    non_trailing_lines = lines[:-1] if lines and lines[-1] == "" else lines
    blank_lines = [i + 1 for i, line in enumerate(non_trailing_lines) if line.strip() == ""]
    assert not blank_lines, (
        f"File {FAILED_ARTIFACTS_PATH} contains blank lines at positions: {blank_lines}"
    )


def test_failed_artifacts_file_no_extra_whitespace():
    with open(FAILED_ARTIFACTS_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    for i, line in enumerate(lines):
        assert line == line.strip(), (
            f"Line {i + 1} in {FAILED_ARTIFACTS_PATH} has extra whitespace.\n"
            f"Got (repr): {repr(line)}"
        )


def test_failed_artifacts_no_artifact_prefix():
    with open(FAILED_ARTIFACTS_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    for i, line in enumerate(lines):
        assert not line.startswith("artifact="), (
            f"Line {i + 1} in {FAILED_ARTIFACTS_PATH} still contains 'artifact=' prefix.\n"
            f"Got: '{line}'"
        )


def test_failed_artifacts_no_brackets():
    with open(FAILED_ARTIFACTS_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    for i, line in enumerate(lines):
        assert "[" not in line and "]" not in line, (
            f"Line {i + 1} in {FAILED_ARTIFACTS_PATH} contains brackets.\n"
            f"Got: '{line}'"
        )


def test_failed_artifacts_no_timestamps():
    with open(FAILED_ARTIFACTS_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    for i, line in enumerate(lines):
        assert "FAILED" not in line and "SUCCESS" not in line, (
            f"Line {i + 1} in {FAILED_ARTIFACTS_PATH} contains status text.\n"
            f"Got: '{line}'"
        )


def test_log_file_unchanged():
    """Ensure the original log file has not been modified."""
    EXPECTED_LOG_CONTENT = (
        "[2024-11-01 02:11:03] [SUCCESS] artifact=libbase-1.0.0.tar.gz size=204800\n"
        "[2024-11-01 02:11:47] [SUCCESS] artifact=libcore-2.1.0.tar.gz size=104857\n"
        "[2024-11-01 02:12:30] [FAILED] artifact=libui-3.0.1.tar.gz size=0\n"
        "[2024-11-01 02:13:15] [SUCCESS] artifact=libnet-1.4.2.tar.gz size=309120\n"
        "[2024-11-01 02:14:02] [FAILED] artifact=libgfx-5.2.0.tar.gz size=0\n"
        "[2024-11-01 02:14:48] [SUCCESS] artifact=libio-2.0.0.tar.gz size=153600\n"
        "[2024-11-01 02:15:33] [FAILED] artifact=libauth-0.9.1.tar.gz size=0\n"
        "[2024-11-01 02:16:19] [SUCCESS] artifact=libcache-3.1.4.tar.gz size=256000\n"
        "[2024-11-01 02:17:05] [FAILED] artifact=libparse-4.0.0.tar.gz size=0\n"
        "[2024-11-01 02:17:50] [SUCCESS] artifact=libsync-1.2.3.tar.gz size=179200"
    )
    assert os.path.isfile(LOG_PATH), (
        f"Log file does not exist: {LOG_PATH}"
    )
    with open(LOG_PATH, "r") as f:
        content = f.read()
    assert content.strip() == EXPECTED_LOG_CONTENT.strip(), (
        f"Log file {LOG_PATH} has been modified!\n"
        f"Expected:\n{EXPECTED_LOG_CONTENT}\n\n"
        f"Got:\n{content}"
    )