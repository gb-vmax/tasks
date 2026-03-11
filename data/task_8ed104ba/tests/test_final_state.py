# test_final_state.py

import os
import pwd
import grp
import stat
import subprocess
import pytest


HOME = "/home/user"
ALERTSYS = os.path.join(HOME, "alertsys")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def stat_ugp(path):
    """Return (owner_name, group_name, octal_perms_str) for a path."""
    result = subprocess.run(
        ["stat", "-c", "%U %G %a", path],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"stat failed for {path}: {result.stderr}"
    )
    parts = result.stdout.strip().split()
    assert len(parts) == 3, f"Unexpected stat output for {path}: {result.stdout!r}"
    return parts[0], parts[1], parts[2]


def get_user_groups(username):
    """Return a list of group names that username belongs to."""
    result = subprocess.run(
        ["id", "-Gn", username],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"'id -Gn {username}' failed: {result.stderr}"
    )
    return result.stdout.strip().split()


# ---------------------------------------------------------------------------
# Step 1: Group and Users
# ---------------------------------------------------------------------------

def test_group_monitors_exists():
    result = subprocess.run(
        ["getent", "group", "monitors"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        "Group 'monitors' must exist, but 'getent group monitors' returned nothing."
    )


def test_user_alertagent_exists():
    result = subprocess.run(
        ["id", "alertagent"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        "User 'alertagent' must exist, but 'id alertagent' failed."
    )


def test_user_logreader_exists():
    result = subprocess.run(
        ["id", "logreader"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        "User 'logreader' must exist, but 'id logreader' failed."
    )


def test_alertagent_shell():
    pw = pwd.getpwnam("alertagent")
    assert pw.pw_shell == "/usr/sbin/nologin", (
        f"alertagent shell must be '/usr/sbin/nologin', got '{pw.pw_shell}'"
    )


def test_logreader_shell():
    pw = pwd.getpwnam("logreader")
    assert pw.pw_shell == "/usr/sbin/nologin", (
        f"logreader shell must be '/usr/sbin/nologin', got '{pw.pw_shell}'"
    )


def test_alertagent_no_home():
    pw = pwd.getpwnam("alertagent")
    # System users with --no-create-home typically have /nonexistent or /
    # The key check is that no home directory was created
    home_dir = pw.pw_dir
    # It should not be a real user home directory that exists as a personal dir
    # Acceptable: doesn't exist, or is /nonexistent, or is /
    if home_dir and home_dir not in ("/", "/nonexistent", "/dev/null"):
        assert not os.path.isdir(home_dir), (
            f"alertagent home directory '{home_dir}' should not exist "
            "(user created with --no-create-home)"
        )


def test_logreader_no_home():
    pw = pwd.getpwnam("logreader")
    home_dir = pw.pw_dir
    if home_dir and home_dir not in ("/", "/nonexistent", "/dev/null"):
        assert not os.path.isdir(home_dir), (
            f"logreader home directory '{home_dir}' should not exist "
            "(user created with --no-create-home)"
        )


def test_alertagent_in_monitors_group():
    groups = get_user_groups("alertagent")
    assert "monitors" in groups, (
        f"alertagent must be a member of 'monitors', but groups are: {groups}"
    )


def test_logreader_in_monitors_group():
    groups = get_user_groups("logreader")
    assert "monitors" in groups, (
        f"logreader must be a member of 'monitors', but groups are: {groups}"
    )


# ---------------------------------------------------------------------------
# Step 2: Directory structure
# ---------------------------------------------------------------------------

def test_dir_configs_exists():
    path = os.path.join(ALERTSYS, "configs")
    assert os.path.isdir(path), f"Directory '{path}' must exist."


def test_dir_logs_exists():
    path = os.path.join(ALERTSYS, "logs")
    assert os.path.isdir(path), f"Directory '{path}' must exist."


def test_dir_reports_exists():
    path = os.path.join(ALERTSYS, "reports")
    assert os.path.isdir(path), f"Directory '{path}' must exist."


def test_dir_configs_owner_group_perms():
    path = "/home/user/alertsys/configs"
    owner, group, perms = stat_ugp(path)
    assert owner == "alertagent", (
        f"{path}: expected owner 'alertagent', got '{owner}'"
    )
    assert group == "monitors", (
        f"{path}: expected group 'monitors', got '{group}'"
    )
    assert perms == "750", (
        f"{path}: expected permissions '750', got '{perms}'"
    )


def test_dir_logs_owner_group_perms():
    path = "/home/user/alertsys/logs"
    owner, group, perms = stat_ugp(path)
    assert owner == "logreader", (
        f"{path}: expected owner 'logreader', got '{owner}'"
    )
    assert group == "monitors", (
        f"{path}: expected group 'monitors', got '{group}'"
    )
    assert perms == "770", (
        f"{path}: expected permissions '770', got '{perms}'"
    )


def test_dir_reports_owner_group_perms():
    path = "/home/user/alertsys/reports"
    owner, group, perms = stat_ugp(path)
    assert owner == "user", (
        f"{path}: expected owner 'user', got '{owner}'"
    )
    assert group == "monitors", (
        f"{path}: expected group 'monitors', got '{group}'"
    )
    assert perms == "775", (
        f"{path}: expected permissions '775', got '{perms}'"
    )


# ---------------------------------------------------------------------------
# Step 3: Files — existence, ownership, permissions, content
# ---------------------------------------------------------------------------

# threshold.conf
THRESHOLD_CONF = "/home/user/alertsys/configs/threshold.conf"
THRESHOLD_CONTENT = "cpu_threshold=85\nmem_threshold=90\ndisk_threshold=80\n"

def test_threshold_conf_exists():
    assert os.path.isfile(THRESHOLD_CONF), (
        f"File '{THRESHOLD_CONF}' must exist."
    )


def test_threshold_conf_owner_group_perms():
    owner, group, perms = stat_ugp(THRESHOLD_CONF)
    assert owner == "alertagent", (
        f"{THRESHOLD_CONF}: expected owner 'alertagent', got '{owner}'"
    )
    assert group == "monitors", (
        f"{THRESHOLD_CONF}: expected group 'monitors', got '{group}'"
    )
    assert perms == "640", (
        f"{THRESHOLD_CONF}: expected permissions '640', got '{perms}'"
    )


def test_threshold_conf_content():
    with open(THRESHOLD_CONF, "r") as f:
        content = f.read()
    assert content == THRESHOLD_CONTENT, (
        f"{THRESHOLD_CONF}: content mismatch.\n"
        f"Expected: {THRESHOLD_CONTENT!r}\n"
        f"Got:      {content!r}"
    )


# alert.log
ALERT_LOG = "/home/user/alertsys/logs/alert.log"
ALERT_LOG_CONTENT = (
    "2024-06-01T08:00:00Z INFO monitoring started\n"
    "2024-06-01T08:15:22Z WARN cpu usage at 87%\n"
    "2024-06-01T08:16:01Z ALERT disk usage at 83%\n"
)

def test_alert_log_exists():
    assert os.path.isfile(ALERT_LOG), (
        f"File '{ALERT_LOG}' must exist."
    )


def test_alert_log_owner_group_perms():
    owner, group, perms = stat_ugp(ALERT_LOG)
    assert owner == "logreader", (
        f"{ALERT_LOG}: expected owner 'logreader', got '{owner}'"
    )
    assert group == "monitors", (
        f"{ALERT_LOG}: expected group 'monitors', got '{group}'"
    )
    assert perms == "660", (
        f"{ALERT_LOG}: expected permissions '660', got '{perms}'"
    )


def test_alert_log_content():
    with open(ALERT_LOG, "r") as f:
        content = f.read()
    assert content == ALERT_LOG_CONTENT, (
        f"{ALERT_LOG}: content mismatch.\n"
        f"Expected: {ALERT_LOG_CONTENT!r}\n"
        f"Got:      {content!r}"
    )


# daily_summary.txt
DAILY_SUMMARY = "/home/user/alertsys/reports/daily_summary.txt"
DAILY_SUMMARY_CONTENT = (
    "Date: 2024-06-01\n"
    "Alerts triggered: 2\n"
    "Status: review required\n"
)

def test_daily_summary_exists():
    assert os.path.isfile(DAILY_SUMMARY), (
        f"File '{DAILY_SUMMARY}' must exist."
    )


def test_daily_summary_owner_group_perms():
    owner, group, perms = stat_ugp(DAILY_SUMMARY)
    assert owner == "user", (
        f"{DAILY_SUMMARY}: expected owner 'user', got '{owner}'"
    )
    assert group == "monitors", (
        f"{DAILY_SUMMARY}: expected group 'monitors', got '{group}'"
    )
    assert perms == "664", (
        f"{DAILY_SUMMARY}: expected permissions '664', got '{perms}'"
    )


def test_daily_summary_content():
    with open(DAILY_SUMMARY, "r") as f:
        content = f.read()
    assert content == DAILY_SUMMARY_CONTENT, (
        f"{DAILY_SUMMARY}: content mismatch.\n"
        f"Expected: {DAILY_SUMMARY_CONTENT!r}\n"
        f"Got:      {content!r}"
    )


# ---------------------------------------------------------------------------
# Step 4: Audit report
# ---------------------------------------------------------------------------

AUDIT_REPORT = "/home/user/alertsys/audit_report.txt"
AUDIT_REPORT_CONTENT = (
    "=== ALERTSYS PERMISSION AUDIT ===\n"
    "\n"
    "[DIRECTORIES]\n"
    "path=/home/user/alertsys/configs owner=alertagent group=monitors perms=750\n"
    "path=/home/user/alertsys/logs owner=logreader group=monitors perms=770\n"
    "path=/home/user/alertsys/reports owner=user group=monitors perms=775\n"
    "\n"
    "[FILES]\n"
    "path=/home/user/alertsys/configs/threshold.conf owner=alertagent group=monitors perms=640\n"
    "path=/home/user/alertsys/logs/alert.log owner=logreader group=monitors perms=660\n"
    "path=/home/user/alertsys/reports/daily_summary.txt owner=user group=monitors perms=664\n"
    "\n"
    "[SUMMARY]\n"
    "total_directories=3\n"
    "total_files=3\n"
    "group_verified=monitors\n"
)


def test_audit_report_exists():
    assert os.path.isfile(AUDIT_REPORT), (
        f"Audit report '{AUDIT_REPORT}' must exist."
    )


def test_audit_report_owner_group_perms():
    owner, group, perms = stat_ugp(AUDIT_REPORT)
    assert owner == "user", (
        f"{AUDIT_REPORT}: expected owner 'user', got '{owner}'"
    )
    assert group == "user", (
        f"{AUDIT_REPORT}: expected group 'user', got '{group}'"
    )
    assert perms == "644", (
        f"{AUDIT_REPORT}: expected permissions '644', got '{perms}'"
    )


def test_audit_report_content():
    with open(AUDIT_REPORT, "r") as f:
        content = f.read()
    assert content == AUDIT_REPORT_CONTENT, (
        f"{AUDIT_REPORT}: content mismatch.\n"
        f"Expected:\n{AUDIT_REPORT_CONTENT}\n"
        f"Got:\n{content}\n"
        f"---\n"
        f"Expected repr: {AUDIT_REPORT_CONTENT!r}\n"
        f"Got repr:      {content!r}"
    )


def test_audit_report_line_by_line():
    """Detailed line-by-line check to give precise failure messages."""
    with open(AUDIT_REPORT, "r") as f:
        content = f.read()

    expected_lines = AUDIT_REPORT_CONTENT.splitlines(keepends=True)
    actual_lines = content.splitlines(keepends=True)

    assert len(actual_lines) == len(expected_lines), (
        f"{AUDIT_REPORT}: expected {len(expected_lines)} lines, "
        f"got {len(actual_lines)} lines.\n"
        f"Full content repr: {content!r}"
    )

    for i, (exp, got) in enumerate(zip(expected_lines, actual_lines), start=1):
        assert exp == got, (
            f"{AUDIT_REPORT}: line {i} mismatch.\n"
            f"Expected: {exp!r}\n"
            f"Got:      {got!r}"
        )