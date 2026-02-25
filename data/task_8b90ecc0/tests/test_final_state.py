# test_final_state.py

import os
import pytest

HOME = "/home/user"
BACKUP_CONFIG = os.path.join(HOME, "backup_config.yaml")
RESTORE_POINTS = os.path.join(HOME, "restore_points.toml")
RESTORE_LOG = os.path.join(HOME, "restore_test.log")

FINAL_YAML = """---
name: daily_backup
enabled: false
paths:
  - /home/user/documents
  - /home/user/photos
retention_days: 3
---
"""

FINAL_TOML = """[restore1]
timestamp = "2024-05-22T10:00:00Z"
path = "/home/user/documents"
status = "valid"

[restore2]
timestamp = "2024-05-22T14:00:00Z"
path = "/home/user/photos"
status = "invalid"
"""

FINAL_LOG = """Backup config updated: enabled false, retention_days 3
Restore2 status updated: invalid
"""

def normalize_newlines(s):
    # Normalize all CRLF/CR to LF
    return s.replace('\r\n', '\n').replace('\r', '\n')

@pytest.mark.describe("Final state validation after student actions")
class TestFinalState:

    def test_backup_config_yaml_exists(self):
        assert os.path.isfile(BACKUP_CONFIG), (
            f"Missing required file: {BACKUP_CONFIG}"
        )

    def test_backup_config_yaml_content_exact(self):
        with open(BACKUP_CONFIG, "r", encoding="utf-8") as f:
            content = f.read()
        norm_expected = normalize_newlines(FINAL_YAML.strip())
        norm_actual = normalize_newlines(content.strip())
        assert norm_actual == norm_expected, (
            f"{BACKUP_CONFIG} does not have the correct final content.\n"
            f"Expected:\n{FINAL_YAML}\n"
            f"Got:\n{content}"
        )

    def test_backup_config_yaml_enabled_field(self):
        with open(BACKUP_CONFIG, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        enabled_line = next((l for l in lines if l.startswith("enabled:")), None)
        assert enabled_line == "enabled: false", (
            f"enabled field in {BACKUP_CONFIG} is not set to false as required.\n"
            f"Found line: {enabled_line!r}"
        )

    def test_backup_config_yaml_retention_days(self):
        with open(BACKUP_CONFIG, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        retention_line = next((l for l in lines if l.startswith("retention_days:")), None)
        assert retention_line == "retention_days: 3", (
            f"retention_days in {BACKUP_CONFIG} is not set to 3 as required.\n"
            f"Found line: {retention_line!r}"
        )

    def test_restore_points_toml_exists(self):
        assert os.path.isfile(RESTORE_POINTS), (
            f"Missing required file: {RESTORE_POINTS}"
        )

    def test_restore_points_toml_content_exact(self):
        with open(RESTORE_POINTS, "r", encoding="utf-8") as f:
            content = f.read()
        norm_expected = normalize_newlines(FINAL_TOML.strip())
        norm_actual = normalize_newlines(content.strip())
        assert norm_actual == norm_expected, (
            f"{RESTORE_POINTS} does not have the correct final content.\n"
            f"Expected:\n{FINAL_TOML}\n"
            f"Got:\n{content}"
        )

    def test_restore2_status_invalid(self):
        with open(RESTORE_POINTS, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f]
        in_restore2 = False
        status_line = None
        for line in lines:
            if line == "[restore2]":
                in_restore2 = True
            elif line.startswith("[") and line != "[restore2]":
                in_restore2 = False
            elif in_restore2 and line.startswith("status"):
                status_line = line
                break
        assert status_line == 'status = "invalid"', (
            f'The status for [restore2] in {RESTORE_POINTS} is not "invalid".\n'
            f"Found line: {status_line!r}"
        )

    def test_restore_log_exists(self):
        assert os.path.isfile(RESTORE_LOG), (
            f"Missing required log file: {RESTORE_LOG}"
        )

    def test_restore_log_content_exact(self):
        with open(RESTORE_LOG, "r", encoding="utf-8") as f:
            content = f.read()
        norm_expected = normalize_newlines(FINAL_LOG.strip())
        norm_actual = normalize_newlines(content.strip())
        assert norm_actual == norm_expected, (
            f"{RESTORE_LOG} does not have the exact required content.\n"
            f"Expected:\n{FINAL_LOG}\n"
            f"Got:\n{content}"
        )

    def test_restore_log_no_extra_lines(self):
        with open(RESTORE_LOG, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Should be exactly 2 lines, no extra blank lines
        nonblank_lines = [l.rstrip('\r\n') for l in lines if l.strip() != ""]
        assert len(nonblank_lines) == 2, (
            f"{RESTORE_LOG} should have exactly 2 non-empty lines in the required format, "
            f"but found {len(nonblank_lines)} lines.\n"
            f"Lines: {nonblank_lines!r}"
        )
        assert nonblank_lines[0] == "Backup config updated: enabled false, retention_days 3", (
            f"First line of {RESTORE_LOG} is not correct.\n"
            f"Expected: 'Backup config updated: enabled false, retention_days 3'\n"
            f"Got: {nonblank_lines[0]!r}"
        )
        assert nonblank_lines[1] == "Restore2 status updated: invalid", (
            f"Second line of {RESTORE_LOG} is not correct.\n"
            f"Expected: 'Restore2 status updated: invalid'\n"
            f"Got: {nonblank_lines[1]!r}"
        )