# test_final_state.py

import os
import pytest

BASE = "/home/user/i18n"
LOCALES = os.path.join(BASE, "locales")
ACTIVE = os.path.join(BASE, "active")
REPORT = os.path.join(BASE, "symlink_report.txt")


# ── Locale source files still exist ───────────────────────────────────────────

def test_en_us_messages_po_exists():
    path = os.path.join(LOCALES, "en_US", "messages.po")
    assert os.path.isfile(path), f"Missing file: {path}"

def test_pt_br_messages_po_exists():
    path = os.path.join(LOCALES, "pt_BR", "messages.po")
    assert os.path.isfile(path), f"Missing file: {path}"

def test_pt_pt_messages_po_exists():
    path = os.path.join(LOCALES, "pt_PT", "messages.po")
    assert os.path.isfile(path), f"Missing file: {path}"

def test_fr_fr_messages_po_exists():
    path = os.path.join(LOCALES, "fr_FR", "messages.po")
    assert os.path.isfile(path), f"Missing file: {path}"


# ── english.po symlink ────────────────────────────────────────────────────────

def test_english_po_is_symlink():
    path = os.path.join(ACTIVE, "english.po")
    assert os.path.islink(path), (
        f"{path} must be a symlink, but it is not. "
        "The symlink was not created correctly."
    )

def test_english_po_points_to_correct_target():
    path = os.path.join(ACTIVE, "english.po")
    target = os.readlink(path)
    expected = "../locales/en_US/messages.po"
    assert target == expected, (
        f"{path} should point to {expected!r}, but currently points to {target!r}. "
        "The symlink was not updated to point to the English locale."
    )

def test_english_po_resolves_to_existing_file():
    path = os.path.join(ACTIVE, "english.po")
    assert os.path.exists(path), (
        f"{path} symlink is broken — the target does not exist. "
        "The symlink must resolve to a real file."
    )

def test_english_po_resolves_to_english_content():
    path = os.path.join(ACTIVE, "english.po")
    content = open(path).read()
    assert "English translations" in content, (
        f"{path} resolves to a file that does not contain 'English translations'. "
        f"Got content: {content!r}"
    )


# ── portuguese.po symlink ─────────────────────────────────────────────────────

def test_portuguese_po_is_symlink():
    path = os.path.join(ACTIVE, "portuguese.po")
    assert os.path.islink(path), (
        f"{path} must be a symlink, but it is not. "
        "The symlink was not created correctly."
    )

def test_portuguese_po_points_to_correct_target():
    path = os.path.join(ACTIVE, "portuguese.po")
    target = os.readlink(path)
    expected = "../locales/pt_BR/messages.po"
    assert target == expected, (
        f"{path} should point to {expected!r}, but currently points to {target!r}. "
        "The broken symlink was not fixed to point to the Brazilian Portuguese locale."
    )

def test_portuguese_po_resolves_to_existing_file():
    path = os.path.join(ACTIVE, "portuguese.po")
    assert os.path.exists(path), (
        f"{path} symlink is broken — the target does not exist. "
        "The symlink must resolve to a real file."
    )

def test_portuguese_po_resolves_to_portuguese_content():
    path = os.path.join(ACTIVE, "portuguese.po")
    content = open(path).read()
    assert "Brazilian Portuguese translations" in content, (
        f"{path} resolves to a file that does not contain 'Brazilian Portuguese translations'. "
        f"Got content: {content!r}"
    )


# ── french.po symlink (must remain untouched) ─────────────────────────────────

def test_french_po_is_symlink():
    path = os.path.join(ACTIVE, "french.po")
    assert os.path.islink(path), (
        f"{path} must remain a symlink, but it is not. "
        "The french.po symlink should have been left untouched."
    )

def test_french_po_points_to_correct_target():
    path = os.path.join(ACTIVE, "french.po")
    target = os.readlink(path)
    expected = "../locales/fr_FR/messages.po"
    assert target == expected, (
        f"{path} should point to {expected!r}, but currently points to {target!r}. "
        "The french.po symlink should have been left untouched."
    )

def test_french_po_resolves_to_existing_file():
    path = os.path.join(ACTIVE, "french.po")
    assert os.path.exists(path), (
        f"{path} symlink is broken — the target does not exist. "
        "The french.po symlink must resolve to a real file."
    )

def test_french_po_resolves_to_french_content():
    path = os.path.join(ACTIVE, "french.po")
    content = open(path).read()
    assert "French translations" in content, (
        f"{path} resolves to a file that does not contain 'French translations'. "
        f"Got content: {content!r}"
    )


# ── symlink_report.txt ────────────────────────────────────────────────────────

def test_symlink_report_exists():
    assert os.path.isfile(REPORT), (
        f"Missing file: {REPORT}. "
        "The verification report was not created."
    )

def test_symlink_report_exact_content():
    expected_content = (
        "english.po -> ../locales/en_US/messages.po\n"
        "french.po -> ../locales/fr_FR/messages.po\n"
        "portuguese.po -> ../locales/pt_BR/messages.po\n"
    )
    with open(REPORT, "r") as f:
        actual_content = f.read()
    assert actual_content == expected_content, (
        f"Content of {REPORT} does not match expected.\n"
        f"Expected:\n{expected_content!r}\n"
        f"Got:\n{actual_content!r}"
    )

def test_symlink_report_line_count():
    with open(REPORT, "r") as f:
        lines = f.readlines()
    # Strip trailing newline from last line for counting non-empty lines
    non_empty_lines = [l for l in lines if l.strip()]
    assert len(non_empty_lines) == 3, (
        f"{REPORT} should contain exactly 3 non-empty lines, "
        f"but found {len(non_empty_lines)}: {lines!r}"
    )

def test_symlink_report_alphabetical_order():
    with open(REPORT, "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines() if l.strip()]
    names = [line.split(" -> ")[0] for line in lines]
    assert names == sorted(names), (
        f"Lines in {REPORT} are not in alphabetical order by symlink name. "
        f"Got order: {names}"
    )

def test_symlink_report_english_line():
    with open(REPORT, "r") as f:
        content = f.read()
    expected_line = "english.po -> ../locales/en_US/messages.po"
    assert expected_line in content, (
        f"Expected line {expected_line!r} not found in {REPORT}.\n"
        f"File content: {content!r}"
    )

def test_symlink_report_french_line():
    with open(REPORT, "r") as f:
        content = f.read()
    expected_line = "french.po -> ../locales/fr_FR/messages.po"
    assert expected_line in content, (
        f"Expected line {expected_line!r} not found in {REPORT}.\n"
        f"File content: {content!r}"
    )

def test_symlink_report_portuguese_line():
    with open(REPORT, "r") as f:
        content = f.read()
    expected_line = "portuguese.po -> ../locales/pt_BR/messages.po"
    assert expected_line in content, (
        f"Expected line {expected_line!r} not found in {REPORT}.\n"
        f"File content: {content!r}"
    )

def test_symlink_report_no_trailing_spaces():
    with open(REPORT, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"{REPORT} line {i} has trailing spaces: {line!r}"
        )

def test_symlink_report_no_blank_lines():
    with open(REPORT, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"{REPORT} has a blank line at line {i}. No blank lines are allowed."
        )