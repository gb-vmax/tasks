# test_final_state.py

import os
import pytest

UPTIME_MONITOR_DIR = "/home/user/uptime_monitor"
VERSION_PATH = os.path.join(UPTIME_MONITOR_DIR, "VERSION")
CHANGELOG_PATH = os.path.join(UPTIME_MONITOR_DIR, "CHANGELOG.md")

EXPECTED_VERSION = "1.4.2"

EXPECTED_CHANGELOG_LINES = [
    "## [1.4.2] - 2023-08-10",
    "### Fixed",
    "- Corrected bug in downtime duration calculation.",
    "",
    "## [1.4.1] - 2023-07-01",
    "### Changed",
    "- Improved response time tracking.",
    "",
    "## [1.4.0] - 2023-06-25",
    "### Added",
    "- Introduced uptime monitor for service health.",
]

EXPECTED_CHANGELOG_FIRST6 = [
    "## [1.4.2] - 2023-08-10",
    "### Fixed",
    "- Corrected bug in downtime duration calculation.",
    "",
    "## [1.4.1] - 2023-07-01",
    "### Changed",
]

@pytest.mark.describe("Final state of uptime_monitor project after version bump and changelog update")
class TestFinalState:
    def test_project_directory_exists(self):
        assert os.path.isdir(UPTIME_MONITOR_DIR), (
            f"Required directory '{UPTIME_MONITOR_DIR}' is missing."
        )

    def test_version_file_exists(self):
        assert os.path.isfile(VERSION_PATH), (
            f"Required file '{VERSION_PATH}' is missing."
        )

    def test_changelog_file_exists(self):
        assert os.path.isfile(CHANGELOG_PATH), (
            f"Required file '{CHANGELOG_PATH}' is missing."
        )

    def test_version_file_content(self):
        with open(VERSION_PATH, "r", encoding="utf-8") as f:
            content = f.read().strip()
        assert content == EXPECTED_VERSION, (
            f"Expected '{VERSION_PATH}' to contain '{EXPECTED_VERSION}', but found: '{content}'"
        )

    def test_changelog_file_content_exact(self):
        with open(CHANGELOG_PATH, "r", encoding="utf-8") as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
        # Check length
        assert len(lines) == len(EXPECTED_CHANGELOG_LINES), (
            f"'{CHANGELOG_PATH}' has {len(lines)} lines, expected {len(EXPECTED_CHANGELOG_LINES)}."
        )
        # Check all lines
        for i, expected_line in enumerate(EXPECTED_CHANGELOG_LINES):
            assert lines[i] == expected_line, (
                f"Line {i+1} of '{CHANGELOG_PATH}' does not match.\n"
                f"Expected: '{expected_line}'\n"
                f"Found:    '{lines[i]}'"
            )

    def test_changelog_first_6_lines(self, capsys):
        with open(CHANGELOG_PATH, "r", encoding="utf-8") as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
        output_lines = lines[:6]
        print('\n'.join(output_lines))
        # Validate output matches the expectation
        for idx, expected_line in enumerate(EXPECTED_CHANGELOG_FIRST6):
            if idx >= len(output_lines):
                pytest.fail(
                    f"When printing the first 6 lines of '{CHANGELOG_PATH}', "
                    f"output is missing line {idx+1}: '{expected_line}'"
                )
            assert output_lines[idx] == expected_line, (
                f"When printing the first 6 lines of '{CHANGELOG_PATH}', line {idx+1} does not match.\n"
                f"Expected: '{expected_line}'\n"
                f"Found:    '{output_lines[idx]}'"
            )

    def test_version_print_output(self, capsys):
        with open(VERSION_PATH, "r", encoding="utf-8") as f:
            content = f.read().strip()
        print(content)
        assert content == EXPECTED_VERSION, (
            f"When printing the contents of '{VERSION_PATH}', expected '{EXPECTED_VERSION}', but found: '{content}'"
        )