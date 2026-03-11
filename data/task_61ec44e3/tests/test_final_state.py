# test_final_state.py

import os
import stat
import pytest

MONITORING_DIR = "/home/user/monitoring"
SCRIPT_PATH = "/home/user/monitoring/check_alerts.sh"
LOG_PATH = "/home/user/monitoring/cpu_usage.log"
OUTPUT_PATH = "/home/user/monitoring/alerts_output.txt"

EXPECTED_SCRIPT_CONTENT = """#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_FILE="$SCRIPT_DIR/cpu_usage.log"

while IFS=' ' read -r hostname timestamp cpu; do
    if awk -v val="$cpu" 'BEGIN { exit !(val > 80.0) }'; then
        echo "ALERT: $hostname exceeded threshold at $timestamp (CPU: ${cpu}%)"
    fi
done < "$LOG_FILE"
"""

EXPECTED_LOG_CONTENT = """webserver01 2024-03-15T08:00:00 45.2
webserver02 2024-03-15T08:00:00 91.7
webserver01 2024-03-15T08:05:00 78.4
webserver03 2024-03-15T08:05:00 83.1
webserver02 2024-03-15T08:05:00 55.0
webserver01 2024-03-15T08:10:00 99.3
webserver03 2024-03-15T08:10:00 80.0
webserver02 2024-03-15T08:10:00 62.8
webserver01 2024-03-15T08:15:00 81.5
webserver03 2024-03-15T08:15:00 77.9
"""

EXPECTED_OUTPUT_CONTENT = """\
ALERT: webserver02 exceeded threshold at 2024-03-15T08:00:00 (CPU: 91.7%)
ALERT: webserver03 exceeded threshold at 2024-03-15T08:05:00 (CPU: 83.1%)
ALERT: webserver01 exceeded threshold at 2024-03-15T08:10:00 (CPU: 99.3%)
ALERT: webserver01 exceeded threshold at 2024-03-15T08:15:00 (CPU: 81.5%)
"""


# ---------------------------------------------------------------------------
# Directory and file existence
# ---------------------------------------------------------------------------

def test_monitoring_directory_exists():
    assert os.path.isdir(MONITORING_DIR), (
        f"Monitoring directory '{MONITORING_DIR}' does not exist."
    )


def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), (
        f"Script '{SCRIPT_PATH}' does not exist."
    )


def test_log_file_exists():
    assert os.path.isfile(LOG_PATH), (
        f"Log file '{LOG_PATH}' does not exist."
    )


def test_output_file_exists():
    assert os.path.isfile(OUTPUT_PATH), (
        f"Output file '{OUTPUT_PATH}' does not exist. "
        "The script must be run and its output saved to this path."
    )


# ---------------------------------------------------------------------------
# Script permissions — must now be executable
# ---------------------------------------------------------------------------

def test_script_is_executable():
    file_stat = os.stat(SCRIPT_PATH)
    mode = file_stat.st_mode
    is_executable = bool(mode & stat.S_IXUSR)
    assert is_executable, (
        f"Script '{SCRIPT_PATH}' is not executable (mode: {oct(stat.S_IMODE(mode))}). "
        "Run 'chmod +x /home/user/monitoring/check_alerts.sh' to make it executable."
    )


def test_script_owner_executable_bit_set():
    """Owner execute bit (S_IXUSR) must be set."""
    file_stat = os.stat(SCRIPT_PATH)
    mode = file_stat.st_mode
    assert bool(mode & stat.S_IXUSR), (
        f"Owner execute bit is not set on '{SCRIPT_PATH}' "
        f"(current mode: {oct(stat.S_IMODE(mode))})."
    )


# ---------------------------------------------------------------------------
# Script content unchanged
# ---------------------------------------------------------------------------

def test_script_content_unchanged():
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    assert content.strip() == EXPECTED_SCRIPT_CONTENT.strip(), (
        f"Script '{SCRIPT_PATH}' content has been modified.\n"
        f"Got:\n{content}\n\nExpected:\n{EXPECTED_SCRIPT_CONTENT}"
    )


# ---------------------------------------------------------------------------
# Log file content unchanged
# ---------------------------------------------------------------------------

def test_log_file_content_unchanged():
    with open(LOG_PATH, "r") as f:
        content = f.read()
    assert content.strip() == EXPECTED_LOG_CONTENT.strip(), (
        f"Log file '{LOG_PATH}' content has been modified.\n"
        f"Got:\n{content}\n\nExpected:\n{EXPECTED_LOG_CONTENT}"
    )


# ---------------------------------------------------------------------------
# Output file content
# ---------------------------------------------------------------------------

def test_output_file_is_not_empty():
    size = os.path.getsize(OUTPUT_PATH)
    assert size > 0, (
        f"Output file '{OUTPUT_PATH}' is empty. "
        "The script must produce alert output when run."
    )


def test_output_file_exact_content():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    assert content.strip() == EXPECTED_OUTPUT_CONTENT.strip(), (
        f"Output file '{OUTPUT_PATH}' does not match expected content.\n"
        f"Got:\n{content!r}\n\nExpected:\n{EXPECTED_OUTPUT_CONTENT!r}"
    )


def test_output_file_has_exactly_four_alert_lines():
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    assert len(lines) == 4, (
        f"Output file '{OUTPUT_PATH}' should have exactly 4 alert lines, "
        f"but has {len(lines)}.\nLines found:\n" + "\n".join(lines)
    )


def test_output_alert_for_webserver02_high_cpu():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    expected_line = "ALERT: webserver02 exceeded threshold at 2024-03-15T08:00:00 (CPU: 91.7%)"
    assert expected_line in content, (
        f"Expected alert line not found in '{OUTPUT_PATH}':\n"
        f"  Missing: {expected_line!r}\n"
        f"  Got:\n{content}"
    )


def test_output_alert_for_webserver03_high_cpu():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    expected_line = "ALERT: webserver03 exceeded threshold at 2024-03-15T08:05:00 (CPU: 83.1%)"
    assert expected_line in content, (
        f"Expected alert line not found in '{OUTPUT_PATH}':\n"
        f"  Missing: {expected_line!r}\n"
        f"  Got:\n{content}"
    )


def test_output_alert_for_webserver01_99_percent():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    expected_line = "ALERT: webserver01 exceeded threshold at 2024-03-15T08:10:00 (CPU: 99.3%)"
    assert expected_line in content, (
        f"Expected alert line not found in '{OUTPUT_PATH}':\n"
        f"  Missing: {expected_line!r}\n"
        f"  Got:\n{content}"
    )


def test_output_alert_for_webserver01_81_percent():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    expected_line = "ALERT: webserver01 exceeded threshold at 2024-03-15T08:15:00 (CPU: 81.5%)"
    assert expected_line in content, (
        f"Expected alert line not found in '{OUTPUT_PATH}':\n"
        f"  Missing: {expected_line!r}\n"
        f"  Got:\n{content}"
    )


def test_output_no_alert_for_webserver03_at_80_percent():
    """webserver03 at exactly 80.0% must NOT appear as an alert (threshold is strictly > 80.0)."""
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    forbidden = "webserver03 exceeded threshold at 2024-03-15T08:10:00"
    assert forbidden not in content, (
        f"Output file '{OUTPUT_PATH}' incorrectly contains an alert for webserver03 at 80.0%.\n"
        "The threshold is strictly greater than 80.0, so 80.0% must NOT trigger an alert.\n"
        f"Got:\n{content}"
    )


def test_output_no_alert_for_low_cpu_entries():
    """Entries with CPU <= 80.0 must not appear as alerts."""
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()

    # These entries are all at or below 80.0%
    non_alert_entries = [
        ("webserver01", "2024-03-15T08:00:00", "45.2"),
        ("webserver01", "2024-03-15T08:05:00", "78.4"),
        ("webserver02", "2024-03-15T08:05:00", "55.0"),
        ("webserver03", "2024-03-15T08:10:00", "80.0"),
        ("webserver02", "2024-03-15T08:10:00", "62.8"),
        ("webserver03", "2024-03-15T08:15:00", "77.9"),
    ]

    for hostname, timestamp, cpu in non_alert_entries:
        fragment = f"{hostname} exceeded threshold at {timestamp}"
        assert fragment not in content, (
            f"Output file '{OUTPUT_PATH}' incorrectly contains an alert for "
            f"{hostname} at {timestamp} (CPU: {cpu}%) — this is at or below the 80.0% threshold.\n"
            f"Got:\n{content}"
        )


def test_output_lines_start_with_alert_prefix():
    """Every non-empty line in the output must start with 'ALERT: '."""
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    for line in lines:
        assert line.startswith("ALERT: "), (
            f"Output line does not start with 'ALERT: ':\n  {line!r}\n"
            f"in '{OUTPUT_PATH}'"
        )


def test_output_line_order():
    """Alert lines must appear in the same order as the log file."""
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    expected_lines = [
        "ALERT: webserver02 exceeded threshold at 2024-03-15T08:00:00 (CPU: 91.7%)",
        "ALERT: webserver03 exceeded threshold at 2024-03-15T08:05:00 (CPU: 83.1%)",
        "ALERT: webserver01 exceeded threshold at 2024-03-15T08:10:00 (CPU: 99.3%)",
        "ALERT: webserver01 exceeded threshold at 2024-03-15T08:15:00 (CPU: 81.5%)",
    ]

    assert lines == expected_lines, (
        f"Alert lines in '{OUTPUT_PATH}' are not in the expected order.\n"
        f"Got:\n" + "\n".join(lines) + "\n\nExpected:\n" + "\n".join(expected_lines)
    )