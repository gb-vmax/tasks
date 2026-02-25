# test_final_state.py

import os
import pytest

SETTINGS_CFG_PATH = "/home/user/config/settings.cfg"
MODIFIED_KEYS_PATH = "/home/user/config/modified_keys.txt"
EXPECTED_MODIFIED_KEYS = ["user", "theme", "language"]
EXPECTED_MODIFIED_KEYS_CONTENT = "user\ntheme\nlanguage\n"


def test_modified_keys_txt_exists():
    assert os.path.isfile(MODIFIED_KEYS_PATH), (
        f"The file {MODIFIED_KEYS_PATH} does not exist.\n"
        "You must create this file containing the list of modified keys after the task."
    )


def test_modified_keys_txt_content_exact():
    try:
        with open(MODIFIED_KEYS_PATH, "r") as f:
            content = f.read()
    except Exception as e:
        pytest.fail(f"Could not read {MODIFIED_KEYS_PATH}: {e}")

    assert content == EXPECTED_MODIFIED_KEYS_CONTENT, (
        f"The contents of {MODIFIED_KEYS_PATH} are incorrect.\n"
        "Expected (including exact newlines):\n"
        f"{EXPECTED_MODIFIED_KEYS_CONTENT!r}\n"
        "Found:\n"
        f"{content!r}\n"
        "Ensure the file contains only the modified keys (one per line), in the correct order, with no extra spaces or blank lines."
    )


def test_modified_keys_txt_no_extra_lines():
    """
    This test ensures there are no blank lines or extra keys in the output file.
    """
    try:
        with open(MODIFIED_KEYS_PATH, "r") as f:
            lines = f.readlines()
    except Exception as e:
        pytest.fail(f"Could not read {MODIFIED_KEYS_PATH}: {e}")

    # Remove trailing newline characters
    lines_stripped = [line.rstrip("\n") for line in lines]

    assert lines_stripped == EXPECTED_MODIFIED_KEYS, (
        f"{MODIFIED_KEYS_PATH} contains incorrect lines.\n"
        f"Expected lines: {EXPECTED_MODIFIED_KEYS}\n"
        f"Found lines: {lines_stripped}\n"
        "Ensure there are no extra or missing keys, no blank lines, and no trailing spaces."
    )


def test_modified_keys_txt_is_freshly_written(tmp_path):
    """
    This test ensures that the file is overwritten, not appended to.
    """
    # Save original content
    try:
        with open(MODIFIED_KEYS_PATH, "r") as f:
            content = f.read()
    except Exception as e:
        pytest.fail(f"Could not read {MODIFIED_KEYS_PATH}: {e}")

    # Simulate what would happen if the file was appended to (should not be the case)
    appended_content = EXPECTED_MODIFIED_KEYS_CONTENT + "extrakey\n"
    assert content != appended_content, (
        f"{MODIFIED_KEYS_PATH} appears to have been appended to instead of overwritten.\n"
        "The file must contain only the expected keys, and nothing more."
    )


def test_settings_cfg_untouched():
    """
    Ensure the original settings.cfg file remains unchanged after the task.
    """
    expected = (
        "user=alice\n"
        "timeout=unchanged\n"
        "theme=dark\n"
        "autosave=unchanged\n"
        "language=en\n"
    )
    try:
        with open(SETTINGS_CFG_PATH, "r") as f:
            content = f.read()
    except Exception as e:
        pytest.fail(f"Could not read {SETTINGS_CFG_PATH}: {e}")

    assert content == expected, (
        f"The file {SETTINGS_CFG_PATH} was modified during the task. "
        "You must not change the original configuration file."
    )