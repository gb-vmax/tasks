# test_final_state.py

import json
import os
import pytest

OUTPUT_JSON = "/home/user/store/active_products.json"

EXPECTED_CONTENT = (
    '[\n'
    '  {\n'
    '    "id": "P001",\n'
    '    "name": "Widget A",\n'
    '    "price": 9.99,\n'
    '    "category": "widgets"\n'
    '  },\n'
    '  {\n'
    '    "id": "P003",\n'
    '    "name": "Thingamajig",\n'
    '    "price": 4.75,\n'
    '    "category": "misc"\n'
    '  },\n'
    '  {\n'
    '    "id": "P005",\n'
    '    "name": "Doohickey",\n'
    '    "price": 7.25,\n'
    '    "category": "misc"\n'
    '  },\n'
    '  {\n'
    '    "id": "P006",\n'
    '    "name": "Mega Gadget",\n'
    '    "price": 49.99,\n'
    '    "category": "gadgets"\n'
    '  }\n'
    ']'
)

EXPECTED_OBJECTS = [
    {"id": "P001", "name": "Widget A",    "price": 9.99,  "category": "widgets"},
    {"id": "P003", "name": "Thingamajig", "price": 4.75,  "category": "misc"},
    {"id": "P005", "name": "Doohickey",   "price": 7.25,  "category": "misc"},
    {"id": "P006", "name": "Mega Gadget", "price": 49.99, "category": "gadgets"},
]


def test_output_file_exists():
    assert os.path.isfile(OUTPUT_JSON), (
        f"Expected output file '{OUTPUT_JSON}' to exist, but it does not. "
        "The task requires writing active products to this path."
    )


def test_output_file_is_readable():
    assert os.access(OUTPUT_JSON, os.R_OK), (
        f"Output file '{OUTPUT_JSON}' exists but is not readable."
    )


def test_output_file_is_valid_json():
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        content = f.read()
    try:
        json.loads(content)
    except json.JSONDecodeError as e:
        pytest.fail(
            f"Output file '{OUTPUT_JSON}' is not valid JSON.\n"
            f"JSON parse error: {e}"
        )


def test_output_is_json_array():
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, list), (
        f"Expected the top-level JSON value in '{OUTPUT_JSON}' to be an array, "
        f"but got {type(data).__name__}."
    )


def test_output_has_correct_number_of_entries():
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 4, (
        f"Expected 4 active product entries in '{OUTPUT_JSON}', "
        f"but found {len(data)}. "
        "Active products should be: P001, P003, P005, P006."
    )


def test_output_entries_are_objects():
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    for i, item in enumerate(data):
        assert isinstance(item, dict), (
            f"Entry at index {i} in '{OUTPUT_JSON}' is not a JSON object; "
            f"got {type(item).__name__}."
        )


def test_output_no_status_field():
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    for i, item in enumerate(data):
        assert "status" not in item, (
            f"Entry at index {i} in '{OUTPUT_JSON}' still contains the 'status' field, "
            "which should have been dropped."
        )


def test_output_required_keys_present():
    required_keys = {"id", "name", "price", "category"}
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    for i, item in enumerate(data):
        missing = required_keys - set(item.keys())
        assert not missing, (
            f"Entry at index {i} in '{OUTPUT_JSON}' is missing required keys: {missing}. "
            f"Entry: {item}"
        )


def test_output_no_extra_keys():
    allowed_keys = {"id", "name", "price", "category"}
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    for i, item in enumerate(data):
        extra = set(item.keys()) - allowed_keys
        assert not extra, (
            f"Entry at index {i} in '{OUTPUT_JSON}' has unexpected keys: {extra}. "
            f"Only 'id', 'name', 'price', 'category' are allowed."
        )


def test_output_key_order():
    expected_key_order = ["id", "name", "price", "category"]
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    for i, item in enumerate(data):
        actual_keys = list(item.keys())
        assert actual_keys == expected_key_order, (
            f"Entry at index {i} in '{OUTPUT_JSON}' has incorrect key order.\n"
            f"Expected order: {expected_key_order}\n"
            f"Actual order:   {actual_keys}"
        )


def test_output_price_is_float():
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    for i, item in enumerate(data):
        price = item.get("price")
        assert isinstance(price, float), (
            f"Entry at index {i} in '{OUTPUT_JSON}' has 'price' of type "
            f"{type(price).__name__!r} (value: {price!r}). "
            "Expected a JSON number (float), not a string."
        )


def test_output_correct_values():
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == len(EXPECTED_OBJECTS), (
        f"Cannot compare values: expected {len(EXPECTED_OBJECTS)} entries, "
        f"found {len(data)}."
    )
    for i, (actual, expected) in enumerate(zip(data, EXPECTED_OBJECTS)):
        assert actual["id"] == expected["id"], (
            f"Entry at index {i}: 'id' mismatch. "
            f"Expected {expected['id']!r}, got {actual['id']!r}."
        )
        assert actual["name"] == expected["name"], (
            f"Entry at index {i}: 'name' mismatch. "
            f"Expected {expected['name']!r}, got {actual['name']!r}."
        )
        assert actual["price"] == pytest.approx(expected["price"]), (
            f"Entry at index {i}: 'price' mismatch. "
            f"Expected {expected['price']}, got {actual['price']}."
        )
        assert actual["category"] == expected["category"], (
            f"Entry at index {i}: 'category' mismatch. "
            f"Expected {expected['category']!r}, got {actual['category']!r}."
        )


def test_output_only_active_products():
    inactive_ids = {"P002", "P004"}
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    found_ids = {item.get("id") for item in data}
    overlap = found_ids & inactive_ids
    assert not overlap, (
        f"Output file '{OUTPUT_JSON}' contains inactive product IDs: {overlap}. "
        "Only active products (P001, P003, P005, P006) should be included."
    )


def test_output_pretty_printed_two_space_indent():
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.splitlines()
    # Check that object-level keys are indented with exactly 4 spaces (2 for array + 2 for object)
    key_lines = [line for line in lines if line.lstrip().startswith('"id"')]
    assert key_lines, (
        f"Could not find any lines starting with '\"id\"' in '{OUTPUT_JSON}'. "
        "Is the file pretty-printed?"
    )
    for line in key_lines:
        assert line.startswith("    "), (
            f"Expected key lines to be indented with 4 spaces (2-space indent), "
            f"but found: {line!r}"
        )


def test_output_no_trailing_newline():
    with open(OUTPUT_JSON, "rb") as f:
        content = f.read()
    assert content.endswith(b"]"), (
        f"Output file '{OUTPUT_JSON}' should end with ']' and have no trailing newline. "
        f"Last bytes: {content[-5:]!r}"
    )


def test_output_exact_content():
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        actual_content = f.read()
    assert actual_content == EXPECTED_CONTENT, (
        f"Content of '{OUTPUT_JSON}' does not exactly match the expected output.\n"
        f"--- Expected ---\n{EXPECTED_CONTENT}\n"
        f"--- Actual ---\n{actual_content}"
    )