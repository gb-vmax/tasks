# test_final_state.py

import os
import re
import pytest
from datetime import datetime

DASHBOARD_CONFIG_DIR = "/home/user/observability/dashboard_config"
DASHBOARD_METRICS_YAML = os.path.join(DASHBOARD_CONFIG_DIR, "dashboard_metrics.yaml")
AUDIT_LOG = os.path.join(DASHBOARD_CONFIG_DIR, "audit.log")


@pytest.mark.describe("Final state validation for dashboard config update task")
class TestFinalState:

    def test_dashboard_config_directory_exists(self):
        assert os.path.isdir(DASHBOARD_CONFIG_DIR), (
            f"Required directory {DASHBOARD_CONFIG_DIR} does not exist. "
            "The dashboard_config directory must exist after the task."
        )

    def test_dashboard_metrics_yaml_exists(self):
        assert os.path.isfile(DASHBOARD_METRICS_YAML), (
            f"File {DASHBOARD_METRICS_YAML} does not exist. "
            "dashboard_metrics.yaml must exist after the task."
        )

    def test_dashboard_metrics_yaml_content(self):
        """
        Validates that:
        - refresh_interval is set to 60s
        - The comment "# Increased refresh interval from 30s to 60s on request" is present directly above refresh_interval
        - The structure matches the expected result
        """
        expected_lines = [
            "metrics:",
            "  cpu: usage",
            "  memory: usage",
            "# Dashboard refresh interval (update as needed)",
            "# Increased refresh interval from 30s to 60s on request",
            "refresh_interval: 60s"
        ]

        try:
            with open(DASHBOARD_METRICS_YAML, "r", encoding="utf-8") as f:
                content = f.read().strip().splitlines()
        except Exception as e:
            pytest.fail(f"Failed to read {DASHBOARD_METRICS_YAML}: {e}")

        # Remove empty lines for comparison
        content_no_empty = [line for line in content if line.strip()]

        # Check that all expected lines are present in order (no extra lines in between the last 3 lines)
        # Allow for possible extra blank lines elsewhere
        # The last three lines must be in this exact order and contiguous
        if len(content_no_empty) < 6:
            pytest.fail(
                f"{DASHBOARD_METRICS_YAML} is missing lines. "
                f"Expected at least 6 non-empty lines, found {len(content_no_empty)}."
            )

        # Check first three lines (metrics)
        for i in range(3):
            assert content_no_empty[i] == expected_lines[i], (
                f"dashboard_metrics.yaml line {i+1} is:\n"
                f"  '{content_no_empty[i]}'\nbut expected:\n"
                f"  '{expected_lines[i]}'"
            )

        # Find the index of "# Dashboard refresh interval (update as needed)"
        try:
            dash_comment_idx = content_no_empty.index(expected_lines[3])
        except ValueError:
            pytest.fail(
                f"dashboard_metrics.yaml is missing the line:\n"
                f"  '{expected_lines[3]}'"
            )

        # The next two lines must be the new comment, then the new refresh_interval
        if dash_comment_idx + 2 >= len(content_no_empty):
            pytest.fail(
                f"dashboard_metrics.yaml is missing expected lines after:\n"
                f"  '{expected_lines[3]}'"
            )

        assert content_no_empty[dash_comment_idx + 1] == expected_lines[4], (
            f"dashboard_metrics.yaml line after '{expected_lines[3]}' is:\n"
            f"  '{content_no_empty[dash_comment_idx + 1]}'\nbut expected:\n"
            f"  '{expected_lines[4]}'\n"
            "The required comment is missing or not directly above refresh_interval."
        )

        assert content_no_empty[dash_comment_idx + 2] == expected_lines[5], (
            f"dashboard_metrics.yaml line after comment is:\n"
            f"  '{content_no_empty[dash_comment_idx + 2]}'\nbut expected:\n"
            f"  '{expected_lines[5]}'\n"
            "refresh_interval must be set to '60s' after the comment."
        )

        # Ensure "refresh_interval: 30s" does NOT appear anywhere
        for line in content_no_empty:
            assert "refresh_interval: 30s" not in line, (
                "dashboard_metrics.yaml still contains 'refresh_interval: 30s'; it must be changed to '60s'."
            )

    def test_audit_log_exists(self):
        assert os.path.isfile(AUDIT_LOG), (
            f"File {AUDIT_LOG} does not exist. "
            "audit.log must exist after the task."
        )

    def test_audit_log_entry_appended(self):
        """
        Validates that:
        - The last line of audit.log is appended in the correct format.
        - The entry is for user, with the dashboard_metrics.yaml interval updated to 60s.
        - The timestamp is in the correct format and is not in the past (relative to previous entries).
        """
        expected_start = "[2024-06-23 10:03:55] alice: Created dashboard_metrics.yaml"
        expected_second = "[2024-06-23 10:10:02] bob: Edited dashboard_metrics.yaml"
        expected_action = "user: Refreshed dashboard_metrics.yaml interval to 60s"

        try:
            with open(AUDIT_LOG, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
        except Exception as e:
            pytest.fail(f"Failed to read {AUDIT_LOG}: {e}")

        assert len(lines) >= 3, (
            f"{AUDIT_LOG} should contain at least three lines after the task, found {len(lines)}."
        )
        assert lines[0] == expected_start, (
            f"First line of {AUDIT_LOG} is:\n"
            f"  '{lines[0]}'\nbut expected:\n"
            f"  '{expected_start}'"
        )
        assert lines[1] == expected_second, (
            f"Second line of {AUDIT_LOG} is:\n"
            f"  '{lines[1]}'\nbut expected:\n"
            f"  '{expected_second}'"
        )

        last_line = lines[-1]

        # Pattern: [YYYY-MM-DD HH:MM:SS] user: Refreshed dashboard_metrics.yaml interval to 60s
        audit_regex = (
            r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] user: Refreshed dashboard_metrics\.yaml interval to 60s$"
        )

        match = re.match(audit_regex, last_line)
        assert match is not None, (
            f"The last line of {AUDIT_LOG} is not in the required format:\n"
            f"  '{last_line}'\n"
            "Expected format:\n"
            "  [YYYY-MM-DD HH:MM:SS] user: Refreshed dashboard_metrics.yaml interval to 60s"
        )

        # Validate the timestamp is a valid ISO 8601 UTC time and not before the previous entries
        timestamp_str = match.group(1)
        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        except Exception:
            pytest.fail(
                f"The timestamp in the last audit.log entry is not a valid ISO 8601 UTC datetime:\n"
                f"  '{timestamp_str}'"
            )

        # Check that the timestamp is >= the previous entry (2024-06-23 10:10:02)
        previous_str = lines[1].split("]")[0][1:]  # Remove the leading '['
        previous_dt = datetime.strptime(previous_str, "%Y-%m-%d %H:%M:%S")
        assert timestamp >= previous_dt, (
            f"The timestamp of the new audit.log entry ({timestamp_str}) "
            f"is earlier than the previous entry ({previous_str})."
        )

        # Ensure no duplicate or misplaced entries
        for i, line in enumerate(lines[:-1]):
            assert "user: Refreshed dashboard_metrics.yaml interval to 60s" not in line, (
                f"The audit action for user appears before the last line (line {i+1}):\n"
                f"  '{line}'\n"
                "The new audit entry must be appended at the end."
            )