# test_final_state.py

import os
import json
import csv
import pytest

HOME = "/home/user"
TRANSACTIONS_CSV = os.path.join(HOME, "user_transactions.csv")
PROFILES_JSON = os.path.join(HOME, "user_profiles.json")
OPTIMIZED_USERS_JSON = os.path.join(HOME, "optimized_query_users.json")
OPTIMIZATION_REPORT_CSV = os.path.join(HOME, "optimization_report.csv")

# ----- Ground-truth for verification -----

TRUTH_OPTIMIZED_USERS = [
    {
        "user_id": 2,
        "email": "bob@example.com",
        "sign_up_date": "2022-10-15",
        "last_login": "2024-05-13"
    },
    {
        "user_id": 5,
        "email": "emma@example.com",
        "sign_up_date": "2022-12-25",
        "last_login": "2024-05-15"
    }
]

TRUTH_OPTIMIZATION_REPORT = [
    ["user_id", "username", "completed_transaction_count"],
    ["2", "bob", "4"],
    ["5", "emma", "4"]
]

TRUTH_USER_IDS = {2, 5}


def test_optimized_query_users_json_exists():
    assert os.path.isfile(OPTIMIZED_USERS_JSON), (
        f"Missing required file: {OPTIMIZED_USERS_JSON}. "
        "You must create this file as a valid JSON array with the correct users and fields."
    )


def test_optimized_query_users_json_content():
    with open(OPTIMIZED_USERS_JSON, "r") as f:
        try:
            data = json.load(f)
        except Exception as e:
            pytest.fail(f"{OPTIMIZED_USERS_JSON} is not valid JSON: {e}")

    assert isinstance(data, list), (
        f"{OPTIMIZED_USERS_JSON} must be a JSON array. Found type: {type(data).__name__}"
    )
    # Check array length and each object
    assert len(data) == len(TRUTH_OPTIMIZED_USERS), (
        f"{OPTIMIZED_USERS_JSON} must contain exactly {len(TRUTH_OPTIMIZED_USERS)} user profiles "
        f"(found {len(data)})."
    )

    # Check all truth users are present, and only those
    # We'll compare as dicts, but ensure no extra keys
    expected_profiles = []
    for t in TRUTH_OPTIMIZED_USERS:
        expected_profiles.append({
            "user_id": t["user_id"],
            "email": t["email"],
            "sign_up_date": t["sign_up_date"],
            "last_login": t["last_login"]
        })

    actual_profiles = []
    for idx, profile in enumerate(data):
        assert isinstance(profile, dict), (
            f"Element {idx} in {OPTIMIZED_USERS_JSON} is not a JSON object."
        )
        keys = set(profile.keys())
        expected_keys = {"user_id", "email", "sign_up_date", "last_login"}
        extra = keys - expected_keys
        missing = expected_keys - keys
        assert not extra, (
            f"Profile at index {idx} in {OPTIMIZED_USERS_JSON} has unexpected fields: {sorted(extra)}."
        )
        assert not missing, (
            f"Profile at index {idx} in {OPTIMIZED_USERS_JSON} is missing fields: {sorted(missing)}."
        )
        # Ensure correct types
        assert isinstance(profile["user_id"], int), (
            f"Field 'user_id' in profile at index {idx} must be an integer."
        )
        for field in ("email", "sign_up_date", "last_login"):
            assert isinstance(profile[field], str), (
                f"Field '{field}' in profile at index {idx} must be a string."
            )
        actual_profiles.append(profile)

    # Sort both lists by user_id for comparison
    actual_profiles_sorted = sorted(actual_profiles, key=lambda x: x["user_id"])
    expected_profiles_sorted = sorted(expected_profiles, key=lambda x: x["user_id"])
    assert actual_profiles_sorted == expected_profiles_sorted, (
        f"{OPTIMIZED_USERS_JSON} does not match the expected user profiles.\n"
        f"Expected: {json.dumps(expected_profiles_sorted, indent=2)}\n"
        f"Found: {json.dumps(actual_profiles_sorted, indent=2)}"
    )


def test_optimization_report_csv_exists():
    assert os.path.isfile(OPTIMIZATION_REPORT_CSV), (
        f"Missing required file: {OPTIMIZATION_REPORT_CSV}. "
        "You must create this file as a CSV report for the correct users."
    )


def test_optimization_report_csv_content_and_format():
    with open(OPTIMIZATION_REPORT_CSV, newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Header must be exact
    assert rows, f"{OPTIMIZATION_REPORT_CSV} must not be empty."
    expected_header = ["user_id", "username", "completed_transaction_count"]
    assert rows[0] == expected_header, (
        f"{OPTIMIZATION_REPORT_CSV} header must be: {expected_header}\n"
        f"Found: {rows[0]}"
    )

    expected_data = TRUTH_OPTIMIZATION_REPORT[1:]
    actual_data = rows[1:]

    # Ensure row count is correct
    assert len(actual_data) == len(expected_data), (
        f"{OPTIMIZATION_REPORT_CSV} must have {len(expected_data)} data rows (found {len(actual_data)})."
    )

    # Ensure rows are sorted by user_id ascending (as string)
    user_ids = [row[0] for row in actual_data]
    assert user_ids == sorted(user_ids, key=int), (
        f"{OPTIMIZATION_REPORT_CSV} rows must be sorted by user_id ascending. Found order: {user_ids}"
    )

    # Check each row matches the truth (strict order)
    for idx, (actual, expected) in enumerate(zip(actual_data, expected_data)):
        assert actual == expected, (
            f"Row {idx+1} in {OPTIMIZATION_REPORT_CSV} does not match expected:\n"
            f"Expected: {expected}\nFound:    {actual}"
        )

    # Check for extra spaces or delimiters
    for idx, row in enumerate(actual_data):
        for field in row:
            assert field == field.strip(), (
                f"Field '{field}' in row {idx+1} of {OPTIMIZATION_REPORT_CSV} has unexpected leading/trailing spaces."
            )


def test_optimization_report_and_json_consistency():
    # Ensure report and optimized JSON are for the same users
    with open(OPTIMIZED_USERS_JSON) as f_json:
        json_data = json.load(f_json)
    with open(OPTIMIZATION_REPORT_CSV, newline="") as f_csv:
        reader = csv.DictReader(f_csv)
        csv_rows = list(reader)

    json_ids = set(profile["user_id"] for profile in json_data)
    csv_ids = set(int(row["user_id"]) for row in csv_rows)
    assert json_ids == TRUTH_USER_IDS, (
        f"{OPTIMIZED_USERS_JSON} must only contain user_ids: {sorted(TRUTH_USER_IDS)}. "
        f"Found user_ids: {sorted(json_ids)}"
    )
    assert csv_ids == TRUTH_USER_IDS, (
        f"{OPTIMIZATION_REPORT_CSV} must only report user_ids: {sorted(TRUTH_USER_IDS)}. "
        f"Found user_ids: {sorted(csv_ids)}"
    )
    # Check username and completed_transaction_count correctness (cross-check)
    expected_map = {str(t["user_id"]): (t["email"], t["sign_up_date"], t["last_login"])
                    for t in TRUTH_OPTIMIZED_USERS}
    for row in csv_rows:
        user_id = row["user_id"]
        username = row["username"]
        count = row["completed_transaction_count"]
        if user_id == "2":
            assert username == "bob", (
                f"user_id=2 in report should have username 'bob', found '{username}'"
            )
            assert count == "4", (
                f"user_id=2 in report should have completed_transaction_count 4, found '{count}'"
            )
        elif user_id == "5":
            assert username == "emma", (
                f"user_id=5 in report should have username 'emma', found '{username}'"
            )
            assert count == "4", (
                f"user_id=5 in report should have completed_transaction_count 4, found '{count}'"
            )
        else:
            pytest.fail(
                f"Unexpected user_id '{user_id}' in {OPTIMIZATION_REPORT_CSV}. "
                f"Only user_ids {sorted(TRUTH_USER_IDS)} are allowed."
            )