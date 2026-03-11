# test_final_state.py

import os
import json
import pytest

SERVICES_JSON_PATH = "/home/user/data/services.json"
SERVICES_REPORT_PATH = "/home/user/data/services_report.csv"

EXPECTED_CSV_CONTENT = (
    "id,name,status,response_time_ms\n"
    "1,api-gateway,healthy,45\n"
    "2,auth-service,degraded,320\n"
    "3,billing-worker,healthy,88\n"
    "4,notification-service,down,9999\n"
    "5,search-indexer,healthy,112"
)

EXPECTED_LINES = [
    "id,name,status,response_time_ms",
    "1,api-gateway,healthy,45",
    "2,auth-service,degraded,320",
    "3,billing-worker,healthy,88",
    "4,notification-service,down,9999",
    "5,search-indexer,healthy,112",
]


def test_output_file_exists():
    assert os.path.isfile(SERVICES_REPORT_PATH), (
        f"Output file '{SERVICES_REPORT_PATH}' does not exist. "
        "The task requires writing the CSV report to this path."
    )


def test_output_file_is_readable():
    assert os.access(SERVICES_REPORT_PATH, os.R_OK), (
        f"Output file '{SERVICES_REPORT_PATH}' exists but is not readable."
    )


def test_source_json_still_intact():
    """Ensure the source JSON file was not modified."""
    assert os.path.isfile(SERVICES_JSON_PATH), (
        f"Source file '{SERVICES_JSON_PATH}' is missing after the task. "
        "It should remain untouched."
    )
    with open(SERVICES_JSON_PATH, "r") as f:
        data = json.load(f)
    assert len(data) == 5, (
        f"Source JSON '{SERVICES_JSON_PATH}' should still have 5 entries, "
        f"but found {len(data)}."
    )


def test_csv_exact_content():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    assert content == EXPECTED_CSV_CONTENT, (
        f"Content of '{SERVICES_REPORT_PATH}' does not match expected.\n"
        f"Expected (repr): {repr(EXPECTED_CSV_CONTENT)}\n"
        f"Got      (repr): {repr(content)}"
    )


def test_csv_no_trailing_newline():
    with open(SERVICES_REPORT_PATH, "rb") as f:
        raw = f.read()
    assert not raw.endswith(b"\n"), (
        f"File '{SERVICES_REPORT_PATH}' ends with a newline character, "
        "but the task requires no trailing newline after the last data row."
    )


def test_csv_line_count():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    assert len(lines) == 6, (
        f"Expected exactly 6 lines (1 header + 5 data rows) in '{SERVICES_REPORT_PATH}', "
        f"but found {len(lines)} lines. Lines: {lines}"
    )


def test_csv_header_row():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    header = lines[0]
    assert header == "id,name,status,response_time_ms", (
        f"CSV header row is incorrect.\n"
        f"Expected: 'id,name,status,response_time_ms'\n"
        f"Got:      '{header}'"
    )


def test_csv_data_rows_count():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    data_rows = lines[1:]
    assert len(data_rows) == 5, (
        f"Expected 5 data rows in '{SERVICES_REPORT_PATH}', "
        f"but found {len(data_rows)}. Rows: {data_rows}"
    )


def test_csv_each_row_exact():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    for i, (actual_line, expected_line) in enumerate(zip(lines, EXPECTED_LINES)):
        assert actual_line == expected_line, (
            f"Line {i} of '{SERVICES_REPORT_PATH}' is incorrect.\n"
            f"Expected: '{expected_line}'\n"
            f"Got:      '{actual_line}'"
        )


def test_csv_no_extra_spaces():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    for i, line in enumerate(lines):
        fields = line.split(",")
        for j, field in enumerate(fields):
            assert field == field.strip(), (
                f"Line {i}, field {j} in '{SERVICES_REPORT_PATH}' has extra whitespace.\n"
                f"Field value (repr): {repr(field)}\n"
                f"Full line: '{line}'"
            )


def test_csv_row1_api_gateway():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    assert lines[1] == "1,api-gateway,healthy,45", (
        f"Data row 1 (api-gateway) is incorrect.\n"
        f"Expected: '1,api-gateway,healthy,45'\n"
        f"Got:      '{lines[1]}'"
    )


def test_csv_row2_auth_service():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    assert lines[2] == "2,auth-service,degraded,320", (
        f"Data row 2 (auth-service) is incorrect.\n"
        f"Expected: '2,auth-service,degraded,320'\n"
        f"Got:      '{lines[2]}'"
    )


def test_csv_row3_billing_worker():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    assert lines[3] == "3,billing-worker,healthy,88", (
        f"Data row 3 (billing-worker) is incorrect.\n"
        f"Expected: '3,billing-worker,healthy,88'\n"
        f"Got:      '{lines[3]}'"
    )


def test_csv_row4_notification_service():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    assert lines[4] == "4,notification-service,down,9999", (
        f"Data row 4 (notification-service) is incorrect.\n"
        f"Expected: '4,notification-service,down,9999'\n"
        f"Got:      '{lines[4]}'"
    )


def test_csv_row5_search_indexer():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    assert lines[5] == "5,search-indexer,healthy,112", (
        f"Data row 5 (search-indexer) is incorrect.\n"
        f"Expected: '5,search-indexer,healthy,112'\n"
        f"Got:      '{lines[5]}'"
    )


def test_csv_excludes_region_field():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    assert "us-east-1" not in content, (
        f"CSV file '{SERVICES_REPORT_PATH}' contains 'us-east-1' (region field), "
        "but only id, name, status, and response_time_ms should be included."
    )
    assert "us-west-2" not in content, (
        f"CSV file '{SERVICES_REPORT_PATH}' contains 'us-west-2' (region field), "
        "but only id, name, status, and response_time_ms should be included."
    )
    assert "eu-central-1" not in content, (
        f"CSV file '{SERVICES_REPORT_PATH}' contains 'eu-central-1' (region field), "
        "but only id, name, status, and response_time_ms should be included."
    )
    assert "ap-southeast-1" not in content, (
        f"CSV file '{SERVICES_REPORT_PATH}' contains 'ap-southeast-1' (region field), "
        "but only id, name, status, and response_time_ms should be included."
    )


def test_csv_excludes_owner_email_field():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    assert "ops@example.com" not in content, (
        f"CSV file '{SERVICES_REPORT_PATH}' contains 'ops@example.com' (owner_email field), "
        "but only id, name, status, and response_time_ms should be included."
    )
    assert "security@example.com" not in content, (
        f"CSV file '{SERVICES_REPORT_PATH}' contains 'security@example.com' (owner_email field), "
        "but only id, name, status, and response_time_ms should be included."
    )
    assert "@example.com" not in content, (
        f"CSV file '{SERVICES_REPORT_PATH}' contains email addresses (owner_email field), "
        "but only id, name, status, and response_time_ms should be included."
    )


def test_csv_correct_field_order_in_header():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    header = content.split("\n")[0]
    fields = header.split(",")
    assert fields == ["id", "name", "status", "response_time_ms"], (
        f"CSV header fields are in wrong order or incorrect.\n"
        f"Expected: ['id', 'name', 'status', 'response_time_ms']\n"
        f"Got:      {fields}"
    )


def test_csv_each_data_row_has_four_fields():
    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    data_rows = lines[1:]
    for i, row in enumerate(data_rows, start=2):
        fields = row.split(",")
        assert len(fields) == 4, (
            f"Data row {i} in '{SERVICES_REPORT_PATH}' has {len(fields)} fields, "
            f"expected 4.\nRow content: '{row}'"
        )


def test_csv_service_order_matches_json():
    """Verify services appear in the same order as in the JSON file."""
    with open(SERVICES_JSON_PATH, "r") as f:
        json_data = json.load(f)

    with open(SERVICES_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    data_rows = lines[1:]

    for i, (service, row) in enumerate(zip(json_data, data_rows)):
        expected_id = str(service["id"])
        actual_id = row.split(",")[0]
        assert actual_id == expected_id, (
            f"Service at position {i+1} in CSV has id '{actual_id}', "
            f"but expected '{expected_id}' based on JSON order.\n"
            f"CSV row: '{row}'"
        )