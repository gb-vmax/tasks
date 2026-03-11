# test_final_state.py

import os
import re
import subprocess
import hashlib
import pytest

ARCHIVE_PATH = "/home/user/backups/nightly.tar.gz"
MANIFEST_PATH = "/home/user/backups/manifest.sha256"
RESTORE_DIR = "/home/user/restore_test"
REPORT_PATH = "/home/user/backups/restore_report.txt"

EXPECTED_RESTORED_FILES = [
    "/home/user/restore_test/data/config.json",
    "/home/user/restore_test/data/users.csv",
    "/home/user/restore_test/data/notes.txt",
]

EXPECTED_CONFIG_JSON = '{"env":"production","version":"3.1.4","debug":false}'
EXPECTED_USERS_CSV = "id,name,email\n1,Alice,alice@example.com\n2,Bob,bob@example.com\n3,Carol,carol@example.com"
EXPECTED_NOTES_TXT = "Backup taken at 2024-11-01 02:00:00 UTC.\nAll systems nominal."


# ── Restore directory tests ──────────────────────────────────────────────────

def test_restore_dir_exists():
    assert os.path.isdir(RESTORE_DIR), (
        f"Restore directory does not exist: {RESTORE_DIR!r}. "
        "The agent should have created it during extraction."
    )


def test_restore_data_subdir_exists():
    data_dir = os.path.join(RESTORE_DIR, "data")
    assert os.path.isdir(data_dir), (
        f"Expected sub-directory {data_dir!r} to exist after extraction."
    )


def test_config_json_restored():
    path = os.path.join(RESTORE_DIR, "data", "config.json")
    assert os.path.isfile(path), (
        f"Restored file missing: {path!r}"
    )


def test_users_csv_restored():
    path = os.path.join(RESTORE_DIR, "data", "users.csv")
    assert os.path.isfile(path), (
        f"Restored file missing: {path!r}"
    )


def test_notes_txt_restored():
    path = os.path.join(RESTORE_DIR, "data", "notes.txt")
    assert os.path.isfile(path), (
        f"Restored file missing: {path!r}"
    )


def test_config_json_content():
    path = os.path.join(RESTORE_DIR, "data", "config.json")
    with open(path, "r") as f:
        content = f.read().strip()
    assert content == EXPECTED_CONFIG_JSON, (
        f"Content mismatch in {path!r}.\n"
        f"Expected: {EXPECTED_CONFIG_JSON!r}\n"
        f"Got:      {content!r}"
    )


def test_users_csv_content():
    path = os.path.join(RESTORE_DIR, "data", "users.csv")
    with open(path, "r") as f:
        content = f.read().strip()
    assert content == EXPECTED_USERS_CSV, (
        f"Content mismatch in {path!r}.\n"
        f"Expected: {EXPECTED_USERS_CSV!r}\n"
        f"Got:      {content!r}"
    )


def test_notes_txt_content():
    path = os.path.join(RESTORE_DIR, "data", "notes.txt")
    with open(path, "r") as f:
        content = f.read().strip()
    assert content == EXPECTED_NOTES_TXT, (
        f"Content mismatch in {path!r}.\n"
        f"Expected: {EXPECTED_NOTES_TXT!r}\n"
        f"Got:      {content!r}"
    )


def test_exactly_three_regular_files_restored():
    result = subprocess.run(
        ["find", RESTORE_DIR, "-type", "f"],
        capture_output=True,
        text=True,
        check=True,
    )
    files = [line for line in result.stdout.splitlines() if line.strip()]
    assert len(files) == 3, (
        f"Expected exactly 3 regular files under {RESTORE_DIR!r}, found {len(files)}.\n"
        f"Files found: {files}"
    )


def test_checksums_pass_against_manifest():
    """sha256sum --check must pass for all files when run from RESTORE_DIR."""
    result = subprocess.run(
        ["sha256sum", "--check", MANIFEST_PATH],
        capture_output=True,
        text=True,
        cwd=RESTORE_DIR,
    )
    assert result.returncode == 0, (
        f"sha256sum --check failed (return code {result.returncode}).\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )
    # All lines should say OK
    for line in result.stdout.splitlines():
        if line.strip():
            assert line.strip().endswith(": OK"), (
                f"Checksum verification did not pass for a file: {line!r}"
            )


# ── Restore report tests ─────────────────────────────────────────────────────

def test_report_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Restore report does not exist: {REPORT_PATH!r}"
    )


def test_report_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Restore report is not readable: {REPORT_PATH!r}"
    )


@pytest.fixture(scope="module")
def report_lines():
    with open(REPORT_PATH, "r") as f:
        raw = f.read()
    return raw, raw.splitlines()


def test_report_ends_with_single_newline(report_lines):
    raw, _ = report_lines
    assert raw.endswith("\n"), (
        f"Report file does not end with a newline character.\n"
        f"Last 20 chars: {raw[-20:]!r}"
    )
    assert not raw.endswith("\n\n"), (
        "Report file ends with more than one newline. It must end with exactly one."
    )


def test_report_has_exactly_seven_lines(report_lines):
    raw, lines = report_lines
    # Strip the trailing newline before counting
    content_lines = raw.rstrip("\n").splitlines()
    assert len(content_lines) == 7, (
        f"Report must have exactly 7 lines of content, found {len(content_lines)}.\n"
        f"Content:\n{raw!r}"
    )


def test_report_line1_header(report_lines):
    _, lines = report_lines
    assert lines[0] == "=== RESTORE TEST REPORT ===", (
        f"Line 1 mismatch.\n"
        f"Expected: '=== RESTORE TEST REPORT ==='\n"
        f"Got:      {lines[0]!r}"
    )


def test_report_line2_archive(report_lines):
    _, lines = report_lines
    expected = f"Archive: {ARCHIVE_PATH}"
    assert lines[1] == expected, (
        f"Line 2 mismatch.\n"
        f"Expected: {expected!r}\n"
        f"Got:      {lines[1]!r}"
    )


def test_report_line3_destination(report_lines):
    _, lines = report_lines
    expected = f"Destination: {RESTORE_DIR}"
    assert lines[2] == expected, (
        f"Line 3 mismatch.\n"
        f"Expected: {expected!r}\n"
        f"Got:      {lines[2]!r}"
    )


def test_report_line4_extraction_time_format(report_lines):
    _, lines = report_lines
    line = lines[3]
    prefix = "Extraction time (s): "
    assert line.startswith(prefix), (
        f"Line 4 must start with {prefix!r}.\nGot: {line!r}"
    )
    time_str = line[len(prefix):]
    pattern = re.compile(r"^\d+\.\d{2}$")
    assert pattern.match(time_str), (
        f"Extraction time {time_str!r} does not match required format X.XX "
        f"(integer digits, dot, exactly two decimal digits)."
    )
    # Must be a non-negative number
    assert float(time_str) >= 0.0, (
        f"Extraction time must be non-negative, got {time_str!r}"
    )


def test_report_line5_archive_size(report_lines):
    _, lines = report_lines
    line = lines[4]
    prefix = "Archive size (bytes): "
    assert line.startswith(prefix), (
        f"Line 5 must start with {prefix!r}.\nGot: {line!r}"
    )
    reported_size_str = line[len(prefix):]
    assert reported_size_str.isdigit(), (
        f"Archive size value {reported_size_str!r} is not a plain integer."
    )
    reported_size = int(reported_size_str)

    # Get actual size via stat
    result = subprocess.run(
        ["stat", "--format=%s", ARCHIVE_PATH],
        capture_output=True,
        text=True,
        check=True,
    )
    actual_size = int(result.stdout.strip())

    assert reported_size == actual_size, (
        f"Archive size in report ({reported_size}) does not match "
        f"actual size from stat ({actual_size}) for {ARCHIVE_PATH!r}."
    )


def test_report_line6_files_restored(report_lines):
    _, lines = report_lines
    line = lines[5]
    expected = "Files restored: 3"
    assert line == expected, (
        f"Line 6 mismatch.\n"
        f"Expected: {expected!r}\n"
        f"Got:      {line!r}"
    )


def test_report_line7_checksum_status(report_lines):
    _, lines = report_lines
    line = lines[6]
    expected = "Checksum status: OK"
    assert line == expected, (
        f"Line 7 mismatch.\n"
        f"Expected: {expected!r}\n"
        f"Got:      {line!r}"
    )


def test_report_no_trailing_spaces(report_lines):
    _, lines = report_lines
    for i, line in enumerate(lines, start=1):
        assert not line.endswith(" "), (
            f"Line {i} has trailing space(s): {line!r}"
        )


def test_report_no_extra_blank_lines(report_lines):
    raw, _ = report_lines
    content_lines = raw.rstrip("\n").splitlines()
    for i, line in enumerate(content_lines, start=1):
        assert line != "", (
            f"Line {i} is blank; the report must contain no blank lines."
        )