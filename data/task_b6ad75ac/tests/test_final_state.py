# test_final_state.py

import hashlib
import os
import re
import subprocess
import pytest

ARCHIVE_PATH = "/home/user/backups/configs_backup.tar.gz"
CHECKSUM_PATH = "/home/user/backups/configs_backup.tar.gz.sha256"
BACKUPS_DIR = "/home/user/backups"


def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive file {ARCHIVE_PATH} does not exist. "
        "The student must create a gzip-compressed tar archive at this path."
    )


def test_archive_is_valid_gzip_tar():
    result = subprocess.run(
        ["tar", "-tzf", ARCHIVE_PATH],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, (
        f"Archive {ARCHIVE_PATH} failed integrity check (tar -tzf returned non-zero exit code {result.returncode}). "
        f"stdout: {result.stdout!r}, stderr: {result.stderr!r}. "
        "The archive may be corrupt or not a valid gzip tar file."
    )


def test_archive_contains_config_files():
    result = subprocess.run(
        ["tar", "-tzf", ARCHIVE_PATH],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, (
        f"Cannot list archive contents; tar -tzf failed with exit code {result.returncode}."
    )
    listed_files = result.stdout
    # Check that at least the three config files are present somewhere in the archive listing
    for conf_file in ["app.conf", "db.conf", "nginx.conf"]:
        assert conf_file in listed_files, (
            f"Expected config file '{conf_file}' not found in archive listing.\n"
            f"Archive contents:\n{listed_files}"
        )


def test_checksum_file_exists():
    assert os.path.isfile(CHECKSUM_PATH), (
        f"Checksum file {CHECKSUM_PATH} does not exist. "
        "The student must generate a SHA-256 checksum file at this path."
    )


def test_checksum_file_has_exactly_one_line():
    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 1, (
        f"Checksum file {CHECKSUM_PATH} must contain exactly 1 line, "
        f"but found {len(lines)} lines. Content: {content!r}"
    )


def test_checksum_file_ends_with_newline():
    with open(CHECKSUM_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"Checksum file {CHECKSUM_PATH} must end with a newline character, "
        f"but it does not. Raw content: {content!r}"
    )


def test_checksum_file_format():
    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()
    line = content.strip()
    pattern = r"^[a-f0-9]{64}  /home/user/backups/configs_backup\.tar\.gz$"
    assert re.match(pattern, line), (
        f"Checksum file line does not match expected format.\n"
        f"Expected format: '<64-hex-chars>  /home/user/backups/configs_backup.tar.gz'\n"
        f"(Note: two spaces between hash and path, absolute path, lowercase hex)\n"
        f"Actual line: {line!r}"
    )


def test_checksum_hash_matches_archive():
    # Compute the actual SHA-256 of the archive
    sha256 = hashlib.sha256()
    with open(ARCHIVE_PATH, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    actual_hash = sha256.hexdigest()

    # Read the hash from the checksum file
    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()
    line = content.strip()
    recorded_hash = line.split()[0] if line else ""

    assert recorded_hash == actual_hash, (
        f"The hash in the checksum file does not match the actual SHA-256 of the archive.\n"
        f"Expected (computed from archive): {actual_hash}\n"
        f"Found in checksum file:           {recorded_hash}\n"
        "The checksum file may have been generated from a different version of the archive."
    )


def test_sha256sum_check_passes():
    result = subprocess.run(
        ["sha256sum", "--check", CHECKSUM_PATH],
        capture_output=True,
        text=True,
        cwd=BACKUPS_DIR
    )
    assert result.returncode == 0, (
        f"sha256sum --check {CHECKSUM_PATH} failed with exit code {result.returncode}.\n"
        f"stdout: {result.stdout!r}\n"
        f"stderr: {result.stderr!r}\n"
        "The checksum verification failed; the archive or checksum file may be incorrect."
    )


def test_sha256sum_check_output_contains_ok():
    result = subprocess.run(
        ["sha256sum", "--check", CHECKSUM_PATH],
        capture_output=True,
        text=True,
        cwd=BACKUPS_DIR
    )
    combined_output = result.stdout + result.stderr
    assert "OK" in combined_output, (
        f"sha256sum --check output does not contain 'OK'.\n"
        f"stdout: {result.stdout!r}\n"
        f"stderr: {result.stderr!r}\n"
        "Expected to see confirmation that the archive passed checksum verification."
    )