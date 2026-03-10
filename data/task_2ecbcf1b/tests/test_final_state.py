# test_final_state.py

import os
import json
import pytest

INVENTORY_PATH = "/home/user/servers/inventory.json"
REPORT_PATH = "/home/user/servers/report.csv"
SERVERS_DIR = "/home/user/servers"

EXPECTED_CSV_CONTENT = (
    "hostname,ip_address,cpu_cores,ram_gb,status\n"
    "cache01,10.0.3.20,4,32,active\n"
    "db01,10.0.2.10,16,128,active\n"
    "storage01,10.0.1.50,8,64,active\n"
    "web01,10.0.0.1,4,16,active\n"
    "web02,10.0.0.2,4,16,inactive\n"
    "web03,10.0.0.3,2,8,maintenance\n"
)

EXPECTED_LINES = [
    "hostname,ip_address,cpu_cores,ram_gb,status",
    "cache01,10.0.3.20,4,32,active",
    "db01,10.0.2.10,16,128,active",
    "storage01,10.0.1.50,8,64,active",
    "web01,10.0.0.1,4,16,active",
    "web02,10.0.0.2,4,16,inactive",
    "web03,10.0.0.3,2,8,maintenance",
]


def test_servers_directory_exists():
    assert os.path.isdir(SERVERS_DIR), (
        f"Directory '{SERVERS_DIR}' does not exist. "
        "The servers directory must be present."
    )


def test_inventory_file_still_exists():
    """Ensure the original inventory.json was not removed or corrupted."""
    assert os.path.isfile(INVENTORY_PATH), (
        f"The original inventory file '{INVENTORY_PATH}' no longer exists. "
        "It should not have been removed."
    )


def test_inventory_file_still_valid_json():
    """Ensure the original inventory.json is still valid JSON."""
    with open(INVENTORY_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            pytest.fail(
                f"File '{INVENTORY_PATH}' is no longer valid JSON: {e}"
            )
    assert isinstance(data, list), (
        f"Expected '{INVENTORY_PATH}' to contain a JSON array, "
        f"but got {type(data).__name__}."
    )


def test_report_csv_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The task requires creating this CSV report file."
    )


def test_report_csv_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file '{REPORT_PATH}' is not readable. "
        "The file must be readable."
    )


def test_report_csv_ends_with_newline():
    with open(REPORT_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"Report file '{REPORT_PATH}' does not end with a newline character. "
        "The file must end with a newline after the last data row."
    )


def test_report_csv_exact_content():
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()
    assert actual_content == EXPECTED_CSV_CONTENT, (
        f"Report file '{REPORT_PATH}' content does not match expected.\n"
        f"Expected:\n{EXPECTED_CSV_CONTENT!r}\n"
        f"Got:\n{actual_content!r}"
    )


def test_report_csv_line_count():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    # Split by newline; trailing newline means last element is empty string
    lines = content.split("\n")
    # Remove the trailing empty string caused by the final newline
    if lines and lines[-1] == "":
        lines = lines[:-1]
    assert len(lines) == 7, (
        f"Report file '{REPORT_PATH}' should have 7 lines "
        f"(1 header + 6 data rows), but found {len(lines)} lines.\n"
        f"Lines found: {lines}"
    )


def test_report_csv_header_row():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    assert len(lines) >= 1, (
        f"Report file '{REPORT_PATH}' is empty or has no lines."
    )
    header = lines[0]
    expected_header = "hostname,ip_address,cpu_cores,ram_gb,status"
    assert header == expected_header, (
        f"First line (header) of '{REPORT_PATH}' is incorrect.\n"
        f"Expected: {expected_header!r}\n"
        f"Got:      {header!r}"
    )


def test_report_csv_header_has_exactly_five_columns():
    with open(REPORT_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")
    columns = first_line.split(",")
    assert len(columns) == 5, (
        f"Header row should have exactly 5 columns, but found {len(columns)}: {columns}"
    )


def test_report_csv_column_order():
    with open(REPORT_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")
    columns = first_line.split(",")
    expected_columns = ["hostname", "ip_address", "cpu_cores", "ram_gb", "status"]
    assert columns == expected_columns, (
        f"Header columns are in wrong order or incorrect.\n"
        f"Expected: {expected_columns}\n"
        f"Got:      {columns}"
    )


def test_report_csv_no_extra_columns():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    excluded_fields = {"os", "datacenter"}
    for i, line in enumerate(lines[1:], start=2):  # skip header
        if not line:
            continue
        parts = line.split(",")
        assert len(parts) == 5, (
            f"Line {i} in '{REPORT_PATH}' has {len(parts)} fields instead of 5: {line!r}"
        )
        # Check that excluded fields don't appear as values (best-effort)
        for field in excluded_fields:
            # os and datacenter values should not appear as standalone columns
            pass  # We rely on exact content match for this


def test_report_csv_sorted_by_hostname():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    # Skip header
    data_lines = [l for l in lines[1:] if l]
    hostnames = [line.split(",")[0] for line in data_lines]
    assert hostnames == sorted(hostnames), (
        f"Data rows in '{REPORT_PATH}' are not sorted alphabetically by hostname.\n"
        f"Current order: {hostnames}\n"
        f"Expected order: {sorted(hostnames)}"
    )


def test_report_csv_no_trailing_spaces():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} in '{REPORT_PATH}' has trailing whitespace: {line!r}"
        )


def test_report_csv_no_quoted_fields():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert '"' not in content, (
        f"Report file '{REPORT_PATH}' contains quoted fields (double-quote characters). "
        "All fields must be plain comma-separated values without quotes."
    )


def test_report_csv_no_blank_lines():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    # The last element after split will be "" due to trailing newline — that's OK
    # But any other blank line is not allowed
    for i, line in enumerate(lines[:-1], start=1):  # exclude last empty string
        assert line != "", (
            f"Line {i} in '{REPORT_PATH}' is blank. No blank lines are allowed."
        )


def test_report_csv_each_data_row():
    """Validate each expected data row is present and correct."""
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    # Skip header
    data_lines = lines[1:]
    assert len(data_lines) == 6, (
        f"Expected 6 data rows in '{REPORT_PATH}', but found {len(data_lines)}."
    )
    expected_data_lines = EXPECTED_LINES[1:]  # skip header
    for i, (expected, actual) in enumerate(zip(expected_data_lines, data_lines), start=2):
        assert actual == expected, (
            f"Line {i} in '{REPORT_PATH}' does not match expected.\n"
            f"Expected: {expected!r}\n"
            f"Got:      {actual!r}"
        )


def test_report_csv_cache01_row():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    data_lines = lines[1:]
    assert "cache01,10.0.3.20,4,32,active" in data_lines, (
        f"Expected row 'cache01,10.0.3.20,4,32,active' not found in '{REPORT_PATH}'.\n"
        f"Data rows: {data_lines}"
    )


def test_report_csv_db01_row():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    data_lines = lines[1:]
    assert "db01,10.0.2.10,16,128,active" in data_lines, (
        f"Expected row 'db01,10.0.2.10,16,128,active' not found in '{REPORT_PATH}'.\n"
        f"Data rows: {data_lines}"
    )


def test_report_csv_storage01_row():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    data_lines = lines[1:]
    assert "storage01,10.0.1.50,8,64,active" in data_lines, (
        f"Expected row 'storage01,10.0.1.50,8,64,active' not found in '{REPORT_PATH}'.\n"
        f"Data rows: {data_lines}"
    )


def test_report_csv_web01_row():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    data_lines = lines[1:]
    assert "web01,10.0.0.1,4,16,active" in data_lines, (
        f"Expected row 'web01,10.0.0.1,4,16,active' not found in '{REPORT_PATH}'.\n"
        f"Data rows: {data_lines}"
    )


def test_report_csv_web02_row():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    data_lines = lines[1:]
    assert "web02,10.0.0.2,4,16,inactive" in data_lines, (
        f"Expected row 'web02,10.0.0.2,4,16,inactive' not found in '{REPORT_PATH}'.\n"
        f"Data rows: {data_lines}"
    )


def test_report_csv_web03_row():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    data_lines = lines[1:]
    assert "web03,10.0.0.3,2,8,maintenance" in data_lines, (
        f"Expected row 'web03,10.0.0.3,2,8,maintenance' not found in '{REPORT_PATH}'.\n"
        f"Data rows: {data_lines}"
    )


def test_report_csv_numeric_values_not_quoted_or_altered():
    """cpu_cores and ram_gb should appear as plain integers, not floats or strings."""
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()
    data_lines = lines[1:]
    for line in data_lines:
        parts = line.split(",")
        assert len(parts) == 5, f"Row has wrong number of fields: {line!r}"
        cpu_cores_str = parts[2]
        ram_gb_str = parts[3]
        # Should be integer strings (no decimal point)
        assert "." not in cpu_cores_str, (
            f"cpu_cores value '{cpu_cores_str}' in row {line!r} should be an integer, not a float."
        )
        assert "." not in ram_gb_str, (
            f"ram_gb value '{ram_gb_str}' in row {line!r} should be an integer, not a float."
        )
        # Should be parseable as integers
        try:
            int(cpu_cores_str)
        except ValueError:
            pytest.fail(
                f"cpu_cores value '{cpu_cores_str}' in row {line!r} is not a valid integer."
            )
        try:
            int(ram_gb_str)
        except ValueError:
            pytest.fail(
                f"ram_gb value '{ram_gb_str}' in row {line!r} is not a valid integer."
            )