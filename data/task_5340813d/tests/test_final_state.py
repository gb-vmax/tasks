# test_final_state.py

import csv
import io
import os
import pytest

TRIAGE_CSV_PATH = "/home/user/incidents/triage.csv"

EXPECTED_HEADER = ["id", "severity", "service", "title", "opened_at"]

EXPECTED_ROWS = [
    {"id": "INC-003", "severity": "critical", "service": "api-gateway", "title": "API gateway returning 503 errors", "opened_at": "2024-11-01T07:55:00Z"},
    {"id": "INC-007", "severity": "critical", "service": "auth", "title": "Auth service, token validation failing", "opened_at": "2024-11-01T08:05:00Z"},
    {"id": "INC-001", "severity": "critical", "service": "postgres", "title": "Database connection pool exhausted", "opened_at": "2024-11-01T08:23:00Z"},
    {"id": "INC-010", "severity": "critical", "service": "storage", "title": "Object storage bucket unreachable", "opened_at": "2024-11-01T09:00:00Z"},
    {"id": "INC-008", "severity": "high", "service": "search", "title": "Search index out of sync", "opened_at": "2024-11-01T08:50:00Z"},
    {"id": "INC-005", "severity": "high", "service": "payments", "title": "Payment service latency spike", "opened_at": "2024-11-01T09:45:00Z"},
]

EXPECTED_FULL_CONTENT = (
    "id,severity,service,title,opened_at\n"
    "INC-003,critical,api-gateway,API gateway returning 503 errors,2024-11-01T07:55:00Z\n"
    'INC-007,critical,auth,"Auth service, token validation failing",2024-11-01T08:05:00Z\n'
    "INC-001,critical,postgres,Database connection pool exhausted,2024-11-01T08:23:00Z\n"
    "INC-010,critical,storage,Object storage bucket unreachable,2024-11-01T09:00:00Z\n"
    "INC-008,high,search,Search index out of sync,2024-11-01T08:50:00Z\n"
    "INC-005,high,payments,Payment service latency spike,2024-11-01T09:45:00Z\n"
)


def test_triage_csv_exists():
    assert os.path.isfile(TRIAGE_CSV_PATH), (
        f"Triage CSV file '{TRIAGE_CSV_PATH}' does not exist. "
        "The task requires writing filtered incidents to this file."
    )


def test_triage_csv_is_readable():
    assert os.access(TRIAGE_CSV_PATH, os.R_OK), (
        f"Triage CSV file '{TRIAGE_CSV_PATH}' exists but is not readable."
    )


def test_triage_csv_exact_content():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        actual_content = f.read()
    assert actual_content == EXPECTED_FULL_CONTENT, (
        f"The content of '{TRIAGE_CSV_PATH}' does not match expected.\n"
        f"Expected:\n{EXPECTED_FULL_CONTENT!r}\n\n"
        f"Actual:\n{actual_content!r}"
    )


def test_triage_csv_header():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
    assert header is not None, (
        f"'{TRIAGE_CSV_PATH}' appears to be empty — no header row found."
    )
    assert header == EXPECTED_HEADER, (
        f"CSV header mismatch.\n"
        f"Expected: {EXPECTED_HEADER}\n"
        f"Actual:   {header}"
    )


def test_triage_csv_row_count():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    # rows includes header
    data_rows = rows[1:]
    assert len(data_rows) == 6, (
        f"Expected 6 data rows in '{TRIAGE_CSV_PATH}', but found {len(data_rows)}.\n"
        f"Rows present: {data_rows}"
    )


def test_triage_csv_row_order_and_values():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        reader = csv.DictReader(f)
        actual_rows = list(reader)

    assert len(actual_rows) == len(EXPECTED_ROWS), (
        f"Expected {len(EXPECTED_ROWS)} data rows but found {len(actual_rows)}."
    )

    for i, (actual, expected) in enumerate(zip(actual_rows, EXPECTED_ROWS)):
        for field in EXPECTED_HEADER:
            assert actual.get(field) == expected[field], (
                f"Row {i + 1} (0-indexed data row {i}): field '{field}' mismatch.\n"
                f"Expected: '{expected[field]}'\n"
                f"Actual:   '{actual.get(field)}'\n"
                f"Full actual row: {dict(actual)}\n"
                f"Full expected row: {expected}"
            )


def test_triage_csv_no_resolved_incidents():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    resolved_ids = {"INC-002", "INC-009"}
    found_resolved = [row for row in rows if row.get("id") in resolved_ids]
    assert not found_resolved, (
        f"Resolved incidents should not appear in triage.csv, but found: "
        f"{[r['id'] for r in found_resolved]}"
    )


def test_triage_csv_no_medium_or_low_severity():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    excluded_ids = {"INC-004", "INC-006"}
    found_excluded = [row for row in rows if row.get("id") in excluded_ids]
    assert not found_excluded, (
        f"Medium/low severity incidents should not appear in triage.csv, but found: "
        f"{[r['id'] for r in found_excluded]}"
    )


def test_triage_csv_only_critical_and_high():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        assert row.get("severity") in ("critical", "high"), (
            f"Row with id '{row.get('id')}' has severity '{row.get('severity')}', "
            f"but only 'critical' and 'high' should be included."
        )


def test_triage_csv_critical_before_high():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    severities = [row["severity"] for row in rows]
    # Once we see a 'high', we should not see 'critical' again
    seen_high = False
    for sev in severities:
        if sev == "high":
            seen_high = True
        if seen_high and sev == "critical":
            pytest.fail(
                f"Sort order is wrong: found 'critical' row after 'high' row. "
                f"All critical rows must come before all high rows. "
                f"Severity order in file: {severities}"
            )


def test_triage_csv_sorted_by_opened_at_within_severity():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    critical_rows = [r for r in rows if r["severity"] == "critical"]
    high_rows = [r for r in rows if r["severity"] == "high"]

    critical_timestamps = [r["opened_at"] for r in critical_rows]
    assert critical_timestamps == sorted(critical_timestamps), (
        f"Critical rows are not sorted by opened_at ascending.\n"
        f"Actual order: {critical_timestamps}\n"
        f"Expected order: {sorted(critical_timestamps)}"
    )

    high_timestamps = [r["opened_at"] for r in high_rows]
    assert high_timestamps == sorted(high_timestamps), (
        f"High rows are not sorted by opened_at ascending.\n"
        f"Actual order: {high_timestamps}\n"
        f"Expected order: {sorted(high_timestamps)}"
    )


def test_triage_csv_comma_in_title_is_quoted():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        raw_content = f.read()

    # INC-007 has a comma in its title; find the line for INC-007
    lines = raw_content.splitlines()
    inc007_line = next((line for line in lines if line.startswith("INC-007,")), None)
    assert inc007_line is not None, (
        "INC-007 line not found in triage.csv."
    )
    # The title with a comma must be quoted
    assert '"Auth service, token validation failing"' in inc007_line, (
        f"INC-007 title contains a comma and must be wrapped in double quotes in CSV.\n"
        f"Actual line: {inc007_line}"
    )


def test_triage_csv_line_endings_are_unix():
    with open(TRIAGE_CSV_PATH, "rb") as f:
        raw_bytes = f.read()

    assert b"\r\n" not in raw_bytes, (
        f"'{TRIAGE_CSV_PATH}' contains Windows-style line endings (\\r\\n). "
        "The file must use Unix line endings (\\n only)."
    )
    assert b"\r" not in raw_bytes, (
        f"'{TRIAGE_CSV_PATH}' contains carriage return characters (\\r). "
        "The file must use Unix line endings (\\n only)."
    )


def test_triage_csv_ends_with_single_newline():
    with open(TRIAGE_CSV_PATH, "rb") as f:
        raw_bytes = f.read()

    assert raw_bytes.endswith(b"\n"), (
        f"'{TRIAGE_CSV_PATH}' does not end with a newline character. "
        "The last data row must end with \\n."
    )
    assert not raw_bytes.endswith(b"\n\n"), (
        f"'{TRIAGE_CSV_PATH}' ends with more than one newline (trailing blank line). "
        "There should be exactly one newline after the last data row."
    )


def test_triage_csv_line_count():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        raw_content = f.read()

    # Split on \n; last element after final \n should be empty string
    lines = raw_content.split("\n")
    # The file should have 7 lines of content + trailing newline = 8 parts when split
    # i.e., lines[7] == ""
    non_empty_lines = [l for l in lines if l]
    assert len(non_empty_lines) == 7, (
        f"Expected 7 non-empty lines (1 header + 6 data rows) in '{TRIAGE_CSV_PATH}', "
        f"but found {len(non_empty_lines)}.\n"
        f"Lines: {non_empty_lines}"
    )


def test_triage_csv_column_count_per_row():
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    for i, row in enumerate(rows):
        assert len(row) == 5, (
            f"Row {i} has {len(row)} columns but expected 5.\n"
            f"Row content: {row}"
        )


def test_triage_csv_all_expected_incident_ids_present():
    expected_ids = {"INC-001", "INC-003", "INC-005", "INC-007", "INC-008", "INC-010"}
    with open(TRIAGE_CSV_PATH, "r", newline="") as f:
        reader = csv.DictReader(f)
        actual_ids = {row["id"] for row in reader}

    assert actual_ids == expected_ids, (
        f"The set of incident IDs in triage.csv does not match expected.\n"
        f"Expected IDs: {sorted(expected_ids)}\n"
        f"Actual IDs:   {sorted(actual_ids)}\n"
        f"Missing: {sorted(expected_ids - actual_ids)}\n"
        f"Extra:   {sorted(actual_ids - expected_ids)}"
    )