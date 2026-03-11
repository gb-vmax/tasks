# test_final_state.py

import os
import pytest

ACTIVE_USERS_CSV = "/home/user/active_users.csv"
ACTIVE_COUNT_TXT = "/home/user/active_count.txt"

EXPECTED_CSV_CONTENT = (
    "id,username,email,first_name,last_name,department,created_at\n"
    "1,jdoe,jdoe@example.com,John,Doe,Engineering,2024-01-15\n"
    "3,bsmith,bsmith@example.com,Bob,Smith,Marketing,2024-03-10\n"
    "5,tlee,tlee@example.com,Tom,Lee,HR,2023-08-19\n"
    "12,mwilliams,mwilliams@example.com,Maria,Williams,Engineering,2024-01-05\n"
)

EXPECTED_HEADER = "id,username,email,first_name,last_name,department,created_at"

EXPECTED_DATA_ROWS = [
    "1,jdoe,jdoe@example.com,John,Doe,Engineering,2024-01-15",
    "3,bsmith,bsmith@example.com,Bob,Smith,Marketing,2024-03-10",
    "5,tlee,tlee@example.com,Tom,Lee,HR,2023-08-19",
    "12,mwilliams,mwilliams@example.com,Maria,Williams,Engineering,2024-01-05",
]

EXPECTED_COUNT = 4


# ── CSV file tests ────────────────────────────────────────────────────────────

def test_active_users_csv_exists():
    assert os.path.isfile(ACTIVE_USERS_CSV), (
        f"Expected CSV file does not exist: {ACTIVE_USERS_CSV}"
    )


def test_active_users_csv_is_readable():
    assert os.access(ACTIVE_USERS_CSV, os.R_OK), (
        f"CSV file is not readable: {ACTIVE_USERS_CSV}"
    )


def test_active_users_csv_exact_content():
    with open(ACTIVE_USERS_CSV, "r") as f:
        content = f.read()
    assert content == EXPECTED_CSV_CONTENT, (
        f"CSV file content does not match expected.\n"
        f"Expected:\n{EXPECTED_CSV_CONTENT!r}\n"
        f"Got:\n{content!r}"
    )


def test_active_users_csv_header():
    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = f.read().splitlines()
    assert len(lines) >= 1, "CSV file is empty; expected at least a header line."
    assert lines[0] == EXPECTED_HEADER, (
        f"CSV header mismatch.\n"
        f"Expected: {EXPECTED_HEADER!r}\n"
        f"Got:      {lines[0]!r}"
    )


def test_active_users_csv_row_count():
    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = [line for line in f.read().splitlines() if line]
    # lines[0] is the header
    data_rows = lines[1:]
    assert len(data_rows) == EXPECTED_COUNT, (
        f"Expected {EXPECTED_COUNT} data rows in CSV, got {len(data_rows)}.\n"
        f"Rows found: {data_rows}"
    )


def test_active_users_csv_data_rows():
    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = f.read().splitlines()
    data_rows = [line for line in lines[1:] if line]
    assert data_rows == EXPECTED_DATA_ROWS, (
        f"CSV data rows do not match expected.\n"
        f"Expected rows:\n" + "\n".join(EXPECTED_DATA_ROWS) + "\n"
        f"Got rows:\n" + "\n".join(data_rows)
    )


def test_active_users_csv_sorted_by_id():
    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = f.read().splitlines()
    data_rows = [line for line in lines[1:] if line]
    ids = []
    for row in data_rows:
        fields = row.split(",")
        assert fields[0].isdigit(), (
            f"First field (id) is not a digit in row: {row!r}"
        )
        ids.append(int(fields[0]))
    assert ids == sorted(ids), (
        f"CSV rows are not sorted by id in ascending order. Got ids: {ids}"
    )


def test_active_users_csv_no_inactive_users():
    with open(ACTIVE_USERS_CSV, "r") as f:
        content = f.read()
    assert "ajones" not in content, (
        "Inactive user 'ajones' (id=7) should NOT appear in active_users.csv, but was found."
    )
    assert "kpatel" not in content, (
        "Suspended user 'kpatel' (id=19) should NOT appear in active_users.csv, but was found."
    )


def test_active_users_csv_contains_all_active_users():
    with open(ACTIVE_USERS_CSV, "r") as f:
        content = f.read()
    for username in ("jdoe", "bsmith", "tlee", "mwilliams"):
        assert username in content, (
            f"Active user '{username}' is missing from {ACTIVE_USERS_CSV}."
        )


def test_active_users_csv_no_extra_spaces():
    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = f.read().splitlines()
    for line in lines:
        if not line:
            continue
        assert " ," not in line and ", " not in line, (
            f"Found extra spaces around commas in line: {line!r}"
        )


def test_active_users_csv_no_trailing_comma():
    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = f.read().splitlines()
    for line in lines:
        if not line:
            continue
        assert not line.endswith(","), (
            f"Line has a trailing comma: {line!r}"
        )


def test_active_users_csv_correct_column_count():
    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = f.read().splitlines()
    for line in lines:
        if not line:
            continue
        fields = line.split(",")
        assert len(fields) == 7, (
            f"Expected 7 columns per row, got {len(fields)} in line: {line!r}"
        )


def test_active_users_csv_specific_row_jdoe():
    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = f.read().splitlines()
    data_rows = [line for line in lines[1:] if line]
    jdoe_row = next((r for r in data_rows if r.startswith("1,")), None)
    assert jdoe_row is not None, "Row for jdoe (id=1) not found in CSV."
    assert jdoe_row == "1,jdoe,jdoe@example.com,John,Doe,Engineering,2024-01-15", (
        f"jdoe row mismatch. Got: {jdoe_row!r}"
    )


def test_active_users_csv_specific_row_bsmith():
    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = f.read().splitlines()
    data_rows = [line for line in lines[1:] if line]
    bsmith_row = next((r for r in data_rows if r.startswith("3,")), None)
    assert bsmith_row is not None, "Row for bsmith (id=3) not found in CSV."
    assert bsmith_row == "3,bsmith,bsmith@example.com,Bob,Smith,Marketing,2024-03-10", (
        f"bsmith row mismatch. Got: {bsmith_row!r}"
    )


def test_active_users_csv_specific_row_tlee():
    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = f.read().splitlines()
    data_rows = [line for line in lines[1:] if line]
    tlee_row = next((r for r in data_rows if r.startswith("5,")), None)
    assert tlee_row is not None, "Row for tlee (id=5) not found in CSV."
    assert tlee_row == "5,tlee,tlee@example.com,Tom,Lee,HR,2023-08-19", (
        f"tlee row mismatch. Got: {tlee_row!r}"
    )


def test_active_users_csv_specific_row_mwilliams():
    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = f.read().splitlines()
    data_rows = [line for line in lines[1:] if line]
    mwilliams_row = next((r for r in data_rows if r.startswith("12,")), None)
    assert mwilliams_row is not None, "Row for mwilliams (id=12) not found in CSV."
    assert mwilliams_row == "12,mwilliams,mwilliams@example.com,Maria,Williams,Engineering,2024-01-05", (
        f"mwilliams row mismatch. Got: {mwilliams_row!r}"
    )


# ── Count file tests ──────────────────────────────────────────────────────────

def test_active_count_txt_exists():
    assert os.path.isfile(ACTIVE_COUNT_TXT), (
        f"Expected count file does not exist: {ACTIVE_COUNT_TXT}"
    )


def test_active_count_txt_is_readable():
    assert os.access(ACTIVE_COUNT_TXT, os.R_OK), (
        f"Count file is not readable: {ACTIVE_COUNT_TXT}"
    )


def test_active_count_txt_content():
    with open(ACTIVE_COUNT_TXT, "r") as f:
        content = f.read()
    stripped = content.strip()
    assert stripped == str(EXPECTED_COUNT), (
        f"Expected {ACTIVE_COUNT_TXT} to contain '{EXPECTED_COUNT}', "
        f"but got: {content!r}"
    )


def test_active_count_txt_is_integer():
    with open(ACTIVE_COUNT_TXT, "r") as f:
        content = f.read().strip()
    assert content.isdigit(), (
        f"Content of {ACTIVE_COUNT_TXT} is not a plain integer. Got: {content!r}"
    )


def test_active_count_txt_matches_csv_rows():
    with open(ACTIVE_COUNT_TXT, "r") as f:
        count_str = f.read().strip()
    assert count_str.isdigit(), (
        f"Count file does not contain a plain integer: {count_str!r}"
    )
    count = int(count_str)

    with open(ACTIVE_USERS_CSV, "r") as f:
        lines = f.read().splitlines()
    data_rows = [line for line in lines[1:] if line]

    assert count == len(data_rows), (
        f"Count in {ACTIVE_COUNT_TXT} ({count}) does not match "
        f"the number of data rows in {ACTIVE_USERS_CSV} ({len(data_rows)})."
    )