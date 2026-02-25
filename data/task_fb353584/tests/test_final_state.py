# test_final_state.py

import os
import pytest
import csv
import json

CSV_PATH = "/home/user/translations.csv"
JSON_PATH = "/home/user/translations_fr.json"

EXPECTED_CSV_ROWS = [
    {"key": "greeting", "en": "Hello",    "fr": "Salut"},
    {"key": "farewell", "en": "Goodbye",  "fr": "Au revoir"},
    {"key": "welcome",  "en": "Welcome",  "fr": "Bienvenue"},
]

EXPECTED_JSON = {
    "Hello": "Salut",
    "Goodbye": "Au revoir",
    "Welcome": "Bienvenue"
}

EXPECTED_JSON_PRETTY = (
    '{\n'
    '  "Hello": "Salut",\n'
    '  "Goodbye": "Au revoir",\n'
    '  "Welcome": "Bienvenue"\n'
    '}'
)


def test_translations_csv_exists():
    assert os.path.isfile(CSV_PATH), (
        f"Expected file missing: {CSV_PATH}. "
        "You must not delete or rename the original CSV file."
    )


def test_translations_csv_content_final():
    """
    Verify /home/user/translations.csv has the correct final content after the update.
    """
    with open(CSV_PATH, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        actual_rows = list(reader)

    expected_fields = ["key", "en", "fr"]
    assert reader.fieldnames == expected_fields, (
        f"CSV file {CSV_PATH} columns must be {expected_fields}, "
        f"but found: {reader.fieldnames}"
    )

    assert len(actual_rows) == len(EXPECTED_CSV_ROWS), (
        f"CSV file {CSV_PATH} should have {len(EXPECTED_CSV_ROWS)} data rows, "
        f"but found {len(actual_rows)}."
    )

    for i, (actual, expected) in enumerate(zip(actual_rows, EXPECTED_CSV_ROWS)):
        for field in expected_fields:
            assert actual[field] == expected[field], (
                f"CSV file {CSV_PATH} row {i+2} (key={expected['key']}): "
                f"expected {field}='{expected[field]}', found '{actual[field]}'."
            )


def test_translations_fr_json_exists():
    assert os.path.isfile(JSON_PATH), (
        f"Missing required output file: {JSON_PATH}. "
        "You must create this file as part of the task."
    )


def test_translations_fr_json_content():
    """
    Verify that /home/user/translations_fr.json has the correct pretty-printed JSON content and structure.
    """
    # Check exact content for pretty-printing and ordering
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Check for exact pretty-print (including 2-space indentation and order)
    if content != EXPECTED_JSON_PRETTY:
        # Try to provide a helpful diff
        import difflib
        diff = "\n".join(difflib.unified_diff(
            EXPECTED_JSON_PRETTY.splitlines(),
            content.splitlines(),
            fromfile="expected",
            tofile="actual",
            lineterm=""
        ))
        pytest.fail(
            f"The file {JSON_PATH} does not match the required pretty-printed JSON format "
            f"with 2-space indentation and correct order/values.\n"
            f"Expected content:\n{EXPECTED_JSON_PRETTY}\n"
            f"Actual content:\n{content}\n"
            f"Diff:\n{diff}"
        )

    # Also check structure and values just in case (parsing)
    try:
        data = json.loads(content)
    except Exception as e:
        pytest.fail(
            f"The file {JSON_PATH} contains invalid JSON: {e}"
        )

    assert isinstance(data, dict), (
        f"The file {JSON_PATH} must contain a top-level JSON object (dictionary)."
    )
    assert data == EXPECTED_JSON, (
        f"The JSON object in {JSON_PATH} does not have the expected keys/values.\n"
        f"Expected: {EXPECTED_JSON}\n"
        f"Actual: {data}"
    )


def test_translations_fr_json_no_extra_keys():
    """
    Ensure no extra keys are present in the output JSON.
    """
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    extra_keys = set(data.keys()) - set(EXPECTED_JSON.keys())
    assert not extra_keys, (
        f"The file {JSON_PATH} contains unexpected keys: {extra_keys}."
    )