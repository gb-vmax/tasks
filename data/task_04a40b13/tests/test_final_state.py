# test_final_state.py

import os
import pytest

FR_PO_PATH = "/home/user/translations/fr.po"
COUNT_FILE_PATH = "/home/user/translations/untranslated_count.txt"

EXPECTED_FR_PO_CONTENT = (
    "# French translations for myapp\n"
    "# Copyright (C) 2024\n"
    'msgid ""\n'
    'msgstr ""\n'
    '"Project-Id-Version: myapp 2.0\\n"\n'
    '"Report-Msgid-Bugs-To: \\n"\n'
    '"POT-Creation-Date: 2024-06-01 12:00+0000\\n"\n'
    '"PO-Revision-Date: 2024-06-10 09:00+0000\\n"\n'
    '"Last-Translator: Jean Dupont <jean@example.com>\\n"\n'
    '"Language: fr\\n"\n'
    '"MIME-Version: 1.0\\n"\n'
    '"Content-Type: text/plain; charset=UTF-8\\n"\n'
    '"Content-Transfer-Encoding: 8bit\\n"\n'
    '"X-Untranslated-Count: 6\\n"\n'
    "\n"
    'msgid "Welcome"\n'
    'msgstr "Bienvenue"\n'
    "\n"
    'msgid "Sign in"\n'
    'msgstr ""\n'
    "\n"
    'msgid "Sign out"\n'
    'msgstr "Se déconnecter"\n'
    "\n"
    'msgid "Username"\n'
    'msgstr ""\n'
    "\n"
    'msgid "Password"\n'
    'msgstr "Mot de passe"\n'
    "\n"
    'msgid "Forgot password?"\n'
    'msgstr ""\n'
    "\n"
    'msgid "Submit"\n'
    'msgstr "Envoyer"\n'
    "\n"
    'msgid "Cancel"\n'
    'msgstr ""\n'
    "\n"
    'msgid "Save changes"\n'
    'msgstr "Enregistrer les modifications"\n'
    "\n"
    'msgid "Delete account"\n'
    'msgstr ""\n'
)

EXPECTED_COUNT = 6
EXPECTED_COUNT_FILE_CONTENT = f"Untranslated strings: {EXPECTED_COUNT}\n"


# ---------------------------------------------------------------------------
# Tests for untranslated_count.txt
# ---------------------------------------------------------------------------

def test_count_file_exists():
    assert os.path.isfile(COUNT_FILE_PATH), (
        f"File '{COUNT_FILE_PATH}' does not exist. "
        "Step 1 requires creating this file with the untranslated string count."
    )


def test_count_file_exact_content():
    with open(COUNT_FILE_PATH, "r", encoding="utf-8") as f:
        actual = f.read()
    assert actual == EXPECTED_COUNT_FILE_CONTENT, (
        f"File '{COUNT_FILE_PATH}' has unexpected content.\n"
        f"Expected (repr): {EXPECTED_COUNT_FILE_CONTENT!r}\n"
        f"Actual   (repr): {actual!r}\n"
        "The file must contain exactly one line: "
        f"'Untranslated strings: {EXPECTED_COUNT}' followed by a newline."
    )


def test_count_file_single_line():
    with open(COUNT_FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 1, (
        f"File '{COUNT_FILE_PATH}' should contain exactly one line, "
        f"but found {len(lines)} line(s).\n"
        f"Content (repr): {content!r}"
    )


def test_count_file_correct_number():
    with open(COUNT_FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read().strip()
    expected_line = f"Untranslated strings: {EXPECTED_COUNT}"
    assert content == expected_line, (
        f"Count file content (stripped) is wrong.\n"
        f"Expected: {expected_line!r}\n"
        f"Actual:   {content!r}\n"
        f"The count of untranslated strings should be {EXPECTED_COUNT}."
    )


def test_count_file_ends_with_newline():
    with open(COUNT_FILE_PATH, "rb") as f:
        raw = f.read()
    assert raw.endswith(b"\n"), (
        f"File '{COUNT_FILE_PATH}' must end with a newline character, "
        f"but it does not.\nRaw content (repr): {raw!r}"
    )


def test_count_file_no_trailing_spaces():
    with open(COUNT_FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    line = content.rstrip("\n")
    assert line == line.rstrip(), (
        f"File '{COUNT_FILE_PATH}' contains trailing spaces on the line.\n"
        f"Line (repr): {line!r}"
    )


# ---------------------------------------------------------------------------
# Tests for fr.po file
# ---------------------------------------------------------------------------

def test_fr_po_file_exists():
    assert os.path.isfile(FR_PO_PATH), (
        f"File '{FR_PO_PATH}' does not exist. "
        "The French .po translation file must still be present after the task."
    )


def test_fr_po_x_untranslated_count_updated():
    with open(FR_PO_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    matching_new = [l for l in lines if l.strip() == f'"X-Untranslated-Count: {EXPECTED_COUNT}\\n"']
    assert len(matching_new) == 1, (
        f"Expected exactly one line matching "
        f"'\"X-Untranslated-Count: {EXPECTED_COUNT}\\n\"' in '{FR_PO_PATH}', "
        f"found {len(matching_new)}.\n"
        "Step 2 requires updating the X-Untranslated-Count metadata to "
        f"{EXPECTED_COUNT}."
    )


def test_fr_po_old_x_untranslated_count_gone():
    with open(FR_PO_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    matching_old = [l for l in lines if l.strip() == '"X-Untranslated-Count: 0\\n"']
    assert len(matching_old) == 0, (
        f"Found {len(matching_old)} line(s) still containing "
        f"'\"X-Untranslated-Count: 0\\n\"' in '{FR_PO_PATH}'.\n"
        "The old value (0) must be replaced with the new count "
        f"({EXPECTED_COUNT})."
    )


def test_fr_po_exact_content():
    with open(FR_PO_PATH, "r", encoding="utf-8") as f:
        actual = f.read()
    assert actual == EXPECTED_FR_PO_CONTENT, (
        f"File '{FR_PO_PATH}' does not match the expected final content.\n"
        f"Expected (repr):\n{EXPECTED_FR_PO_CONTENT!r}\n\n"
        f"Actual (repr):\n{actual!r}\n\n"
        "Only the X-Untranslated-Count line should have changed; "
        "all other lines must remain byte-for-byte identical to the original."
    )


def test_fr_po_still_has_six_empty_msgstr():
    with open(FR_PO_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    empty_msgstr = [l for l in lines if l.rstrip("\n") == 'msgstr ""']
    assert len(empty_msgstr) == EXPECTED_COUNT, (
        f"Expected exactly {EXPECTED_COUNT} lines matching 'msgstr \"\"' "
        f"in '{FR_PO_PATH}', found {len(empty_msgstr)}.\n"
        "The untranslated entries themselves must not be modified."
    )


def test_fr_po_translated_strings_unchanged():
    with open(FR_PO_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    expected_translations = [
        'msgstr "Bienvenue"',
        'msgstr "Se déconnecter"',
        'msgstr "Mot de passe"',
        'msgstr "Envoyer"',
        'msgstr "Enregistrer les modifications"',
    ]
    for translation in expected_translations:
        assert translation in content, (
            f"Expected to find '{translation}' in '{FR_PO_PATH}', but it is missing.\n"
            "Existing translated strings must not be modified."
        )


def test_fr_po_msgids_unchanged():
    with open(FR_PO_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    expected_msgids = [
        'msgid "Welcome"',
        'msgid "Sign in"',
        'msgid "Sign out"',
        'msgid "Username"',
        'msgid "Password"',
        'msgid "Forgot password?"',
        'msgid "Submit"',
        'msgid "Cancel"',
        'msgid "Save changes"',
        'msgid "Delete account"',
    ]
    for msgid in expected_msgids:
        assert msgid in content, (
            f"Expected to find '{msgid}' in '{FR_PO_PATH}', but it is missing.\n"
            "All msgid entries must remain unchanged."
        )


def test_fr_po_header_metadata_intact():
    with open(FR_PO_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    expected_metadata = [
        '"Project-Id-Version: myapp 2.0\\n"',
        '"Report-Msgid-Bugs-To: \\n"',
        '"POT-Creation-Date: 2024-06-01 12:00+0000\\n"',
        '"PO-Revision-Date: 2024-06-10 09:00+0000\\n"',
        '"Last-Translator: Jean Dupont <jean@example.com>\\n"',
        '"Language: fr\\n"',
        '"MIME-Version: 1.0\\n"',
        '"Content-Type: text/plain; charset=UTF-8\\n"',
        '"Content-Transfer-Encoding: 8bit\\n"',
    ]
    for meta_line in expected_metadata:
        assert meta_line in content, (
            f"Expected to find metadata line {meta_line!r} in '{FR_PO_PATH}', "
            "but it is missing.\n"
            "Only the X-Untranslated-Count line should have been changed."
        )