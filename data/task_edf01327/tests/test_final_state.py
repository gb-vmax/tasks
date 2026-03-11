# test_final_state.py

import os
import pytest

BACKUP_DIR = '/home/user/backup_analysis'

# ── Expected file contents (exact strings) ───────────────────────────────────

EXPECTED_PROJECTS_SUMMARY = """\
Directory: /home/user/datastore/projects
Total size (bytes): 70424
File count: 5
Largest file: beta/app.py (43008 bytes)
Smallest file: alpha/README.md (512 bytes)"""

EXPECTED_PROJECTS_TOP3 = """\
Top 3 largest files in /home/user/datastore/projects:
1. beta/app.py (43008 bytes)
2. alpha/main.c (18200 bytes)
3. shared/utils.py (7680 bytes)"""

EXPECTED_MEDIA_SUMMARY = """\
Directory: /home/user/datastore/media
Total size (bytes): 387072
File count: 4
Largest file: videos/clip.mp4 (204800 bytes)
Smallest file: thumbs/thumb1.png (3072 bytes)"""

EXPECTED_MEDIA_TOP3 = """\
Top 3 largest files in /home/user/datastore/media:
1. videos/clip.mp4 (204800 bytes)
2. images/photo1.jpg (92160 bytes)
3. images/photo2.jpg (87040 bytes)"""

EXPECTED_LOGS_SUMMARY = """\
Directory: /home/user/datastore/logs
Total size (bytes): 58368
File count: 3
Largest file: app/app.log (34816 bytes)
Smallest file: app/error.log (8192 bytes)"""

EXPECTED_LOGS_TOP3 = """\
Top 3 largest files in /home/user/datastore/logs:
1. app/app.log (34816 bytes)
2. system/syslog (15360 bytes)
3. app/error.log (8192 bytes)"""

EXPECTED_DATABASES_SUMMARY = """\
Directory: /home/user/datastore/databases
Total size (bytes): 112640
File count: 3
Largest file: backups/db1_bak.sqlite (46080 bytes)
Smallest file: db2.sqlite (20480 bytes)"""

EXPECTED_DATABASES_TOP3 = """\
Top 3 largest files in /home/user/datastore/databases:
1. backups/db1_bak.sqlite (46080 bytes)
2. db1.sqlite (46080 bytes)
3. db2.sqlite (20480 bytes)"""

EXPECTED_MASTER_REPORT = """\
=== BACKUP ANALYSIS REPORT ===
Generated from: /home/user/datastore

DIRECTORY SUMMARY (sorted by total size, largest first):
  1. media: 387072 bytes (4 files)
  2. databases: 112640 bytes (3 files)
  3. projects: 70424 bytes (5 files)
  4. logs: 58368 bytes (3 files)

GRAND TOTAL: 628504 bytes across 15 files

ARCHIVE RECOMMENDATIONS:
  Exceeds 100KB: databases, media
  Exceeds 50KB:  databases, logs, media, projects

LARGEST SINGLE FILE OVERALL:
  media/videos/clip.mp4 (204800 bytes)"""

# ── Helper ────────────────────────────────────────────────────────────────────

def read_file(path: str) -> str:
    """Read a file and return its content with trailing whitespace stripped per line."""
    with open(path, 'r') as fh:
        return fh.read()


def normalise(text: str) -> str:
    """Strip trailing whitespace from every line and remove a single trailing newline."""
    lines = text.splitlines()
    stripped = [line.rstrip() for line in lines]
    # Remove a single trailing blank line produced by a final '\n'
    while stripped and stripped[-1] == '':
        stripped.pop()
    return '\n'.join(stripped)


# ── Existence tests ───────────────────────────────────────────────────────────

def test_backup_analysis_dir_exists():
    assert os.path.isdir(BACKUP_DIR), (
        f"Output directory {BACKUP_DIR!r} does not exist. "
        "The student's solution must create it."
    )


@pytest.mark.parametrize("filename", [
    'projects_summary.txt',
    'projects_top3.txt',
    'media_summary.txt',
    'media_top3.txt',
    'logs_summary.txt',
    'logs_top3.txt',
    'databases_summary.txt',
    'databases_top3.txt',
    'master_report.txt',
])
def test_output_file_exists(filename):
    path = os.path.join(BACKUP_DIR, filename)
    assert os.path.isfile(path), (
        f"Expected output file does not exist: {path!r}"
    )


# ── Content tests: per-directory summaries ────────────────────────────────────

def test_projects_summary_content():
    path = os.path.join(BACKUP_DIR, 'projects_summary.txt')
    assert os.path.isfile(path), f"File missing: {path!r}"
    actual = normalise(read_file(path))
    expected = normalise(EXPECTED_PROJECTS_SUMMARY)
    assert actual == expected, (
        f"projects_summary.txt content mismatch.\n"
        f"Expected:\n{expected}\n\nActual:\n{actual}"
    )


def test_projects_top3_content():
    path = os.path.join(BACKUP_DIR, 'projects_top3.txt')
    assert os.path.isfile(path), f"File missing: {path!r}"
    actual = normalise(read_file(path))
    expected = normalise(EXPECTED_PROJECTS_TOP3)
    assert actual == expected, (
        f"projects_top3.txt content mismatch.\n"
        f"Expected:\n{expected}\n\nActual:\n{actual}"
    )


def test_media_summary_content():
    path = os.path.join(BACKUP_DIR, 'media_summary.txt')
    assert os.path.isfile(path), f"File missing: {path!r}"
    actual = normalise(read_file(path))
    expected = normalise(EXPECTED_MEDIA_SUMMARY)
    assert actual == expected, (
        f"media_summary.txt content mismatch.\n"
        f"Expected:\n{expected}\n\nActual:\n{actual}"
    )


def test_media_top3_content():
    path = os.path.join(BACKUP_DIR, 'media_top3.txt')
    assert os.path.isfile(path), f"File missing: {path!r}"
    actual = normalise(read_file(path))
    expected = normalise(EXPECTED_MEDIA_TOP3)
    assert actual == expected, (
        f"media_top3.txt content mismatch.\n"
        f"Expected:\n{expected}\n\nActual:\n{actual}"
    )


def test_logs_summary_content():
    path = os.path.join(BACKUP_DIR, 'logs_summary.txt')
    assert os.path.isfile(path), f"File missing: {path!r}"
    actual = normalise(read_file(path))
    expected = normalise(EXPECTED_LOGS_SUMMARY)
    assert actual == expected, (
        f"logs_summary.txt content mismatch.\n"
        f"Expected:\n{expected}\n\nActual:\n{actual}"
    )


def test_logs_top3_content():
    path = os.path.join(BACKUP_DIR, 'logs_top3.txt')
    assert os.path.isfile(path), f"File missing: {path!r}"
    actual = normalise(read_file(path))
    expected = normalise(EXPECTED_LOGS_TOP3)
    assert actual == expected, (
        f"logs_top3.txt content mismatch.\n"
        f"Expected:\n{expected}\n\nActual:\n{actual}"
    )


def test_databases_summary_content():
    path = os.path.join(BACKUP_DIR, 'databases_summary.txt')
    assert os.path.isfile(path), f"File missing: {path!r}"
    actual = normalise(read_file(path))
    expected = normalise(EXPECTED_DATABASES_SUMMARY)
    assert actual == expected, (
        f"databases_summary.txt content mismatch.\n"
        f"Expected:\n{expected}\n\nActual:\n{actual}"
    )


def test_databases_top3_content():
    path = os.path.join(BACKUP_DIR, 'databases_top3.txt')
    assert os.path.isfile(path), f"File missing: {path!r}"
    actual = normalise(read_file(path))
    expected = normalise(EXPECTED_DATABASES_TOP3)
    assert actual == expected, (
        f"databases_top3.txt content mismatch.\n"
        f"Expected:\n{expected}\n\nActual:\n{actual}"
    )


# ── Content test: master report ───────────────────────────────────────────────

def test_master_report_content():
    path = os.path.join(BACKUP_DIR, 'master_report.txt')
    assert os.path.isfile(path), f"File missing: {path!r}"
    actual = normalise(read_file(path))
    expected = normalise(EXPECTED_MASTER_REPORT)
    assert actual == expected, (
        f"master_report.txt content mismatch.\n"
        f"Expected:\n{expected}\n\nActual:\n{actual}"
    )


# ── Fine-grained master report line checks ────────────────────────────────────

def _master_lines():
    path = os.path.join(BACKUP_DIR, 'master_report.txt')
    if not os.path.isfile(path):
        return []
    return [line.rstrip() for line in read_file(path).splitlines()]


def test_master_report_header():
    lines = _master_lines()
    assert lines, "master_report.txt is empty or missing"
    assert lines[0] == '=== BACKUP ANALYSIS REPORT ===', (
        f"First line of master_report.txt is wrong: {lines[0]!r}"
    )


def test_master_report_generated_from():
    lines = _master_lines()
    assert any('Generated from: /home/user/datastore' in l for l in lines), (
        "'Generated from: /home/user/datastore' not found in master_report.txt"
    )


def test_master_report_directory_summary_order():
    lines = _master_lines()
    # Extract the four numbered directory lines
    dir_lines = [l.strip() for l in lines if l.strip().startswith(('1.', '2.', '3.', '4.'))]
    assert len(dir_lines) >= 4, (
        f"Expected 4 numbered directory lines in master_report.txt, found: {dir_lines}"
    )
    assert 'media' in dir_lines[0], (
        f"Line 1 should be 'media', got: {dir_lines[0]!r}"
    )
    assert 'databases' in dir_lines[1], (
        f"Line 2 should be 'databases', got: {dir_lines[1]!r}"
    )
    assert 'projects' in dir_lines[2], (
        f"Line 3 should be 'projects', got: {dir_lines[2]!r}"
    )
    assert 'logs' in dir_lines[3], (
        f"Line 4 should be 'logs', got: {dir_lines[3]!r}"
    )


def test_master_report_grand_total():
    lines = _master_lines()
    assert any('GRAND TOTAL: 628504 bytes across 15 files' in l for l in lines), (
        "Grand total line 'GRAND TOTAL: 628504 bytes across 15 files' not found in master_report.txt"
    )


def test_master_report_exceeds_100kb():
    lines = _master_lines()
    assert any('Exceeds 100KB: databases, media' in l for l in lines), (
        "'Exceeds 100KB: databases, media' not found in master_report.txt"
    )


def test_master_report_exceeds_50kb():
    lines = _master_lines()
    assert any('Exceeds 50KB:  databases, logs, media, projects' in l for l in lines), (
        "'Exceeds 50KB:  databases, logs, media, projects' not found in master_report.txt"
    )


def test_master_report_largest_single_file():
    lines = _master_lines()
    assert any('media/videos/clip.mp4 (204800 bytes)' in l for l in lines), (
        "'media/videos/clip.mp4 (204800 bytes)' not found in master_report.txt"
    )


# ── Sanity: source datastore files are untouched ─────────────────────────────

@pytest.mark.parametrize("filepath,expected_size", [
    ('/home/user/datastore/projects/alpha/main.c', 18200),
    ('/home/user/datastore/projects/alpha/README.md', 512),
    ('/home/user/datastore/projects/beta/app.py', 43008),
    ('/home/user/datastore/projects/beta/config.yaml', 1024),
    ('/home/user/datastore/projects/shared/utils.py', 7680),
    ('/home/user/datastore/media/images/photo1.jpg', 92160),
    ('/home/user/datastore/media/images/photo2.jpg', 87040),
    ('/home/user/datastore/media/videos/clip.mp4', 204800),
    ('/home/user/datastore/media/thumbs/thumb1.png', 3072),
    ('/home/user/datastore/logs/app/app.log', 34816),
    ('/home/user/datastore/logs/app/error.log', 8192),
    ('/home/user/datastore/logs/system/syslog', 15360),
    ('/home/user/datastore/databases/db1.sqlite', 46080),
    ('/home/user/datastore/databases/db2.sqlite', 20480),
    ('/home/user/datastore/databases/backups/db1_bak.sqlite', 46080),
])
def test_source_file_intact(filepath, expected_size):
    assert os.path.isfile(filepath), (
        f"Source file {filepath!r} is missing — it must not be deleted."
    )
    actual = os.path.getsize(filepath)
    assert actual == expected_size, (
        f"Source file {filepath!r} has been modified: "
        f"expected {expected_size} bytes, got {actual} bytes."
    )