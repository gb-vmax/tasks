# test_final_state.py

import os
import pytest

REPORT_FILE = "/home/user/backups/restore_verification.txt"

EXPECTED_CONTENT = """\
=== RESTORE VERIFICATION REPORT ===
Successful backups eligible for restore testing:

  JOB003  fileserver01        1523 MB   ( 95 sec)
  JOB005  webserver02         4096 MB   (210 sec)

Total eligible: 2 jobs, 5619 MB"""


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file '{REPORT_FILE}' does not exist. "
        "The student must create this file as part of the task."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_FILE, os.R_OK), (
        f"Report file '{REPORT_FILE}' exists but is not readable."
    )


def test_report_file_exact_content():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    # Strip a single trailing newline if present (common with shell redirects)
    actual = content.rstrip("\n")

    assert actual == EXPECTED_CONTENT, (
        f"Report file '{REPORT_FILE}' does not match expected content.\n\n"
        f"=== EXPECTED (repr) ===\n{repr(EXPECTED_CONTENT)}\n\n"
        f"=== ACTUAL (repr) ===\n{repr(actual)}\n\n"
        f"=== EXPECTED ===\n{EXPECTED_CONTENT}\n\n"
        f"=== ACTUAL ===\n{actual}"
    )


def test_report_header_line():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, "Report file is empty."
    assert lines[0] == "=== RESTORE VERIFICATION REPORT ===", (
        f"First line of report is wrong.\n"
        f"Expected: '=== RESTORE VERIFICATION REPORT ==='\n"
        f"Got:      '{lines[0]}'"
    )


def test_report_subheader_line():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 2, "Report file has fewer than 2 lines."
    assert lines[1] == "Successful backups eligible for restore testing:", (
        f"Second line of report is wrong.\n"
        f"Expected: 'Successful backups eligible for restore testing:'\n"
        f"Got:      '{lines[1]}'"
    )


def test_report_blank_line_after_subheader():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 3, "Report file has fewer than 3 lines."
    assert lines[2] == "", (
        f"Third line (after subheader) should be blank.\n"
        f"Got: '{lines[2]}'"
    )


def test_report_job_lines():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    expected_job_lines = [
        "  JOB003  fileserver01        1523 MB   ( 95 sec)",
        "  JOB005  webserver02         4096 MB   (210 sec)",
    ]

    assert len(lines) >= 5, (
        f"Report file has fewer than 5 lines (expected at least header + subheader + blank + 2 jobs)."
    )

    assert lines[3] == expected_job_lines[0], (
        f"Job line 1 (line 4) is wrong.\n"
        f"Expected: '{expected_job_lines[0]}'\n"
        f"Got:      '{lines[3]}'\n"
        f"Expected (repr): {repr(expected_job_lines[0])}\n"
        f"Got (repr):      {repr(lines[3])}"
    )

    assert lines[4] == expected_job_lines[1], (
        f"Job line 2 (line 5) is wrong.\n"
        f"Expected: '{expected_job_lines[1]}'\n"
        f"Got:      '{lines[4]}'\n"
        f"Expected (repr): {repr(expected_job_lines[1])}\n"
        f"Got (repr):      {repr(lines[4])}"
    )


def test_report_blank_line_before_summary():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 6, (
        f"Report file has fewer than 6 lines (expected blank line before summary)."
    )
    assert lines[5] == "", (
        f"Line 6 (before summary) should be blank.\n"
        f"Got: '{lines[5]}'"
    )


def test_report_summary_line():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 7, (
        f"Report file has fewer than 7 lines (missing summary line)."
    )
    assert lines[6] == "Total eligible: 2 jobs, 5619 MB", (
        f"Summary line (line 7) is wrong.\n"
        f"Expected: 'Total eligible: 2 jobs, 5619 MB'\n"
        f"Got:      '{lines[6]}'"
    )


def test_report_line_count():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    # Strip a single trailing newline if present
    lines = content.rstrip("\n").splitlines()

    assert len(lines) == 7, (
        f"Report file should have exactly 7 lines, but has {len(lines)}.\n"
        f"Lines:\n" + "\n".join(f"  [{i+1}]: {repr(l)}" for i, l in enumerate(lines))
    )


def test_report_job_line_formatting_details():
    """Check character-level formatting of each job line."""
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    # Line 4 (index 3): JOB003
    line1 = lines[3]
    # Check 2-space indent
    assert line1[:2] == "  ", (
        f"Job line 1 should start with 2 spaces. Got: {repr(line1[:2])}"
    )
    # Check job_id field (8 chars, left-aligned): "JOB003  "
    assert line1[2:10] == "JOB003  ", (
        f"Job line 1 job_id field (chars 3-10) should be 'JOB003  ' (8 chars). "
        f"Got: {repr(line1[2:10])}"
    )
    # Check hostname field (20 chars, left-aligned): "fileserver01        "
    assert line1[10:30] == "fileserver01        ", (
        f"Job line 1 hostname field (chars 11-30) should be 'fileserver01        ' (20 chars). "
        f"Got: {repr(line1[10:30])}"
    )
    # Check size field (4 chars right-aligned) + " MB": "1523 MB"
    assert line1[30:37] == "1523 MB", (
        f"Job line 1 size+MB field (chars 31-37) should be '1523 MB'. "
        f"Got: {repr(line1[30:37])}"
    )
    # Check "   (" separator
    assert line1[37:41] == "   (", (
        f"Job line 1 separator (chars 38-41) should be '   ('. "
        f"Got: {repr(line1[37:41])}"
    )
    # Check duration " 95 sec)"
    assert line1[41:] == " 95 sec)", (
        f"Job line 1 duration should be ' 95 sec)'. "
        f"Got: {repr(line1[41:])}"
    )

    # Line 5 (index 4): JOB005
    line2 = lines[4]
    # Check 2-space indent
    assert line2[:2] == "  ", (
        f"Job line 2 should start with 2 spaces. Got: {repr(line2[:2])}"
    )
    # Check job_id field (8 chars, left-aligned): "JOB005  "
    assert line2[2:10] == "JOB005  ", (
        f"Job line 2 job_id field (chars 3-10) should be 'JOB005  ' (8 chars). "
        f"Got: {repr(line2[2:10])}"
    )
    # Check hostname field (20 chars, left-aligned): "webserver02         "
    assert line2[10:30] == "webserver02         ", (
        f"Job line 2 hostname field (chars 11-30) should be 'webserver02         ' (20 chars). "
        f"Got: {repr(line2[10:30])}"
    )
    # Check size field (4 chars right-aligned) + " MB": "4096 MB"
    assert line2[30:37] == "4096 MB", (
        f"Job line 2 size+MB field (chars 31-37) should be '4096 MB'. "
        f"Got: {repr(line2[30:37])}"
    )
    # Check "   (" separator
    assert line2[37:41] == "   (", (
        f"Job line 2 separator (chars 38-41) should be '   ('. "
        f"Got: {repr(line2[37:41])}"
    )
    # Check duration "210 sec)"
    assert line2[41:] == "210 sec)", (
        f"Job line 2 duration should be '210 sec)'. "
        f"Got: {repr(line2[41:])}"
    )


def test_report_only_eligible_jobs_present():
    """Verify that excluded jobs (JOB001, JOB002, JOB004, JOB006, JOB007) are not in the report."""
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    excluded_jobs = ["JOB001", "JOB002", "JOB004", "JOB006", "JOB007"]
    for job in excluded_jobs:
        assert job not in content, (
            f"Report file should not contain excluded job '{job}', but it does.\n"
            f"Job '{job}' was excluded because it either failed or had size <= 1000 MB."
        )


def test_report_contains_eligible_jobs():
    """Verify that eligible jobs (JOB003, JOB005) are present in the report."""
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    for job in ["JOB003", "JOB005"]:
        assert job in content, (
            f"Report file should contain eligible job '{job}', but it does not."
        )


def test_report_total_size_correct():
    """Verify the total size in the summary is 5619 MB."""
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    summary = lines[6] if len(lines) >= 7 else ""
    assert "5619" in summary, (
        f"Summary line should contain total size '5619'. Got: '{summary}'"
    )


def test_report_total_count_correct():
    """Verify the job count in the summary is 2."""
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    summary = lines[6] if len(lines) >= 7 else ""
    assert "2 jobs" in summary, (
        f"Summary line should contain '2 jobs'. Got: '{summary}'"
    )