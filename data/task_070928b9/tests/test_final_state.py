# test_final_state.py

import os
import stat
import pytest

HOME = "/home/user"
LOGS_DIR = os.path.join(HOME, "logs")
SCAN_FILE = os.path.join(LOGS_DIR, "world_writable_scan.txt")

# The expected files and their permissions (octal)
FILES_AND_MODES = {
    os.path.join(LOGS_DIR, "app.log"): 0o666,
    os.path.join(LOGS_DIR, "error.log"): 0o640,
    os.path.join(LOGS_DIR, "old", "debug.out"): 0o666,
    os.path.join(LOGS_DIR, "old", "archive.log"): 0o600,
    os.path.join(LOGS_DIR, "secure", ".keep"): 0o644,
}
# Expected directories
DIRS = [
    LOGS_DIR,
    os.path.join(LOGS_DIR, "old"),
    os.path.join(LOGS_DIR, "secure"),
]
# Expected contents of scan file (order matters)
EXPECTED_SCAN_CONTENTS = [
    os.path.join(LOGS_DIR, "app.log"),
    os.path.join(LOGS_DIR, "old", "debug.out"),
]


@pytest.mark.parametrize("dpath", DIRS)
def test_directories_still_exist(dpath):
    assert os.path.isdir(dpath), f"Required directory missing after scan: {dpath}"


@pytest.mark.parametrize("fpath,mode", FILES_AND_MODES.items())
def test_files_unchanged_and_have_permissions(fpath, mode):
    assert os.path.isfile(fpath), f"Required file missing after scan: {fpath}"
    st = os.stat(fpath)
    actual_mode = stat.S_IMODE(st.st_mode)
    assert actual_mode == mode, (
        f"File {fpath} permissions changed after scan: {oct(actual_mode)} (expected {oct(mode)})"
    )


def test_secure_dir_is_still_only_keep():
    secure_dir = os.path.join(LOGS_DIR, "secure")
    entries = os.listdir(secure_dir)
    assert set(entries) == {".keep"}, (
        f"{secure_dir} should contain only '.keep' after scan, found: {entries}"
    )


def test_logs_dir_contents_unchanged_except_scan_file():
    expected = {"app.log", "error.log", "old", "secure", "world_writable_scan.txt"}
    actual = set(os.listdir(LOGS_DIR))
    missing = expected - actual
    extra = actual - expected
    assert not missing, f"Missing in {LOGS_DIR} after scan: {missing}"
    assert not extra, f"Unexpected entries in {LOGS_DIR} after scan: {extra}"


def test_old_dir_contents_unchanged():
    old_dir = os.path.join(LOGS_DIR, "old")
    expected = {"debug.out", "archive.log"}
    actual = set(os.listdir(old_dir))
    missing = expected - actual
    extra = actual - expected
    assert not missing, f"Missing in {old_dir} after scan: {missing}"
    assert not extra, f"Unexpected entries in {old_dir} after scan: {extra}"


def test_scan_file_exists_and_is_regular_file():
    assert os.path.exists(SCAN_FILE), (
        f"Scan output file {SCAN_FILE} was not created."
    )
    assert os.path.isfile(SCAN_FILE), (
        f"Scan output file {SCAN_FILE} exists but is not a regular file."
    )


def test_scan_file_contents_exact():
    """
    Check that world_writable_scan.txt contains exactly the correct file paths,
    one per line, in the expected order, with no extra whitespace or lines.
    """
    with open(SCAN_FILE, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    assert lines == EXPECTED_SCAN_CONTENTS, (
        f"{SCAN_FILE} contents incorrect.\n"
        f"Expected lines:\n{EXPECTED_SCAN_CONTENTS}\n"
        f"Found lines:\n{lines}\n"
        f"Each line should be the absolute path of a world-writable regular file, "
        f"one per line, with no extra whitespace, blank lines, or explanations."
    )


def test_scan_file_lists_only_world_writable_regular_files():
    """
    Double-check that every path in the scan file is a world-writable regular file,
    and that no extra files are listed.
    """
    with open(SCAN_FILE, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    for path in lines:
        assert os.path.isabs(path), (
            f"Scan file entry is not an absolute path: {path}"
        )
        assert os.path.isfile(path), (
            f"Scan file entry is not a regular file: {path}"
        )
        st = os.stat(path)
        mode = stat.S_IMODE(st.st_mode)
        assert (mode & 0o002), (
            f"Scan file entry {path} is not world-writable (mode: {oct(mode)})"
        )

    # Also check that no world-writable regular files are missing from the scan
    all_found = set(lines)
    expected_set = set(EXPECTED_SCAN_CONTENTS)
    missing = expected_set - all_found
    extra = all_found - expected_set
    assert not missing, (
        f"Scan file is missing world-writable regular files: {missing}"
    )
    assert not extra, (
        f"Scan file contains unexpected extra paths: {extra}"
    )


def test_no_other_files_or_dirs_created():
    """
    Ensure no unexpected new files or directories have been created under /home/user/logs.
    """
    # Recursively collect all files and dirs under logs after scan
    expected_files = set(FILES_AND_MODES.keys()) | {SCAN_FILE}
    expected_dirs = set(DIRS)

    found_files = set()
    found_dirs = set()

    for dirpath, dirnames, filenames in os.walk(LOGS_DIR):
        found_dirs.add(dirpath)
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            found_files.add(fpath)

    extra_files = found_files - expected_files
    extra_dirs = found_dirs - expected_dirs

    assert not extra_files, (
        f"Unexpected new files found after scan: {sorted(extra_files)}"
    )
    assert not extra_dirs, (
        f"Unexpected new directories found after scan: {sorted(extra_dirs)}"
    )