# test_final_state.py

import os
import tarfile
import pytest

HOME = "/home/user"
LOGS_DIR = os.path.join(HOME, "logs")
DIAG_DIR = os.path.join(HOME, "diagnostics")

SYSLOG = "syslog.txt"
AUTHLOG = "auth.log"
KERNELLOG = "kernel.log"
EXPECTED_ARCHIVE_FILES = [SYSLOG, AUTHLOG, KERNELLOG]

ARCHIVE_PATH = os.path.join(DIAG_DIR, "diagnostics.tar.gz")
ARCHIVE_LIST_PATH = os.path.join(DIAG_DIR, "diagnostics_archive_contents.txt")


def test_diagnostics_archive_exists_and_is_file():
    """Check that diagnostics.tar.gz exists as a file."""
    assert os.path.exists(ARCHIVE_PATH), (
        f"Expected archive {ARCHIVE_PATH} is missing."
    )
    assert os.path.isfile(ARCHIVE_PATH), (
        f"{ARCHIVE_PATH} exists but is not a file."
    )


def test_archive_contains_only_expected_files_at_root():
    """
    Ensure that diagnostics.tar.gz contains only syslog.txt, auth.log,
    and kernel.log at the root level, in any order.
    """
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive file {ARCHIVE_PATH} does not exist."
    )
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tar:
        names = [member.name for member in tar.getmembers() if member.isfile()]
    # Check for exact contents (order doesn't matter)
    missing = set(EXPECTED_ARCHIVE_FILES) - set(names)
    unexpected = set(names) - set(EXPECTED_ARCHIVE_FILES)
    if missing or unexpected:
        msg = []
        if missing:
            msg.append(f"Missing files in archive: {', '.join(sorted(missing))}")
        if unexpected:
            msg.append(f"Unexpected files in archive: {', '.join(sorted(unexpected))}")
        msg.append(f"Archive contents: {sorted(names)}")
        pytest.fail('\n'.join(msg))
    # Check that all files are at root (no directories in the names)
    non_root = [n for n in names if "/" in n or n.startswith(".") or n.startswith("/")]
    assert not non_root, (
        f"The following files are not at the root of the archive: {non_root}"
    )


def test_archive_list_file_exists_and_content_exact():
    """
    Ensure that diagnostics_archive_contents.txt exists and contains the exact
    expected lines, no more, no less, and in the correct order.
    """
    assert os.path.exists(ARCHIVE_LIST_PATH), (
        f"Expected list file {ARCHIVE_LIST_PATH} is missing."
    )
    assert os.path.isfile(ARCHIVE_LIST_PATH), (
        f"{ARCHIVE_LIST_PATH} exists but is not a file."
    )
    with open(ARCHIVE_LIST_PATH, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    expected_lines = EXPECTED_ARCHIVE_FILES
    if lines != expected_lines:
        pytest.fail(
            f"{ARCHIVE_LIST_PATH} does not contain the expected contents.\n"
            f"Expected lines:\n{repr(expected_lines)}\n"
            f"Found lines:\n{repr(lines)}"
        )


def test_no_extra_files_in_diagnostics_directory():
    """
    Ensure that only diagnostics.tar.gz and diagnostics_archive_contents.txt
    are present in /home/user/diagnostics (along with any pre-existing files,
    if any, but no new files should have been created by the agent).
    """
    allowed_files = {"diagnostics.tar.gz", "diagnostics_archive_contents.txt"}
    actual_files = set(
        f for f in os.listdir(DIAG_DIR)
        if os.path.isfile(os.path.join(DIAG_DIR, f))
    )
    extra_files = actual_files - allowed_files
    missing_files = allowed_files - actual_files
    if extra_files:
        pytest.fail(
            f"Unexpected extra files found in {DIAG_DIR}: {sorted(extra_files)}"
        )
    if missing_files:
        pytest.fail(
            f"Expected files missing from {DIAG_DIR}: {sorted(missing_files)}"
        )


def test_archive_file_contents_match_originals():
    """
    Ensure that the files inside the archive have the same content as the originals
    in /home/user/logs.
    """
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tar:
        for fname in EXPECTED_ARCHIVE_FILES:
            try:
                member = tar.getmember(fname)
            except KeyError:
                pytest.fail(f"{fname} missing from archive {ARCHIVE_PATH}")
            with tar.extractfile(member) as f:
                archived_content = f.read()
            original_path = os.path.join(LOGS_DIR, fname)
            with open(original_path, "rb") as orig_f:
                original_content = orig_f.read()
            assert archived_content == original_content, (
                f"Content mismatch for {fname} in archive vs original file.\n"
                f"Archive content: {repr(archived_content)}\n"
                f"Original content: {repr(original_content)}"
            )