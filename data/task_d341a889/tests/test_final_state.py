# test_final_state.py
#
# Pytest suite to validate the FINAL state after cloud provisioning automation task.
# See task description for requirements and expected outputs.
#
import os
import json
import csv
import re
import pytest

HOME = "/home/user"
INVENTORY_PATH = os.path.join(HOME, "server_inventory.csv")
PROVISION_REQUESTS_PATH = os.path.join(HOME, "provision_requests.json")
AUDIT_LOG_PATH = os.path.join(HOME, "provisioning_audit.log")

EXPECTED_INVENTORY = (
    "hostname,ip_address,os_type,provisioned\n"
    "srv1,10.0.0.1,ubuntu,yes\n"
    "srv2,10.0.0.2,centos,yes\n"
    "srv3,10.0.0.3,debian,yes\n"
)

EXPECTED_PROVISION_REQUESTS = [
    {
        "hostname": "srv1",
        "ip_address": "10.0.0.1",
        "os_type": "ubuntu"
    },
    {
        "hostname": "srv3",
        "ip_address": "10.0.0.3",
        "os_type": "debian"
    }
]

AUDIT_LOG_REGEXES = [
    # Will match: [YYYY-MM-DD HH:MM:SS] Changed server srv1 provisioning status from 'no' to 'yes'
    re.compile(
        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] Changed server srv1 provisioning status from 'no' to 'yes'"
    ),
    # Will match: [YYYY-MM-DD HH:MM:SS] Changed server srv3 provisioning status from 'no' to 'yes'
    re.compile(
        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] Changed server srv3 provisioning status from 'no' to 'yes'"
    ),
]


def test_inventory_file_exists_and_contents():
    assert os.path.isfile(INVENTORY_PATH), (
        f"Missing inventory file at {INVENTORY_PATH} after completion."
    )
    with open(INVENTORY_PATH, "r", encoding="utf-8") as f:
        actual = f.read()
    assert actual == EXPECTED_INVENTORY, (
        f"The file {INVENTORY_PATH} does not have the expected FINAL contents.\n"
        "Expected contents:\n"
        f"{EXPECTED_INVENTORY}\n"
        "Actual contents:\n"
        f"{actual}"
    )


def test_provision_requests_json_exists_and_format():
    assert os.path.isfile(PROVISION_REQUESTS_PATH), (
        f"Missing required output file {PROVISION_REQUESTS_PATH}."
    )

    # Read and validate JSON structure
    with open(PROVISION_REQUESTS_PATH, "r", encoding="utf-8") as f:
        try:
            parsed = json.load(f)
        except Exception as e:
            pytest.fail(
                f"Failed to parse {PROVISION_REQUESTS_PATH} as JSON: {e}"
            )

    # Must be a list of length 2
    assert isinstance(parsed, list), (
        f"{PROVISION_REQUESTS_PATH} must contain a JSON array at the top level."
    )
    assert len(parsed) == 2, (
        f"{PROVISION_REQUESTS_PATH} must contain exactly 2 objects "
        f"(for the unprovisioned servers), but found {len(parsed)}."
    )

    # Each object must match the expected dictionaries, and not contain extra keys
    for idx, (actual, expected) in enumerate(zip(parsed, EXPECTED_PROVISION_REQUESTS)):
        assert isinstance(actual, dict), (
            f"Element {idx} in {PROVISION_REQUESTS_PATH} is not a JSON object."
        )
        assert set(actual.keys()) == set(expected.keys()), (
            f"Element {idx} in {PROVISION_REQUESTS_PATH} must have exactly the keys "
            f"{sorted(expected.keys())}, but has {sorted(actual.keys())}."
        )
        for k in expected:
            assert actual[k] == expected[k], (
                f"Element {idx} in {PROVISION_REQUESTS_PATH}: key '{k}' value is '{actual[k]}', "
                f"expected '{expected[k]}'."
            )

    # Now check pretty-printing (indented with 4 spaces, matches the format)
    with open(PROVISION_REQUESTS_PATH, "r", encoding="utf-8") as f:
        raw_json = f.read()

    # It should start with "[\n" and each object line should be indented by exactly 4 spaces
    lines = raw_json.splitlines()
    assert lines[0].strip() == "[", (
        f"{PROVISION_REQUESTS_PATH} must start with '[' on its own line (pretty-printed JSON)."
    )
    # Each object in the array should be indented by 4 spaces
    object_lines = [l for l in lines if l.strip().startswith('"hostname"')]
    for l in object_lines:
        assert l.startswith(" " * 8), (
            f"Each key in JSON objects in {PROVISION_REQUESTS_PATH} must be indented by 8 spaces "
            f"(4 for array, 4 for object), but got: {repr(l)}"
        )
    # Final line must be "]"
    assert lines[-1].strip() == "]", (
        f"{PROVISION_REQUESTS_PATH} must end with ']' on its own line."
    )


def test_inventory_csv_has_only_provisioned_yes():
    # Double-check that all 'provisioned' fields are 'yes'
    with open(INVENTORY_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    for row in rows:
        assert row["provisioned"] == "yes", (
            f"After automation, all servers must have 'provisioned' set to 'yes'.\n"
            f"Found row with hostname '{row['hostname']}' still marked as '{row['provisioned']}'."
        )


def test_audit_log_exists_and_format():
    assert os.path.isfile(AUDIT_LOG_PATH), (
        f"Missing audit log file at {AUDIT_LOG_PATH}."
    )
    with open(AUDIT_LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    assert len(lines) == 2, (
        f"{AUDIT_LOG_PATH} must contain exactly 2 log entries, one for each server updated from 'no' to 'yes'.\n"
        f"Actual lines:\n{lines}"
    )
    # Each line must match the expected regex in order (srv1, srv3)
    for idx, regex in enumerate(AUDIT_LOG_REGEXES):
        line = lines[idx]
        assert regex.fullmatch(line), (
            f"Line {idx+1} of {AUDIT_LOG_PATH} is not in the correct format.\n"
            f"Expected format: [YYYY-MM-DD HH:MM:SS] Changed server <hostname> provisioning status from 'no' to 'yes'\n"
            f"Actual line: {line}"
        )


def test_no_extra_files_created():
    # Only the three files should exist in /home/user (plus possibly .bashrc etc., but not more output files)
    allowed = {
        "server_inventory.csv",
        "provision_requests.json",
        "provisioning_audit.log",
    }
    user_files = os.listdir(HOME)
    extra_outputs = [f for f in user_files if f.startswith("provision") and f not in allowed]
    assert not extra_outputs, (
        f"Found unexpected files in {HOME}: {extra_outputs}.\n"
        "Only the three expected outputs should exist."
    )