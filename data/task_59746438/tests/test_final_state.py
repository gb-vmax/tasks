# test_final_state.py

import os
import pwd
import grp
import stat
import pytest

ANALYTICS_DIR = "/home/user/team_projects/analytics_data"
REPORT_PATH = "/home/user/analytics_permission_report.txt"
EXPECTED_REPORT = "/home/user/team_projects/analytics_data analyst01 analytics drwxrwx---"

def get_permission_string(path):
    """Return a string like 'drwxrwx---' for the directory at path."""
    mode = os.stat(path).st_mode
    perms = ['d' if stat.S_ISDIR(mode) else '-']
    perms_map = (
        (stat.S_IRUSR, 'r'), (stat.S_IWUSR, 'w'), (stat.S_IXUSR, 'x'),
        (stat.S_IRGRP, 'r'), (stat.S_IWGRP, 'w'), (stat.S_IXGRP, 'x'),
        (stat.S_IROTH, 'r'), (stat.S_IWOTH, 'w'), (stat.S_IXOTH, 'x'),
    )
    for mask, char in perms_map:
        perms.append(char if mode & mask else '-')
    return ''.join(perms)

def user_exists(username):
    try:
        pwd.getpwnam(username)
        return True
    except KeyError:
        return False

def group_exists(groupname):
    try:
        grp.getgrnam(groupname)
        return True
    except KeyError:
        return False

def user_in_group(username, groupname):
    """Return True if user is a member of the group, either as primary or supplementary."""
    try:
        group = grp.getgrnam(groupname)
        user = pwd.getpwnam(username)
        in_gr_mem = username in group.gr_mem
        primary_gid = user.pw_gid == group.gr_gid
        return in_gr_mem or primary_gid
    except KeyError:
        return False

def get_dir_owner_group(path):
    st = os.stat(path)
    owner = pwd.getpwuid(st.st_uid).pw_name
    group = grp.getgrgid(st.st_gid).gr_name
    return owner, group

@pytest.mark.order(1)
def test_user_analyst01_exists():
    assert user_exists("analyst01"), (
        "User 'analyst01' does not exist in /etc/passwd. "
        "The user must be present after completing the task."
    )

@pytest.mark.order(2)
def test_group_analytics_exists():
    assert group_exists("analytics"), (
        "Group 'analytics' does not exist in /etc/group. "
        "The group must be present after completing the task."
    )

@pytest.mark.order(3)
def test_analyst01_is_member_of_analytics_group():
    assert user_in_group("analyst01", "analytics"), (
        "User 'analyst01' is not a member of group 'analytics'. "
        "Ensure 'analyst01' is a member (either as primary or supplementary group)."
    )

@pytest.mark.order(4)
def test_analytics_data_directory_exists():
    assert os.path.isdir(ANALYTICS_DIR), (
        f"Directory '{ANALYTICS_DIR}' does not exist. "
        "It must be created at the specified absolute path."
    )

@pytest.mark.order(5)
def test_analytics_data_directory_ownership():
    owner, group = get_dir_owner_group(ANALYTICS_DIR)
    assert owner == "analyst01", (
        f"Directory '{ANALYTICS_DIR}' is owned by '{owner}', "
        "expected owner 'analyst01'."
    )
    assert group == "analytics", (
        f"Directory '{ANALYTICS_DIR}' is in group '{group}', "
        "expected group 'analytics'."
    )

@pytest.mark.order(6)
def test_analytics_data_directory_permissions():
    perms = get_permission_string(ANALYTICS_DIR)
    assert perms == "drwxrwx---", (
        f"Directory '{ANALYTICS_DIR}' permissions are '{perms}', "
        "expected 'drwxrwx---' (octal 770: only owner and group have full access, others have none)."
    )

@pytest.mark.order(7)
def test_analytics_permission_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "It must be created after completing the task."
    )

@pytest.mark.order(8)
def test_analytics_permission_report_file_content():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) == 1, (
        f"Report file '{REPORT_PATH}' should contain exactly one line. "
        f"Found {len(lines)} lines. Ensure no extra blank lines."
    )
    line = lines[0].rstrip('\n')
    assert line == EXPECTED_REPORT, (
        f"Report file content is incorrect.\n"
        f"Expected: '{EXPECTED_REPORT}'\n"
        f"Found:    '{line}'\n"
        "Ensure the report is exactly as specified: absolute path, owner, group, permissions string, one space between fields, all on one line."
    )