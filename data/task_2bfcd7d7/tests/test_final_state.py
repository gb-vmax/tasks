# test_final_state.py

import os
import csv
import json
import pytest

REGISTRY_PATH = "/home/user/configs/registry.json"
SUMMARY_PATH = "/home/user/configs/summary.csv"
CONFIGS_DIR = "/home/user/configs"

EXPECTED_HEADER = ["service", "env", "version", "last_modified"]

EXPECTED_ROWS = [
    ["auth-service", "production", "2.3.1", "2024-11-01"],
    ["cache-manager", "development", "0.9.2", "2024-11-20"],
    ["data-pipeline", "production", "3.1.0", "2024-09-30"],
    ["feature-flags", "production", "1.5.3", "2024-10-22"],
]

EXPECTED_LINES = [
    "service,env,version,last_modified",
    "auth-service,production,2.3.1,2024-11-01",
    "cache-manager,development,0.9.2,2024-11-20",
    "data-pipeline,production,3.1.0,2024-09-30",
    "feature-flags,production,1.5.3,2024-10-22",
]


def test_configs_directory_exists():
    assert os.path.isdir(CONFIGS_DIR), (
        f"Directory '{CONFIGS_DIR}' does not exist. "
        "The configs directory must be present."
    )


def test_summary_file_exists():
    assert os.path.isfile(SUMMARY_PATH), (
        f"File '{SUMMARY_PATH}' does not exist. "
        "The task requires creating summary.csv in /home/user/configs/."
    )


def test_summary_file_is_readable():
    assert os.access(SUMMARY_PATH, os.R_OK), (
        f"File '{SUMMARY_PATH}' is not readable. "
        "Please ensure the file has appropriate read permissions."
    )


def test_summary_no_carriage_returns():
    with open(SUMMARY_PATH, "rb") as f:
        raw_content = f.read()
    assert b"\r" not in raw_content, (
        f"File '{SUMMARY_PATH}' contains carriage return characters (\\r). "
        "The file must use Unix line endings only (no \\r\\n)."
    )


def test_summary_no_trailing_blank_lines():
    with open(SUMMARY_PATH, "rb") as f:
        raw_content = f.read()
    # The file should end with exactly one newline (after the last data row)
    # and not have extra blank lines
    decoded = raw_content.decode("utf-8")
    # Strip the single trailing newline and check there are no more trailing newlines
    assert not decoded.endswith("\n\n"), (
        f"File '{SUMMARY_PATH}' has extra blank lines at the end. "
        "There should be no trailing blank lines after the last data row."
    )


def test_summary_ends_with_newline():
    with open(SUMMARY_PATH, "rb") as f:
        raw_content = f.read()
    assert raw_content.endswith(b"\n"), (
        f"File '{SUMMARY_PATH}' does not end with a newline character. "
        "The file should end with a Unix newline after the last record."
    )


def test_summary_exact_line_count():
    with open(SUMMARY_PATH, "r", newline="") as f:
        content = f.read()
    # Split on newlines; last element after final \n should be empty
    lines = content.split("\n")
    # Remove trailing empty string caused by final newline
    if lines and lines[-1] == "":
        lines = lines[:-1]
    assert len(lines) == 5, (
        f"File '{SUMMARY_PATH}' has {len(lines)} lines, but expected 5 "
        "(1 header + 4 data rows). "
        f"Actual lines: {lines}"
    )


def test_summary_header_row():
    with open(SUMMARY_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
    assert header == EXPECTED_HEADER, (
        f"Header row in '{SUMMARY_PATH}' is incorrect. "
        f"Expected: {EXPECTED_HEADER}, "
        f"Got: {header}. "
        "The header must be exactly: service,env,version,last_modified"
    )


def test_summary_no_enabled_column():
    with open(SUMMARY_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
    assert "enabled" not in header, (
        f"The 'enabled' column should NOT appear in '{SUMMARY_PATH}', "
        f"but the header contains: {header}."
    )


def test_summary_excludes_disabled_entries():
    with open(SUMMARY_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        rows = list(reader)
    services_in_csv = [row[0] for row in rows if row]
    assert "billing-api" not in services_in_csv, (
        f"'billing-api' should NOT appear in '{SUMMARY_PATH}' because it is disabled. "
        f"Services found: {services_in_csv}"
    )
    assert "email-worker" not in services_in_csv, (
        f"'email-worker' should NOT appear in '{SUMMARY_PATH}' because it is disabled. "
        f"Services found: {services_in_csv}"
    )


def test_summary_includes_only_enabled_entries():
    with open(SUMMARY_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        rows = [row for row in reader if row]
    services_in_csv = [row[0] for row in rows]
    expected_services = ["auth-service", "cache-manager", "data-pipeline", "feature-flags"]
    for svc in expected_services:
        assert svc in services_in_csv, (
            f"Service '{svc}' is enabled but is missing from '{SUMMARY_PATH}'. "
            f"Services found: {services_in_csv}"
        )


def test_summary_sorted_alphabetically_by_service():
    with open(SUMMARY_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        rows = [row for row in reader if row]
    services = [row[0] for row in rows]
    assert services == sorted(services), (
        f"Rows in '{SUMMARY_PATH}' are not sorted alphabetically by service name. "
        f"Current order: {services}, "
        f"Expected order: {sorted(services)}"
    )


def test_summary_data_rows_match_expected():
    with open(SUMMARY_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        rows = [row for row in reader if row]

    assert len(rows) == len(EXPECTED_ROWS), (
        f"Expected {len(EXPECTED_ROWS)} data rows in '{SUMMARY_PATH}', "
        f"but found {len(rows)}. "
        f"Rows found: {rows}"
    )

    for i, (actual, expected) in enumerate(zip(rows, EXPECTED_ROWS)):
        assert actual == expected, (
            f"Row {i + 1} in '{SUMMARY_PATH}' does not match expected. "
            f"Expected: {expected}, "
            f"Got: {actual}."
        )


def test_summary_column_order():
    with open(SUMMARY_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader if row]

    assert header == ["service", "env", "version", "last_modified"], (
        f"Column order in '{SUMMARY_PATH}' is wrong. "
        f"Expected: ['service', 'env', 'version', 'last_modified'], "
        f"Got: {header}"
    )

    # Verify data rows have 4 columns
    for i, row in enumerate(rows):
        assert len(row) == 4, (
            f"Data row {i + 1} in '{SUMMARY_PATH}' has {len(row)} columns, "
            f"expected 4. Row content: {row}"
        )


def test_summary_no_trailing_spaces_in_lines():
    with open(SUMMARY_PATH, "r", newline="") as f:
        content = f.read()
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if line == "" and i == len(lines) - 1:
            continue  # skip the trailing empty string after final newline
        assert line == line.rstrip(), (
            f"Line {i + 1} in '{SUMMARY_PATH}' has trailing spaces: {repr(line)}. "
            "No trailing spaces are allowed."
        )


def test_summary_exact_content():
    """Verify the exact content of the file matches expected output."""
    with open(SUMMARY_PATH, "r", newline="") as f:
        content = f.read()

    expected_content = "\n".join(EXPECTED_LINES) + "\n"

    assert content == expected_content, (
        f"Content of '{SUMMARY_PATH}' does not exactly match expected output.\n"
        f"Expected:\n{repr(expected_content)}\n"
        f"Got:\n{repr(content)}"
    )


def test_registry_file_unchanged():
    """Verify the original registry.json was not modified."""
    expected_registry = [
        {"service": "auth-service", "env": "production", "last_modified": "2024-11-01", "enabled": True, "version": "2.3.1"},
        {"service": "billing-api", "env": "staging", "last_modified": "2024-10-15", "enabled": False, "version": "1.0.4"},
        {"service": "cache-manager", "env": "development", "last_modified": "2024-11-20", "enabled": True, "version": "0.9.2"},
        {"service": "data-pipeline", "env": "production", "last_modified": "2024-09-30", "enabled": True, "version": "3.1.0"},
        {"service": "email-worker", "env": "staging", "last_modified": "2024-11-05", "enabled": False, "version": "1.2.0"},
        {"service": "feature-flags", "env": "production", "last_modified": "2024-10-22", "enabled": True, "version": "1.5.3"},
    ]

    assert os.path.isfile(REGISTRY_PATH), (
        f"Registry file '{REGISTRY_PATH}' no longer exists. It should not have been deleted."
    )

    with open(REGISTRY_PATH, "r") as f:
        actual_registry = json.load(f)

    actual_sorted = sorted(actual_registry, key=lambda x: x["service"])
    expected_sorted = sorted(expected_registry, key=lambda x: x["service"])

    assert actual_sorted == expected_sorted, (
        f"Registry file '{REGISTRY_PATH}' has been modified. "
        f"Expected: {expected_sorted}, "
        f"Got: {actual_sorted}"
    )