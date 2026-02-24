# test_final_state.py

import os
import pytest

RELEASE_CONFIGS_DIR = "/home/user/release_configs"
APP_YAML = os.path.join(RELEASE_CONFIGS_DIR, "app.yaml")
DATABASE_TOML = os.path.join(RELEASE_CONFIGS_DIR, "database.toml")
CONFIG_UPDATE_LOG = os.path.join(RELEASE_CONFIGS_DIR, "config_update.log")

EXPECTED_APP_YAML = (
    "release: 2.1.0\n"
    "changelog:\n"
    "  - Added feature X\n"
    "  - Fixed bug Y\n"
    "config:\n"
    "  debug: false\n"
    "  port: 8080\n"
)

EXPECTED_DATABASE_TOML = (
    "[connection]\n"
    "host = \"db.internal\"\n"
    "port = 5432\n"
    "max_active = 40\n"
)

EXPECTED_CONFIG_UPDATE_LOG_LINES = [
    "Updated app.yaml release version to 2.1.0",
    "Added changelog to app.yaml",
    "Set database.toml connection.max_active to 40",
]


def test_release_configs_directory_exists_and_is_dir():
    assert os.path.exists(RELEASE_CONFIGS_DIR), (
        f"Missing directory: {RELEASE_CONFIGS_DIR}"
    )
    assert os.path.isdir(RELEASE_CONFIGS_DIR), (
        f"{RELEASE_CONFIGS_DIR} exists but is not a directory"
    )


def test_app_yaml_exists_and_content_exact():
    assert os.path.exists(APP_YAML), (
        f"Missing file: {APP_YAML}"
    )
    assert os.path.isfile(APP_YAML), (
        f"{APP_YAML} exists but is not a file"
    )

    with open(APP_YAML, "r") as f:
        content = f.read()

    # Check for exact match (including order and indentation)
    if content != EXPECTED_APP_YAML:
        # Find where the difference is for better error reporting
        from difflib import unified_diff
        diff = "\n".join(unified_diff(
            EXPECTED_APP_YAML.splitlines(),
            content.splitlines(),
            fromfile="expected",
            tofile="found",
            lineterm=""
        ))
        pytest.fail(
            f"{APP_YAML} content does not match expected final state.\n"
            f"Diff:\n{diff}"
        )

    # Additional: Check 'release' is 2.1.0 and changelog is present and in order
    lines = content.splitlines()
    assert lines[0] == "release: 2.1.0", (
        f"{APP_YAML} first line should be 'release: 2.1.0', got: {lines[0]}"
    )
    assert "changelog:" in lines[1], (
        f"{APP_YAML} should have 'changelog:' as the second line."
    )
    assert lines[2].strip() == "- Added feature X", (
        f"{APP_YAML} should have '- Added feature X' as the first changelog entry."
    )
    assert lines[3].strip() == "- Fixed bug Y", (
        f"{APP_YAML} should have '- Fixed bug Y' as the second changelog entry."
    )


def test_database_toml_exists_and_content_exact():
    assert os.path.exists(DATABASE_TOML), (
        f"Missing file: {DATABASE_TOML}"
    )
    assert os.path.isfile(DATABASE_TOML), (
        f"{DATABASE_TOML} exists but is not a file"
    )

    with open(DATABASE_TOML, "r") as f:
        content = f.read()

    # Check for exact match
    if content != EXPECTED_DATABASE_TOML:
        from difflib import unified_diff
        diff = "\n".join(unified_diff(
            EXPECTED_DATABASE_TOML.splitlines(),
            content.splitlines(),
            fromfile="expected",
            tofile="found",
            lineterm=""
        ))
        pytest.fail(
            f"{DATABASE_TOML} content does not match expected final state.\n"
            f"Diff:\n{diff}"
        )

    # Check that max_active is exactly 40 and not 20
    assert "max_active = 40" in content, (
        f"{DATABASE_TOML} should have 'max_active = 40'"
    )
    assert "max_active = 20" not in content, (
        f"{DATABASE_TOML} should NOT have 'max_active = 20'"
    )


def test_config_update_log_exists_and_content_is_exact():
    assert os.path.exists(CONFIG_UPDATE_LOG), (
        f"Missing file: {CONFIG_UPDATE_LOG}"
    )
    assert os.path.isfile(CONFIG_UPDATE_LOG), (
        f"{CONFIG_UPDATE_LOG} exists but is not a file"
    )

    with open(CONFIG_UPDATE_LOG, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    if lines != EXPECTED_CONFIG_UPDATE_LOG_LINES:
        diff = "\n".join(
            f"Expected: {e!r} | Found: {f!r}"
            for e, f in zip(EXPECTED_CONFIG_UPDATE_LOG_LINES, lines)
            if e != f
        )
        pytest.fail(
            f"{CONFIG_UPDATE_LOG} content does not match expected log lines.\n"
            f"Expected lines (in order):\n"
            f"{EXPECTED_CONFIG_UPDATE_LOG_LINES}\n"
            f"Found lines:\n{lines}\n"
            f"Differences:\n{diff}"
        )

    # Ensure there are exactly 3 lines and no extra content
    assert len(lines) == 3, (
        f"{CONFIG_UPDATE_LOG} should contain exactly 3 lines, found {len(lines)}."
    )