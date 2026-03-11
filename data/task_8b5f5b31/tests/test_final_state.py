# test_final_state.py

import hashlib
import os
import re
import subprocess
import tarfile

import pytest

BACKUPS_DIR = "/home/user/infra/backups"
CONFIGS_DIR = "/home/user/infra/configs"
ARCHIVE_PATH = os.path.join(BACKUPS_DIR, "configs_backup.tar.gz")
CHECKSUM_PATH = os.path.join(BACKUPS_DIR, "configs_backup.tar.gz.sha256")


# ---------------------------------------------------------------------------
# Directory existence
# ---------------------------------------------------------------------------

def test_backups_directory_exists():
    assert os.path.isdir(BACKUPS_DIR), (
        f"The backups directory {BACKUPS_DIR!r} does not exist. "
        "It must be created as part of the task."
    )


def test_configs_directory_still_exists():
    """Original configs directory must not have been removed."""
    assert os.path.isdir(CONFIGS_DIR), (
        f"The configs directory {CONFIGS_DIR!r} no longer exists. "
        "It must not be removed by the task."
    )


# ---------------------------------------------------------------------------
# Archive file
# ---------------------------------------------------------------------------

def test_archive_file_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive file {ARCHIVE_PATH!r} does not exist. "
        "Step 1 of the task requires creating this gzip-compressed tar archive."
    )


def test_archive_is_valid_gzip_tar():
    assert tarfile.is_tarfile(ARCHIVE_PATH), (
        f"{ARCHIVE_PATH!r} exists but is not a valid tar file."
    )
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            members = tf.getnames()
    except Exception as exc:
        pytest.fail(
            f"Could not open {ARCHIVE_PATH!r} as a gzip-compressed tar archive: {exc}"
        )


def test_archive_contains_expected_files():
    expected_relative = {
        "configs/nginx.conf",
        "configs/db.env",
        "configs/haproxy.cfg",
    }
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = set(tf.getnames())

    for expected in expected_relative:
        assert expected in members, (
            f"Archive {ARCHIVE_PATH!r} does not contain {expected!r}. "
            f"Found members: {sorted(members)}. "
            "Paths inside the archive must start with 'configs/' (relative paths)."
        )


def test_archive_paths_are_relative_not_absolute():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getnames()

    absolute_members = [m for m in members if m.startswith("/")]
    assert not absolute_members, (
        f"Archive {ARCHIVE_PATH!r} contains absolute paths: {absolute_members}. "
        "All paths inside the archive must be relative (starting with 'configs/')."
    )


def test_archive_paths_start_with_configs():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getnames()

    # Filter out the top-level 'configs' directory entry itself
    file_members = [m for m in members if m != "configs" and not m.endswith("/")]
    bad_members = [m for m in file_members if not m.startswith("configs/")]
    assert not bad_members, (
        f"Archive contains paths that do not start with 'configs/': {bad_members}. "
        "The archive must preserve the directory structure with 'configs/' prefix."
    )


def test_archive_file_content_nginx_conf():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        try:
            member = tf.getmember("configs/nginx.conf")
            f = tf.extractfile(member)
            content = f.read().decode()
        except KeyError:
            pytest.fail("configs/nginx.conf not found inside the archive.")
    assert "worker_processes 4;" in content, (
        "configs/nginx.conf inside the archive does not contain expected content."
    )


def test_archive_file_content_db_env():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        try:
            member = tf.getmember("configs/db.env")
            f = tf.extractfile(member)
            content = f.read().decode()
        except KeyError:
            pytest.fail("configs/db.env not found inside the archive.")
    assert "DB_HOST=10.0.1.5" in content, (
        "configs/db.env inside the archive does not contain expected content."
    )


def test_archive_file_content_haproxy_cfg():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        try:
            member = tf.getmember("configs/haproxy.cfg")
            f = tf.extractfile(member)
            content = f.read().decode()
        except KeyError:
            pytest.fail("configs/haproxy.cfg not found inside the archive.")
    assert "timeout connect 5s" in content, (
        "configs/haproxy.cfg inside the archive does not contain expected content."
    )


# ---------------------------------------------------------------------------
# Checksum file
# ---------------------------------------------------------------------------

def test_checksum_file_exists():
    assert os.path.isfile(CHECKSUM_PATH), (
        f"Checksum file {CHECKSUM_PATH!r} does not exist. "
        "Step 2 of the task requires generating a SHA-256 checksum file."
    )


def test_checksum_file_has_exactly_one_line():
    with open(CHECKSUM_PATH, "r") as f:
        raw = f.read()

    lines = raw.splitlines()
    assert len(lines) == 1, (
        f"Checksum file {CHECKSUM_PATH!r} must contain exactly one line, "
        f"but it has {len(lines)} line(s). Content: {raw!r}"
    )


def test_checksum_file_ends_with_newline():
    with open(CHECKSUM_PATH, "rb") as f:
        raw = f.read()

    assert raw.endswith(b"\n"), (
        f"Checksum file {CHECKSUM_PATH!r} must end with a newline character, "
        f"but it does not. Raw bytes tail: {raw[-10:]!r}"
    )


def test_checksum_file_format():
    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()

    line = content.strip()
    # Expected format: <64-hex-chars>  configs_backup.tar.gz
    pattern = r"^([0-9a-f]{64})  configs_backup\.tar\.gz$"
    match = re.match(pattern, line)
    assert match, (
        f"Checksum file {CHECKSUM_PATH!r} does not match the expected format.\n"
        f"Expected format: '<64-char-hex>  configs_backup.tar.gz'\n"
        f"Actual content:  {content!r}\n"
        "Note: there must be TWO spaces between the hash and the filename, "
        "and the filename must be just 'configs_backup.tar.gz' (no directory prefix)."
    )


def test_checksum_hash_matches_archive():
    """Verify the SHA-256 hash in the checksum file matches the actual archive."""
    sha256 = hashlib.sha256()
    with open(ARCHIVE_PATH, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    expected_hash = sha256.hexdigest()

    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()

    line = content.strip()
    parts = line.split("  ", 1)
    assert len(parts) == 2, (
        f"Checksum file line could not be split into hash and filename: {line!r}"
    )
    actual_hash = parts[0]

    assert actual_hash == expected_hash, (
        f"SHA-256 hash in checksum file does not match the archive.\n"
        f"Hash in file:    {actual_hash}\n"
        f"Expected hash:   {expected_hash}\n"
        f"Archive:         {ARCHIVE_PATH!r}"
    )


def test_checksum_filename_portion_has_no_path():
    """The filename portion must be just the basename, not a full path."""
    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()

    line = content.strip()
    parts = line.split("  ", 1)
    assert len(parts) == 2, (
        f"Checksum file line cannot be parsed: {line!r}"
    )
    filename_portion = parts[1]

    assert filename_portion == "configs_backup.tar.gz", (
        f"The filename portion in the checksum file must be exactly "
        f"'configs_backup.tar.gz', but got: {filename_portion!r}. "
        "Do not include a directory prefix."
    )


# ---------------------------------------------------------------------------
# sha256sum --check verification (end-to-end)
# ---------------------------------------------------------------------------

def test_sha256sum_check_passes():
    """Run sha256sum --check from within the backups directory; must exit 0."""
    result = subprocess.run(
        ["sha256sum", "--check", "configs_backup.tar.gz.sha256"],
        cwd=BACKUPS_DIR,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"'sha256sum --check configs_backup.tar.gz.sha256' failed with exit code "
        f"{result.returncode}.\n"
        f"stdout: {result.stdout!r}\n"
        f"stderr: {result.stderr!r}\n"
        "The checksum file must be valid and match the archive."
    )


def test_sha256sum_check_output_contains_ok():
    """The sha256sum --check output must contain 'configs_backup.tar.gz: OK'."""
    result = subprocess.run(
        ["sha256sum", "--check", "configs_backup.tar.gz.sha256"],
        cwd=BACKUPS_DIR,
        capture_output=True,
        text=True,
    )
    assert "configs_backup.tar.gz: OK" in result.stdout, (
        f"Expected 'configs_backup.tar.gz: OK' in sha256sum output, "
        f"but got: {result.stdout!r}\n"
        f"stderr: {result.stderr!r}"
    )