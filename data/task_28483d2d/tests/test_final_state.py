# test_final_state.py

import os
import pytest

ACCESS_REPORT_PATH = "/home/user/project/access_report.csv"
NON_READ_PERMISSIONS_PATH = "/home/user/project/non_read_permissions.json"
PROJECT_DIR = "/home/user/project"

EXPECTED_JSON_CONTENT = (
    '[\n'
    '{"username":"alice","filename":"secret.txt","permission":"write"},\n'
    '{"username":"bob","filename":"log.txt","permission":"execute"}\n'
    ']'
)

EXPECTED_CSV_CONTENT = (
    "username,filename,permission\n"
    "alice,secret.txt,write\n"
    "bob,log.txt,execute\n"
    "carol,data.txt,read\n"
    "dave,audit.log,read\n"
)

@pytest.mark.describe("Final state: Output JSON file exists with correct contents")
def test_project_directory_still_exists():
    assert os.path.isdir(PROJECT_DIR), (
        f"Required directory '{PROJECT_DIR}' does not exist after the task. "
        "The project directory must not be removed or renamed."
    )

def test_access_report_csv_still_exists_and_unchanged():
    assert os.path.isfile(ACCESS_REPORT_PATH), (
        f"Input file '{ACCESS_REPORT_PATH}' is missing after the task. "
        "The input CSV file must not be removed or renamed."
    )
    with open(ACCESS_REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_CSV_CONTENT, (
        f"The contents of '{ACCESS_REPORT_PATH}' were changed.\n"
        "Expected:\n"
        f"{EXPECTED_CSV_CONTENT!r}\n"
        "Found:\n"
        f"{content!r}\n"
        "The input CSV file must remain unchanged after the task."
    )

def test_non_read_permissions_json_exists():
    assert os.path.isfile(NON_READ_PERMISSIONS_PATH), (
        f"The output file '{NON_READ_PERMISSIONS_PATH}' does not exist. "
        "You must create this file as specified in the instructions."
    )

def test_non_read_permissions_json_content_exact():
    with open(NON_READ_PERMISSIONS_PATH, "r", encoding="utf-8") as f:
        actual_content = f.read()
    if actual_content != EXPECTED_JSON_CONTENT:
        # Try to give a helpful diff
        import difflib
        diff = '\n'.join(
            difflib.unified_diff(
                EXPECTED_JSON_CONTENT.splitlines(),
                actual_content.splitlines(),
                fromfile='expected',
                tofile='found',
                lineterm=''
            )
        )
        pytest.fail(
            f"The contents of '{NON_READ_PERMISSIONS_PATH}' are not exactly as required.\n"
            "Expected content:\n"
            f"{EXPECTED_JSON_CONTENT!r}\n"
            "Actual content:\n"
            f"{actual_content!r}\n"
            "Difference:\n"
            f"{diff}\n"
            "Ensure the JSON file matches the required structure, order, and formatting (no extra spaces, each object on its own line, no trailing commas, and correct array brackets)."
        )