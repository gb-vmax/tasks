# test_final_state.py

import os
import json
import pytest

POLICY_REPORT_PATH = "/home/user/output/policy_report.json"

EXPECTED_POLICY_REPORT = [
    {
        "container_name": "devops-tool",
        "image_source": "docker.io/library/devops-tool:latest",
        "compliance": "FAIL"
    },
    {
        "container_name": "testservice",
        "image_source": "quay.io/example/testservice:1.1",
        "compliance": "FAIL"
    }
]

@pytest.mark.describe("Final OS/Filesystem State - DevSecOps container policy compliance report")
def test_policy_report_json_exists():
    """The policy_report.json file must exist at the expected location."""
    assert os.path.isfile(POLICY_REPORT_PATH), (
        f"Expected policy compliance report file at {POLICY_REPORT_PATH}, but it does not exist."
    )

@pytest.mark.describe("Final OS/Filesystem State - DevSecOps container policy compliance report")
def test_policy_report_json_valid_and_exact_contents():
    """
    The policy_report.json file must:
    - Be valid JSON
    - Contain only non-compliant containers
    - Match the expected array, order, and field values exactly
    """
    # Check file exists
    assert os.path.isfile(POLICY_REPORT_PATH), (
        f"Expected policy compliance report file at {POLICY_REPORT_PATH}, but it does not exist."
    )

    # Read and parse the JSON file
    try:
        with open(POLICY_REPORT_PATH, "r", encoding="utf-8") as f:
            report_data = json.load(f)
    except Exception as e:
        pytest.fail(
            f"The file {POLICY_REPORT_PATH} could not be parsed as valid JSON: {e}"
        )

    # Ensure it's a list
    assert isinstance(report_data, list), (
        f"The file {POLICY_REPORT_PATH} must be a JSON array, but got {type(report_data).__name__}."
    )

    # Check that the report matches exactly the expected report, including order
    assert report_data == EXPECTED_POLICY_REPORT, (
        f"The policy report does not match the expected non-compliant containers.\n"
        f"Expected:\n{json.dumps(EXPECTED_POLICY_REPORT, indent=2)}\n"
        f"Found:\n{json.dumps(report_data, indent=2)}"
    )

    # Additional structure/field checks (robustness)
    for idx, entry in enumerate(report_data):
        # Each entry must be a dict with the required keys
        assert isinstance(entry, dict), (
            f"Entry {idx} in the report is not an object/dict: {entry}"
        )
        for field in ("container_name", "image_source", "compliance"):
            assert field in entry, (
                f"Entry {idx} is missing required field '{field}'. Entry: {entry}"
            )
        # Compliance value must be "FAIL"
        assert entry["compliance"] == "FAIL", (
            f"Entry {idx} has compliance value '{entry['compliance']}', expected 'FAIL'."
        )

@pytest.mark.describe("Final OS/Filesystem State - DevSecOps container policy compliance report")
def test_policy_report_json_does_not_include_compliant():
    """
    The policy_report.json file must not include compliant containers.
    """
    with open(POLICY_REPORT_PATH, "r", encoding="utf-8") as f:
        report_data = json.load(f)
    compliant_names = {"frontend", "backend"}
    reported_names = {entry["container_name"] for entry in report_data}
    intersection = compliant_names & reported_names
    assert not intersection, (
        f"The report at {POLICY_REPORT_PATH} incorrectly includes compliant containers: {', '.join(intersection)}"
    )