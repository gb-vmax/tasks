# test_final_state.py

"""
Pytest suite to verify the final state of the OS/container after the localization translation update task.

Validates:
- /home/user/localization/fr_translations.csv
- /home/user/localization/fr_translations_updated.csv
- /home/user/localization/update_log.txt

Ensures:
- Only these files are created/modified (no other files).
- File contents and formats exactly match the "truth" expected values.
"""

import os
import pytest

LOCALIZATION_DIR = "/home/user/localization"
TRANSLATIONS_CSV = os.path.join(LOCALIZATION_DIR, "translations.csv")
FR_UPDATES_CSV = os.path.join(LOCALIZATION_DIR, "fr_updates.csv")
FR_TRANSLATIONS_CSV = os.path.join(LOCALIZATION_DIR, "fr_translations.csv")
FR_TRANSLATIONS_UPDATED_CSV = os.path.join(LOCALIZATION_DIR, "fr_translations_updated.csv")
UPDATE_LOG_TXT = os.path.join(LOCALIZATION_DIR, "update_log.txt")

def file_contents(path):
    # Always normalize line endings to '\n' for comparison
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().replace('\r\n', '\n').replace('\r', '\n')

def assert_file_exists_and_contents(path, expected_content, fname):
    assert os.path.isfile(path), f"{fname} does not exist at expected path: {path}"
    actual_content = file_contents(path)
    # Remove trailing newlines for comparison (allow extra at end)
    actual = actual_content.strip('\n')
    expected = expected_content.strip('\n')
    assert actual == expected, (
        f"{fname} contents do not match expected.\n"
        f"Expected:\n{expected_content}\n"
        f"Actual:\n{actual_content}\n"
    )

def assert_file_exists_only(path, fname):
    assert os.path.isfile(path), f"{fname} does not exist at expected path: {path}"

def assert_directory_exists(path, dname):
    assert os.path.isdir(path), f"{dname} directory does not exist at expected path: {path}"

def get_all_files_in_dir(directory):
    # Returns all files (not dirs) in directory (non-recursive)
    return sorted([os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

@pytest.mark.final_state
def test_localization_final_files_and_contents():
    """Check that all and only the expected files exist after the task, with correct contents."""

    # 1. The /home/user/localization directory exists
    assert_directory_exists(LOCALIZATION_DIR, "localization")

    # 2. All and only the expected files exist in the directory
    expected_files = {
        "translations.csv",
        "fr_updates.csv",
        "fr_translations.csv",
        "fr_translations_updated.csv",
        "update_log.txt",
    }
    all_files = set(f for f in os.listdir(LOCALIZATION_DIR) if os.path.isfile(os.path.join(LOCALIZATION_DIR, f)))
    missing = expected_files - all_files
    extra = all_files - expected_files
    assert not missing, (
        f"Missing required output file(s): {', '.join(sorted(missing))} in {LOCALIZATION_DIR}"
    )
    assert not extra, (
        f"Unexpected file(s) present after the task: {', '.join(sorted(extra))} in {LOCALIZATION_DIR}"
    )

    # 3. fr_translations.csv content
    expected_fr_translations_csv = (
        "key,fr\n"
        "greeting,Bonjour\n"
        "farewell,Au revoir\n"
        "thanks,Merci\n"
        "apology,Désolé\n"
        "welcome,Bienvenue\n"
    )
    assert_file_exists_and_contents(
        FR_TRANSLATIONS_CSV, expected_fr_translations_csv, "fr_translations.csv"
    )

    # 4. fr_translations_updated.csv content
    expected_fr_translations_updated_csv = (
        "key,fr\n"
        "greeting,Salut\n"
        "farewell,Au revoir\n"
        "thanks,Merci beaucoup\n"
        "apology,Désolé\n"
        "welcome,Bienvenue\n"
    )
    assert_file_exists_and_contents(
        FR_TRANSLATIONS_UPDATED_CSV, expected_fr_translations_updated_csv, "fr_translations_updated.csv"
    )

    # 5. update_log.txt content
    expected_update_log_txt = (
        "key: greeting | old_fr: Bonjour | new_fr: Salut\n"
        "key: thanks | old_fr: Merci | new_fr: Merci beaucoup\n"
    )
    assert_file_exists_and_contents(
        UPDATE_LOG_TXT, expected_update_log_txt, "update_log.txt"
    )

@pytest.mark.final_state
def test_no_extra_files_created():
    """Ensure that no extra files are present in /home/user/localization after the task."""
    allowed = {
        "translations.csv",
        "fr_updates.csv",
        "fr_translations.csv",
        "fr_translations_updated.csv",
        "update_log.txt",
    }
    all_files = set(f for f in os.listdir(LOCALIZATION_DIR) if os.path.isfile(os.path.join(LOCALIZATION_DIR, f)))
    extra = all_files - allowed
    assert not extra, (
        f"Unexpected file(s) present after the task: {', '.join(sorted(extra))} in {LOCALIZATION_DIR}"
    )

@pytest.mark.final_state
def test_output_csv_format_and_no_quotes():
    """Verify that CSV files have no quoted fields, no extra spaces, and proper comma separation."""

    # Helper to check quotes and spaces
    def assert_csv_format(path, fname):
        with open(path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                line = line.rstrip('\r\n')
                # No quoted fields
                assert '"' not in line and "'" not in line, (
                    f"{fname} line {i} contains quoted fields: {line!r}"
                )
                # No extra spaces
                if ',' in line:
                    before, after = line.split(',', 1)
                    assert before == before.strip(), (
                        f"{fname} line {i}: key field has extra spaces: {repr(before)}"
                    )
                    assert after == after.strip(), (
                        f"{fname} line {i}: translation field has extra spaces: {repr(after)}"
                    )
    assert_csv_format(FR_TRANSLATIONS_CSV, "fr_translations.csv")
    assert_csv_format(FR_TRANSLATIONS_UPDATED_CSV, "fr_translations_updated.csv")

@pytest.mark.final_state
def test_update_log_matches_updated_keys_and_order():
    """Verify that update_log.txt lists only the updated keys, in the order of fr_translations.csv."""

    # Read fr_translations.csv and fr_translations_updated.csv into lists of (key, fr)
    def read_key_fr_csv(path):
        with open(path, 'r', encoding='utf-8') as f:
            lines = [line.rstrip('\r\n') for line in f]
        assert lines, f"{path} is empty"
        header = lines[0]
        assert header == "key,fr", f"{os.path.basename(path)} header is not 'key,fr': {header}"
        data = []
        for line in lines[1:]:
            # must split into exactly 2 columns
            cols = line.split(',', 1)
            assert len(cols) == 2, f"{os.path.basename(path)}: line does not have 2 columns: {line!r}"
            data.append(tuple(cols))
        return data

    orig_data = read_key_fr_csv(FR_TRANSLATIONS_CSV)
    updated_data = read_key_fr_csv(FR_TRANSLATIONS_UPDATED_CSV)

    assert len(orig_data) == len(updated_data), (
        "fr_translations.csv and fr_translations_updated.csv must have the same number of rows"
    )

    # Compute list of updated keys and their old/new values, preserving order
    updated = []
    for (key, old_fr), (_, new_fr) in zip(orig_data, updated_data):
        if old_fr != new_fr:
            updated.append((key, old_fr, new_fr))

    # Read update_log.txt lines
    log_lines = []
    with open(UPDATE_LOG_TXT, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\r\n')
            if line:
                log_lines.append(line)

    # Each updated key must be present in update_log.txt in order, with correct format
    assert len(log_lines) == len(updated), (
        f"update_log.txt should have {len(updated)} entries (one per updated key), but has {len(log_lines)}."
    )
    for i, (key, old_fr, new_fr) in enumerate(updated):
        expected_line = f"key: {key} | old_fr: {old_fr} | new_fr: {new_fr}"
        actual_line = log_lines[i]
        assert actual_line == expected_line, (
            f"update_log.txt line {i+1} does not match expected.\n"
            f"Expected: {expected_line}\n"
            f"Actual:   {actual_line}\n"
        )

    # No extra lines
    assert len(log_lines) == len(updated), (
        "update_log.txt contains extra lines not corresponding to updated keys."
    )