# test_final_state.py

import os
import pytest
import re

RESOURCE_SNAPSHOT_PATH = "/home/user/resource_snapshot.log"
EXPECTED_KEYS = [
    "Memory_Total_MB:",
    "Memory_Used_MB:",
    "Memory_Free_MB:",
    "CPU_Count:",
    "Load_Average_1min:",
    "Load_Average_5min:",
    "Load_Average_15min:",
]

def parse_line(line):
    """
    Parse a line of the format 'Key: value' and return (key, value) tuple.
    """
    if ':' not in line:
        return None, None
    key, value = line.split(':', 1)
    return key.strip() + ':', value.strip()

def test_resource_snapshot_log_exists():
    """
    The file /home/user/resource_snapshot.log must exist after the task is performed.
    """
    assert os.path.exists(RESOURCE_SNAPSHOT_PATH), (
        f"The file {RESOURCE_SNAPSHOT_PATH} does not exist. "
        f"Please create it with the required resource snapshot information."
    )

def test_resource_snapshot_log_format_and_content():
    """
    The file must contain exactly 7 lines, each starting with the expected key,
    and each value must be formatted as specified.
    """
    assert os.path.exists(RESOURCE_SNAPSHOT_PATH), (
        f"The file {RESOURCE_SNAPSHOT_PATH} does not exist."
    )
    with open(RESOURCE_SNAPSHOT_PATH, "r") as f:
        lines = f.read().splitlines()

    # Check for exactly 7 lines
    assert len(lines) == 7, (
        f"{RESOURCE_SNAPSHOT_PATH} must contain exactly 7 lines, but contains {len(lines)}."
    )

    # Check that all expected keys are present and in the correct order
    for i, expected_key in enumerate(EXPECTED_KEYS):
        line = lines[i]
        assert line.startswith(expected_key), (
            f"Line {i+1} of {RESOURCE_SNAPSHOT_PATH} must start with '{expected_key}' "
            f"but found: '{line}'"
        )

    # Check for no trailing whitespace on any line
    for i, line in enumerate(lines):
        assert line == line.rstrip(), (
            f"Line {i+1} of {RESOURCE_SNAPSHOT_PATH} has trailing whitespace: '{line}'"
        )

    # Validate value formats
    # Memory values: integer (MB)
    for i in range(3):
        key, value = parse_line(lines[i])
        assert value.isdigit(), (
            f"Line {i+1} ('{key}') value must be an integer (MB), got: '{value}'"
        )

    # CPU_Count: integer
    key, value = parse_line(lines[3])
    assert value.isdigit(), (
        f"Line 4 ('{key}') value must be an integer, got: '{value}'"
    )

    # Load averages: float with exactly two digits after the decimal point
    loadavg_pattern = re.compile(r"^\d+\.\d{2}$")
    for i in range(4, 7):
        key, value = parse_line(lines[i])
        assert loadavg_pattern.match(value), (
            f"Line {i+1} ('{key}') value must be a floating point number "
            f"with exactly two digits after the decimal point (e.g., 0.18), got: '{value}'"
        )