# test_final_state.py

import os
import pytest

WORKFLOWS_DIR = "/home/user/workflows"
YAML_FILE = os.path.join(WORKFLOWS_DIR, "base_workflow.yaml")
TOML_FILE = os.path.join(WORKFLOWS_DIR, "advanced_workflow.toml")
VERIFICATION_LOG = os.path.join(WORKFLOWS_DIR, "verification.log")

EXPECTED_YAML = (
    "jobs:\n"
    "  test:\n"
    "    runs-on: ubuntu-latest\n"
    "    steps:\n"
    "      - name: Run tests\n"
    "        run: echo \"Running tests\"\n"
    "  deploy:\n"
    "    runs-on: ubuntu-22.04\n"
    "    steps:\n"
    "      - name: Print deployment\n"
    "        run: echo \"Deploying application\"\n"
)

EXPECTED_TOML = (
    "[job.test]\n"
    "runs_on = \"ubuntu-latest\"\n"
    "[[job.test.steps]]\n"
    "name = \"Run tests\"\n"
    "run = \"echo 'Running tests'\"\n"
    "\n"
    "[job.deploy]\n"
    "runs_on = \"ubuntu-22.04\"\n"
    "[[job.deploy.steps]]\n"
    "name = \"Print deployment\"\n"
    "run = \"echo 'Deploying application'\"\n"
)

EXPECTED_LOG = "WORKFLOW CONFIGURATION: COMPLETE\n"

@pytest.mark.describe("Final OS and filesystem state after workflow configuration task")
class TestFinalState:
    def test_workflows_directory_exists(self):
        assert os.path.isdir(WORKFLOWS_DIR), (
            f"Required directory '{WORKFLOWS_DIR}' is missing. "
            "The workflows directory must exist at the end of the task."
        )

    def test_base_workflow_yaml_exists(self):
        assert os.path.isfile(YAML_FILE), (
            f"Required file '{YAML_FILE}' is missing. "
            "The YAML configuration file must exist after the task."
        )

    def test_advanced_workflow_toml_exists(self):
        assert os.path.isfile(TOML_FILE), (
            f"Required file '{TOML_FILE}' is missing. "
            "The TOML configuration file must exist after the task."
        )

    def test_verification_log_exists(self):
        assert os.path.isfile(VERIFICATION_LOG), (
            f"Verification log '{VERIFICATION_LOG}' is missing. "
            "You must create this file at the end of the task."
        )

    def test_base_workflow_yaml_content_exact(self):
        try:
            with open(YAML_FILE, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            pytest.fail(f"Could not read '{YAML_FILE}': {e}")
        if content != EXPECTED_YAML:
            pytest.fail(
                f"Content of '{YAML_FILE}' does not match the required final state.\n"
                "---- Expected ----\n"
                f"{EXPECTED_YAML}"
                "---- Found ----\n"
                f"{content}"
                "Please ensure the YAML file is formatted exactly as shown, "
                "including indentation (2 spaces), list syntax, and order."
            )

    def test_advanced_workflow_toml_content_exact(self):
        try:
            with open(TOML_FILE, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            pytest.fail(f"Could not read '{TOML_FILE}': {e}")
        if content != EXPECTED_TOML:
            pytest.fail(
                f"Content of '{TOML_FILE}' does not match the required final state.\n"
                "---- Expected ----\n"
                f"{EXPECTED_TOML}"
                "---- Found ----\n"
                f"{content}"
                "Please ensure the TOML file is formatted exactly as shown, "
                "including section/table syntax, spacing, and order."
            )

    def test_verification_log_content_exact(self):
        try:
            with open(VERIFICATION_LOG, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            pytest.fail(f"Could not read '{VERIFICATION_LOG}': {e}")
        if content != EXPECTED_LOG:
            pytest.fail(
                f"Content of '{VERIFICATION_LOG}' is incorrect.\n"
                f"---- Expected ----\n{EXPECTED_LOG}---- Found ----\n{content}"
                "The log must contain exactly 'WORKFLOW CONFIGURATION: COMPLETE' (all uppercase), "
                "with no extra lines or spaces."
            )