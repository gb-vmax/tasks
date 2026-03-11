# test_final_state.py

import os
import pytest

IMPORT_PATH = "/home/user/translations/import_fr.tsv"

EXPECTED_LINES = [
    "string_id\ttranslation_fr\tsource_en",
    "btn_save\tEnregistrer\tSave",
    "btn_cancel\tAnnuler\tCancel",
    "msg_welcome\tBon retour !\tWelcome back!",
    "err_not_found\tPage introuvable\tPage not found",
    "lbl_username\tNom d'utilisateur\tUsername",
]


def test_import_file_exists():
    assert os.path.isfile(IMPORT_PATH), (
        f"File '{IMPORT_PATH}' does not exist. "
        "The import_fr.tsv file must be created as part of the task."
    )


def test_import_file_is_readable():
    assert os.access(IMPORT_PATH, os.R_OK), (
        f"File '{IMPORT_PATH}' is not readable."
    )


def test_import_file_unix_line_endings():
    with open(IMPORT_PATH, "rb") as f:
        content = f.read()
    assert b"\r\n" not in content, (
        f"File '{IMPORT_PATH}' contains Windows line endings (CRLF). "
        "Expected Unix line endings (LF only)."
    )


def test_import_file_line_count():
    with open(IMPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip trailing newline for counting (a single trailing newline is acceptable)
    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 6, (
        f"File '{IMPORT_PATH}' has {len(lines)} lines, expected 6 (including header). "
        f"Lines found: {lines}"
    )


def test_import_file_header():
    with open(IMPORT_PATH, "r", encoding="utf-8") as f:
        header = f.readline().rstrip("\n")

    columns = header.split("\t")
    assert columns == ["string_id", "translation_fr", "source_en"], (
        f"Header of '{IMPORT_PATH}' has unexpected columns: {columns}. "
        "Expected: ['string_id', 'translation_fr', 'source_en']"
    )


def test_import_file_has_three_columns_per_row():
    with open(IMPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.rstrip("\n").split("\n")
    for i, line in enumerate(lines, start=1):
        cols = line.split("\t")
        assert len(cols) == 3, (
            f"Line {i} of '{IMPORT_PATH}' has {len(cols)} columns, expected 3.\n"
            f"  Line content: {repr(line)}"
        )


def test_import_file_no_context_column():
    with open(IMPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.rstrip("\n").split("\n")
    # Check that none of the known context values appear as a full tab-separated field
    context_values = [
        "Used on all form footers",
        "Shown on login page",
        "HTTP 404 page",
        "Login form label",
        "context",
    ]
    for i, line in enumerate(lines, start=1):
        cols = line.split("\t")
        for ctx in context_values:
            assert ctx not in cols, (
                f"Line {i} of '{IMPORT_PATH}' still contains context value '{ctx}'. "
                "The context column must be dropped from the output file.\n"
                f"  Line content: {repr(line)}"
            )


def test_import_file_column_order():
    """Verify that translation_fr comes before source_en (columns are swapped vs export)."""
    with open(IMPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.rstrip("\n").split("\n")
    # Skip header, check data rows
    data_rows = lines[1:]
    # Known mappings: string_id -> (translation_fr, source_en)
    expected_data = {
        "btn_save": ("Enregistrer", "Save"),
        "btn_cancel": ("Annuler", "Cancel"),
        "msg_welcome": ("Bon retour !", "Welcome back!"),
        "err_not_found": ("Page introuvable", "Page not found"),
        "lbl_username": ("Nom d'utilisateur", "Username"),
    }
    for i, line in enumerate(data_rows, start=2):
        cols = line.split("\t")
        assert len(cols) == 3, (
            f"Line {i} of '{IMPORT_PATH}' does not have exactly 3 columns: {repr(line)}"
        )
        string_id, translation_fr, source_en = cols
        assert string_id in expected_data, (
            f"Line {i} of '{IMPORT_PATH}' has unexpected string_id '{string_id}'."
        )
        exp_trans, exp_source = expected_data[string_id]
        assert translation_fr == exp_trans, (
            f"Line {i} of '{IMPORT_PATH}': column 2 (translation_fr) for '{string_id}' "
            f"is wrong.\n  Expected: {repr(exp_trans)}\n  Actual:   {repr(translation_fr)}"
        )
        assert source_en == exp_source, (
            f"Line {i} of '{IMPORT_PATH}': column 3 (source_en) for '{string_id}' "
            f"is wrong.\n  Expected: {repr(exp_source)}\n  Actual:   {repr(source_en)}"
        )


def test_import_file_no_trailing_whitespace():
    with open(IMPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.rstrip("\n").split("\n")
    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} of '{IMPORT_PATH}' has trailing whitespace.\n"
            f"  Line content: {repr(line)}"
        )


def test_import_file_exact_content():
    """Check the complete file content matches the expected output exactly."""
    with open(IMPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    expected_content = (
        "string_id\ttranslation_fr\tsource_en\n"
        "btn_save\tEnregistrer\tSave\n"
        "btn_cancel\tAnnuler\tCancel\n"
        "msg_welcome\tBon retour !\tWelcome back!\n"
        "err_not_found\tPage introuvable\tPage not found\n"
        "lbl_username\tNom d'utilisateur\tUsername\n"
    )

    assert content == expected_content, (
        f"Content of '{IMPORT_PATH}' does not exactly match expected content.\n"
        f"  Expected: {repr(expected_content)}\n"
        f"  Actual:   {repr(content)}"
    )


def test_import_file_all_rows_present():
    """Ensure all 5 data rows (plus header) are present."""
    with open(IMPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 6, (
        f"Expected 6 lines in '{IMPORT_PATH}' (1 header + 5 data rows), "
        f"but found {len(lines)}."
    )

    for i, (actual, expected) in enumerate(zip(lines, EXPECTED_LINES), start=1):
        assert actual == expected, (
            f"Line {i} of '{IMPORT_PATH}' does not match expected content.\n"
            f"  Expected: {repr(expected)}\n"
            f"  Actual:   {repr(actual)}"
        )


def test_export_file_unchanged():
    """Verify the original export.tsv was not modified."""
    export_path = "/home/user/translations/export.tsv"
    expected_export_lines = [
        "string_id\tcontext\tsource_en\ttranslation_fr",
        "btn_save\tUsed on all form footers\tSave\tEnregistrer",
        "btn_cancel\tUsed on all form footers\tCancel\tAnnuler",
        "msg_welcome\tShown on login page\tWelcome back!\tBon retour !",
        "err_not_found\tHTTP 404 page\tPage not found\tPage introuvable",
        "lbl_username\tLogin form label\tUsername\tNom d'utilisateur",
    ]

    assert os.path.isfile(export_path), (
        f"Original file '{export_path}' no longer exists. It must not be deleted."
    )

    with open(export_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 6, (
        f"Original file '{export_path}' now has {len(lines)} lines; expected 6."
    )

    for i, (actual, expected) in enumerate(zip(lines, expected_export_lines), start=1):
        assert actual == expected, (
            f"Line {i} of original '{export_path}' was modified.\n"
            f"  Expected: {repr(expected)}\n"
            f"  Actual:   {repr(actual)}"
        )