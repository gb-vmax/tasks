# test_final_state.py

import os
import stat
import tarfile
import pytest

HOME = "/home/user"
MICROSERVICES = os.path.join(HOME, "microservices")
AUTH_DIR = os.path.join(MICROSERVICES, "auth")
PAYMENT_DIR = os.path.join(MICROSERVICES, "payment")
AUTH_LOG = os.path.join(AUTH_DIR, "auth.log")
PAYMENT_LOG = os.path.join(PAYMENT_DIR, "payment.log")

BACKUP_TAR = os.path.join(HOME, "logs_backup.tar.gz")
RESTORE_DIR = os.path.join(HOME, "logs_restore")
RESTORE_AUTH_LOG = os.path.join(RESTORE_DIR, "auth.log")
RESTORE_PAYMENT_LOG = os.path.join(RESTORE_DIR, "payment.log")
RESTORE_REPORT = os.path.join(RESTORE_DIR, "restore_report.txt")

AUTH_LOG_CONTENT = "[2024-06-01 09:00:00] User login successful.\n"
PAYMENT_LOG_CONTENT = "[2024-06-01 09:05:22] Payment processed for order #1278.\n"
RESTORE_REPORT_CONTENT = "Restored Files:\nauth.log\npayment.log\n"

def _assert_user_rw_permissions(path, is_dir=False):
    st = os.stat(path)
    # Owner read/write
    mode = st.st_mode
    if is_dir:
        expected = stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
    else:
        expected = stat.S_IRUSR | stat.S_IWUSR
    assert (mode & expected) == expected, (
        f"{'Directory' if is_dir else 'File'} {path} does not have user read/write"
        f"{' and execute' if is_dir else ''} permissions."
    )

def test_logs_backup_tar_exists():
    assert os.path.isfile(BACKUP_TAR), (
        f"The backup archive {BACKUP_TAR} does not exist."
    )

def test_logs_backup_tar_contents_and_integrity():
    assert os.path.isfile(BACKUP_TAR), (
        f"The backup archive {BACKUP_TAR} does not exist."
    )
    with tarfile.open(BACKUP_TAR, "r:gz") as tf:
        names = tf.getnames()
        # Should be exactly these two files at the root
        expected_files = ["auth.log", "payment.log"]
        assert sorted(names) == sorted(expected_files), (
            f"{BACKUP_TAR} should contain only these files at its root: {expected_files}, "
            f"but contains: {names}"
        )
        # Check contents
        auth_member = tf.getmember("auth.log")
        payment_member = tf.getmember("payment.log")
        # Should not be directories
        assert auth_member.isfile(), "auth.log in archive is not a regular file."
        assert payment_member.isfile(), "payment.log in archive is not a regular file."
        with tf.extractfile(auth_member) as f:
            data = f.read().decode("utf-8")
            assert data == AUTH_LOG_CONTENT, (
                f"The content of auth.log in {BACKUP_TAR} is incorrect.\n"
                f"Expected:\n{AUTH_LOG_CONTENT!r}\nGot:\n{data!r}"
            )
        with tf.extractfile(payment_member) as f:
            data = f.read().decode("utf-8")
            assert data == PAYMENT_LOG_CONTENT, (
                f"The content of payment.log in {BACKUP_TAR} is incorrect.\n"
                f"Expected:\n{PAYMENT_LOG_CONTENT!r}\nGot:\n{data!r}"
            )

def test_logs_restore_directory_exists_and_permissions():
    assert os.path.isdir(RESTORE_DIR), (
        f"The directory {RESTORE_DIR} does not exist."
    )
    _assert_user_rw_permissions(RESTORE_DIR, is_dir=True)

@pytest.mark.parametrize(
    "path,expected_content,desc",
    [
        (RESTORE_AUTH_LOG, AUTH_LOG_CONTENT, "auth.log"),
        (RESTORE_PAYMENT_LOG, PAYMENT_LOG_CONTENT, "payment.log"),
    ]
)
def test_restored_log_files_exist_and_content(path, expected_content, desc):
    assert os.path.isfile(path), (
        f"The restored log file {path} is missing."
    )
    with open(path, "rt") as f:
        content = f.read()
    assert content == expected_content, (
        f"The contents of {path} are incorrect.\n"
        f"Expected:\n{expected_content!r}\nGot:\n{content!r}"
    )
    _assert_user_rw_permissions(path)

def test_restore_report_exists_and_content():
    assert os.path.isfile(RESTORE_REPORT), (
        f"The restore report {RESTORE_REPORT} does not exist."
    )
    with open(RESTORE_REPORT, "rt") as f:
        content = f.read()
    assert content == RESTORE_REPORT_CONTENT, (
        f"The contents of {RESTORE_REPORT} are incorrect.\n"
        f"Expected:\n{RESTORE_REPORT_CONTENT!r}\nGot:\n{content!r}"
    )
    _assert_user_rw_permissions(RESTORE_REPORT)

def test_no_extra_files_in_logs_restore():
    expected_files = {"auth.log", "payment.log", "restore_report.txt"}
    actual_files = set(os.listdir(RESTORE_DIR))
    assert actual_files == expected_files, (
        f"{RESTORE_DIR} contains unexpected files or is missing expected files.\n"
        f"Expected: {sorted(expected_files)}\nGot: {sorted(actual_files)}"
    )