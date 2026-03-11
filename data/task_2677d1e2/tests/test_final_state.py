# test_final_state.py

import os
import pytest

LOG_FILE = "/home/user/migration/services.log"
OUTPUT_FILE = "/home/user/migration/failed_services.txt"
MIGRATION_DIR = "/home/user/migration"

EXPECTED_FAILED_SERVICES = ["api-gateway", "billing-service", "data-pipeline", "payment-processor"]
EXPECTED_OUTPUT_CONTENT = "api-gateway\nbilling-service\ndata-pipeline\npayment-processor\n"


def test_migration_directory_still_exists():
    assert os.path.isdir(MIGRATION_DIR), (
        f"Migration directory '{MIGRATION_DIR}' does not exist. "
        "It should still be present after task completion."
    )


def test_log_file_still_exists():
    assert os.path.isfile(LOG_FILE), (
        f"Log file '{LOG_FILE}' does not exist. "
        "The original services.log must not be removed or altered."
    )


def test_output_file_exists():
    assert os.path.isfile(OUTPUT_FILE), (
        f"Output file '{OUTPUT_FILE}' does not exist. "
        "The task requires creating this file with the sorted failed service names."
    )


def test_output_file_is_readable():
    assert os.access(OUTPUT_FILE, os.R_OK), (
        f"Output file '{OUTPUT_FILE}' exists but is not readable."
    )


def test_output_file_line_count():
    with open(OUTPUT_FILE, "r") as f:
        lines = [line for line in f.read().splitlines() if line.strip()]
    assert len(lines) == 4, (
        f"Expected exactly 4 lines in '{OUTPUT_FILE}', but found {len(lines)}.\n"
        f"Lines found: {lines}\n"
        "The file should contain exactly one service name per line for each FAILED entry."
    )


def test_output_file_contains_correct_service_names():
    with open(OUTPUT_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines() if line.strip()]
    service_set = set(lines)
    expected_set = set(EXPECTED_FAILED_SERVICES)
    assert service_set == expected_set, (
        f"Output file '{OUTPUT_FILE}' contains incorrect service names.\n"
        f"Expected services: {sorted(expected_set)}\n"
        f"Found services:    {sorted(service_set)}\n"
        "Ensure only FAILED service names are extracted from the log."
    )


def test_output_file_is_sorted_alphabetically():
    with open(OUTPUT_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines() if line.strip()]
    assert lines == sorted(lines), (
        f"Service names in '{OUTPUT_FILE}' are not sorted alphabetically.\n"
        f"Current order:   {lines}\n"
        f"Expected order:  {sorted(lines)}\n"
        "Please sort the service names alphabetically."
    )


def test_output_file_exact_content():
    with open(OUTPUT_FILE, "r") as f:
        actual_content = f.read()
    assert actual_content == EXPECTED_OUTPUT_CONTENT, (
        f"Output file '{OUTPUT_FILE}' does not have the exact expected content.\n"
        f"Expected (repr): {EXPECTED_OUTPUT_CONTENT!r}\n"
        f"Actual   (repr): {actual_content!r}\n"
        "Check for extra spaces, blank lines, brackets, timestamps, or missing newlines."
    )


def test_output_file_no_extra_whitespace_per_line():
    with open(OUTPUT_FILE, "r") as f:
        lines = f.read().splitlines()
    # Filter out empty lines for this check
    non_empty_lines = [line for line in lines if line]
    for line in non_empty_lines:
        assert line == line.strip(), (
            f"Line {line!r} in '{OUTPUT_FILE}' has leading or trailing whitespace. "
            "Each line should contain only the bare service name."
        )


def test_output_file_no_brackets_or_timestamps():
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()
    assert "[" not in content and "]" not in content, (
        f"Output file '{OUTPUT_FILE}' contains bracket characters '[' or ']'.\n"
        "The file should contain only plain service names, no brackets or status tags."
    )
    assert "::" not in content, (
        f"Output file '{OUTPUT_FILE}' contains '::' separator.\n"
        "The file should contain only plain service names."
    )


def test_output_file_ends_with_newline():
    with open(OUTPUT_FILE, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"Output file '{OUTPUT_FILE}' does not end with a newline character.\n"
        "A standard text file should end with a newline after the last line."
    )


def test_output_file_no_trailing_blank_lines():
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()
    # Should end with exactly one newline after the last service name
    assert not content.endswith("\n\n"), (
        f"Output file '{OUTPUT_FILE}' has trailing blank lines.\n"
        f"Content (repr): {content!r}\n"
        "There should be no blank lines after the last service name."
    )


def test_original_log_file_unchanged():
    expected_log_content = (
        "[2024-06-10 08:01:32] [SUCCESS] auth-service :: Migrated to us-east-2 successfully\n"
        "[2024-06-10 08:03:11] [FAILED] billing-service :: Connection timeout during snapshot transfer\n"
        "[2024-06-10 08:07:45] [SKIPPED] legacy-reporting :: Marked for decommission, skipping migration\n"
        "[2024-06-10 08:09:02] [SUCCESS] user-profile-service :: All data synced and verified\n"
        "[2024-06-10 08:11:58] [FAILED] api-gateway :: TLS certificate mismatch on target region\n"
        "[2024-06-10 08:14:30] [SUCCESS] notification-service :: Migrated to us-east-2 successfully\n"
        "[2024-06-10 08:17:44] [FAILED] data-pipeline :: Disk quota exceeded on destination bucket\n"
        "[2024-06-10 08:20:05] [SKIPPED] internal-dashboard :: Dependency on legacy-reporting, skipping\n"
        "[2024-06-10 08:23:19] [SUCCESS] search-service :: Migrated to us-east-2 successfully\n"
        "[2024-06-10 08:26:52] [FAILED] payment-processor :: IAM role missing required S3 permissions"
    )
    with open(LOG_FILE, "r") as f:
        actual_content = f.read().rstrip("\n")
    assert actual_content == expected_log_content, (
        f"The original log file '{LOG_FILE}' has been modified.\n"
        "The task should only read from this file, not alter it."
    )