# test_final_state.py

"""
Pytest suite to validate the FINAL state of the OS/container for the restore Makefile task.

Checks:
- /home/user/restore_test/Makefile exists and contains a 'restore' target with correct logic.
- All .bak files remain unchanged.
- Corresponding .restored files exist with correct contents.
- No files are deleted or renamed.
- Running 'make restore' from /home/user/restore_test:
    - Produces correct .restored files.
    - Produces exactly one correctly-formatted console output line per restored file.
    - Output order is not enforced, but format is strict.
"""

import os
import stat
import subprocess
import re
import pytest

RESTORE_DIR = '/home/user/restore_test'
MAKEFILE_PATH = os.path.join(RESTORE_DIR, 'Makefile')

BAK_FILES = {
    'file1.bak': 'DATA1',
    'file2.bak': 'DATA2',
    'file3.bak': 'DATA3',
}
RESTORED_FILES = {
    'file1.restored': 'DATA1',
    'file2.restored': 'DATA2',
    'file3.restored': 'DATA3',
}

@pytest.mark.describe("Final state: Makefile exists and is correct")
def test_makefile_exists():
    assert os.path.isfile(MAKEFILE_PATH), (
        f"Makefile '{MAKEFILE_PATH}' does not exist. "
        "You must create this file in /home/user/restore_test."
    )

def test_makefile_has_restore_target():
    with open(MAKEFILE_PATH, 'r', encoding='utf-8') as f:
        makefile_content = f.read()

    # Check for a restore target at start of line (allow leading whitespace)
    restore_target_pattern = re.compile(r'^\s*restore\s*:', re.MULTILINE)
    assert restore_target_pattern.search(makefile_content), (
        "Makefile does not contain a 'restore' target. "
        "Ensure you have a line starting with 'restore:' (no typos, no variables)."
    )

    # Check that the restore target copies .bak to .restored with correct echo
    # We cannot fully parse Makefile, but check for .bak and .restored, and 'Restored:' string.
    assert '.bak' in makefile_content and '.restored' in makefile_content, (
        "Makefile does not reference both '.bak' and '.restored' file extensions. "
        "Ensure your recipe finds all '.bak' files and produces '.restored' files."
    )
    assert 'Restored:' in makefile_content, (
        "Makefile does not echo the required 'Restored:' string. "
        "Ensure your recipe prints the correct message for each file restored."
    )

@pytest.mark.describe("Final state: .bak files unchanged")
@pytest.mark.parametrize("filename,expected_content", list(BAK_FILES.items()))
def test_bak_files_unchanged(filename, expected_content):
    full_path = os.path.join(RESTORE_DIR, filename)
    assert os.path.isfile(full_path), (
        f"Original backup file '{full_path}' is missing after task completion. "
        "Do not delete, rename, or overwrite the .bak files."
    )
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == expected_content, (
        f"Backup file '{full_path}' was modified. "
        f"Expected contents: {repr(expected_content)}, found: {repr(content)}. "
        "Do not alter the original .bak files."
    )

@pytest.mark.describe("Final state: .restored files exist and correct")
@pytest.mark.parametrize("filename,expected_content", list(RESTORED_FILES.items()))
def test_restored_files_exist_and_correct(filename, expected_content):
    full_path = os.path.join(RESTORE_DIR, filename)
    assert os.path.isfile(full_path), (
        f"Restored file '{full_path}' does not exist. "
        "You must create this file as part of the restore process."
    )
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == expected_content, (
        f"Restored file '{full_path}' does not contain the correct data. "
        f"Expected: {repr(expected_content)}, found: {repr(content)}. "
        "Ensure the .restored file matches the original .bak file's contents."
    )

@pytest.mark.describe("Final state: No files are missing or renamed")
def test_no_files_deleted_or_renamed():
    # Gather expected files
    expected_files = set(['Makefile'] + list(BAK_FILES.keys()) + list(RESTORED_FILES.keys()))
    found_files = set(os.listdir(RESTORE_DIR))
    missing = expected_files - found_files
    unexpected = found_files - expected_files
    assert not missing, (
        f"The following required files are missing from '{RESTORE_DIR}': {sorted(missing)}. "
        "Do not delete or rename any required files."
    )
    # Allow extra files, but warn if there are unexpected ones (not fail)
    if unexpected:
        pytest.skip(f"Warning: Unexpected files found in '{RESTORE_DIR}': {sorted(unexpected)}. "
                    "This does not fail the test, but only the specified files are required.")

@pytest.mark.describe("Final state: Running 'make restore' produces correct output and files")
def test_make_restore_creates_restored_files_and_output(tmp_path, monkeypatch):
    """
    This test:
    - Copies all relevant files into a tmpdir.
    - Runs 'make restore' in that tmpdir.
    - Asserts that output is correct and all .restored files are created with correct contents.
    """
    import shutil

    # Copy all files to a temp directory for isolated test
    for fname in ['Makefile'] + list(BAK_FILES.keys()):
        src = os.path.join(RESTORE_DIR, fname)
        dst = os.path.join(tmp_path, fname)
        shutil.copy(src, dst)

    # Run 'make restore' in tmp_path
    proc = subprocess.run(
        ['make', 'restore'],
        cwd=str(tmp_path),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8'
    )
    # Show make errors for easier debugging
    assert proc.returncode == 0, (
        f"'make restore' failed with exit code {proc.returncode}.\n"
        f"STDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
    )

    # Check output: one line per .bak file, format strict
    output_lines = [line for line in proc.stdout.strip().split('\n') if line.strip()]
    expected_lines = {
        f"Restored: {bak} → {bak.replace('.bak', '.restored')}"
        for bak in BAK_FILES
    }
    got_lines = set(output_lines)
    missing_lines = expected_lines - got_lines
    extra_lines = got_lines - expected_lines

    assert not missing_lines, (
        "Missing required output lines from 'make restore':\n"
        + "\n".join(sorted(missing_lines))
        + "\nYour Makefile must echo exactly one line for each restored file, in the format:\n"
        "Restored: <original_file.bak> → <restored_file.restored>"
    )
    assert not extra_lines, (
        "Unexpected output lines from 'make restore':\n"
        + "\n".join(sorted(extra_lines))
        + "\nDo not print extra lines or deviate from the required format."
    )

    # Check .restored files created and contents correct
    for bak, expected_content in BAK_FILES.items():
        restored = bak.replace('.bak', '.restored')
        restored_path = tmp_path / restored
        assert restored_path.is_file(), (
            f"After 'make restore', '{restored_path}' does not exist. "
            f"Your Makefile must create this file for each .bak."
        )
        with open(restored_path, 'r', encoding='utf-8') as f:
            content = f.read()
        assert content == expected_content, (
            f"Restored file '{restored_path}' does not match original .bak contents. "
            f"Expected: {repr(expected_content)}, found: {repr(content)}."
        )