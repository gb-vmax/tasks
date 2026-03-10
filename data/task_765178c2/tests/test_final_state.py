# test_final_state.py

import hashlib
import os
import subprocess
import tarfile
import tempfile
import pytest

DEPLOY_DIR = "/home/user/deployments/app-v2.3.1"
BACKUPS_DIR = "/home/user/backups"
ARCHIVE_PATH = "/home/user/backups/app-v2.3.1.tar.gz"
CHECKSUM_PATH = "/home/user/backups/app-v2.3.1.tar.gz.sha256"

CONFIG_YML_CONTENT = """\
environment: production
port: 8080
log_level: info
database_url: postgres://db.internal:5432/appdb"""

RUN_SH_CONTENT = """\
#!/bin/bash
echo "Starting app-v2.3.1"
exec ./app --config config.yml"""

APP_CONTENT = "BINARY_PLACEHOLDER_v2.3.1"


# ---------------------------------------------------------------------------
# Archive existence and validity
# ---------------------------------------------------------------------------

def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive file does not exist: {ARCHIVE_PATH}"
    )


def test_archive_is_valid_gzip_tar():
    assert tarfile.is_tarfile(ARCHIVE_PATH), (
        f"File is not a valid tar archive: {ARCHIVE_PATH}"
    )
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            members = tf.getnames()
    except Exception as e:
        pytest.fail(f"Failed to open archive as gzip-compressed tar: {e}")


def test_archive_contains_expected_members():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getnames()

    # Normalise: strip leading ./ if present
    normalised = {m.lstrip("./") for m in members}

    expected_files = {
        "app-v2.3.1/config.yml",
        "app-v2.3.1/run.sh",
        "app-v2.3.1/app",
    }
    for expected in expected_files:
        assert expected in normalised, (
            f"Expected member '{expected}' not found in archive. "
            f"Archive members: {sorted(members)}"
        )


def test_archive_top_level_is_app_v2_3_1_directory():
    """Extracting the archive must recreate the app-v2.3.1 directory."""
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getnames()

    # Every member must start with app-v2.3.1 (or be app-v2.3.1 itself)
    for member in members:
        norm = member.lstrip("./")
        assert norm == "app-v2.3.1" or norm.startswith("app-v2.3.1/"), (
            f"Archive member '{member}' does not sit under 'app-v2.3.1/'. "
            "The archive must preserve the directory structure."
        )


def test_archive_extraction_recreates_directory():
    """Actually extract the archive and verify the directory structure."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            tf.extractall(tmpdir)

        extracted_dir = os.path.join(tmpdir, "app-v2.3.1")
        assert os.path.isdir(extracted_dir), (
            f"Extracting the archive did not recreate 'app-v2.3.1/' directory."
        )

        for filename in ("config.yml", "run.sh", "app"):
            fpath = os.path.join(extracted_dir, filename)
            assert os.path.isfile(fpath), (
                f"Expected file '{filename}' not found after extraction."
            )


def test_archive_extracted_config_yml_content():
    with tempfile.TemporaryDirectory() as tmpdir:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            tf.extractall(tmpdir)
        fpath = os.path.join(tmpdir, "app-v2.3.1", "config.yml")
        with open(fpath, "r") as f:
            content = f.read().strip()
    assert content == CONFIG_YML_CONTENT, (
        f"config.yml content inside archive is wrong.\n"
        f"Expected:\n{CONFIG_YML_CONTENT}\nGot:\n{content}"
    )


def test_archive_extracted_run_sh_content():
    with tempfile.TemporaryDirectory() as tmpdir:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            tf.extractall(tmpdir)
        fpath = os.path.join(tmpdir, "app-v2.3.1", "run.sh")
        with open(fpath, "r") as f:
            content = f.read().strip()
    assert content == RUN_SH_CONTENT, (
        f"run.sh content inside archive is wrong.\n"
        f"Expected:\n{RUN_SH_CONTENT}\nGot:\n{content}"
    )


def test_archive_extracted_app_content():
    with tempfile.TemporaryDirectory() as tmpdir:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            tf.extractall(tmpdir)
        fpath = os.path.join(tmpdir, "app-v2.3.1", "app")
        with open(fpath, "r") as f:
            content = f.read().strip()
    assert content == APP_CONTENT, (
        f"app binary content inside archive is wrong.\n"
        f"Expected:\n{APP_CONTENT}\nGot:\n{content}"
    )


# ---------------------------------------------------------------------------
# Checksum file existence and format
# ---------------------------------------------------------------------------

def test_checksum_file_exists():
    assert os.path.isfile(CHECKSUM_PATH), (
        f"Checksum file does not exist: {CHECKSUM_PATH}"
    )


def test_checksum_file_has_exactly_one_line():
    with open(CHECKSUM_PATH, "r") as f:
        raw = f.read()

    # Must end with a newline
    assert raw.endswith("\n"), (
        "Checksum file must end with a newline character."
    )

    lines = raw.splitlines()
    assert len(lines) == 1, (
        f"Checksum file must contain exactly 1 line, found {len(lines)} lines."
    )


def test_checksum_file_format():
    with open(CHECKSUM_PATH, "r") as f:
        line = f.read().rstrip("\n")

    # Expected format: "<64-hex>  app-v2.3.1.tar.gz"
    parts = line.split("  ", 1)
    assert len(parts) == 2, (
        f"Checksum line must be '<hash>  <filename>' (two spaces). Got: {line!r}"
    )

    hex_digest, filename = parts
    assert len(hex_digest) == 64, (
        f"SHA-256 hex digest must be 64 characters long, got {len(hex_digest)}: {hex_digest!r}"
    )
    assert all(c in "0123456789abcdef" for c in hex_digest), (
        f"SHA-256 hex digest must contain only lowercase hex characters. Got: {hex_digest!r}"
    )
    assert filename == "app-v2.3.1.tar.gz", (
        f"Filename in checksum file must be 'app-v2.3.1.tar.gz' (not a full path). Got: {filename!r}"
    )


def test_checksum_matches_archive():
    """The SHA-256 in the checksum file must match the actual archive."""
    sha256 = hashlib.sha256()
    with open(ARCHIVE_PATH, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    actual_digest = sha256.hexdigest()

    with open(CHECKSUM_PATH, "r") as f:
        line = f.read().rstrip("\n")

    recorded_digest = line.split("  ", 1)[0]
    assert recorded_digest == actual_digest, (
        f"Checksum mismatch!\n"
        f"  Recorded in file : {recorded_digest}\n"
        f"  Actual archive   : {actual_digest}"
    )


def test_sha256sum_verification_command():
    """sha256sum -c must exit 0 when run from the backups directory."""
    result = subprocess.run(
        ["sha256sum", "-c", "app-v2.3.1.tar.gz.sha256"],
        cwd=BACKUPS_DIR,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"'sha256sum -c app-v2.3.1.tar.gz.sha256' failed (exit {result.returncode}).\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )


# ---------------------------------------------------------------------------
# Original deployment directory must be unchanged
# ---------------------------------------------------------------------------

def test_original_deploy_dir_exists():
    assert os.path.isdir(DEPLOY_DIR), (
        f"Original deployment directory was removed or moved: {DEPLOY_DIR}"
    )


def test_original_deploy_dir_has_exactly_three_files():
    entries = sorted(os.listdir(DEPLOY_DIR))
    assert entries == ["app", "config.yml", "run.sh"], (
        f"Original deployment directory contents changed. Expected ['app', 'config.yml', 'run.sh'], "
        f"got: {entries}"
    )


def test_original_config_yml_unchanged():
    fpath = os.path.join(DEPLOY_DIR, "config.yml")
    with open(fpath, "r") as f:
        content = f.read().strip()
    assert content == CONFIG_YML_CONTENT, (
        f"Original config.yml was modified!\nExpected:\n{CONFIG_YML_CONTENT}\nGot:\n{content}"
    )


def test_original_run_sh_unchanged():
    fpath = os.path.join(DEPLOY_DIR, "run.sh")
    with open(fpath, "r") as f:
        content = f.read().strip()
    assert content == RUN_SH_CONTENT, (
        f"Original run.sh was modified!\nExpected:\n{RUN_SH_CONTENT}\nGot:\n{content}"
    )


def test_original_app_unchanged():
    fpath = os.path.join(DEPLOY_DIR, "app")
    with open(fpath, "r") as f:
        content = f.read().strip()
    assert content == APP_CONTENT, (
        f"Original app binary was modified!\nExpected:\n{APP_CONTENT}\nGot:\n{content}"
    )


# ---------------------------------------------------------------------------
# Backups directory sanity
# ---------------------------------------------------------------------------

def test_backups_directory_contains_exactly_two_files():
    entries = sorted(os.listdir(BACKUPS_DIR))
    assert entries == ["app-v2.3.1.tar.gz", "app-v2.3.1.tar.gz.sha256"], (
        f"Backups directory should contain exactly the archive and checksum file. "
        f"Found: {entries}"
    )