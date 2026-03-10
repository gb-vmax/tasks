# test_final_state.py

import os
import pytest

MANIFEST_PATH = "/home/user/iot/deployment_manifest.txt"
CONFIGS_DIR = "/home/user/iot/configs"

EXPECTED_MANIFEST = """\
=== IoT Deployment Manifest ===
Generated for: edge-cluster-07
Total devices scanned: 6
Eligible for deployment: 2
Ineligible (skipped): 4

--- ELIGIBLE DEVICES ---
[A1]
  Model:              SensorPro-200
  Current Firmware:   1.4
  Network:            mqtt://192.168.1.10:1883
  Sensor Type:        temperature
  Sample Rate:        10 Hz
  Calibration Offset: -0.5
  Battery:            85%
  Sleep Mode:         light

[E5]
  Model:              SensorPro-400
  Current Firmware:   1.7
  Network:            mqtt://192.168.2.20:1883
  Sensor Type:        vibration
  Sample Rate:        50 Hz
  Calibration Offset: -1.2
  Battery:            72%
  Sleep Mode:         light

--- INELIGIBLE DEVICES ---
[B3] SKIP: firmware current (2.1)
[C7] SKIP: disabled
[D2] SKIP: low battery (15%)
[F9] SKIP: firmware current (2.0)

--- SENSOR STATISTICS (eligible devices) ---
Sensor types present: temperature, vibration
Average sample rate: 30.00 Hz
Highest calibration offset: -0.5
Lowest calibration offset: -1.2
"""


def test_manifest_file_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Deployment manifest '{MANIFEST_PATH}' does not exist. "
        "The task requires generating this file."
    )


def test_manifest_file_is_readable():
    assert os.access(MANIFEST_PATH, os.R_OK), (
        f"Deployment manifest '{MANIFEST_PATH}' exists but is not readable."
    )


def test_manifest_ends_with_newline():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        "The manifest file must end with a newline character after the last statistics line. "
        f"Last 20 chars: {repr(content[-20:])}"
    )


def test_manifest_exact_content():
    with open(MANIFEST_PATH, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_MANIFEST, (
        "The manifest content does not match the expected output.\n\n"
        f"EXPECTED:\n{EXPECTED_MANIFEST}\n\n"
        f"ACTUAL:\n{actual}\n\n"
        f"DIFF (expected vs actual):\n"
        + _diff(EXPECTED_MANIFEST, actual)
    )


def _diff(expected, actual):
    """Simple line-by-line diff for error messages."""
    expected_lines = expected.splitlines(keepends=True)
    actual_lines = actual.splitlines(keepends=True)
    lines = []
    max_len = max(len(expected_lines), len(actual_lines))
    for i in range(max_len):
        exp_line = expected_lines[i] if i < len(expected_lines) else "<MISSING>"
        act_line = actual_lines[i] if i < len(actual_lines) else "<MISSING>"
        if exp_line != act_line:
            lines.append(f"Line {i+1}:")
            lines.append(f"  Expected: {repr(exp_line)}")
            lines.append(f"  Actual:   {repr(act_line)}")
    return "\n".join(lines) if lines else "(no line-level differences found)"


def test_manifest_header():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert lines[0] == "=== IoT Deployment Manifest ===", (
        f"First line of manifest is wrong.\n"
        f"Expected: '=== IoT Deployment Manifest ==='\n"
        f"Actual:   '{lines[0]}'"
    )
    assert lines[1] == "Generated for: edge-cluster-07", (
        f"Second line of manifest is wrong.\n"
        f"Expected: 'Generated for: edge-cluster-07'\n"
        f"Actual:   '{lines[1]}'"
    )


def test_manifest_totals():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert lines[2] == "Total devices scanned: 6", (
        f"Total devices scanned line is wrong.\n"
        f"Expected: 'Total devices scanned: 6'\n"
        f"Actual:   '{lines[2]}'"
    )
    assert lines[3] == "Eligible for deployment: 2", (
        f"Eligible for deployment line is wrong.\n"
        f"Expected: 'Eligible for deployment: 2'\n"
        f"Actual:   '{lines[3]}'"
    )
    assert lines[4] == "Ineligible (skipped): 4", (
        f"Ineligible (skipped) line is wrong.\n"
        f"Expected: 'Ineligible (skipped): 4'\n"
        f"Actual:   '{lines[4]}'"
    )


def test_manifest_eligible_section_header():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "--- ELIGIBLE DEVICES ---" in content, (
        "The manifest is missing the '--- ELIGIBLE DEVICES ---' section header."
    )


def test_manifest_ineligible_section_header():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "--- INELIGIBLE DEVICES ---" in content, (
        "The manifest is missing the '--- INELIGIBLE DEVICES ---' section header."
    )


def test_manifest_sensor_statistics_section_header():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "--- SENSOR STATISTICS (eligible devices) ---" in content, (
        "The manifest is missing the '--- SENSOR STATISTICS (eligible devices) ---' section header."
    )


def test_eligible_device_A1_block():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    expected_block = (
        "[A1]\n"
        "  Model:              SensorPro-200\n"
        "  Current Firmware:   1.4\n"
        "  Network:            mqtt://192.168.1.10:1883\n"
        "  Sensor Type:        temperature\n"
        "  Sample Rate:        10 Hz\n"
        "  Calibration Offset: -0.5\n"
        "  Battery:            85%\n"
        "  Sleep Mode:         light"
    )
    assert expected_block in content, (
        f"Device A1 block not found or incorrect in the manifest.\n"
        f"Expected block:\n{expected_block}\n\n"
        f"Actual manifest:\n{content}"
    )


def test_eligible_device_E5_block():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    expected_block = (
        "[E5]\n"
        "  Model:              SensorPro-400\n"
        "  Current Firmware:   1.7\n"
        "  Network:            mqtt://192.168.2.20:1883\n"
        "  Sensor Type:        vibration\n"
        "  Sample Rate:        50 Hz\n"
        "  Calibration Offset: -1.2\n"
        "  Battery:            72%\n"
        "  Sleep Mode:         light"
    )
    assert expected_block in content, (
        f"Device E5 block not found or incorrect in the manifest.\n"
        f"Expected block:\n{expected_block}\n\n"
        f"Actual manifest:\n{content}"
    )


def test_eligible_devices_order():
    """A1 must appear before E5 in the eligible section."""
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    eligible_start = content.find("--- ELIGIBLE DEVICES ---")
    ineligible_start = content.find("--- INELIGIBLE DEVICES ---")
    assert eligible_start != -1, "Missing '--- ELIGIBLE DEVICES ---' section."
    assert ineligible_start != -1, "Missing '--- INELIGIBLE DEVICES ---' section."
    eligible_section = content[eligible_start:ineligible_start]
    pos_a1 = eligible_section.find("[A1]")
    pos_e5 = eligible_section.find("[E5]")
    assert pos_a1 != -1, "Device [A1] not found in eligible section."
    assert pos_e5 != -1, "Device [E5] not found in eligible section."
    assert pos_a1 < pos_e5, (
        "Eligible devices must be listed in ascending alphabetical order. "
        "A1 should appear before E5."
    )


def test_blank_line_between_eligible_devices():
    """There should be exactly one blank line between the A1 and E5 blocks."""
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    # The A1 block ends with "  Sleep Mode:         light" and then a blank line before [E5]
    assert "  Sleep Mode:         light\n\n[E5]" in content, (
        "There should be exactly one blank line between the A1 and E5 device blocks.\n"
        "Expected pattern: '  Sleep Mode:         light\\n\\n[E5]'"
    )


def test_no_trailing_blank_line_after_last_eligible_device():
    """No trailing blank line after the last eligible device block before ineligible section."""
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    # After the last eligible device (E5), there should be a blank line then the ineligible header
    # The E5 block ends with "  Sleep Mode:         light\n\n--- INELIGIBLE"
    assert "  Sleep Mode:         light\n\n--- INELIGIBLE DEVICES ---" in content, (
        "After the last eligible device block (E5), there should be exactly one blank line "
        "before '--- INELIGIBLE DEVICES ---'.\n"
        "Expected pattern: '  Sleep Mode:         light\\n\\n--- INELIGIBLE DEVICES ---'"
    )


def test_ineligible_B3():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "[B3] SKIP: firmware current (2.1)" in content, (
        "Ineligible device B3 line not found or incorrect.\n"
        "Expected: '[B3] SKIP: firmware current (2.1)'"
    )


def test_ineligible_C7():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "[C7] SKIP: disabled" in content, (
        "Ineligible device C7 line not found or incorrect.\n"
        "Expected: '[C7] SKIP: disabled'"
    )


def test_ineligible_D2():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "[D2] SKIP: low battery (15%)" in content, (
        "Ineligible device D2 line not found or incorrect.\n"
        "Expected: '[D2] SKIP: low battery (15%)'"
    )


def test_ineligible_F9():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "[F9] SKIP: firmware current (2.0)" in content, (
        "Ineligible device F9 line not found or incorrect.\n"
        "Expected: '[F9] SKIP: firmware current (2.0)'"
    )


def test_ineligible_devices_order():
    """Ineligible devices must be in ascending alphabetical order: B3, C7, D2, F9."""
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    ineligible_start = content.find("--- INELIGIBLE DEVICES ---")
    stats_start = content.find("--- SENSOR STATISTICS")
    assert ineligible_start != -1, "Missing '--- INELIGIBLE DEVICES ---' section."
    assert stats_start != -1, "Missing '--- SENSOR STATISTICS' section."
    ineligible_section = content[ineligible_start:stats_start]
    pos_b3 = ineligible_section.find("[B3]")
    pos_c7 = ineligible_section.find("[C7]")
    pos_d2 = ineligible_section.find("[D2]")
    pos_f9 = ineligible_section.find("[F9]")
    assert pos_b3 != -1, "[B3] not found in ineligible section."
    assert pos_c7 != -1, "[C7] not found in ineligible section."
    assert pos_d2 != -1, "[D2] not found in ineligible section."
    assert pos_f9 != -1, "[F9] not found in ineligible section."
    assert pos_b3 < pos_c7 < pos_d2 < pos_f9, (
        "Ineligible devices must be listed in ascending alphabetical order: B3, C7, D2, F9.\n"
        f"Found positions: B3={pos_b3}, C7={pos_c7}, D2={pos_d2}, F9={pos_f9}"
    )


def test_sensor_statistics_types():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "Sensor types present: temperature, vibration" in content, (
        "Sensor types line is wrong or missing.\n"
        "Expected: 'Sensor types present: temperature, vibration'"
    )


def test_sensor_statistics_average_sample_rate():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "Average sample rate: 30.00 Hz" in content, (
        "Average sample rate line is wrong or missing.\n"
        "Expected: 'Average sample rate: 30.00 Hz'"
    )


def test_sensor_statistics_highest_calibration():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "Highest calibration offset: -0.5" in content, (
        "Highest calibration offset line is wrong or missing.\n"
        "Expected: 'Highest calibration offset: -0.5'"
    )


def test_sensor_statistics_lowest_calibration():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "Lowest calibration offset: -1.2" in content, (
        "Lowest calibration offset line is wrong or missing.\n"
        "Expected: 'Lowest calibration offset: -1.2'"
    )


def test_sensor_statistics_section_order():
    """Statistics section must come after ineligible section."""
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    ineligible_pos = content.find("--- INELIGIBLE DEVICES ---")
    stats_pos = content.find("--- SENSOR STATISTICS (eligible devices) ---")
    assert ineligible_pos != -1, "Missing '--- INELIGIBLE DEVICES ---' section."
    assert stats_pos != -1, "Missing '--- SENSOR STATISTICS (eligible devices) ---' section."
    assert stats_pos > ineligible_pos, (
        "The sensor statistics section must appear after the ineligible devices section."
    )


def test_no_blank_line_between_ineligible_and_stats():
    """No blank line between the last ineligible line and the stats section header."""
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    # The last ineligible line is [F9] and then a blank line then stats header
    assert "[F9] SKIP: firmware current (2.0)\n\n--- SENSOR STATISTICS (eligible devices) ---" in content, (
        "There should be exactly one blank line between the last ineligible device line "
        "and the '--- SENSOR STATISTICS (eligible devices) ---' header.\n"
        "Expected pattern: '[F9] SKIP: firmware current (2.0)\\n\\n--- SENSOR STATISTICS...'"
    )


def test_manifest_last_line():
    """The last line of the manifest should be the lowest calibration offset line."""
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    # Strip the trailing newline and check the last line
    lines = content.rstrip("\n").splitlines()
    assert lines[-1] == "Lowest calibration offset: -1.2", (
        f"The last line of the manifest should be 'Lowest calibration offset: -1.2'.\n"
        f"Actual last line: '{lines[-1]}'"
    )


def test_configs_directory_unchanged():
    """The original config files should still be present and unmodified."""
    expected_files = {
        "device_A1.ini", "device_B3.ini", "device_C7.ini",
        "device_D2.ini", "device_E5.ini", "device_F9.ini"
    }
    assert os.path.isdir(CONFIGS_DIR), (
        f"Configs directory '{CONFIGS_DIR}' no longer exists."
    )
    existing = set(os.listdir(CONFIGS_DIR))
    missing = expected_files - existing
    assert not missing, (
        f"Config files were removed from '{CONFIGS_DIR}': {sorted(missing)}"
    )