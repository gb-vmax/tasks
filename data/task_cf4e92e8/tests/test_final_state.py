# test_final_state.py

import pytest
import os

ORIGINAL_CONF_PATH = "/home/user/original.conf"
UPDATED_CONF_PATH = "/home/user/updated.conf"
CHANGE_LOG_PATH = "/home/user/change.log"

EXPECTED_CHANGE_LOG_CONTENT = (
    "ADDED: setting4=true\n"
    "ADDED: setting5=maybe\n"
)

@pytest.mark.describe("Final state validation for configuration changelog task")
class TestFinalState:
    def test_original_conf_intact(self):
        """Ensure /home/user/original.conf still exists and is unchanged."""
        assert os.path.isfile(ORIGINAL_CONF_PATH), (
            f"{ORIGINAL_CONF_PATH} is missing. The original config file must not be deleted or moved."
        )
        with open(ORIGINAL_CONF_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        expected = "setting1=on\nsetting2=off\nsetting3=yes\n"
        assert content == expected, (
            f"{ORIGINAL_CONF_PATH} has been changed.\n"
            "Expected contents:\n"
            f"{expected!r}\n"
            "Actual contents:\n"
            f"{content!r}"
        )

    def test_updated_conf_intact(self):
        """Ensure /home/user/updated.conf still exists and is unchanged."""
        assert os.path.isfile(UPDATED_CONF_PATH), (
            f"{UPDATED_CONF_PATH} is missing. The updated config file must not be deleted or moved."
        )
        with open(UPDATED_CONF_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        expected = "setting1=on\nsetting2=off\nsetting3=yes\nsetting4=true\nsetting5=maybe\n"
        assert content == expected, (
            f"{UPDATED_CONF_PATH} has been changed.\n"
            "Expected contents:\n"
            f"{expected!r}\n"
            "Actual contents:\n"
            f"{content!r}"
        )

    def test_change_log_exists(self):
        """Ensure /home/user/change.log exists."""
        assert os.path.isfile(CHANGE_LOG_PATH), (
            f"{CHANGE_LOG_PATH} does not exist. You must create this file containing the changelog of added lines."
        )

    def test_change_log_content_exact(self):
        """Ensure /home/user/change.log contains only and exactly the correct added lines, in order, with correct format."""
        with open(CHANGE_LOG_PATH, "r", encoding="utf-8") as f:
            actual = f.read()
        assert actual == EXPECTED_CHANGE_LOG_CONTENT, (
            f"{CHANGE_LOG_PATH} contents are incorrect.\n"
            "Expected:\n"
            f"{EXPECTED_CHANGE_LOG_CONTENT!r}\n"
            "Found:\n"
            f"{actual!r}\n"
            "Each added line must be present, prefixed by 'ADDED: ', in the order they appear in updated.conf, with no extra lines or blank lines."
        )

    def test_change_log_no_extra_lines(self):
        """Ensure no extra lines or blank lines are present in the changelog."""
        with open(CHANGE_LOG_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        expected_lines = [
            "ADDED: setting4=true\n",
            "ADDED: setting5=maybe\n",
        ]
        assert lines == expected_lines, (
            f"{CHANGE_LOG_PATH} contains unexpected lines or formatting issues.\n"
            "Expected lines:\n"
            f"{expected_lines!r}\n"
            "Found lines:\n"
            f"{lines!r}\n"
            "Make sure there are no blank lines or extra content."
        )