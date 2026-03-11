# test_final_state.py

import os
import subprocess
import pytest

# Paths
SCRIPT_PATH = "/home/user/scripts/nightly_build.sh"
SERVICE_PATH = "/home/user/.config/systemd/user/nightly-build.service"
TIMER_PATH = "/home/user/.config/systemd/user/nightly-build.timer"
TIMERS_TARGET_WANTS_SYMLINK = "/home/user/.config/systemd/user/timers.target.wants/nightly-build.timer"

EXPECTED_SERVICE_CONTENT = (
    "[Unit]\n"
    "Description=Nightly Mobile Build Pipeline\n"
    "After=network.target\n"
    "\n"
    "[Service]\n"
    "Type=oneshot\n"
    "ExecStart=/home/user/scripts/nightly_build.sh\n"
    "StandardOutput=journal\n"
    "StandardError=journal\n"
)

EXPECTED_TIMER_CONTENT = (
    "[Unit]\n"
    "Description=Run Nightly Mobile Build Pipeline at 02:30\n"
    "\n"
    "[Timer]\n"
    "OnCalendar=*-*-* 02:30:00\n"
    "Persistent=true\n"
    "\n"
    "[Install]\n"
    "WantedBy=timers.target\n"
)


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def run_systemctl_user(*args):
    """Run a systemctl --user command as the 'user' account and return CompletedProcess."""
    cmd = ["sudo", "-u", "user", "systemctl", "--user"] + list(args)
    # We need XDG_RUNTIME_DIR and DBUS_SESSION_BUS_ADDRESS for user systemd
    env = os.environ.copy()
    env.setdefault("XDG_RUNTIME_DIR", "/run/user/1000")
    env.setdefault("DBUS_SESSION_BUS_ADDRESS", "unix:path=/run/user/1000/bus")
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        env=env,
    )
    return result


# ---------------------------------------------------------------------------
# Pre-existing script checks (still valid at final state)
# ---------------------------------------------------------------------------

def test_script_still_exists():
    """The nightly build script must still exist after the task."""
    assert os.path.isfile(SCRIPT_PATH), (
        f"Pre-existing build script is missing: {SCRIPT_PATH}\n"
        "This file should not have been removed."
    )


def test_script_still_executable():
    """The nightly build script must still be executable."""
    assert os.access(SCRIPT_PATH, os.X_OK), (
        f"Build script exists but is no longer executable: {SCRIPT_PATH}"
    )


# ---------------------------------------------------------------------------
# Service file checks
# ---------------------------------------------------------------------------

def test_service_file_exists():
    """The systemd user service file must exist."""
    assert os.path.isfile(SERVICE_PATH), (
        f"Service unit file not found: {SERVICE_PATH}\n"
        "Create the file as described in the task."
    )


def test_service_file_exact_content():
    """The service file must match the expected content byte-for-byte."""
    with open(SERVICE_PATH, "r") as f:
        content = f.read()
    assert content == EXPECTED_SERVICE_CONTENT, (
        f"Service file content does not match expected.\n"
        f"Expected:\n{repr(EXPECTED_SERVICE_CONTENT)}\n"
        f"Got:\n{repr(content)}"
    )


def test_service_file_no_install_section():
    """The service file must NOT contain an [Install] section."""
    with open(SERVICE_PATH, "r") as f:
        content = f.read()
    assert "[Install]" not in content, (
        f"Service file contains an [Install] section, which it must NOT have.\n"
        f"The timer activates the service; no [Install] section is needed.\n"
        f"File: {SERVICE_PATH}"
    )


# ---------------------------------------------------------------------------
# Timer file checks
# ---------------------------------------------------------------------------

def test_timer_file_exists():
    """The systemd user timer file must exist."""
    assert os.path.isfile(TIMER_PATH), (
        f"Timer unit file not found: {TIMER_PATH}\n"
        "Create the file as described in the task."
    )


def test_timer_file_exact_content():
    """The timer file must match the expected content byte-for-byte."""
    with open(TIMER_PATH, "r") as f:
        content = f.read()
    assert content == EXPECTED_TIMER_CONTENT, (
        f"Timer file content does not match expected.\n"
        f"Expected:\n{repr(EXPECTED_TIMER_CONTENT)}\n"
        f"Got:\n{repr(content)}"
    )


def test_timer_file_has_oncalendar():
    """The timer file must contain the correct OnCalendar directive."""
    with open(TIMER_PATH, "r") as f:
        content = f.read()
    assert "OnCalendar=*-*-* 02:30:00" in content, (
        f"Timer file is missing 'OnCalendar=*-*-* 02:30:00'.\n"
        f"File: {TIMER_PATH}"
    )


def test_timer_file_has_persistent():
    """The timer file must contain Persistent=true."""
    with open(TIMER_PATH, "r") as f:
        content = f.read()
    assert "Persistent=true" in content, (
        f"Timer file is missing 'Persistent=true'.\n"
        f"File: {TIMER_PATH}"
    )


def test_timer_file_has_install_section():
    """The timer file must contain an [Install] section with WantedBy=timers.target."""
    with open(TIMER_PATH, "r") as f:
        content = f.read()
    assert "[Install]" in content, (
        f"Timer file is missing an [Install] section.\n"
        f"File: {TIMER_PATH}"
    )
    assert "WantedBy=timers.target" in content, (
        f"Timer file is missing 'WantedBy=timers.target'.\n"
        f"File: {TIMER_PATH}"
    )


# ---------------------------------------------------------------------------
# Enable symlink check
# ---------------------------------------------------------------------------

def test_timers_target_wants_symlink_exists():
    """The enable symlink must exist, created by 'systemctl --user enable'."""
    assert os.path.islink(TIMERS_TARGET_WANTS_SYMLINK), (
        f"Symlink not found: {TIMERS_TARGET_WANTS_SYMLINK}\n"
        "Run 'systemctl --user enable nightly-build.timer' to create it."
    )


def test_timers_target_wants_symlink_points_to_timer():
    """The enable symlink must point to the timer unit file."""
    assert os.path.islink(TIMERS_TARGET_WANTS_SYMLINK), (
        f"Symlink not found: {TIMERS_TARGET_WANTS_SYMLINK}"
    )
    link_target = os.readlink(TIMERS_TARGET_WANTS_SYMLINK)
    # The symlink may be absolute or relative; resolve it
    if not os.path.isabs(link_target):
        symlink_dir = os.path.dirname(TIMERS_TARGET_WANTS_SYMLINK)
        resolved = os.path.normpath(os.path.join(symlink_dir, link_target))
    else:
        resolved = link_target
    assert resolved == TIMER_PATH, (
        f"Symlink {TIMERS_TARGET_WANTS_SYMLINK} points to {resolved!r},\n"
        f"but it should point to {TIMER_PATH!r}."
    )


# ---------------------------------------------------------------------------
# systemctl --user is-enabled check
# ---------------------------------------------------------------------------

def test_timer_is_enabled():
    """systemctl --user is-enabled nightly-build.timer must output 'enabled'."""
    result = run_systemctl_user("is-enabled", "nightly-build.timer")
    stdout = result.stdout.strip()
    assert result.returncode == 0, (
        f"'systemctl --user is-enabled nightly-build.timer' returned exit code {result.returncode}.\n"
        f"stdout: {stdout!r}\n"
        f"stderr: {result.stderr.strip()!r}\n"
        "Run 'systemctl --user enable nightly-build.timer' to enable it."
    )
    assert stdout == "enabled", (
        f"Expected 'enabled' but got {stdout!r}.\n"
        "Run 'systemctl --user enable nightly-build.timer' to enable it."
    )


# ---------------------------------------------------------------------------
# systemctl --user is-active check
# ---------------------------------------------------------------------------

def test_timer_is_active():
    """systemctl --user is-active nightly-build.timer must output 'active'."""
    result = run_systemctl_user("is-active", "nightly-build.timer")
    stdout = result.stdout.strip()
    assert result.returncode == 0, (
        f"'systemctl --user is-active nightly-build.timer' returned exit code {result.returncode}.\n"
        f"stdout: {stdout!r}\n"
        f"stderr: {result.stderr.strip()!r}\n"
        "Run 'systemctl --user start nightly-build.timer' to start it."
    )
    assert stdout == "active", (
        f"Expected 'active' but got {stdout!r}.\n"
        "Run 'systemctl --user start nightly-build.timer' to start it."
    )


# ---------------------------------------------------------------------------
# systemctl --user list-timers check
# ---------------------------------------------------------------------------

def test_timer_appears_in_list_timers():
    """nightly-build.timer must appear in 'systemctl --user list-timers --all'."""
    result = run_systemctl_user("list-timers", "--all")
    assert result.returncode == 0, (
        f"'systemctl --user list-timers --all' failed with exit code {result.returncode}.\n"
        f"stderr: {result.stderr.strip()!r}"
    )
    assert "nightly-build.timer" in result.stdout, (
        f"'nightly-build.timer' not found in 'systemctl --user list-timers --all' output.\n"
        f"Output was:\n{result.stdout}\n"
        "Ensure the timer is enabled and started."
    )