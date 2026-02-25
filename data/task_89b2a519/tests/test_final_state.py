# test_final_state.py

import os
import pytest

HOME = "/home/user"
PROJECT = os.path.join(HOME, "project")
CONFIG = os.path.join(PROJECT, "config")

APP_CONFIG_YAML = os.path.join(CONFIG, "app_config.yaml")
ENV_CONFIG_TOML = os.path.join(CONFIG, "env_config.toml")
INCIDENT_REPORT_LOG = os.path.join(PROJECT, "incident_report.log")

EXPECTED_APP_CONFIG_YAML = (
    "settings:\n"
    "  debug: false\n"
    "  version: \"1.2.3\"\n"
    "services:\n"
    "  - web\n"
    "  - auth\n"
    "  - logging\n"
    "  - notification\n"
)

EXPECTED_ENV_CONFIG_TOML = (
    "[server]\n"
    "HOST = \"0.0.0.0\"\n"
    "PORT = 9090\n"
    "\n"
    "[database]\n"
    "url = \"postgres://user:pass@localhost/db\"\n"
    "timeout = 30\n"
)

EXPECTED_INCIDENT_REPORT_LOG = (
    "app_config.yaml:\n"
    "- Set settings.debug to false\n"
    "- Added 'notification' to services list\n"
    "\n"
    "env_config.toml:\n"
    "- Set server.PORT to 9090\n"
    "- Added database.timeout = 30\n"
)

@pytest.mark.describe("Final OS/filesystem state after incident response config repair")
class TestFinalState:

    def test_app_config_yaml_exists(self):
        assert os.path.isfile(APP_CONFIG_YAML), (
            f"Expected YAML config file at {APP_CONFIG_YAML}, but it does not exist."
        )

    def test_env_config_toml_exists(self):
        assert os.path.isfile(ENV_CONFIG_TOML), (
            f"Expected TOML config file at {ENV_CONFIG_TOML}, but it does not exist."
        )

    def test_incident_report_log_exists(self):
        assert os.path.isfile(INCIDENT_REPORT_LOG), (
            f"Expected incident report log at {INCIDENT_REPORT_LOG}, but it does not exist."
        )

    def test_app_config_yaml_content_exact(self):
        with open(APP_CONFIG_YAML, encoding="utf-8") as f:
            content = f.read()
        # Compare with trailing newlines stripped for robustness
        expected = EXPECTED_APP_CONFIG_YAML.rstrip('\n')
        actual = content.rstrip('\n')
        assert actual == expected, (
            f"{APP_CONFIG_YAML} does not match the expected FINAL content.\n"
            "If you changed anything beyond the specified edits (formatting, whitespace, or structure), this will fail.\n"
            "Expected:\n"
            f"{EXPECTED_APP_CONFIG_YAML}\n"
            "Found:\n"
            f"{content}"
        )

    def test_env_config_toml_content_exact(self):
        with open(ENV_CONFIG_TOML, encoding="utf-8") as f:
            content = f.read()
        expected = EXPECTED_ENV_CONFIG_TOML.rstrip('\n')
        actual = content.rstrip('\n')
        assert actual == expected, (
            f"{ENV_CONFIG_TOML} does not match the expected FINAL content.\n"
            "If you changed anything beyond the specified edits (formatting, whitespace, or structure), this will fail.\n"
            "Expected:\n"
            f"{EXPECTED_ENV_CONFIG_TOML}\n"
            "Found:\n"
            f"{content}"
        )

    def test_incident_report_log_content_exact(self):
        with open(INCIDENT_REPORT_LOG, encoding="utf-8") as f:
            content = f.read()
        expected = EXPECTED_INCIDENT_REPORT_LOG.rstrip('\n')
        actual = content.rstrip('\n')
        assert actual == expected, (
            f"{INCIDENT_REPORT_LOG} does not match the required format and content.\n"
            "Expected:\n"
            f"{EXPECTED_INCIDENT_REPORT_LOG}\n"
            "Found:\n"
            f"{content}"
        )

    def test_app_config_yaml_no_extra_lines(self):
        """Ensure there are no extra lines/whitespace in the YAML config."""
        with open(APP_CONFIG_YAML, encoding="utf-8") as f:
            lines = f.readlines()
        expected_lines = EXPECTED_APP_CONFIG_YAML.splitlines(keepends=False)
        actual_lines = [line.rstrip('\r\n') for line in lines]
        assert actual_lines == expected_lines, (
            f"{APP_CONFIG_YAML} contains unexpected extra lines, whitespace, or formatting differences.\n"
            "Expected lines:\n"
            f"{expected_lines}\n"
            "Found lines:\n"
            f"{actual_lines}"
        )

    def test_env_config_toml_no_extra_lines(self):
        """Ensure there are no extra lines/whitespace in the TOML config."""
        with open(ENV_CONFIG_TOML, encoding="utf-8") as f:
            lines = f.readlines()
        expected_lines = EXPECTED_ENV_CONFIG_TOML.splitlines(keepends=False)
        actual_lines = [line.rstrip('\r\n') for line in lines]
        assert actual_lines == expected_lines, (
            f"{ENV_CONFIG_TOML} contains unexpected extra lines, whitespace, or formatting differences.\n"
            "Expected lines:\n"
            f"{expected_lines}\n"
            "Found lines:\n"
            f"{actual_lines}"
        )

    def test_incident_report_log_no_extra_lines(self):
        """Ensure the incident report log matches exactly, no extra whitespace or lines."""
        with open(INCIDENT_REPORT_LOG, encoding="utf-8") as f:
            lines = f.readlines()
        expected_lines = EXPECTED_INCIDENT_REPORT_LOG.splitlines(keepends=False)
        actual_lines = [line.rstrip('\r\n') for line in lines]
        assert actual_lines == expected_lines, (
            f"{INCIDENT_REPORT_LOG} contains unexpected extra lines, whitespace, or formatting differences.\n"
            "Expected lines:\n"
            f"{expected_lines}\n"
            "Found lines:\n"
            f"{actual_lines}"
        )