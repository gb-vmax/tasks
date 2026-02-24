# test_final_state.py

import os
import pytest

LOCALIZATION_DIR = "/home/user/localization"
SOURCE_TXT = os.path.join(LOCALIZATION_DIR, "source.txt")
OLD_FR_TXT = os.path.join(LOCALIZATION_DIR, "old_fr.txt")
NEW_FR_TXT = os.path.join(LOCALIZATION_DIR, "new_fr.txt")
UPDATE_LOG = os.path.join(LOCALIZATION_DIR, "update.log")

EXPECTED_NEW_FR_LINES = [
    "Welcome=Bienvenue",
    "Hello=Bonjour",
    "Save=",
    "Exit=Sortie",
]

EXPECTED_UPDATE_LOG_LINES = [
    "COPIED: Welcome",
    "COPIED: Hello",
    "MISSING: Save",
    "COPIED: Exit",
]

def read_lines(path):
    """Read a file and return its lines without trailing newlines."""
    with open(path, encoding="utf-8") as f:
        return [line.rstrip('\n') for line in f]

def test_new_fr_txt_exists():
    assert os.path.isfile(NEW_FR_TXT), (
        f"File {NEW_FR_TXT} is missing. "
        f"Expected the new French translation file to exist after completing the task."
    )

def test_update_log_exists():
    assert os.path.isfile(UPDATE_LOG), (
        f"File {UPDATE_LOG} is missing. "
        f"Expected the update log file to exist after completing the task."
    )

def test_new_fr_txt_content():
    assert os.path.isfile(NEW_FR_TXT), (
        f"File {NEW_FR_TXT} is missing. "
        f"Cannot check its content."
    )
    lines = read_lines(NEW_FR_TXT)
    assert lines == EXPECTED_NEW_FR_LINES, (
        f"{NEW_FR_TXT} does not have the expected content after the task.\n"
        f"Expected lines:\n{EXPECTED_NEW_FR_LINES}\nFound lines:\n{lines}\n"
        f"- Check for correct order, missing or extra lines, and exact format (no extra spaces or lines)."
    )
    assert len(lines) == 4, (
        f"{NEW_FR_TXT} should have exactly 4 lines (one for each phrase in source.txt), but found {len(lines)}."
    )

def test_update_log_content():
    assert os.path.isfile(UPDATE_LOG), (
        f"File {UPDATE_LOG} is missing. "
        f"Cannot check its content."
    )
    lines = read_lines(UPDATE_LOG)
    assert lines == EXPECTED_UPDATE_LOG_LINES, (
        f"{UPDATE_LOG} does not have the expected content after the task.\n"
        f"Expected lines:\n{EXPECTED_UPDATE_LOG_LINES}\nFound lines:\n{lines}\n"
        f"- Check for correct order, missing or extra lines, and exact format (no extra spaces or lines)."
    )
    assert len(lines) == 4, (
        f"{UPDATE_LOG} should have exactly 4 lines (one for each phrase in source.txt), but found {len(lines)}."
    )

def test_no_extra_files_created():
    """Ensure only the expected files exist in the localization directory after task completion."""
    expected_files = {"source.txt", "old_fr.txt", "new_fr.txt", "update.log"}
    actual_files = set(os.listdir(LOCALIZATION_DIR))
    extra_files = actual_files - expected_files
    missing_files = expected_files - actual_files
    assert not missing_files, (
        f"Missing expected files in {LOCALIZATION_DIR}: {missing_files}"
    )
    assert not extra_files, (
        f"Unexpected extra files present in {LOCALIZATION_DIR} after task: {extra_files}"
    )