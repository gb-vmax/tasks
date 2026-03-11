# test_final_state.py

import os
import stat
import pytest

DEPLOY_DIR = "/home/user/deploy"
START_SH = "/home/user/deploy/start.sh"
DB_CONF = "/home/user/deploy/config/db.conf"
APP_CONF = "/home/user/deploy/config/app.conf"
LOGS_DIR = "/home/user/deploy/logs"
AUDIT_FILE = "/home/user/deploy/security_audit.txt"

EXPECTED_AUDIT_CONTENT = (
    "DEPLOYMENT SECURITY AUDIT\n"
    "=========================\n"
    "start.sh: -rwxr-x---\n"
    "config/db.conf: -rw-------\n"
    "config/app.conf: -rw-r-----\n"
    "logs/: drwxr-x---\n"
    "STATUS: SECURED"
)


def get_octal_permissions(path):
    """Return the octal permission bits for a path."""
    st = os.stat(path)
    return stat.S_IMODE(st.st_mode)


class TestDeployDirectoryExists:
    def test_deploy_dir_exists(self):
        assert os.path.isdir(DEPLOY_DIR), (
            f"Deploy directory {DEPLOY_DIR} does not exist."
        )

    def test_config_dir_exists(self):
        config_dir = os.path.join(DEPLOY_DIR, "config")
        assert os.path.isdir(config_dir), (
            f"Config directory {config_dir} does not exist."
        )


class TestStartShFinalState:
    def test_start_sh_exists(self):
        assert os.path.isfile(START_SH), (
            f"File {START_SH} does not exist."
        )

    def test_start_sh_permissions(self):
        perms = get_octal_permissions(START_SH)
        assert perms == 0o750, (
            f"start.sh has permissions {oct(perms)} ({stat.filemode(os.stat(START_SH).st_mode)}), "
            f"expected 0o750 (-rwxr-x---). "
            f"start.sh must not be world-writable or world-readable."
        )

    def test_start_sh_content_unchanged(self):
        with open(START_SH, 'r') as f:
            content = f.read()
        expected = "#!/bin/bash\necho 'Starting app'\n"
        assert content == expected, (
            f"start.sh content was modified.\n"
            f"Expected: {repr(expected)}\n"
            f"Got: {repr(content)}"
        )


class TestDbConfFinalState:
    def test_db_conf_exists(self):
        assert os.path.isfile(DB_CONF), (
            f"File {DB_CONF} does not exist."
        )

    def test_db_conf_permissions(self):
        perms = get_octal_permissions(DB_CONF)
        assert perms == 0o600, (
            f"config/db.conf has permissions {oct(perms)} ({stat.filemode(os.stat(DB_CONF).st_mode)}), "
            f"expected 0o600 (-rw-------). "
            f"db.conf must only be readable/writable by owner with no group or other permissions."
        )

    def test_db_conf_content_unchanged(self):
        with open(DB_CONF, 'r') as f:
            content = f.read()
        expected = "host=localhost\npassword=s3cr3t\n"
        assert content == expected, (
            f"config/db.conf content was modified.\n"
            f"Expected: {repr(expected)}\n"
            f"Got: {repr(content)}"
        )


class TestAppConfFinalState:
    def test_app_conf_exists(self):
        assert os.path.isfile(APP_CONF), (
            f"File {APP_CONF} does not exist."
        )

    def test_app_conf_permissions(self):
        perms = get_octal_permissions(APP_CONF)
        assert perms == 0o640, (
            f"config/app.conf has permissions {oct(perms)} ({stat.filemode(os.stat(APP_CONF).st_mode)}), "
            f"expected 0o640 (-rw-r-----). "
            f"app.conf must be readable/writable by owner, readable by group, no permissions for others."
        )

    def test_app_conf_content_unchanged(self):
        with open(APP_CONF, 'r') as f:
            content = f.read()
        expected = "debug=false\nport=8080\n"
        assert content == expected, (
            f"config/app.conf content was modified.\n"
            f"Expected: {repr(expected)}\n"
            f"Got: {repr(content)}"
        )


class TestLogsDirFinalState:
    def test_logs_dir_exists(self):
        assert os.path.isdir(LOGS_DIR), (
            f"Directory {LOGS_DIR} does not exist."
        )

    def test_logs_dir_permissions(self):
        perms = get_octal_permissions(LOGS_DIR)
        assert perms == 0o750, (
            f"logs/ directory has permissions {oct(perms)} ({stat.filemode(os.stat(LOGS_DIR).st_mode)}), "
            f"expected 0o750 (drwxr-x---). "
            f"logs/ must be writable only by owner, readable/executable by group, no permissions for others."
        )


class TestSecurityAuditFile:
    def test_audit_file_exists(self):
        assert os.path.isfile(AUDIT_FILE), (
            f"security_audit.txt does not exist at {AUDIT_FILE}. "
            f"The audit file must be created after fixing permissions."
        )

    def test_audit_file_content_exact(self):
        with open(AUDIT_FILE, 'r') as f:
            content = f.read()

        # Accept content with or without a single trailing newline
        content_stripped = content.rstrip('\n')
        expected_stripped = EXPECTED_AUDIT_CONTENT.rstrip('\n')

        assert content_stripped == expected_stripped, (
            f"security_audit.txt content does not match expected.\n"
            f"Expected:\n{repr(EXPECTED_AUDIT_CONTENT)}\n\n"
            f"Got:\n{repr(content)}\n\n"
            f"Differences:\n"
            + _diff_lines(expected_stripped, content_stripped)
        )

    def test_audit_file_no_trailing_spaces(self):
        with open(AUDIT_FILE, 'r') as f:
            lines = f.readlines()
        for i, line in enumerate(lines, 1):
            stripped = line.rstrip('\n')
            assert stripped == stripped.rstrip(), (
                f"Line {i} in security_audit.txt has trailing whitespace: {repr(line)}"
            )

    def test_audit_file_line_count(self):
        with open(AUDIT_FILE, 'r') as f:
            content = f.read()
        # Strip a single trailing newline if present, then count lines
        content_stripped = content.rstrip('\n')
        lines = content_stripped.split('\n')
        assert len(lines) == 7, (
            f"security_audit.txt should have 7 lines (including STATUS: SECURED), "
            f"but has {len(lines)} lines. Content: {repr(content)}"
        )

    def test_audit_file_header(self):
        with open(AUDIT_FILE, 'r') as f:
            lines = f.read().rstrip('\n').split('\n')
        assert lines[0] == "DEPLOYMENT SECURITY AUDIT", (
            f"First line of security_audit.txt is wrong.\n"
            f"Expected: 'DEPLOYMENT SECURITY AUDIT'\n"
            f"Got: {repr(lines[0])}"
        )

    def test_audit_file_separator(self):
        with open(AUDIT_FILE, 'r') as f:
            lines = f.read().rstrip('\n').split('\n')
        assert lines[1] == "=========================", (
            f"Second line of security_audit.txt is wrong.\n"
            f"Expected: '========================='\n"
            f"Got: {repr(lines[1])}"
        )

    def test_audit_file_start_sh_entry(self):
        with open(AUDIT_FILE, 'r') as f:
            lines = f.read().rstrip('\n').split('\n')
        assert lines[2] == "start.sh: -rwxr-x---", (
            f"start.sh entry in security_audit.txt is wrong.\n"
            f"Expected: 'start.sh: -rwxr-x---'\n"
            f"Got: {repr(lines[2])}"
        )

    def test_audit_file_db_conf_entry(self):
        with open(AUDIT_FILE, 'r') as f:
            lines = f.read().rstrip('\n').split('\n')
        assert lines[3] == "config/db.conf: -rw-------", (
            f"config/db.conf entry in security_audit.txt is wrong.\n"
            f"Expected: 'config/db.conf: -rw-------'\n"
            f"Got: {repr(lines[3])}"
        )

    def test_audit_file_app_conf_entry(self):
        with open(AUDIT_FILE, 'r') as f:
            lines = f.read().rstrip('\n').split('\n')
        assert lines[4] == "config/app.conf: -rw-r-----", (
            f"config/app.conf entry in security_audit.txt is wrong.\n"
            f"Expected: 'config/app.conf: -rw-r-----'\n"
            f"Got: {repr(lines[4])}"
        )

    def test_audit_file_logs_entry(self):
        with open(AUDIT_FILE, 'r') as f:
            lines = f.read().rstrip('\n').split('\n')
        assert lines[5] == "logs/: drwxr-x---", (
            f"logs/ entry in security_audit.txt is wrong.\n"
            f"Expected: 'logs/: drwxr-x---'\n"
            f"Got: {repr(lines[5])}"
        )

    def test_audit_file_status_line(self):
        with open(AUDIT_FILE, 'r') as f:
            lines = f.read().rstrip('\n').split('\n')
        assert lines[6] == "STATUS: SECURED", (
            f"STATUS line in security_audit.txt is wrong.\n"
            f"Expected: 'STATUS: SECURED'\n"
            f"Got: {repr(lines[6])}"
        )

    def test_audit_file_uses_relative_paths(self):
        with open(AUDIT_FILE, 'r') as f:
            content = f.read()
        assert "/home/user/deploy" not in content, (
            f"security_audit.txt contains absolute paths. "
            f"File paths in the audit must be relative (e.g., 'start.sh', not '/home/user/deploy/start.sh')."
        )


def _diff_lines(expected, got):
    """Helper to show line-by-line differences."""
    expected_lines = expected.split('\n')
    got_lines = got.split('\n')
    diffs = []
    max_lines = max(len(expected_lines), len(got_lines))
    for i in range(max_lines):
        exp_line = expected_lines[i] if i < len(expected_lines) else "<missing>"
        got_line = got_lines[i] if i < len(got_lines) else "<missing>"
        if exp_line != got_line:
            diffs.append(f"  Line {i+1}: expected {repr(exp_line)}, got {repr(got_line)}")
    return '\n'.join(diffs) if diffs else "No line differences found (check whitespace/encoding)"