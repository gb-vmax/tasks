# test_final_state.py

import os
import pytest

PROJECT_DIR = "/home/user/localization_project"
ENV_EXAMPLE_PATH = os.path.join(PROJECT_DIR, ".env.example")
ENV_PATH = os.path.join(PROJECT_DIR, ".env")
LOCALE_LOG_PATH = os.path.join(PROJECT_DIR, "locale_status.log")

EXPECTED_ENV_CONTENT = [
    "LANG=fr_FR",
    "LANGUAGE=fr",
    "LC_ALL=fr_FR.UTF-8"
]

EXPECTED_LOG_LINES = [
    "Current LANG: fr_FR",
    "Current LANGUAGE: fr",
    "Current LC_ALL: fr_FR.UTF-8"
]

EXPECTED_ENV_VARS = {
    "LANG": "fr_FR",
    "LANGUAGE": "fr",
    "LC_ALL": "fr_FR.UTF-8"
}


def test_env_file_exists_with_correct_content():
    assert os.path.isfile(ENV_PATH), (
        f"File '{ENV_PATH}' does not exist. You must create this file by copying and editing '.env.example'."
    )
    with open(ENV_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]
    assert lines == EXPECTED_ENV_CONTENT, (
        f"File '{ENV_PATH}' does not have the expected content.\n"
        f"Expected:\n{EXPECTED_ENV_CONTENT}\n"
        f"Found:\n{lines}\n"
        "Check that you have set LANG, LANGUAGE, and LC_ALL to the correct French values, with no extra spaces or lines."
    )


@pytest.mark.parametrize("var,expected", EXPECTED_ENV_VARS.items())
def test_environment_variables_set_in_session(var, expected):
    value = os.environ.get(var)
    assert value == expected, (
        f"Environment variable {var} is not set correctly in the current session.\n"
        f"Expected {var}={expected!r}, but found {var}={value!r}.\n"
        "You must export the variables in your session after editing '.env'."
    )


def test_locale_status_log_exists_and_correct_content():
    assert os.path.isfile(LOCALE_LOG_PATH), (
        f"File '{LOCALE_LOG_PATH}' does not exist. You must create this file to document the current localization settings."
    )
    with open(LOCALE_LOG_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]
    assert lines == EXPECTED_LOG_LINES, (
        f"File '{LOCALE_LOG_PATH}' does not have the expected content.\n"
        f"Expected exactly:\n{EXPECTED_LOG_LINES}\n"
        f"Found:\n{lines}\n"
        "Check that the log contains exactly three lines, no extra spaces, and matches the required format."
    )
    assert len(lines) == 3, (
        f"File '{LOCALE_LOG_PATH}' should contain exactly 3 lines, but found {len(lines)} lines."
    )
    for idx, (expected, actual) in enumerate(zip(EXPECTED_LOG_LINES, lines), 1):
        assert expected == actual, (
            f"Line {idx} in '{LOCALE_LOG_PATH}' is incorrect.\n"
            f"Expected: '{expected}'\n"
            f"Found:    '{actual}'\n"
            "Ensure there are no extra spaces or typos."
        )