# test_final_state.py

import os
import pytest

SUMMARY_PATH = "/home/user/finops/cost_summary.txt"
CSV_PATH = "/home/user/finops/resources.csv"

EXPECTED_CONTENT = (
    "Monthly Cost Summary\n"
    "====================\n"
    "EC2: $265.75\n"
    "RDS: $445.75\n"
    "S3: $45.45\n"
    "====================\n"
    "Total: $756.95\n"
)


def test_finops_directory_exists():
    dirpath = "/home/user/finops"
    assert os.path.isdir(dirpath), (
        f"Directory '{dirpath}' does not exist. "
        "The /home/user/finops directory must be present."
    )


def test_csv_file_still_exists():
    assert os.path.isfile(CSV_PATH), (
        f"CSV file '{CSV_PATH}' no longer exists. "
        "The original resources.csv file must not be removed or modified."
    )


def test_summary_file_exists():
    assert os.path.isfile(SUMMARY_PATH), (
        f"Output file '{SUMMARY_PATH}' does not exist. "
        "The cost summary report must be written to this path."
    )


def test_summary_file_is_readable():
    assert os.access(SUMMARY_PATH, os.R_OK), (
        f"Output file '{SUMMARY_PATH}' is not readable. "
        "The file must be readable after the task."
    )


def test_summary_file_exact_content():
    with open(SUMMARY_PATH, "r") as f:
        actual = f.read()

    assert actual == EXPECTED_CONTENT, (
        f"Content of '{SUMMARY_PATH}' does not match expected.\n"
        f"Expected (repr): {repr(EXPECTED_CONTENT)}\n"
        f"Actual   (repr): {repr(actual)}"
    )


def test_summary_file_ends_with_single_newline():
    with open(SUMMARY_PATH, "rb") as f:
        raw = f.read()

    assert raw.endswith(b"\n"), (
        f"File '{SUMMARY_PATH}' does not end with a newline character."
    )
    assert not raw.endswith(b"\n\n"), (
        f"File '{SUMMARY_PATH}' ends with more than one newline character. "
        "It should end with exactly one newline."
    )


def test_summary_header_line():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 1, f"File '{SUMMARY_PATH}' is empty."
    assert lines[0].rstrip("\n") == "Monthly Cost Summary", (
        f"First line should be 'Monthly Cost Summary', got: {repr(lines[0].rstrip())}"
    )


def test_summary_separator_lines():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    separator = "===================="
    assert len(lines) >= 2, f"File '{SUMMARY_PATH}' has fewer than 2 lines."
    assert lines[1].rstrip("\n") == separator, (
        f"Second line should be '{separator}', got: {repr(lines[1].rstrip())}"
    )
    assert len(lines) >= 6, f"File '{SUMMARY_PATH}' has fewer than 6 lines."
    assert lines[5].rstrip("\n") == separator, (
        f"Sixth line should be '{separator}', got: {repr(lines[5].rstrip())}"
    )


def test_summary_ec2_line():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 3, f"File '{SUMMARY_PATH}' has fewer than 3 lines."
    ec2_line = lines[2].rstrip("\n")
    assert ec2_line == "EC2: $265.75", (
        f"EC2 line is incorrect. Expected 'EC2: $265.75', got: {repr(ec2_line)}"
    )


def test_summary_rds_line():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 4, f"File '{SUMMARY_PATH}' has fewer than 4 lines."
    rds_line = lines[3].rstrip("\n")
    assert rds_line == "RDS: $445.75", (
        f"RDS line is incorrect. Expected 'RDS: $445.75', got: {repr(rds_line)}"
    )


def test_summary_s3_line():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 5, f"File '{SUMMARY_PATH}' has fewer than 5 lines."
    s3_line = lines[4].rstrip("\n")
    assert s3_line == "S3: $45.45", (
        f"S3 line is incorrect. Expected 'S3: $45.45', got: {repr(s3_line)}"
    )


def test_summary_total_line():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 7, f"File '{SUMMARY_PATH}' has fewer than 7 lines."
    total_line = lines[6].rstrip("\n")
    assert total_line == "Total: $756.95", (
        f"Total line is incorrect. Expected 'Total: $756.95', got: {repr(total_line)}"
    )


def test_summary_services_in_alphabetical_order():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    # Lines 2, 3, 4 (0-indexed) are the service lines
    assert len(lines) >= 5, f"File '{SUMMARY_PATH}' has fewer than 5 lines."
    service_lines = [lines[2].rstrip("\n"), lines[3].rstrip("\n"), lines[4].rstrip("\n")]
    services = [line.split(":")[0] for line in service_lines]
    assert services == sorted(services), (
        f"Services are not in alphabetical order. Got: {services}"
    )


def test_summary_no_trailing_whitespace():
    with open(SUMMARY_PATH, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} has trailing whitespace: {repr(line)}"
        )


def test_summary_exact_line_count():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()

    lines = content.split("\n")
    # The file ends with \n so split produces an empty string at the end
    # Expected: 7 content lines + 1 empty string from trailing newline = 8 parts
    assert len(lines) == 8, (
        f"Expected exactly 7 lines followed by a single newline (8 parts when split by '\\n'), "
        f"but got {len(lines)} parts. Content repr: {repr(content)}"
    )
    assert lines[-1] == "", (
        f"Last element after split should be empty string (trailing newline), "
        f"got: {repr(lines[-1])}"
    )


def test_csv_file_content_unchanged():
    """Ensure the original CSV file was not modified."""
    expected_csv = (
        "resource_id,service,region,monthly_cost_usd\n"
        "i-0a1b2c3d,EC2,us-east-1,72.50\n"
        "i-0b2c3d4e,EC2,us-west-2,118.30\n"
        "db-0c3d4e5f,RDS,us-east-1,210.00\n"
        "db-0d4e5f6g,RDS,eu-west-1,95.75\n"
        "s3-0e5f6g7h,S3,us-east-1,14.40\n"
        "i-0f6g7h8i,EC2,ap-southeast-1,43.20\n"
        "s3-0g7h8i9j,S3,us-west-2,8.90\n"
        "db-0h8i9j0k,RDS,us-east-1,140.00\n"
        "i-0i9j0k1l,EC2,eu-west-1,31.75\n"
        "s3-0j0k1l2m,S3,us-east-1,22.15\n"
    )
    with open(CSV_PATH, "r") as f:
        actual = f.read()

    assert actual.strip() == expected_csv.strip(), (
        f"CSV file '{CSV_PATH}' content has been modified.\n"
        f"Expected (stripped):\n{expected_csv.strip()}\n\n"
        f"Actual (stripped):\n{actual.strip()}"
    )