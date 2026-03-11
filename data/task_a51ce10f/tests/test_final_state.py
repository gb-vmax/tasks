# test_final_state.py

import hashlib
import os
import pytest

# ── constants ─────────────────────────────────────────────────────────────────

ARCHIVE_DIR = "/home/user/backup/archive"
MANIFEST_PATH = "/home/user/backup/manifest.txt"

# Files that must be present in the archive
EXPECTED_ARCHIVED = {
    "access.log":  (b"a", 15000),
    "error.log":   (b"c", 12500),
    "queries.log": (b"d", 20000),
    "tasks.log":   (b"f", 11000),
}

# Files that must NOT be present in the archive
FORBIDDEN_ARCHIVED = {"debug.log", "slow.log", "archive.log"}

# Sorted order for manifest lines
SORTED_FILENAMES = sorted(EXPECTED_ARCHIVED.keys())

# ── helpers ───────────────────────────────────────────────────────────────────

def compute_expected_md5(char: bytes, count: int) -> str:
    return hashlib.md5(char * count).hexdigest()

def get_expected_hashes():
    return {
        fname: compute_expected_md5(char, size)
        for fname, (char, size) in EXPECTED_ARCHIVED.items()
    }

# ── archive directory tests ───────────────────────────────────────────────────

def test_archive_directory_exists():
    assert os.path.isdir(ARCHIVE_DIR), (
        f"Archive directory {ARCHIVE_DIR} does not exist. "
        "The student must create it and copy the qualifying .log files into it."
    )

def test_archive_contains_exactly_expected_files():
    actual_files = set(os.listdir(ARCHIVE_DIR))
    expected_files = set(EXPECTED_ARCHIVED.keys())
    missing = expected_files - actual_files
    extra = actual_files - expected_files
    assert not missing and not extra, (
        f"Archive directory {ARCHIVE_DIR} has wrong contents.\n"
        f"  Missing files: {sorted(missing)}\n"
        f"  Unexpected/extra files: {sorted(extra)}\n"
        f"  Expected exactly: {sorted(expected_files)}"
    )

@pytest.mark.parametrize("filename", sorted(EXPECTED_ARCHIVED.keys()))
def test_archived_file_exists(filename):
    path = os.path.join(ARCHIVE_DIR, filename)
    assert os.path.isfile(path), (
        f"Expected file {path} is missing from the archive directory."
    )

@pytest.mark.parametrize("filename", sorted(EXPECTED_ARCHIVED.keys()))
def test_archived_file_size(filename):
    char, expected_size = EXPECTED_ARCHIVED[filename]
    path = os.path.join(ARCHIVE_DIR, filename)
    actual_size = os.path.getsize(path)
    assert actual_size == expected_size, (
        f"Archived file {path}: expected {expected_size} bytes, "
        f"but found {actual_size} bytes."
    )

@pytest.mark.parametrize("filename", sorted(EXPECTED_ARCHIVED.keys()))
def test_archived_file_content(filename):
    char, size = EXPECTED_ARCHIVED[filename]
    path = os.path.join(ARCHIVE_DIR, filename)
    with open(path, "rb") as fh:
        data = fh.read()
    expected_data = char * size
    assert data == expected_data, (
        f"Archived file {path}: content does not match expected "
        f"{size} × {char!r}. File may have been corrupted or is the wrong file."
    )

@pytest.mark.parametrize("filename", sorted(FORBIDDEN_ARCHIVED))
def test_forbidden_file_not_in_archive(filename):
    path = os.path.join(ARCHIVE_DIR, filename)
    assert not os.path.exists(path), (
        f"File {path} must NOT be in the archive (it does not meet the "
        ">10 KB size requirement), but it was found there."
    )

# ── manifest file tests ───────────────────────────────────────────────────────

def test_manifest_file_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Manifest file {MANIFEST_PATH} does not exist. "
        "The student must generate it using find + xargs + md5sum."
    )

def test_manifest_no_trailing_newline():
    with open(MANIFEST_PATH, "rb") as fh:
        raw = fh.read()
    assert not raw.endswith(b"\n"), (
        f"Manifest file {MANIFEST_PATH} must NOT end with a trailing newline, "
        "but it does. The last line should be 'TOTAL FILES: 4' with no newline after it."
    )

def test_manifest_line_count():
    with open(MANIFEST_PATH, "r") as fh:
        content = fh.read()
    lines = content.split("\n")
    expected_count = len(EXPECTED_ARCHIVED) + 1  # 4 hash lines + 1 TOTAL line
    assert len(lines) == expected_count, (
        f"Manifest file {MANIFEST_PATH} has {len(lines)} lines, "
        f"but expected exactly {expected_count} lines "
        f"(4 checksum lines + 1 TOTAL FILES line).\n"
        f"Actual lines:\n" + "\n".join(f"  {i+1}: {repr(l)}" for i, l in enumerate(lines))
    )

def test_manifest_total_files_line():
    with open(MANIFEST_PATH, "r") as fh:
        content = fh.read()
    lines = content.split("\n")
    last_line = lines[-1]
    expected_last = f"TOTAL FILES: {len(EXPECTED_ARCHIVED)}"
    assert last_line == expected_last, (
        f"Last line of manifest must be exactly {expected_last!r}, "
        f"but found {last_line!r}."
    )

def test_manifest_checksum_lines_sorted_alphabetically():
    with open(MANIFEST_PATH, "r") as fh:
        content = fh.read()
    lines = content.split("\n")
    checksum_lines = lines[:-1]  # all but TOTAL FILES line
    filenames_in_order = []
    for line in checksum_lines:
        parts = line.split("  ", 1)
        assert len(parts) == 2, (
            f"Checksum line does not have the expected format '<hash>  <filename>': {line!r}"
        )
        filenames_in_order.append(parts[1])
    expected_order = sorted(EXPECTED_ARCHIVED.keys())
    assert filenames_in_order == expected_order, (
        f"Manifest checksum lines are not sorted alphabetically by filename.\n"
        f"  Expected order: {expected_order}\n"
        f"  Actual order:   {filenames_in_order}"
    )

@pytest.mark.parametrize("filename", SORTED_FILENAMES)
def test_manifest_checksum_line_format_and_hash(filename):
    expected_hashes = get_expected_hashes()
    expected_hash = expected_hashes[filename]

    with open(MANIFEST_PATH, "r") as fh:
        content = fh.read()
    lines = content.split("\n")
    checksum_lines = lines[:-1]  # exclude TOTAL FILES line

    # Find the line for this filename
    matching_lines = [l for l in checksum_lines if l.endswith("  " + filename)]
    assert len(matching_lines) == 1, (
        f"Expected exactly one manifest line for '{filename}', "
        f"but found {len(matching_lines)}.\n"
        f"Checksum lines:\n" + "\n".join(f"  {repr(l)}" for l in checksum_lines)
    )

    line = matching_lines[0]
    parts = line.split("  ", 1)
    assert len(parts) == 2, (
        f"Manifest line for '{filename}' does not match format '<hash>  <filename>': {line!r}"
    )
    actual_hash, actual_filename = parts

    # Validate hash is 32-char hex
    assert len(actual_hash) == 32 and all(c in "0123456789abcdef" for c in actual_hash), (
        f"Hash for '{filename}' is not a valid 32-character lowercase hex MD5 digest: {actual_hash!r}"
    )

    # Validate filename (no path prefix)
    assert actual_filename == filename, (
        f"Manifest line for '{filename}' has filename {actual_filename!r} "
        f"instead of bare filename {filename!r}. No directory path should be included."
    )

    # Validate hash value
    assert actual_hash == expected_hash, (
        f"MD5 hash for '{filename}' in manifest is wrong.\n"
        f"  Expected: {expected_hash}\n"
        f"  Actual:   {actual_hash}\n"
        f"  (Hash should be computed from the original file content.)"
    )

def test_manifest_no_path_prefix_in_any_line():
    with open(MANIFEST_PATH, "r") as fh:
        content = fh.read()
    lines = content.split("\n")
    checksum_lines = lines[:-1]
    for line in checksum_lines:
        parts = line.split("  ", 1)
        if len(parts) == 2:
            filename_part = parts[1]
            assert "/" not in filename_part, (
                f"Manifest line contains a path prefix in the filename part: {line!r}\n"
                "Only the bare filename (no directory) should appear."
            )

def test_manifest_hash_lines_use_two_spaces():
    """Each checksum line must use exactly two spaces between hash and filename."""
    with open(MANIFEST_PATH, "r") as fh:
        content = fh.read()
    lines = content.split("\n")
    checksum_lines = lines[:-1]
    for line in checksum_lines:
        # Should split into exactly 2 parts on "  " (two spaces)
        parts = line.split("  ", 1)
        assert len(parts) == 2, (
            f"Manifest line does not use two spaces as separator: {line!r}\n"
            "Format must be '<md5hash>  <filename>' with exactly two spaces."
        )
        hash_part = parts[0]
        # Ensure there's no extra space at start/end of hash
        assert hash_part == hash_part.strip(), (
            f"Hash part has unexpected whitespace: {hash_part!r} in line {line!r}"
        )

# ── integration: manifest matches archive ─────────────────────────────────────

def test_manifest_covers_all_archived_files():
    """Every file in the archive must have a corresponding line in the manifest."""
    with open(MANIFEST_PATH, "r") as fh:
        content = fh.read()
    lines = content.split("\n")
    checksum_lines = lines[:-1]

    manifest_filenames = set()
    for line in checksum_lines:
        parts = line.split("  ", 1)
        if len(parts) == 2:
            manifest_filenames.add(parts[1])

    archived_files = set(os.listdir(ARCHIVE_DIR))
    assert manifest_filenames == archived_files, (
        f"Manifest filenames do not match archive contents.\n"
        f"  In manifest but not archive: {manifest_filenames - archived_files}\n"
        f"  In archive but not manifest: {archived_files - manifest_filenames}"
    )