# test_final_state.py

import os
import pytest

HOME = "/home/user"
OPERATOR_DIR = os.path.join(HOME, "old-operator")
DEPLOYMENT_YAML = os.path.join(OPERATOR_DIR, "deployment.yaml")
SERVICE_YAML = os.path.join(OPERATOR_DIR, "service.yaml")
VALIDATION_REPORT = os.path.join(OPERATOR_DIR, "validation_report.txt")
APPLY_DRYRUN_LOG = os.path.join(OPERATOR_DIR, "apply_dryrun.log")

# Expected contents after the task is completed
DEPLOYMENT_YAML_EXPECTED = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: old-app-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: old-app
  template:
    metadata:
      labels:
        app: old-app
    spec:
      containers:
      - name: old-app-container
        image: old-app-image:v1.2.3
        ports:
        - containerPort: 80
"""

SERVICE_YAML_EXPECTED = """apiVersion: v1
kind: Service
metadata:
  name: old-app-service
spec:
  selector:
    app: old-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: ClusterIP
"""

VALIDATION_REPORT_EXPECTED = """Validation Report for Kubernetes Manifests

deployment.yaml: OK
service.yaml: OK
"""

APPLY_DRYRUN_LOG_EXPECTED = """deployment.apps/old-app-deployment configured (dry run)
service/old-app-service configured (dry run)
"""

@pytest.mark.describe("Final filesystem state for old-operator troubleshooting workflow")
class TestFinalState:
    def test_operator_directory_exists(self):
        assert os.path.isdir(OPERATOR_DIR), (
            f"Directory missing: {OPERATOR_DIR}\n"
            f"Expected an 'old-operator' directory in {HOME}."
        )

    def test_deployment_yaml_exists_and_content(self):
        assert os.path.isfile(DEPLOYMENT_YAML), (
            f"File missing: {DEPLOYMENT_YAML}\n"
            "Expected deployment.yaml to be present after completing the task."
        )
        with open(DEPLOYMENT_YAML, "r") as f:
            content = f.read()
        expected_lines = DEPLOYMENT_YAML_EXPECTED.strip().splitlines()
        actual_lines = content.strip().splitlines()
        assert actual_lines == expected_lines, (
            f"File {DEPLOYMENT_YAML} content does not match the expected final deployment.yaml.\n"
            "Did you forget to update the 'replicas' field to 2?\n"
            "Expected:\n"
            + "\n".join(expected_lines)
            + "\nActual:\n"
            + "\n".join(actual_lines)
        )

    def test_service_yaml_exists_and_content(self):
        assert os.path.isfile(SERVICE_YAML), (
            f"File missing: {SERVICE_YAML}\n"
            "Expected service.yaml to be present after completing the task."
        )
        with open(SERVICE_YAML, "r") as f:
            content = f.read()
        expected_lines = SERVICE_YAML_EXPECTED.strip().splitlines()
        actual_lines = content.strip().splitlines()
        assert actual_lines == expected_lines, (
            f"File {SERVICE_YAML} content does not match the expected final service.yaml.\n"
            "service.yaml should be unchanged.\n"
            "Expected:\n"
            + "\n".join(expected_lines)
            + "\nActual:\n"
            + "\n".join(actual_lines)
        )

    def test_validation_report_exists_and_content(self):
        assert os.path.isfile(VALIDATION_REPORT), (
            f"File missing: {VALIDATION_REPORT}\n"
            "Expected validation_report.txt to be created as part of the troubleshooting workflow."
        )
        with open(VALIDATION_REPORT, "r") as f:
            content = f.read()
        expected_lines = VALIDATION_REPORT_EXPECTED.strip().splitlines()
        actual_lines = content.strip().splitlines()
        assert actual_lines == expected_lines, (
            f"File {VALIDATION_REPORT} content does not match expected validation report.\n"
            "Did you validate both YAML files successfully and write 'OK' for both?\n"
            "Expected:\n"
            + "\n".join(expected_lines)
            + "\nActual:\n"
            + "\n".join(actual_lines)
        )

    def test_apply_dryrun_log_exists_and_content(self):
        assert os.path.isfile(APPLY_DRYRUN_LOG), (
            f"File missing: {APPLY_DRYRUN_LOG}\n"
            "Expected apply_dryrun.log to be created as part of the troubleshooting workflow."
        )
        with open(APPLY_DRYRUN_LOG, "r") as f:
            content = f.read()
        expected_lines = APPLY_DRYRUN_LOG_EXPECTED.strip().splitlines()
        actual_lines = content.strip().splitlines()
        assert actual_lines == expected_lines, (
            f"File {APPLY_DRYRUN_LOG} content does not match expected dry-run apply log.\n"
            "Did you extract the correct deployment and service names from the manifests?\n"
            "Expected:\n"
            + "\n".join(expected_lines)
            + "\nActual:\n"
            + "\n".join(actual_lines)
        )