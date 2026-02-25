# test_final_state.py

"""
Pytest suite to validate the final state of /home/user/k8s_manifests
after summarizing Kubernetes Deployment manifests into a CSV file.

This test checks that:
- /home/user/k8s_manifests/deployment_summary.csv exists
- The CSV contents strictly match the expected output, including header, order, and newlines
- The CSV rows are in the order: frontend, backend, database
- The CSV columns are: deployment,replicas,container_image
- Each row matches the corresponding data from the YAML manifests
"""

import os
import pytest

K8S_DIR = "/home/user/k8s_manifests"
DEPLOYMENT_SUMMARY_CSV = os.path.join(K8S_DIR, "deployment_summary.csv")

EXPECTED_CSV = (
    "deployment,replicas,container_image\n"
    "frontend,3,nginx:1.19\n"
    "backend,2,python:3.9\n"
    "database,1,mongo:4.4\n"
)

@pytest.mark.describe("Final state: deployment_summary.csv is correct and present")
class TestDeploymentSummaryCSVFinalState:
    def test_deployment_summary_csv_exists(self):
        assert os.path.isfile(DEPLOYMENT_SUMMARY_CSV), (
            f"Expected file {DEPLOYMENT_SUMMARY_CSV} does not exist. "
            "You must create the deployment_summary.csv in the specified directory."
        )

    def test_deployment_summary_csv_contents_exact(self):
        with open(DEPLOYMENT_SUMMARY_CSV, "r", encoding="utf-8") as f:
            content = f.read()
        # Normalize line endings for robust comparison
        normalized_content = content.replace('\r\n', '\n')
        normalized_expected = EXPECTED_CSV.replace('\r\n', '\n')
        assert normalized_content == normalized_expected, (
            f"The contents of {DEPLOYMENT_SUMMARY_CSV} do not match the expected CSV output exactly.\n"
            "Expected:\n"
            f"{EXPECTED_CSV!r}\n"
            "Got:\n"
            f"{content!r}\n"
            "Check that:\n"
            "- The header row is present and matches exactly\n"
            "- Each deployment row is present and in the correct order (frontend, backend, database)\n"
            "- The correct number of replicas and container images are used\n"
            "- Each line is terminated with a newline character\n"
            "- There are no extra or missing rows or columns"
        )

    def test_deployment_summary_csv_no_extra_bytes(self):
        """Ensure there are no extra trailing spaces or blank lines."""
        with open(DEPLOYMENT_SUMMARY_CSV, "rb") as f:
            raw = f.read()
        # Check for double newlines at the end or trailing spaces
        assert not raw.endswith(b"\n\n"), (
            f"{DEPLOYMENT_SUMMARY_CSV} has extra blank lines at the end. "
            "There should be exactly one newline after the last record."
        )
        assert b" " not in [line[-2:] for line in raw.splitlines() if line], (
            f"{DEPLOYMENT_SUMMARY_CSV} has trailing spaces at the end of a line. "
            "Each line should not have trailing whitespace."
        )

    def test_deployment_summary_csv_column_headers(self):
        """Ensure the column headers are correct and in the right order."""
        with open(DEPLOYMENT_SUMMARY_CSV, "r", encoding="utf-8") as f:
            header = f.readline().strip()
        assert header == "deployment,replicas,container_image", (
            f"The CSV header is incorrect. Got: {header!r} "
            "Expected: 'deployment,replicas,container_image'."
        )

    def test_deployment_summary_csv_row_order(self):
        """Ensure the deployments are listed in the correct order."""
        with open(DEPLOYMENT_SUMMARY_CSV, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
        expected_rows = [
            "deployment,replicas,container_image",
            "frontend,3,nginx:1.19",
            "backend,2,python:3.9",
            "database,1,mongo:4.4"
        ]
        assert lines == expected_rows, (
            f"The CSV rows are not in the correct order or do not strictly match the expected rows.\n"
            f"Expected rows:\n{expected_rows}\nGot:\n{lines}"
        )