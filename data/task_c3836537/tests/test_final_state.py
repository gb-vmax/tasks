# test_final_state.py

import os
import re
import stat
import pytest

MONITORING_DIR = "/home/user/monitoring"
HOSTS_FILE = "/home/user/monitoring/hosts.txt"
SCRIPT_FILE = "/home/user/monitoring/check_uptime.sh"
REPORT_FILE = "/home/user/monitoring/uptime_report.txt"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_report_lines():
    """Return the report as a list of lines (newline stripped)."""
    with open(REPORT_FILE, "r") as f:
        return [line.rstrip("\n") for line in f.readlines()]


# ---------------------------------------------------------------------------
# Script existence & permissions
# ---------------------------------------------------------------------------

def test_script_file_exists():
    assert os.path.isfile(SCRIPT_FILE), (
        f"Script {SCRIPT_FILE} does not exist. "
        "The student must create the monitoring script."
    )


def test_script_is_executable():
    st = os.stat(SCRIPT_FILE)
    is_exec = bool(st.st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
    assert is_exec, (
        f"{SCRIPT_FILE} is not executable. "
        "Run 'chmod +x /home/user/monitoring/check_uptime.sh' to fix this."
    )


def test_script_contains_shebang():
    with open(SCRIPT_FILE, "r") as f:
        first_line = f.readline().rstrip("\n")
    assert first_line.startswith("#!"), (
        f"Script {SCRIPT_FILE} does not start with a shebang line. "
        f"First line is: {first_line!r}"
    )


def test_script_uses_ping_c2_W3():
    with open(SCRIPT_FILE, "r") as f:
        content = f.read()
    assert "ping -c 2 -W 3" in content, (
        f"Script {SCRIPT_FILE} does not contain 'ping -c 2 -W 3'. "
        "The script must use exactly 2 packets and a 3-second timeout."
    )


# ---------------------------------------------------------------------------
# Report existence
# ---------------------------------------------------------------------------

def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file {REPORT_FILE} does not exist. "
        "The student must run the script to generate the report."
    )


def test_report_file_is_not_empty():
    size = os.path.getsize(REPORT_FILE)
    assert size > 0, (
        f"Report file {REPORT_FILE} is empty. "
        "The script must write content to the report."
    )


# ---------------------------------------------------------------------------
# Report line-by-line structure
# ---------------------------------------------------------------------------

def test_report_has_at_least_12_lines():
    lines = read_report_lines()
    assert len(lines) >= 12, (
        f"Report has only {len(lines)} lines; expected at least 12.\n"
        f"Full report content:\n" + "\n".join(lines)
    )


def test_report_line1_header():
    lines = read_report_lines()
    assert lines[0] == "=== Uptime Report ===", (
        f"Line 1 should be '=== Uptime Report ===' but got: {lines[0]!r}"
    )


def test_report_line2_timestamp():
    lines = read_report_lines()
    line = lines[1]
    pattern = r"^Timestamp: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"
    assert re.match(pattern, line), (
        f"Line 2 should match 'Timestamp: YYYY-MM-DD HH:MM:SS' but got: {line!r}"
    )


def test_report_line3_hosts_checked():
    lines = read_report_lines()
    assert lines[2] == "Hosts checked: 3", (
        f"Line 3 should be 'Hosts checked: 3' but got: {lines[2]!r}"
    )


def test_report_line4_empty():
    lines = read_report_lines()
    assert lines[3] == "", (
        f"Line 4 should be empty but got: {lines[3]!r}"
    )


def test_report_line5_status_label():
    lines = read_report_lines()
    assert lines[4] == "Status:", (
        f"Line 5 should be 'Status:' but got: {lines[4]!r}"
    )


def test_report_line6_localhost_up():
    lines = read_report_lines()
    assert lines[5] == "  localhost: UP", (
        f"Line 6 should be '  localhost: UP' but got: {lines[5]!r}. "
        "localhost should be reachable and reported as UP."
    )


def test_report_line7_fake_host_one_down():
    lines = read_report_lines()
    assert lines[6] == "  fake-host-one.internal: DOWN", (
        f"Line 7 should be '  fake-host-one.internal: DOWN' but got: {lines[6]!r}. "
        "fake-host-one.internal is not a real host and should be DOWN."
    )


def test_report_line8_fake_host_two_down():
    lines = read_report_lines()
    assert lines[7] == "  fake-host-two.internal: DOWN", (
        f"Line 8 should be '  fake-host-two.internal: DOWN' but got: {lines[7]!r}. "
        "fake-host-two.internal is not a real host and should be DOWN."
    )


def test_report_line9_empty():
    lines = read_report_lines()
    assert lines[8] == "", (
        f"Line 9 should be empty but got: {lines[8]!r}"
    )


def test_report_line10_summary_label():
    lines = read_report_lines()
    assert lines[9] == "Summary:", (
        f"Line 10 should be 'Summary:' but got: {lines[9]!r}"
    )


def test_report_line11_up_count():
    lines = read_report_lines()
    assert lines[10] == "  UP:   1", (
        f"Line 11 should be '  UP:   1' but got: {lines[10]!r}. "
        "Expected exactly 1 UP host (localhost)."
    )


def test_report_line12_down_count():
    lines = read_report_lines()
    assert lines[11] == "  DOWN: 2", (
        f"Line 12 should be '  DOWN: 2' but got: {lines[11]!r}. "
        "Expected exactly 2 DOWN hosts (the two fake hostnames)."
    )


# ---------------------------------------------------------------------------
# Holistic / cross-cutting checks
# ---------------------------------------------------------------------------

def test_report_exact_line_count():
    lines = read_report_lines()
    # The report should be exactly 12 lines (possibly with a trailing newline
    # that produces an empty 13th element — we allow that).
    if len(lines) == 13:
        assert lines[12] == "", (
            f"Report has 13 lines but line 13 is not empty: {lines[12]!r}"
        )
    else:
        assert len(lines) == 12, (
            f"Report should have exactly 12 lines (or 12 + trailing newline), "
            f"but has {len(lines)} lines.\nFull content:\n" + "\n".join(lines)
        )


def test_report_status_indentation():
    """Each host status line must be indented with exactly two spaces."""
    lines = read_report_lines()
    host_lines = lines[5:8]
    for line in host_lines:
        assert line.startswith("  "), (
            f"Host status line is not indented with two spaces: {line!r}"
        )
        assert not line.startswith("   "), (
            f"Host status line has more than two leading spaces: {line!r}"
        )


def test_report_summary_indentation():
    """Summary count lines must be indented with exactly two spaces."""
    lines = read_report_lines()
    for line in [lines[10], lines[11]]:
        assert line.startswith("  "), (
            f"Summary line is not indented with two spaces: {line!r}"
        )
        assert not line.startswith("   "), (
            f"Summary line has more than two leading spaces: {line!r}"
        )


def test_report_no_extra_status_lines():
    """There should be exactly 3 host status lines between 'Status:' and the blank line."""
    lines = read_report_lines()
    # Lines 6, 7, 8 (0-indexed 5, 6, 7) are the status lines; line 9 (index 8) is blank.
    status_lines = lines[5:8]
    assert len(status_lines) == 3, (
        f"Expected exactly 3 host status lines, got {len(status_lines)}: {status_lines}"
    )


def test_hosts_file_unchanged():
    """The hosts.txt file must not have been modified."""
    with open(HOSTS_FILE, "r") as f:
        content = f.read()
    lines = [line.strip() for line in content.splitlines()
             if line.strip() and not line.strip().startswith("#")]
    expected = ["localhost", "fake-host-one.internal", "fake-host-two.internal"]
    assert lines == expected, (
        f"hosts.txt has been modified.\nExpected: {expected}\nGot: {lines}"
    )