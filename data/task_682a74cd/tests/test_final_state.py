# test_final_state.py

import os
import pytest

OUTPUT_FILE = "/home/user/finops/aws_costs_reordered.csv"
INPUT_FILE = "/home/user/finops/aws_costs.csv"

EXPECTED_CONTENT = """team,account_id,region,service,cost_usd,usage_hours
platform,123456789012,us-east-1,EC2,412.50,1200
platform,123456789012,us-west-2,S3,18.75,0
data,987654321098,eu-west-1,RDS,930.00,720
backend,555000111222,ap-southeast-1,Lambda,7.30,45000
frontend,987654321098,us-east-1,CloudFront,53.20,0
data,555000111222,eu-central-1,EC2,601.80,1800
backend,123456789012,us-west-2,DynamoDB,144.00,0
frontend,987654321098,ap-northeast-1,S3,22.10,0"""

EXPECTED_LINES = EXPECTED_CONTENT.strip().splitlines()


def test_output_file_exists():
    assert os.path.isfile(OUTPUT_FILE), (
        f"Output file does not exist: {OUTPUT_FILE}. "
        "The reordered CSV file was not created."
    )


def test_output_file_is_readable():
    assert os.access(OUTPUT_FILE, os.R_OK), (
        f"Output file is not readable: {OUTPUT_FILE}"
    )


def test_output_file_has_9_lines():
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").splitlines()
    assert len(lines) == 9, (
        f"Expected 9 lines (1 header + 8 data rows) in {OUTPUT_FILE}, got {len(lines)}.\n"
        f"Actual content:\n{content}"
    )


def test_output_file_header():
    with open(OUTPUT_FILE, "r") as f:
        header = f.readline().rstrip("\n")
    expected_header = "team,account_id,region,service,cost_usd,usage_hours"
    assert header == expected_header, (
        f"Header row mismatch in {OUTPUT_FILE}:\n"
        f"  Expected: {expected_header!r}\n"
        f"  Actual:   {header!r}\n"
        "The columns must be reordered to: team, account_id, region, service, cost_usd, usage_hours"
    )


def test_output_file_is_comma_delimited():
    with open(OUTPUT_FILE, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    for i, line in enumerate(lines):
        fields = line.split(",")
        assert len(fields) == 6, (
            f"Line {i+1} in {OUTPUT_FILE} does not have 6 comma-separated fields.\n"
            f"  Line: {line!r}\n"
            f"  Fields found: {fields}"
        )


def test_output_file_exact_content():
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()
    actual_lines = content.rstrip("\n").splitlines()

    assert len(actual_lines) == len(EXPECTED_LINES), (
        f"Expected {len(EXPECTED_LINES)} lines, got {len(actual_lines)}.\n"
        f"Actual content:\n{content}"
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, EXPECTED_LINES)):
        assert actual == expected, (
            f"Line {i+1} mismatch in {OUTPUT_FILE}:\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}\n"
            "Check that columns are reordered correctly and values are preserved exactly."
        )


def test_output_column_order_is_correct():
    with open(OUTPUT_FILE, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    header = lines[0].split(",")
    expected_order = ["team", "account_id", "region", "service", "cost_usd", "usage_hours"]
    assert header == expected_order, (
        f"Column order is wrong.\n"
        f"  Expected: {expected_order}\n"
        f"  Actual:   {header}"
    )


def test_output_data_rows_match_expected():
    with open(OUTPUT_FILE, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    data_rows = lines[1:]
    expected_data_rows = EXPECTED_LINES[1:]

    assert len(data_rows) == len(expected_data_rows), (
        f"Expected {len(expected_data_rows)} data rows, got {len(data_rows)}."
    )

    for i, (actual, expected) in enumerate(zip(data_rows, expected_data_rows)):
        assert actual == expected, (
            f"Data row {i+1} mismatch:\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}\n"
            "Values must be preserved exactly (no rounding or reformatting)."
        )


def test_output_no_trailing_spaces():
    with open(OUTPUT_FILE, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    for i, line in enumerate(lines):
        assert line == line.rstrip(), (
            f"Line {i+1} has trailing whitespace in {OUTPUT_FILE}:\n"
            f"  Line: {line!r}"
        )


def test_output_no_extra_blank_lines():
    with open(OUTPUT_FILE, "r") as f:
        content = f.read()

    lines = content.rstrip("\n").splitlines()
    for i, line in enumerate(lines):
        assert line.strip() != "", (
            f"Blank line found at line {i+1} in {OUTPUT_FILE}. No extra blank lines allowed."
        )


def test_input_file_unchanged():
    """Verify the original input file was not modified."""
    expected_input = (
        "region,service,account_id,cost_usd,usage_hours,team\n"
        "us-east-1,EC2,123456789012,412.50,1200,platform\n"
        "us-west-2,S3,123456789012,18.75,0,platform\n"
        "eu-west-1,RDS,987654321098,930.00,720,data\n"
        "ap-southeast-1,Lambda,555000111222,7.30,45000,backend\n"
        "us-east-1,CloudFront,987654321098,53.20,0,frontend\n"
        "eu-central-1,EC2,555000111222,601.80,1800,data\n"
        "us-west-2,DynamoDB,123456789012,144.00,0,backend\n"
        "ap-northeast-1,S3,987654321098,22.10,0,frontend"
    )
    with open(INPUT_FILE, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").splitlines()
    expected_lines = expected_input.splitlines()

    assert actual_lines == expected_lines, (
        f"The input file {INPUT_FILE} was modified! It should remain unchanged.\n"
        f"Expected content:\n{expected_input}\n\nActual content:\n{content}"
    )


def test_output_team_column_is_first():
    with open(OUTPUT_FILE, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    # Check header
    assert lines[0].split(",")[0] == "team", (
        f"First column in header should be 'team', got {lines[0].split(',')[0]!r}"
    )

    # Check data rows - team values from original
    expected_teams = ["platform", "platform", "data", "backend", "frontend", "data", "backend", "frontend"]
    for i, (line, expected_team) in enumerate(zip(lines[1:], expected_teams), start=2):
        actual_team = line.split(",")[0]
        assert actual_team == expected_team, (
            f"Line {i}: expected team {expected_team!r} as first column, got {actual_team!r}"
        )


def test_output_account_id_column_is_second():
    with open(OUTPUT_FILE, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    assert lines[0].split(",")[1] == "account_id", (
        f"Second column in header should be 'account_id', got {lines[0].split(',')[1]!r}"
    )

    expected_accounts = [
        "123456789012", "123456789012", "987654321098",
        "555000111222", "987654321098", "555000111222",
        "123456789012", "987654321098"
    ]
    for i, (line, expected_account) in enumerate(zip(lines[1:], expected_accounts), start=2):
        actual_account = line.split(",")[1]
        assert actual_account == expected_account, (
            f"Line {i}: expected account_id {expected_account!r} as second column, got {actual_account!r}"
        )