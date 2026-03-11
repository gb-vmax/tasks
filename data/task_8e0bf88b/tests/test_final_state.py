# test_final_state.py

import os
import stat
import pytest

FILESERVER = "/home/user/fileserver"
ARCHIVE = "/home/user/fileserver/archive"
AUDIT_LOG = "/home/user/audit.log"


# ── Step 1: Old .tmp files must be deleted ────────────────────────────────────

@pytest.mark.parametrize("path", [
    "/home/user/fileserver/tmp/session_old.tmp",
    "/home/user/fileserver/tmp/cache_old.tmp",
    "/home/user/fileserver/uploads/scratch_old.tmp",
])
def test_old_tmp_files_deleted(path):
    assert not os.path.exists(path), (
        f"Old .tmp file should have been deleted but still exists: {path}"
    )


# ── Step 1: Recent .tmp file must survive ─────────────────────────────────────

def test_recent_tmp_file_survives():
    path = "/home/user/fileserver/tmp/session_new.tmp"
    assert os.path.isfile(path), (
        f"Recent .tmp file should NOT have been deleted but is missing: {path}"
    )


def test_recent_tmp_file_content():
    path = "/home/user/fileserver/tmp/session_new.tmp"
    with open(path) as f:
        content = f.read().strip()
    assert content == "new session", (
        f"Content of {path} changed unexpectedly: got {content!r}"
    )


# ── Step 2: World-writable .sh files must no longer be world-writable ─────────

@pytest.mark.parametrize("path", [
    "/home/user/fileserver/scripts/deploy.sh",
    "/home/user/fileserver/scripts/backup.sh",
])
def test_formerly_world_writable_sh_not_world_writable(path):
    assert os.path.isfile(path), f"Script file is missing: {path}"
    mode = os.stat(path).st_mode
    is_world_writable = bool(mode & stat.S_IWOTH)
    assert not is_world_writable, (
        f"File {path} should NOT be world-writable after chmod o-w, "
        f"but current mode is {oct(mode)}"
    )


# ── Step 2: Non-world-writable .sh file must be unchanged ─────────────────────

def test_monitor_sh_still_exists():
    path = "/home/user/fileserver/scripts/monitor.sh"
    assert os.path.isfile(path), f"monitor.sh should still exist but is missing: {path}"


def test_monitor_sh_permissions_unchanged():
    path = "/home/user/fileserver/scripts/monitor.sh"
    mode = os.stat(path).st_mode & 0o777
    assert mode == 0o755, (
        f"monitor.sh permissions should be unchanged (0755) but are now {oct(mode)}"
    )


def test_monitor_sh_not_world_writable():
    path = "/home/user/fileserver/scripts/monitor.sh"
    mode = os.stat(path).st_mode
    assert not bool(mode & stat.S_IWOTH), (
        f"monitor.sh should not be world-writable; mode is {oct(mode)}"
    )


# ── Step 3: Old .report files must be archived ────────────────────────────────

@pytest.mark.parametrize("filename,expected_content", [
    ("q1_sales.report", "Q1 Sales"),
    ("q2_sales.report", "Q2 Sales"),
    ("system_health.report", "Health OK"),
])
def test_old_report_in_archive(filename, expected_content):
    path = os.path.join(ARCHIVE, filename)
    assert os.path.isfile(path), (
        f"Old report should have been moved to archive but is missing: {path}"
    )
    with open(path) as f:
        content = f.read().strip()
    assert content == expected_content, (
        f"Content of archived {path} is wrong: expected {expected_content!r}, got {content!r}"
    )


@pytest.mark.parametrize("path", [
    "/home/user/fileserver/reports/q1_sales.report",
    "/home/user/fileserver/reports/q2_sales.report",
    "/home/user/fileserver/reports/system_health.report",
])
def test_old_report_removed_from_original_location(path):
    assert not os.path.exists(path), (
        f"Old report should have been moved out of reports/ but still exists: {path}"
    )


# ── Step 3: Recent .report file must stay in place ────────────────────────────

def test_recent_report_stays_in_reports():
    path = "/home/user/fileserver/reports/q3_sales.report"
    assert os.path.isfile(path), (
        f"Recent report should NOT have been moved but is missing: {path}"
    )


def test_recent_report_content():
    path = "/home/user/fileserver/reports/q3_sales.report"
    with open(path) as f:
        content = f.read().strip()
    assert content == "Q3 Sales", (
        f"Content of {path} changed unexpectedly: got {content!r}"
    )


def test_recent_report_not_in_archive():
    path = os.path.join(ARCHIVE, "q3_sales.report")
    assert not os.path.exists(path), (
        f"Recent report q3_sales.report should NOT be in archive but was found at: {path}"
    )


# ── Step 4: Audit log existence and exact content ─────────────────────────────

def test_audit_log_exists():
    assert os.path.isfile(AUDIT_LOG), (
        f"Audit log does not exist at: {AUDIT_LOG}"
    )


def test_audit_log_exact_content():
    expected = (
        "=== REMAINING TMP FILES ===\n"
        "/home/user/fileserver/tmp/session_new.tmp\n"
        "=== FIXED SCRIPTS ===\n"
        "/home/user/fileserver/scripts/backup.sh\n"
        "/home/user/fileserver/scripts/deploy.sh\n"
        "/home/user/fileserver/scripts/monitor.sh\n"
        "=== ARCHIVED REPORTS ===\n"
        "/home/user/fileserver/archive/q1_sales.report\n"
        "/home/user/fileserver/archive/q2_sales.report\n"
        "/home/user/fileserver/archive/system_health.report\n"
    )
    with open(AUDIT_LOG) as f:
        actual = f.read()
    assert actual == expected, (
        f"Audit log content does not match expected.\n"
        f"--- EXPECTED ---\n{expected!r}\n"
        f"--- ACTUAL ---\n{actual!r}"
    )


def test_audit_log_section_remaining_tmp():
    with open(AUDIT_LOG) as f:
        content = f.read()
    assert "=== REMAINING TMP FILES ===" in content, (
        "Audit log is missing the '=== REMAINING TMP FILES ===' header"
    )
    lines = content.splitlines()
    header_idx = lines.index("=== REMAINING TMP FILES ===")
    # The line immediately after the header should be the surviving tmp file
    assert header_idx + 1 < len(lines), (
        "Nothing follows the REMAINING TMP FILES header"
    )
    assert lines[header_idx + 1] == "/home/user/fileserver/tmp/session_new.tmp", (
        f"Expected session_new.tmp after REMAINING TMP FILES header, "
        f"got: {lines[header_idx + 1]!r}"
    )


def test_audit_log_section_fixed_scripts():
    with open(AUDIT_LOG) as f:
        lines = f.read().splitlines()
    header_idx = lines.index("=== FIXED SCRIPTS ===")
    script_lines = []
    for line in lines[header_idx + 1:]:
        if line.startswith("==="):
            break
        script_lines.append(line)
    expected_scripts = sorted([
        "/home/user/fileserver/scripts/backup.sh",
        "/home/user/fileserver/scripts/deploy.sh",
        "/home/user/fileserver/scripts/monitor.sh",
    ])
    assert script_lines == expected_scripts, (
        f"FIXED SCRIPTS section content mismatch.\n"
        f"Expected: {expected_scripts}\n"
        f"Got: {script_lines}"
    )


def test_audit_log_section_archived_reports():
    with open(AUDIT_LOG) as f:
        lines = f.read().splitlines()
    header_idx = lines.index("=== ARCHIVED REPORTS ===")
    report_lines = []
    for line in lines[header_idx + 1:]:
        if line.startswith("==="):
            break
        report_lines.append(line)
    expected_reports = sorted([
        "/home/user/fileserver/archive/q1_sales.report",
        "/home/user/fileserver/archive/q2_sales.report",
        "/home/user/fileserver/archive/system_health.report",
    ])
    assert report_lines == expected_reports, (
        f"ARCHIVED REPORTS section content mismatch.\n"
        f"Expected: {expected_reports}\n"
        f"Got: {report_lines}"
    )


def test_audit_log_section_order():
    with open(AUDIT_LOG) as f:
        lines = f.read().splitlines()
    headers = [l for l in lines if l.startswith("===")]
    expected_headers = [
        "=== REMAINING TMP FILES ===",
        "=== FIXED SCRIPTS ===",
        "=== ARCHIVED REPORTS ===",
    ]
    assert headers == expected_headers, (
        f"Audit log headers are in wrong order or missing.\n"
        f"Expected: {expected_headers}\n"
        f"Got: {headers}"
    )


def test_audit_log_no_blank_lines_between_sections():
    with open(AUDIT_LOG) as f:
        content = f.read()
    lines = content.splitlines()
    # Check that no blank lines exist anywhere in the file
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert blank_lines == [], (
        f"Audit log contains blank lines at line numbers: {blank_lines}. "
        f"No blank lines should appear between sections or at the end."
    )


def test_audit_log_ends_with_newline():
    with open(AUDIT_LOG, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        "Audit log should end with a newline character"
    )


def test_audit_log_no_old_tmp_files_listed():
    with open(AUDIT_LOG) as f:
        content = f.read()
    for fname in ["session_old.tmp", "cache_old.tmp", "scratch_old.tmp"]:
        assert fname not in content, (
            f"Audit log should not reference deleted file {fname}, but it does"
        )


def test_audit_log_no_unarachived_reports_listed():
    """q3_sales.report should not appear in the ARCHIVED REPORTS section."""
    with open(AUDIT_LOG) as f:
        lines = f.read().splitlines()
    header_idx = lines.index("=== ARCHIVED REPORTS ===")
    report_lines = []
    for line in lines[header_idx + 1:]:
        if line.startswith("==="):
            break
        report_lines.append(line)
    for line in report_lines:
        assert "q3_sales" not in line, (
            f"q3_sales.report should NOT be in ARCHIVED REPORTS section, "
            f"but found: {line!r}"
        )