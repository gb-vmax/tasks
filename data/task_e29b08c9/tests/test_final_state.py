# test_final_state.py

import os
import json
import pytest

K8S_MANIFESTS_DIR = '/home/user/k8s-manifests'
DEPLOYMENTS_CSV = '/home/user/k8s-manifests/deployments.csv'
DEPLOYMENTS_JSON = '/home/user/k8s-manifests/deployments.json'
UPDATE_LOG = '/home/user/k8s-manifests/update.log'

EXPECTED_JSON = [
    {
        "name": "frontend",
        "namespace": "default",
        "image": "nginx:1.20",
        "replicas": "3"
    },
    {
        "name": "backend",
        "namespace": "prod",
        "image": "backend-app:2.1",
        "replicas": "5"
    },
    {
        "name": "analytics",
        "namespace": "default",
        "image": "my-analytics:0.4",
        "replicas": "1"
    }
]

EXPECTED_LOG_LINE = "Updated backend in prod: replicas set to 5\n"

@pytest.mark.describe("Post-task: Output files existence and exclusivity")
def test_only_expected_files_present():
    files = sorted(
        f for f in os.listdir(K8S_MANIFESTS_DIR)
        if not f.startswith('.')  # ignore hidden files
    )
    expected = ['deployments.csv', 'deployments.json', 'update.log']
    assert files == expected, (
        f"Expected only {expected} in {K8S_MANIFESTS_DIR}, but found: {files}. "
        f"Ensure only the required files exist after the task."
    )

@pytest.mark.describe("Post-task: deployments.json correctness")
def test_deployments_json_exists_and_is_valid_json():
    assert os.path.isfile(DEPLOYMENTS_JSON), (
        f"File {DEPLOYMENTS_JSON} does not exist after the task."
    )
    with open(DEPLOYMENTS_JSON, 'r', encoding='utf-8') as f:
        json_text = f.read()
    try:
        data = json.loads(json_text)
    except Exception as e:
        pytest.fail(
            f"{DEPLOYMENTS_JSON} is not valid JSON: {e}\n"
            f"Content:\n{json_text}"
        )

@pytest.mark.describe("Post-task: deployments.json has correct structure and contents")
def test_deployments_json_exact_content_and_order():
    with open(DEPLOYMENTS_JSON, 'r', encoding='utf-8') as f:
        json_text = f.read()
    try:
        data = json.loads(json_text)
    except Exception as e:
        pytest.skip("Already failed in previous test: not valid JSON.")

    # Check it's a list of dicts with correct length
    assert isinstance(data, list), (
        f"{DEPLOYMENTS_JSON} does not contain a JSON array."
    )
    assert len(data) == len(EXPECTED_JSON), (
        f"{DEPLOYMENTS_JSON} should contain {len(EXPECTED_JSON)} deployments, "
        f"but found {len(data)}."
    )

    # Check each object for exact keys, order, and string values
    for idx, (item, expected) in enumerate(zip(data, EXPECTED_JSON)):
        # Check keys and order using list(item.keys())
        item_keys = list(item.keys())
        expected_keys = list(expected.keys())
        assert item_keys == expected_keys, (
            f"Deployment at index {idx} in {DEPLOYMENTS_JSON} has keys {item_keys}, "
            f"but expected {expected_keys} (order matters!)."
        )
        # Check values and types
        for key in expected_keys:
            assert key in item, (
                f"Key '{key}' missing in deployment at index {idx}."
            )
            actual_val = item[key]
            expected_val = expected[key]
            assert isinstance(actual_val, str), (
                f"Value for '{key}' in deployment at index {idx} is not a string: {actual_val!r}"
            )
            assert actual_val == expected_val, (
                f"Value for '{key}' in deployment at index {idx} is {actual_val!r}, "
                f"expected {expected_val!r}."
            )

@pytest.mark.describe("Post-task: Only backend/prod replicas changed")
def test_only_backend_prod_replicas_changed():
    with open(DEPLOYMENTS_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        if item["name"] == "backend" and item["namespace"] == "prod":
            assert item["replicas"] == "5", (
                "The 'replicas' for backend in prod namespace must be '5'."
            )
        elif item["name"] == "frontend" and item["namespace"] == "default":
            assert item["replicas"] == "3", (
                "The 'replicas' for frontend in default namespace must remain '3'."
            )
        elif item["name"] == "analytics" and item["namespace"] == "default":
            assert item["replicas"] == "1", (
                "The 'replicas' for analytics in default namespace must remain '1'."
            )
        else:
            pytest.fail(
                f"Unexpected deployment object in {DEPLOYMENTS_JSON}: {item!r}"
            )

@pytest.mark.describe("Post-task: deployments.json formatting")
def test_deployments_json_no_trailing_commas_and_strict_json():
    with open(DEPLOYMENTS_JSON, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Check for trailing commas in array or object
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        if stripped.endswith(','):
            # Only allow commas between items, not after the last
            if i < len(lines) - 2 and lines[i+1].strip().startswith('{'):
                continue  # comma between objects
            pytest.fail(
                f"Trailing comma detected in {DEPLOYMENTS_JSON} at line {i+1}: {stripped!r}"
            )
    # Check for comments (shouldn't be any)
    for i, line in enumerate(lines):
        if '//' in line or '#' in line:
            pytest.fail(
                f"Comment detected in {DEPLOYMENTS_JSON} at line {i+1}: {line!r}"
            )

@pytest.mark.describe("Post-task: update.log correctness")
def test_update_log_exists_and_content():
    assert os.path.isfile(UPDATE_LOG), (
        f"File {UPDATE_LOG} does not exist after the task."
    )
    with open(UPDATE_LOG, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == EXPECTED_LOG_LINE, (
        f"{UPDATE_LOG} should contain exactly:\n{EXPECTED_LOG_LINE!r}\n"
        f"but got:\n{content!r}\n"
        f"Ensure the update log is correct and contains only one line."
    )