# test_final_state.py

import os
import pytest

LOG_FILE = "/home/user/storage/file_audit.log"
REPORT_FILE = "/home/user/storage/disk_report.txt"

EXPECTED_REPORT = """\
=== DISK USAGE REPORT ===

-- Top 3 Users by File Count --
1. alice: 8 files
2. bob: 7 files
3. charlie: 6 files

-- Top 5 Extensions by File Count --
1. jpg: 5 files
2. log: 5 files
3. pdf: 5 files
4. (none): 4 files
5. csv: 4 files

-- Summary --
Total files: 30
Total unique users: 5
Total unique extensions: 8
"""

EXPECTED_LOG_CONTENT = (
    "204800\talice\t/data/projects/report.pdf\n"
    "512000\tbob\t/data/projects/summary.pdf\n"
    "102400\talice\t/data/logs/access.log\n"
    "307200\tcharlie\t/data/media/photo.jpg\n"
    "819200\talice\t/data/projects/presentation.pptx\n"
    "204800\tbob\t/data/reports/budget.xlsx\n"
    "102400\tdiana\t/data/logs/error.log\n"
    "409600\talice\t/data/media/banner.jpg\n"
    "614400\tbob\t/data/projects/design.pdf\n"
    "102400\tcharlie\t/data/scripts/deploy\n"
    "204800\tdiana\t/data/projects/notes.txt\n"
    "307200\talice\t/data/reports/q1.pdf\n"
    "204800\tbob\t/data/logs/server.log\n"
    "102400\teve\t/data/scripts/backup\n"
    "512000\tcharlie\t/data/projects/data.csv\n"
    "204800\tdiana\t/data/media/logo.jpg\n"
    "102400\talice\t/data/scripts/setup\n"
    "307200\tbob\t/data/media/diagram.jpg\n"
    "204800\teve\t/data/projects/readme.txt\n"
    "102400\tcharlie\t/data/logs/app.log\n"
    "409600\talice\t/data/data/export.csv\n"
    "204800\tdiana\t/data/data/import.csv\n"
    "307200\teve\t/data/projects/plan.pdf\n"
    "102400\tbob\t/data/scripts/init\n"
    "204800\tcharlie\t/data/reports/analysis.xlsx\n"
    "307200\talice\t/data/projects/spec.txt\n"
    "204800\tdiana\t/data/logs/debug.log\n"
    "512000\teve\t/data/data/results.csv\n"
    "102400\tbob\t/data/data/config.txt\n"
    "204800\tcharlie\t/data/media/thumbnail.jpg\n"
)


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def read_report():
    with open(REPORT_FILE, "r", newline="") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# Tests for the report file existence and basic properties
# ---------------------------------------------------------------------------

def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file '{REPORT_FILE}' does not exist. "
        "The task requires writing a disk_report.txt file."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_FILE, os.R_OK), (
        f"Report file '{REPORT_FILE}' exists but is not readable."
    )


# ---------------------------------------------------------------------------
# Tests for unix line endings (no \r)
# ---------------------------------------------------------------------------

def test_report_no_carriage_returns():
    content = read_report()
    assert "\r" not in content, (
        f"Report file '{REPORT_FILE}' contains carriage-return characters (\\r). "
        "The file must use Unix line endings (LF only)."
    )


# ---------------------------------------------------------------------------
# Tests for exact content
# ---------------------------------------------------------------------------

def test_report_exact_content():
    content = read_report()
    assert content == EXPECTED_REPORT, (
        f"Report file '{REPORT_FILE}' does not match the expected content.\n\n"
        f"EXPECTED ({len(EXPECTED_REPORT)} chars):\n{EXPECTED_REPORT!r}\n\n"
        f"ACTUAL   ({len(content)} chars):\n{content!r}"
    )


# ---------------------------------------------------------------------------
# Fine-grained section tests (provide clear failure messages)
# ---------------------------------------------------------------------------

def test_report_header():
    content = read_report()
    assert content.startswith("=== DISK USAGE REPORT ===\n"), (
        f"Report does not start with '=== DISK USAGE REPORT ===' on the first line.\n"
        f"Actual first line: {content.splitlines()[0]!r}"
    )


def test_report_top3_users_section_present():
    content = read_report()
    assert "-- Top 3 Users by File Count --" in content, (
        "Report is missing the section header '-- Top 3 Users by File Count --'."
    )


def test_report_top3_users_values():
    content = read_report()
    expected_lines = [
        "1. alice: 8 files",
        "2. bob: 7 files",
        "3. charlie: 6 files",
    ]
    for line in expected_lines:
        assert line in content, (
            f"Expected line not found in report: {line!r}\n"
            f"Full report content:\n{content}"
        )


def test_report_top5_extensions_section_present():
    content = read_report()
    assert "-- Top 5 Extensions by File Count --" in content, (
        "Report is missing the section header '-- Top 5 Extensions by File Count --'."
    )


def test_report_top5_extensions_values():
    content = read_report()
    expected_lines = [
        "1. jpg: 5 files",
        "2. log: 5 files",
        "3. pdf: 5 files",
        "4. (none): 4 files",
        "5. csv: 4 files",
    ]
    for line in expected_lines:
        assert line in content, (
            f"Expected line not found in report: {line!r}\n"
            f"Full report content:\n{content}"
        )


def test_report_summary_section_present():
    content = read_report()
    assert "-- Summary --" in content, (
        "Report is missing the section header '-- Summary --'."
    )


def test_report_summary_total_files():
    content = read_report()
    assert "Total files: 30" in content, (
        "Report does not contain 'Total files: 30' in the Summary section.\n"
        f"Full report content:\n{content}"
    )


def test_report_summary_total_unique_users():
    content = read_report()
    assert "Total unique users: 5" in content, (
        "Report does not contain 'Total unique users: 5' in the Summary section.\n"
        f"Full report content:\n{content}"
    )


def test_report_summary_total_unique_extensions():
    content = read_report()
    assert "Total unique extensions: 8" in content, (
        "Report does not contain 'Total unique extensions: 8' in the Summary section.\n"
        "Remember: (none) counts as an extension label, so there are 8 unique extensions "
        "(jpg, log, pdf, csv, txt, xlsx, pptx, (none)).\n"
        f"Full report content:\n{content}"
    )


def test_report_no_trailing_spaces():
    content = read_report()
    lines = content.split("\n")
    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} in report has trailing whitespace: {line!r}"
        )


# ---------------------------------------------------------------------------
# Test that the original log file was NOT modified
# ---------------------------------------------------------------------------

def test_log_file_unchanged():
    assert os.path.isfile(LOG_FILE), (
        f"Original log file '{LOG_FILE}' no longer exists — it must not be deleted."
    )
    with open(LOG_FILE, "r", newline="") as fh:
        actual = fh.read()
    # Normalise: allow trailing newline differences for comparison
    actual_stripped = actual.rstrip("\n")
    expected_stripped = EXPECTED_LOG_CONTENT.rstrip("\n")
    assert actual_stripped == expected_stripped, (
        f"The original log file '{LOG_FILE}' has been modified!\n"
        f"The task explicitly states: 'Do not modify the original file_audit.log'.\n\n"
        f"EXPECTED (stripped):\n{expected_stripped!r}\n\n"
        f"ACTUAL   (stripped):\n{actual_stripped!r}"
    )