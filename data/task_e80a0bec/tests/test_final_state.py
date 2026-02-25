# test_final_state.py

import os
import stat
import pwd
import pytest

ORDERSERVICE_DIR = "/home/user/microservices/orderservice"
START_SH = os.path.join(ORDERSERVICE_DIR, "start.sh")
PERMISSIONS_REPORT = os.path.join(ORDERSERVICE_DIR, "permissions_report.log")
USER = "user"

def _get_stat(path):
    try:
        return os.stat(path)
    except FileNotFoundError:
        return None

def _get_file_owner(path):
    st = _get_stat(path)
    if st is None:
        return None
    return pwd.getpwuid(st.st_uid).pw_name

def _read_report_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return lines

def test_start_sh_permissions_owner_only():
    st = _get_stat(START_SH)
    assert st is not None, f"File {START_SH} does not exist."
    mode = stat.S_IMODE(st.st_mode)
    assert mode == 0o700, (
        f"File {START_SH} permissions are {oct(mode)}, expected 0o700 (-rwx------)."
    )
    owner = _get_file_owner(START_SH)
    assert owner == USER, (
        f"File {START_SH} is owned by '{owner}', expected '{USER}'."
    )

def test_orderservice_dir_permissions_owner_only():
    st = _get_stat(ORDERSERVICE_DIR)
    assert st is not None, f"Directory {ORDERSERVICE_DIR} does not exist."
    mode = stat.S_IMODE(st.st_mode)
    assert mode == 0o700, (
        f"Directory {ORDERSERVICE_DIR} permissions are {oct(mode)}, expected 0o700 (drwx------)."
    )
    owner = _get_file_owner(ORDERSERVICE_DIR)
    assert owner == USER, (
        f"Directory {ORDERSERVICE_DIR} is owned by '{owner}', expected '{USER}'."
    )

def test_permissions_report_exists():
    assert os.path.exists(PERMISSIONS_REPORT), (
        f"File {PERMISSIONS_REPORT} does not exist. You must create it as specified."
    )
    assert os.path.isfile(PERMISSIONS_REPORT), (
        f"{PERMISSIONS_REPORT} exists but is not a regular file."
    )

def test_permissions_report_content_exact():
    # Get actual stat output for comparison
    from subprocess import check_output, CalledProcessError

    try:
        start_sh_stat = check_output(
            ['stat', '-c', '%A %n', START_SH], encoding='utf-8'
        ).strip()
        dir_stat = check_output(
            ['stat', '-c', '%A %n', ORDERSERVICE_DIR], encoding='utf-8'
        ).strip()
    except CalledProcessError as e:
        pytest.fail(f"Failed to run stat command: {e}")

    expected_lines = [
        start_sh_stat,
        dir_stat
    ]

    actual_lines = _read_report_lines(PERMISSIONS_REPORT)

    assert len(actual_lines) == 2, (
        f"{PERMISSIONS_REPORT} must contain exactly 2 lines, found {len(actual_lines)}."
    )

    if actual_lines != expected_lines:
        msg = (
            f"File {PERMISSIONS_REPORT} contents do not exactly match expected stat output.\n"
            f"Expected:\n"
            f"{expected_lines[0]!r}\n"
            f"{expected_lines[1]!r}\n"
            f"Actual:\n"
            f"{actual_lines[0]!r}\n"
            f"{actual_lines[1]!r}\n"
            f"Ensure you use the precise stat command format and no extra whitespace or lines."
        )
        pytest.fail(msg)