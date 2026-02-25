# test_final_state.py

import os
import stat
import pytest

ARTIFACTS_DIR = "/home/user/mlops_artifacts"
RESULTS_FILE = "/home/user/mlops_artifacts/results.csv"
MODEL_FILE = "/home/user/mlops_artifacts/model.pt"
LOG_FILE = "/home/user/artifact_permission_fix.log"

EXPECTED_ARTIFACTS_MODE = 0o755  # drwxr-xr-x
EXPECTED_FILE_MODE = 0o644       # -rw-r--r--
LOG_EXPECTED_CONTENT = (
    "Directory: /home/user/mlops_artifacts/\n"
    "Writable by group: no\n"
    "Writable by others: no\n"
    "All files and subdirectories now writable only by owner: yes\n"
)

def check_mode(path):
    """Return the permission bits (as an int) for the given path."""
    return stat.S_IMODE(os.lstat(path).st_mode)

def is_group_writable(mode):
    """Check if group has write permission."""
    return bool(mode & stat.S_IWGRP)

def is_others_writable(mode):
    """Check if others have write permission."""
    return bool(mode & stat.S_IWOTH)

def is_owner_writable(mode):
    """Check if owner has write permission."""
    return bool(mode & stat.S_IWUSR)

@pytest.mark.describe("Final OS and filesystem state after permissions fix")
class TestFinalState:

    def test_artifacts_dir_exists_with_correct_permissions(self):
        assert os.path.isdir(ARTIFACTS_DIR), (
            f"Directory {ARTIFACTS_DIR} is missing after the task."
        )
        mode = check_mode(ARTIFACTS_DIR)
        assert mode == EXPECTED_ARTIFACTS_MODE, (
            f"{ARTIFACTS_DIR} permissions should be 755 (drwxr-xr-x) after the fix, "
            f"but are {oct(mode)}."
        )
        assert not is_group_writable(mode), (
            f"{ARTIFACTS_DIR} should NOT be group-writable after the fix."
        )
        assert not is_others_writable(mode), (
            f"{ARTIFACTS_DIR} should NOT be world-writable after the fix."
        )
        assert is_owner_writable(mode), (
            f"{ARTIFACTS_DIR} should be owner-writable after the fix."
        )

    def test_results_file_exists_with_correct_permissions(self):
        assert os.path.isfile(RESULTS_FILE), (
            f"File {RESULTS_FILE} is missing after the task."
        )
        mode = check_mode(RESULTS_FILE)
        assert mode == EXPECTED_FILE_MODE, (
            f"{RESULTS_FILE} permissions should be 644 (-rw-r--r--) after the fix, "
            f"but are {oct(mode)}."
        )
        assert not is_group_writable(mode), (
            f"{RESULTS_FILE} should NOT be group-writable after the fix."
        )
        assert not is_others_writable(mode), (
            f"{RESULTS_FILE} should NOT be world-writable after the fix."
        )
        assert is_owner_writable(mode), (
            f"{RESULTS_FILE} should be owner-writable after the fix."
        )

    def test_model_file_exists_with_correct_permissions(self):
        assert os.path.isfile(MODEL_FILE), (
            f"File {MODEL_FILE} is missing after the task."
        )
        mode = check_mode(MODEL_FILE)
        assert mode == EXPECTED_FILE_MODE, (
            f"{MODEL_FILE} permissions should be 644 (-rw-r--r--) after the fix, "
            f"but are {oct(mode)}."
        )
        assert not is_group_writable(mode), (
            f"{MODEL_FILE} should NOT be group-writable after the fix."
        )
        assert not is_others_writable(mode), (
            f"{MODEL_FILE} should NOT be world-writable after the fix."
        )
        assert is_owner_writable(mode), (
            f"{MODEL_FILE} should be owner-writable after the fix."
        )

    def test_no_unexpected_files_in_artifacts_dir(self):
        expected = {RESULTS_FILE, MODEL_FILE}
        contents = set(
            os.path.join(ARTIFACTS_DIR, name)
            for name in os.listdir(ARTIFACTS_DIR)
        )
        unexpected = contents - expected
        assert not unexpected, (
            f"Unexpected files or directories found in {ARTIFACTS_DIR}: {unexpected}. "
            "Only results.csv and model.pt should be present after the task."
        )

    def test_log_file_exists_with_correct_content(self):
        assert os.path.isfile(LOG_FILE), (
            f"Verification log {LOG_FILE} does not exist after the task."
        )
        with open(LOG_FILE, "r") as f:
            content = f.read()
        assert content == LOG_EXPECTED_CONTENT, (
            f"{LOG_FILE} has incorrect content.\n"
            "Expected:\n"
            f"{LOG_EXPECTED_CONTENT!r}\n"
            "Got:\n"
            f"{content!r}"
        )

    def test_no_unexpected_files_created(self):
        # Only /home/user/mlops_artifacts/{results.csv, model.pt} and /home/user/artifact_permission_fix.log should exist
        allowed = {
            RESULTS_FILE,
            MODEL_FILE,
            LOG_FILE,
            ARTIFACTS_DIR,
            "/home/user"
        }
        # Collect all files/dirs under /home/user (not recursively)
        actual = set(
            os.path.join("/home/user", name)
            for name in os.listdir("/home/user")
        )
        # Add files in artifacts dir
        actual |= set(
            os.path.join(ARTIFACTS_DIR, name)
            for name in os.listdir(ARTIFACTS_DIR)
        )
        unexpected = actual - allowed
        # Ignore .bashrc, .profile, etc. if present (only test for extra files related to this task)
        unexpected = {p for p in unexpected if p.startswith(ARTIFACTS_DIR) or p == LOG_FILE}
        assert not unexpected, (
            f"Unexpected files or directories found: {unexpected}. "
            "No new files or directories should be created except the verification log."
        )

    def test_no_files_or_dirs_are_group_or_others_writable(self):
        """Recursively check that nothing in /home/user/mlops_artifacts is group/others writable."""
        for root, dirs, files in os.walk(ARTIFACTS_DIR):
            # Check the directory itself
            dir_mode = check_mode(root)
            assert not is_group_writable(dir_mode) and not is_others_writable(dir_mode), (
                f"Directory {root} is still group- or world-writable after the fix "
                f"(mode: {oct(dir_mode)})."
            )
            # Check files
            for name in files:
                file_path = os.path.join(root, name)
                file_mode = check_mode(file_path)
                assert not is_group_writable(file_mode) and not is_others_writable(file_mode), (
                    f"File {file_path} is still group- or world-writable after the fix "
                    f"(mode: {oct(file_mode)})."
                )
            # Check subdirectories
            for name in dirs:
                subdir_path = os.path.join(root, name)
                subdir_mode = check_mode(subdir_path)
                assert not is_group_writable(subdir_mode) and not is_others_writable(subdir_mode), (
                    f"Subdirectory {subdir_path} is still group- or world-writable after the fix "
                    f"(mode: {oct(subdir_mode)})."
                )