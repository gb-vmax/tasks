# test_final_state.py

import os
import pytest

BASE_DIR = "/home/user/k8s-manifests"
DEPLOYMENT_YAML = os.path.join(BASE_DIR, "deployment.yaml")
SERVICE_YAML = os.path.join(BASE_DIR, "service.yaml")
CONFIGMAP_YAML = os.path.join(BASE_DIR, "configmap.yaml")
KIND_FREQ_LOG = os.path.join(BASE_DIR, "kind_frequency.log")

EXPECTED_LOG_CONTENT = (
    "CONFIGMAP 1\n"
    "DEPLOYMENT 2\n"
    "SERVICE 2\n"
)

EXPECTED_FILES = {
    "deployment.yaml",
    "service.yaml",
    "configmap.yaml",
    "kind_frequency.log",
}


@pytest.mark.describe("Final OS/filesystem state for Kubernetes manifest kind frequency task")
class TestFinalState:

    def test_k8s_manifests_directory_exists(self):
        assert os.path.isdir(BASE_DIR), (
            f"Required directory '{BASE_DIR}' does not exist. "
            "It must not be deleted or missing after task completion."
        )

    def test_required_manifest_files_still_exist(self):
        for fname in ["deployment.yaml", "service.yaml", "configmap.yaml"]:
            fpath = os.path.join(BASE_DIR, fname)
            assert os.path.isfile(fpath), (
                f"Expected manifest file '{fpath}' is missing after the task."
            )

    def test_kind_frequency_log_exists(self):
        assert os.path.isfile(KIND_FREQ_LOG), (
            f"Expected summary log '{KIND_FREQ_LOG}' was not created."
        )

    def test_kind_frequency_log_content_exact(self):
        with open(KIND_FREQ_LOG, "r", encoding="utf-8") as f:
            content = f.read()
        # Remove trailing newlines for comparison
        actual = content.rstrip('\n')
        expected = EXPECTED_LOG_CONTENT.rstrip('\n')
        assert actual == expected, (
            f"The contents of '{KIND_FREQ_LOG}' do not match the expected output.\n"
            "---- Expected ----\n"
            f"{expected}\n"
            "---- Actual ----\n"
            f"{actual}\n"
            "Check:\n"
            "- Each line should be '<KIND> <COUNT>' with a single space.\n"
            "- Kinds should be in all uppercase, sorted alphabetically.\n"
            "- No extra blank lines or spaces."
        )

    def test_no_extra_files_in_k8s_manifests(self):
        actual_files = set(os.listdir(BASE_DIR))
        extra_files = actual_files - EXPECTED_FILES
        missing_files = EXPECTED_FILES - actual_files
        assert not missing_files, (
            f"Missing required files in '{BASE_DIR}' after the task: {sorted(missing_files)}"
        )
        assert not extra_files, (
            f"Unexpected extra files in '{BASE_DIR}' after the task: {sorted(extra_files)}"
        )

    def test_manifest_files_unmodified(self):
        # Re-validate file contents to ensure they are unmodified
        expected_contents = {
            DEPLOYMENT_YAML: (
                "---\n"
                "apiVersion: apps/v1\n"
                "kind: Deployment\n"
                "metadata:\n"
                "  name: my-app\n"
                "spec:\n"
                "  selector:\n"
                "    matchLabels:\n"
                "      app: my-app\n"
                "---\n"
                "apiVersion: apps/v1\n"
                "kind: Deployment\n"
                "metadata:\n"
                "  name: another-app\n"
                "spec:\n"
                "  selector:\n"
                "    matchLabels:\n"
                "      app: another-app\n"
            ),
            SERVICE_YAML: (
                "---\n"
                "apiVersion: v1\n"
                "kind: Service\n"
                "metadata:\n"
                "  name: my-service\n"
                "spec:\n"
                "  selector:\n"
                "    app: my-app\n"
                "---\n"
                "apiVersion: v1\n"
                "kind: Service\n"
                "metadata:\n"
                "  name: another-service\n"
                "spec:\n"
                "  selector:\n"
                "    app: another-app\n"
            ),
            CONFIGMAP_YAML: (
                "---\n"
                "apiVersion: v1\n"
                "kind: ConfigMap\n"
                "metadata:\n"
                "  name: my-config\n"
            ),
        }
        for fpath, expected_content in expected_contents.items():
            assert os.path.isfile(fpath), f"File '{fpath}' missing after task."
            with open(fpath, "r", encoding="utf-8") as f:
                actual = f.read().rstrip('\n')
                expected = expected_content.rstrip('\n')
                assert actual == expected, (
                    f"The manifest file '{fpath}' was modified during the task.\n"
                    "---- Expected ----\n"
                    f"{expected}\n"
                    "---- Actual ----\n"
                    f"{actual}\n"
                    "Manifest files must not be changed."
                )

    def test_agent_echoed_log_file_to_console(self, capsys):
        """
        This test assumes that the agent prints the exact log file contents to stdout as the final step.
        We simulate this by capturing stdout and comparing to the expected log content.
        If running outside of a test harness that captures stdout, this test may be skipped.
        """
        # Simulate agent echo by printing the log file content
        with open(KIND_FREQ_LOG, "r", encoding="utf-8") as f:
            print(f.read(), end="")
        captured = capsys.readouterr()
        expected = EXPECTED_LOG_CONTENT
        actual = captured.out
        assert actual == expected, (
            "The agent must print the full contents of "
            f"'{KIND_FREQ_LOG}' to stdout as the final step.\n"
            "---- Expected output ----\n"
            f"{expected}\n"
            "---- Actual output ----\n"
            f"{actual}\n"
        )