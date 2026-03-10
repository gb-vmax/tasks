# test_final_state.py

import os
import tarfile
import pytest

ARCHIVE_PATH = "/home/user/backups/client_alpha.tar.gz"
MANIFEST_PATH = "/home/user/backups/manifest.txt"
EXPECTED_FILE_COUNT = 4


def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive file {ARCHIVE_PATH} does not exist. "
        "The task requires creating a gzip-compressed tar archive at this path."
    )


def test_archive_is_valid_tar_gz():
    assert tarfile.is_tarfile(ARCHIVE_PATH), (
        f"{ARCHIVE_PATH} exists but is not a valid tar file. "
        "Ensure it was created with gzip compression (tar czf ...)."
    )
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            members = tf.getmembers()
    except Exception as e:
        pytest.fail(
            f"Failed to open {ARCHIVE_PATH} as a gzip-compressed tar archive: {e}"
        )


def test_archive_contains_exactly_four_regular_files():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        regular_files = [m for m in tf.getmembers() if m.isfile()]
    assert len(regular_files) == EXPECTED_FILE_COUNT, (
        f"Expected exactly {EXPECTED_FILE_COUNT} regular files in the archive, "
        f"but found {len(regular_files)}. "
        f"Files found: {[m.name for m in regular_files]}"
    )


def test_archive_contains_expected_files():
    expected_filenames = {"report.txt", "notes.md", "data.csv", "settings.cfg"}
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        regular_files = [m for m in tf.getmembers() if m.isfile()]
        actual_basenames = {os.path.basename(m.name) for m in regular_files}
    assert expected_filenames == actual_basenames, (
        f"Archive does not contain the expected files.\n"
        f"Expected basenames: {expected_filenames}\n"
        f"Actual basenames: {actual_basenames}"
    )


def test_archive_preserves_directory_structure():
    """Extracting should recreate a client_alpha directory."""
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        member_names = tf.getnames()
    # At least one entry should start with 'client_alpha'
    has_client_alpha = any(
        name == "client_alpha" or name.startswith("client_alpha/")
        for name in member_names
    )
    assert has_client_alpha, (
        f"Archive does not preserve the client_alpha directory structure. "
        f"Member names in archive: {member_names}. "
        "The archive should be created from the parent of client_alpha so that "
        "extraction recreates the client_alpha directory."
    )


def test_manifest_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Manifest file {MANIFEST_PATH} does not exist. "
        "The task requires creating a backup manifest at this path."
    )


def test_manifest_has_exactly_three_lines():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    # Strip a single trailing newline if present (acceptable), then split
    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 3, (
        f"Manifest file should have exactly 3 lines, but found {len(lines)}.\n"
        f"Content: {repr(content)}"
    )


def test_manifest_line1_archive():
    with open(MANIFEST_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 1, "Manifest file is empty or has fewer than 1 line."
    assert lines[0] == "archive: client_alpha.tar.gz", (
        f"Line 1 of manifest is incorrect.\n"
        f"Expected: 'archive: client_alpha.tar.gz'\n"
        f"Got:      {repr(lines[0])}"
    )


def test_manifest_line2_size_bytes():
    actual_size = os.stat(ARCHIVE_PATH).st_size
    with open(MANIFEST_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 2, "Manifest file has fewer than 2 lines."
    expected_line2 = f"size_bytes: {actual_size}"
    assert lines[1] == expected_line2, (
        f"Line 2 of manifest is incorrect.\n"
        f"Expected: {repr(expected_line2)}\n"
        f"Got:      {repr(lines[1])}\n"
        f"Actual archive size is {actual_size} bytes. "
        "Ensure the size_bytes value matches the exact byte count of the .tar.gz file."
    )


def test_manifest_line3_files():
    with open(MANIFEST_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 3, "Manifest file has fewer than 3 lines."
    assert lines[2] == f"files: {EXPECTED_FILE_COUNT}", (
        f"Line 3 of manifest is incorrect.\n"
        f"Expected: 'files: {EXPECTED_FILE_COUNT}'\n"
        f"Got:      {repr(lines[2])}"
    )


def test_manifest_no_extra_whitespace_or_blank_lines():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    # Should not have trailing spaces on any line
    lines = content.rstrip("\n").split("\n")
    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} of manifest has trailing whitespace: {repr(line)}"
        )
        assert line == line.lstrip() or line.startswith("archive") or line.startswith("size_bytes") or line.startswith("files"), (
            f"Line {i} of manifest has unexpected leading whitespace: {repr(line)}"
        )
    # Check no blank lines exist among the 3 lines
    for i, line in enumerate(lines, start=1):
        assert line != "", (
            f"Line {i} of manifest is blank. The manifest must have exactly 3 non-blank lines."
        )


def test_manifest_size_bytes_is_integer():
    with open(MANIFEST_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 2, "Manifest file has fewer than 2 lines."
    line2 = lines[1]
    assert line2.startswith("size_bytes: "), (
        f"Line 2 does not start with 'size_bytes: ': {repr(line2)}"
    )
    size_str = line2[len("size_bytes: "):]
    try:
        size_val = int(size_str)
    except ValueError:
        pytest.fail(
            f"The size_bytes value in the manifest is not a valid integer: {repr(size_str)}"
        )
    assert size_val > 0, (
        f"The size_bytes value should be a positive integer, got: {size_val}"
    )