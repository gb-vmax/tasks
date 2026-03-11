# test_final_state.py

import hashlib
import os
import re
import subprocess
import tarfile
import pytest

BACKUPS_DIR = "/home/user/backups"
ARCHIVE_PATH = "/home/user/backups/v2.4.0-release.tar.gz"
CHECKSUM_PATH = "/home/user/backups/v2.4.0-release.tar.gz.sha256"
ARCHIVE_FILENAME = "v2.4.0-release.tar.gz"

EXPECTED_TAR_MEMBERS = {
    "v2.4.0/",
    "v2.4.0/app-linux-amd64",
    "v2.4.0/app-linux-arm64",
    "v2.4.0/app-darwin-amd64",
    "v2.4.0/checksums.txt",
}

EXPECTED_FILE_CONTENTS = {
    "v2.4.0/app-linux-amd64": b"ELFBINARY_APP_AMD64_v2.4.0\n",
    "v2.4.0/app-linux-arm64": b"ELFBINARY_APP_ARM64_v2.4.0\n",
    "v2.4.0/app-darwin-amd64": b"MACHOBINARY_APP_AMD64_v2.4.0\n",
    "v2.4.0/checksums.txt": b"app-linux-amd64: abc123\napp-linux-arm64: def456\napp-darwin-amd64: ghi789\n",
}


def test_backups_directory_exists():
    assert os.path.isdir(BACKUPS_DIR), (
        f"Backups directory '{BACKUPS_DIR}' does not exist. "
        "The student should have created it with: mkdir -p /home/user/backups"
    )


def test_archive_file_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive file '{ARCHIVE_PATH}' does not exist. "
        "The student should have created a gzip-compressed tar archive at this path."
    )


def test_checksum_file_exists():
    assert os.path.isfile(CHECKSUM_PATH), (
        f"Checksum file '{CHECKSUM_PATH}' does not exist. "
        "The student should have generated a SHA-256 checksum file at this path."
    )


def test_archive_is_valid_gzip_tar():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    assert tarfile.is_tarfile(ARCHIVE_PATH), (
        f"'{ARCHIVE_PATH}' is not a valid tar archive."
    )
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            members = tf.getmembers()
    except Exception as e:
        pytest.fail(
            f"Failed to open '{ARCHIVE_PATH}' as a gzip-compressed tar archive: {e}"
        )
    assert len(members) > 0, (
        f"Archive '{ARCHIVE_PATH}' is empty — no members found."
    )


def test_archive_contains_expected_members():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        actual_names = set(tf.getnames())

    # Normalize: strip trailing slashes for directory entries for comparison
    normalized_actual = set()
    for name in actual_names:
        normalized_actual.add(name.rstrip("/") + ("/" if name.endswith("/") else ""))

    # Check that all expected members are present
    for expected in EXPECTED_TAR_MEMBERS:
        # Check with and without trailing slash for directories
        found = (expected in actual_names) or (expected.rstrip("/") in actual_names)
        assert found, (
            f"Expected member '{expected}' not found in archive '{ARCHIVE_PATH}'. "
            f"Actual members: {sorted(actual_names)}"
        )


def test_archive_contains_correct_file_contents():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        for member_name, expected_content in EXPECTED_FILE_CONTENTS.items():
            try:
                member = tf.getmember(member_name)
            except KeyError:
                pytest.fail(
                    f"Member '{member_name}' not found in archive '{ARCHIVE_PATH}'."
                )
            f = tf.extractfile(member)
            assert f is not None, (
                f"Could not extract file '{member_name}' from archive."
            )
            actual_content = f.read()
            assert actual_content == expected_content, (
                f"Content mismatch for '{member_name}' inside archive.\n"
                f"Expected: {expected_content!r}\n"
                f"Actual:   {actual_content!r}"
            )


def test_archive_no_extra_members():
    """Ensure archive contains exactly the expected members (no extras)."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        actual_names = set(tf.getnames())

    # Normalize expected: allow directory entries with or without trailing slash
    expected_without_slash = {name.rstrip("/") for name in EXPECTED_TAR_MEMBERS}
    actual_without_slash = {name.rstrip("/") for name in actual_names}

    extra = actual_without_slash - expected_without_slash
    missing = expected_without_slash - actual_without_slash

    assert not extra and not missing, (
        f"Archive member mismatch.\n"
        f"Extra members: {sorted(extra)}\n"
        f"Missing members: {sorted(missing)}"
    )


def test_checksum_file_format():
    assert os.path.isfile(CHECKSUM_PATH), f"Checksum file '{CHECKSUM_PATH}' does not exist."
    with open(CHECKSUM_PATH, "rb") as f:
        raw_content = f.read()

    # Must end with a newline
    assert raw_content.endswith(b"\n"), (
        f"Checksum file '{CHECKSUM_PATH}' does not end with a newline. "
        f"Raw content: {raw_content!r}"
    )

    text_content = raw_content.decode("utf-8")
    lines = text_content.splitlines()

    assert len(lines) == 1, (
        f"Checksum file '{CHECKSUM_PATH}' must contain exactly 1 line, "
        f"but found {len(lines)} lines. Content: {text_content!r}"
    )

    line = lines[0]
    pattern = r'^[a-f0-9]{64}  v2\.4\.0-release\.tar\.gz$'
    assert re.match(pattern, line), (
        f"Checksum file line does not match expected format.\n"
        f"Expected format: '<64-hex-chars>  v2.4.0-release.tar.gz'\n"
        f"Actual line:     {line!r}\n"
        "Note: there must be exactly TWO spaces between the hash and filename, "
        "and the filename must not include any directory path."
    )


def test_checksum_matches_archive():
    """Verify that the SHA-256 hash in the checksum file matches the actual archive."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    assert os.path.isfile(CHECKSUM_PATH), f"Checksum file '{CHECKSUM_PATH}' does not exist."

    # Compute actual SHA-256 of the archive
    sha256 = hashlib.sha256()
    with open(ARCHIVE_PATH, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    actual_hash = sha256.hexdigest()

    # Read hash from checksum file
    with open(CHECKSUM_PATH, "r") as f:
        content = f.read().strip()

    # Extract hash from checksum file (format: "<hash>  <filename>")
    parts = content.split("  ", 1)
    assert len(parts) == 2, (
        f"Checksum file content could not be parsed: {content!r}"
    )
    recorded_hash = parts[0]

    assert recorded_hash == actual_hash, (
        f"SHA-256 hash in checksum file does not match the actual archive.\n"
        f"Recorded hash: {recorded_hash}\n"
        f"Actual hash:   {actual_hash}\n"
        f"The checksum file may have been generated from a different version of the archive."
    )


def test_sha256sum_check_passes():
    """Run sha256sum --check from the backups directory and verify it passes."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    assert os.path.isfile(CHECKSUM_PATH), f"Checksum file '{CHECKSUM_PATH}' does not exist."

    result = subprocess.run(
        ["sha256sum", "--check", "v2.4.0-release.tar.gz.sha256"],
        cwd=BACKUPS_DIR,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, (
        f"'sha256sum --check' failed with exit code {result.returncode}.\n"
        f"stdout: {result.stdout!r}\n"
        f"stderr: {result.stderr!r}\n"
        "This means the checksum does not match the archive file."
    )

    assert "v2.4.0-release.tar.gz: OK" in result.stdout, (
        f"Expected 'v2.4.0-release.tar.gz: OK' in sha256sum output, but got:\n"
        f"stdout: {result.stdout!r}\n"
        f"stderr: {result.stderr!r}"
    )


def test_archive_file_is_nonempty():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    size = os.path.getsize(ARCHIVE_PATH)
    assert size > 0, (
        f"Archive file '{ARCHIVE_PATH}' is empty (0 bytes)."
    )


def test_checksum_file_is_nonempty():
    assert os.path.isfile(CHECKSUM_PATH), f"Checksum file '{CHECKSUM_PATH}' does not exist."
    size = os.path.getsize(CHECKSUM_PATH)
    assert size > 0, (
        f"Checksum file '{CHECKSUM_PATH}' is empty (0 bytes)."
    )


def test_tar_listing_via_subprocess():
    """Use tar -tzf to list archive members and verify expected entries are present."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."

    result = subprocess.run(
        ["tar", "-tzf", ARCHIVE_PATH],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, (
        f"'tar -tzf {ARCHIVE_PATH}' failed with exit code {result.returncode}.\n"
        f"stderr: {result.stderr!r}"
    )

    listed_entries = set(result.stdout.strip().splitlines())

    # Check for each expected file (allowing directory entry with or without slash)
    expected_files = [
        "v2.4.0/app-linux-amd64",
        "v2.4.0/app-linux-arm64",
        "v2.4.0/app-darwin-amd64",
        "v2.4.0/checksums.txt",
    ]
    for expected_file in expected_files:
        assert expected_file in listed_entries, (
            f"Expected file '{expected_file}' not found in tar listing.\n"
            f"Actual entries: {sorted(listed_entries)}"
        )

    # Check that v2.4.0 directory entry is present (with or without trailing slash)
    v240_dir_present = ("v2.4.0/" in listed_entries) or ("v2.4.0" in listed_entries)
    assert v240_dir_present, (
        f"Expected directory entry 'v2.4.0/' not found in tar listing.\n"
        f"Actual entries: {sorted(listed_entries)}"
    )