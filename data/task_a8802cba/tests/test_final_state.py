# test_final_state.py

import os
import pytest

HOME = "/home/user"
YAML_PATH = os.path.join(HOME, "deploy_settings.yaml")
TOML_PATH = os.path.join(HOME, "deploy_settings.toml")
LOG_PATH = os.path.join(HOME, "config_update.log")

YAML_EXPECTED = """env_variables:
  - name: APP_ENVIRONMENT
    value: production
  - name: DB_HOST
    value: db.example.local
"""

TOML_EXPECTED = """[[env_variables]]
name = "APP_ENVIRONMENT"
value = "production"

[[env_variables]]
name = "DB_HOST"
value = "db.example.local"
"""

LOG_EXPECTED = """YAML APP_ENVIRONMENT: production
TOML APP_ENVIRONMENT: production
"""

@pytest.mark.describe("Final OS/FS state after student modification")
class TestFinalState:
    def test_yaml_file_exists(self):
        assert os.path.isfile(YAML_PATH), (
            f"Missing required file: {YAML_PATH}"
        )

    def test_toml_file_exists(self):
        assert os.path.isfile(TOML_PATH), (
            f"Missing required file: {TOML_PATH}"
        )

    def test_log_file_exists(self):
        assert os.path.isfile(LOG_PATH), (
            f"Missing required log file: {LOG_PATH}"
        )

    def test_yaml_file_content(self):
        with open(YAML_PATH, encoding="utf-8") as f:
            content = f.read()
        # Normalize line endings for comparison
        content_stripped = content.strip().replace('\r\n', '\n')
        expected_stripped = YAML_EXPECTED.strip().replace('\r\n', '\n')
        assert content_stripped == expected_stripped, (
            f"{YAML_PATH} does not match expected final content.\n"
            f"--- Expected ---\n{YAML_EXPECTED}\n--- Found ---\n{content}\n"
            "Check that only the APP_ENVIRONMENT value is changed to 'production',"
            " and the rest of the YAML file (including indentation and order) is unaltered."
        )

    def test_toml_file_content(self):
        with open(TOML_PATH, encoding="utf-8") as f:
            content = f.read()
        # Normalize line endings for comparison
        content_stripped = content.strip().replace('\r\n', '\n')
        expected_stripped = TOML_EXPECTED.strip().replace('\r\n', '\n')
        assert content_stripped == expected_stripped, (
            f"{TOML_PATH} does not match expected final content.\n"
            f"--- Expected ---\n{TOML_EXPECTED}\n--- Found ---\n{content}\n"
            "Check that only the APP_ENVIRONMENT value is changed to 'production',"
            " and the rest of the TOML file (including blank lines and order) is unaltered."
        )

    def test_yaml_app_environment_only_changed(self):
        # Ensure only APP_ENVIRONMENT value is changed, other values untouched
        with open(YAML_PATH, encoding="utf-8") as f:
            lines = [line.rstrip('\r\n') for line in f]
        found_app_env = False
        found_db_host = False
        for idx, line in enumerate(lines):
            if line.strip() == "- name: APP_ENVIRONMENT":
                found_app_env = True
                # Next line must be value: production
                if idx+1 >= len(lines) or lines[idx+1].strip() != "value: production":
                    pytest.fail(
                        f"{YAML_PATH}: APP_ENVIRONMENT value not set to 'production' directly after its name."
                    )
            if line.strip() == "- name: DB_HOST":
                found_db_host = True
                if idx+1 >= len(lines) or lines[idx+1].strip() != "value: db.example.local":
                    pytest.fail(
                        f"{YAML_PATH}: DB_HOST value has been changed or misplaced. It must remain 'db.example.local'."
                    )
        assert found_app_env, f"{YAML_PATH}: Could not find APP_ENVIRONMENT entry."
        assert found_db_host, f"{YAML_PATH}: Could not find DB_HOST entry."

    def test_toml_app_environment_only_changed(self):
        # Ensure only APP_ENVIRONMENT value is changed, other values untouched
        with open(TOML_PATH, encoding="utf-8") as f:
            lines = [line.rstrip('\r\n') for line in f]
        env_blocks = []
        block = []
        for line in lines:
            if line.strip() == "[[env_variables]]":
                if block:
                    env_blocks.append(block)
                block = [line]
            else:
                if block:
                    block.append(line)
        if block:
            env_blocks.append(block)
        found_app_env = False
        found_db_host = False
        for blk in env_blocks:
            blk_str = "\n".join(blk)
            if any('name = "APP_ENVIRONMENT"' in l for l in blk):
                found_app_env = True
                # Check value line
                value_lines = [l for l in blk if l.strip().startswith('value =')]
                assert len(value_lines) == 1, (
                    f"{TOML_PATH}: APP_ENVIRONMENT block should have exactly one value line.\nBlock:\n{blk_str}"
                )
                assert value_lines[0].strip() == 'value = "production"', (
                    f"{TOML_PATH}: APP_ENVIRONMENT value must be 'production', found: {value_lines[0]}"
                )
            if any('name = "DB_HOST"' in l for l in blk):
                found_db_host = True
                value_lines = [l for l in blk if l.strip().startswith('value =')]
                assert len(value_lines) == 1, (
                    f"{TOML_PATH}: DB_HOST block should have exactly one value line.\nBlock:\n{blk_str}"
                )
                assert value_lines[0].strip() == 'value = "db.example.local"', (
                    f"{TOML_PATH}: DB_HOST value must remain 'db.example.local', found: {value_lines[0]}"
                )
        assert found_app_env, f"{TOML_PATH}: Could not find APP_ENVIRONMENT block."
        assert found_db_host, f"{TOML_PATH}: Could not find DB_HOST block."

    def test_log_file_content_exact(self):
        with open(LOG_PATH, encoding="utf-8") as f:
            content = f.read()
        # Normalize line endings for comparison
        content_stripped = content.strip().replace('\r\n', '\n')
        expected_stripped = LOG_EXPECTED.strip().replace('\r\n', '\n')
        assert content_stripped == expected_stripped, (
            f"{LOG_PATH} does not match the exact required content.\n"
            f"--- Expected ---\n{LOG_EXPECTED}\n--- Found ---\n{content}\n"
            "Ensure the log output matches the required format, wording, and spacing exactly."
        )