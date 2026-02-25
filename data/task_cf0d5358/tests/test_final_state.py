# test_final_state.py

import os
import stat
import pytest
from datetime import datetime

ALERT_SCRIPTS_DIR = "/home/user/alert_scripts"
CHECK_DISK_SH = os.path.join(ALERT_SCRIPTS_DIR, "check_disk.sh")
CHANGELOG_MD = os.path.join(ALERT_SCRIPTS_DIR, "CHANGELOG.md")
RELEASE_LOG = os.path.join(ALERT_SCRIPTS_DIR, "release.log")

EXPECTED_VERSION_LINE = "# Version: 1.3.0\n"
EXPECTED_CHECK_DISK_SH = [
    "# Version: 1.3.0\n",
    "#!/bin/bash\n",
    "# Script to check disk space and trigger alerts\n"
]

RELEASE_LOG_CONTENT = (
    "Bumped version to 1.3.0\n"
    "Changelog updated for 1.3.0\n"
    "Release prepared successfully\n"
)

def check_rw_permissions(path):
    """Check if file exists and is readable/writable by the user."""
    try:
        st = os.stat(path)
    except FileNotFoundError:
        return False
    mode = st.st_mode
    # User read and write
    return bool(mode & stat.S_IRUSR) and bool(mode & stat.S_IWUSR)

@pytest.mark.describe("Final filesystem state after release preparation")
class TestFinalState:
    def test_alert_scripts_directory_exists(self):
        assert os.path.isdir(ALERT_SCRIPTS_DIR), (
            f"Missing directory: {ALERT_SCRIPTS_DIR}"
        )

    def test_check_disk_sh_version_bumped_and_content_preserved(self):
        assert os.path.isfile(CHECK_DISK_SH), (
            f"Missing script file: {CHECK_DISK_SH}"
        )
        assert check_rw_permissions(CHECK_DISK_SH), (
            f"{CHECK_DISK_SH} must be readable and writable by the user"
        )
        with open(CHECK_DISK_SH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if len(lines) < 3:
            pytest.fail(
                f"{CHECK_DISK_SH} must have at least 3 lines, found {len(lines)}"
            )
        normalized_lines = [line.rstrip('\r\n') for line in lines[:3]]
        normalized_expected = [line.rstrip('\n') for line in EXPECTED_CHECK_DISK_SH]
        assert normalized_lines == normalized_expected, (
            f"{CHECK_DISK_SH} must start with:\n"
            f"{''.join(EXPECTED_CHECK_DISK_SH)}"
        )
        # Ensure no old "# Version: 1.2.3" anywhere in the file
        for idx, line in enumerate(lines):
            if "# Version: 1.2.3" in line:
                pytest.fail(
                    f"{CHECK_DISK_SH} must not contain old version string '# Version: 1.2.3' (found on line {idx+1})"
                )

    def test_changelog_md_entry_at_top_and_previous_entries_preserved(self):
        assert os.path.isfile(CHANGELOG_MD), (
            f"CHANGELOG.md must exist at {CHANGELOG_MD} after release preparation."
        )
        assert check_rw_permissions(CHANGELOG_MD), (
            f"{CHANGELOG_MD} must be readable and writable by the user"
        )
        with open(CHANGELOG_MD, "r", encoding="utf-8") as f:
            changelog = f.read()
        # Compute today's date in UTC, ISO format
        today = datetime.utcnow().date().isoformat()
        expected_top = (
            f"## [1.3.0] - {today}\n"
            "### Added\n"
            "- Initial alert email integration.\n"
        )
        # The new entry must be at the very top
        if not changelog.startswith(expected_top):
            # Try to give a helpful diff
            actual_top = "".join(changelog.splitlines(keepends=True)[:4])
            pytest.fail(
                f"{CHANGELOG_MD} does not start with expected new entry.\n"
                f"Expected top lines:\n{expected_top!r}\n"
                f"Actual top lines:\n{actual_top!r}\n"
                f"Check entry format, version, or date."
            )
        # Must not lose previous entries
        # (If file is longer than just the new entry, check that old content is preserved)
        remaining = changelog[len(expected_top):]
        if remaining.strip():
            # There are previous entries; check that the previous entry is still present and not overwritten
            if "## [1.2.3]" not in remaining and "## [" not in remaining:
                pytest.fail(
                    f"{CHANGELOG_MD} does not preserve previous changelog entries after the new 1.3.0 entry."
                )

    def test_release_log_exists_and_content_exact(self):
        assert os.path.isfile(RELEASE_LOG), (
            f"Release log must exist at {RELEASE_LOG} after release preparation."
        )
        assert check_rw_permissions(RELEASE_LOG), (
            f"{RELEASE_LOG} must be readable and writable by the user"
        )
        with open(RELEASE_LOG, "r", encoding="utf-8") as f:
            content = f.read()
        if content != RELEASE_LOG_CONTENT:
            pytest.fail(
                f"{RELEASE_LOG} does not contain the expected release log content.\n"
                f"Expected:\n{RELEASE_LOG_CONTENT!r}\n"
                f"Actual:\n{content!r}\n"
                f"Check for missing lines, typos, or extra whitespace."
            )