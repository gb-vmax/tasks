# test_final_state.py

import os
import pytest

DEPLOY_SUMMARY_PATH = "/home/user/edge/deploy_summary.conf"
INI_PATH = "/home/user/edge/device_master.ini"
EDGE_DIR = "/home/user/edge"

EXPECTED_LINES = [
    "DEVICE_ID=node-47-alpha",
    "FIRMWARE=2.11.4",
    "MQTT_HOST=mqtt.edgefleet.internal",
    "MQTT_PORT=1883",
    "POLL_INTERVAL=30",
    "TEMP_MAX=85",
    "BATTERY_MIN=15",
    "TOTAL_KEYS=16",
]


def test_edge_directory_exists():
    assert os.path.isdir(EDGE_DIR), (
        f"Directory '{EDGE_DIR}' does not exist. "
        "The /home/user/edge directory must be present."
    )


def test_ini_file_still_exists():
    assert os.path.isfile(INI_PATH), (
        f"The original INI file '{INI_PATH}' no longer exists. "
        "The master INI configuration file must not be removed."
    )


def test_deploy_summary_exists():
    assert os.path.isfile(DEPLOY_SUMMARY_PATH), (
        f"The deployment summary file '{DEPLOY_SUMMARY_PATH}' does not exist. "
        "The student must create this file as part of the task."
    )


def test_deploy_summary_is_readable():
    assert os.access(DEPLOY_SUMMARY_PATH, os.R_OK), (
        f"File '{DEPLOY_SUMMARY_PATH}' is not readable. "
        "Ensure the file has appropriate read permissions."
    )


def test_deploy_summary_exact_line_count():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        content = f.read()

    # Strip trailing newline for counting purposes, then split
    lines = content.rstrip("\n").split("\n")

    assert len(lines) == 8, (
        f"Expected exactly 8 lines in '{DEPLOY_SUMMARY_PATH}', "
        f"but found {len(lines)} lines. "
        f"Actual content:\n{content}"
    )


def test_deploy_summary_no_extra_blank_lines():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        content = f.read()

    lines = content.rstrip("\n").split("\n")

    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"Line {i} in '{DEPLOY_SUMMARY_PATH}' is blank or whitespace-only. "
            "The file must contain exactly 8 non-blank lines with no extra blank lines."
        )


def test_deploy_summary_line_1_device_id():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    assert len(lines) >= 1, (
        f"'{DEPLOY_SUMMARY_PATH}' has fewer than 1 line."
    )
    assert lines[0] == "DEVICE_ID=node-47-alpha", (
        f"Line 1 of '{DEPLOY_SUMMARY_PATH}' is incorrect.\n"
        f"Expected: 'DEVICE_ID=node-47-alpha'\n"
        f"Actual:   '{lines[0]}'"
    )


def test_deploy_summary_line_2_firmware():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    assert len(lines) >= 2, (
        f"'{DEPLOY_SUMMARY_PATH}' has fewer than 2 lines."
    )
    assert lines[1] == "FIRMWARE=2.11.4", (
        f"Line 2 of '{DEPLOY_SUMMARY_PATH}' is incorrect.\n"
        f"Expected: 'FIRMWARE=2.11.4'\n"
        f"Actual:   '{lines[1]}'"
    )


def test_deploy_summary_line_3_mqtt_host():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    assert len(lines) >= 3, (
        f"'{DEPLOY_SUMMARY_PATH}' has fewer than 3 lines."
    )
    assert lines[2] == "MQTT_HOST=mqtt.edgefleet.internal", (
        f"Line 3 of '{DEPLOY_SUMMARY_PATH}' is incorrect.\n"
        f"Expected: 'MQTT_HOST=mqtt.edgefleet.internal'\n"
        f"Actual:   '{lines[2]}'"
    )


def test_deploy_summary_line_4_mqtt_port():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    assert len(lines) >= 4, (
        f"'{DEPLOY_SUMMARY_PATH}' has fewer than 4 lines."
    )
    assert lines[3] == "MQTT_PORT=1883", (
        f"Line 4 of '{DEPLOY_SUMMARY_PATH}' is incorrect.\n"
        f"Expected: 'MQTT_PORT=1883'\n"
        f"Actual:   '{lines[3]}'"
    )


def test_deploy_summary_line_5_poll_interval():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    assert len(lines) >= 5, (
        f"'{DEPLOY_SUMMARY_PATH}' has fewer than 5 lines."
    )
    assert lines[4] == "POLL_INTERVAL=30", (
        f"Line 5 of '{DEPLOY_SUMMARY_PATH}' is incorrect.\n"
        f"Expected: 'POLL_INTERVAL=30'\n"
        f"Actual:   '{lines[4]}'"
    )


def test_deploy_summary_line_6_temp_max():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    assert len(lines) >= 6, (
        f"'{DEPLOY_SUMMARY_PATH}' has fewer than 6 lines."
    )
    assert lines[5] == "TEMP_MAX=85", (
        f"Line 6 of '{DEPLOY_SUMMARY_PATH}' is incorrect.\n"
        f"Expected: 'TEMP_MAX=85'\n"
        f"Actual:   '{lines[5]}'"
    )


def test_deploy_summary_line_7_battery_min():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    assert len(lines) >= 7, (
        f"'{DEPLOY_SUMMARY_PATH}' has fewer than 7 lines."
    )
    assert lines[6] == "BATTERY_MIN=15", (
        f"Line 7 of '{DEPLOY_SUMMARY_PATH}' is incorrect.\n"
        f"Expected: 'BATTERY_MIN=15'\n"
        f"Actual:   '{lines[6]}'"
    )


def test_deploy_summary_line_8_total_keys():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    assert len(lines) >= 8, (
        f"'{DEPLOY_SUMMARY_PATH}' has fewer than 8 lines."
    )
    assert lines[7] == "TOTAL_KEYS=16", (
        f"Line 8 of '{DEPLOY_SUMMARY_PATH}' is incorrect.\n"
        f"Expected: 'TOTAL_KEYS=16'\n"
        f"Actual:   '{lines[7]}'"
    )


def test_deploy_summary_all_lines_match_exactly():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        content = f.read()

    actual_lines = content.rstrip("\n").split("\n")

    assert len(actual_lines) == len(EXPECTED_LINES), (
        f"Expected {len(EXPECTED_LINES)} lines in '{DEPLOY_SUMMARY_PATH}', "
        f"but found {len(actual_lines)}.\n"
        f"Full content:\n{content}"
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, EXPECTED_LINES), start=1):
        assert actual == expected, (
            f"Line {i} of '{DEPLOY_SUMMARY_PATH}' does not match.\n"
            f"Expected: '{expected}'\n"
            f"Actual:   '{actual}'"
        )


def test_deploy_summary_no_spaces_around_equals():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    for i, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        # Check that there are no spaces around the '=' sign
        assert " = " not in line and "= " not in line and " =" not in line, (
            f"Line {i} in '{DEPLOY_SUMMARY_PATH}' has spaces around '='.\n"
            f"The format must be KEY=value with no spaces around '='.\n"
            f"Actual line: '{line}'"
        )


def test_deploy_summary_each_line_has_key_value_format():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    for i, line in enumerate(lines, start=1):
        assert "=" in line, (
            f"Line {i} in '{DEPLOY_SUMMARY_PATH}' does not contain '='.\n"
            f"Each line must follow the KEY=value format.\n"
            f"Actual line: '{line}'"
        )
        parts = line.split("=", 1)
        assert len(parts) == 2, (
            f"Line {i} in '{DEPLOY_SUMMARY_PATH}' cannot be split into KEY=value.\n"
            f"Actual line: '{line}'"
        )
        key, value = parts
        assert key, (
            f"Line {i} in '{DEPLOY_SUMMARY_PATH}' has an empty key.\n"
            f"Actual line: '{line}'"
        )
        assert value, (
            f"Line {i} in '{DEPLOY_SUMMARY_PATH}' has an empty value.\n"
            f"Actual line: '{line}'"
        )


def test_deploy_summary_keys_are_uppercase():
    with open(DEPLOY_SUMMARY_PATH, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    expected_keys = [
        "DEVICE_ID", "FIRMWARE", "MQTT_HOST", "MQTT_PORT",
        "POLL_INTERVAL", "TEMP_MAX", "BATTERY_MIN", "TOTAL_KEYS"
    ]

    for i, (line, expected_key) in enumerate(zip(lines, expected_keys), start=1):
        key = line.split("=", 1)[0]
        assert key == expected_key, (
            f"Line {i} in '{DEPLOY_SUMMARY_PATH}' has key '{key}', "
            f"but expected '{expected_key}'.\n"
            f"Actual line: '{line}'"
        )


def test_ini_file_unchanged():
    """Verify the original INI file has not been modified."""
    expected_content = """; Master configuration for IoT edge sensor nodes
; Generated by provisioning system

[device]
id = node-47-alpha
firmware_version = 2.11.4
location = warehouse-B
manufacturer = SensorTech

[network]
broker_host = mqtt.edgefleet.internal
broker_port = 1883
use_tls = false
keepalive_sec = 60
reconnect_delay = 5

[sensors]
poll_interval_sec = 30
enabled_sensors = temp,humidity,pressure
calibration_offset = -1.2

[thresholds]
temp_max_celsius = 85
temp_min_celsius = -10
humidity_max_pct = 95
battery_min_pct = 15"""

    with open(INI_PATH, "r") as f:
        actual_content = f.read()

    assert actual_content.strip() == expected_content.strip(), (
        f"The original INI file '{INI_PATH}' has been modified.\n"
        f"Expected content:\n{expected_content}\n\n"
        f"Actual content:\n{actual_content}"
    )