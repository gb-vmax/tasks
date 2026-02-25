# test_final_state.py

"""
Pytest suite to validate the final OS/container state after running the legacy tool scripts and log collection task.

This suite verifies:
- Existence, content, and permissions of the two per-tool log files.
- Existence, content, and permissions of the summary log in the correct directory.
- Directory properties for /home/user/legacy_scripts_outputs.
- Exact summary formatting and log confirmation lines.

All paths are absolute and must match the specification exactly.
"""

import os
import stat
import pytest

HOME = "/home/user"
TOOL_A_DIR = os.path.join(HOME, "legacy_tool_a")
TOOL_B_DIR = os.path.join(HOME, "legacy_tool_b")
TOOL_A_PY = os.path.join(TOOL_A_DIR, "tool_a.py")
TOOL_B_PY = os.path.join(TOOL_B_DIR, "tool_b.py")
TOOL_A_RUN_LOG = os.path.join(TOOL_A_DIR, "run_output.log")
TOOL_B_RUN_LOG = os.path.join(TOOL_B_DIR, "run_output.log")
OUTPUTS_DIR = os.path.join(HOME, "legacy_scripts_outputs")
SUMMARY_LOG = os.path.join(OUTPUTS_DIR, "summary.log")

TOOL_A_OUTPUT = (
    "Tool A started\n"
    "Processing data...\n"
    "Tool A completed successfully\n"
)

TOOL_B_OUTPUT = (
    "Tool B initiated\n"
    "Analyzing files...\n"
    "Tool B finished without errors\n"
)

SUMMARY_EXPECTED = (
    "=== tool_a.py Output ===\n"
    "Tool A started\n"
    "Processing data...\n"
    "Tool A completed successfully\n"
    "=== tool_b.py Output ===\n"
    "Tool B initiated\n"
    "Analyzing files...\n"
    "Tool B finished without errors\n"
    "[LOG FILES CONFIRMED]\n"
    "legacy_tool_a/run_output.log\n"
    "legacy_tool_b/run_output.log\n"
    "summary.log\n"
)

def is_owned_and_accessible(path, mode=os.R_OK):
    """Check if file/directory is owned by user and accessible (readable or writable)"""
    try:
        st = os.stat(path)
        return st.st_uid == os.getuid() and os.access(path, mode)
    except Exception:
        return False

def assert_file_content(path, expected, msg):
    assert os.path.isfile(path), f"{msg}: '{path}' does not exist or is not a file."
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == expected, (
        f"{msg}: '{path}' contents do not match expected.\n"
        f"Expected:\n{expected!r}\nGot:\n{content!r}"
    )

def assert_file_exists_and_readable(path, msg):
    assert os.path.isfile(path), f"{msg}: '{path}' does not exist or is not a file."
    assert os.access(path, os.R_OK), f"{msg}: '{path}' is not readable by current user."
    st = os.stat(path)
    assert st.st_uid == os.getuid(), f"{msg}: '{path}' is not owned by the current user."

def assert_dir_exists_and_writable(path, msg):
    assert os.path.isdir(path), f"{msg}: '{path}' does not exist or is not a directory."
    assert os.access(path, os.W_OK), f"{msg}: '{path}' is not writable by current user."
    st = os.stat(path)
    assert st.st_uid == os.getuid(), f"{msg}: '{path}' is not owned by the current user."

@pytest.mark.describe("Final state: /home/user/legacy_tool_a/run_output.log exists and is correct")
def test_tool_a_run_output_log_exists_and_correct():
    assert_file_exists_and_readable(
        TOOL_A_RUN_LOG,
        "Tool A run output log missing or unreadable"
    )
    assert_file_content(
        TOOL_A_RUN_LOG,
        TOOL_A_OUTPUT,
        "Tool A run output log content incorrect"
    )

@pytest.mark.describe("Final state: /home/user/legacy_tool_b/run_output.log exists and is correct")
def test_tool_b_run_output_log_exists_and_correct():
    assert_file_exists_and_readable(
        TOOL_B_RUN_LOG,
        "Tool B run output log missing or unreadable"
    )
    assert_file_content(
        TOOL_B_RUN_LOG,
        TOOL_B_OUTPUT,
        "Tool B run output log content incorrect"
    )

@pytest.mark.describe("Final state: /home/user/legacy_scripts_outputs directory exists, owned, and writable")
def test_outputs_dir_exists_and_writable():
    assert_dir_exists_and_writable(
        OUTPUTS_DIR,
        "Legacy scripts outputs directory missing, not a directory, not writable, or not owned by user"
    )

@pytest.mark.describe("Final state: /home/user/legacy_scripts_outputs/summary.log exists and is correct")
def test_summary_log_exists_and_correct():
    assert_file_exists_and_readable(
        SUMMARY_LOG,
        "Summary log missing or unreadable"
    )
    assert_file_content(
        SUMMARY_LOG,
        SUMMARY_EXPECTED,
        "Summary log content does not match the required format"
    )

@pytest.mark.describe("Final state: Summary log confirms all three log files by relative path")
def test_summary_log_logfiles_confirmed_section():
    # Already checked entire file above, but let's check for the confirmation section as well
    with open(SUMMARY_LOG, "r", encoding="utf-8") as f:
        content = f.read()
    confirmation_section = (
        "[LOG FILES CONFIRMED]\n"
        "legacy_tool_a/run_output.log\n"
        "legacy_tool_b/run_output.log\n"
        "summary.log\n"
    )
    assert confirmation_section in content, (
        "Summary log does not contain the required '[LOG FILES CONFIRMED]' section with the exact three relative log paths."
    )

@pytest.mark.describe("Final state: All log files are regular files, readable and owned by user")
@pytest.mark.parametrize("log_path, label", [
    (TOOL_A_RUN_LOG, "Tool A run log"),
    (TOOL_B_RUN_LOG, "Tool B run log"),
    (SUMMARY_LOG, "Summary log"),
])
def test_log_files_are_regular_and_owned_and_readable(log_path, label):
    assert_file_exists_and_readable(
        log_path,
        f"{label} is missing, unreadable, or not owned by user"
    )
    st = os.stat(log_path)
    assert stat.S_ISREG(st.st_mode), f"{label} ('{log_path}') must be a regular file."

@pytest.mark.describe("Final state: No error output, command prompts, or extraneous content in log files")
def test_no_error_or_prompt_lines_in_logs():
    # The log files must contain only the correct output, with no error lines or shell prompts
    for path, expected, label in [
        (TOOL_A_RUN_LOG, TOOL_A_OUTPUT, "Tool A run log"),
        (TOOL_B_RUN_LOG, TOOL_B_OUTPUT, "Tool B run log"),
        (SUMMARY_LOG, SUMMARY_EXPECTED, "Summary log"),
    ]:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        # No '$', 'Traceback', or 'Error' or 'Exception' lines
        forbidden = ["$", "Traceback", "Error", "Exception"]
        for word in forbidden:
            assert word not in content, (
                f"{label} ('{path}') contains forbidden text ('{word}'). "
                f"Log files must only contain the expected output."
            )

@pytest.mark.describe("Final state: All required log files exist in correct absolute locations")
def test_log_files_exist_in_absolute_locations():
    assert os.path.isfile(TOOL_A_RUN_LOG), (
        f"Log file missing: {TOOL_A_RUN_LOG}"
    )
    assert os.path.isfile(TOOL_B_RUN_LOG), (
        f"Log file missing: {TOOL_B_RUN_LOG}"
    )
    assert os.path.isfile(SUMMARY_LOG), (
        f"Summary log missing: {SUMMARY_LOG}"
    )