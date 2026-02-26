# test_final_state.py

import os
import pytest

API_TEST_DIR = "/home/user/api_test"
RESPONSE_JSON = os.path.join(API_TEST_DIR, "response.json")
API_TEST_LOG = os.path.join(API_TEST_DIR, "api_test.log")

EXPECTED_RESPONSE_JSON_CONTENT = (
    '{\n'
    '    "status": "success",\n'
    '    "code": 200,\n'
    '    "data": {\n'
    '        "message": "API call successful"\n'
    '    }\n'
    '}\n'
)

def test_api_test_directory_exists():
    assert os.path.isdir(API_TEST_DIR), (
        f"Directory {API_TEST_DIR} does not exist. "
        "It must exist after completing the task."
    )

def test_response_json_exists():
    assert os.path.isfile(RESPONSE_JSON), (
        f"File {RESPONSE_JSON} does not exist. "
        "It must be created in the directory."
    )

def test_response_json_content_exact():
    assert os.path.isfile(RESPONSE_JSON), (
        f"File {RESPONSE_JSON} does not exist, cannot check content."
    )
    with open(RESPONSE_JSON, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_RESPONSE_JSON_CONTENT, (
        f"File {RESPONSE_JSON} content does not match the required JSON exactly.\n"
        f"\n--- Expected ---\n{EXPECTED_RESPONSE_JSON_CONTENT!r}\n"
        f"\n--- Found ---\n{content!r}\n"
        "The content, formatting, spacing, and newlines must match the example exactly."
    )

def test_api_test_log_exists_and_empty():
    assert os.path.isfile(API_TEST_LOG), (
        f"File {API_TEST_LOG} does not exist. "
        "It must be created as an empty file."
    )
    size = os.stat(API_TEST_LOG).st_size
    assert size == 0, (
        f"File {API_TEST_LOG} is not empty (size: {size} bytes). "
        "This file must be empty (zero bytes)."
    )

def test_no_extra_files_in_api_test_dir():
    assert os.path.isdir(API_TEST_DIR), (
        f"Directory {API_TEST_DIR} does not exist, cannot check for extra files."
    )
    expected_files = {"response.json", "api_test.log"}
    actual_files = set(os.listdir(API_TEST_DIR))
    missing = expected_files - actual_files
    extra = actual_files - expected_files
    assert not missing, (
        f"Missing file(s) in {API_TEST_DIR}: {', '.join(sorted(missing))}. "
        "Only 'response.json' and 'api_test.log' must be present."
    )
    assert not extra, (
        f"Unexpected file(s) or directory(ies) found in {API_TEST_DIR}: {', '.join(sorted(extra))}. "
        "Only 'response.json' and 'api_test.log' must be present, no others."
    )