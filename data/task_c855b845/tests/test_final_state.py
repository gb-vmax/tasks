# test_final_state.py

"""
Pytest suite to validate the final state after DevOps troubleshooting task:
- List all installed packages in /home/user/devops/logs/installed_packages.txt
- Log broken/partially installed packages in /home/user/devops/logs/package_issues.log
- Ensure /home/user/devops/logs/ exists, owned and writable by 'user'
"""

import os
import stat
import pwd
import grp
import subprocess
import pytest

LOGS_DIR = "/home/user/devops/logs/"
INSTALLED_PKGS_FILE = os.path.join(LOGS_DIR, "installed_packages.txt")
PKG_ISSUES_FILE = os.path.join(LOGS_DIR, "package_issues.log")
USER = "user"

def get_owner_username(path):
    st = os.stat(path)
    return pwd.getpwuid(st.st_uid).pw_name

def is_writable_by_user(path, username):
    st = os.stat(path)
    # User
    if st.st_uid == pwd.getpwnam(username).pw_uid:
        return bool(st.st_mode & stat.S_IWUSR)
    # Group
    user_groups = [g.gr_gid for g in [grp.getgrgid(gid) for gid in os.getgrouplist(username, st.st_gid)]]
    if st.st_gid in user_groups:
        return bool(st.st_mode & stat.S_IWGRP)
    # Others
    return bool(st.st_mode & stat.S_IWOTH)

def get_installed_packages():
    """Return a list of installed package names using dpkg-query."""
    try:
        out = subprocess.check_output(
            ["dpkg-query", "-W", "-f", "${Package}\n"], text=True
        )
        pkgs = [line.strip() for line in out.strip().splitlines() if line.strip()]
        return pkgs
    except Exception as e:
        pytest.skip(f"Cannot get installed packages: {e}")

def get_broken_packages():
    """Return a list of broken or partially installed package names using dpkg --audit."""
    try:
        out = subprocess.check_output(
            ["dpkg", "--audit"], text=True
        )
        # dpkg --audit output: look for lines like "  package-name: ..."
        pkgs = []
        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue
            if ':' in line:
                pkg = line.split(':', 1)[0].strip()
                if pkg and all(c not in pkg for c in ' \t'):
                    pkgs.append(pkg)
        return pkgs
    except subprocess.CalledProcessError as e:
        # Non-zero exit status, but still with output
        out = e.output
        pkgs = []
        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue
            if ':' in line:
                pkg = line.split(':', 1)[0].strip()
                if pkg and all(c not in pkg for c in ' \t'):
                    pkgs.append(pkg)
        return pkgs
    except Exception as e:
        pytest.skip(f"Cannot check for broken packages: {e}")

def test_logs_directory_exists_and_owned_and_writable():
    """Check /home/user/devops/logs/ exists, is directory, owned and writable by 'user'."""
    assert os.path.exists(LOGS_DIR), (
        f"Directory '{LOGS_DIR}' does not exist."
    )
    assert os.path.isdir(LOGS_DIR), (
        f"'{LOGS_DIR}' exists but is not a directory."
    )
    owner = get_owner_username(LOGS_DIR)
    assert owner == USER, (
        f"Directory '{LOGS_DIR}' is owned by '{owner}', should be owned by '{USER}'."
    )
    assert is_writable_by_user(LOGS_DIR, USER), (
        f"Directory '{LOGS_DIR}' is not writable by '{USER}'."
    )

def test_installed_packages_file_exists_and_correct():
    """Check installed_packages.txt exists and contains correct, sorted package names only."""
    assert os.path.exists(INSTALLED_PKGS_FILE), (
        f"File '{INSTALLED_PKGS_FILE}' does not exist."
    )
    # Read actual file contents
    with open(INSTALLED_PKGS_FILE, "r") as f:
        file_pkgs = [line.rstrip('\n') for line in f]
    # No empty lines
    assert all(line.strip() for line in file_pkgs), (
        f"'{INSTALLED_PKGS_FILE}' contains empty or whitespace-only lines."
    )
    # Get actual installed packages
    sys_pkgs = get_installed_packages()
    sys_pkgs_sorted = sorted(sys_pkgs)
    assert file_pkgs == sys_pkgs_sorted, (
        f"'{INSTALLED_PKGS_FILE}' contents do not match installed packages list.\n"
        f"Expected (first 10): {sys_pkgs_sorted[:10]}\n"
        f"Actual (first 10):   {file_pkgs[:10]}"
    )

def test_package_issues_log_exists_and_correct():
    """Check package_issues.log exists and has correct content depending on broken pkgs."""
    assert os.path.exists(PKG_ISSUES_FILE), (
        f"File '{PKG_ISSUES_FILE}' does not exist."
    )
    with open(PKG_ISSUES_FILE, "r") as f:
        lines = [line.rstrip('\n') for line in f]
    # No empty lines except possibly a single line for "No broken packages found."
    lines = [line for line in lines if line.strip()]
    broken_pkgs = get_broken_packages()
    if not broken_pkgs:
        assert lines == ["No broken packages found."], (
            f"'{PKG_ISSUES_FILE}' should contain exactly 'No broken packages found.'\n"
            f"Found instead: {lines!r}"
        )
    else:
        expected_lines = [f"[BROKEN] {pkg}" for pkg in broken_pkgs]
        assert lines == expected_lines, (
            f"'{PKG_ISSUES_FILE}' does not correctly list broken packages.\n"
            f"Expected: {expected_lines!r}\nActual:   {lines!r}"
        )
        # Check for no extra lines
        assert len(lines) == len(broken_pkgs), (
            f"'{PKG_ISSUES_FILE}' has extra or missing lines for broken packages."
        )