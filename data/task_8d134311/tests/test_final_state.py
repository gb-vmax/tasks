# test_final_state.py

"""
Pytest suite to validate the final state after artifact verification.

This test suite checks that:
- /home/user/project/artifact_verification.log exists
- Its contents exactly match the expected output, in order, with correct line formatting
- The artifacts.ini file and artifact files have not been changed

Do not modify this file.
"""

import os
import pytest
import configparser

ARTIFACTS_INI = "/home/user/project/artifacts.ini"
BIN_DIR = "/home/user/project/bin"
ARTIFACT1_PATH = os.path.join(BIN_DIR, "artifact1-1.0.2.tar.gz")
ARTIFACT2_PATH = os.path.join(BIN_DIR, "artifact2-2.5.8.tar.gz")
ARTIFACT3_PATH = os.path.join(BIN_DIR, "artifact3-0.9.0.tar.gz")
LOG_PATH = "/home/user/project/artifact_verification.log"

EXPECTED_LOG_LINES = [
    f"artifact:artifact1 version:1.0.2 path:{ARTIFACT1_PATH} exists:yes",
    f"artifact:artifact2 version:2.5.8 path:{ARTIFACT2_PATH} exists:no",
    f"artifact:artifact3 version:0.9.0 path:{ARTIFACT3_PATH} exists:yes",
]


@pytest.mark.parametrize("path,should_exist", [
    (ARTIFACT1_PATH, True),
    (ARTIFACT2_PATH, False),
    (ARTIFACT3_PATH, True),
])
def test_artifact_file_state(path, should_exist):
    """Ensure artifact files' existence has not changed after task."""
    if should_exist:
        assert os.path.isfile(path), (
            f"Artifact file {path} is missing, but it must exist after the task."
        )
    else:
        assert not os.path.exists(path), (
            f"Artifact file {path} must NOT exist after the task."
        )


def test_artifacts_ini_still_correct():
    """Check that artifacts.ini still exists and has not been altered."""
    assert os.path.isfile(ARTIFACTS_INI), (
        f"{ARTIFACTS_INI} is missing after the task (should not be changed)."
    )
    config = configparser.ConfigParser()
    read_files = config.read(ARTIFACTS_INI)
    assert read_files, f"Failed to read {ARTIFACTS_INI} after the task."
    expected = {
        "artifact1": {
            "version": "1.0.2",
            "path": ARTIFACT1_PATH,
        },
        "artifact2": {
            "version": "2.5.8",
            "path": ARTIFACT2_PATH,
        },
        "artifact3": {
            "version": "0.9.0",
            "path": ARTIFACT3_PATH,
        },
    }
    for section, values in expected.items():
        assert config.has_section(section), (
            f"Missing section [{section}] in {ARTIFACTS_INI} after the task."
        )
        for key, expected_value in values.items():
            assert config.has_option(section, key), (
                f"Missing key '{key}' in section [{section}] after the task."
            )
            actual_value = config.get(section, key)
            assert actual_value == expected_value, (
                f"Incorrect value for '{key}' in section [{section}] after the task: "
                f"expected '{expected_value}', found '{actual_value}'."
            )


def test_artifact_verification_log_exists():
    """Check for existence of the log file."""
    assert os.path.isfile(LOG_PATH), (
        f"Expected log file {LOG_PATH} to exist after the task, but it does not."
    )


def test_artifact_verification_log_contents():
    """Check the exact contents of the log file."""
    assert os.path.isfile(LOG_PATH), (
        f"Expected log file {LOG_PATH} to exist after the task, but it does not."
    )

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        log_lines = f.read().splitlines()

    # Check number of lines
    assert len(log_lines) == len(EXPECTED_LOG_LINES), (
        f"Log file {LOG_PATH} has {len(log_lines)} lines; expected {len(EXPECTED_LOG_LINES)}.\n"
        f"Actual lines:\n{log_lines}\nExpected lines:\n{EXPECTED_LOG_LINES}"
    )

    # Check content and order
    for idx, (actual, expected) in enumerate(zip(log_lines, EXPECTED_LOG_LINES), 1):
        assert actual == expected, (
            f"Line {idx} in {LOG_PATH} is incorrect.\n"
            f"Expected: '{expected}'\n"
            f"Found:    '{actual}'"
        )

    # Check that there is no trailing blank line
    with open(LOG_PATH, "rb") as f:
        content = f.read()
        if content.endswith(b"\n"):
            # If the file ends with a newline, ensure it is not an extra blank line
            if content.endswith(b"\n\n"):
                pytest.fail(f"{LOG_PATH} has a trailing blank line at the end (should not).")


def test_log_file_formatting_strict():
    """Check that each line in the log file strictly follows the required format."""
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        log_lines = f.read().splitlines()

    import re
    line_re = re.compile(
        r"^artifact:([a-zA-Z0-9_]+) version:([0-9]+\.[0-9]+\.[0-9]+) path:(/home/user/project/bin/[^ ]+) exists:(yes|no)$"
    )
    for idx, line in enumerate(log_lines, 1):
        m = line_re.match(line)
        assert m, (
            f"Line {idx} in {LOG_PATH} does not match the required format:\n"
            f"  {line}\n"
            f"Expected format:\n"
            "  artifact:<artifact_name> version:<version> path:<path> exists:<yes|no>"
        )

        # Extra: Ensure path is absolute and matches the one from the ini file
        artifact_name, version, path, exists = m.groups()
        ini_config = configparser.ConfigParser()
        ini_config.read(ARTIFACTS_INI)
        assert ini_config.has_section(artifact_name), (
            f"Artifact '{artifact_name}' in log file does not appear in {ARTIFACTS_INI}."
        )
        expected_path = ini_config.get(artifact_name, "path")
        expected_version = ini_config.get(artifact_name, "version")
        assert path == expected_path, (
            f"Path for artifact '{artifact_name}' in log file is '{path}', "
            f"but expected '{expected_path}' from {ARTIFACTS_INI}."
        )
        assert version == expected_version, (
            f"Version for artifact '{artifact_name}' in log file is '{version}', "
            f"but expected '{expected_version}' from {ARTIFACTS_INI}."
        )
        # Check exists matches actual file presence
        file_should_exist = os.path.isfile(path)
        expected_exists = "yes" if file_should_exist else "no"
        assert exists == expected_exists, (
            f"Log file line for artifact '{artifact_name}' reports exists:{exists}, "
            f"but the file {path} {'exists' if file_should_exist else 'does NOT exist'}."
        )