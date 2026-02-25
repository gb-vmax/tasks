# test_final_state.py

import os
import re
import pytest

WORKFLOWS_DIR = '/home/user/workflows'
DEPLOY_YAML = '/home/user/workflows/deploy.yaml'
SETTINGS_TOML = '/home/user/workflows/settings.toml'
CONFIG_EDIT_LOG = '/home/user/workflows/config_edit.log'

EXPECTED_DEPLOY_YAML = (
    'workflows:\n'
    '  staging_deploy:\n'
    '    description: "Deploy to staging environment"\n'
    '    steps:\n'
    '      - name: build\n'
    '        command: "./scripts/build.sh"\n'
    '      - name: test\n'
    '        command: "./scripts/test.sh"\n'
    '      - name: deploy\n'
    '        command: "./scripts/deploy.sh"\n'
)

EXPECTED_SETTINGS_TOML = (
    '[staging]\n'
    'url = "https://staging.example.com"\n'
    'api_key = "STAGING123ABC"\n'
    'timeout = 60\n'
)

def is_writable_dir(path):
    """Return True if path is a writable directory."""
    return os.path.isdir(path) and os.access(path, os.W_OK | os.X_OK)

def test_workflows_directory_exists_and_writable():
    assert os.path.isdir(WORKFLOWS_DIR), (
        f"Required directory {WORKFLOWS_DIR!r} does not exist. "
        "Please create it before starting the task."
    )
    assert is_writable_dir(WORKFLOWS_DIR), (
        f"Directory {WORKFLOWS_DIR!r} exists but is not writable by the agent. "
        "Please ensure the agent has write permissions."
    )

def test_deploy_yaml_exists_and_contents():
    assert os.path.isfile(DEPLOY_YAML), (
        f"File {DEPLOY_YAML!r} does not exist. "
        "You must create this file as specified."
    )
    with open(DEPLOY_YAML, "r", encoding="utf-8") as f:
        contents = f.read()
    if contents != EXPECTED_DEPLOY_YAML:
        # Show a diff-like context in the error message
        import difflib
        diff = "\n".join(
            difflib.unified_diff(
                EXPECTED_DEPLOY_YAML.splitlines(),
                contents.splitlines(),
                fromfile='expected',
                tofile='actual',
                lineterm=''
            )
        )
        pytest.fail(
            f"Contents of {DEPLOY_YAML!r} do not match the required structure and formatting.\n"
            "Expected:\n"
            f"{EXPECTED_DEPLOY_YAML!r}\n"
            "Actual:\n"
            f"{contents!r}\n"
            "Diff:\n"
            f"{diff}"
        )

def test_settings_toml_exists_and_contents():
    assert os.path.isfile(SETTINGS_TOML), (
        f"File {SETTINGS_TOML!r} does not exist. "
        "You must create this file as specified."
    )
    with open(SETTINGS_TOML, "r", encoding="utf-8") as f:
        contents = f.read()
    if contents != EXPECTED_SETTINGS_TOML:
        import difflib
        diff = "\n".join(
            difflib.unified_diff(
                EXPECTED_SETTINGS_TOML.splitlines(),
                contents.splitlines(),
                fromfile='expected',
                tofile='actual',
                lineterm=''
            )
        )
        pytest.fail(
            f"Contents of {SETTINGS_TOML!r} do not match the required structure and formatting.\n"
            "Expected:\n"
            f"{EXPECTED_SETTINGS_TOML!r}\n"
            "Actual:\n"
            f"{contents!r}\n"
            "Diff:\n"
            f"{diff}"
        )

def test_config_edit_log_exists_and_format():
    assert os.path.isfile(CONFIG_EDIT_LOG), (
        f"File {CONFIG_EDIT_LOG!r} does not exist. "
        "You must create this file as specified."
    )
    with open(CONFIG_EDIT_LOG, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if len(lines) != 2:
        pytest.fail(
            f"File {CONFIG_EDIT_LOG!r} must contain exactly two lines, one for each edit. "
            f"Found {len(lines)} line(s):\n{lines}"
        )

    # Check line 1: [YYYY-MM-DD HH:MM:SS] Edited deploy.yaml
    line1 = lines[0].rstrip('\n')
    pattern1 = r'^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] Edited deploy\.yaml$'
    match1 = re.match(pattern1, line1)
    if not match1:
        pytest.fail(
            f"The first line of {CONFIG_EDIT_LOG!r} must match the format:\n"
            "[YYYY-MM-DD HH:MM:SS] Edited deploy.yaml\n"
            f"Found:\n{line1!r}"
        )

    # Check line 2: [YYYY-MM-DD HH:MM:SS] Edited settings.toml
    line2 = lines[1].rstrip('\n')
    pattern2 = r'^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] Edited settings\.toml$'
    match2 = re.match(pattern2, line2)
    if not match2:
        pytest.fail(
            f"The second line of {CONFIG_EDIT_LOG!r} must match the format:\n"
            "[YYYY-MM-DD HH:MM:SS] Edited settings.toml\n"
            f"Found:\n{line2!r}"
        )

    # Optional: check that the first timestamp is not after the second
    from datetime import datetime
    try:
        ts1 = datetime.strptime(match1.group(1), "%Y-%m-%d %H:%M:%S")
        ts2 = datetime.strptime(match2.group(1), "%Y-%m-%d %H:%M:%S")
        if ts1 > ts2:
            pytest.fail(
                f"The timestamp for deploy.yaml ({match1.group(1)}) "
                f"should not be later than settings.toml ({match2.group(1)})."
            )
    except ValueError:
        pytest.fail(
            f"Timestamp format error in {CONFIG_EDIT_LOG!r}. "
            "Timestamps must be in 'YYYY-MM-DD HH:MM:SS' 24-hour format."
        )

def test_no_extra_files_in_workflows_dir():
    """Ensure that only the required files exist in /home/user/workflows."""
    expected = {"deploy.yaml", "settings.toml", "config_edit.log"}
    files = set(
        f for f in os.listdir(WORKFLOWS_DIR)
        if os.path.isfile(os.path.join(WORKFLOWS_DIR, f))
    )
    extra = files - expected
    if extra:
        pytest.fail(
            f"Unexpected extra file(s) found in {WORKFLOWS_DIR!r}: {sorted(extra)}. "
            "Only deploy.yaml, settings.toml, and config_edit.log should be present."
        )