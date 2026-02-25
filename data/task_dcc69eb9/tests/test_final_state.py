# test_final_state.py

import os
import sys
import pytest

HOME = "/home/user"
USER_MANAGEMENT_DIR = os.path.join(HOME, "user_management")
VENV_DIR = os.path.join(USER_MANAGEMENT_DIR, "venv")
SETUP_LOG = os.path.join(USER_MANAGEMENT_DIR, "setup_log.txt")

@pytest.mark.describe("Final state of user_management Python venv setup")
class TestUserManagementFinalState:

    def test_user_management_dir_exists(self):
        assert os.path.isdir(USER_MANAGEMENT_DIR), (
            f"Directory '{USER_MANAGEMENT_DIR}' does not exist. "
            "You must create this directory in your home directory."
        )

    def test_user_management_contents(self):
        assert os.path.isdir(USER_MANAGEMENT_DIR), (
            f"Directory '{USER_MANAGEMENT_DIR}' does not exist."
        )
        entries = sorted(os.listdir(USER_MANAGEMENT_DIR))
        expected = ["setup_log.txt", "venv"]
        assert entries == expected, (
            f"Directory '{USER_MANAGEMENT_DIR}' must contain only these items: {expected}.\n"
            f"Found: {entries}"
        )

    def test_setup_log_exists(self):
        assert os.path.isfile(SETUP_LOG), (
            f"File '{SETUP_LOG}' does not exist. "
            "You must create this file with the directory listing."
        )

    def test_setup_log_contents(self):
        assert os.path.isfile(SETUP_LOG), (
            f"File '{SETUP_LOG}' does not exist."
        )
        with open(SETUP_LOG, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        expected = ["setup_log.txt", "venv"]
        assert lines == expected, (
            f"File '{SETUP_LOG}' must contain exactly these lines in this order:\n"
            "setup_log.txt\nvenv\n"
            f"Found:\n{lines}"
        )

    def test_venv_dir_exists_and_is_dir(self):
        assert os.path.isdir(VENV_DIR), (
            f"'{VENV_DIR}' does not exist or is not a directory. "
            "You must create the virtual environment directory using Python 3 venv."
        )

    def test_venv_structure(self):
        # Check for key venv structure elements
        expected_items = ["bin", "lib", "pyvenv.cfg"]
        missing = []
        for item in expected_items:
            path = os.path.join(VENV_DIR, item)
            if item.endswith("/"):
                if not os.path.isdir(path):
                    missing.append(item)
            else:
                # bin and lib are dirs, pyvenv.cfg is file
                if item == "pyvenv.cfg":
                    if not os.path.isfile(path):
                        missing.append(item)
                else:
                    if not os.path.isdir(path):
                        missing.append(item)
        assert not missing, (
            f"Virtual environment directory '{VENV_DIR}' is missing expected items: {missing}. "
            "It should be created using 'python3 -m venv venv'."
        )

    def test_venv_python_is_python3(self):
        # Check that the python executable in venv/bin is python3
        python_bin = os.path.join(VENV_DIR, "bin", "python")
        assert os.path.isfile(python_bin) or os.path.islink(python_bin), (
            f"Python executable '{python_bin}' not found in the virtual environment."
        )
        # Check the version string if possible
        import subprocess
        try:
            output = subprocess.check_output([python_bin, "--version"], stderr=subprocess.STDOUT, timeout=3)
            version_line = output.decode().strip()
            assert version_line.startswith("Python 3."), (
                f"Virtual environment does not use Python 3: '{version_line}'"
            )
        except Exception as e:
            pytest.fail(f"Could not check Python version in venv: {e}")

    def test_no_extra_files_or_dirs(self):
        # Check that there are no extra files or directories under /home/user/user_management
        entries = set(os.listdir(USER_MANAGEMENT_DIR))
        expected = {"setup_log.txt", "venv"}
        extra = entries - expected
        assert not extra, (
            f"Directory '{USER_MANAGEMENT_DIR}' contains unexpected files or directories: {sorted(extra)}"
        )