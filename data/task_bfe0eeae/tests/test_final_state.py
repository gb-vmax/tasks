# test_final_state.py

import os
import re
import stat
import pytest

AUDIT_DIR = "/home/user/audit"
SCRIPT_PATH = "/home/user/audit/gen_audit_entry.sh"
LOG_PATH = "/home/user/audit/audit_trail.log"

LOG_LINE_PATTERN = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\|COMPLIANCE\|INFO\|Audit trail initialized\|TZ=UTC\|LANG=en_US\.UTF-8$"
)


def test_audit_directory_exists():
    """The /home/user/audit directory must exist after task completion."""
    assert os.path.isdir(AUDIT_DIR), (
        f"Expected directory '{AUDIT_DIR}' to exist, but it does not. "
        "The student must create the /home/user/audit/ directory."
    )


def test_script_exists():
    """The gen_audit_entry.sh script must exist after task completion."""
    assert os.path.isfile(SCRIPT_PATH), (
        f"Expected file '{SCRIPT_PATH}' to exist, but it does not. "
        "The student must create the shell script at the specified path."
    )


def test_script_is_executable():
    """The gen_audit_entry.sh script must be executable."""
    assert os.path.isfile(SCRIPT_PATH), (
        f"Cannot check executability: '{SCRIPT_PATH}' does not exist."
    )
    file_stat = os.stat(SCRIPT_PATH)
    is_executable = bool(
        file_stat.st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    )
    assert is_executable, (
        f"Expected '{SCRIPT_PATH}' to be executable, but it is not. "
        "Run 'chmod +x /home/user/audit/gen_audit_entry.sh' to fix this."
    )


def test_script_sets_tz_utc():
    """The script must set TZ=UTC."""
    assert os.path.isfile(SCRIPT_PATH), (
        f"Cannot check script contents: '{SCRIPT_PATH}' does not exist."
    )
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    assert "TZ=UTC" in content, (
        f"Expected the script '{SCRIPT_PATH}' to set TZ=UTC, but it does not contain 'TZ=UTC'. "
        "The script must export or use TZ=UTC to ensure UTC timestamps."
    )


def test_script_sets_lang_en_us():
    """The script must set LANG=en_US.UTF-8."""
    assert os.path.isfile(SCRIPT_PATH), (
        f"Cannot check script contents: '{SCRIPT_PATH}' does not exist."
    )
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    assert "LANG=en_US.UTF-8" in content, (
        f"Expected the script '{SCRIPT_PATH}' to set LANG=en_US.UTF-8, but it does not. "
        "The script must export or use LANG=en_US.UTF-8."
    )


def test_script_appends_to_log():
    """The script must append (>>) to the audit log file, not overwrite (>)."""
    assert os.path.isfile(SCRIPT_PATH), (
        f"Cannot check script contents: '{SCRIPT_PATH}' does not exist."
    )
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    assert ">>" in content, (
        f"Expected the script '{SCRIPT_PATH}' to use '>>' (append) to write to the log, "
        "but '>>' was not found. The script must append to the log file, not overwrite it."
    )


def test_script_references_log_path():
    """The script must reference the correct log file path."""
    assert os.path.isfile(SCRIPT_PATH), (
        f"Cannot check script contents: '{SCRIPT_PATH}' does not exist."
    )
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    assert "/home/user/audit/audit_trail.log" in content, (
        f"Expected the script '{SCRIPT_PATH}' to reference '/home/user/audit/audit_trail.log', "
        "but it does not. The log must be written to the correct path."
    )


def test_log_file_exists():
    """The audit_trail.log file must exist after the script is run."""
    assert os.path.isfile(LOG_PATH), (
        f"Expected file '{LOG_PATH}' to exist, but it does not. "
        "The student must execute the script to generate the audit log."
    )


def test_log_file_has_exactly_one_line():
    """The audit_trail.log file must contain exactly one line."""
    assert os.path.isfile(LOG_PATH), (
        f"Cannot check line count: '{LOG_PATH}' does not exist."
    )
    with open(LOG_PATH, "r") as f:
        content = f.read()

    # Count non-empty lines (also check raw line count)
    lines = content.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]

    assert len(non_empty_lines) == 1, (
        f"Expected '{LOG_PATH}' to contain exactly 1 non-empty line, "
        f"but found {len(non_empty_lines)} non-empty lines. "
        f"File content:\n{content!r}"
    )


def test_log_line_matches_pattern():
    """The single log line must match the required regex pattern."""
    assert os.path.isfile(LOG_PATH), (
        f"Cannot check log content: '{LOG_PATH}' does not exist."
    )
    with open(LOG_PATH, "r") as f:
        content = f.read()

    lines = [line for line in content.splitlines() if line.strip()]
    assert len(lines) >= 1, (
        f"Expected at least one line in '{LOG_PATH}', but the file is empty."
    )

    log_line = lines[0]
    assert LOG_LINE_PATTERN.match(log_line), (
        f"The log line does not match the required format.\n"
        f"Expected pattern: {LOG_LINE_PATTERN.pattern}\n"
        f"Actual line:      {log_line!r}\n\n"
        "The line must follow: "
        "<YYYY-MM-DDTHH:MM:SSZ>|COMPLIANCE|INFO|Audit trail initialized|TZ=UTC|LANG=en_US.UTF-8"
    )


def test_log_timestamp_ends_with_z():
    """The timestamp in the log line must end with literal 'Z', not a numeric offset."""
    assert os.path.isfile(LOG_PATH), (
        f"Cannot check log content: '{LOG_PATH}' does not exist."
    )
    with open(LOG_PATH, "r") as f:
        content = f.read()

    lines = [line for line in content.splitlines() if line.strip()]
    assert len(lines) >= 1, (
        f"Expected at least one line in '{LOG_PATH}', but the file is empty."
    )

    log_line = lines[0]
    # Extract the timestamp (everything before the first '|')
    parts = log_line.split("|")
    assert len(parts) >= 1, (
        f"Could not parse log line into pipe-delimited fields: {log_line!r}"
    )

    timestamp = parts[0]
    assert timestamp.endswith("Z"), (
        f"Expected the timestamp to end with literal 'Z' (UTC indicator), "
        f"but got: {timestamp!r}. "
        "Do not use '+0000' or '+00:00' — use the format '%Y-%m-%dT%H:%M:%SZ'."
    )

    # Also ensure no numeric offset is present
    assert "+" not in timestamp, (
        f"The timestamp '{timestamp}' contains a '+' character, suggesting a numeric UTC offset. "
        "Use 'Z' suffix instead (e.g., '2024-03-15T09:00:00Z')."
    )


def test_log_line_has_correct_fields():
    """The log line must have all required pipe-delimited fields in the correct order."""
    assert os.path.isfile(LOG_PATH), (
        f"Cannot check log content: '{LOG_PATH}' does not exist."
    )
    with open(LOG_PATH, "r") as f:
        content = f.read()

    lines = [line for line in content.splitlines() if line.strip()]
    assert len(lines) >= 1, (
        f"Expected at least one line in '{LOG_PATH}', but the file is empty."
    )

    log_line = lines[0]
    parts = log_line.split("|")

    assert len(parts) == 6, (
        f"Expected the log line to have exactly 6 pipe-delimited fields, "
        f"but found {len(parts)}. "
        f"Line: {log_line!r}\n"
        "Expected format: <timestamp>|COMPLIANCE|INFO|Audit trail initialized|TZ=UTC|LANG=en_US.UTF-8"
    )

    timestamp, level, severity, message, tz_field, lang_field = parts

    assert level == "COMPLIANCE", (
        f"Expected field 2 to be 'COMPLIANCE', but got: {level!r}"
    )
    assert severity == "INFO", (
        f"Expected field 3 to be 'INFO', but got: {severity!r}"
    )
    assert message == "Audit trail initialized", (
        f"Expected field 4 to be 'Audit trail initialized', but got: {message!r}"
    )
    assert tz_field == "TZ=UTC", (
        f"Expected field 5 to be 'TZ=UTC', but got: {tz_field!r}"
    )
    assert lang_field == "LANG=en_US.UTF-8", (
        f"Expected field 6 to be 'LANG=en_US.UTF-8', but got: {lang_field!r}"
    )


def test_log_file_no_trailing_blank_lines():
    """The log file must not have trailing blank lines (wc -l should return 1)."""
    assert os.path.isfile(LOG_PATH), (
        f"Cannot check log content: '{LOG_PATH}' does not exist."
    )
    with open(LOG_PATH, "rb") as f:
        raw_content = f.read()

    # Count actual newlines in the file
    newline_count = raw_content.count(b"\n")

    # A single line with a trailing newline = 1 newline (which is acceptable for wc -l = 1)
    # A single line without trailing newline = 0 newlines (wc -l = 0, but content is still 1 line)
    # More than 1 newline means extra blank lines
    assert newline_count <= 1, (
        f"Expected the log file to have at most 1 newline character (no trailing blank lines), "
        f"but found {newline_count} newline(s). "
        f"Raw file content: {raw_content!r}"
    )

    # Also verify there are no blank lines in the content
    lines = raw_content.decode("utf-8").splitlines()
    blank_lines = [i + 1 for i, line in enumerate(lines) if not line.strip()]
    assert not blank_lines, (
        f"Found blank lines at positions {blank_lines} in '{LOG_PATH}'. "
        "The file must contain exactly one non-empty line with no trailing blank lines."
    )