# test_final_state.py

import os
import pytest

HOME = "/home/user"
TOOLS_DIR = os.path.join(HOME, "tools")
PING_TEST_SH = os.path.join(TOOLS_DIR, "ping_test.sh")
PING_OUTPUT_LOG = os.path.join(TOOLS_DIR, "ping_output.log")
PINGTEST_SYMLINK = os.path.join(HOME, "pingtest")
PINGLOG_SYMLINK = os.path.join(HOME, "pinglog")
SYMLINK_REPORT = os.path.join(HOME, "symlink_report.log")

@pytest.mark.describe("Final OS/filesystem state after symlink management is complete")
class TestFinalState:

    def test_pingtest_symlink_exists_and_points_correctly(self):
        assert os.path.islink(PINGTEST_SYMLINK), (
            f"Symlink missing: {PINGTEST_SYMLINK}. "
            "It must exist and be a symlink."
        )
        target = os.readlink(PINGTEST_SYMLINK)
        expected = PING_TEST_SH
        assert target == expected, (
            f"Symlink {PINGTEST_SYMLINK} points to '{target}', but should point to '{expected}'."
        )

    def test_pinglog_symlink_exists_and_points_correctly(self):
        assert os.path.islink(PINGLOG_SYMLINK), (
            f"Symlink missing: {PINGLOG_SYMLINK}. "
            "It must exist and be a symlink."
        )
        target = os.readlink(PINGLOG_SYMLINK)
        expected = PING_OUTPUT_LOG
        assert target == expected, (
            f"Symlink {PINGLOG_SYMLINK} points to '{target}', but should point to '{expected}'."
        )

    def test_no_other_symlinks_in_home(self):
        expected_symlinks = {"pingtest", "pinglog"}
        found_symlinks = set()
        for entry in os.listdir(HOME):
            path = os.path.join(HOME, entry)
            if os.path.islink(path):
                found_symlinks.add(entry)
        extra = found_symlinks - expected_symlinks
        missing = expected_symlinks - found_symlinks
        assert not missing, (
            f"Expected symlinks missing in {HOME}: {sorted(missing)}"
        )
        assert not extra, (
            f"Unexpected symlinks present in {HOME}: {sorted(extra)}. "
            "Only 'pingtest' and 'pinglog' should be present."
        )

    def test_symlink_report_log_content(self):
        assert os.path.isfile(SYMLINK_REPORT), (
            f"Required file missing: {SYMLINK_REPORT}"
        )
        with open(SYMLINK_REPORT, "r", encoding="utf-8") as f:
            lines = [line.rstrip('\n\r') for line in f]

        # Build expected lines
        expected_lines = {
            f"pingtest -> {PING_TEST_SH}",
            f"pinglog -> {PING_OUTPUT_LOG}"
        }

        # Ignore blank lines, check only non-empty ones
        actual_lines = set(line for line in lines if line.strip())

        # Check for missing or extra lines
        missing = expected_lines - actual_lines
        extra = actual_lines - expected_lines

        assert not missing, (
            f"symlink_report.log is missing required lines: {sorted(missing)}"
        )
        assert not extra, (
            f"symlink_report.log has unexpected extra lines: {sorted(extra)}"
        )
        assert len(actual_lines) == 2, (
            f"symlink_report.log should have exactly 2 lines (one for each symlink), "
            f"but has {len(actual_lines)} lines: {sorted(actual_lines)}"
        )

    def test_symlink_report_does_not_include_other_symlinks(self):
        # If there were any other symlinks in /home/user, they should not be listed
        with open(SYMLINK_REPORT, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        # Acceptable lines only:
        valid_lines = {
            f"pingtest -> {PING_TEST_SH}",
            f"pinglog -> {PING_OUTPUT_LOG}"
        }
        for line in lines:
            assert line in valid_lines, (
                f"symlink_report.log contains invalid line: '{line}'. "
                "Only 'pingtest' and 'pinglog' symlinks should be reported."
            )