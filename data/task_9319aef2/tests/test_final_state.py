# test_final_state.py

import os
import stat
import subprocess
import pytest

BASE = "/home/user/research/datasets"

EXPECTED_DIRS = [
    BASE,
    os.path.join(BASE, "raw"),
    os.path.join(BASE, "raw", "images"),
    os.path.join(BASE, "raw", "tabular"),
    os.path.join(BASE, "processed"),
    os.path.join(BASE, "processed", "train"),
    os.path.join(BASE, "processed", "val"),
    os.path.join(BASE, "processed", "test"),
    os.path.join(BASE, "archive"),
]

INDEX_PATH = os.path.join(BASE, "INDEX.txt")

EXPECTED_INDEX_LINES = [
    "DATASET REGISTRY",
    "================",
    "",
    "raw/images       - unprocessed image files",
    "raw/tabular      - unprocessed CSV and tabular data",
    "processed/train  - training split",
    "processed/val    - validation split",
    "processed/test   - test split",
    "archive          - deprecated or backed-up datasets",
]

ARCHIVE_PATH = os.path.join(BASE, "archive")


# ---------------------------------------------------------------------------
# Directory structure tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("dirpath", EXPECTED_DIRS)
def test_directory_exists(dirpath):
    assert os.path.exists(dirpath), (
        f"Expected directory does not exist: {dirpath}"
    )
    assert os.path.isdir(dirpath), (
        f"Path exists but is not a directory: {dirpath}"
    )


# ---------------------------------------------------------------------------
# INDEX.txt content tests
# ---------------------------------------------------------------------------

def test_index_file_exists():
    assert os.path.exists(INDEX_PATH), (
        f"INDEX.txt file does not exist at {INDEX_PATH}"
    )
    assert os.path.isfile(INDEX_PATH), (
        f"Path exists but is not a regular file: {INDEX_PATH}"
    )


def test_index_file_line_count():
    with open(INDEX_PATH, "r") as f:
        content = f.read()
    # Split keeping all lines; strip only the final trailing newline if present
    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 9, (
        f"INDEX.txt should have 9 lines (after stripping a single trailing newline), "
        f"but got {len(lines)} lines. Content:\n{content!r}"
    )


def test_index_file_line_content():
    with open(INDEX_PATH, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    for i, (actual, expected) in enumerate(zip(lines, EXPECTED_INDEX_LINES), start=1):
        assert actual == expected, (
            f"INDEX.txt line {i} mismatch.\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}"
        )


def test_index_file_blank_line_after_header():
    with open(INDEX_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    assert len(lines) >= 3, "INDEX.txt has fewer than 3 lines"
    assert lines[2] == "", (
        f"Line 3 of INDEX.txt should be blank, got: {lines[2]!r}"
    )


def test_index_file_spacing_alignment():
    """Verify the exact multi-space alignment used in each data line."""
    with open(INDEX_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    # Lines 4-9 (index 3-8)
    expected_data_lines = EXPECTED_INDEX_LINES[3:]
    actual_data_lines = lines[3:]

    for i, (actual, expected) in enumerate(zip(actual_data_lines, expected_data_lines), start=4):
        assert actual == expected, (
            f"INDEX.txt line {i} spacing/content mismatch.\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}"
        )


def test_index_file_exact_content():
    """Full byte-exact content check (allowing optional single trailing newline)."""
    expected_body = "\n".join(EXPECTED_INDEX_LINES)
    with open(INDEX_PATH, "r") as f:
        actual = f.read()
    # Accept with or without a single trailing newline
    actual_stripped = actual.rstrip("\n")
    assert actual_stripped == expected_body, (
        f"INDEX.txt content does not match exactly.\n"
        f"Expected (repr): {expected_body!r}\n"
        f"Actual   (repr): {actual_stripped!r}"
    )


# ---------------------------------------------------------------------------
# Archive directory permissions test
# ---------------------------------------------------------------------------

def test_archive_directory_exists():
    assert os.path.isdir(ARCHIVE_PATH), (
        f"archive directory does not exist: {ARCHIVE_PATH}"
    )


def test_archive_permissions_octal():
    st = os.stat(ARCHIVE_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert mode == 0o500, (
        f"archive/ permissions should be 0500 (dr-x------), "
        f"but got {oct(mode)}. "
        f"Run: chmod 500 {ARCHIVE_PATH}"
    )


def test_archive_owner_read():
    st = os.stat(ARCHIVE_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert mode & stat.S_IRUSR, (
        "archive/ should have owner read permission (r), but it does not."
    )


def test_archive_owner_no_write():
    st = os.stat(ARCHIVE_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert not (mode & stat.S_IWUSR), (
        "archive/ should NOT have owner write permission (w), but it does."
    )


def test_archive_owner_execute():
    st = os.stat(ARCHIVE_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert mode & stat.S_IXUSR, (
        "archive/ should have owner execute permission (x), but it does not."
    )


def test_archive_no_group_permissions():
    st = os.stat(ARCHIVE_PATH)
    mode = stat.S_IMODE(st.st_mode)
    group_bits = mode & (stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP)
    assert group_bits == 0, (
        f"archive/ should have no group permissions, but got group bits: {oct(group_bits)}"
    )


def test_archive_no_other_permissions():
    st = os.stat(ARCHIVE_PATH)
    mode = stat.S_IMODE(st.st_mode)
    other_bits = mode & (stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH)
    assert other_bits == 0, (
        f"archive/ should have no other permissions, but got other bits: {oct(other_bits)}"
    )


def test_archive_ls_ld_output():
    """Verify ls -ld output starts with dr-x------"""
    result = subprocess.run(
        ["ls", "-ld", ARCHIVE_PATH],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"ls -ld {ARCHIVE_PATH} failed with: {result.stderr}"
    )
    output = result.stdout.strip()
    assert output.startswith("dr-x------"), (
        f"ls -ld output should start with 'dr-x------', but got:\n{output}"
    )