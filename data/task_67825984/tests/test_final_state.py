# test_final_state.py

import os
import stat
import pytest

HOME = "/home/user"
ETL_SCRIPT = f"{HOME}/etl/run_pipeline.sh"
SYSTEMD_USER_DIR = f"{HOME}/.config/systemd/user"
SERVICE_FILE = f"{SYSTEMD_USER_DIR}/etl-pipeline.service"
TIMER_FILE = f"{SYSTEMD_USER_DIR}/etl-pipeline.timer"
TIMERS_TARGET_WANTS_DIR = f"{SYSTEMD_USER_DIR}/timers.target.wants"
SYMLINK = f"{TIMERS_TARGET_WANTS_DIR}/etl-pipeline.timer"

EXPECTED_SERVICE_CONTENT = """\
[Unit]
Description=ETL Pipeline Job

[Service]
Type=oneshot
ExecStart=/home/user/etl/run_pipeline.sh
"""

EXPECTED_TIMER_CONTENT = """\
[Unit]
Description=Run ETL Pipeline daily at 02:30

[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true

[Install]
WantedBy=timers.target
"""


# ---------------------------------------------------------------------------
# Pre-existing script checks
# ---------------------------------------------------------------------------

def test_etl_script_exists():
    assert os.path.isfile(ETL_SCRIPT), (
        f"ETL script not found at {ETL_SCRIPT}. "
        "The file /home/user/etl/run_pipeline.sh must exist."
    )


def test_etl_script_is_executable():
    assert os.access(ETL_SCRIPT, os.X_OK), (
        f"ETL script at {ETL_SCRIPT} is not executable. "
        "Run: chmod +x /home/user/etl/run_pipeline.sh"
    )


# ---------------------------------------------------------------------------
# Directory checks
# ---------------------------------------------------------------------------

def test_systemd_user_dir_exists():
    assert os.path.isdir(SYSTEMD_USER_DIR), (
        f"Directory {SYSTEMD_USER_DIR} does not exist. "
        "Create it with: mkdir -p /home/user/.config/systemd/user"
    )


def test_timers_target_wants_dir_exists():
    assert os.path.isdir(TIMERS_TARGET_WANTS_DIR), (
        f"Directory {TIMERS_TARGET_WANTS_DIR} does not exist. "
        "This directory is normally created by 'systemctl --user enable etl-pipeline.timer'. "
        "Make sure you ran that command."
    )


# ---------------------------------------------------------------------------
# Service file checks
# ---------------------------------------------------------------------------

def test_service_file_exists():
    assert os.path.isfile(SERVICE_FILE), (
        f"Service unit file not found at {SERVICE_FILE}. "
        "Create the file with the required content."
    )


def test_service_file_content():
    with open(SERVICE_FILE, "r") as f:
        content = f.read()

    # Normalize line endings for comparison
    content_stripped = content.strip()
    expected_stripped = EXPECTED_SERVICE_CONTENT.strip()

    assert content_stripped == expected_stripped, (
        f"Service file at {SERVICE_FILE} has unexpected content.\n"
        f"Expected:\n{EXPECTED_SERVICE_CONTENT}\n"
        f"Got:\n{content}\n"
        "Ensure the file matches the required structure exactly."
    )


def test_service_file_has_unit_section():
    with open(SERVICE_FILE, "r") as f:
        content = f.read()
    assert "[Unit]" in content, (
        f"Service file at {SERVICE_FILE} is missing the [Unit] section."
    )


def test_service_file_description():
    with open(SERVICE_FILE, "r") as f:
        content = f.read()
    assert "Description=ETL Pipeline Job" in content, (
        f"Service file at {SERVICE_FILE} is missing 'Description=ETL Pipeline Job' "
        "in the [Unit] section."
    )


def test_service_file_has_service_section():
    with open(SERVICE_FILE, "r") as f:
        content = f.read()
    assert "[Service]" in content, (
        f"Service file at {SERVICE_FILE} is missing the [Service] section."
    )


def test_service_file_type_oneshot():
    with open(SERVICE_FILE, "r") as f:
        content = f.read()
    assert "Type=oneshot" in content, (
        f"Service file at {SERVICE_FILE} is missing 'Type=oneshot' "
        "in the [Service] section."
    )


def test_service_file_exec_start():
    with open(SERVICE_FILE, "r") as f:
        content = f.read()
    assert "ExecStart=/home/user/etl/run_pipeline.sh" in content, (
        f"Service file at {SERVICE_FILE} is missing "
        "'ExecStart=/home/user/etl/run_pipeline.sh' in the [Service] section."
    )


# ---------------------------------------------------------------------------
# Timer file checks
# ---------------------------------------------------------------------------

def test_timer_file_exists():
    assert os.path.isfile(TIMER_FILE), (
        f"Timer unit file not found at {TIMER_FILE}. "
        "Create the file with the required content."
    )


def test_timer_file_content():
    with open(TIMER_FILE, "r") as f:
        content = f.read()

    content_stripped = content.strip()
    expected_stripped = EXPECTED_TIMER_CONTENT.strip()

    assert content_stripped == expected_stripped, (
        f"Timer file at {TIMER_FILE} has unexpected content.\n"
        f"Expected:\n{EXPECTED_TIMER_CONTENT}\n"
        f"Got:\n{content}\n"
        "Ensure the file matches the required structure exactly."
    )


def test_timer_file_has_unit_section():
    with open(TIMER_FILE, "r") as f:
        content = f.read()
    assert "[Unit]" in content, (
        f"Timer file at {TIMER_FILE} is missing the [Unit] section."
    )


def test_timer_file_description():
    with open(TIMER_FILE, "r") as f:
        content = f.read()
    assert "Description=Run ETL Pipeline daily at 02:30" in content, (
        f"Timer file at {TIMER_FILE} is missing "
        "'Description=Run ETL Pipeline daily at 02:30' in the [Unit] section."
    )


def test_timer_file_has_timer_section():
    with open(TIMER_FILE, "r") as f:
        content = f.read()
    assert "[Timer]" in content, (
        f"Timer file at {TIMER_FILE} is missing the [Timer] section."
    )


def test_timer_file_on_calendar():
    with open(TIMER_FILE, "r") as f:
        content = f.read()
    assert "OnCalendar=*-*-* 02:30:00" in content, (
        f"Timer file at {TIMER_FILE} is missing 'OnCalendar=*-*-* 02:30:00' "
        "in the [Timer] section."
    )


def test_timer_file_persistent():
    with open(TIMER_FILE, "r") as f:
        content = f.read()
    assert "Persistent=true" in content, (
        f"Timer file at {TIMER_FILE} is missing 'Persistent=true' "
        "in the [Timer] section."
    )


def test_timer_file_has_install_section():
    with open(TIMER_FILE, "r") as f:
        content = f.read()
    assert "[Install]" in content, (
        f"Timer file at {TIMER_FILE} is missing the [Install] section."
    )


def test_timer_file_wanted_by():
    with open(TIMER_FILE, "r") as f:
        content = f.read()
    assert "WantedBy=timers.target" in content, (
        f"Timer file at {TIMER_FILE} is missing 'WantedBy=timers.target' "
        "in the [Install] section."
    )


# ---------------------------------------------------------------------------
# Symlink checks (created by systemctl --user enable etl-pipeline.timer)
# ---------------------------------------------------------------------------

def test_symlink_exists():
    assert os.path.islink(SYMLINK), (
        f"Symlink not found at {SYMLINK}. "
        "Run: systemctl --user enable etl-pipeline.timer"
    )


def test_symlink_points_to_timer_file():
    assert os.path.islink(SYMLINK), (
        f"Symlink not found at {SYMLINK}. "
        "Run: systemctl --user enable etl-pipeline.timer"
    )
    link_target = os.readlink(SYMLINK)
    # The symlink may be absolute or relative; resolve to absolute for comparison
    if not os.path.isabs(link_target):
        link_target = os.path.normpath(
            os.path.join(os.path.dirname(SYMLINK), link_target)
        )
    assert link_target == TIMER_FILE, (
        f"Symlink at {SYMLINK} points to '{link_target}' "
        f"but should point to '{TIMER_FILE}'. "
        "Re-run: systemctl --user enable etl-pipeline.timer"
    )


def test_symlink_target_is_accessible():
    assert os.path.exists(SYMLINK), (
        f"Symlink at {SYMLINK} is broken (target does not exist). "
        f"Ensure {TIMER_FILE} exists and the symlink points to it correctly."
    )