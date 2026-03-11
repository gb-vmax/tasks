# test_final_state.py

import hashlib
import os
import re
import subprocess
import tarfile
import pytest

ARCHIVE_DIR = "/home/user/archive"
ARCHIVE_FILE = "/home/user/archive/Q3_audit.tar.gz"
CHECKSUM_FILE = "/home/user/archive/Q3_audit.tar.gz.sha256"

EXPECTED_TAR_ENTRIES = {
    "audit_logs/access.log",
    "audit_logs/auth.log",
    "audit_logs/error.log",
}


def test_archive_directory_exists():
    assert os.path.isdir(ARCHIVE_DIR), (
        f"Directory {ARCHIVE_DIR} does not exist. "
        "The archive directory must be created as part of the task."
    )


def test_archive_file_exists():
    assert os.path.isfile(ARCHIVE_FILE), (
        f"Archive file {ARCHIVE_FILE} does not exist. "
        "The task requires creating a gzip-compressed tar archive at this path."
    )


def test_checksum_file_exists():
    assert os.path.isfile(CHECKSUM_FILE), (
        f"Checksum file {CHECKSUM_FILE} does not exist. "
        "The task requires generating a SHA256 checksum file at this path."
    )


def test_archive_is_valid_gzip_tar():
    assert tarfile.is_tarfile(ARCHIVE_FILE), (
        f"{ARCHIVE_FILE} is not a valid tar file. "
        "The archive must be a valid gzip-compressed tar archive."
    )
    try:
        with tarfile.open(ARCHIVE_FILE, "r:gz") as tf:
            _ = tf.getmembers()
    except Exception as e:
        pytest.fail(
            f"{ARCHIVE_FILE} could not be opened as a gzip tar archive: {e}. "
            "Ensure the archive is properly gzip-compressed."
        )


def test_archive_contains_expected_entries():
    with tarfile.open(ARCHIVE_FILE, "r:gz") as tf:
        members = tf.getmembers()
    # Collect names, stripping trailing slashes for directories
    member_names = {m.name.rstrip("/") for m in members if m.isfile()}
    assert member_names == EXPECTED_TAR_ENTRIES, (
        f"Archive entries do not match expected entries.\n"
        f"Expected: {sorted(EXPECTED_TAR_ENTRIES)}\n"
        f"Found (files only): {sorted(member_names)}\n"
        "Ensure the archive contains exactly audit_logs/access.log, "
        "audit_logs/auth.log, and audit_logs/error.log."
    )


def test_archive_entries_have_correct_path_prefix():
    with tarfile.open(ARCHIVE_FILE, "r:gz") as tf:
        members = tf.getmembers()
    file_members = [m for m in members if m.isfile()]
    for member in file_members:
        assert member.name.startswith("audit_logs/"), (
            f"Archive entry '{member.name}' does not start with 'audit_logs/' prefix. "
            "All log files inside the archive must appear as audit_logs/<filename>."
        )


def test_archive_contains_no_extra_files():
    with tarfile.open(ARCHIVE_FILE, "r:gz") as tf:
        members = tf.getmembers()
    file_members = {m.name for m in members if m.isfile()}
    extra = file_members - EXPECTED_TAR_ENTRIES
    assert not extra, (
        f"Archive contains unexpected file entries: {extra}. "
        "Only the three .log files should be included."
    )


def test_archive_log_file_contents():
    """Verify the archived log files have the expected content."""
    expected_contents = {
        "audit_logs/access.log": (
            '192.168.1.10 - - [01/Jul/2024 08:12:03] "GET /dashboard HTTP/1.1" 200 4523\n'
            '192.168.1.22 - - [01/Jul/2024 08:14:55] "POST /login HTTP/1.1" 200 312\n'
            '192.168.1.45 - - [01/Jul/2024 08:19:30] "GET /reports HTTP/1.1" 403 89'
        ),
        "audit_logs/error.log": (
            "[01/Jul/2024 08:19:30] ERROR: Access denied for user 'jsmith' on /reports\n"
            "[02/Jul/2024 11:43:01] ERROR: Database connection timeout after 30s\n"
            "[03/Jul/2024 09:05:17] ERROR: Invalid session token from 10.0.0.8"
        ),
        "audit_logs/auth.log": (
            "Jul 01 08:14:55 appserver sshd[1042]: Accepted password for deploy from 192.168.1.22 port 54312 ssh2\n"
            "Jul 02 14:22:10 appserver sshd[1198]: Failed password for root from 10.0.0.99 port 41200 ssh2\n"
            "Jul 03 09:00:01 appserver sudo: jsmith : TTY=pts/0 ; PWD=/home/jsmith ; USER=root ; COMMAND=/bin/cat /etc/shadow"
        ),
    }
    with tarfile.open(ARCHIVE_FILE, "r:gz") as tf:
        for entry_name, expected in expected_contents.items():
            try:
                member = tf.getmember(entry_name)
            except KeyError:
                pytest.fail(
                    f"Entry '{entry_name}' not found in archive {ARCHIVE_FILE}."
                )
            f = tf.extractfile(member)
            assert f is not None, (
                f"Could not extract '{entry_name}' from archive."
            )
            actual_content = f.read().decode("utf-8").strip()
            assert actual_content == expected.strip(), (
                f"Content of '{entry_name}' in archive does not match expected.\n"
                f"Expected:\n{expected}\n\nActual:\n{actual_content}"
            )


def test_checksum_file_format():
    with open(CHECKSUM_FILE, "r") as f:
        content = f.read()

    lines = content.splitlines()
    assert len(lines) == 1, (
        f"Checksum file {CHECKSUM_FILE} must contain exactly one line, "
        f"but found {len(lines)} lines. Content:\n{content!r}"
    )

    line = lines[0]
    # Standard sha256sum format: <64 hex chars>  <filename>
    pattern = r"^([0-9a-f]{64})  (Q3_audit\.tar\.gz)$"
    match = re.match(pattern, line)
    assert match is not None, (
        f"Checksum file line does not match expected format.\n"
        f"Expected format: '<64-hex-chars>  Q3_audit.tar.gz'\n"
        f"Actual line: {line!r}\n"
        "Ensure there are exactly two spaces between the hash and filename, "
        "and that the filename is just 'Q3_audit.tar.gz' (not a full path)."
    )


def test_checksum_file_ends_with_newline():
    with open(CHECKSUM_FILE, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"Checksum file {CHECKSUM_FILE} must end with a newline character. "
        f"File content (raw): {content!r}"
    )


def test_checksum_hash_matches_archive():
    """Verify the hash in the checksum file matches the actual archive."""
    with open(CHECKSUM_FILE, "r") as f:
        line = f.read().strip()

    parts = line.split("  ", 1)
    assert len(parts) == 2, (
        f"Cannot parse checksum file line: {line!r}. "
        "Expected format: '<hash>  <filename>'"
    )
    recorded_hash = parts[0]

    # Compute actual SHA256 of the archive
    sha256 = hashlib.sha256()
    with open(ARCHIVE_FILE, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    actual_hash = sha256.hexdigest()

    assert recorded_hash == actual_hash, (
        f"SHA256 hash in checksum file does not match actual archive hash.\n"
        f"Hash in checksum file: {recorded_hash}\n"
        f"Actual archive hash:   {actual_hash}\n"
        "The checksum file must contain the SHA256 hash of the current archive."
    )


def test_sha256sum_verification_passes():
    """Run sha256sum -c from inside the archive directory and verify it passes."""
    result = subprocess.run(
        ["sha256sum", "-c", "Q3_audit.tar.gz.sha256"],
        cwd=ARCHIVE_DIR,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"sha256sum -c verification failed (exit code {result.returncode}).\n"
        f"stdout: {result.stdout!r}\n"
        f"stderr: {result.stderr!r}\n"
        "Running 'sha256sum -c Q3_audit.tar.gz.sha256' from /home/user/archive/ must exit 0."
    )
    assert "Q3_audit.tar.gz: OK" in result.stdout, (
        f"sha256sum output did not contain 'Q3_audit.tar.gz: OK'.\n"
        f"stdout: {result.stdout!r}\n"
        f"stderr: {result.stderr!r}"
    )


def test_only_expected_files_in_archive_dir():
    """The archive directory should contain exactly the two expected files."""
    entries = os.listdir(ARCHIVE_DIR)
    files = {e for e in entries if os.path.isfile(os.path.join(ARCHIVE_DIR, e))}
    expected_files = {"Q3_audit.tar.gz", "Q3_audit.tar.gz.sha256"}
    assert files == expected_files, (
        f"Unexpected files in {ARCHIVE_DIR}.\n"
        f"Expected: {sorted(expected_files)}\n"
        f"Found: {sorted(files)}\n"
        "The archive directory should contain exactly Q3_audit.tar.gz and Q3_audit.tar.gz.sha256."
    )


def test_checksum_filename_is_not_full_path():
    """Ensure the checksum file uses just the filename, not a full path."""
    with open(CHECKSUM_FILE, "r") as f:
        line = f.read().strip()

    parts = line.split("  ", 1)
    assert len(parts) == 2, (
        f"Cannot parse checksum file line: {line!r}"
    )
    filename_part = parts[1]
    assert filename_part == "Q3_audit.tar.gz", (
        f"Checksum file must reference just the filename 'Q3_audit.tar.gz', "
        f"not a full path. Found: {filename_part!r}"
    )
    assert "/" not in filename_part, (
        f"Checksum file filename part must not contain a path separator. "
        f"Found: {filename_part!r}"
    )