# test_final_state.py

import json
import os
import pytest

DEPLOYMENTS_DIR = "/home/user/deployments"
MANIFEST_PATH = "/home/user/deployments/manifest.json"
PRODUCTION_READY_PATH = "/home/user/deployments/production_ready.json"
REPLICA_COUNT_PATH = "/home/user/deployments/replica_count.txt"

EXPECTED_PRODUCTION_READY = [
    {"service": "auth-service", "version": "2.3.1", "replicas": 4},
    {"service": "notification-service", "version": "1.2.9", "replicas": 3},
    {"service": "analytics-service", "version": "2.0.0", "replicas": 2},
]

EXPECTED_REPLICA_COUNT = 9


# ── production_ready.json existence and readability ──────────────────────────

def test_production_ready_file_exists():
    assert os.path.isfile(PRODUCTION_READY_PATH), (
        f"{PRODUCTION_READY_PATH} does not exist. "
        "The file must be created as part of Step 1."
    )


def test_production_ready_file_is_readable():
    assert os.access(PRODUCTION_READY_PATH, os.R_OK), (
        f"{PRODUCTION_READY_PATH} exists but is not readable."
    )


# ── production_ready.json content ────────────────────────────────────────────

def test_production_ready_is_valid_json():
    with open(PRODUCTION_READY_PATH, "r") as f:
        content = f.read()
    try:
        json.loads(content)
    except json.JSONDecodeError as e:
        pytest.fail(
            f"{PRODUCTION_READY_PATH} is not valid JSON: {e}\n"
            f"File content:\n{content}"
        )


def test_production_ready_is_json_array():
    with open(PRODUCTION_READY_PATH, "r") as f:
        data = json.load(f)
    assert isinstance(data, list), (
        f"{PRODUCTION_READY_PATH} should contain a JSON array, "
        f"but got {type(data).__name__}."
    )


def test_production_ready_entry_count():
    with open(PRODUCTION_READY_PATH, "r") as f:
        data = json.load(f)
    assert len(data) == 3, (
        f"{PRODUCTION_READY_PATH} should contain exactly 3 entries "
        f"(auth-service, notification-service, analytics-service), "
        f"but found {len(data)}: {[e.get('service') for e in data]}"
    )


def test_production_ready_entry_order():
    with open(PRODUCTION_READY_PATH, "r") as f:
        data = json.load(f)
    actual_services = [e.get("service") for e in data]
    expected_services = [e["service"] for e in EXPECTED_PRODUCTION_READY]
    assert actual_services == expected_services, (
        f"Services in {PRODUCTION_READY_PATH} are in the wrong order or wrong set.\n"
        f"Expected: {expected_services}\n"
        f"Got:      {actual_services}"
    )


def test_production_ready_entries_have_exactly_three_fields():
    with open(PRODUCTION_READY_PATH, "r") as f:
        data = json.load(f)
    allowed_fields = {"service", "version", "replicas"}
    for entry in data:
        extra = set(entry.keys()) - allowed_fields
        missing = allowed_fields - set(entry.keys())
        assert not extra, (
            f"Entry for service '{entry.get('service', 'unknown')}' contains "
            f"unexpected extra fields: {extra}. "
            f"Only 'service', 'version', and 'replicas' are allowed."
        )
        assert not missing, (
            f"Entry for service '{entry.get('service', 'unknown')}' is missing "
            f"required fields: {missing}."
        )


def test_production_ready_auth_service():
    with open(PRODUCTION_READY_PATH, "r") as f:
        data = json.load(f)
    entry = next((e for e in data if e.get("service") == "auth-service"), None)
    assert entry is not None, (
        "auth-service is missing from production_ready.json. "
        "It has status='ready' and environment='production' in the manifest."
    )
    assert entry.get("version") == "2.3.1", (
        f"auth-service version should be '2.3.1', got '{entry.get('version')}'."
    )
    assert entry.get("replicas") == 4, (
        f"auth-service replicas should be 4, got {entry.get('replicas')}."
    )


def test_production_ready_notification_service():
    with open(PRODUCTION_READY_PATH, "r") as f:
        data = json.load(f)
    entry = next((e for e in data if e.get("service") == "notification-service"), None)
    assert entry is not None, (
        "notification-service is missing from production_ready.json. "
        "It has status='ready' and environment='production' in the manifest."
    )
    assert entry.get("version") == "1.2.9", (
        f"notification-service version should be '1.2.9', got '{entry.get('version')}'."
    )
    assert entry.get("replicas") == 3, (
        f"notification-service replicas should be 3, got {entry.get('replicas')}."
    )


def test_production_ready_analytics_service():
    with open(PRODUCTION_READY_PATH, "r") as f:
        data = json.load(f)
    entry = next((e for e in data if e.get("service") == "analytics-service"), None)
    assert entry is not None, (
        "analytics-service is missing from production_ready.json. "
        "It has status='ready' and environment='production' in the manifest."
    )
    assert entry.get("version") == "2.0.0", (
        f"analytics-service version should be '2.0.0', got '{entry.get('version')}'."
    )
    assert entry.get("replicas") == 2, (
        f"analytics-service replicas should be 2, got {entry.get('replicas')}."
    )


def test_production_ready_excludes_billing_service():
    with open(PRODUCTION_READY_PATH, "r") as f:
        data = json.load(f)
    services = [e.get("service") for e in data]
    assert "billing-service" not in services, (
        "billing-service should NOT be in production_ready.json because "
        "its environment is 'staging', not 'production'."
    )


def test_production_ready_excludes_user_service():
    with open(PRODUCTION_READY_PATH, "r") as f:
        data = json.load(f)
    services = [e.get("service") for e in data]
    assert "user-service" not in services, (
        "user-service should NOT be in production_ready.json because "
        "its status is 'pending', not 'ready'."
    )


def test_production_ready_excludes_search_service():
    with open(PRODUCTION_READY_PATH, "r") as f:
        data = json.load(f)
    services = [e.get("service") for e in data]
    assert "search-service" not in services, (
        "search-service should NOT be in production_ready.json because "
        "its status is 'failed', not 'ready'."
    )


def test_production_ready_full_content():
    """End-to-end check: the parsed array must exactly match the expected data."""
    with open(PRODUCTION_READY_PATH, "r") as f:
        data = json.load(f)
    assert data == EXPECTED_PRODUCTION_READY, (
        f"Content of {PRODUCTION_READY_PATH} does not match expected.\n"
        f"Expected: {json.dumps(EXPECTED_PRODUCTION_READY, indent=2)}\n"
        f"Got:      {json.dumps(data, indent=2)}"
    )


def test_production_ready_pretty_printed():
    """The file must be pretty-printed with 2-space indentation (jq default)."""
    with open(PRODUCTION_READY_PATH, "r") as f:
        raw = f.read()
    # Re-serialise with 2-space indent and compare
    data = json.loads(raw)
    expected_text = json.dumps(data, indent=2)
    # Normalise trailing newline for comparison
    assert raw.rstrip("\n") == expected_text.rstrip("\n"), (
        f"{PRODUCTION_READY_PATH} is not pretty-printed with 2-space indentation.\n"
        f"Expected format:\n{expected_text}\n"
        f"Actual content:\n{raw}"
    )


# ── replica_count.txt existence and readability ───────────────────────────────

def test_replica_count_file_exists():
    assert os.path.isfile(REPLICA_COUNT_PATH), (
        f"{REPLICA_COUNT_PATH} does not exist. "
        "The file must be created as part of Step 2."
    )


def test_replica_count_file_is_readable():
    assert os.access(REPLICA_COUNT_PATH, os.R_OK), (
        f"{REPLICA_COUNT_PATH} exists but is not readable."
    )


# ── replica_count.txt content ─────────────────────────────────────────────────

def test_replica_count_single_line():
    with open(REPLICA_COUNT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 1, (
        f"{REPLICA_COUNT_PATH} should contain exactly one line, "
        f"but found {len(lines)} lines.\nContent: {repr(content)}"
    )


def test_replica_count_is_integer():
    with open(REPLICA_COUNT_PATH, "r") as f:
        content = f.read().strip()
    try:
        int(content)
    except ValueError:
        pytest.fail(
            f"{REPLICA_COUNT_PATH} does not contain a plain integer. "
            f"Content: {repr(content)}"
        )


def test_replica_count_correct_value():
    with open(REPLICA_COUNT_PATH, "r") as f:
        content = f.read().strip()
    try:
        value = int(content)
    except ValueError:
        pytest.fail(
            f"{REPLICA_COUNT_PATH} does not contain a plain integer. "
            f"Content: {repr(content)}"
        )
    assert value == EXPECTED_REPLICA_COUNT, (
        f"Replica count in {REPLICA_COUNT_PATH} is wrong.\n"
        f"Expected: {EXPECTED_REPLICA_COUNT} "
        f"(auth-service(4) + notification-service(3) + analytics-service(2))\n"
        f"Got: {value}"
    )


def test_replica_count_no_extra_whitespace():
    with open(REPLICA_COUNT_PATH, "r") as f:
        content = f.read()
    # Allow exactly one trailing newline; no leading/trailing spaces on the line
    stripped = content.rstrip("\n")
    assert stripped == str(EXPECTED_REPLICA_COUNT), (
        f"{REPLICA_COUNT_PATH} must contain only the integer {EXPECTED_REPLICA_COUNT} "
        f"followed by a newline, with no extra spaces or text.\n"
        f"Actual content: {repr(content)}"
    )


# ── manifest.json must remain unchanged ──────────────────────────────────────

def test_manifest_still_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"The original manifest file {MANIFEST_PATH} has been removed or moved. "
        "It must not be modified or deleted."
    )


def test_manifest_unchanged():
    with open(MANIFEST_PATH, "r") as f:
        data = json.load(f)
    assert len(data) == 6, (
        f"manifest.json should still have 6 entries but now has {len(data)}. "
        "The manifest must not be modified."
    )
    service_names = [e["service"] for e in data]
    expected = [
        "auth-service", "billing-service", "user-service",
        "notification-service", "search-service", "analytics-service",
    ]
    assert service_names == expected, (
        f"manifest.json service order/names have changed.\n"
        f"Expected: {expected}\nGot: {service_names}"
    )
    # Spot-check a few fields to confirm no data was altered
    auth = next(e for e in data if e["service"] == "auth-service")
    assert auth["status"] == "ready" and auth["environment"] == "production", (
        "auth-service entry in manifest.json has been unexpectedly modified."
    )