# test_final_state.py

import os
import sqlite3
import pytest

REPORT_FILE = "/home/user/databases/migration_report.txt"
SOURCE_DB = "/home/user/databases/source.db"
MIGRATED_DB = "/home/user/databases/migrated.db"

EXPECTED_REPORT = """\
=== MIGRATION INTEGRITY REPORT ===

[CHECK 1] Row Count
  source: 5
  migrated: 4
  status: FAIL

[CHECK 2] Balance Sum
  source: 5800.50
  migrated: 5711.00
  status: FAIL

[CHECK 3] Email Uniqueness
  source distinct emails: 5
  migrated distinct emails: 4
  status: FAIL

[CHECK 4] Missing Records
  missing IDs: 3
  status: FAIL

=== OVERALL: FAIL ==="""


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Migration report file '{REPORT_FILE}' does not exist. "
        "The student must generate this file as part of the task."
    )


def test_report_file_exact_content():
    assert os.path.isfile(REPORT_FILE), (
        f"Cannot check content: '{REPORT_FILE}' does not exist."
    )
    with open(REPORT_FILE, "r") as f:
        actual = f.read()

    # Strip trailing newline for comparison if present
    actual_stripped = actual.rstrip("\n")
    expected_stripped = EXPECTED_REPORT.rstrip("\n")

    assert actual_stripped == expected_stripped, (
        f"Report file content does not match expected.\n"
        f"--- EXPECTED ---\n{expected_stripped}\n"
        f"--- ACTUAL ---\n{actual_stripped}\n"
        f"--- END ---\n"
        "Check spacing, capitalization, punctuation, and numeric formatting."
    )


def test_report_header():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "=== MIGRATION INTEGRITY REPORT ===" in content, (
        "Report is missing the header line '=== MIGRATION INTEGRITY REPORT ==='."
    )


def test_report_check1_row_count_source():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "  source: 5" in content, (
        "Check 1 (Row Count): Report should contain '  source: 5' "
        "indicating the source database has 5 rows."
    )


def test_report_check1_row_count_migrated():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "  migrated: 4" in content, (
        "Check 1 (Row Count): Report should contain '  migrated: 4' "
        "indicating the migrated database has 4 rows."
    )


def test_report_check1_status_fail():
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    # Find the [CHECK 1] section and verify its status line
    in_check1 = False
    for line in lines:
        if "[CHECK 1] Row Count" in line:
            in_check1 = True
        if in_check1 and line.strip().startswith("status:"):
            assert "FAIL" in line, (
                f"Check 1 (Row Count) status should be FAIL since row counts differ, "
                f"but got: '{line.strip()}'"
            )
            return
    pytest.fail("Could not find status line for [CHECK 1] Row Count in the report.")


def test_report_check2_balance_sum_source():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "  source: 5800.50" in content, (
        "Check 2 (Balance Sum): Report should contain '  source: 5800.50'. "
        "Balance must be formatted to exactly 2 decimal places."
    )


def test_report_check2_balance_sum_migrated():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "  migrated: 5711.00" in content, (
        "Check 2 (Balance Sum): Report should contain '  migrated: 5711.00'. "
        "Balance must be formatted to exactly 2 decimal places."
    )


def test_report_check2_status_fail():
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    in_check2 = False
    for line in lines:
        if "[CHECK 2] Balance Sum" in line:
            in_check2 = True
        if in_check2 and line.strip().startswith("status:"):
            assert "FAIL" in line, (
                f"Check 2 (Balance Sum) status should be FAIL since sums differ, "
                f"but got: '{line.strip()}'"
            )
            return
    pytest.fail("Could not find status line for [CHECK 2] Balance Sum in the report.")


def test_report_check3_email_uniqueness_source():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "  source distinct emails: 5" in content, (
        "Check 3 (Email Uniqueness): Report should contain "
        "'  source distinct emails: 5'."
    )


def test_report_check3_email_uniqueness_migrated():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "  migrated distinct emails: 4" in content, (
        "Check 3 (Email Uniqueness): Report should contain "
        "'  migrated distinct emails: 4'."
    )


def test_report_check3_status_fail():
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    in_check3 = False
    for line in lines:
        if "[CHECK 3] Email Uniqueness" in line:
            in_check3 = True
        if in_check3 and line.strip().startswith("status:"):
            assert "FAIL" in line, (
                f"Check 3 (Email Uniqueness) status should be FAIL since distinct "
                f"email counts differ, but got: '{line.strip()}'"
            )
            return
    pytest.fail("Could not find status line for [CHECK 3] Email Uniqueness in the report.")


def test_report_check4_missing_ids():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "  missing IDs: 3" in content, (
        "Check 4 (Missing Records): Report should contain '  missing IDs: 3' "
        "since id=3 is present in source but missing from migrated database."
    )


def test_report_check4_status_fail():
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    in_check4 = False
    for line in lines:
        if "[CHECK 4] Missing Records" in line:
            in_check4 = True
        if in_check4 and line.strip().startswith("status:"):
            assert "FAIL" in line, (
                f"Check 4 (Missing Records) status should be FAIL since there are "
                f"missing IDs, but got: '{line.strip()}'"
            )
            return
    pytest.fail("Could not find status line for [CHECK 4] Missing Records in the report.")


def test_report_overall_fail():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "=== OVERALL: FAIL ===" in content, (
        "The overall status line should be '=== OVERALL: FAIL ===' since not all "
        "checks passed. Found content does not contain this line."
    )


def test_report_overall_not_pass():
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    assert "=== OVERALL: PASS ===" not in content, (
        "The overall status line should NOT be '=== OVERALL: PASS ===' since "
        "checks 1-4 all failed."
    )


def test_report_check_section_headers_present():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    for header in [
        "[CHECK 1] Row Count",
        "[CHECK 2] Balance Sum",
        "[CHECK 3] Email Uniqueness",
        "[CHECK 4] Missing Records",
    ]:
        assert header in content, (
            f"Report is missing the section header '{header}'."
        )


def test_report_no_pass_statuses():
    """All four checks should be FAIL, not PASS."""
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    status_lines = [line.strip() for line in lines if line.strip().startswith("status:")]
    assert len(status_lines) == 4, (
        f"Expected exactly 4 'status:' lines in the report, found {len(status_lines)}. "
        f"Status lines found: {status_lines}"
    )
    for status_line in status_lines:
        assert status_line == "status: FAIL", (
            f"All check statuses should be 'status: FAIL', but found: '{status_line}'. "
            "All four integrity checks should fail given the data discrepancies."
        )


def test_report_balance_formatting_no_single_decimal():
    """Ensure balance values are not formatted with a single decimal place."""
    with open(REPORT_FILE, "r") as f:
        content = f.read()
    # These would be wrong formats
    assert "5800.5\n" not in content and "5800.5 " not in content, (
        "Balance 5800.50 must be formatted with exactly 2 decimal places, "
        "not as '5800.5'."
    )
    assert "5711.0\n" not in content and "5711.0 " not in content, (
        "Balance 5711.00 must be formatted with exactly 2 decimal places, "
        "not as '5711.0'."
    )


def test_source_db_unchanged():
    """Verify the source database was not modified during the report generation."""
    conn = sqlite3.connect(SOURCE_DB)
    cursor = conn.execute("SELECT COUNT(*) FROM customers")
    count = cursor.fetchone()[0]
    conn.close()
    assert count == 5, (
        f"Source database should still have 5 rows after report generation, "
        f"but found {count}. The source database must not be modified."
    )


def test_migrated_db_unchanged():
    """Verify the migrated database was not modified during the report generation."""
    conn = sqlite3.connect(MIGRATED_DB)
    cursor = conn.execute("SELECT COUNT(*) FROM customers")
    count = cursor.fetchone()[0]
    conn.close()
    assert count == 4, (
        f"Migrated database should still have 4 rows after report generation, "
        f"but found {count}. The migrated database must not be modified."
    )