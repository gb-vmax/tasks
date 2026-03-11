# test_final_state.py

import os
import pytest

DEPLOY_TARGETS = "/home/user/iot/deploy_targets.csv"
DEVICES_CSV = "/home/user/iot/devices.csv"
IOT_DIR = "/home/user/iot"

EXPECTED_LINES = [
    "10.0.0.11:sensor-001:1.9.4",
    "10.0.0.22:sensor-002:2.0.1",
    "10.0.0.33:sensor-003:2.1.0",
    "10.0.0.44:sensor-004:2.1.0",
    "10.0.0.55:sensor-005:1.8.7",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES)


def test_iot_directory_exists():
    assert os.path.isdir(IOT_DIR), (
        f"Directory '{IOT_DIR}' does not exist. "
        "The IoT working directory must exist."
    )


def test_deploy_targets_exists():
    assert os.path.isfile(DEPLOY_TARGETS), (
        f"Output file '{DEPLOY_TARGETS}' does not exist. "
        "The student must create this file as part of the task."
    )


def test_deploy_targets_is_readable():
    assert os.access(DEPLOY_TARGETS, os.R_OK), (
        f"File '{DEPLOY_TARGETS}' is not readable. "
        "Check file permissions."
    )


def test_deploy_targets_exact_content():
    with open(DEPLOY_TARGETS, "r") as f:
        content = f.read()

    actual = content.strip()
    assert actual == EXPECTED_CONTENT, (
        f"Content of '{DEPLOY_TARGETS}' does not match expected.\n"
        f"Expected:\n{EXPECTED_CONTENT}\n\n"
        f"Got:\n{actual}"
    )


def test_deploy_targets_no_header():
    with open(DEPLOY_TARGETS, "r") as f:
        first_line = f.readline().rstrip("\n")

    # The first line must NOT be a header (i.e., must not contain 'ip_address' or 'device_id')
    assert "ip_address" not in first_line, (
        f"The first line of '{DEPLOY_TARGETS}' appears to be a header line: '{first_line}'. "
        "The output file must contain NO header line."
    )
    assert "device_id" not in first_line, (
        f"The first line of '{DEPLOY_TARGETS}' appears to be a header line: '{first_line}'. "
        "The output file must contain NO header line."
    )


def test_deploy_targets_line_count():
    with open(DEPLOY_TARGETS, "r") as f:
        lines = [line for line in f.read().splitlines() if line.strip()]

    assert len(lines) == 5, (
        f"'{DEPLOY_TARGETS}' should have exactly 5 data lines (no header), "
        f"but found {len(lines)} non-empty lines."
    )


def test_deploy_targets_colon_delimiter():
    with open(DEPLOY_TARGETS, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines, start=1):
        assert ":" in line, (
            f"Line {i} of '{DEPLOY_TARGETS}' does not contain a colon delimiter: '{line}'. "
            "Fields must be separated by colons (':')."
        )
        assert "," not in line, (
            f"Line {i} of '{DEPLOY_TARGETS}' contains a comma, but the delimiter should be ':': '{line}'."
        )
        parts = line.split(":")
        assert len(parts) == 3, (
            f"Line {i} of '{DEPLOY_TARGETS}' should have exactly 3 colon-separated fields, "
            f"but found {len(parts)}: '{line}'."
        )


def test_deploy_targets_column_order():
    """Verify columns are in order: ip_address, device_id, firmware_version."""
    with open(DEPLOY_TARGETS, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    # Expected: ip_address first, device_id second, firmware_version third
    # ip_address matches pattern like 10.0.0.XX
    # device_id matches pattern like sensor-XXX
    # firmware_version matches pattern like X.X.X
    import re
    ip_pattern = re.compile(r"^\d+\.\d+\.\d+\.\d+$")
    device_pattern = re.compile(r"^sensor-\d+$")
    firmware_pattern = re.compile(r"^\d+\.\d+\.\d+$")

    for i, line in enumerate(lines, start=1):
        parts = line.split(":")
        if len(parts) != 3:
            continue  # Already caught by previous test

        col1, col2, col3 = parts

        assert ip_pattern.match(col1), (
            f"Line {i}: First field should be ip_address (e.g., '10.0.0.11'), "
            f"but got '{col1}'. Check column order: ip_address:device_id:firmware_version."
        )
        assert device_pattern.match(col2), (
            f"Line {i}: Second field should be device_id (e.g., 'sensor-001'), "
            f"but got '{col2}'. Check column order: ip_address:device_id:firmware_version."
        )
        assert firmware_pattern.match(col3), (
            f"Line {i}: Third field should be firmware_version (e.g., '1.9.4'), "
            f"but got '{col3}'. Check column order: ip_address:device_id:firmware_version."
        )


def test_deploy_targets_each_row():
    with open(DEPLOY_TARGETS, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    assert len(lines) == len(EXPECTED_LINES), (
        f"Expected {len(EXPECTED_LINES)} lines, got {len(lines)}."
    )

    for i, (actual, expected) in enumerate(zip(lines, EXPECTED_LINES), start=1):
        assert actual == expected, (
            f"Row {i} of '{DEPLOY_TARGETS}' is incorrect.\n"
            f"Expected: {expected}\n"
            f"Got:      {actual}"
        )


def test_deploy_targets_no_trailing_blank_line():
    with open(DEPLOY_TARGETS, "r") as f:
        content = f.read()

    # The file should end with exactly one newline or no newline after the last data line
    # It must NOT have extra blank lines at the end
    lines = content.splitlines()
    non_empty_lines = [l for l in lines if l.strip()]

    assert len(non_empty_lines) == 5, (
        f"'{DEPLOY_TARGETS}' should have exactly 5 non-empty lines, "
        f"but found {len(non_empty_lines)}. "
        "Check for extra blank lines or missing data rows."
    )


def test_source_file_unchanged():
    """Ensure the original devices.csv was not modified."""
    EXPECTED_SOURCE = (
        "device_id,location,firmware_version,ip_address,status,last_seen\n"
        "sensor-001,factory-floor,1.9.4,10.0.0.11,active,2024-10-30\n"
        "sensor-002,loading-dock,2.0.1,10.0.0.22,inactive,2024-10-28\n"
        "sensor-003,rooftop,2.1.0,10.0.0.33,active,2024-11-01\n"
        "sensor-004,warehouse-b,2.1.0,10.0.0.44,active,2024-11-01\n"
        "sensor-005,parking-lot,1.8.7,10.0.0.55,maintenance,2024-10-15"
    )

    assert os.path.isfile(DEVICES_CSV), (
        f"Source file '{DEVICES_CSV}' is missing. It must not be deleted."
    )

    with open(DEVICES_CSV, "r") as f:
        content = f.read().strip()

    assert content == EXPECTED_SOURCE.strip(), (
        f"Source file '{DEVICES_CSV}' was modified. Its content should remain unchanged.\n"
        f"Expected:\n{EXPECTED_SOURCE}\n\n"
        f"Got:\n{content}"
    )