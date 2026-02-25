# test_final_state.py

import os
import pwd
import stat
import pytest

LOCALIZATION_DIR = "/home/user/localization"
EN_PATH = os.path.join(LOCALIZATION_DIR, "en.txt")
FR_PATH = os.path.join(LOCALIZATION_DIR, "fr.txt")
LOG_PATH = os.path.join(LOCALIZATION_DIR, "update_log.txt")

EXPECTED_EN = {
    "greeting": "Hello",
    "farewell": "Goodbye",
    "question": "How are you?"
}

EXPECTED_FR = [
    "greeting=Bonjour",
    "question=Comment ça va ?",
    "farewell="
]

EXPECTED_LOG = [
    "Added missing translation: farewell"
]

USER_NAME = "user"

def get_file_owner(path):
    return pwd.getpwuid(os.stat(path).st_uid).pw_name

def is_user_writable(path):
    st = os.stat(path)
    user_uid = pwd.getpwnam(USER_NAME).pw_uid
    return (st.st_uid == user_uid) and (st.st_mode & stat.S_IWUSR)

def permissions_user_only_writable(path):
    """
    Checks that the file is owned by 'user' and is user-writable ONLY
    (i.e., group/others do not have write permission).
    """
    st = os.stat(path)
    user_uid = pwd.getpwnam(USER_NAME).pw_uid
    mode = st.st_mode
    # Only user has write permission, group/other do not
    return (
        st.st_uid == user_uid and
        (mode & stat.S_IWUSR) and
        not (mode & stat.S_IWGRP) and
        not (mode & stat.S_IWOTH)
    )

@pytest.mark.describe("Final OS/container state after localization update")
class TestLocalizationFinalState:
    def test_localization_dir_exists_and_owned_by_user(self):
        assert os.path.isdir(LOCALIZATION_DIR), (
            f"Directory {LOCALIZATION_DIR} does not exist."
        )
        dir_stat = os.stat(LOCALIZATION_DIR)
        user_uid = pwd.getpwnam(USER_NAME).pw_uid
        assert dir_stat.st_uid == user_uid, (
            f"Directory {LOCALIZATION_DIR} is not owned by '{USER_NAME}'."
        )
        assert dir_stat.st_mode & stat.S_IWUSR, (
            f"Directory {LOCALIZATION_DIR} is not writable by '{USER_NAME}'."
        )

    def test_en_txt_unchanged(self):
        assert os.path.isfile(EN_PATH), (
            f"File {EN_PATH} does not exist."
        )
        with open(EN_PATH, "r", encoding="utf-8") as f:
            contents = f.read().strip().splitlines()
        en_dict = {}
        for line in contents:
            line = line.strip()
            if line and '=' in line:
                key, value = line.split('=', 1)
                en_dict[key.strip()] = value.strip()
        assert en_dict == EXPECTED_EN, (
            f"File {EN_PATH} content has changed or is incorrect. "
            f"Expected: {EXPECTED_EN}, Found: {en_dict}"
        )

    def test_fr_txt_content_and_order(self):
        assert os.path.isfile(FR_PATH), (
            f"File {FR_PATH} does not exist."
        )
        with open(FR_PATH, "r", encoding="utf-8") as f:
            contents = [line.rstrip('\n') for line in f]
        # Remove trailing empty lines for comparison
        while contents and not contents[-1].strip():
            contents.pop()
        assert contents == EXPECTED_FR, (
            f"File {FR_PATH} content is incorrect.\n"
            f"Expected (in order):\n{EXPECTED_FR}\n"
            f"Found:\n{contents}"
        )

    def test_fr_txt_permissions_and_ownership(self):
        assert os.path.isfile(FR_PATH), (
            f"File {FR_PATH} does not exist."
        )
        assert permissions_user_only_writable(FR_PATH), (
            f"File {FR_PATH} must be owned by '{USER_NAME}' and writable only by that user "
            f"(not group/others)."
        )

    def test_update_log_txt_content(self):
        assert os.path.isfile(LOG_PATH), (
            f"File {LOG_PATH} does not exist."
        )
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            log_lines = [line.rstrip('\n') for line in f]
        # Remove trailing empty lines for comparison
        while log_lines and not log_lines[-1].strip():
            log_lines.pop()
        if EXPECTED_LOG:
            assert log_lines == EXPECTED_LOG, (
                f"File {LOG_PATH} has incorrect content.\n"
                f"Expected (in order):\n{EXPECTED_LOG}\n"
                f"Found:\n{log_lines}"
            )
        else:
            assert log_lines == ["No missing translations found."], (
                f"File {LOG_PATH} should contain 'No missing translations found.' if there were no additions."
            )

    def test_update_log_txt_permissions_and_ownership(self):
        assert os.path.isfile(LOG_PATH), (
            f"File {LOG_PATH} does not exist."
        )
        assert permissions_user_only_writable(LOG_PATH), (
            f"File {LOG_PATH} must be owned by '{USER_NAME}' and writable only by that user "
            f"(not group/others)."
        )