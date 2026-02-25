# test_final_state.py

import os
import json
import pytest

LOCALIZATION_DIR = "/home/user/localization"
EN_JSON = os.path.join(LOCALIZATION_DIR, "en.json")
FR_JSON = os.path.join(LOCALIZATION_DIR, "fr.json")
DE_JSON = os.path.join(LOCALIZATION_DIR, "de.json")
UPDATE_LOG = os.path.join(LOCALIZATION_DIR, "update_verification.log")

EXPECTED_EN_JSON = {
    "welcome": "Welcome to our site.",
    "login_message": "Please enter your username and password.",
    "logout_message": "You have been logged out successfully."
}

EXPECTED_FR_JSON = {
    "welcome": "Bienvenue sur notre site.",
    "login_message": "Veuillez entrer votre identifiant et votre mot de passe.",
    "logout_message": "Vous avez été déconnecté avec succès."
}

EXPECTED_DE_JSON = {
    "welcome": "Willkommen auf unserer Seite.",
    "login_message": "Bitte geben Sie Ihren Benutzernamen und Ihr Passwort ein.",
    "logout_message": "Sie wurden erfolgreich abgemeldet."
}

EXPECTED_LOG = (
    "en:\n"
    "  exists: true\n"
    "  value: \"You have been logged out successfully.\"\n"
    "fr:\n"
    "  exists: true\n"
    "  value: \"Vous avez été déconnecté avec succès.\"\n"
    "de:\n"
    "  exists: true\n"
    "  value: \"Sie wurden erfolgreich abgemeldet.\"\n"
)

@pytest.mark.parametrize(
    "filepath", [EN_JSON, FR_JSON, DE_JSON],
)
def test_translation_files_exist(filepath):
    assert os.path.isfile(filepath), f"Missing required translation file: {filepath}"

def test_localization_directory_exists():
    assert os.path.isdir(LOCALIZATION_DIR), f"Directory missing: {LOCALIZATION_DIR}"

def test_en_json_final_content():
    with open(EN_JSON, encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            pytest.fail(f"Failed to parse {EN_JSON} as JSON: {e}")
    assert data == EXPECTED_EN_JSON, (
        f"{EN_JSON} does not contain the expected final content.\n"
        f"Expected: {EXPECTED_EN_JSON}\nFound: {data}"
    )

def test_fr_json_final_content():
    with open(FR_JSON, encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            pytest.fail(f"Failed to parse {FR_JSON} as JSON: {e}")
    assert data == EXPECTED_FR_JSON, (
        f"{FR_JSON} does not contain the expected final content.\n"
        f"Expected: {EXPECTED_FR_JSON}\nFound: {data}"
    )

def test_de_json_final_content():
    with open(DE_JSON, encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            pytest.fail(f"Failed to parse {DE_JSON} as JSON: {e}")
    assert data == EXPECTED_DE_JSON, (
        f"{DE_JSON} does not contain the expected final content.\n"
        f"Expected: {EXPECTED_DE_JSON}\nFound: {data}"
    )

def test_update_verification_log_exists():
    assert os.path.isfile(UPDATE_LOG), f"Verification log file missing: {UPDATE_LOG}"

def test_update_verification_log_content():
    assert os.path.isfile(UPDATE_LOG), f"Verification log file missing: {UPDATE_LOG}"
    with open(UPDATE_LOG, encoding="utf-8") as f:
        content = f.read()
    # Remove any trailing whitespace for comparison, but require exact formatting otherwise.
    if content != EXPECTED_LOG:
        diff_lines = []
        expected_lines = EXPECTED_LOG.splitlines()
        actual_lines = content.splitlines()
        max_len = max(len(expected_lines), len(actual_lines))
        for i in range(max_len):
            exp = expected_lines[i] if i < len(expected_lines) else "<MISSING>"
            act = actual_lines[i] if i < len(actual_lines) else "<MISSING>"
            if exp != act:
                diff_lines.append(
                    f"Line {i+1} differs:\n  Expected: {repr(exp)}\n  Found:    {repr(act)}"
                )
        diff_str = "\n".join(diff_lines) if diff_lines else "Content differs, but could not compute line difference."
        pytest.fail(
            f"{UPDATE_LOG} does not exactly match the required YAML format and content.\n"
            f"--- Expected ---\n{EXPECTED_LOG}"
            f"--- Found ---\n{content}\n"
            f"Differences:\n{diff_str}"
        )

def test_update_verification_log_no_extra_content():
    """Ensure that the log file does not contain any extra keys, comments, or content."""
    with open(UPDATE_LOG, encoding="utf-8") as f:
        content = f.read()
    # The log must only contain the three language sections, in order, no extra keys or comments.
    # Check for absence of '#' (comments) and any other top-level keys.
    for illegal in ['#', 'extra', 'comment', '//']:
        assert illegal not in content, (
            f"{UPDATE_LOG} contains illegal content (e.g., '{illegal}'). "
            "Only the exact YAML structure as specified is allowed."
        )

def test_logout_message_keys_only_in_translation_files():
    """Ensure only the specified keys are present in each translation file."""
    lang_files = [
        (EN_JSON, set(EXPECTED_EN_JSON.keys())),
        (FR_JSON, set(EXPECTED_FR_JSON.keys())),
        (DE_JSON, set(EXPECTED_DE_JSON.keys())),
    ]
    for filepath, expected_keys in lang_files:
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
        extra_keys = set(data.keys()) - expected_keys
        missing_keys = expected_keys - set(data.keys())
        assert not extra_keys, (
            f"{filepath} contains unexpected keys: {extra_keys}. "
            f"Only these keys should be present: {sorted(expected_keys)}"
        )
        assert not missing_keys, (
            f"{filepath} is missing required keys: {missing_keys}. "
            f"Expected keys: {sorted(expected_keys)}"
        )