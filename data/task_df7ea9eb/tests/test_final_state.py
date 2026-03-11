# test_final_state.py

import os
import pytest

SUMMARY_PATH = "/home/user/backups/archive_summary.txt"
LOG_PATH = "/home/user/backups/backup_nightly.log"
BACKUPS_DIR = "/home/user/backups"

EXPECTED_LINES = [
    "Job: db_primary_backup | Completed at: 2024-11-03 02:14:37",
    "Job: media_archive | Completed at: 2024-11-03 02:31:05",
    "Job: config_snapshot | Completed at: 2024-11-03 02:35:02",
    "Job: userdata_weekly | Completed at: 2024-11-03 03:58:21",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES) + "\n"


def test_backups_directory_still_exists():
    assert os.path.isdir(BACKUPS_DIR), (
        f"Directory '{BACKUPS_DIR}' does not exist. "
        "The backups directory must still be present after the task."
    )


def test_log_file_still_exists():
    assert os.path.isfile(LOG_PATH), (
        f"Log file '{LOG_PATH}' does not exist. "
        "The original log file must not be removed or altered."
    )


def test_archive_summary_exists():
    assert os.path.isfile(SUMMARY_PATH), (
        f"Output file '{SUMMARY_PATH}' does not exist. "
        "The student's solution must create this file."
    )


def test_archive_summary_is_readable():
    assert os.access(SUMMARY_PATH, os.R_OK), (
        f"Output file '{SUMMARY_PATH}' is not readable. "
        "The file must be readable after creation."
    )


def test_archive_summary_line_count():
    with open(SUMMARY_PATH, "r") as f:
        lines = [line for line in f.readlines() if line.strip()]
    assert len(lines) == 4, (
        f"Expected exactly 4 non-empty lines in '{SUMMARY_PATH}', "
        f"but found {len(lines)}. Lines found:\n" +
        "\n".join(repr(l) for l in lines)
    )


def test_archive_summary_exact_content():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    # Accept with or without a single trailing newline, but no blank lines
    stripped = content.rstrip("\n")
    actual_lines = stripped.split("\n")

    assert actual_lines == EXPECTED_LINES, (
        f"Content of '{SUMMARY_PATH}' does not match expected.\n"
        f"Expected lines:\n" + "\n".join(repr(l) for l in EXPECTED_LINES) + "\n\n"
        f"Actual lines:\n" + "\n".join(repr(l) for l in actual_lines)
    )


def test_archive_summary_no_blank_lines():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"Found blank lines in '{SUMMARY_PATH}' at line numbers: {blank_lines}. "
        "The output must contain no blank lines."
    )


def test_archive_summary_no_header_or_footer():
    with open(SUMMARY_PATH, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    for line in lines:
        assert line.startswith("Job: "), (
            f"Found a line that does not start with 'Job: ': {repr(line)}. "
            "There should be no header, footer, or extra lines."
        )


def test_archive_summary_line_format():
    import re
    pattern = re.compile(
        r"^Job: (\S+) \| Completed at: (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})$"
    )
    with open(SUMMARY_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines() if line.strip()]

    for line in lines:
        match = pattern.match(line)
        assert match is not None, (
            f"Line does not match expected format "
            f"'Job: <name> | Completed at: <YYYY-MM-DD> <HH:MM:SS>'.\n"
            f"Offending line: {repr(line)}"
        )


def test_archive_summary_correct_job_names():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read().rstrip("\n")

    actual_lines = content.split("\n")
    actual_jobs = []
    for line in actual_lines:
        if line.strip():
            # Extract job name after "Job: " and before " |"
            parts = line.split(" | ")
            job_part = parts[0]  # "Job: <name>"
            job_name = job_part[len("Job: "):]
            actual_jobs.append(job_name)

    expected_jobs = [
        "db_primary_backup",
        "media_archive",
        "config_snapshot",
        "userdata_weekly",
    ]
    assert actual_jobs == expected_jobs, (
        f"Job names or order do not match.\n"
        f"Expected: {expected_jobs}\n"
        f"Actual:   {actual_jobs}"
    )


def test_archive_summary_logs_offsite_excluded():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "logs_offsite" not in content, (
        f"'logs_offsite' should NOT appear in '{SUMMARY_PATH}' because it FAILED. "
        "Only COMPLETED jobs should be included."
    )


def test_archive_summary_started_excluded():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "STARTED" not in content, (
        f"'STARTED' lines should not appear in '{SUMMARY_PATH}'. "
        "Only COMPLETED jobs should be included."
    )


def test_archive_summary_failed_excluded():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "FAILED" not in content, (
        f"'FAILED' lines should not appear in '{SUMMARY_PATH}'. "
        "Only COMPLETED jobs should be included."
    )


def test_archive_summary_warning_excluded():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "WARNING" not in content, (
        f"'WARNING' lines should not appear in '{SUMMARY_PATH}'. "
        "Only COMPLETED jobs should be included."
    )


def test_archive_summary_info_excluded():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    assert "] INFO " not in content, (
        f"'INFO' lines should not appear in '{SUMMARY_PATH}'. "
        "Only COMPLETED jobs should be included."
    )


def test_archive_summary_correct_timestamps():
    expected_timestamps = {
        "db_primary_backup": "2024-11-03 02:14:37",
        "media_archive": "2024-11-03 02:31:05",
        "config_snapshot": "2024-11-03 02:35:02",
        "userdata_weekly": "2024-11-03 03:58:21",
    }

    with open(SUMMARY_PATH, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    for line in lines:
        # Parse: "Job: <name> | Completed at: <timestamp>"
        parts = line.split(" | ")
        assert len(parts) == 2, (
            f"Line cannot be split into two parts by ' | ': {repr(line)}"
        )
        job_name = parts[0][len("Job: "):]
        timestamp = parts[1][len("Completed at: "):]

        if job_name in expected_timestamps:
            assert timestamp == expected_timestamps[job_name], (
                f"Timestamp for job '{job_name}' is wrong.\n"
                f"Expected: {expected_timestamps[job_name]}\n"
                f"Actual:   {timestamp}"
            )


def test_archive_summary_order_matches_log():
    """Verify lines appear in the same order as in the original log."""
    with open(SUMMARY_PATH, "r") as f:
        summary_lines = [line.strip() for line in f.readlines() if line.strip()]

    expected_order = [
        "db_primary_backup",
        "media_archive",
        "config_snapshot",
        "userdata_weekly",
    ]

    actual_order = []
    for line in summary_lines:
        parts = line.split(" | ")
        job_name = parts[0][len("Job: "):]
        actual_order.append(job_name)

    assert actual_order == expected_order, (
        f"Jobs are not in the same order as they appear in the log.\n"
        f"Expected order: {expected_order}\n"
        f"Actual order:   {actual_order}"
    )


def test_log_file_unchanged():
    """Ensure the original log file was not modified."""
    EXPECTED_LOG_CONTENT = """\
[2024-11-03 01:00:00] STARTED db_primary_backup
[2024-11-03 01:00:03] INFO Connecting to database host db01.internal
[2024-11-03 01:00:05] STARTED media_archive
[2024-11-03 02:14:37] COMPLETED db_primary_backup
[2024-11-03 02:14:40] WARNING Disk usage on backup target at 78%
[2024-11-03 02:31:05] COMPLETED media_archive
[2024-11-03 02:31:06] STARTED config_snapshot
[2024-11-03 02:31:10] INFO Snapshotting /etc and /home/user/.config
[2024-11-03 02:31:11] STARTED logs_offsite
[2024-11-03 02:33:44] FAILED logs_offsite
[2024-11-03 02:33:44] INFO Remote host unreachable, skipping offsite transfer
[2024-11-03 02:35:02] COMPLETED config_snapshot
[2024-11-03 02:35:03] STARTED userdata_weekly
[2024-11-03 03:58:21] COMPLETED userdata_weekly
[2024-11-03 03:58:25] INFO All jobs finished"""

    with open(LOG_PATH, "r") as f:
        content = f.read()

    actual = content.rstrip("\n")
    assert actual == EXPECTED_LOG_CONTENT, (
        f"The original log file '{LOG_PATH}' was modified!\n"
        f"Expected:\n{EXPECTED_LOG_CONTENT}\n\n"
        f"Actual:\n{actual}"
    )