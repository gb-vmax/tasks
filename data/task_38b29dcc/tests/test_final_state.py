# test_final_state.py

import os
import hashlib
import pytest

BACKUP_DIR = "/home/user/backups/pg"
CHECKSUMS_FILE = "/home/user/backups/pg/checksums.sha256"
REPORT_FILE = "/home/user/backups/integrity_report.txt"

EXPECTED_FILES_ORDERED = [
    "db_primary_20240801.dump",
    "db_replica_20240801.dump",
    "db_primary_20240731.dump",
    "db_replica_20240731.dump",
]

# Expected verification result per file (based on truth data)
EXPECTED_RESULTS = {
    "db_primary_20240801.dump": "OK",
    "db_replica_20240801.dump": "OK",
    "db_primary_20240731.dump": "FAILED",
    "db_replica_20240731.dump": "OK",
}

EXPECTED_PASSED = 3
EXPECTED_FAILED = 1
EXPECTED_STATUS = "CORRUPTED"

SEPARATOR = "=" * 23

EXPECTED_REPORT_LINES = [
    "BACKUP INTEGRITY REPORT",
    SEPARATOR,
    "db_primary_20240801.dump: OK",
    "db_replica_20240801.dump: OK",
    "db_primary_20240731.dump: FAILED",
    "db_replica_20240731.dump: OK",
    SEPARATOR,
    f"PASSED: {EXPECTED_PASSED}",
    f"FAILED: {EXPECTED_FAILED}",
    f"STATUS: {EXPECTED_STATUS}",
]


# ── helpers ──────────────────────────────────────────────────────────────────

def _read_report_lines():
    """Read the report file and return a list of non-empty stripped lines."""
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    return content.splitlines()


# ── existence tests ───────────────────────────────────────────────────────────

def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Integrity report file does not exist: {REPORT_FILE}\n"
        "The task requires writing the report to this exact path."
    )


# ── structural / content tests ────────────────────────────────────────────────

def test_report_line_count():
    lines = _read_report_lines()
    # 10 content lines; trailing newline means splitlines gives exactly 10
    assert len(lines) == 10, (
        f"Report should have exactly 10 lines (excluding trailing newline), "
        f"but got {len(lines)}.\n"
        f"Actual lines:\n" + "\n".join(repr(l) for l in lines)
    )


def test_report_header_line():
    lines = _read_report_lines()
    assert lines[0] == "BACKUP INTEGRITY REPORT", (
        f"Line 1 (header) is wrong.\n"
        f"  Expected: 'BACKUP INTEGRITY REPORT'\n"
        f"  Actual:   {lines[0]!r}"
    )


def test_report_first_separator():
    lines = _read_report_lines()
    assert lines[1] == SEPARATOR, (
        f"Line 2 (first separator) is wrong.\n"
        f"  Expected: {SEPARATOR!r} (23 '=' chars)\n"
        f"  Actual:   {lines[1]!r}"
    )


@pytest.mark.parametrize("filename,expected_result", [
    ("db_primary_20240801.dump", "OK"),
    ("db_replica_20240801.dump", "OK"),
    ("db_primary_20240731.dump", "FAILED"),
    ("db_replica_20240731.dump", "OK"),
])
def test_report_file_result_line(filename, expected_result):
    lines = _read_report_lines()
    # File lines are at indices 2, 3, 4, 5
    file_lines = lines[2:6]
    expected_line = f"{filename}: {expected_result}"
    assert expected_line in file_lines, (
        f"Expected line '{expected_line}' not found among file-result lines.\n"
        f"File-result lines in report:\n" + "\n".join(repr(l) for l in file_lines)
    )


def test_report_file_lines_order():
    """Files must appear in the same order as in checksums.sha256."""
    lines = _read_report_lines()
    file_lines = lines[2:6]
    for idx, filename in enumerate(EXPECTED_FILES_ORDERED):
        expected_result = EXPECTED_RESULTS[filename]
        expected_line = f"{filename}: {expected_result}"
        assert file_lines[idx] == expected_line, (
            f"File-result line {idx + 1} (report line {idx + 3}) is wrong.\n"
            f"  Expected: {expected_line!r}\n"
            f"  Actual:   {file_lines[idx]!r}\n"
            "Files must be listed in the same order they appear in checksums.sha256."
        )


def test_report_second_separator():
    lines = _read_report_lines()
    assert lines[6] == SEPARATOR, (
        f"Line 7 (second separator) is wrong.\n"
        f"  Expected: {SEPARATOR!r} (23 '=' chars)\n"
        f"  Actual:   {lines[6]!r}"
    )


def test_report_passed_count():
    lines = _read_report_lines()
    assert lines[7] == f"PASSED: {EXPECTED_PASSED}", (
        f"PASSED count line is wrong.\n"
        f"  Expected: 'PASSED: {EXPECTED_PASSED}'\n"
        f"  Actual:   {lines[7]!r}"
    )


def test_report_failed_count():
    lines = _read_report_lines()
    assert lines[8] == f"FAILED: {EXPECTED_FAILED}", (
        f"FAILED count line is wrong.\n"
        f"  Expected: 'FAILED: {EXPECTED_FAILED}'\n"
        f"  Actual:   {lines[8]!r}"
    )


def test_report_status_line():
    lines = _read_report_lines()
    assert lines[9] == f"STATUS: {EXPECTED_STATUS}", (
        f"STATUS line is wrong.\n"
        f"  Expected: 'STATUS: {EXPECTED_STATUS}'\n"
        f"  Actual:   {lines[9]!r}\n"
        "STATUS should be 'CORRUPTED' because db_primary_20240731.dump failed verification."
    )


def test_report_ends_with_newline():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        "The report file should end with a trailing newline character.\n"
        f"Last 10 chars of file: {content[-10:]!r}"
    )


def test_report_exact_content():
    """Full exact-match check of the entire report content."""
    expected_content = "\n".join(EXPECTED_REPORT_LINES) + "\n"
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    assert actual_content == expected_content, (
        "The integrity report content does not exactly match the expected format.\n"
        f"Expected:\n{expected_content!r}\n\n"
        f"Actual:\n{actual_content!r}"
    )


# ── verify backup files are still intact (task must not alter them) ───────────

def test_backup_files_still_exist():
    for filename in EXPECTED_FILES_ORDERED:
        filepath = os.path.join(BACKUP_DIR, filename)
        assert os.path.isfile(filepath), (
            f"Backup file is missing after task completion: {filepath}\n"
            "The task should not delete or move backup files."
        )


def test_corrupted_file_still_corrupted():
    """db_primary_20240731.dump must still contain the corrupted content."""
    filepath = os.path.join(BACKUP_DIR, "db_primary_20240731.dump")
    actual = open(filepath, "rb").read()
    expected = b"PGDUMP_PRIMARY_20240731_DATA_BLOCK_CORRUPTED"
    assert actual == expected, (
        f"db_primary_20240731.dump should still contain the corrupted content.\n"
        f"  Expected: {expected!r}\n"
        f"  Actual:   {actual!r}"
    )


def test_valid_files_unchanged():
    """The three valid backup files must remain unmodified."""
    expected_contents = {
        "db_primary_20240801.dump": b"PGDUMP_PRIMARY_20240801_DATA_BLOCK_VALID",
        "db_replica_20240801.dump": b"PGDUMP_REPLICA_20240801_DATA_BLOCK_VALID",
        "db_replica_20240731.dump": b"PGDUMP_REPLICA_20240731_DATA_BLOCK_VALID",
    }
    for filename, expected in expected_contents.items():
        filepath = os.path.join(BACKUP_DIR, filename)
        actual = open(filepath, "rb").read()
        assert actual == expected, (
            f"{filename} has been modified (should be unchanged).\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}"
        )


def test_checksums_manifest_unchanged():
    """The checksums.sha256 manifest must not have been altered."""
    # Re-derive expected hashes from known content
    manifest_hash_contents = {
        "db_primary_20240801.dump": b"PGDUMP_PRIMARY_20240801_DATA_BLOCK_VALID",
        "db_replica_20240801.dump": b"PGDUMP_REPLICA_20240801_DATA_BLOCK_VALID",
        "db_primary_20240731.dump": b"PGDUMP_PRIMARY_20240731_DATA_BLOCK_VALID",
        "db_replica_20240731.dump": b"PGDUMP_REPLICA_20240731_DATA_BLOCK_VALID",
    }

    with open(CHECKSUMS_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    assert len(lines) == 4, (
        f"checksums.sha256 should have 4 entries, got {len(lines)}."
    )

    for i, filename in enumerate(EXPECTED_FILES_ORDERED):
        full_path = os.path.join(BACKUP_DIR, filename)
        expected_hash = hashlib.sha256(manifest_hash_contents[filename]).hexdigest()
        parts = lines[i].split("  ", 1)
        assert len(parts) == 2, (
            f"Manifest line {i+1} is malformed: {lines[i]!r}"
        )
        actual_hash, actual_path = parts
        assert actual_path == full_path, (
            f"Manifest line {i+1}: path changed.\n"
            f"  Expected: {full_path!r}\n"
            f"  Actual:   {actual_path!r}"
        )
        assert actual_hash == expected_hash, (
            f"Manifest hash for {filename} was altered.\n"
            f"  Expected: {expected_hash}\n"
            f"  Actual:   {actual_hash}"
        )