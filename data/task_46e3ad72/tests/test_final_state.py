# test_final_state.py

"""
Pytest suite to validate the FINAL state of the OS/container after the backup task.

Validates:
- exp_42_backup_YYYYMMDD.tar.gz exists, is a valid archive, and contains the correct structure.
- exp_42_backup_YYYYMMDD.sha256 exists and matches the archive's SHA256 in standard format.
- /home/user/ml_experiments/exp_42/backup.log exists and matches the required format and values.
- No stray or temporary files remain.
"""

import os
import stat
import hashlib
import tarfile
import pytest
from datetime import date

HOME = "/home/user"
ML_DIR = os.path.join(HOME, "ml_experiments")
EXP_DIR = os.path.join(ML_DIR, "exp_42")
MODEL_DIR = os.path.join(EXP_DIR, "model")
LOGS_DIR = os.path.join(EXP_DIR, "logs")

# --- Helper functions ---

def get_today_str():
    """Return today's date as YYYYMMDD and YYYY-MM-DD tuple."""
    today = date.today()
    yyyymmdd = today.strftime("%Y%m%d")
    yyyy_mm_dd = today.strftime("%Y-%m-%d")
    return yyyymmdd, yyyy_mm_dd

def compute_sha256(path):
    """Compute SHA256 hash of the file at given path."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def get_expected_archive_members():
    """Return the expected internal paths of the archive, in sorted order."""
    return [
        "exp_42/model/model.h5",
        "exp_42/model/params.json",
        "exp_42/logs/train.log",
        "exp_42/metrics.csv",
    ]

def get_expected_backup_log(backup_date, archive_name, archive_size, sha256_hash):
    """Return the expected backup.log content as a string."""
    return (
        f"Backup Date: {backup_date}\n"
        f"Archive Name: {archive_name}\n"
        f"Archive Size: {archive_size} bytes\n"
        f"SHA256: {sha256_hash}\n"
        f"Backup Files:\n"
        f"- model/model.h5\n"
        f"- model/params.json\n"
        f"- logs/train.log\n"
        f"- metrics.csv\n"
    )

# --- Tests ---

def test_backup_archive_exists_and_valid():
    yyyymmdd, _ = get_today_str()
    archive_name = f"exp_42_backup_{yyyymmdd}.tar.gz"
    archive_path = os.path.join(ML_DIR, archive_name)

    # Check file exists and is a regular file
    assert os.path.isfile(archive_path), (
        f"Backup archive {archive_path} does not exist or is not a regular file."
    )

    # Check permissions: user owns and can write
    st = os.stat(archive_path)
    assert st.st_uid == os.getuid(), (
        f"Backup archive {archive_path} is not owned by the current user."
    )
    assert st.st_mode & stat.S_IWUSR, (
        f"Backup archive {archive_path} is not writable by the user."
    )

    # Check it's a valid tar.gz and contains the correct structure
    try:
        with tarfile.open(archive_path, "r:gz") as tar:
            names = sorted([m.name for m in tar.getmembers() if m.isfile()])
    except Exception as e:
        pytest.fail(f"Backup archive {archive_path} is not a valid tar.gz: {e}")

    expected_members = sorted(get_expected_archive_members())
    assert names == expected_members, (
        f"Backup archive {archive_path} does not contain the expected files.\n"
        f"Expected: {expected_members}\nFound: {names}"
    )

def test_sha256_file_exists_and_matches_archive():
    yyyymmdd, _ = get_today_str()
    archive_name = f"exp_42_backup_{yyyymmdd}.tar.gz"
    archive_path = os.path.join(ML_DIR, archive_name)
    sha256_path = os.path.join(ML_DIR, f"exp_42_backup_{yyyymmdd}.sha256")

    # Check file exists and is regular file
    assert os.path.isfile(sha256_path), (
        f"SHA256 file {sha256_path} does not exist."
    )

    # Check permissions: user owns and can write
    st = os.stat(sha256_path)
    assert st.st_uid == os.getuid(), (
        f"SHA256 file {sha256_path} is not owned by the current user."
    )
    assert st.st_mode & stat.S_IWUSR, (
        f"SHA256 file {sha256_path} is not writable by the user."
    )

    # Compute actual SHA256
    actual_hash = compute_sha256(archive_path)

    # Read and check content
    with open(sha256_path, "rt", encoding="utf-8") as f:
        content = f.read()
    # Must be exactly: SHA256_HASH  exp_42_backup_YYYYMMDD.tar.gz\n
    expected_line = f"{actual_hash}  {archive_name}\n"
    assert content == expected_line, (
        f"SHA256 file {sha256_path} content is incorrect.\n"
        f"Expected: {repr(expected_line)}\nFound: {repr(content)}"
    )

def test_backup_log_exists_and_correct():
    yyyymmdd, yyyy_mm_dd = get_today_str()
    archive_name = f"exp_42_backup_{yyyymmdd}.tar.gz"
    archive_path = os.path.join(ML_DIR, archive_name)
    log_path = os.path.join(EXP_DIR, "backup.log")

    # Check file exists and is regular file
    assert os.path.isfile(log_path), (
        f"Backup log {log_path} does not exist."
    )

    # Check permissions: user owns and can write
    st = os.stat(log_path)
    assert st.st_uid == os.getuid(), (
        f"Backup log {log_path} is not owned by the current user."
    )
    assert st.st_mode & stat.S_IWUSR, (
        f"Backup log {log_path} is not writable by the user."
    )

    # Gather dynamic values: archive_size, sha256
    archive_size = os.path.getsize(archive_path)
    sha256_hash = compute_sha256(archive_path)
    expected_log = get_expected_backup_log(
        backup_date=yyyy_mm_dd,
        archive_name=archive_name,
        archive_size=archive_size,
        sha256_hash=sha256_hash,
    )

    with open(log_path, "rt", encoding="utf-8") as f:
        content = f.read()
    assert content == expected_log, (
        f"Backup log {log_path} content does not match the expected format/content.\n"
        f"Expected:\n{repr(expected_log)}\nFound:\n{repr(content)}"
    )

def test_no_stray_temp_or_partial_files():
    """
    Ensure there are no stray .tar (uncompressed), .tmp, .partial, or other unexpected backup files.
    """
    yyyymmdd, _ = get_today_str()
    allowed_files = {
        f"exp_42_backup_{yyyymmdd}.tar.gz",
        f"exp_42_backup_{yyyymmdd}.sha256",
    }
    # Check for uncompressed .tar
    tar_uncompressed = f"exp_42_backup_{yyyymmdd}.tar"
    tar_uncompressed_path = os.path.join(ML_DIR, tar_uncompressed)
    assert not os.path.exists(tar_uncompressed_path), (
        f"Stray uncompressed tar file {tar_uncompressed_path} exists. "
        "Please clean up any intermediate files."
    )
    # Check for .tmp, .partial, or other backup-related stray files
    for filename in os.listdir(ML_DIR):
        if filename.startswith("exp_42_backup_"):
            if (
                filename.endswith(".tmp")
                or filename.endswith(".partial")
                or filename.endswith(".tar")
            ):
                pytest.fail(
                    f"Stray temporary or partial file {os.path.join(ML_DIR, filename)} exists. "
                    "No temp or intermediate files should remain after backup."
                )
            if filename not in allowed_files:
                pytest.fail(
                    f"Unexpected file {os.path.join(ML_DIR, filename)} exists. "
                    f"Only {sorted(allowed_files)} should exist in {ML_DIR} matching the backup prefix."
                )

def test_no_stray_files_in_exp_42():
    """
    Only the original experiment files and backup.log should exist inside /home/user/ml_experiments/exp_42.
    """
    allowed = {
        "model",
        "logs",
        "metrics.csv",
        "backup.log",
    }
    entries = set(os.listdir(EXP_DIR))
    extra = entries - allowed
    assert not extra, (
        f"Unexpected files or directories in {EXP_DIR}: {sorted(extra)}"
    )