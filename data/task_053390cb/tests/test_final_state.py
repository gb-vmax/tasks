# test_final_state.py

import os
import pytest
import json

CSV_PATH = '/home/user/data/resource_usage.csv'
JSON_OUTPUT_PATH = '/home/user/data/dept_with_highest_avg_cpu.json'
DATA_DIR = '/home/user/data'

EXPECTED_CSV_CONTENT = (
    "department,server,cpu_usage\n"
    "IT,server01,25.0\n"
    "Marketing,server02,63.28\n"
    "Sales,server03,41.2\n"
    "Marketing,server08,62.21\n"
    "IT,server09,24.8\n"
    "Sales,server04,40.1\n"
    "IT,server06,28.5\n"
    "Marketing,server13,62.75\n"
)

EXPECTED_JSON_LINE = '{"department": "Marketing", "avg_cpu_usage": 62.75}'
EXPECTED_JSON_DICT = {"department": "Marketing", "avg_cpu_usage": 62.75}

@pytest.mark.describe("Final OS/Filesystem State Validation")
class TestFinalState:

    def test_data_directory_still_exists(self):
        assert os.path.isdir(DATA_DIR), (
            f"Required directory '{DATA_DIR}' is missing after task completion. "
            "It must not be deleted or moved."
        )

    def test_resource_usage_csv_untouched(self):
        assert os.path.isfile(CSV_PATH), (
            f"Required file '{CSV_PATH}' is missing after task completion. "
            "It must not be deleted or moved."
        )
        with open(CSV_PATH, 'r', encoding='utf-8') as f:
            actual = f.read()
        normalized_actual = actual.replace('\r\n', '\n').replace('\r', '\n')
        assert normalized_actual == EXPECTED_CSV_CONTENT, (
            f"File '{CSV_PATH}' has been changed. "
            "The input CSV must remain unchanged after the task.\n"
            "Expected:\n"
            f"{EXPECTED_CSV_CONTENT!r}\n"
            "Found:\n"
            f"{normalized_actual!r}"
        )

    def test_output_json_exists(self):
        assert os.path.isfile(JSON_OUTPUT_PATH), (
            f"Expected output file '{JSON_OUTPUT_PATH}' does not exist. "
            "You must create this file after analyzing the CSV."
        )

    def test_output_json_is_single_line_and_exact(self):
        with open(JSON_OUTPUT_PATH, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        assert len(lines) == 1, (
            f"Output JSON file '{JSON_OUTPUT_PATH}' must contain exactly one line. "
            f"Found {len(lines)} lines."
        )
        line = lines[0].rstrip('\n\r')
        assert line == EXPECTED_JSON_LINE, (
            f"Output JSON in '{JSON_OUTPUT_PATH}' does not match the expected result or format.\n"
            f"Expected:\n{EXPECTED_JSON_LINE!r}\n"
            f"Found:\n{line!r}\n"
            "Make sure you:\n"
            "- Use exactly the key names 'department' and 'avg_cpu_usage' (all lowercase)\n"
            "- Round avg_cpu_usage to two decimal places (as a number, not a string)\n"
            "- Do not include extra spaces or newlines\n"
            "- Use standard JSON serialization"
        )
        # Additional check: JSON is valid and keys are as expected
        try:
            parsed = json.loads(line)
        except Exception as e:
            pytest.fail(
                f"Output file '{JSON_OUTPUT_PATH}' does not contain valid JSON. Error: {e}"
            )
        assert isinstance(parsed, dict), (
            f"Output JSON in '{JSON_OUTPUT_PATH}' is not a JSON object."
        )
        assert set(parsed.keys()) == set(EXPECTED_JSON_DICT.keys()), (
            f"Output JSON keys are incorrect.\n"
            f"Expected keys: {sorted(EXPECTED_JSON_DICT.keys())}\n"
            f"Found keys: {sorted(parsed.keys())}"
        )
        assert parsed == EXPECTED_JSON_DICT, (
            f"Output JSON values are incorrect.\n"
            f"Expected: {EXPECTED_JSON_DICT!r}\n"
            f"Found: {parsed!r}"
        )

    def test_no_extra_files_created(self):
        allowed_files = {'resource_usage.csv', 'dept_with_highest_avg_cpu.json'}
        actual_files = set(os.listdir(DATA_DIR))
        extra_files = actual_files - allowed_files
        assert not extra_files, (
            f"Unexpected extra file(s) found in '{DATA_DIR}' after task completion: {sorted(extra_files)}. "
            "Do not create any additional files."
        )
        missing_files = allowed_files - actual_files
        assert not missing_files, (
            f"Missing expected file(s) in '{DATA_DIR}': {sorted(missing_files)}"
        )