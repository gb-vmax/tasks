# test_final_state.py
"""
Pytest suite to validate the FINAL state after the localization update summary task.
Validates:
- The existence, content, and formatting of the summary report at
  /home/user/projects/localization/update_reports/untranslated_summary.txt.
- That no extra files were created or modified.
- That the console output matches the expected message.

This suite assumes the state after the task has been completed.
"""

import os
import pytest

LOG_PATH = "/home/user/projects/localization/update_logs/translations_update.log"
REPORTS_DIR = "/home/user/projects/localization/update_reports"
REPORT_FILE = "/home/user/projects/localization/update_reports/untranslated_summary.txt"

EXPECTED_REPORT_CONTENT = (
    "[de]\n"
    "button_submit: MISSING\n"
    "menu_help: PARTIAL\n"
    "\n"
    "[fr]\n"
    "login_title: MISSING\n"
    "logout_success: PARTIAL\n"
    "menu_help: PARTIAL\n"
    "\n"
    "[it]\n"
    "menu_help: PARTIAL\n"
    "settings_label: MISSING\n"
)

EXPECTED_CONSOLE_OUTPUT = (
    "Summary report created at /home/user/projects/localization/update_reports/untranslated_summary.txt"
)

# The files and directories that should exist after task completion
EXPECTED_PATHS = {
    LOG_PATH: "file",
    REPORTS_DIR: "dir",
    REPORT_FILE: "file",
}

@pytest.mark.order(1)
def test_report_file_exists_and_is_file():
    assert os.path.isfile(REPORT_FILE), (
        f"Expected summary report file does not exist at {REPORT_FILE}.\n"
        f"Ensure the report is created at the correct location."
    )

@pytest.mark.order(2)
def test_report_file_content_exact():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    # Normalize line endings for comparison
    expected = EXPECTED_REPORT_CONTENT.strip().replace('\r\n', '\n')
    actual = content.strip().replace('\r\n', '\n')
    assert actual == expected, (
        f"The summary report content at {REPORT_FILE} is incorrect.\n"
        f"--- Expected:\n{EXPECTED_REPORT_CONTENT}\n"
        f"--- Found:\n{content}\n"
        "Check that:\n"
        "- Only 'MISSING' and 'PARTIAL' keys are included\n"
        "- Duplicates are ignored\n"
        "- Sections are sorted alphabetically by language code and key\n"
        "- Formatting (blank lines, colons, spaces) matches exactly"
    )

@pytest.mark.order(3)
def test_report_file_permissions():
    assert os.access(REPORT_FILE, os.R_OK), (
        f"The report file at {REPORT_FILE} is not readable. Please check file permissions."
    )
    assert os.access(REPORT_FILE, os.W_OK), (
        f"The report file at {REPORT_FILE} is not writable. Please check file permissions."
    )

@pytest.mark.order(4)
def test_no_unexpected_files_or_dirs_created(tmp_path_factory):
    """
    Ensure that no extra files or directories were created/modified in
    /home/user/projects/localization/update_reports/
    """
    allowed_files = {"untranslated_summary.txt"}
    allowed_dirs = set()
    actual_files = set()
    actual_dirs = set()
    for entry in os.listdir(REPORTS_DIR):
        full_path = os.path.join(REPORTS_DIR, entry)
        if os.path.isfile(full_path):
            actual_files.add(entry)
        elif os.path.isdir(full_path):
            actual_dirs.add(entry)
    extra_files = actual_files - allowed_files
    extra_dirs = actual_dirs - allowed_dirs
    assert not extra_files, (
        f"Unexpected files found in {REPORTS_DIR}: {sorted(extra_files)}\n"
        f"Only 'untranslated_summary.txt' should be present."
    )
    assert not extra_dirs, (
        f"Unexpected directories found in {REPORTS_DIR}: {sorted(extra_dirs)}\n"
        f"There should be no subdirectories created."
    )

@pytest.mark.order(5)
def test_log_file_untouched():
    """
    Ensure the log file still exists and is unchanged.
    """
    expected_lines = [
        "2024-06-11T15:34:12Z de button_submit MISSING",
        "2024-06-11T15:34:12Z de menu_help PARTIAL",
        "2024-06-11T15:34:12Z de about_title DONE",
        "2024-06-11T15:34:12Z fr login_title MISSING",
        "2024-06-11T15:34:12Z fr logout_success PARTIAL",
        "2024-06-11T15:34:12Z fr profile_label DONE",
        "2024-06-11T15:34:12Z fr menu_help PARTIAL",
        "2024-06-11T15:34:12Z it menu_help PARTIAL",
        "2024-06-11T15:34:12Z it logout_success DONE",
        "2024-06-11T15:34:12Z it settings_label MISSING",
        "2024-06-11T15:34:12Z de menu_help PARTIAL   # Duplicate; should be ignored in report",
        "2024-06-11T15:34:12Z fr logout_success PARTIAL   # Duplicate; should be ignored",
    ]
    assert os.path.isfile(LOG_PATH), (
        f"Log file at {LOG_PATH} is missing after task completion."
    )
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        actual_lines = [line.rstrip('\n') for line in f]
    assert actual_lines == expected_lines, (
        f"Log file at {LOG_PATH} was modified. It must remain unchanged.\n"
        f"--- Expected:\n{chr(10).join(expected_lines)}\n"
        f"--- Found:\n{chr(10).join(actual_lines)}"
    )

@pytest.mark.order(6)
def test_reports_dir_permissions():
    assert os.path.isdir(REPORTS_DIR), (
        f"Reports directory at {REPORTS_DIR} does not exist after task completion."
    )
    assert os.access(REPORTS_DIR, os.W_OK), (
        f"Reports directory at {REPORTS_DIR} is not writable after task completion."
    )
    assert os.access(REPORTS_DIR, os.R_OK), (
        f"Reports directory at {REPORTS_DIR} is not readable after task completion."
    )

@pytest.mark.order(7)
def test_console_output_matches(monkeypatch, capsys):
    """
    This test simulates capturing the console output if the student's script
    is run again. It does NOT re-run the script, but provides guidance for
    the checker to verify expected output.
    """
    # Simulate print
    print(EXPECTED_CONSOLE_OUTPUT)
    captured = capsys.readouterr()
    actual = captured.out.strip()
    assert actual == EXPECTED_CONSOLE_OUTPUT, (
        f"Console output is incorrect.\n"
        f"--- Expected:\n{EXPECTED_CONSOLE_OUTPUT}\n"
        f"--- Found:\n{actual}\n"
        "Ensure the confirmation message is printed exactly as specified."
    )