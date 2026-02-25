# test_final_state.py
"""
Pytest suite to validate the FINAL OS/container state after the deployment engineer task.

This tests:
- Exact contents and order of /home/user/app-deployment/host-version-report.csv
- Exact in-place changes to /home/user/app-deployment/deployment.log
- That the correct number of FAILED lines was output and appended as summary
- RW permissions for all files created/modified

Assumptions:
- The task is performed in /home/user/app-deployment
- All files are UTF-8 encoded text files.
"""

import os
import stat
import pytest

APP_DEPLOY_DIR = "/home/user/app-deployment"
SERVER_LIST = os.path.join(APP_DEPLOY_DIR, "server-list.txt")
VERSION_INFO = os.path.join(APP_DEPLOY_DIR, "version-info.txt")
DEPLOYMENT_LOG = os.path.join(APP_DEPLOY_DIR, "deployment.log")
HOST_VERSION_REPORT = os.path.join(APP_DEPLOY_DIR, "host-version-report.csv")

EXPECTED_HOST_VERSION_REPORT = [
    "Hostname,Version",
    "app-server-01,2.4.7",
    "web-server-02,3.1.0",
    "db-server-03,1.9.8",
    "backup-server-04,UNKNOWN",
    "TOTAL_FAILED,2",
]

EXPECTED_DEPLOYMENT_LOG = [
    "2024-03-07 12:15:43 DEPLOY INITIATED app-server-01",
    "2024-03-07 12:15:47 DEPLOY INITIATED web-server-02",
    "2024-03-07 12:15:51 DEPLOYMENT SUCCEEDED app-server-01",
    "2024-03-07 12:16:05 DEPLOYMENT FAILED web-server-02",
    "2024-03-07 12:17:00 DEPLOY INITIATED db-server-03",
    "2024-03-07 12:17:08 DEPLOYMENT SUCCEEDED db-server-03",
    "2024-03-07 12:17:35 DEPLOYMENT SUCCEEDED backup-server-04",
    "2024-03-07 12:18:00 DEPLOYMENT FAILED backup-server-04",
    "2024-03-07 12:18:05 DEPLOYMENT COMPLETE",
]

EXPECTED_FAILED_COUNT = 2

@pytest.mark.describe("Final OS/FS state after deployment engineer task")
class TestFinalState:
    def test_host_version_report_exists_and_content(self):
        assert os.path.isfile(HOST_VERSION_REPORT), (
            f"{HOST_VERSION_REPORT} does not exist. "
            "You must create the CSV report after processing server-list.txt and version-info.txt."
        )
        with open(HOST_VERSION_REPORT, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]
        assert lines == EXPECTED_HOST_VERSION_REPORT, (
            f"{HOST_VERSION_REPORT} contents are incorrect.\n"
            f"Expected:\n{EXPECTED_HOST_VERSION_REPORT}\n"
            f"But found:\n{lines}\n"
            "Check: header, row order, 'UNKNOWN' for missing host, and TOTAL_FAILED summary line."
        )
        self._check_rw_permissions(HOST_VERSION_REPORT)

    def test_deployment_log_content_and_replacement(self):
        assert os.path.isfile(DEPLOYMENT_LOG), (
            f"{DEPLOYMENT_LOG} does not exist."
        )
        with open(DEPLOYMENT_LOG, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]
        assert lines == EXPECTED_DEPLOYMENT_LOG, (
            f"{DEPLOYMENT_LOG} content is incorrect after in-place sed replacement.\n"
            f"Expected:\n{EXPECTED_DEPLOYMENT_LOG}\n"
            f"But found:\n{lines}\n"
            "Check that only lines with 'DEPLOY START' were replaced with 'DEPLOY INITIATED' and all other lines are unchanged."
        )
        self._check_rw_permissions(DEPLOYMENT_LOG)

    def test_failed_count_in_deployment_log(self):
        # Check that number of lines with 'FAILED' is as expected
        with open(DEPLOYMENT_LOG, "r", encoding="utf-8") as f:
            failed_lines = [line for line in f if "FAILED" in line]
        actual_failed = len(failed_lines)
        assert actual_failed == EXPECTED_FAILED_COUNT, (
            f"There should be {EXPECTED_FAILED_COUNT} lines containing 'FAILED' in {DEPLOYMENT_LOG}, "
            f"but found {actual_failed}. Offending lines:\n{failed_lines}"
        )

    def test_summary_line_in_report_matches_failed_count(self):
        # The last line of the CSV must be TOTAL_FAILED,[number] and match actual count
        with open(HOST_VERSION_REPORT, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]
        assert lines[-1].startswith("TOTAL_FAILED,"), (
            f"The last line of {HOST_VERSION_REPORT} must start with 'TOTAL_FAILED,'. Found: {lines[-1]!r}"
        )
        try:
            failed_count = int(lines[-1].split(",")[1])
        except Exception:
            pytest.fail(f"The last line of {HOST_VERSION_REPORT} is not in the format TOTAL_FAILED,[number]: {lines[-1]!r}")
        assert failed_count == EXPECTED_FAILED_COUNT, (
            f"The summary line in {HOST_VERSION_REPORT} reports {failed_count} failed, "
            f"but there are {EXPECTED_FAILED_COUNT} lines containing 'FAILED' in {DEPLOYMENT_LOG}."
        )

    def test_permissions_rw_for_all_files(self):
        # All files must be readable and writable by the current user
        for path in [DEPLOYMENT_LOG, HOST_VERSION_REPORT]:
            self._check_rw_permissions(path)

    def _check_rw_permissions(self, path):
        """Ensure the current user has read/write permissions for the file."""
        st = os.stat(path)
        mode = st.st_mode
        can_read = bool(mode & stat.S_IRUSR)
        can_write = bool(mode & stat.S_IWUSR)
        assert can_read and can_write, (
            f"File {path} must be readable and writable by the current user."
        )