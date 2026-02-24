# test_final_state.py

import os
import pytest
import re
from datetime import datetime

HOME = "/home/user"
CONFIG_DIR = os.path.join(HOME, "opt_solver", "configs")
SOLVER_CONF = os.path.join(CONFIG_DIR, "solver.conf")
SOLVER_CONF_BAK = os.path.join(CONFIG_DIR, "solver.conf.bak")
DEPLOY_LOG = os.path.join(HOME, "opt_solver", "deploy.log")

ORIGINAL_SOLVER_CONF_LINES = [
    "# Solver configuration",
    "max_iterations = 1000",
    "tolerance = 1e-6",
    "method = conjugate_gradient"
]

UPDATED_SOLVER_CONF_LINES = [
    "# Solver configuration",
    "max_iterations = 2000",
    "tolerance = 1e-6",
    "method = conjugate_gradient"
]

INITIAL_DEPLOY_LOG_LINE = "[2024-04-01 12:05:13] Initial deployment completed."

LOG_ENTRY_REGEX = (
    r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] solver\.conf updated: max_iterations set to 2000 and backup created as solver\.conf\.bak"
)


def test_configs_directory_still_exists():
    assert os.path.isdir(CONFIG_DIR), (
        f"Required directory does not exist: {CONFIG_DIR}. "
        f"Configuration directory should still exist after task completion."
    )


def test_solver_conf_bak_exists_and_is_exact_backup():
    assert os.path.isfile(SOLVER_CONF_BAK), (
        f"Backup file missing: {SOLVER_CONF_BAK}. "
        f"A backup of solver.conf must be created as solver.conf.bak."
    )
    with open(SOLVER_CONF_BAK, "r", encoding="utf-8") as f:
        bak_lines = f.read().splitlines()
    assert bak_lines == ORIGINAL_SOLVER_CONF_LINES, (
        f"The contents of {SOLVER_CONF_BAK} do not match the required backup.\n"
        f"Expected:\n{ORIGINAL_SOLVER_CONF_LINES}\nActual:\n{bak_lines}\n"
        f"solver.conf.bak must be an exact copy of the original solver.conf before the update."
    )


def test_solver_conf_updated_correctly():
    assert os.path.isfile(SOLVER_CONF), (
        f"Configuration file missing: {SOLVER_CONF}. "
        f"solver.conf must exist after the task."
    )
    with open(SOLVER_CONF, "r", encoding="utf-8") as f:
        conf_lines = f.read().splitlines()

    # Check for exact match with expected updated content
    assert conf_lines == UPDATED_SOLVER_CONF_LINES, (
        f"The contents of {SOLVER_CONF} do not match the required final state.\n"
        f"Expected:\n{UPDATED_SOLVER_CONF_LINES}\nActual:\n{conf_lines}\n"
        "solver.conf must have ONLY the max_iterations line updated to 2000; all other lines unchanged and in the same order."
    )

    # Ensure there is exactly one max_iterations line
    max_iter_lines = [l for l in conf_lines if l.strip().startswith("max_iterations")]
    assert len(max_iter_lines) == 1, (
        f"There should be exactly one 'max_iterations' line in {SOLVER_CONF}, "
        f"but found {len(max_iter_lines)}.\n"
        f"Lines: {max_iter_lines}"
    )
    assert max_iter_lines[0].strip() == "max_iterations = 2000", (
        f"The 'max_iterations' line in {SOLVER_CONF} must be exactly 'max_iterations = 2000', "
        f"but found: {max_iter_lines[0]!r}"
    )


def test_deploy_log_entry_appended_and_format_is_correct():
    assert os.path.isfile(DEPLOY_LOG), (
        f"Deployment log file missing: {DEPLOY_LOG}. "
        f"deploy.log must exist after the task."
    )
    with open(DEPLOY_LOG, "r", encoding="utf-8") as f:
        log_lines = f.read().splitlines()

    assert len(log_lines) >= 2, (
        f"deploy.log should contain at least two lines after the operation.\n"
        f"Expected initial log line and new appended entry, but found {len(log_lines)} line(s):\n{log_lines}"
    )

    # The first line must be the unchanged initial log line
    assert log_lines[0] == INITIAL_DEPLOY_LOG_LINE, (
        f"The first line of {DEPLOY_LOG} should remain unchanged:\n"
        f"Expected: {INITIAL_DEPLOY_LOG_LINE!r}\nActual: {log_lines[0]!r}"
    )

    # The last line must match the required format and have a valid timestamp
    last_line = log_lines[-1]
    match = re.fullmatch(LOG_ENTRY_REGEX, last_line)
    assert match, (
        f"The last line of {DEPLOY_LOG} does not match the required format for the log entry.\n"
        f"Expected format:\n"
        f"[YYYY-MM-DD HH:MM:SS] solver.conf updated: max_iterations set to 2000 and backup created as solver.conf.bak\n"
        f"Actual last line:\n{last_line!r}"
    )

    # Validate the timestamp is a plausible system time (within the last 48h)
    timestamp_str = match.group(1)
    try:
        timestamp_dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        pytest.fail(
            f"Timestamp in the appended log entry is not a valid datetime: {timestamp_str!r}"
        )
    # Optionally, check that the timestamp is not in the past (before the initial deployment)
    min_dt = datetime.strptime("2024-04-01 12:05:13", "%Y-%m-%d %H:%M:%S")
    now_dt = datetime.now()
    assert timestamp_dt >= min_dt, (
        f"Timestamp in the new deploy.log entry ({timestamp_str}) "
        f"is before the initial deployment ({min_dt.strftime('%Y-%m-%d %H:%M:%S')})."
    )
    # Allow up to 48 hours into the future for slow-running tests/CI
    assert (now_dt - timestamp_dt).total_seconds() < 48 * 3600, (
        f"Timestamp in the new deploy.log entry ({timestamp_str}) "
        f"is more than 48 hours in the past (now: {now_dt.strftime('%Y-%m-%d %H:%M:%S')})."
    )

    # Ensure only one such log entry was appended (no duplicates)
    log_entry_count = sum(1 for line in log_lines if re.fullmatch(LOG_ENTRY_REGEX, line))
    assert log_entry_count == 1, (
        f"There should be exactly one appended log entry matching the required format in {DEPLOY_LOG}, "
        f"but found {log_entry_count}.\n"
        f"Log lines matching entry format: {[line for line in log_lines if re.fullmatch(LOG_ENTRY_REGEX, line)]}"
    )


def test_no_extra_files_created():
    # Ensure only the expected files exist in the configs directory
    expected_files = {"solver.conf", "solver.conf.bak"}
    actual_files = set(os.listdir(CONFIG_DIR))
    unexpected_files = actual_files - expected_files
    assert not unexpected_files, (
        f"Unexpected files found in {CONFIG_DIR}: {unexpected_files}. "
        f"Only solver.conf and solver.conf.bak should be present."
    )