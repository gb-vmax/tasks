# test_final_state.py

import hashlib
import os
import subprocess
import tarfile
import pytest

BACKUPS_DIR = "/home/user/backups"
ARCHIVE_PATH = "/home/user/backups/audit_2024-02.tar.gz"
CHECKSUM_PATH = "/home/user/backups/audit_2024-02.tar.gz.sha256"
AUDIT_DIR = "/home/user/audit_logs/2024-02"

EXPECTED_ARCHIVE_MEMBERS = {
    "2024-02/auth.log",
    "2024-02/access.log",
    "2024-02/changes.log",
}


def compute_sha256(filepath):
    """Compute SHA256 hex digest of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_backups_dir_exists():
    assert os.path.isdir(BACKUPS_DIR), (
        f"Directory {BACKUPS_DIR} does not exist. "
        "The student must create the /home/user/backups/ directory."
    )


def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive file {ARCHIVE_PATH} does not exist. "
        "The student must create the gzip-compressed tar archive."
    )


def test_archive_is_valid_gzip_tar():
    assert tarfile.is_tarfile(ARCHIVE_PATH), (
        f"{ARCHIVE_PATH} is not a valid tar archive."
    )
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            members = tf.getnames()
    except Exception as e:
        pytest.fail(
            f"{ARCHIVE_PATH} could not be opened as a gzip-compressed tar archive: {e}"
        )


def test_archive_contains_expected_members():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = set(tf.getnames())

    # Filter out directory entries (e.g. "2024-02/") and keep only file entries
    file_members = {m for m in members if not m.endswith("/")}

    # Normalize: strip leading "./" if present
    normalized = {m.lstrip("./") for m in file_members}

    for expected in EXPECTED_ARCHIVE_MEMBERS:
        assert expected in normalized, (
            f"Expected member '{expected}' not found in archive {ARCHIVE_PATH}. "
            f"Archive contains: {sorted(members)}"
        )


def test_archive_paths_start_with_2024_02():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getnames()

    for member in members:
        # Allow the bare directory entry "2024-02" or "2024-02/"
        clean = member.lstrip("./")
        assert clean.startswith("2024-02"), (
            f"Archive member '{member}' does not start with '2024-02/'. "
            "All paths inside the archive must be relative and start with '2024-02/'."
        )


def test_archive_does_not_contain_absolute_paths():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getnames()

    for member in members:
        assert not member.startswith("/"), (
            f"Archive member '{member}' is an absolute path. "
            "All paths inside the archive must be relative."
        )


def test_checksum_file_exists():
    assert os.path.isfile(CHECKSUM_PATH), (
        f"Checksum file {CHECKSUM_PATH} does not exist. "
        "The student must generate a SHA256 checksum file."
    )


def test_checksum_file_format():
    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines(keepends=True)
    assert len(lines) == 1, (
        f"Checksum file {CHECKSUM_PATH} must contain exactly one line, "
        f"but it has {len(lines)} line(s). Content: {repr(content)}"
    )

    line = lines[0]
    assert line.endswith("\n"), (
        f"Checksum file {CHECKSUM_PATH} must end with a newline. "
        f"Got: {repr(line)}"
    )

    # Strip the trailing newline for parsing
    line_stripped = line.rstrip("\n")

    # Must be: <64-hex-chars>  <filename>  (two spaces)
    parts = line_stripped.split("  ", 1)
    assert len(parts) == 2, (
        f"Checksum file line must be '<hash>  <filename>' (two spaces). "
        f"Got: {repr(line_stripped)}"
    )

    hash_part, filename_part = parts

    assert len(hash_part) == 64, (
        f"Hash in checksum file must be 64 hex characters (SHA256), "
        f"but got {len(hash_part)} characters: {repr(hash_part)}"
    )

    assert all(c in "0123456789abcdef" for c in hash_part), (
        f"Hash in checksum file must be lowercase hex digits, "
        f"but got: {repr(hash_part)}"
    )

    assert filename_part == "audit_2024-02.tar.gz", (
        f"Filename in checksum file must be 'audit_2024-02.tar.gz' (bare filename, no path), "
        f"but got: {repr(filename_part)}"
    )


def test_checksum_matches_archive():
    actual_hash = compute_sha256(ARCHIVE_PATH)

    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()

    line = content.strip()
    parts = line.split("  ", 1)
    assert len(parts) == 2, (
        f"Cannot parse checksum file {CHECKSUM_PATH}: {repr(content)}"
    )
    recorded_hash = parts[0]

    assert recorded_hash == actual_hash, (
        f"Checksum mismatch for {ARCHIVE_PATH}.\n"
        f"Recorded in {CHECKSUM_PATH}: {recorded_hash}\n"
        f"Actual SHA256 of archive:    {actual_hash}\n"
        "The checksum file does not match the archive."
    )


def test_sha256sum_verification_passes():
    """Run 'sha256sum -c' from the backups directory to verify the checksum."""
    result = subprocess.run(
        ["sha256sum", "-c", "audit_2024-02.tar.gz.sha256"],
        cwd=BACKUPS_DIR,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"'sha256sum -c audit_2024-02.tar.gz.sha256' failed with return code {result.returncode}.\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}\n"
        "The checksum verification must pass."
    )


def test_archive_content_integrity():
    """Verify that the archive actually contains the expected log file contents."""
    expected_contents = {
        "2024-02/auth.log": (
            "2024-02-01 00:00:01 USER login success admin\n"
            "2024-02-01 00:05:33 USER login failure jsmith\n"
            "2024-02-01 00:07:12 USER login success jsmith\n"
            "2024-02-28 23:59:59 USER logout admin\n"
        ),
        "2024-02/access.log": (
            "2024-02-01 08:00:00 READ /reports/q4.pdf admin\n"
            "2024-02-01 08:15:22 WRITE /reports/q4.pdf admin\n"
            "2024-02-15 14:30:00 READ /reports/q4.pdf jsmith\n"
            "2024-02-28 17:45:00 DELETE /tmp/scratch.txt admin\n"
        ),
        "2024-02/changes.log": (
            "2024-02-03 09:00:00 CONFIG changed firewall rules by admin\n"
            "2024-02-10 11:22:45 PERMISSION granted jsmith access to /reports\n"
            "2024-02-20 16:00:00 USER created bwilson by admin\n"
        ),
    }

    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = {m.name: m for m in tf.getmembers() if m.isfile()}

        # Normalize keys
        normalized_members = {k.lstrip("./"): v for k, v in members.items()}

        for expected_path, expected_content in expected_contents.items():
            assert expected_path in normalized_members, (
                f"Expected file '{expected_path}' not found in archive. "
                f"Available files: {sorted(normalized_members.keys())}"
            )
            member = normalized_members[expected_path]
            extracted = tf.extractfile(member)
            assert extracted is not None, (
                f"Could not extract '{expected_path}' from archive."
            )
            actual_content = extracted.read().decode("utf-8")
            # Compare stripped to be lenient about trailing newlines
            assert actual_content.strip() == expected_content.strip(), (
                f"Content of '{expected_path}' in archive does not match expected.\n"
                f"Expected:\n{expected_content}\n\nGot:\n{actual_content}"
            )