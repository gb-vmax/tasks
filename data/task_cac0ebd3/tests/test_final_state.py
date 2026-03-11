# test_final_state.py

import hashlib
import os
import tarfile
import pytest

BACKUP_DIR = "/home/user/backup"
ARCHIVE_PATH = "/home/user/backup/release_bundle.tar.gz"
CHECKSUM_PATH = "/home/user/backup/release_bundle.tar.gz.sha256"
MANIFEST_PATH = "/home/user/backup/MANIFEST.txt"

EXPECTED_ARCHIVE_MEMBERS = {
    "v1.0/app.bin": 1024,
    "v1.0/libcore.so": 2048,
    "v1.1/app.bin": 1536,
    "v1.2/app.bin": 2048,
    "v1.2/librender.so": 512,
}

EXPECTED_MANIFEST_LINES = [
    "v1.0/app.bin 1024",
    "v1.0/libcore.so 2048",
    "v1.1/app.bin 1536",
    "v1.2/app.bin 2048",
    "v1.2/librender.so 512",
]

EXPECTED_MANIFEST_CONTENT = "\n".join(EXPECTED_MANIFEST_LINES) + "\n"


# ── Backup directory ──────────────────────────────────────────────────────────

def test_backup_directory_exists():
    assert os.path.isdir(BACKUP_DIR), (
        f"Backup directory does not exist: {BACKUP_DIR}"
    )


# ── Archive file ──────────────────────────────────────────────────────────────

def test_archive_file_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive file does not exist: {ARCHIVE_PATH}"
    )


def test_archive_is_valid_tar_gz():
    assert tarfile.is_tarfile(ARCHIVE_PATH), (
        f"File is not a valid tar archive: {ARCHIVE_PATH}"
    )
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            tf.getmembers()
    except Exception as exc:
        pytest.fail(f"Cannot open archive as gzip-compressed tar: {exc}")


def test_archive_contains_exactly_expected_members():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = {m.name for m in tf.getmembers() if not m.isdir()}
    expected = set(EXPECTED_ARCHIVE_MEMBERS.keys())
    extra = members - expected
    missing = expected - members
    assert not extra, (
        f"Archive contains unexpected members: {extra}"
    )
    assert not missing, (
        f"Archive is missing expected members: {missing}"
    )


@pytest.mark.parametrize("member_path,expected_size", EXPECTED_ARCHIVE_MEMBERS.items())
def test_archive_member_size(member_path, expected_size):
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        try:
            info = tf.getmember(member_path)
        except KeyError:
            pytest.fail(f"Member '{member_path}' not found in archive")
    assert info.size == expected_size, (
        f"Archive member '{member_path}' has size {info.size}, expected {expected_size}"
    )


@pytest.mark.parametrize("member_path", EXPECTED_ARCHIVE_MEMBERS.keys())
def test_archive_member_path_is_relative(member_path):
    """Paths inside the archive must not start with '/' or contain the host prefix."""
    assert not member_path.startswith("/"), (
        f"Archive member path '{member_path}' must be relative (no leading '/')"
    )
    assert "home/user/artifacts" not in member_path, (
        f"Archive member path '{member_path}' must not contain the host directory prefix"
    )


# ── Checksum file ─────────────────────────────────────────────────────────────

def test_checksum_file_exists():
    assert os.path.isfile(CHECKSUM_PATH), (
        f"Checksum file does not exist: {CHECKSUM_PATH}"
    )


def test_checksum_file_has_exactly_one_line():
    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 1, (
        f"Checksum file must contain exactly one line, found {len(lines)}: {CHECKSUM_PATH}"
    )


def test_checksum_file_format():
    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()
    # Must end with a newline
    assert content.endswith("\n"), (
        f"Checksum file must end with a newline: {CHECKSUM_PATH!r}"
    )
    line = content.rstrip("\n")
    parts = line.split("  ", 1)
    assert len(parts) == 2, (
        f"Checksum line must be '<hash>  <filename>' (two spaces), got: {line!r}"
    )
    hex_digest, filename = parts
    assert len(hex_digest) == 64, (
        f"Hash must be 64 hex characters, got {len(hex_digest)}: {hex_digest!r}"
    )
    assert all(c in "0123456789abcdef" for c in hex_digest), (
        f"Hash contains non-hex characters: {hex_digest!r}"
    )
    assert filename == "release_bundle.tar.gz", (
        f"Filename in checksum must be bare 'release_bundle.tar.gz', got: {filename!r}"
    )


def test_checksum_matches_archive():
    # Compute actual SHA256 of the archive
    sha256 = hashlib.sha256()
    with open(ARCHIVE_PATH, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    actual_digest = sha256.hexdigest()

    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()
    line = content.strip()
    recorded_digest = line.split("  ", 1)[0]

    assert recorded_digest == actual_digest, (
        f"Checksum mismatch: checksum file records {recorded_digest!r} "
        f"but actual SHA256 of archive is {actual_digest!r}"
    )


# ── Manifest file ─────────────────────────────────────────────────────────────

def test_manifest_file_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Manifest file does not exist: {MANIFEST_PATH}"
    )


def test_manifest_exact_content():
    with open(MANIFEST_PATH, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_MANIFEST_CONTENT, (
        f"Manifest content does not match.\n"
        f"Expected:\n{EXPECTED_MANIFEST_CONTENT!r}\n"
        f"Got:\n{actual!r}"
    )


def test_manifest_ends_with_newline():
    with open(MANIFEST_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"Manifest file must end with a newline: {MANIFEST_PATH}"
    )


def test_manifest_no_blank_lines():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    blank = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank, (
        f"Manifest contains blank lines at line numbers: {blank}"
    )


def test_manifest_no_trailing_spaces():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    bad = [i + 1 for i, line in enumerate(lines) if line != line.rstrip(" ")]
    assert not bad, (
        f"Manifest has trailing spaces on lines: {bad}"
    )


def test_manifest_sorted_alphabetically():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    lines = [l for l in content.splitlines() if l.strip()]
    assert lines == sorted(lines), (
        f"Manifest lines are not sorted alphabetically.\nGot:\n" +
        "\n".join(lines)
    )


def test_manifest_line_count():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    lines = [l for l in content.splitlines() if l.strip()]
    assert len(lines) == len(EXPECTED_ARCHIVE_MEMBERS), (
        f"Manifest must have {len(EXPECTED_ARCHIVE_MEMBERS)} lines, found {len(lines)}"
    )


@pytest.mark.parametrize("expected_line", EXPECTED_MANIFEST_LINES)
def test_manifest_contains_expected_line(expected_line):
    with open(MANIFEST_PATH, "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines()]
    assert expected_line in lines, (
        f"Manifest is missing expected line: {expected_line!r}\n"
        f"Actual lines: {lines}"
    )