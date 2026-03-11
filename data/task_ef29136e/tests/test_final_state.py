# test_final_state.py

import os
import subprocess
import pytest

REPORT_PATH = "/home/user/storage_report.txt"

EXPECTED_REPORT = """\
=== DISK SPACE REPORT ===
Generated for: /home/user/storage

--- Directory Usage ---
/home/user/storage/appdata: 53MB [WARN] (threshold: 50MB)
/home/user/storage/logs: 28MB [OK] (threshold: 30MB)
/home/user/storage/backups: 82MB [WARN] (threshold: 80MB)
/home/user/storage/uploads: 21MB [WARN] (threshold: 20MB)

--- Top 3 Largest Files ---
1. /home/user/storage/backups/backup_full.tar.gz (61440KB)
2. /home/user/storage/appdata/database.db (38912KB)
3. /home/user/storage/backups/backup_inc.tar.gz (22528KB)

--- Summary ---
Total monitored usage: 184MB
Directories in WARNING: 3
"""


# ---------------------------------------------------------------------------
# Helper: read the report once and cache it
# ---------------------------------------------------------------------------

def _read_report():
    with open(REPORT_PATH, "r") as f:
        return f.read()


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_report_file_exists():
    """The report file must exist at the expected path."""
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The student must generate it by running the disk-space analysis script."
    )


def test_report_ends_with_newline():
    """The report file must end with exactly one newline."""
    content = _read_report()
    assert content.endswith("\n"), (
        f"Report file '{REPORT_PATH}' does not end with a newline character."
    )


def test_report_exact_content():
    """The entire report must match the expected content byte-for-byte."""
    content = _read_report()
    assert content == EXPECTED_REPORT, (
        f"Report file content does not match expected.\n\n"
        f"=== EXPECTED ===\n{EXPECTED_REPORT!r}\n\n"
        f"=== ACTUAL ===\n{content!r}"
    )


# ---------------------------------------------------------------------------
# Fine-grained section tests (useful for partial-credit diagnosis)
# ---------------------------------------------------------------------------

def _get_lines():
    return _read_report().splitlines()


def test_report_header_line():
    lines = _get_lines()
    assert lines[0] == "=== DISK SPACE REPORT ===", (
        f"First line of report is wrong.\n"
        f"Expected: '=== DISK SPACE REPORT ==='\n"
        f"Actual:   '{lines[0]}'"
    )


def test_report_generated_for_line():
    lines = _get_lines()
    assert lines[1] == "Generated for: /home/user/storage", (
        f"Second line of report is wrong.\n"
        f"Expected: 'Generated for: /home/user/storage'\n"
        f"Actual:   '{lines[1]}'"
    )


def test_report_blank_line_after_header():
    lines = _get_lines()
    assert lines[2] == "", (
        f"Line 3 (after header) should be blank.\n"
        f"Actual: '{lines[2]}'"
    )


def test_directory_usage_section_header():
    lines = _get_lines()
    assert lines[3] == "--- Directory Usage ---", (
        f"Line 4 should be '--- Directory Usage ---'.\n"
        f"Actual: '{lines[3]}'"
    )


def test_appdata_usage_line():
    lines = _get_lines()
    expected = "/home/user/storage/appdata: 53MB [WARN] (threshold: 50MB)"
    assert lines[4] == expected, (
        f"appdata usage line is wrong.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[4]}'"
    )


def test_logs_usage_line():
    lines = _get_lines()
    expected = "/home/user/storage/logs: 28MB [OK] (threshold: 30MB)"
    assert lines[5] == expected, (
        f"logs usage line is wrong.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[5]}'"
    )


def test_backups_usage_line():
    lines = _get_lines()
    expected = "/home/user/storage/backups: 82MB [WARN] (threshold: 80MB)"
    assert lines[6] == expected, (
        f"backups usage line is wrong.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[6]}'"
    )


def test_uploads_usage_line():
    lines = _get_lines()
    expected = "/home/user/storage/uploads: 21MB [WARN] (threshold: 20MB)"
    assert lines[7] == expected, (
        f"uploads usage line is wrong.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[7]}'"
    )


def test_blank_line_after_directory_usage():
    lines = _get_lines()
    assert lines[8] == "", (
        f"Line 9 (after Directory Usage block) should be blank.\n"
        f"Actual: '{lines[8]}'"
    )


def test_top3_section_header():
    lines = _get_lines()
    assert lines[9] == "--- Top 3 Largest Files ---", (
        f"Line 10 should be '--- Top 3 Largest Files ---'.\n"
        f"Actual: '{lines[9]}'"
    )


def test_top3_first_entry():
    lines = _get_lines()
    expected = "1. /home/user/storage/backups/backup_full.tar.gz (61440KB)"
    assert lines[10] == expected, (
        f"Top-3 entry #1 is wrong.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[10]}'"
    )


def test_top3_second_entry():
    lines = _get_lines()
    expected = "2. /home/user/storage/appdata/database.db (38912KB)"
    assert lines[11] == expected, (
        f"Top-3 entry #2 is wrong.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[11]}'"
    )


def test_top3_third_entry():
    lines = _get_lines()
    expected = "3. /home/user/storage/backups/backup_inc.tar.gz (22528KB)"
    assert lines[12] == expected, (
        f"Top-3 entry #3 is wrong.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[12]}'"
    )


def test_blank_line_after_top3():
    lines = _get_lines()
    assert lines[13] == "", (
        f"Line 14 (after Top 3 block) should be blank.\n"
        f"Actual: '{lines[13]}'"
    )


def test_summary_section_header():
    lines = _get_lines()
    assert lines[14] == "--- Summary ---", (
        f"Line 15 should be '--- Summary ---'.\n"
        f"Actual: '{lines[14]}'"
    )


def test_total_monitored_usage_line():
    lines = _get_lines()
    expected = "Total monitored usage: 184MB"
    assert lines[15] == expected, (
        f"Total monitored usage line is wrong.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[15]}'"
    )


def test_directories_in_warning_line():
    lines = _get_lines()
    expected = "Directories in WARNING: 3"
    assert lines[16] == expected, (
        f"Directories in WARNING line is wrong.\n"
        f"Expected: '{expected}'\n"
        f"Actual:   '{lines[16]}'"
    )


def test_report_line_count():
    """Report should have exactly 17 lines of content plus a trailing newline."""
    lines = _get_lines()
    assert len(lines) == 17, (
        f"Report has {len(lines)} lines, expected 17.\n"
        f"Lines: {lines}"
    )


# ---------------------------------------------------------------------------
# Sanity-check: underlying data still intact
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("dirpath,expected_mb", [
    ("/home/user/storage/appdata", 53),
    ("/home/user/storage/logs", 28),
    ("/home/user/storage/backups", 82),
    ("/home/user/storage/uploads", 21),
])
def test_du_values_still_correct(dirpath, expected_mb):
    """Confirm the du -sm values match what the report claims."""
    result = subprocess.run(
        ["du", "-sm", dirpath],
        capture_output=True, text=True, check=True
    )
    actual_mb = int(result.stdout.split()[0])
    assert actual_mb == expected_mb, (
        f"du -sm {dirpath} reports {actual_mb}MB, expected {expected_mb}MB. "
        "The underlying storage data may have changed."
    )


@pytest.mark.parametrize("filepath,expected_bytes", [
    ("/home/user/storage/backups/backup_full.tar.gz", 60 * 1024 * 1024),
    ("/home/user/storage/appdata/database.db", 38 * 1024 * 1024),
    ("/home/user/storage/backups/backup_inc.tar.gz", 22 * 1024 * 1024),
])
def test_top3_file_sizes_still_correct(filepath, expected_bytes):
    """Confirm the top-3 files still have the expected byte sizes."""
    actual = os.path.getsize(filepath)
    expected_kb = expected_bytes // 1024
    assert actual == expected_bytes, (
        f"File '{filepath}' has {actual} bytes (= {actual // 1024}KB), "
        f"expected {expected_bytes} bytes (= {expected_kb}KB)."
    )