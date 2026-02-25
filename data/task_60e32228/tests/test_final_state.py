# test_final_state.py
import os
import json
import pytest

LOCALIZATION_DIR = "/home/user/localization"
EN_JSON = os.path.join(LOCALIZATION_DIR, "en.json")
FR_JSON = os.path.join(LOCALIZATION_DIR, "fr.json")
ES_JSON = os.path.join(LOCALIZATION_DIR, "es.json")
UPDATE_LOG = os.path.join(LOCALIZATION_DIR, "update_report.log")

EXPECTED_EN = {
    "login": "Login",
    "logout": "Logout",
    "profile": "Profile",
    "settings": "Settings",
    "welcome": "Welcome",
}

EXPECTED_FR = {
    "login": "Connexion",
    "logout": "[[MISSING_TRANSLATION]]Logout[[MISSING_TRANSLATION]]",
    "profile": "Profil",
    "settings": "[[MISSING_TRANSLATION]]Settings[[MISSING_TRANSLATION]]",
    "welcome": "Bienvenue",
}

EXPECTED_ES = {
    "login": "Iniciar sesión",
    "logout": "Cerrar sesión",
    "profile": "[[MISSING_TRANSLATION]]Profile[[MISSING_TRANSLATION]]",
    "settings": "[[MISSING_TRANSLATION]]Settings[[MISSING_TRANSLATION]]",
    "welcome": "Bienvenido",
}

EXPECTED_LOG = """Missing keys added
Added to fr.json: logout
Added to fr.json: settings
Added to es.json: profile
Added to es.json: settings

Extra keys removed
Removed from fr.json: extra_fr
Removed from es.json: extra_es

Final key count
en.json: 5 keys
fr.json: 5 keys
es.json: 5 keys
"""

@pytest.mark.describe("Final OS/filesystem state after localization translation update task")
class TestFinalState:

    def test_localization_directory_exists(self):
        assert os.path.isdir(LOCALIZATION_DIR), (
            f"Directory {LOCALIZATION_DIR} does not exist. "
            f"The required directory must remain present after processing."
        )

    @pytest.mark.parametrize("fpath", [EN_JSON, FR_JSON, ES_JSON])
    def test_translation_files_exist(self, fpath):
        assert os.path.isfile(fpath), (
            f"File {fpath} does not exist after processing. "
            f"All translation JSON files must remain present."
        )

    def test_en_json_content_and_format(self):
        with open(EN_JSON, encoding="utf-8") as f:
            content = f.read()
            try:
                data = json.loads(content)
            except Exception as e:
                pytest.fail(f"{EN_JSON} is not valid JSON: {e}")

        # Check keys and values
        assert data == EXPECTED_EN, (
            f"{EN_JSON} does not match the expected keys and values after processing.\n"
            f"Expected: {EXPECTED_EN}\nFound: {data}"
        )

        # Check that keys are sorted alphabetically in the file (not just in dict)
        keys_in_file = _get_json_keys_in_order(content)
        expected_sorted_keys = sorted(EXPECTED_EN.keys())
        assert keys_in_file == expected_sorted_keys, (
            f"{EN_JSON} keys are not sorted alphabetically in the file.\n"
            f"Expected order: {expected_sorted_keys}\nFound order: {keys_in_file}"
        )

        # Check pretty-print: 2-space indentation (first key should be indented 2 spaces, etc.)
        _assert_json_pretty_printed(content, EN_JSON)

    def test_fr_json_content_and_format(self):
        with open(FR_JSON, encoding="utf-8") as f:
            content = f.read()
            try:
                data = json.loads(content)
            except Exception as e:
                pytest.fail(f"{FR_JSON} is not valid JSON: {e}")

        # Check keys and values
        assert data == EXPECTED_FR, (
            f"{FR_JSON} does not match the expected keys and values after processing.\n"
            f"Expected: {EXPECTED_FR}\nFound: {data}"
        )

        # Check that keys are sorted alphabetically in the file
        keys_in_file = _get_json_keys_in_order(content)
        expected_sorted_keys = sorted(EXPECTED_FR.keys())
        assert keys_in_file == expected_sorted_keys, (
            f"{FR_JSON} keys are not sorted alphabetically in the file.\n"
            f"Expected order: {expected_sorted_keys}\nFound order: {keys_in_file}"
        )

        # Check pretty-print: 2-space indentation
        _assert_json_pretty_printed(content, FR_JSON)

    def test_es_json_content_and_format(self):
        with open(ES_JSON, encoding="utf-8") as f:
            content = f.read()
            try:
                data = json.loads(content)
            except Exception as e:
                pytest.fail(f"{ES_JSON} is not valid JSON: {e}")

        # Check keys and values
        assert data == EXPECTED_ES, (
            f"{ES_JSON} does not match the expected keys and values after processing.\n"
            f"Expected: {EXPECTED_ES}\nFound: {data}"
        )

        # Check that keys are sorted alphabetically in the file
        keys_in_file = _get_json_keys_in_order(content)
        expected_sorted_keys = sorted(EXPECTED_ES.keys())
        assert keys_in_file == expected_sorted_keys, (
            f"{ES_JSON} keys are not sorted alphabetically in the file.\n"
            f"Expected order: {expected_sorted_keys}\nFound order: {keys_in_file}"
        )

        # Check pretty-print: 2-space indentation
        _assert_json_pretty_printed(content, ES_JSON)

    def test_all_json_files_have_the_same_keys(self):
        with open(EN_JSON, encoding="utf-8") as f:
            en_keys = set(json.load(f).keys())
        with open(FR_JSON, encoding="utf-8") as f:
            fr_keys = set(json.load(f).keys())
        with open(ES_JSON, encoding="utf-8") as f:
            es_keys = set(json.load(f).keys())
        assert en_keys == fr_keys == es_keys, (
            "All translation files must contain exactly the same set of keys after processing.\n"
            f"en.json: {en_keys}\nfr.json: {fr_keys}\nes.json: {es_keys}"
        )

    def test_update_report_log_content_and_format(self):
        assert os.path.isfile(UPDATE_LOG), (
            f"{UPDATE_LOG} does not exist after processing. "
            "You must create a log file as specified."
        )
        with open(UPDATE_LOG, encoding="utf-8") as f:
            log_content = f.read()
        # Remove trailing spaces on each line for robust comparison
        expected_lines = [line.rstrip() for line in EXPECTED_LOG.strip('\n').splitlines()]
        found_lines = [line.rstrip() for line in log_content.strip('\n').splitlines()]

        assert expected_lines == found_lines, (
            "The contents of update_report.log do not match the expected log format or values.\n"
            "==== Expected ====\n"
            f"{EXPECTED_LOG.strip()}\n"
            "==== Found ====\n"
            f"{log_content.strip()}\n"
            "===="
        )


def _get_json_keys_in_order(json_text):
    """
    Helper to extract the order of keys as they appear in the JSON file.
    Assumes top-level flat JSON.
    """
    lines = json_text.splitlines()
    key_order = []
    for line in lines:
        line = line.strip()
        if not line or line == '{' or line == '}':
            continue
        if ':' not in line:
            continue
        # Get key part
        key_part = line.split(':', 1)[0].strip()
        if key_part.startswith('"') and key_part.endswith('"'):
            key = key_part[1:-1]
            key_order.append(key)
    return key_order

def _assert_json_pretty_printed(json_text, fname):
    """
    Asserts that the given JSON text is pretty-printed with 2-space indentation.
    Checks that:
      - Each key line (except the first '{' and last '}') is indented exactly 2 spaces.
      - There are no tabs.
    """
    lines = json_text.splitlines()
    if len(lines) < 3:
        pytest.fail(f"{fname} does not appear to be pretty-printed (too few lines).")
    assert lines[0].strip() == "{", f"{fname} does not start with '{{'."
    assert lines[-1].strip() == "}", f"{fname} does not end with '}}'."
    for i, line in enumerate(lines[1:-1], start=2):
        if not line.strip():
            continue  # skip blank lines
        assert line.startswith("  "), (
            f"{fname} line {i} ('{line}') is not indented with 2 spaces as required."
        )
        assert not line.startswith("   "), (
            f"{fname} line {i} ('{line}') is indented with more than 2 spaces."
        )
        assert "\t" not in line, (
            f"{fname} line {i} ('{line}') contains a tab character; use spaces only."
        )