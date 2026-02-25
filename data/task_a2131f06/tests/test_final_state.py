# test_final_state.py

import os
import json
import pytest

PROFILE_DATA_DIR = "/home/user/profile_data"
CSV_PATH = os.path.join(PROFILE_DATA_DIR, "app_memory.csv")
JSON_PATH = os.path.join(PROFILE_DATA_DIR, "max_memory_per_app.json")

EXPECTED_JSON = {
    "renderer": 195,
    "indexer": 135
}

@pytest.mark.final_state
def test_max_memory_per_app_json_exists():
    assert os.path.isfile(JSON_PATH), (
        f"Expected output JSON file '{JSON_PATH}' does not exist.\n"
        "You must create this file at the specified absolute path."
    )

@pytest.mark.final_state
def test_max_memory_per_app_json_content_exact():
    assert os.path.isfile(JSON_PATH), (
        f"Expected output JSON file '{JSON_PATH}' does not exist, so its contents cannot be checked."
    )
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            pytest.fail(
                f"File '{JSON_PATH}' is not valid JSON: {e}\n"
                "Ensure the file contains well-formatted JSON."
            )
    # Check that the JSON is a dict with exactly the expected keys and values
    assert isinstance(data, dict), (
        f"File '{JSON_PATH}' must contain a JSON object (dictionary), "
        f"but got type {type(data).__name__}."
    )
    # Check for extra or missing keys
    expected_keys = set(EXPECTED_JSON.keys())
    actual_keys = set(data.keys())
    missing = expected_keys - actual_keys
    extra = actual_keys - expected_keys
    assert not missing, (
        f"File '{JSON_PATH}' is missing expected key(s): {', '.join(sorted(missing))}."
    )
    assert not extra, (
        f"File '{JSON_PATH}' contains unexpected extra key(s): {', '.join(sorted(extra))}."
    )
    # Check each value is the correct integer
    for app, expected_max in EXPECTED_JSON.items():
        actual_val = data[app]
        assert isinstance(actual_val, int), (
            f"Value for key '{app}' in '{JSON_PATH}' must be an integer, "
            f"but got {type(actual_val).__name__}."
        )
        assert actual_val == expected_max, (
            f"Incorrect value for key '{app}' in '{JSON_PATH}': "
            f"expected {expected_max}, got {actual_val}."
        )

@pytest.mark.final_state
def test_no_extra_files_created():
    # Only app_memory.csv and max_memory_per_app.json should be present
    expected_files = {"app_memory.csv", "max_memory_per_app.json"}
    try:
        actual_files = set(os.listdir(PROFILE_DATA_DIR))
    except FileNotFoundError:
        pytest.fail(
            f"Required directory '{PROFILE_DATA_DIR}' does not exist. "
            "It must exist after the task is completed."
        )
    extra_files = actual_files - expected_files
    missing_files = expected_files - actual_files
    assert not missing_files, (
        f"Missing expected file(s) in '{PROFILE_DATA_DIR}': {', '.join(sorted(missing_files))}."
    )
    assert not extra_files, (
        f"Unexpected extra file(s) found in '{PROFILE_DATA_DIR}': {', '.join(sorted(extra_files))}.\n"
        "Only 'app_memory.csv' and 'max_memory_per_app.json' should be present."
    )