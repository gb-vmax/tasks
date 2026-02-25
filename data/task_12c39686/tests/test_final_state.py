# test_final_state.py

import os
import pytest
from datetime import datetime, timezone

HOME = "/home/user"
SRC_DIR = os.path.join(HOME, "app_profile", "results")
TGT_DIR = os.path.join(HOME, "remote_server", "backup", "results")
LOG_PATH = os.path.join(HOME, "sync_report.log")

# "Truth" constants
TRUTH_SOURCE_FILES = {
    "cpu.prof": {
        "size": 24576,
        "mtime": "2024-06-15T14:25:36Z",
    },
    "mem.prof": {
        "size": 16832,
        "mtime": "2024-06-15T14:21:00Z",
    },
}
TRUTH_TARGET_FILES = {
    "cpu.prof": {
        "size": 24576,
        "mtime": "2024-06-15T14:25:36Z",
    },
    "mem.prof": {
        "size": 16832,
        "mtime": "2024-06-15T14:21:00Z",
    },
}
TRUTH_LOG = (
    "[BEFORE]\n"
    "cpu.prof 24576 2024-06-15T14:25:36Z\n"
    "mem.prof 16832 2024-06-15T14:21:00Z\n"
    "\n"
    "[SYNC OPERATIONS]\n"
    "COPIED cpu.prof\n"
    "DELETED old.prof\n"
    "\n"
    "[AFTER]\n"
    "cpu.prof 24576 2024-06-15T14:25:36Z\n"
    "mem.prof 16832 2024-06-15T14:21:00Z\n"
)

def to_utc_iso8601(ts):
    # Accepts a POSIX timestamp, returns UTC ISO8601 'YYYY-MM-DDTHH:MM:SSZ'
    dt = datetime.utcfromtimestamp(ts).replace(tzinfo=timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

def file_info(path):
    st = os.stat(path)
    return {
        "size": st.st_size,
        "mtime": to_utc_iso8601(st.st_mtime)
    }

def list_profs(dirpath):
    # Returns sorted list of .prof filenames in dirpath
    return sorted(f for f in os.listdir(dirpath) if f.endswith('.prof'))

def profs_info(dirpath):
    # Returns dict: filename -> dict(size, mtime)
    profs = {}
    for fn in list_profs(dirpath):
        fp = os.path.join(dirpath, fn)
        profs[fn] = file_info(fp)
    return profs

def read_file_bytes(path):
    with open(path, "rb") as f:
        return f.read()

@pytest.mark.describe("Final state: profiling source directory is unchanged and correct")
def test_source_directory_unchanged():
    assert os.path.isdir(SRC_DIR), (
        f"Source directory {SRC_DIR} does not exist or is not a directory."
    )
    files = sorted(os.listdir(SRC_DIR))
    expected_files = sorted(TRUTH_SOURCE_FILES.keys())
    assert files == expected_files, (
        f"Source directory {SRC_DIR} must contain only {expected_files}, but contains {files}."
    )
    # Check each file
    for fname, truth in TRUTH_SOURCE_FILES.items():
        fpath = os.path.join(SRC_DIR, fname)
        assert os.path.isfile(fpath), f"{fpath} does not exist."
        info = file_info(fpath)
        assert info["size"] == truth["size"], (
            f"{fpath} must be {truth['size']} bytes, found {info['size']} bytes."
        )
        assert info["mtime"] == truth["mtime"], (
            f"{fpath} must have mtime {truth['mtime']}, found {info['mtime']}."
        )

@pytest.mark.describe("Final state: backup target directory matches source exactly")
def test_backup_directory_matches_source_exactly():
    assert os.path.isdir(TGT_DIR), (
        f"Backup target directory {TGT_DIR} does not exist or is not a directory."
    )
    files = sorted(os.listdir(TGT_DIR))
    expected_files = sorted(TRUTH_TARGET_FILES.keys())
    assert files == expected_files, (
        f"Backup target directory {TGT_DIR} must contain only {expected_files}, but contains {files}."
    )
    # Check each file: existence, size, mtime, and byte-for-byte content match source
    for fname, truth in TRUTH_TARGET_FILES.items():
        tgt_path = os.path.join(TGT_DIR, fname)
        src_path = os.path.join(SRC_DIR, fname)
        assert os.path.isfile(tgt_path), f"{tgt_path} does not exist."
        tinfo = file_info(tgt_path)
        assert tinfo["size"] == truth["size"], (
            f"{tgt_path} must be {truth['size']} bytes, found {tinfo['size']} bytes."
        )
        assert tinfo["mtime"] == truth["mtime"], (
            f"{tgt_path} must have mtime {truth['mtime']}, found {tinfo['mtime']}."
        )
        # Content byte-for-byte match
        src_bytes = read_file_bytes(src_path)
        tgt_bytes = read_file_bytes(tgt_path)
        assert src_bytes == tgt_bytes, (
            f"Contents of {tgt_path} do not match {src_path}."
        )

@pytest.mark.describe("Final state: extraneous files in backup are deleted")
def test_extraneous_prof_files_deleted_from_backup():
    # Only cpu.prof and mem.prof should exist; old.prof must be deleted
    files = set(list_profs(TGT_DIR))
    expected = set(TRUTH_TARGET_FILES.keys())
    extraneous = files - expected
    assert not extraneous, (
        f"Backup directory {TGT_DIR} contains extraneous .prof files: {sorted(extraneous)}. "
        "Only cpu.prof and mem.prof should remain."
    )
    # Also check that old.prof specifically is gone
    old_prof = os.path.join(TGT_DIR, "old.prof")
    assert not os.path.exists(old_prof), (
        f"{old_prof} should have been deleted from backup directory."
    )

@pytest.mark.describe("Final state: log file exists and is correct")
def test_sync_report_log_correct():
    assert os.path.isfile(LOG_PATH), (
        f"Log file {LOG_PATH} does not exist after sync."
    )
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == TRUTH_LOG, (
        f"Log file {LOG_PATH} content is incorrect.\n"
        f"Expected:\n{TRUTH_LOG!r}\n\nFound:\n{content!r}"
    )

@pytest.mark.describe("Final state: no extra files present in source or backup")
def test_no_unexpected_files():
    # Source: only cpu.prof and mem.prof
    src_files = set(os.listdir(SRC_DIR))
    expected_src = set(TRUTH_SOURCE_FILES.keys())
    unexpected_src = src_files - expected_src
    assert not unexpected_src, (
        f"Source directory {SRC_DIR} contains unexpected files: {sorted(unexpected_src)}"
    )
    # Backup: only cpu.prof and mem.prof
    tgt_files = set(os.listdir(TGT_DIR))
    expected_tgt = set(TRUTH_TARGET_FILES.keys())
    unexpected_tgt = tgt_files - expected_tgt
    assert not unexpected_tgt, (
        f"Backup target directory {TGT_DIR} contains unexpected files: {sorted(unexpected_tgt)}"
    )