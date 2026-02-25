# test_final_state.py

import os
import pytest

YAML_PATH = "/home/user/backup/settings.yaml"
TOML_PATH = "/home/user/backup/settings.toml"
REPORT_PATH = "/home/user/backup/integrity_check_report.log"

@pytest.mark.describe("Verify final state after integrity check report generation")
class TestFinalState:

    def test_yaml_file_still_exists_and_unchanged(self):
        assert os.path.isfile(YAML_PATH), (
            f"Required YAML configuration file missing: {YAML_PATH}"
        )
        with open(YAML_PATH, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]
        expected_lines = [
            "integrity_check: true",
            'backup_schedule: "daily"',
            'compression: "gzip"',
        ]
        assert lines == expected_lines, (
            f"{YAML_PATH} contents have changed unexpectedly.\n"
            f"Expected:\n{expected_lines}\nFound:\n{lines}"
        )

    def test_toml_file_still_exists_and_unchanged(self):
        assert os.path.isfile(TOML_PATH), (
            f"Required TOML configuration file missing: {TOML_PATH}"
        )
        with open(TOML_PATH, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]
        expected_lines = [
            "integrity_check = false",
            'backup_schedule = "weekly"',
            'compression = "bzip2"',
        ]
        assert lines == expected_lines, (
            f"{TOML_PATH} contents have changed unexpectedly.\n"
            f"Expected:\n{expected_lines}\nFound:\n{lines}"
        )

    def test_report_file_exists(self):
        assert os.path.isfile(REPORT_PATH), (
            f"Integrity check report file does not exist at: {REPORT_PATH}"
        )

    def test_report_file_content_and_format(self):
        """
        The report log must contain exactly:
        YAML integrity_check: true
        TOML integrity_check: false
        (in this order, and nothing else)
        """
        with open(REPORT_PATH, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]

        expected_lines = [
            "YAML integrity_check: true",
            "TOML integrity_check: false",
        ]
        assert lines == expected_lines, (
            f"{REPORT_PATH} has incorrect content or format.\n"
            f"Expected exactly:\n{expected_lines}\nFound:\n{lines}\n"
            "Ensure the file contains ONLY these two lines, in order, with no extra content."
        )

    def test_report_file_permissions(self):
        """
        Optional: check that the report file is readable by the owner.
        """
        st = os.stat(REPORT_PATH)
        assert bool(st.st_mode & 0o400), (
            f"{REPORT_PATH} is not readable by the owner."
        )