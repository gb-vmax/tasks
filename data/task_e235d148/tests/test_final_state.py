# test_final_state.py

import os
import stat
import subprocess
import pytest

SCRIPT_PATH = "/home/user/pipeline/summarize_build.sh"
BUILD_LOG = "/home/user/pipeline/build.log"
PIPELINE_DIR = "/home/user/pipeline"

EXPECTED_OUTPUT = """\
=== BUILD SUMMARY ===
Started:  2024-05-10 08:31:45
Finished: 2024-05-10 08:44:02
Status:   FAILED
Modules compiled: 7
Modules failed:   2
Warnings:         3"""


def test_pipeline_directory_exists():
    assert os.path.isdir(PIPELINE_DIR), (
        f"Pipeline directory '{PIPELINE_DIR}' does not exist."
    )


def test_build_log_still_exists():
    assert os.path.isfile(BUILD_LOG), (
        f"Build log file '{BUILD_LOG}' no longer exists. It must not be removed."
    )


def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), (
        f"Script '{SCRIPT_PATH}' does not exist. "
        "The student must create this file."
    )


def test_script_is_executable():
    st = os.stat(SCRIPT_PATH)
    is_executable = bool(st.st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
    assert is_executable, (
        f"Script '{SCRIPT_PATH}' is not executable. "
        "Run 'chmod +x /home/user/pipeline/summarize_build.sh' to fix this."
    )


def test_script_is_shell_script():
    with open(SCRIPT_PATH, "r") as f:
        first_line = f.readline().strip()
    assert first_line.startswith("#!"), (
        f"Script '{SCRIPT_PATH}' does not start with a shebang line (e.g., '#!/bin/bash'). "
        f"First line was: {first_line!r}"
    )
    assert "sh" in first_line or "bash" in first_line, (
        f"Script '{SCRIPT_PATH}' shebang does not reference a shell interpreter. "
        f"First line was: {first_line!r}"
    )


def test_script_reads_correct_log_file():
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    assert "/home/user/pipeline/build.log" in content, (
        f"Script '{SCRIPT_PATH}' does not reference the required log file path "
        "'/home/user/pipeline/build.log'. The path must be hardcoded or used in the script."
    )


def test_script_does_not_use_python_or_perl():
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    # Check that the script itself doesn't invoke python or perl
    import re
    python_pattern = re.compile(r'\bpython[23]?\b', re.IGNORECASE)
    perl_pattern = re.compile(r'\bperl\b', re.IGNORECASE)
    assert not python_pattern.search(content), (
        f"Script '{SCRIPT_PATH}' appears to use Python, which is not allowed. "
        "Use only standard shell tools (grep, awk, sed, wc, etc.)."
    )
    assert not perl_pattern.search(content), (
        f"Script '{SCRIPT_PATH}' appears to use Perl, which is not allowed. "
        "Use only standard shell tools (grep, awk, sed, wc, etc.)."
    )


def test_script_runs_successfully():
    result = subprocess.run(
        [SCRIPT_PATH],
        capture_output=True,
        text=True,
        timeout=30
    )
    assert result.returncode == 0, (
        f"Script '{SCRIPT_PATH}' exited with non-zero return code {result.returncode}.\n"
        f"stdout: {result.stdout!r}\n"
        f"stderr: {result.stderr!r}"
    )


def test_script_output_matches_expected():
    result = subprocess.run(
        [SCRIPT_PATH],
        capture_output=True,
        text=True,
        timeout=30
    )
    actual_output = result.stdout.strip()
    assert actual_output == EXPECTED_OUTPUT, (
        f"Script output does not match expected output.\n\n"
        f"Expected:\n{EXPECTED_OUTPUT}\n\n"
        f"Got:\n{actual_output}\n\n"
        f"Diff (expected vs actual):\n"
        + _diff_strings(EXPECTED_OUTPUT, actual_output)
    )


def test_output_header_line():
    result = subprocess.run(
        [SCRIPT_PATH],
        capture_output=True,
        text=True,
        timeout=30
    )
    lines = result.stdout.splitlines()
    assert len(lines) >= 1, "Script produced no output."
    assert lines[0] == "=== BUILD SUMMARY ===", (
        f"First line of output should be '=== BUILD SUMMARY ===', "
        f"but got: {lines[0]!r}"
    )


def test_output_started_line():
    result = subprocess.run(
        [SCRIPT_PATH],
        capture_output=True,
        text=True,
        timeout=30
    )
    lines = result.stdout.splitlines()
    started_lines = [l for l in lines if l.startswith("Started:")]
    assert len(started_lines) == 1, (
        f"Expected exactly 1 line starting with 'Started:', found {len(started_lines)}.\n"
        f"Output lines: {lines}"
    )
    assert started_lines[0] == "Started:  2024-05-10 08:31:45", (
        f"'Started:' line does not match expected format and value.\n"
        f"Expected: 'Started:  2024-05-10 08:31:45'\n"
        f"Got:      {started_lines[0]!r}\n"
        "Note: There must be exactly two spaces after 'Started:' before the value."
    )


def test_output_finished_line():
    result = subprocess.run(
        [SCRIPT_PATH],
        capture_output=True,
        text=True,
        timeout=30
    )
    lines = result.stdout.splitlines()
    finished_lines = [l for l in lines if l.startswith("Finished:")]
    assert len(finished_lines) == 1, (
        f"Expected exactly 1 line starting with 'Finished:', found {len(finished_lines)}.\n"
        f"Output lines: {lines}"
    )
    assert finished_lines[0] == "Finished: 2024-05-10 08:44:02", (
        f"'Finished:' line does not match expected format and value.\n"
        f"Expected: 'Finished: 2024-05-10 08:44:02'\n"
        f"Got:      {finished_lines[0]!r}\n"
        "Note: There must be exactly one space after 'Finished:' before the value."
    )


def test_output_status_line():
    result = subprocess.run(
        [SCRIPT_PATH],
        capture_output=True,
        text=True,
        timeout=30
    )
    lines = result.stdout.splitlines()
    status_lines = [l for l in lines if l.startswith("Status:")]
    assert len(status_lines) == 1, (
        f"Expected exactly 1 line starting with 'Status:', found {len(status_lines)}.\n"
        f"Output lines: {lines}"
    )
    assert status_lines[0] == "Status:   FAILED", (
        f"'Status:' line does not match expected format and value.\n"
        f"Expected: 'Status:   FAILED'\n"
        f"Got:      {status_lines[0]!r}\n"
        "Note: There must be exactly three spaces after 'Status:' before the value."
    )


def test_output_modules_compiled_line():
    result = subprocess.run(
        [SCRIPT_PATH],
        capture_output=True,
        text=True,
        timeout=30
    )
    lines = result.stdout.splitlines()
    compiled_lines = [l for l in lines if l.startswith("Modules compiled:")]
    assert len(compiled_lines) == 1, (
        f"Expected exactly 1 line starting with 'Modules compiled:', found {len(compiled_lines)}.\n"
        f"Output lines: {lines}"
    )
    assert compiled_lines[0] == "Modules compiled: 7", (
        f"'Modules compiled:' line does not match expected format and value.\n"
        f"Expected: 'Modules compiled: 7'\n"
        f"Got:      {compiled_lines[0]!r}\n"
        "Note: There must be exactly one space after 'Modules compiled:' before the value, "
        "and the count must be 7."
    )


def test_output_modules_failed_line():
    result = subprocess.run(
        [SCRIPT_PATH],
        capture_output=True,
        text=True,
        timeout=30
    )
    lines = result.stdout.splitlines()
    failed_lines = [l for l in lines if l.startswith("Modules failed:")]
    assert len(failed_lines) == 1, (
        f"Expected exactly 1 line starting with 'Modules failed:', found {len(failed_lines)}.\n"
        f"Output lines: {lines}"
    )
    assert failed_lines[0] == "Modules failed:   2", (
        f"'Modules failed:' line does not match expected format and value.\n"
        f"Expected: 'Modules failed:   2'\n"
        f"Got:      {failed_lines[0]!r}\n"
        "Note: There must be exactly three spaces after 'Modules failed:' before the value, "
        "and the count must be 2."
    )


def test_output_warnings_line():
    result = subprocess.run(
        [SCRIPT_PATH],
        capture_output=True,
        text=True,
        timeout=30
    )
    lines = result.stdout.splitlines()
    warnings_lines = [l for l in lines if l.startswith("Warnings:")]
    assert len(warnings_lines) == 1, (
        f"Expected exactly 1 line starting with 'Warnings:', found {len(warnings_lines)}.\n"
        f"Output lines: {lines}"
    )
    assert warnings_lines[0] == "Warnings:         3", (
        f"'Warnings:' line does not match expected format and value.\n"
        f"Expected: 'Warnings:         3'\n"
        f"Got:      {warnings_lines[0]!r}\n"
        "Note: There must be exactly nine spaces after 'Warnings:' before the value, "
        "and the count must be 3."
    )


def test_output_has_exactly_seven_lines():
    result = subprocess.run(
        [SCRIPT_PATH],
        capture_output=True,
        text=True,
        timeout=30
    )
    lines = result.stdout.strip().splitlines()
    assert len(lines) == 7, (
        f"Expected exactly 7 lines of output, but got {len(lines)}.\n"
        f"Output:\n{result.stdout}"
    )


def test_build_log_content_unchanged():
    """Ensure the build log was not modified by the script."""
    expected_content = """\
[TIMESTAMP] BUILD STARTED: 2024-05-10 08:31:45
[INFO] Initializing build environment
[INFO] Compiled module: core SUCCESS
[INFO] Compiled module: auth SUCCESS
[WARN] Deprecated API usage in NetworkManager.kt
[INFO] Compiled module: payments FAILED
[INFO] Compiled module: ui SUCCESS
[WARN] Using legacy serialization in DataStore.kt
[INFO] Compiled module: notifications SUCCESS
[WARN] Null safety bypass detected in UserSession.kt
[INFO] Compiled module: analytics FAILED
[INFO] Compiled module: sync SUCCESS
[TIMESTAMP] BUILD FINISHED: 2024-05-10 08:44:02
[RESULT] BUILD STATUS: FAILED"""

    with open(BUILD_LOG, "r") as f:
        content = f.read().strip()
    assert content == expected_content, (
        f"Build log file '{BUILD_LOG}' has been modified from its original content.\n"
        f"Expected:\n{expected_content}\n\n"
        f"Got:\n{content}"
    )


def _diff_strings(expected: str, actual: str) -> str:
    """Return a simple line-by-line diff of two strings."""
    expected_lines = expected.splitlines()
    actual_lines = actual.splitlines()
    diff_lines = []
    max_len = max(len(expected_lines), len(actual_lines))
    for i in range(max_len):
        exp_line = expected_lines[i] if i < len(expected_lines) else "<missing>"
        act_line = actual_lines[i] if i < len(actual_lines) else "<missing>"
        if exp_line != act_line:
            diff_lines.append(f"  Line {i+1}:")
            diff_lines.append(f"    Expected: {exp_line!r}")
            diff_lines.append(f"    Actual:   {act_line!r}")
    return "\n".join(diff_lines) if diff_lines else "(no line-level differences found)"