# test_final_state.py

import os
import pytest
import json

LEGACY_DIR = "/home/user/legacy_services"
CSV_PATH = os.path.join(LEGACY_DIR, "services.csv")
JSONL_PATH = os.path.join(LEGACY_DIR, "active_services.jsonl")
LOG_PATH = os.path.join(LEGACY_DIR, "transform.log")

EXPECTED_JSONL_LINES = [
    '{"id": "1", "name": "AuthService", "endpoint": "tcp://10.10.2.15:8080", "admin": "alice"}',
    '{"id": "3", "name": "WebFront", "endpoint": "tcp://10.10.2.45:80", "admin": "carol"}',
    '{"id": "5", "name": "Billing", "endpoint": "tcp://10.10.2.75:8443", "admin": "erin"}',
]

EXPECTED_LOG_LINES = [
    "Total services found: 5",
    "Total active services exported: 3",
]

@pytest.mark.describe("Final OS/filesystem state after migration task")
def test_active_services_jsonl_exists_and_contents():
    assert os.path.isfile(JSONL_PATH), (
        f"Required output file {JSONL_PATH} does not exist.\n"
        "You must create this file with the correct JSON Lines output."
    )
    with open(JSONL_PATH, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]

    assert lines == EXPECTED_JSONL_LINES, (
        f"{JSONL_PATH} contents are not correct.\n"
        "Expected lines:\n"
        + "\n".join(EXPECTED_JSONL_LINES)
        + "\nActual lines:\n"
        + "\n".join(lines)
        + "\n"
        "Ensure every line is a valid JSON object, matches the required transformation, and is in the correct order."
    )

    # Additionally, check that each line is valid JSON and has exactly the expected fields/values
    for idx, (actual_line, expected_line) in enumerate(zip(lines, EXPECTED_JSONL_LINES)):
        try:
            actual_obj = json.loads(actual_line)
        except Exception as e:
            pytest.fail(
                f"Line {idx+1} in {JSONL_PATH} is not valid JSON: {actual_line}\nError: {e}"
            )
        expected_obj = json.loads(expected_line)
        assert actual_obj == expected_obj, (
            f"Line {idx+1} in {JSONL_PATH} does not match expected object.\n"
            f"Expected: {expected_obj}\n"
            f"Actual:   {actual_obj}\n"
            "Check your transformation logic."
        )

def test_transform_log_exists_and_contents():
    assert os.path.isfile(LOG_PATH), (
        f"Required log file {LOG_PATH} does not exist.\n"
        "You must create this summary log file after transformation."
    )
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        log_lines = [line.rstrip('\n') for line in f]

    assert log_lines == EXPECTED_LOG_LINES, (
        f"{LOG_PATH} contents are not correct.\n"
        "Expected:\n"
        + "\n".join(EXPECTED_LOG_LINES)
        + "\nActual:\n"
        + "\n".join(log_lines)
        + "\n"
        "Ensure you count all services (including inactive/maintenance) for line 1, "
        "and only exported active services for line 2."
    )

def test_no_extra_files_created():
    """Ensure no unexpected files were created in the legacy_services directory."""
    expected_files = {"services.csv", "active_services.jsonl", "transform.log"}
    actual_files = set(os.listdir(LEGACY_DIR))
    extra_files = actual_files - expected_files
    assert not extra_files, (
        f"Unexpected files found in {LEGACY_DIR}: {extra_files}\n"
        "Only the input CSV, active_services.jsonl, and transform.log should be present."
    )