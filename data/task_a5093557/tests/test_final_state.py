# test_final_state.py

import os
import stat
import pytest

BACKUP_DIR = "/home/user/backup_verification"
VENV_DIR = os.path.join(BACKUP_DIR, "venv")
CHECK_SCRIPT = os.path.join(BACKUP_DIR, "check_backup.py")
BACKUP_FILE = os.path.join(BACKUP_DIR, "backup.tar.gz")
VERIFY_LOG = os.path.join(BACKUP_DIR, "verify.log")

@pytest.mark.describe("Backup Verification Final State")
class TestBackupVerificationFinalState:

    def test_backup_verification_directory_exists(self):
        assert os.path.isdir(BACKUP_DIR), (
            f"Required directory '{BACKUP_DIR}' does not exist. "
            "Please ensure the backup_verification directory remains present after task completion."
        )

    def test_check_backup_script_exists(self):
        assert os.path.isfile(CHECK_SCRIPT), (
            f"Required script '{CHECK_SCRIPT}' does not exist. "
            "check_backup.py must still be present in /home/user/backup_verification."
        )

    def test_backup_tar_gz_exists(self):
        assert os.path.isfile(BACKUP_FILE), (
            f"Required backup file '{BACKUP_FILE}' does not exist. "
            "backup.tar.gz must still be present in /home/user/backup_verification."
        )

    def test_venv_directory_exists(self):
        assert os.path.isdir(VENV_DIR), (
            f"Virtual environment directory '{VENV_DIR}' does not exist. "
            "The venv directory must remain after task completion."
        )

    def test_venv_structure(self):
        """
        Checks for key files/folders in a standard Python venv.
        """
        expected_entries = [
            "bin",      # Unix venvs have 'bin'
            "lib",      # Should have 'lib'
            "pyvenv.cfg" # Standard venv config file
        ]
        missing = []
        for entry in expected_entries:
            path = os.path.join(VENV_DIR, entry)
            if entry == "pyvenv.cfg":
                if not os.path.isfile(path):
                    missing.append(f"file {path}")
            else:
                if not os.path.isdir(path):
                    missing.append(f"directory {path}")
        assert not missing, (
            "The virtual environment directory does not have the expected structure. "
            "Missing: " + ", ".join(missing)
        )

    def test_venv_bin_python_exists_and_executable(self):
        bin_python = os.path.join(VENV_DIR, "bin", "python")
        assert os.path.isfile(bin_python), (
            f"The virtual environment is missing its Python executable at '{bin_python}'. "
            "Please ensure you have created the venv using the standard 'venv' module."
        )
        st = os.stat(bin_python)
        assert bool(st.st_mode & stat.S_IXUSR), (
            f"The Python executable at '{bin_python}' is not marked as executable."
        )

    def test_verify_log_exists(self):
        assert os.path.isfile(VERIFY_LOG), (
            f"The log file '{VERIFY_LOG}' does not exist. "
            "verify.log must remain after running the backup verification."
        )

    def test_verify_log_last_line_backup_ok(self):
        with open(VERIFY_LOG, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        assert lines, (
            f"The log file '{VERIFY_LOG}' is empty. "
            "It must contain at least one line with 'Backup OK'."
        )
        last_line = lines[-1]
        assert last_line == "Backup OK", (
            f"The last line of '{VERIFY_LOG}' must be exactly 'Backup OK'. "
            f"Found: {repr(last_line)}"
        )

    def test_verify_log_no_extra_whitespace_on_last_line(self):
        with open(VERIFY_LOG, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        last_line = lines[-1] if lines else ""
        assert last_line.strip() == "Backup OK", (
            f"The last line of '{VERIFY_LOG}' must be exactly 'Backup OK' with no extra whitespace. "
            f"Found: {repr(last_line)}"
        )
        assert last_line == "Backup OK", (
            f"The last line of '{VERIFY_LOG}' must be exactly 'Backup OK', no leading/trailing spaces. "
            f"Found: {repr(last_line)}"
        )