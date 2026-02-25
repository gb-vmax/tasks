# test_final_state.py

import os
import stat
import pwd
import pytest

HOME = "/home/user"
ALERTS_DIR = os.path.join(HOME, "alerts")
CONF_PATH = os.path.join(ALERTS_DIR, "service_alerts.conf")
LOG_PATH = os.path.join(ALERTS_DIR, "alert.log")

CONF_EXPECTED = [
    "THRESHOLD=85",
    "NOTIFY_EMAIL=on",
    "LOGFILE=/home/user/alerts/alert.log",
    "ENABLED=true",
]

LOG_EXPECTED = "[2024-06-11 12:00:00] ALERT: THRESHOLD exceeded (value: 92)"

def get_file_owner(path):
    return pwd.getpwuid(os.stat(path).st_uid).pw_name

def get_dir_owner(path):
    return pwd.getpwuid(os.stat(path).st_uid).pw_name

@pytest.mark.order(1)
def test_alerts_directory_exists_and_owned():
    assert os.path.isdir(ALERTS_DIR), (
        f"Directory {ALERTS_DIR} does not exist. "
        "You must create it at the absolute path /home/user/alerts/."
    )
    owner = get_dir_owner(ALERTS_DIR)
    assert owner == "user", (
        f"Directory {ALERTS_DIR} is owned by '{owner}', expected owner is 'user'."
    )

@pytest.mark.order(2)
def test_service_alerts_conf_exists_and_exact_content_and_permissions():
    assert os.path.isfile(CONF_PATH), (
        f"Configuration file {CONF_PATH} does not exist. "
        "You must create it at the absolute path /home/user/alerts/service_alerts.conf."
    )
    with open(CONF_PATH, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    assert lines == CONF_EXPECTED, (
        f"Configuration file {CONF_PATH} does not have the expected content.\n"
        "Expected (exactly):\n"
        + "\n".join(CONF_EXPECTED)
        + "\nFound:\n"
        + "\n".join(lines)
    )
    st = os.stat(CONF_PATH)
    mode = st.st_mode
    # Permissions: at least readable and writable by user
    assert mode & stat.S_IRUSR, (
        f"Configuration file {CONF_PATH} is not readable by 'user'."
    )
    assert mode & stat.S_IWUSR, (
        f"Configuration file {CONF_PATH} is not writable by 'user'."
    )
    owner = get_file_owner(CONF_PATH)
    assert owner == "user", (
        f"Configuration file {CONF_PATH} is owned by '{owner}', expected owner is 'user'."
    )

@pytest.mark.order(3)
def test_alert_log_exists_exact_content_and_permissions():
    assert os.path.isfile(LOG_PATH), (
        f"Log file {LOG_PATH} does not exist. "
        "You must create it at the absolute path /home/user/alerts/alert.log."
    )
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    assert lines == [LOG_EXPECTED], (
        f"Log file {LOG_PATH} must contain exactly one line:\n{LOG_EXPECTED}\n"
        f"Found:\n" + "\n".join(lines)
    )
    st = os.stat(LOG_PATH)
    perm = stat.S_IMODE(st.st_mode)
    assert perm == 0o600, (
        f"Log file {LOG_PATH} permissions are {oct(perm)}, expected 0o600 (-rw-------)."
    )
    owner = get_file_owner(LOG_PATH)
    assert owner == "user", (
        f"Log file {LOG_PATH} is owned by '{owner}', expected owner is 'user'."
    )