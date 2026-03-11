# test_final_state.py

import os
import pytest

CONFIGS_DIR = "/home/user/configs"
APP_CONF = "/home/user/configs/app.conf"
BACKUPS_DIR = "/home/user/configs/backups"
APP_CONF_BAK = "/home/user/configs/backups/app.conf.bak"
CHANGES_DIFF = "/home/user/configs/backups/changes.diff"

EXPECTED_BAK_CONTENT = """# Application Configuration
host=localhost
port=8080
log_level=info
max_connections=100
timeout=30
debug_mode=false
"""

EXPECTED_APP_CONF_CONTENT = """# Application Configuration
host=localhost
port=8080
log_level=debug
max_connections=150
timeout=30
debug_mode=false
"""


# --- Backup directory ---

def test_backups_directory_exists():
    assert os.path.isdir(BACKUPS_DIR), (
        f"Backup directory {BACKUPS_DIR} does not exist. "
        "The backup directory must be created as part of the task."
    )


# --- Backup file ---

def test_backup_file_exists():
    assert os.path.isfile(APP_CONF_BAK), (
        f"Backup file {APP_CONF_BAK} does not exist. "
        "The original app.conf must be copied to the backup directory."
    )


def test_backup_file_contents():
    with open(APP_CONF_BAK, "r") as f:
        content = f.read()
    assert content.strip() == EXPECTED_BAK_CONTENT.strip(), (
        f"Backup file {APP_CONF_BAK} does not have the expected (original) contents.\n"
        f"Expected:\n{EXPECTED_BAK_CONTENT}\n\n"
        f"Got:\n{content}"
    )


def test_backup_has_log_level_info():
    with open(APP_CONF_BAK, "r") as f:
        lines = f.readlines()
    log_level_lines = [l for l in lines if l.startswith("log_level=")]
    assert len(log_level_lines) == 1, (
        f"Expected exactly one 'log_level=' line in backup, found: {log_level_lines}"
    )
    assert log_level_lines[0].strip() == "log_level=info", (
        f"Backup should preserve original 'log_level=info', "
        f"but found '{log_level_lines[0].strip()}'"
    )


def test_backup_has_max_connections_100():
    with open(APP_CONF_BAK, "r") as f:
        lines = f.readlines()
    max_conn_lines = [l for l in lines if l.startswith("max_connections=")]
    assert len(max_conn_lines) == 1, (
        f"Expected exactly one 'max_connections=' line in backup, found: {max_conn_lines}"
    )
    assert max_conn_lines[0].strip() == "max_connections=100", (
        f"Backup should preserve original 'max_connections=100', "
        f"but found '{max_conn_lines[0].strip()}'"
    )


def test_backup_has_correct_line_count():
    with open(APP_CONF_BAK, "r") as f:
        lines = [l for l in f.readlines() if l.strip()]
    assert len(lines) == 7, (
        f"Expected 7 non-empty lines in backup, found {len(lines)}. Lines: {lines}"
    )


# --- Modified app.conf ---

def test_app_conf_exists():
    assert os.path.isfile(APP_CONF), (
        f"File {APP_CONF} does not exist after the task."
    )


def test_app_conf_contents():
    with open(APP_CONF, "r") as f:
        content = f.read()
    assert content.strip() == EXPECTED_APP_CONF_CONTENT.strip(), (
        f"File {APP_CONF} does not have the expected modified contents.\n"
        f"Expected:\n{EXPECTED_APP_CONF_CONTENT}\n\n"
        f"Got:\n{content}"
    )


def test_app_conf_has_log_level_debug():
    with open(APP_CONF, "r") as f:
        lines = f.readlines()
    log_level_lines = [l for l in lines if l.startswith("log_level=")]
    assert len(log_level_lines) == 1, (
        f"Expected exactly one 'log_level=' line in {APP_CONF}, found: {log_level_lines}"
    )
    assert log_level_lines[0].strip() == "log_level=debug", (
        f"Expected 'log_level=debug' but found '{log_level_lines[0].strip()}'"
    )


def test_app_conf_has_max_connections_150():
    with open(APP_CONF, "r") as f:
        lines = f.readlines()
    max_conn_lines = [l for l in lines if l.startswith("max_connections=")]
    assert len(max_conn_lines) == 1, (
        f"Expected exactly one 'max_connections=' line in {APP_CONF}, found: {max_conn_lines}"
    )
    assert max_conn_lines[0].strip() == "max_connections=150", (
        f"Expected 'max_connections=150' but found '{max_conn_lines[0].strip()}'"
    )


def test_app_conf_unchanged_lines():
    """All lines other than log_level and max_connections must be unchanged."""
    with open(APP_CONF, "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines()]

    expected_unchanged = [
        "# Application Configuration",
        "host=localhost",
        "port=8080",
        "timeout=30",
        "debug_mode=false",
    ]
    for expected_line in expected_unchanged:
        assert expected_line in lines, (
            f"Expected line '{expected_line}' not found in {APP_CONF}. "
            f"Only log_level and max_connections should have changed."
        )


def test_app_conf_has_correct_line_count():
    with open(APP_CONF, "r") as f:
        lines = [l for l in f.readlines() if l.strip()]
    assert len(lines) == 7, (
        f"Expected 7 non-empty lines in {APP_CONF}, found {len(lines)}. Lines: {lines}"
    )


# --- Diff file ---

def test_diff_file_exists():
    assert os.path.isfile(CHANGES_DIFF), (
        f"Diff file {CHANGES_DIFF} does not exist. "
        "A unified diff must be generated and saved."
    )


def test_diff_file_is_not_empty():
    with open(CHANGES_DIFF, "r") as f:
        content = f.read()
    assert content.strip(), (
        f"Diff file {CHANGES_DIFF} is empty. It must contain the unified diff output."
    )


def test_diff_file_line_count():
    with open(CHANGES_DIFF, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 10, (
        f"Diff file {CHANGES_DIFF} has only {len(lines)} lines, expected at least 10. "
        f"Content:\n{''.join(lines)}"
    )


def test_diff_header_minus_line():
    with open(CHANGES_DIFF, "r") as f:
        lines = f.readlines()
    minus_lines = [l for l in lines if l.startswith("---")]
    assert len(minus_lines) >= 1, (
        f"No '---' header line found in diff file {CHANGES_DIFF}."
    )
    assert minus_lines[0].startswith("--- backups/app.conf.bak"), (
        f"The '---' header line must start with '--- backups/app.conf.bak', "
        f"but got: '{minus_lines[0].rstrip()}'"
    )


def test_diff_header_plus_line():
    with open(CHANGES_DIFF, "r") as f:
        lines = f.readlines()
    plus_header_lines = [l for l in lines if l.startswith("+++")]
    assert len(plus_header_lines) >= 1, (
        f"No '+++' header line found in diff file {CHANGES_DIFF}."
    )
    assert plus_header_lines[0].startswith("+++ app.conf"), (
        f"The '+++' header line must start with '+++ app.conf', "
        f"but got: '{plus_header_lines[0].rstrip()}'"
    )


def test_diff_contains_removed_log_level():
    with open(CHANGES_DIFF, "r") as f:
        content = f.read()
    assert "-log_level=info" in content, (
        f"Diff file {CHANGES_DIFF} does not contain '-log_level=info'. "
        "The diff must show the original log_level line as removed."
    )


def test_diff_contains_added_log_level():
    with open(CHANGES_DIFF, "r") as f:
        content = f.read()
    assert "+log_level=debug" in content, (
        f"Diff file {CHANGES_DIFF} does not contain '+log_level=debug'. "
        "The diff must show the new log_level line as added."
    )


def test_diff_contains_removed_max_connections():
    with open(CHANGES_DIFF, "r") as f:
        content = f.read()
    assert "-max_connections=100" in content, (
        f"Diff file {CHANGES_DIFF} does not contain '-max_connections=100'. "
        "The diff must show the original max_connections line as removed."
    )


def test_diff_contains_added_max_connections():
    with open(CHANGES_DIFF, "r") as f:
        content = f.read()
    assert "+max_connections=150" in content, (
        f"Diff file {CHANGES_DIFF} does not contain '+max_connections=150'. "
        "The diff must show the new max_connections line as added."
    )


def test_diff_contains_hunk_header():
    with open(CHANGES_DIFF, "r") as f:
        content = f.read()
    assert "@@" in content, (
        f"Diff file {CHANGES_DIFF} does not contain a hunk header (@@). "
        "The diff must be in unified format."
    )


def test_diff_context_lines_present():
    """Context lines (unchanged lines) should appear in the diff."""
    with open(CHANGES_DIFF, "r") as f:
        lines = f.readlines()
    # Context lines start with a space
    context_lines = [l for l in lines if l.startswith(" ")]
    assert len(context_lines) >= 3, (
        f"Expected at least 3 context lines in diff, found {len(context_lines)}. "
        f"Unified diff should include context around changes."
    )


def test_diff_only_two_changes():
    """The diff should show exactly 2 removed and 2 added lines (the two changed settings)."""
    with open(CHANGES_DIFF, "r") as f:
        lines = f.readlines()
    # Lines starting with '-' but not '---' are removed lines
    removed = [l for l in lines if l.startswith("-") and not l.startswith("---")]
    # Lines starting with '+' but not '+++' are added lines
    added = [l for l in lines if l.startswith("+") and not l.startswith("+++")]
    assert len(removed) == 2, (
        f"Expected exactly 2 removed lines in diff, found {len(removed)}: {removed}"
    )
    assert len(added) == 2, (
        f"Expected exactly 2 added lines in diff, found {len(added)}: {added}"
    )


def test_diff_is_unified_format():
    """Verify the diff file is in unified format by checking structure."""
    with open(CHANGES_DIFF, "r") as f:
        content = f.read()
    assert content.startswith("---"), (
        f"Diff file {CHANGES_DIFF} does not start with '---'. "
        "Expected unified diff format."
    )