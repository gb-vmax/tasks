# test_final_state.py

import os
import pytest

HOME = "/home/user"
INPUT_DIR = os.path.join(HOME, "services", "input")
OUTPUT_DIR = os.path.join(HOME, "services", "output")
CSV_PATH = os.path.join(INPUT_DIR, "services.csv")
OUTPUT_JSON = os.path.join(OUTPUT_DIR, "services.json")

EXPECTED_JSON = (
    '[\n'
    '    {\n'
    '        "service_name": "auth-service",\n'
    '        "image": "registry.example.com/auth:1.0",\n'
    '        "exposed_port": 5000\n'
    '    },\n'
    '    {\n'
    '        "service_name": "user-service",\n'
    '        "image": "registry.example.com/user:1.2",\n'
    '        "exposed_port": 5001\n'
    '    }\n'
    ']'
)

@pytest.mark.describe("Validate final OS/filesystem state after student action")
class TestFinalState:

    def test_services_json_exists(self):
        assert os.path.isfile(OUTPUT_JSON), (
            f"The output JSON file '{OUTPUT_JSON}' does not exist. "
            f"Ensure you have created it at the exact required path."
        )

    def test_services_json_content_exact(self):
        assert os.path.isfile(OUTPUT_JSON), (
            f"The output JSON file '{OUTPUT_JSON}' does not exist."
        )
        with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
            content = f.read()
        # Normalize line endings for robust comparison
        norm_content = content.replace('\r\n', '\n').replace('\r', '\n')
        norm_expected = EXPECTED_JSON.replace('\r\n', '\n').replace('\r', '\n')
        assert norm_content == norm_expected, (
            f"The output JSON file '{OUTPUT_JSON}' does not have the exact expected content.\n\n"
            f"Expected content:\n{norm_expected}\n\n"
            f"Actual content:\n{norm_content}\n\n"
            "Differences in indentation, whitespace, or value types (e.g., 'exposed_port' not as integer) will cause this test to fail. "
            "Ensure formatting matches the specification exactly, including 4-space indentation, no trailing commas, and integer values for 'exposed_port'."
        )

    def test_services_json_no_trailing_whitespace(self):
        # This test ensures there are no trailing spaces/tabs at the end of any line,
        # and no blank lines at the end of the file.
        with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if line.rstrip('\r\n') != line.rstrip():
                pytest.fail(
                    f"Line {i+1} in '{OUTPUT_JSON}' has trailing whitespace: {repr(line)}\n"
                    "Remove all trailing spaces and tabs from all lines."
                )
        # Ensure the file does not end with extra blank lines
        if len(lines) > 0 and lines[-1].strip() == '':
            pytest.fail(
                f"The output JSON file '{OUTPUT_JSON}' ends with a blank line. Remove any trailing blank lines."
            )

    def test_services_json_only_in_output_dir(self):
        # Ensure the JSON file only exists at the required location, not in the input dir
        input_json = os.path.join(INPUT_DIR, "services.json")
        assert not os.path.exists(input_json), (
            f"The file '{input_json}' should NOT exist. "
            "Only write the result to /home/user/services/output/services.json."
        )