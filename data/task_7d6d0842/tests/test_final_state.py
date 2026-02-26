# test_final_state.py

"""
Pytest suite to validate the FINAL state after extraction of integrity_check_dir
from /home/user/configs/backup.yml and /home/user/configs/backup.toml,
and creation of /home/user/backup_integrity_locations.log with the exact required format.

This test ensures:
- The log file exists at the correct path.
- The log file content is exactly as specified, including blank lines and order.
- Both source config files still exist and are unchanged.
"""

import os
import pytest

HOME = "/home/user"
YML_PATH = os.path.join(HOME, "configs", "backup.yml")
TOML_PATH = os.path.join(HOME, "configs", "backup.toml")
LOG_PATH = os.path.join(HOME, "backup_integrity_locations.log")

YML_EXPECTED_CONTENT = (
    "backup_dir: /mnt/storage/backups\n"
    "integrity_check_dir: /mnt/storage/integrity\n"
    "retention_days: 30\n"
)

TOML_EXPECTED_CONTENT = (
    'backup_dir = "/mnt/storage/backups"\n'
    'retention_days = 30\n'
    "\n"
    "[checks]\n"
    'integrity_check_dir = "/mnt/storage/integrity"\n'
)

LOG_EXPECTED_CONTENT = (
    "[backup.yml]\n"
    "integrity_check_dir: /mnt/storage/integrity\n"
    "\n"
    "[backup.toml]\n"
    "integrity_check_dir: /mnt/storage/integrity\n"
)

@pytest.mark.describe("Final OS state after backup integrity location extraction")
class TestFinalState:
    def test_log_file_exists(self):
        assert os.path.isfile(LOG_PATH), (
            f"Expected log file {LOG_PATH} does not exist.\n"
            "You must create this file as part of the task."
        )

    def test_log_file_content_exact(self):
        try:
            with open(LOG_PATH, "r") as f:
                actual = f.read()
        except Exception as e:
            pytest.fail(f"Could not read {LOG_PATH}: {e}")
        if actual != LOG_EXPECTED_CONTENT:
            # Show a diff-like output for clarity
            import difflib
            diff = "\n".join(
                difflib.unified_diff(
                    LOG_EXPECTED_CONTENT.splitlines(),
                    actual.splitlines(),
                    fromfile="expected",
                    tofile="actual",
                    lineterm=""
                )
            )
            pytest.fail(
                f"{LOG_PATH} content does not match the expected format and values.\n"
                "Differences (expected vs actual):\n"
                f"{diff}\n"
                "Ensure the file matches the required output exactly, including blank lines and section order."
            )

    def test_backup_yml_still_exists_and_unchanged(self):
        assert os.path.isfile(YML_PATH), (
            f"Required YAML config file {YML_PATH} is missing after the task.\n"
            "Do not delete or move the original configuration files."
        )
        try:
            with open(YML_PATH, "r") as f:
                actual = f.read()
        except Exception as e:
            pytest.fail(f"Could not read {YML_PATH}: {e}")
        # Normalize trailing newlines for comparison
        expected = YML_EXPECTED_CONTENT
        if not actual.endswith("\n"):
            actual += "\n"
        if actual != expected:
            pytest.fail(
                f"{YML_PATH} was modified during the task.\n"
                "Do not alter the original YAML configuration file.\n"
                "Expected content:\n"
                f"{expected}\n"
                "Actual content:\n"
                f"{actual}\n"
            )

    def test_backup_toml_still_exists_and_unchanged(self):
        assert os.path.isfile(TOML_PATH), (
            f"Required TOML config file {TOML_PATH} is missing after the task.\n"
            "Do not delete or move the original configuration files."
        )
        try:
            with open(TOML_PATH, "r") as f:
                actual = f.read()
        except Exception as e:
            pytest.fail(f"Could not read {TOML_PATH}: {e}")
        # Normalize trailing newlines for comparison
        expected = TOML_EXPECTED_CONTENT
        if not actual.endswith("\n"):
            actual += "\n"
        if actual != expected:
            pytest.fail(
                f"{TOML_PATH} was modified during the task.\n"
                "Do not alter the original TOML configuration file.\n"
                "Expected content:\n"
                f"{expected}\n"
                "Actual content:\n"
                f"{actual}\n"
            )