# test_final_state.py

import os
import subprocess
import pytest

HOME = "/home/user"
BACKUPS_DIR = os.path.join(HOME, "backups")
WEBAPP_ARCHIVE = os.path.join(BACKUPS_DIR, "webapp.tar.gz")
DATASERVICE_ARCHIVE = os.path.join(BACKUPS_DIR, "dataservice.tar.gz")
STORAGE_REPORT = os.path.join(BACKUPS_DIR, "storage_report.txt")


# ── Archive existence ──────────────────────────────────────────────────────────

def test_webapp_archive_exists():
    assert os.path.isfile(WEBAPP_ARCHIVE), (
        f"webapp.tar.gz not found at {WEBAPP_ARCHIVE}"
    )


def test_dataservice_archive_exists():
    assert os.path.isfile(DATASERVICE_ARCHIVE), (
        f"dataservice.tar.gz not found at {DATASERVICE_ARCHIVE}"
    )


# ── Archive validity (tar -tzf exits 0) ───────────────────────────────────────

def test_webapp_archive_is_valid_gzip_tar():
    result = subprocess.run(
        ["tar", "-tzf", WEBAPP_ARCHIVE],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"tar -tzf {WEBAPP_ARCHIVE} failed (rc={result.returncode}):\n"
        f"stderr: {result.stderr}"
    )


def test_dataservice_archive_is_valid_gzip_tar():
    result = subprocess.run(
        ["tar", "-tzf", DATASERVICE_ARCHIVE],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"tar -tzf {DATASERVICE_ARCHIVE} failed (rc={result.returncode}):\n"
        f"stderr: {result.stderr}"
    )


# ── Archive contents – expected entries present ───────────────────────────────

def _list_archive(path):
    result = subprocess.run(
        ["tar", "-tzf", path],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"Could not list {path}: {result.stderr}"
    return result.stdout


def test_webapp_archive_contains_index_html():
    listing = _list_archive(WEBAPP_ARCHIVE)
    assert "webapp/index.html" in listing, (
        f"webapp/index.html not found in {WEBAPP_ARCHIVE}.\nListing:\n{listing}"
    )


def test_webapp_archive_contains_app_js():
    listing = _list_archive(WEBAPP_ARCHIVE)
    assert "webapp/app.js" in listing, (
        f"webapp/app.js not found in {WEBAPP_ARCHIVE}.\nListing:\n{listing}"
    )


def test_webapp_archive_contains_settings_json():
    listing = _list_archive(WEBAPP_ARCHIVE)
    assert "webapp/config/settings.json" in listing, (
        f"webapp/config/settings.json not found in {WEBAPP_ARCHIVE}.\nListing:\n{listing}"
    )


def test_dataservice_archive_contains_main_py():
    listing = _list_archive(DATASERVICE_ARCHIVE)
    assert "dataservice/main.py" in listing, (
        f"dataservice/main.py not found in {DATASERVICE_ARCHIVE}.\nListing:\n{listing}"
    )


def test_dataservice_archive_contains_requirements_txt():
    listing = _list_archive(DATASERVICE_ARCHIVE)
    assert "dataservice/requirements.txt" in listing, (
        f"dataservice/requirements.txt not found in {DATASERVICE_ARCHIVE}.\nListing:\n{listing}"
    )


def test_dataservice_archive_contains_schema_sql():
    listing = _list_archive(DATASERVICE_ARCHIVE)
    assert "dataservice/data/schema.sql" in listing, (
        f"dataservice/data/schema.sql not found in {DATASERVICE_ARCHIVE}.\nListing:\n{listing}"
    )


# ── Archive paths are relative (no absolute paths) ────────────────────────────

def test_webapp_archive_has_no_absolute_paths():
    listing = _list_archive(WEBAPP_ARCHIVE)
    assert "/home/user" not in listing, (
        f"Absolute path '/home/user' found in {WEBAPP_ARCHIVE}.\n"
        f"Archive must use relative paths.\nListing:\n{listing}"
    )


def test_dataservice_archive_has_no_absolute_paths():
    listing = _list_archive(DATASERVICE_ARCHIVE)
    assert "/home/user" not in listing, (
        f"Absolute path '/home/user' found in {DATASERVICE_ARCHIVE}.\n"
        f"Archive must use relative paths.\nListing:\n{listing}"
    )


# ── Storage report existence ───────────────────────────────────────────────────

def test_storage_report_exists():
    assert os.path.isfile(STORAGE_REPORT), (
        f"storage_report.txt not found at {STORAGE_REPORT}"
    )


# ── Storage report line count ─────────────────────────────────────────────────

def test_storage_report_has_exactly_4_lines():
    with open(STORAGE_REPORT, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 4, (
        f"Expected exactly 4 lines in storage_report.txt, got {len(lines)}.\n"
        f"Content:\n{content!r}"
    )


# ── Storage report line 1 ─────────────────────────────────────────────────────

def test_storage_report_line1_header():
    with open(STORAGE_REPORT, "r") as f:
        lines = f.read().splitlines()
    assert lines[0] == "=== Backup Storage Report ===", (
        f"Line 1 of storage_report.txt is wrong.\n"
        f"Expected: '=== Backup Storage Report ==='\n"
        f"Got:      {lines[0]!r}"
    )


# ── Storage report line 2 – webapp size ───────────────────────────────────────

def test_storage_report_line2_webapp_size():
    actual_size = os.path.getsize(WEBAPP_ARCHIVE)
    with open(STORAGE_REPORT, "r") as f:
        lines = f.read().splitlines()
    expected_line = f"webapp.tar.gz {actual_size} bytes"
    assert lines[1] == expected_line, (
        f"Line 2 of storage_report.txt is wrong.\n"
        f"Expected: {expected_line!r}\n"
        f"Got:      {lines[1]!r}\n"
        f"Actual size of {WEBAPP_ARCHIVE}: {actual_size} bytes"
    )


# ── Storage report line 3 – dataservice size ──────────────────────────────────

def test_storage_report_line3_dataservice_size():
    actual_size = os.path.getsize(DATASERVICE_ARCHIVE)
    with open(STORAGE_REPORT, "r") as f:
        lines = f.read().splitlines()
    expected_line = f"dataservice.tar.gz {actual_size} bytes"
    assert lines[2] == expected_line, (
        f"Line 3 of storage_report.txt is wrong.\n"
        f"Expected: {expected_line!r}\n"
        f"Got:      {lines[2]!r}\n"
        f"Actual size of {DATASERVICE_ARCHIVE}: {actual_size} bytes"
    )


# ── Storage report line 4 – footer ───────────────────────────────────────────

def test_storage_report_line4_footer():
    with open(STORAGE_REPORT, "r") as f:
        lines = f.read().splitlines()
    assert lines[3] == "total 2 archives", (
        f"Line 4 of storage_report.txt is wrong.\n"
        f"Expected: 'total 2 archives'\n"
        f"Got:      {lines[3]!r}"
    )


# ── No trailing whitespace on any line ───────────────────────────────────────

def test_storage_report_no_trailing_whitespace():
    with open(STORAGE_REPORT, "r") as f:
        lines = f.read().splitlines()
    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} of storage_report.txt has trailing whitespace: {line!r}"
        )


# ── No blank lines anywhere ───────────────────────────────────────────────────

def test_storage_report_no_blank_lines():
    with open(STORAGE_REPORT, "r") as f:
        lines = f.read().splitlines()
    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"Line {i} of storage_report.txt is blank (not allowed)."
        )


# ── webapp appears before dataservice in the report ──────────────────────────

def test_storage_report_webapp_before_dataservice():
    with open(STORAGE_REPORT, "r") as f:
        content = f.read()
    webapp_pos = content.find("webapp.tar.gz")
    dataservice_pos = content.find("dataservice.tar.gz")
    assert webapp_pos != -1, "webapp.tar.gz not mentioned in storage_report.txt"
    assert dataservice_pos != -1, "dataservice.tar.gz not mentioned in storage_report.txt"
    assert webapp_pos < dataservice_pos, (
        "webapp.tar.gz must appear before dataservice.tar.gz in storage_report.txt"
    )