# test_final_state.py

import os
import pytest

HOME = "/home/user"
RELEASES_DIR = os.path.join(HOME, "releases")
CSV_PATH = os.path.join(RELEASES_DIR, "service_list.csv")
DEPLOYMENTS_DIR = os.path.join(RELEASES_DIR, "deployments")
LOG_PATH = os.path.join(RELEASES_DIR, "deployment_manifest.log")

# Truth data for final YAMLs and log file (with exact indentation and line endings).
YAML_EXPECTED = {
    "auth-service-deploy.yaml": (
        "service:\n"
        "  name: auth-service\n"
        "  deploy_version: 1.5.0\n"
        "  maintainer: alice\n"
        "  changelog: |\n"
        "    Upgraded from 1.4.2 to 1.5.0 in this release.\n"
    ),
    "billing-service-deploy.yaml": (
        "service:\n"
        "  name: billing-service\n"
        "  deploy_version: 3.0.0\n"
        "  maintainer: bob\n"
        "  changelog: |\n"
        "    Upgraded from 2.9.0 to 3.0.0 in this release.\n"
    ),
    "inventory-service-deploy.yaml": (
        "service:\n"
        "  name: inventory-service\n"
        "  deploy_version: 0.6.0\n"
        "  maintainer: charlie\n"
        "  changelog: |\n"
        "    Upgraded from 0.5.6 to 0.6.0 in this release.\n"
    ),
}

EXPECTED_LOG_CONTENT = (
    "auth-service-deploy.yaml\n"
    "billing-service-deploy.yaml\n"
    "inventory-service-deploy.yaml\n"
)

@pytest.mark.describe("Final state: The deployments directory exists and contains exactly the expected YAML files with correct content.")
def test_deployment_manifests_exist_and_correct():
    # Check deployments directory exists
    assert os.path.isdir(DEPLOYMENTS_DIR), (
        f"Expected deployments directory at {DEPLOYMENTS_DIR}, but it does not exist."
    )
    files = sorted(os.listdir(DEPLOYMENTS_DIR))
    expected_files = sorted(YAML_EXPECTED.keys())
    assert files == expected_files, (
        f"Deployments directory {DEPLOYMENTS_DIR} does not contain the expected files.\n"
        f"Expected: {expected_files}\n"
        f"Found: {files}\n"
        "Ensure all required YAML manifest files are present and named exactly as required."
    )
    # Check content of each YAML file
    for fname, expected_content in YAML_EXPECTED.items():
        path = os.path.join(DEPLOYMENTS_DIR, fname)
        assert os.path.isfile(path), (
            f"Missing expected manifest file: {path}"
        )
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        # Normalize line endings for robust comparison
        actual = content.replace('\r\n', '\n').replace('\r', '\n')
        expected = expected_content.replace('\r\n', '\n').replace('\r', '\n')
        assert actual == expected, (
            f"Manifest file {path} does not match the expected content.\n"
            f"--- Expected ---\n{expected_content}\n"
            f"--- Found ---\n{content}\n"
            "Check indentation, keys, values, and changelog block formatting."
        )

@pytest.mark.describe("Final state: The deployment_manifest.log exists and lists all manifest files, sorted, one per line, no extra lines.")
def test_deployment_manifest_log_exists_and_correct():
    assert os.path.isfile(LOG_PATH), (
        f"Expected deployment manifest log at {LOG_PATH}, but it does not exist."
    )
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    # Normalize line endings for robust comparison
    actual = content.replace('\r\n', '\n').replace('\r', '\n')
    expected = EXPECTED_LOG_CONTENT.replace('\r\n', '\n').replace('\r', '\n')
    assert actual == expected, (
        f"The log file {LOG_PATH} does not match the expected content.\n"
        f"--- Expected ---\n{EXPECTED_LOG_CONTENT}\n"
        f"--- Found ---\n{content}\n"
        "Ensure the log lists all deployment YAML filenames, one per line, sorted in ascending order, with no extra spaces or lines."
    )

@pytest.mark.describe("Final state: No extra files exist in the deployments directory.")
def test_no_extra_files_in_deployments():
    files = sorted(os.listdir(DEPLOYMENTS_DIR))
    expected_files = sorted(YAML_EXPECTED.keys())
    extra = set(files) - set(expected_files)
    missing = set(expected_files) - set(files)
    assert not extra, (
        f"Extra unexpected files found in {DEPLOYMENTS_DIR}: {sorted(extra)}"
    )
    assert not missing, (
        f"Missing expected manifest files in {DEPLOYMENTS_DIR}: {sorted(missing)}"
    )

@pytest.mark.describe("Final state: The original CSV is still present and unchanged.")
def test_service_list_csv_still_exists_and_unchanged():
    assert os.path.isfile(CSV_PATH), (
        f"CSV file missing after deployment at {CSV_PATH}."
    )
    expected_csv = (
        "service_name,current_version,next_version,maintainer\n"
        "auth-service,1.4.2,1.5.0,alice\n"
        "billing-service,2.9.0,3.0.0,bob\n"
        "inventory-service,0.5.6,0.6.0,charlie\n"
    )
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    actual = content.replace('\r\n', '\n').replace('\r', '\n')
    expected = expected_csv.replace('\r\n', '\n').replace('\r', '\n')
    assert actual == expected, (
        f"CSV file at {CSV_PATH} has been modified unexpectedly after deployment.\n"
        f"--- Expected ---\n{expected_csv}\n"
        f"--- Found ---\n{content}\n"
    )