# test_final_state.py

import os
import pytest

HOME = "/home/user"
ARTIFACTS_DIR = os.path.join(HOME, "artifacts")
BUILD_OUTPUT = os.path.join(ARTIFACTS_DIR, "build-output.txt")
FAILED_ARTIFACTS = os.path.join(ARTIFACTS_DIR, "failed-artifacts.txt")
ARTIFACT_PIPELINE_LOG = os.path.join(ARTIFACTS_DIR, "artifact-pipeline.log")

EXPECTED_FAILED_ARTIFACTS = ["artifact43", "artifact45"]
EXPECTED_ARTIFACT_PIPELINE_LOG = [
    "PROCESSED: [artifact42]",
    "RECOVERED: [artifact43]",
    "PROCESSED: [artifact44]",
    "RECOVERED: [artifact45]",
]
EXPECTED_CONSOLE_OUTPUT = "One or more artifacts failed and are recorded.\n"


def test_artifacts_directory_still_exists():
    assert os.path.isdir(ARTIFACTS_DIR), (
        f"Required directory does not exist: {ARTIFACTS_DIR}"
    )


def test_build_output_txt_unchanged():
    """build-output.txt should remain as initially provided."""
    expected_lines = [
        "artifact42,2024-06-12T16:12:03Z,SUCCESS\n",
        "artifact43,2024-06-12T16:15:45Z,FAILED\n",
        "artifact44,2024-06-12T16:17:00Z,SUCCESS\n",
        "artifact45,2024-06-12T16:18:34Z,MISSING\n",
    ]
    assert os.path.isfile(BUILD_OUTPUT), f"Missing file: {BUILD_OUTPUT}"
    with open(BUILD_OUTPUT, "rt", encoding="utf-8") as f:
        actual_lines = f.readlines()
    assert actual_lines == expected_lines, (
        f"{BUILD_OUTPUT} was modified or is corrupted.\n"
        f"Expected:\n{''.join(expected_lines)}\n"
        f"Found:\n{''.join(actual_lines)}"
    )


def test_failed_artifacts_txt_final_content():
    """failed-artifacts.txt should contain artifact43 and artifact45, one per line, no extra whitespace."""
    assert os.path.isfile(FAILED_ARTIFACTS), f"Missing file: {FAILED_ARTIFACTS}"
    with open(FAILED_ARTIFACTS, "rt", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    assert lines == EXPECTED_FAILED_ARTIFACTS, (
        f"{FAILED_ARTIFACTS} contains incorrect failed artifact IDs.\n"
        f"Expected (one per line):\n{chr(10).join(EXPECTED_FAILED_ARTIFACTS)}\n"
        f"Found (one per line):\n{chr(10).join(lines)}"
    )


def test_artifact_pipeline_log_content():
    """artifact-pipeline.log should have the correct log entries, one per artifact, in order, no blank lines."""
    assert os.path.isfile(ARTIFACT_PIPELINE_LOG), (
        f"{ARTIFACT_PIPELINE_LOG} does not exist after the task is complete."
    )
    with open(ARTIFACT_PIPELINE_LOG, "rt", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    assert lines == EXPECTED_ARTIFACT_PIPELINE_LOG, (
        f"{ARTIFACT_PIPELINE_LOG} has incorrect content.\n"
        f"Expected (one per line):\n{chr(10).join(EXPECTED_ARTIFACT_PIPELINE_LOG)}\n"
        f"Found (one per line):\n{chr(10).join(lines)}"
    )


def test_failed_artifacts_txt_no_blank_lines_or_whitespace():
    """failed-artifacts.txt should have no blank lines or extra whitespace."""
    with open(FAILED_ARTIFACTS, "rt", encoding="utf-8") as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        assert line.strip() == line.rstrip("\n"), (
            f"Line {idx} in {FAILED_ARTIFACTS} has leading/trailing whitespace: {repr(line)}"
        )
        assert line.endswith("\n"), (
            f"Line {idx} in {FAILED_ARTIFACTS} does not end with newline: {repr(line)}"
        )
    assert lines, f"{FAILED_ARTIFACTS} should contain failed artifact IDs, but is empty."


def test_artifact_pipeline_log_no_blank_lines_or_whitespace():
    """artifact-pipeline.log should have no blank lines or extra whitespace."""
    with open(ARTIFACT_PIPELINE_LOG, "rt", encoding="utf-8") as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        assert line.strip() == line.rstrip("\n"), (
            f"Line {idx} in {ARTIFACT_PIPELINE_LOG} has leading/trailing whitespace: {repr(line)}"
        )
        assert line.endswith("\n"), (
            f"Line {idx} in {ARTIFACT_PIPELINE_LOG} does not end with newline: {repr(line)}"
        )
    assert lines, f"{ARTIFACT_PIPELINE_LOG} should contain log entries, but is empty."


@pytest.mark.skipif(
    "ARTIFACT_PIPELINE_STDOUT" not in os.environ,
    reason="Console output capture not available. Set ARTIFACT_PIPELINE_STDOUT env var to test console output."
)
def test_console_output_for_failed_artifacts(monkeypatch):
    """
    If the agent's process outputs to the console, it must print the correct message
    ONLY if any artifact_id is appended to failed-artifacts.txt.
    This test requires the environment variable ARTIFACT_PIPELINE_STDOUT to be set
    to the captured standard output during agent execution.
    """
    stdout = os.environ.get("ARTIFACT_PIPELINE_STDOUT", "")
    assert stdout == EXPECTED_CONSOLE_OUTPUT, (
        "Console output is incorrect or missing.\n"
        f"Expected:\n{EXPECTED_CONSOLE_OUTPUT!r}\n"
        f"Found:\n{stdout!r}"
    )