# test_final_state.py

import os
import stat
import datetime
import pytest

WEBAPP_DIR = "/home/user/webapp"
DIAGNOSTICS_DIR = "/home/user/diagnostics"
SCAN_FILE = "/home/user/diagnostics/security_scan.txt"

EXPECTED_WORLD_WRITABLE = [
    "/home/user/webapp/config/settings.cfg",
    "/home/user/webapp/public/upload.php",
    "/home/user/webapp/static/style.css",
]

TODAY = datetime.date.today().strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def read_scan_lines():
    """Return the lines of the scan file (stripped of trailing newline)."""
    with open(SCAN_FILE, "r") as f:
        content = f.read()
    # Split on newlines; keep blank lines as empty strings
    lines = content.split("\n")
    # Remove a single trailing empty string caused by a final newline
    if lines and lines[-1] == "":
        lines = lines[:-1]
    return lines


# ---------------------------------------------------------------------------
# Directory / file existence
# ---------------------------------------------------------------------------

def test_diagnostics_directory_exists():
    assert os.path.isdir(DIAGNOSTICS_DIR), (
        f"The diagnostics directory {DIAGNOSTICS_DIR!r} does not exist. "
        "The student must create it as part of the task."
    )


def test_scan_file_exists():
    assert os.path.isfile(SCAN_FILE), (
        f"The security scan report {SCAN_FILE!r} does not exist. "
        "The student must create it as part of the task."
    )


# ---------------------------------------------------------------------------
# Line-by-line content checks
# ---------------------------------------------------------------------------

def test_scan_file_has_enough_lines():
    lines = read_scan_lines()
    # Minimum: header(1) + dir(1) + date(1) + blank(1) + "Files found:"(1)
    #          + 3 file paths + blank(1) + total(1) = 10 lines
    assert len(lines) >= 10, (
        f"The scan file has only {len(lines)} line(s); expected at least 10. "
        f"Content:\n{''.join(lines)}"
    )


def test_line1_header():
    lines = read_scan_lines()
    assert lines[0] == "=== WORLD-WRITABLE FILES SCAN ===", (
        f"Line 1 should be '=== WORLD-WRITABLE FILES SCAN ===' "
        f"but got: {lines[0]!r}"
    )


def test_line2_directory():
    lines = read_scan_lines()
    assert lines[1] == "Directory: /home/user/webapp", (
        f"Line 2 should be 'Directory: /home/user/webapp' "
        f"but got: {lines[1]!r}"
    )


def test_line3_date_format():
    lines = read_scan_lines()
    assert lines[2].startswith("Date: "), (
        f"Line 3 should start with 'Date: ' but got: {lines[2]!r}"
    )
    date_str = lines[2][len("Date: "):]
    # Validate it is a valid YYYY-MM-DD date
    try:
        parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        pytest.fail(
            f"Line 3 date portion {date_str!r} is not a valid YYYY-MM-DD date."
        )
    assert date_str == TODAY, (
        f"Line 3 date is {date_str!r} but today is {TODAY!r}. "
        "The report must be dated today."
    )


def test_line4_blank():
    lines = read_scan_lines()
    assert lines[3] == "", (
        f"Line 4 should be blank but got: {lines[3]!r}"
    )


def test_line5_files_found_label():
    lines = read_scan_lines()
    assert lines[4] == "Files found:", (
        f"Line 5 should be 'Files found:' but got: {lines[4]!r}"
    )


def test_lines6_8_world_writable_paths():
    lines = read_scan_lines()
    actual_paths = [lines[5], lines[6], lines[7]]
    expected_sorted = sorted(EXPECTED_WORLD_WRITABLE)
    assert actual_paths == expected_sorted, (
        f"Lines 6-8 (the file paths) do not match.\n"
        f"  Expected (sorted): {expected_sorted}\n"
        f"  Got:               {actual_paths}"
    )


def test_line9_blank():
    lines = read_scan_lines()
    assert lines[8] == "", (
        f"Line 9 should be blank but got: {lines[8]!r}"
    )


def test_line10_total():
    lines = read_scan_lines()
    assert lines[9] == "Total: 3 file(s) found", (
        f"Line 10 should be 'Total: 3 file(s) found' but got: {lines[9]!r}"
    )


def test_no_extra_lines():
    lines = read_scan_lines()
    assert len(lines) == 10, (
        f"The scan file should have exactly 10 lines but has {len(lines)}. "
        f"Extra content detected. Lines:\n" +
        "\n".join(f"  [{i+1}] {l!r}" for i, l in enumerate(lines))
    )


# ---------------------------------------------------------------------------
# Cross-check: world-writable files on disk still match expectations
# ---------------------------------------------------------------------------

def test_world_writable_files_on_disk_unchanged():
    """Verify the original world-writable files still have the correct permissions."""
    for filepath in EXPECTED_WORLD_WRITABLE:
        assert os.path.isfile(filepath), (
            f"Expected world-writable file {filepath!r} no longer exists on disk."
        )
        mode = stat.S_IMODE(os.stat(filepath).st_mode)
        assert mode & stat.S_IWOTH, (
            f"File {filepath!r} is no longer world-writable (permissions: {oct(mode)}). "
            "It should not have been modified."
        )


def test_total_world_writable_count_on_disk():
    """Confirm exactly 3 world-writable files exist under the webapp directory."""
    found_ww = []
    for root, dirs, files in os.walk(WEBAPP_DIR):
        for fname in files:
            fpath = os.path.join(root, fname)
            try:
                mode = stat.S_IMODE(os.stat(fpath).st_mode)
                if mode & stat.S_IWOTH:
                    found_ww.append(fpath)
            except OSError:
                pass
    found_ww.sort()
    expected_sorted = sorted(EXPECTED_WORLD_WRITABLE)
    assert found_ww == expected_sorted, (
        f"World-writable files on disk do not match expectations.\n"
        f"  Expected: {expected_sorted}\n"
        f"  Found:    {found_ww}"
    )