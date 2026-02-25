# test_final_state.py

import os
import json
import re
import pytest

OBS_DATA_DIR = "/home/user/obs-data"
CSV_PATH = os.path.join(OBS_DATA_DIR, "service_health.csv")
SUMMARY_CSV_PATH = os.path.join(OBS_DATA_DIR, "service_health_summary.csv")
SUMMARY_JSON_PATH = os.path.join(OBS_DATA_DIR, "service_health_summary.json")
LOG_PATH = os.path.join(OBS_DATA_DIR, "dashboard_update.log")

EXPECTED_SUMMARY_CSV = (
    "service_name,total_checks,success_count,failure_count,avg_response_time_ms\n"
    "api_gateway,3,2,1,305.33\n"
    "payment_service,2,1,1,520.00\n"
    "user_service,2,2,0,221.00\n"
)

EXPECTED_SUMMARY_JSON = [
    {
        "service_name": "api_gateway",
        "total_checks": 3,
        "success_count": 2,
        "failure_count": 1,
        "avg_response_time_ms": 305.33,
    },
    {
        "service_name": "payment_service",
        "total_checks": 2,
        "success_count": 1,
        "failure_count": 1,
        "avg_response_time_ms": 520.00,
    },
    {
        "service_name": "user_service",
        "total_checks": 2,
        "success_count": 2,
        "failure_count": 0,
        "avg_response_time_ms": 221.00,
    },
]

# Timestamp must be after 2023-10-10T14:29:00Z (i.e., '2023-10-10 14:29:00')
LOG_TIMESTAMP_REGEX = re.compile(
    r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (SUMMARY_CSV_CREATED|SUMMARY_JSON_CREATED): (.+)"
)

@pytest.mark.order(1)
def test_obs_data_dir_final_exists_and_owned():
    assert os.path.isdir(OBS_DATA_DIR), f"Directory {OBS_DATA_DIR} does not exist."
    import pwd
    stat_info = os.stat(OBS_DATA_DIR)
    uid = stat_info.st_uid
    try:
        owner = pwd.getpwuid(uid).pw_name
    except KeyError:
        owner = None
    assert owner == "user", f"Directory {OBS_DATA_DIR} is not owned by 'user' (found owner: '{owner}')"
    assert os.access(OBS_DATA_DIR, os.W_OK), f"Directory {OBS_DATA_DIR} is not writable by user."

@pytest.mark.order(2)
def test_only_expected_files_in_obs_data_dir():
    expected_files = {
        "service_health.csv",
        "service_health_summary.csv",
        "service_health_summary.json",
        "dashboard_update.log",
    }
    files = set(os.listdir(OBS_DATA_DIR))
    missing = expected_files - files
    extra = files - expected_files
    assert not missing, f"Missing expected file(s) in {OBS_DATA_DIR}: {missing}"
    assert not extra, f"Unexpected extra file(s) in {OBS_DATA_DIR}: {extra}"

@pytest.mark.order(3)
def test_service_health_summary_csv_contents():
    assert os.path.isfile(SUMMARY_CSV_PATH), f"Expected {SUMMARY_CSV_PATH} to exist."
    with open(SUMMARY_CSV_PATH, "r", encoding="utf-8") as f:
        contents = f.read()
    norm_contents = contents.replace('\r\n', '\n').replace('\r', '\n')
    # Remove possible trailing blank lines for comparison
    norm_contents = norm_contents.rstrip('\n') + '\n'
    expected = EXPECTED_SUMMARY_CSV
    assert (
        norm_contents == expected
    ), (
        f"service_health_summary.csv contents do not match expected.\n"
        f"Expected:\n{expected!r}\nGot:\n{norm_contents!r}"
    )

@pytest.mark.order(4)
def test_service_health_summary_json_contents():
    assert os.path.isfile(SUMMARY_JSON_PATH), f"Expected {SUMMARY_JSON_PATH} to exist."
    with open(SUMMARY_JSON_PATH, "r", encoding="utf-8") as f:
        contents = f.read()
    # Try to parse JSON, fail helpfully if not parseable
    try:
        data = json.loads(contents)
    except Exception as e:
        pytest.fail(f"Could not parse {SUMMARY_JSON_PATH} as JSON: {e}\nContents:\n{contents!r}")
    # Top-level structure must be a list
    assert isinstance(data, list), "JSON root must be an array."
    # Must match expected number/order of services
    assert len(data) == len(EXPECTED_SUMMARY_JSON), (
        f"JSON must have {len(EXPECTED_SUMMARY_JSON)} records, found {len(data)}"
    )
    for idx, (actual, expected) in enumerate(zip(data, EXPECTED_SUMMARY_JSON)):
        for key in expected:
            assert key in actual, (
                f"Record {idx} is missing key '{key}' in {SUMMARY_JSON_PATH}."
            )
            # Check types and values
            if isinstance(expected[key], float):
                # Allow up to two decimals, must match exactly as float
                assert isinstance(actual[key], (float, int)), (
                    f"Key '{key}' in record {idx} must be a number (not string)."
                )
                actual_float = round(float(actual[key]), 2)
                expected_float = round(float(expected[key]), 2)
                assert actual_float == expected_float, (
                    f"Key '{key}' in record {idx} expected {expected_float}, got {actual_float}."
                )
            else:
                assert actual[key] == expected[key], (
                    f"Key '{key}' in record {idx} expected {expected[key]!r}, got {actual[key]!r}."
                )
    # Check sorted order by service_name
    actual_service_names = [row["service_name"] for row in data]
    expected_service_names = [row["service_name"] for row in EXPECTED_SUMMARY_JSON]
    assert actual_service_names == sorted(expected_service_names), (
        f"JSON records are not sorted alphabetically by service_name.\n"
        f"Expected order: {sorted(expected_service_names)}\n"
        f"Got: {actual_service_names}"
    )

@pytest.mark.order(5)
def test_dashboard_update_log_format_and_contents():
    assert os.path.isfile(LOG_PATH), f"Expected {LOG_PATH} to exist."
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\r\n') for line in f]
    assert len(lines) == 2, (
        f"dashboard_update.log must have exactly 2 lines, found {len(lines)}"
    )
    # Validate each log line
    actions = ["SUMMARY_CSV_CREATED", "SUMMARY_JSON_CREATED"]
    paths = [SUMMARY_CSV_PATH, SUMMARY_JSON_PATH]
    min_ts = "2023-10-10 14:29:00"
    for i, line in enumerate(lines):
        m = LOG_TIMESTAMP_REGEX.fullmatch(line)
        assert m, (
            f"Log line {i+1} has incorrect format.\n"
            f"Expected: [YYYY-MM-DD HH:MM:SS] {actions[i]}: {paths[i]}\n"
            f"Got: {line!r}"
        )
        ts, action, fpath = m.groups()
        # Check action and file path
        assert action == actions[i], (
            f"Log line {i+1} action expected '{actions[i]}', got '{action}'."
        )
        assert fpath == paths[i], (
            f"Log line {i+1} file path expected '{paths[i]}', got '{fpath}'."
        )
        # Check timestamp is after cutoff and valid
        assert ts > min_ts, (
            f"Log line {i+1} timestamp {ts!r} is not after {min_ts!r}."
        )

@pytest.mark.order(6)
def test_no_extra_files_created():
    files = set(os.listdir(OBS_DATA_DIR))
    expected = {
        "service_health.csv",
        "service_health_summary.csv",
        "service_health_summary.json",
        "dashboard_update.log",
    }
    extra = files - expected
    assert not extra, f"Unexpected extra file(s) in {OBS_DATA_DIR}: {extra}"

@pytest.mark.order(7)
def test_summary_csv_and_json_are_not_symlinks():
    assert not os.path.islink(SUMMARY_CSV_PATH), f"{SUMMARY_CSV_PATH} must not be a symlink."
    assert not os.path.islink(SUMMARY_JSON_PATH), f"{SUMMARY_JSON_PATH} must not be a symlink."
    assert not os.path.islink(LOG_PATH), f"{LOG_PATH} must not be a symlink."