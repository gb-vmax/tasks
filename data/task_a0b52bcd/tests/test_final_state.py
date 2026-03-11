# test_final_state.py

import hashlib
import os
import subprocess
import pytest

INCOMING_DIR = "/home/user/etl/incoming"
MANIFEST_PATH = "/home/user/etl/checksums.sha256"
CSV_FILES = ["customers.csv", "orders.csv", "products.csv"]

EXPECTED_CONTENTS = {
    "customers.csv": (
        "id,name,email\n"
        "1,Alice,alice@example.com\n"
        "2,Bob,bob@example.com\n"
        "3,Carol,carol@example.com\n"
    ),
    "orders.csv": (
        "order_id,customer_id,amount\n"
        "101,1,59.99\n"
        "102,2,120.00\n"
        "103,1,34.50\n"
    ),
    "products.csv": (
        "product_id,name,price\n"
        "1001,Widget,9.99\n"
        "1002,Gadget,24.99\n"
        "1003,Doohickey,4.49\n"
    ),
}


def compute_sha256(filepath):
    """Compute SHA-256 hash of a file, returning lowercase hex string."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def get_expected_hashes():
    """Compute expected hashes from the actual CSV files on disk."""
    hashes = {}
    for filename in CSV_FILES:
        filepath = os.path.join(INCOMING_DIR, filename)
        hashes[filename] = compute_sha256(filepath)
    return hashes


# ---------------------------------------------------------------------------
# Prerequisite checks (CSV files must exist with correct content)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filename", CSV_FILES)
def test_csv_file_exists(filename):
    filepath = os.path.join(INCOMING_DIR, filename)
    assert os.path.isfile(filepath), (
        f"Prerequisite CSV file {filepath} does not exist. "
        "The incoming CSV files must be present."
    )


@pytest.mark.parametrize("filename", CSV_FILES)
def test_csv_file_content(filename):
    filepath = os.path.join(INCOMING_DIR, filename)
    with open(filepath, "r") as f:
        actual = f.read()
    expected = EXPECTED_CONTENTS[filename]
    assert actual == expected, (
        f"Content of {filepath} does not match expected.\n"
        f"Expected:\n{expected!r}\n"
        f"Actual:\n{actual!r}"
    )


# ---------------------------------------------------------------------------
# Manifest existence and basic structure
# ---------------------------------------------------------------------------

def test_manifest_file_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Manifest file {MANIFEST_PATH} does not exist. "
        "The student must create the SHA-256 checksum manifest."
    )


def test_manifest_is_not_empty():
    assert os.path.getsize(MANIFEST_PATH) > 0, (
        f"Manifest file {MANIFEST_PATH} is empty. "
        "It must contain three checksum lines."
    )


def test_manifest_has_exactly_three_lines():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    # Strip trailing newline before splitting to avoid counting empty last line
    lines = content.rstrip("\n").splitlines()
    assert len(lines) == 3, (
        f"Manifest file {MANIFEST_PATH} must contain exactly 3 lines, "
        f"but found {len(lines)} line(s).\nContent:\n{content!r}"
    )


# ---------------------------------------------------------------------------
# Line format validation
# ---------------------------------------------------------------------------

def _read_manifest_lines():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    return content.rstrip("\n").splitlines()


@pytest.mark.parametrize("line_index", [0, 1, 2])
def test_manifest_line_format(line_index):
    lines = _read_manifest_lines()
    if line_index >= len(lines):
        pytest.skip(f"Line {line_index} does not exist (manifest has {len(lines)} lines).")
    line = lines[line_index]
    # Must have two-space separator: "<64-char hex>  <filename>"
    parts = line.split("  ", 1)
    assert len(parts) == 2, (
        f"Line {line_index + 1} of {MANIFEST_PATH} does not contain the two-space separator.\n"
        f"Line: {line!r}\n"
        "Expected format: '<64-char hex>  <filename>'"
    )
    hash_part, filename_part = parts
    assert len(hash_part) == 64, (
        f"Line {line_index + 1}: hash portion must be 64 hex characters, "
        f"got {len(hash_part)} characters: {hash_part!r}"
    )
    assert all(c in "0123456789abcdef" for c in hash_part), (
        f"Line {line_index + 1}: hash portion contains non-lowercase-hex characters: {hash_part!r}"
    )


# ---------------------------------------------------------------------------
# Alphabetical order by filename
# ---------------------------------------------------------------------------

def test_manifest_lines_sorted_alphabetically_by_filename():
    lines = _read_manifest_lines()
    filenames = []
    for line in lines:
        parts = line.split("  ", 1)
        if len(parts) == 2:
            filenames.append(parts[1])
    assert filenames == sorted(filenames), (
        f"Manifest lines are not sorted alphabetically by filename.\n"
        f"Found order: {filenames}\n"
        f"Expected order: {sorted(filenames)}"
    )


def test_manifest_filenames_are_correct_set():
    lines = _read_manifest_lines()
    filenames = []
    for line in lines:
        parts = line.split("  ", 1)
        if len(parts) == 2:
            filenames.append(parts[1])
    assert sorted(filenames) == sorted(CSV_FILES), (
        f"Manifest filenames do not match expected set.\n"
        f"Found: {sorted(filenames)}\n"
        f"Expected: {sorted(CSV_FILES)}"
    )


def test_manifest_filenames_are_bare_not_paths():
    lines = _read_manifest_lines()
    for line in lines:
        parts = line.split("  ", 1)
        if len(parts) == 2:
            filename_part = parts[1]
            assert "/" not in filename_part, (
                f"Manifest contains a path instead of a bare filename: {filename_part!r}\n"
                "Filenames must be bare (e.g., 'customers.csv'), not full or relative paths."
            )
            assert not filename_part.startswith("."), (
                f"Manifest filename starts with '.': {filename_part!r}\n"
                "Filenames must be bare (e.g., 'customers.csv'), not relative paths like './customers.csv'."
            )


# ---------------------------------------------------------------------------
# Correct hashes
# ---------------------------------------------------------------------------

def test_manifest_hashes_match_actual_files():
    expected_hashes = get_expected_hashes()
    lines = _read_manifest_lines()
    manifest_map = {}
    for line in lines:
        parts = line.split("  ", 1)
        if len(parts) == 2:
            manifest_map[parts[1]] = parts[0]

    for filename in CSV_FILES:
        expected_hash = expected_hashes[filename]
        actual_hash = manifest_map.get(filename)
        assert actual_hash is not None, (
            f"Filename '{filename}' not found in manifest {MANIFEST_PATH}."
        )
        assert actual_hash == expected_hash, (
            f"Hash mismatch for '{filename}' in {MANIFEST_PATH}.\n"
            f"Expected: {expected_hash}\n"
            f"Got:      {actual_hash}\n"
            "The hash does not match the actual file content."
        )


# ---------------------------------------------------------------------------
# sha256sum --check validation
# ---------------------------------------------------------------------------

def test_sha256sum_check_passes():
    """Run sha256sum --check from INCOMING_DIR and verify all files are OK."""
    result = subprocess.run(
        ["sha256sum", "--check", MANIFEST_PATH],
        capture_output=True,
        text=True,
        cwd=INCOMING_DIR,
    )
    assert result.returncode == 0, (
        f"sha256sum --check failed with return code {result.returncode}.\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}\n"
        "All three files must be reported as OK."
    )
    stdout = result.stdout.strip()
    for filename in CSV_FILES:
        assert f"{filename}: OK" in stdout, (
            f"sha256sum --check output does not contain '{filename}: OK'.\n"
            f"Full stdout:\n{stdout}"
        )


def test_sha256sum_check_no_failures():
    """Ensure sha256sum --check reports zero failures."""
    result = subprocess.run(
        ["sha256sum", "--check", MANIFEST_PATH],
        capture_output=True,
        text=True,
        cwd=INCOMING_DIR,
    )
    stdout = result.stdout + result.stderr
    assert "FAILED" not in stdout.upper() or "0 of" in stdout, (
        f"sha256sum --check reported failures.\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )


def test_manifest_ends_with_newline():
    """The manifest file should end with a newline (standard Unix text file)."""
    with open(MANIFEST_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"Manifest file {MANIFEST_PATH} does not end with a newline character. "
        "Standard sha256sum format requires each line to end with a newline."
    )


def test_manifest_uses_unix_line_endings():
    """The manifest should use Unix line endings (LF), not Windows (CRLF)."""
    with open(MANIFEST_PATH, "rb") as f:
        content = f.read()
    assert b"\r\n" not in content, (
        f"Manifest file {MANIFEST_PATH} contains Windows-style CRLF line endings. "
        "Use Unix LF line endings."
    )