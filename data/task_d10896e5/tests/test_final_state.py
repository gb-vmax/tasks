# test_final_state.py

import os
import pytest

PROJECT_DIR = "/home/user/old_project"
RUN_LOG = os.path.join(PROJECT_DIR, "run.log")
SUMMARY_TXT = os.path.join(PROJECT_DIR, "output_summary.txt")

EXPECTED_RUN_LOG = "Project executed successfully!\nHelper function called.\n"
EXPECTED_SUMMARY = (
    "run.log exists: YES\n"
    "Output preview: Project executed successfully!\n"
)

def test_run_log_exists():
    assert os.path.isfile(RUN_LOG), (
        f"Missing required file: {RUN_LOG}. "
        "Expected 'run.log' to be created in /home/user/old_project after running main.py."
    )

def test_run_log_contents():
    with open(RUN_LOG, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_RUN_LOG, (
        f"Incorrect contents in {RUN_LOG}.\n"
        f"Expected:\n{repr(EXPECTED_RUN_LOG)}\n"
        f"Found:\n{repr(content)}"
    )

def test_summary_exists():
    assert os.path.isfile(SUMMARY_TXT), (
        f"Missing required file: {SUMMARY_TXT}. "
        "Expected 'output_summary.txt' to be created in /home/user/old_project."
    )

def test_summary_contents():
    with open(SUMMARY_TXT, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_SUMMARY, (
        f"Incorrect contents in {SUMMARY_TXT}.\n"
        f"Expected exactly:\n{repr(EXPECTED_SUMMARY)}\n"
        f"Found:\n{repr(content)}"
    )

def test_summary_formatting():
    # Ensure summary file has exactly 2 lines, no extra whitespace or lines
    with open(SUMMARY_TXT, "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) == 2, (
        f"{SUMMARY_TXT} must have exactly two lines, found {len(lines)}.\n"
        f"Lines found:\n{lines}"
    )
    assert lines[0] == "run.log exists: YES\n", (
        f"First line of {SUMMARY_TXT} incorrect.\n"
        f"Expected: 'run.log exists: YES\\n'\n"
        f"Found: {repr(lines[0])}"
    )
    assert lines[1] == "Output preview: Project executed successfully!\n", (
        f"Second line of {SUMMARY_TXT} incorrect.\n"
        f"Expected: 'Output preview: Project executed successfully!\\n'\n"
        f"Found: {repr(lines[1])}"
    )