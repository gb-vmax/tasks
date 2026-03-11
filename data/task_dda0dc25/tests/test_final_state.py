# test_final_state.py

import os
import re
import subprocess
import tarfile
import hashlib
import pytest

ARCHIVE_PATH = "/home/user/backups/configs_v2.tar.gz"
MANIFEST_PATH = "/home/user/backups/configs_v2.manifest"
BACKUP_LOG_PATH = "/home/user/backups/backup.log"
CONFIGS_DIR = "/home/user/configs"

EXPECTED_FIRST_LINE = (
    "configs_v1.tar.gz "
    "a3f1c2e4b5d6789012345678901234567890abcdef1234567890abcdef12345678 "
    "2048"
)

EXPECTED_CONFIG_FILES = {"app.conf", "database.conf", "logging.conf"}

EXPECTED_CONTENTS = {
    "configs/app.conf": "[server]\nhost=localhost\nport=8080\ndebug=false\n",
    "configs/database.conf": "[database]\nhost=db.internal\nport=5432\nname=appdb\nuser=admin\n",
    "configs/logging.conf": "[logging]\nlevel=INFO\nfile=/var/log/app.log\nmax_size=100MB\n",
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def get_actual_sha256(path):
    result = subprocess.run(
        ["sha256sum", path],
        capture_output=True, text=True, check=True
    )
    return result.stdout.split()[0]


def get_actual_size(path):
    result = subprocess.run(
        ["stat", "--format=%s", path],
        capture_output=True, text=True, check=True
    )
    return result.stdout.strip()


def get_tar_listing(path):
    result = subprocess.run(
        ["tar", "-tzvf", path],
        capture_output=True, text=True
    )
    return result


# ---------------------------------------------------------------------------
# Archive existence and validity
# ---------------------------------------------------------------------------

def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive {ARCHIVE_PATH} does not exist. "
        "The student must create the gzip-compressed tar archive."
    )


def test_archive_is_valid_gzip_tar():
    result = subprocess.run(
        ["tar", "-tzf", ARCHIVE_PATH],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"Archive {ARCHIVE_PATH} is not a valid gzip-compressed tar archive. "
        f"tar exit code: {result.returncode}\nstderr: {result.stderr}"
    )


def test_archive_member_paths_start_with_configs():
    result = subprocess.run(
        ["tar", "-tzf", ARCHIVE_PATH],
        capture_output=True, text=True, check=True
    )
    members = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    bad_members = [m for m in members if not m.startswith("configs/")]
    assert not bad_members, (
        f"Archive contains members whose paths do NOT start with 'configs/': {bad_members}\n"
        "All paths inside the archive must be relative and start with 'configs/'."
    )


def test_archive_contains_all_config_files():
    result = subprocess.run(
        ["tar", "-tzf", ARCHIVE_PATH],
        capture_output=True, text=True, check=True
    )
    members = {line.strip() for line in result.stdout.splitlines() if line.strip()}
    for fname in EXPECTED_CONFIG_FILES:
        expected_member = f"configs/{fname}"
        assert expected_member in members, (
            f"Archive does not contain expected member '{expected_member}'. "
            f"Archive members: {sorted(members)}"
        )


def test_archive_extracted_contents_correct():
    """Extract the archive to a temp dir and verify file contents."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        subprocess.run(
            ["tar", "-xzf", ARCHIVE_PATH, "-C", tmpdir],
            check=True
        )
        for member_path, expected_content in EXPECTED_CONTENTS.items():
            full_path = os.path.join(tmpdir, member_path)
            assert os.path.isfile(full_path), (
                f"After extraction, expected file '{full_path}' does not exist."
            )
            with open(full_path, "r") as f:
                actual = f.read()
            # Allow trailing newline flexibility
            assert actual.rstrip("\n") == expected_content.rstrip("\n"), (
                f"Extracted file '{member_path}' has wrong contents.\n"
                f"Expected:\n{expected_content!r}\n"
                f"Got:\n{actual!r}"
            )


# ---------------------------------------------------------------------------
# Manifest file
# ---------------------------------------------------------------------------

def test_manifest_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Manifest file {MANIFEST_PATH} does not exist. "
        "The student must generate it using 'tar -tzvf'."
    )


def test_manifest_is_non_empty():
    size = os.path.getsize(MANIFEST_PATH)
    assert size > 0, (
        f"Manifest file {MANIFEST_PATH} is empty. "
        "It should contain the output of 'tar -tzvf configs_v2.tar.gz'."
    )


def test_manifest_matches_tar_listing():
    tar_result = get_tar_listing(ARCHIVE_PATH)
    assert tar_result.returncode == 0, (
        f"'tar -tzvf {ARCHIVE_PATH}' failed with exit code {tar_result.returncode}.\n"
        f"stderr: {tar_result.stderr}"
    )
    expected_content = tar_result.stdout

    with open(MANIFEST_PATH, "r") as f:
        actual_content = f.read()

    assert actual_content == expected_content, (
        f"Manifest file {MANIFEST_PATH} does not match 'tar -tzvf' output.\n"
        f"Expected:\n{expected_content!r}\n"
        f"Got:\n{actual_content!r}"
    )


def test_manifest_paths_start_with_configs():
    with open(MANIFEST_PATH, "r") as f:
        lines = f.readlines()
    # Each line from tar -tzvf has fields; the last field is the path
    bad_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # tar -tzvf output: permissions links owner group size date time name
        parts = stripped.split()
        if parts:
            name = parts[-1]
            if not name.startswith("configs/"):
                bad_lines.append(line.rstrip())
    assert not bad_lines, (
        f"Manifest contains entries whose paths do NOT start with 'configs/':\n"
        + "\n".join(bad_lines)
    )


# ---------------------------------------------------------------------------
# Backup log
# ---------------------------------------------------------------------------

def test_backup_log_exists():
    assert os.path.isfile(BACKUP_LOG_PATH), (
        f"Backup log {BACKUP_LOG_PATH} does not exist."
    )


def test_backup_log_has_exactly_two_lines():
    with open(BACKUP_LOG_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    # Filter out trailing empty lines for counting non-empty lines
    non_empty = [l for l in lines if l.strip()]
    assert len(non_empty) == 2, (
        f"Expected exactly 2 non-empty lines in {BACKUP_LOG_PATH}, "
        f"found {len(non_empty)}.\nContent:\n{content!r}"
    )


def test_backup_log_first_line_unchanged():
    with open(BACKUP_LOG_PATH, "r") as f:
        lines = f.readlines()
    first_line = lines[0].rstrip("\n")
    assert first_line == EXPECTED_FIRST_LINE, (
        f"First line of {BACKUP_LOG_PATH} was modified (it should be unchanged).\n"
        f"Expected: {EXPECTED_FIRST_LINE!r}\n"
        f"Got:      {first_line!r}"
    )


def test_backup_log_second_line_format():
    with open(BACKUP_LOG_PATH, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 2, (
        f"Expected at least 2 lines in {BACKUP_LOG_PATH}, found {len(lines)}."
    )
    second_line = lines[1].rstrip("\n")
    pattern = r"^configs_v2\.tar\.gz [0-9a-f]{64} [0-9]+$"
    assert re.match(pattern, second_line), (
        f"Second line of {BACKUP_LOG_PATH} does not match expected format.\n"
        f"Expected pattern: {pattern}\n"
        f"Got: {second_line!r}"
    )


def test_backup_log_second_line_sha256_correct():
    actual_sha256 = get_actual_sha256(ARCHIVE_PATH)

    with open(BACKUP_LOG_PATH, "r") as f:
        lines = f.readlines()
    second_line = lines[1].rstrip("\n")
    parts = second_line.split()
    assert len(parts) == 3, (
        f"Second line of {BACKUP_LOG_PATH} should have exactly 3 space-separated fields.\n"
        f"Got: {second_line!r}"
    )
    logged_sha256 = parts[1]
    assert logged_sha256 == actual_sha256, (
        f"SHA256 in backup.log does not match the actual SHA256 of {ARCHIVE_PATH}.\n"
        f"Expected (actual): {actual_sha256}\n"
        f"Got (in log):      {logged_sha256}"
    )


def test_backup_log_second_line_size_correct():
    actual_size = get_actual_size(ARCHIVE_PATH)

    with open(BACKUP_LOG_PATH, "r") as f:
        lines = f.readlines()
    second_line = lines[1].rstrip("\n")
    parts = second_line.split()
    assert len(parts) == 3, (
        f"Second line of {BACKUP_LOG_PATH} should have exactly 3 space-separated fields.\n"
        f"Got: {second_line!r}"
    )
    logged_size = parts[2]
    assert logged_size == actual_size, (
        f"Size in backup.log does not match the actual size of {ARCHIVE_PATH}.\n"
        f"Expected (actual): {actual_size}\n"
        f"Got (in log):      {logged_size}"
    )


def test_backup_log_second_line_filename_correct():
    with open(BACKUP_LOG_PATH, "r") as f:
        lines = f.readlines()
    second_line = lines[1].rstrip("\n")
    parts = second_line.split()
    assert parts[0] == "configs_v2.tar.gz", (
        f"First field of second line in backup.log should be 'configs_v2.tar.gz'.\n"
        f"Got: {parts[0]!r}"
    )


def test_backup_log_second_line_ends_with_newline():
    with open(BACKUP_LOG_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    # The second line should exist and the content should end with newline
    assert content.endswith("\n"), (
        f"The backup log {BACKUP_LOG_PATH} should end with a newline character.\n"
        f"Last 10 chars: {content[-10:]!r}"
    )


def test_backup_log_no_trailing_spaces_on_second_line():
    with open(BACKUP_LOG_PATH, "r") as f:
        lines = f.readlines()
    second_line = lines[1].rstrip("\n")
    assert second_line == second_line.rstrip(), (
        f"Second line of {BACKUP_LOG_PATH} has trailing spaces.\n"
        f"Got: {second_line!r}"
    )