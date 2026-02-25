# test_final_state.py

import os
import pytest

NET_SETTINGS_LOG_PATH = "/home/user/system/logs/net_settings.log"
EXPECTED_NET_SETTINGS_LOG_CONTENT = (
    "net_mode=auto\n"
    "net_timeout=30\n"
    "net_interface=eth0\n"
)

def test_net_settings_log_exists():
    assert os.path.isfile(NET_SETTINGS_LOG_PATH), (
        f"Expected file {NET_SETTINGS_LOG_PATH} does not exist. "
        "The processed net_ settings output file is missing."
    )

def test_net_settings_log_content_exact():
    try:
        with open(NET_SETTINGS_LOG_PATH, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        pytest.fail(f"Could not read {NET_SETTINGS_LOG_PATH}: {e}")

    # Normalize line endings to \n for comparison
    normalized_actual = content.replace('\r\n', '\n').replace('\r', '\n')
    normalized_expected = EXPECTED_NET_SETTINGS_LOG_CONTENT

    assert normalized_actual == normalized_expected, (
        f"Contents of {NET_SETTINGS_LOG_PATH} are incorrect.\n"
        f"Expected exactly:\n{EXPECTED_NET_SETTINGS_LOG_CONTENT!r}\n"
        f"Found:\n{content!r}\n"
        "Check for missing/extra/incorrect lines, comments, or whitespace."
    )

def test_net_settings_log_no_blank_lines_or_comments():
    """
    Ensure there are no blank lines or comment lines in the output.
    """
    with open(NET_SETTINGS_LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        stripped = line.rstrip('\r\n')
        assert stripped, (
            f"Blank line found at line {i} in {NET_SETTINGS_LOG_PATH}."
        )
        assert not stripped.lstrip().startswith("#"), (
            f"Comment line found at line {i} in {NET_SETTINGS_LOG_PATH}: {stripped!r}"
        )

def test_net_settings_log_no_leading_trailing_spaces():
    """
    Ensure no line has leading or trailing spaces.
    """
    with open(NET_SETTINGS_LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        if line.endswith('\n'):
            content = line[:-1]
        else:
            content = line
        assert content == content.strip(), (
            f"Line {i} in {NET_SETTINGS_LOG_PATH} has leading or trailing spaces: {line!r}"
        )