# test_final_state.py

import os
import stat
import pytest

AUDIT_LOG_PATH = "/home/user/security/audit.log"
FAILED_LOGINS_REPORT_PATH = "/home/user/security/failed_logins.report"
SECURITY_DIR = "/home/user/security"

EXPECTED_AUDIT_LOG_CONTENT = """Jan 07 10:15:12 server1 sshd[1245]: Accepted password for bob from 10.0.0.5 port 4857 ssh2
Jan 07 10:16:33 server1 sshd[1247]: Failed password for alice from 10.0.0.7 port 5060 ssh2
Jan 07 10:18:02 server1 su[1250]: authentication failure; logname=bob uid=1000 euid=0 tty=pts/0 ruser=bob rhost=
Jan 07 10:20:59 server1 sshd[1262]: Connection closed by authenticating user alice 10.0.0.7 port 5088 [preauth]
Jan 07 10:21:12 server1 sshd[1270]: Failed password for invalid user admin from 10.0.0.12 port 5164 ssh2
Jan 07 10:22:50 server1 su[1275]: session opened for user root by bob(uid=1000)
Jan 07 10:23:18 server1 sshd[1279]: Failed password for root from 10.0.0.15 port 5210 ssh2
"""

EXPECTED_FAILED_LOGINS_REPORT_CONTENT = """Jan 07 10:16:33 server1 sshd[1247]: Failed password for alice from 10.0.0.7 port 5060 ssh2
Jan 07 10:18:02 server1 su[1250]: authentication failure; logname=bob uid=1000 euid=0 tty=pts/0 ruser=bob rhost=
Jan 07 10:21:12 server1 sshd[1270]: Failed password for invalid user admin from 10.0.0.12 port 5164 ssh2
Jan 07 10:23:18 server1 sshd[1279]: Failed password for root from 10.0.0.15 port 5210 ssh2
"""

@pytest.mark.describe("Final OS state after extracting failed login entries")
class TestFinalState:

    def test_security_directory_unchanged_exists(self):
        assert os.path.isdir(SECURITY_DIR), (
            f"Required directory '{SECURITY_DIR}' does not exist after the task. "
            "It must not be deleted or moved."
        )

    def test_audit_log_unchanged(self):
        assert os.path.isfile(AUDIT_LOG_PATH), (
            f"The original log file '{AUDIT_LOG_PATH}' is missing after the task. "
            "You must not remove or rename this file."
        )
        st = os.stat(AUDIT_LOG_PATH)
        file_mode = st.st_mode
        assert bool(file_mode & stat.S_IRUSR), (
            f"Log file '{AUDIT_LOG_PATH}' is no longer readable by the user after the task. "
            "Permissions must not be changed."
        )
        assert bool(file_mode & stat.S_IWUSR), (
            f"Log file '{AUDIT_LOG_PATH}' is no longer writable by the user after the task. "
            "Permissions must not be changed."
        )
        with open(AUDIT_LOG_PATH, encoding="utf-8") as f:
            actual_content = f.read().strip('\n')
        expected_content = EXPECTED_AUDIT_LOG_CONTENT.strip('\n')
        assert actual_content == expected_content, (
            f"The contents of '{AUDIT_LOG_PATH}' have changed after the task.\n"
            "You must not modify the original log file.\n"
            "Expected:\n"
            f"{expected_content}\n\n"
            "Actual:\n"
            f"{actual_content}\n"
        )

    def test_failed_logins_report_exists(self):
        assert os.path.isfile(FAILED_LOGINS_REPORT_PATH), (
            f"Report file '{FAILED_LOGINS_REPORT_PATH}' does not exist after the task. "
            "You must create this file containing the filtered failed login entries."
        )

    def test_failed_logins_report_content_exact(self):
        with open(FAILED_LOGINS_REPORT_PATH, encoding="utf-8") as f:
            actual_report = f.read().strip('\n')
        expected = EXPECTED_FAILED_LOGINS_REPORT_CONTENT.strip('\n')
        if actual_report != expected:
            # Find line-by-line differences for clarity
            actual_lines = actual_report.splitlines()
            expected_lines = expected.splitlines()
            max_lines = max(len(actual_lines), len(expected_lines))
            diff_lines = []
            for i in range(max_lines):
                exp_line = expected_lines[i] if i < len(expected_lines) else "<no line>"
                act_line = actual_lines[i] if i < len(actual_lines) else "<no line>"
                if exp_line != act_line:
                    diff_lines.append(
                        f"Line {i+1}:\n  Expected: {exp_line!r}\n  Actual:   {act_line!r}"
                    )
            diff_str = "\n".join(diff_lines)
            pytest.fail(
                f"The contents of '{FAILED_LOGINS_REPORT_PATH}' do not match the expected report.\n"
                "Differences:\n"
                f"{diff_str}\n\n"
                "Ensure ONLY lines containing EXACTLY 'Failed password' or 'authentication failure' "
                "are included, in order, with no blank lines or extra text."
            )

    def test_failed_logins_report_no_extra_lines(self):
        """Ensure no blank lines or extra lines are present."""
        with open(FAILED_LOGINS_REPORT_PATH, encoding="utf-8") as f:
            lines = f.read().splitlines()
        for i, line in enumerate(lines, 1):
            assert line.strip() != "", (
                f"Blank line found at line {i} in '{FAILED_LOGINS_REPORT_PATH}'. "
                "The report must not contain blank or empty lines."
            )

    def test_failed_logins_report_only_expected_lines(self):
        """Ensure no unrelated lines are present."""
        expected_lines = [
            "Jan 07 10:16:33 server1 sshd[1247]: Failed password for alice from 10.0.0.7 port 5060 ssh2",
            "Jan 07 10:18:02 server1 su[1250]: authentication failure; logname=bob uid=1000 euid=0 tty=pts/0 ruser=bob rhost=",
            "Jan 07 10:21:12 server1 sshd[1270]: Failed password for invalid user admin from 10.0.0.12 port 5164 ssh2",
            "Jan 07 10:23:18 server1 sshd[1279]: Failed password for root from 10.0.0.15 port 5210 ssh2"
        ]
        with open(FAILED_LOGINS_REPORT_PATH, encoding="utf-8") as f:
            report_lines = f.read().splitlines()
        for line in report_lines:
            assert (
                "Failed password" in line or "authentication failure" in line
            ), (
                f"Line in '{FAILED_LOGINS_REPORT_PATH}' does not contain a required phrase:\n"
                f"  {line!r}\n"
                "Only lines with 'Failed password' or 'authentication failure' (case-sensitive, exact phrase) "
                "must be included."
            )
        assert report_lines == expected_lines, (
            "The lines in the report do not match the expected filtered lines in the correct order.\n"
            f"Expected:\n{expected_lines}\nActual:\n{report_lines}\n"
            "Ensure only the correct lines are present, in order."
        )

    def test_no_unexpected_files_created(self):
        """Ensure no extra files were created in /home/user/security/ except the report."""
        files = set(os.listdir(SECURITY_DIR))
        expected_files = {"audit.log", "failed_logins.report"}
        extra_files = files - expected_files
        assert not extra_files, (
            f"Unexpected files found in '{SECURITY_DIR}': {sorted(extra_files)}\n"
            "You must not create or leave any extra files in the directory."
        )