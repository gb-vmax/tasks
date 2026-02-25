# test_final_state.py

"""
Pytest suite to validate the final state after CI/CD build log analysis.

This test suite checks:
- The existence and content of the build logs and summary report.
- That the summary report matches the expected format and values.
- That the log analysis print statement was output.

Only standard library and pytest are used.
"""

import os
import pytest

CICD_LOGS_DIR = "/home/user/cicd_logs"
LOG1 = os.path.join(CICD_LOGS_DIR, "build_log_2024-06-01.txt")
LOG2 = os.path.join(CICD_LOGS_DIR, "build_log_2024-06-02.txt")
SUMMARY = os.path.join(CICD_LOGS_DIR, "build_failure_summary.txt")

EXPECTED_LOG1 = (
    "Build #101: BUILD SUCCESS\n"
    "Build #102: BUILD FAILED: DependencyError - missing package xyz\n"
    "Build #103: BUILD SUCCESS\n"
    "Build #104: BUILD FAILED: TestError - test suite failed\n"
    "Build #105: BUILD FAILED: DependencyError - missing package xyz\n"
    "Build #106: BUILD SUCCESS\n"
)
EXPECTED_LOG2 = (
    "Build #201: BUILD SUCCESS\n"
    "Build #202: BUILD SUCCESS\n"
    "Build #203: BUILD FAILED: TimeoutError - build step exceeded time limit\n"
    "Build #204: BUILD FAILED: DependencyError - missing package xyz\n"
    "Build #205: BUILD FAILED: TestError - test suite failed\n"
)
EXPECTED_SUMMARY = (
    "Total builds: 11\n"
    "Failed builds: 6\n"
    "Most common failure: DependencyError - missing package xyz\n"
    "\n"
    "Unique failures:\n"
    "2024-06-01 - DependencyError - missing package xyz\n"
    "2024-06-01 - TestError - test suite failed\n"
    "2024-06-02 - TimeoutError - build step exceeded time limit\n"
)

@pytest.mark.parametrize("filepath,expected", [
    (LOG1, EXPECTED_LOG1),
    (LOG2, EXPECTED_LOG2),
])
def test_log_files_exist_and_content(filepath, expected):
    """Check that both log files exist and have the correct content."""
    assert os.path.isfile(filepath), (
        f"Expected log file '{filepath}' does not exist."
    )
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == expected, (
        f"Log file '{filepath}' does not match the expected content.\n"
        "---- Expected ----\n"
        f"{expected!r}\n"
        "---- Actual ----\n"
        f"{content!r}"
    )

def test_summary_report_file_exists():
    """Check that the summary report file exists."""
    assert os.path.isfile(SUMMARY), (
        f"Summary report file '{SUMMARY}' does not exist. "
        "Did you generate it in the correct location?"
    )

def test_summary_report_content_exact():
    """Check that the summary report content matches exactly the expected output."""
    with open(SUMMARY, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_SUMMARY, (
        "Summary report content does not match expected output.\n"
        "---- Expected ----\n"
        f"{EXPECTED_SUMMARY!r}\n"
        "---- Actual ----\n"
        f"{content!r}\n"
        "Check:\n"
        "- Total/Failed builds counts\n"
        "- Most common failure message\n"
        "- Unique failures list (order, format, no duplicates, correct date for first appearance)\n"
        "- That there are no extra or missing blank lines"
    )

def test_no_extra_or_missing_files():
    """Check that only the expected files exist in the cicd_logs directory."""
    expected_files = {
        "build_log_2024-06-01.txt",
        "build_log_2024-06-02.txt",
        "build_failure_summary.txt",
    }
    files = set(os.listdir(CICD_LOGS_DIR))
    extra = files - expected_files
    missing = expected_files - files
    assert not missing, (
        f"Missing expected files in '{CICD_LOGS_DIR}': {missing}"
    )
    assert not extra, (
        f"Found unexpected files in '{CICD_LOGS_DIR}': {extra}"
    )

def test_log_analysis_printed_to_stdout(monkeypatch):
    """
    Check that the correct print statement is output when the script is run.

    NOTE: This test assumes the analysis script is run as a Python script (not as a module).
    If this is not possible to re-invoke, skip this test.
    """
    import sys
    import subprocess

    # Try to find the student's script
    candidate_scripts = []
    for fname in ("analyze_logs.py", "log_analysis.py", "analyze_cicd_logs.py"):
        candidate = os.path.join(CICD_LOGS_DIR, fname)
        if os.path.isfile(candidate):
            candidate_scripts.append(candidate)
    if not candidate_scripts:
        pytest.skip(
            "Could not find the student's log analysis script in /home/user/cicd_logs/. "
            "Please ensure your script is named 'analyze_logs.py' or similar."
        )
    script = candidate_scripts[0]
    result = subprocess.run(
        [sys.executable, script],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        cwd=CICD_LOGS_DIR,
    )
    expected_print = (
        "Log analysis complete. Summary written to /home/user/cicd_logs/build_failure_summary.txt"
    )
    out = result.stdout.strip()
    assert expected_print in out, (
        f"Expected print statement not found when running '{script}'.\n"
        f"Expected: {expected_print!r}\n"
        f"Actual stdout:\n{out!r}\n"
        f"Actual stderr:\n{result.stderr.strip()!r}"
    )