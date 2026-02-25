# test_final_state.py

import os
import stat
import pwd
import grp
import pytest

DEPLOY_SH = "/home/user/scripts/deploy.sh"
LOG_FILE = "/home/user/permission_check.log"
EXPECTED_PERMISSIONS = "-rw-------"
EXPECTED_MODE = 0o600  # rw-------


def test_deploy_sh_exists():
    assert os.path.isfile(DEPLOY_SH), (
        f"Required file missing: {DEPLOY_SH}. The file must exist after the task is completed."
    )


def test_deploy_sh_permissions_restricted():
    st = os.stat(DEPLOY_SH)
    mode = stat.S_IMODE(st.st_mode)
    actual_mode_str = stat.filemode(st.st_mode)
    assert mode == EXPECTED_MODE, (
        f"{DEPLOY_SH} permissions incorrect: expected {EXPECTED_PERMISSIONS} (600), "
        f"but found {actual_mode_str}. Only the owner must have read/write permissions; "
        f"group and others must have no permissions."
    )


def test_deploy_sh_ownership():
    st = os.stat(DEPLOY_SH)
    uid = st.st_uid
    gid = st.st_gid
    try:
        user = pwd.getpwuid(uid).pw_name
        group = grp.getgrgid(gid).gr_name
    except KeyError:
        pytest.fail(f"Cannot resolve UID/GID for {DEPLOY_SH}; got uid={uid}, gid={gid}")
    assert user == "user", (
        f"{DEPLOY_SH} must be owned by user 'user' after the task, but owner is '{user}'"
    )
    assert group == "user", (
        f"{DEPLOY_SH} must be owned by group 'user' after the task, but group is '{group}'"
    )


def test_permission_check_log_exists():
    assert os.path.isfile(LOG_FILE), (
        f"Log file {LOG_FILE} was not found. You must generate this file after completing the task."
    )


def test_permission_check_log_contents():
    """
    The log file must contain exactly one line:
    /home/user/scripts/deploy.sh permissions: -rw-------
    No leading/trailing whitespace, no extra lines.
    """
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    expected_line = f"{DEPLOY_SH} permissions: {EXPECTED_PERMISSIONS}\n"

    if len(lines) != 1:
        pytest.fail(
            f"{LOG_FILE} must contain exactly one line.\n"
            f"Expected: {expected_line!r}\n"
            f"Found {len(lines)} line(s): {lines}"
        )

    actual_line = lines[0]
    if actual_line != expected_line:
        # Give detailed feedback on what is wrong
        msg = (
            f"{LOG_FILE} contents incorrect.\n"
            f"Expected exactly:\n{expected_line!r}\n"
            f"But found:\n{actual_line!r}\n"
        )
        # Check for common mistakes
        if actual_line.strip() == expected_line.strip() and actual_line != expected_line:
            msg += (
                "It looks like there is a problem with line endings or whitespace. "
                "Check for extra or missing newline characters."
            )
        elif actual_line.startswith(" "):
            msg += "Log line has unexpected leading whitespace."
        elif actual_line.endswith(" \n") or actual_line.endswith(" "):
            msg += "Log line has unexpected trailing whitespace."
        pytest.fail(msg)