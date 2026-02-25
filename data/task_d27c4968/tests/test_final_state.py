# test_final_state.py

"""
Pytest suite to validate the FINAL state of the system after the MLOps experiment artifact summary task.

Validates:
1. /home/user/artifacts.json still conforms to the schema in /home/user/artifacts.schema.json.
2. /home/user/checkpoint_summary.json exists and contains the correct summary (list of checkpoint artifacts,
   with only 'artifact_id' and 'created_at' fields, sorted by 'created_at' ascending, and no extra fields).
"""

import os
import json
import pytest
from datetime import datetime

HOME = "/home/user"
ARTIFACTS_JSON = os.path.join(HOME, "artifacts.json")
ARTIFACTS_SCHEMA_JSON = os.path.join(HOME, "artifacts.schema.json")
CHECKPOINT_SUMMARY_JSON = os.path.join(HOME, "checkpoint_summary.json")

EXPECTED_CHECKPOINT_SUMMARY = [
    {
        "artifact_id": "model_v1_ckpt",
        "created_at": "2023-10-01T12:05:00Z"
    },
    {
        "artifact_id": "model_v2_ckpt",
        "created_at": "2023-12-16T15:01:00Z"
    }
]

# The expected schema as per the task description
EXPECTED_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "required": ["artifact_id", "type", "created_at", "size_kb", "location"],
        "properties": {
            "artifact_id": {"type": "string"},
            "type": {"type": "string", "enum": ["checkpoint", "log", "plot"]},
            "created_at": {"type": "string", "format": "date-time"},
            "size_kb": {"type": "integer"},
            "location": {"type": "string"},
        },
    },
}

def load_json_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        pytest.fail(f"Could not load JSON from {path}: {e}")

def is_iso8601_datetime(s):
    # Accepts a string like "2023-10-01T12:05:00Z"
    try:
        datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
        return True
    except Exception:
        return False

def compare_json(a, b):
    # Compares JSON structures for equality
    if isinstance(a, dict) and isinstance(b, dict):
        return a == b
    if isinstance(a, list) and isinstance(b, list):
        return a == b
    return a == b

def validate_schema_instance(schema, instance, path=""):
    """
    Minimal JSON schema validator for the required subset of draft-07.
    Only validates 'type', 'required', 'properties', 'enum', 'format' for our use-case.
    """
    # Array at top level
    if schema.get("type") == "array":
        if not isinstance(instance, list):
            pytest.fail(f"{path or 'Root'}: Expected array, got {type(instance).__name__}")
        item_schema = schema.get("items", {})
        for idx, item in enumerate(instance):
            validate_schema_instance(item_schema, item, path=f"{path}[{idx}]")
    elif schema.get("type") == "object":
        if not isinstance(instance, dict):
            pytest.fail(f"{path or 'Root'}: Expected object, got {type(instance).__name__}")
        required = schema.get("required", [])
        properties = schema.get("properties", {})
        # All required present
        for key in required:
            if key not in instance:
                pytest.fail(f"{path or 'Root'}: Missing required key '{key}'")
        # All properties correct type etc.
        for key, prop_schema in properties.items():
            if key in instance:
                value = instance[key]
                prop_type = prop_schema.get("type")
                if prop_type == "string":
                    if not isinstance(value, str):
                        pytest.fail(f"{path+'.'+key}: Expected string, got {type(value).__name__}")
                    # Check enum
                    if "enum" in prop_schema:
                        if value not in prop_schema["enum"]:
                            pytest.fail(
                                f"{path+'.'+key}: Value '{value}' not in allowed enum {prop_schema['enum']}"
                            )
                    # Check format
                    if prop_schema.get("format") == "date-time":
                        if not is_iso8601_datetime(value):
                            pytest.fail(
                                f"{path+'.'+key}: Value '{value}' is not a valid ISO 8601 datetime with 'Z' (UTC) suffix"
                            )
                elif prop_type == "integer":
                    if not isinstance(value, int):
                        pytest.fail(f"{path+'.'+key}: Expected integer, got {type(value).__name__}")
                # No other types needed for this schema
    else:
        # For this task, only array/object at top.
        pass

def test_artifacts_schema_file_exists_and_correct():
    assert os.path.isfile(ARTIFACTS_SCHEMA_JSON), (
        f"Missing required file: {ARTIFACTS_SCHEMA_JSON}. "
        "You must NOT delete or move the JSON schema."
    )
    schema = load_json_file(ARTIFACTS_SCHEMA_JSON)
    assert compare_json(schema, EXPECTED_SCHEMA), (
        f"The contents of {ARTIFACTS_SCHEMA_JSON} do not match the required JSON schema. "
        "Do not modify the schema file."
    )

def test_artifacts_json_file_exists_and_valid():
    assert os.path.isfile(ARTIFACTS_JSON), (
        f"Missing required file: {ARTIFACTS_JSON}. "
        "You must NOT delete or move the artifacts metadata JSON."
    )
    schema = load_json_file(ARTIFACTS_SCHEMA_JSON)
    artifacts = load_json_file(ARTIFACTS_JSON)
    # Validate against schema
    try:
        validate_schema_instance(schema, artifacts)
    except Exception as e:
        pytest.fail(f"{ARTIFACTS_JSON} does not conform to its schema: {e}")

def test_checkpoint_summary_json_exists_and_correct():
    assert os.path.isfile(CHECKPOINT_SUMMARY_JSON), (
        f"Expected file {CHECKPOINT_SUMMARY_JSON} does not exist. "
        "You must create this file as the summary output."
    )
    data = load_json_file(CHECKPOINT_SUMMARY_JSON)
    assert isinstance(data, list), (
        f"{CHECKPOINT_SUMMARY_JSON} must be a JSON array at the top level."
    )
    # Check each item is a dict with only the correct keys and correct types
    for idx, item in enumerate(data):
        assert isinstance(item, dict), (
            f"Item {idx} in {CHECKPOINT_SUMMARY_JSON} is not a JSON object."
        )
        keys = set(item.keys())
        expected_keys = {"artifact_id", "created_at"}
        extra = keys - expected_keys
        missing = expected_keys - keys
        assert not extra, (
            f"Item {idx} in {CHECKPOINT_SUMMARY_JSON} has extra fields: {list(extra)}. "
            "Each object must have ONLY 'artifact_id' and 'created_at'."
        )
        assert not missing, (
            f"Item {idx} in {CHECKPOINT_SUMMARY_JSON} is missing required fields: {list(missing)}."
        )
        assert isinstance(item["artifact_id"], str), (
            f"Item {idx} 'artifact_id' should be a string."
        )
        assert isinstance(item["created_at"], str), (
            f"Item {idx} 'created_at' should be a string."
        )
        assert is_iso8601_datetime(item["created_at"]), (
            f"Item {idx} 'created_at' is not a valid ISO 8601 datetime with 'Z' (UTC) suffix: {item['created_at']}."
        )
    # Check sorted by created_at ascending
    created_ats = [item["created_at"] for item in data]
    if created_ats != sorted(created_ats):
        pytest.fail(
            f"The 'created_at' values in {CHECKPOINT_SUMMARY_JSON} are not sorted in ascending order: {created_ats}"
        )
    # Check that content matches exactly the expected output
    if data != EXPECTED_CHECKPOINT_SUMMARY:
        pytest.fail(
            f"{CHECKPOINT_SUMMARY_JSON} does not match the required checkpoint summary.\n"
            f"Expected:\n{json.dumps(EXPECTED_CHECKPOINT_SUMMARY, indent=2)}\n"
            f"Found:\n{json.dumps(data, indent=2)}"
        )