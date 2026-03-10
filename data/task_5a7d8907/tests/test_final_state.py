# test_final_state.py

import os
import pytest

L10N = "/home/user/l10n"
VERSIONS = f"{L10N}/versions"
ACTIVE = f"{L10N}/active"
MANIFEST = f"{ACTIVE}/MANIFEST.txt"

EXPECTED_SYMLINKS = {
    "de.po": "../versions/de_v3.po",
    "es.po": "../versions/es_v2.po",
    "fr.po": "../versions/fr_v2.po",
    "ja.po": "../versions/ja_v1.po",
    "ko.po": "../versions/ko_v1.po",
    "pt_BR.po": "../versions/pt_BR_v2.po",
}

EXPECTED_MANIFEST_LINES = [
    "de.po -> ../versions/de_v3.po",
    "es.po -> ../versions/es_v2.po",
    "fr.po -> ../versions/fr_v2.po",
    "ja.po -> ../versions/ja_v1.po",
    "ko.po -> ../versions/ko_v1.po",
    "pt_BR.po -> ../versions/pt_BR_v2.po",
]


# ---------------------------------------------------------------------------
# Directory structure
# ---------------------------------------------------------------------------

def test_l10n_directory_exists():
    assert os.path.isdir(L10N), f"Base directory missing: {L10N}"


def test_versions_directory_exists():
    assert os.path.isdir(VERSIONS), f"versions/ directory missing: {VERSIONS}"


def test_active_directory_exists():
    assert os.path.isdir(ACTIVE), f"active/ directory missing: {ACTIVE}"


# ---------------------------------------------------------------------------
# Versioned .po files still exist
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filename", [
    "de_v3.po",
    "es_v2.po",
    "fr_v1.po",
    "fr_v2.po",
    "pt_BR_v2.po",
    "ja_v1.po",
    "ko_v1.po",
])
def test_versioned_file_exists(filename):
    path = f"{VERSIONS}/{filename}"
    assert os.path.isfile(path), f"Expected versioned file missing: {path}"


def test_pt_BR_v1_still_does_not_exist():
    path = f"{VERSIONS}/pt_BR_v1.po"
    assert not os.path.exists(path), (
        f"pt_BR_v1.po should not exist (it was deleted): {path}"
    )


# ---------------------------------------------------------------------------
# Symlinks in active/ — existence, type, target, and resolution
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("symlink_name,expected_target", EXPECTED_SYMLINKS.items())
def test_symlink_exists(symlink_name, expected_target):
    path = f"{ACTIVE}/{symlink_name}"
    assert os.path.lexists(path), (
        f"Symlink missing from active/: {path}"
    )
    assert os.path.islink(path), (
        f"Entry exists but is not a symlink: {path}"
    )


@pytest.mark.parametrize("symlink_name,expected_target", EXPECTED_SYMLINKS.items())
def test_symlink_target(symlink_name, expected_target):
    path = f"{ACTIVE}/{symlink_name}"
    assert os.path.lexists(path), f"Symlink missing: {path}"
    actual_target = os.readlink(path)
    assert actual_target == expected_target, (
        f"Symlink {symlink_name!r} has wrong target.\n"
        f"  Expected: {expected_target!r}\n"
        f"  Got:      {actual_target!r}"
    )


@pytest.mark.parametrize("symlink_name,expected_target", EXPECTED_SYMLINKS.items())
def test_symlink_resolves(symlink_name, expected_target):
    path = f"{ACTIVE}/{symlink_name}"
    assert os.path.exists(path), (
        f"Symlink {symlink_name!r} is broken — its target does not exist.\n"
        f"  Stored target: {os.readlink(path) if os.path.lexists(path) else 'N/A'}"
    )


# ---------------------------------------------------------------------------
# Exactly the expected symlinks in active/ — no extras, no missing
# ---------------------------------------------------------------------------

def test_active_contains_exactly_expected_symlinks():
    expected = set(EXPECTED_SYMLINKS.keys())
    entries = os.listdir(ACTIVE)
    symlinks_found = {e for e in entries if os.path.islink(f"{ACTIVE}/{e}")}
    missing = expected - symlinks_found
    unexpected = symlinks_found - expected
    assert not missing, (
        f"Expected symlinks missing from active/: {sorted(missing)}"
    )
    assert not unexpected, (
        f"Unexpected symlinks found in active/: {sorted(unexpected)}"
    )


# ---------------------------------------------------------------------------
# MANIFEST.txt — existence and type
# ---------------------------------------------------------------------------

def test_manifest_exists():
    assert os.path.lexists(MANIFEST), (
        f"MANIFEST.txt is missing: {MANIFEST}"
    )


def test_manifest_is_regular_file_not_symlink():
    assert not os.path.islink(MANIFEST), (
        f"MANIFEST.txt must be a regular file, not a symlink: {MANIFEST}"
    )
    assert os.path.isfile(MANIFEST), (
        f"MANIFEST.txt exists but is not a regular file: {MANIFEST}"
    )


# ---------------------------------------------------------------------------
# MANIFEST.txt — content
# ---------------------------------------------------------------------------

def test_manifest_line_count():
    with open(MANIFEST, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 6, (
        f"MANIFEST.txt should have exactly 6 lines, got {len(lines)}.\n"
        f"Content:\n{content!r}"
    )


def test_manifest_ends_with_newline():
    with open(MANIFEST, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"MANIFEST.txt must end with a newline character. "
        f"Last bytes: {content[-4:]!r}"
    )


def test_manifest_exact_content():
    expected_content = "\n".join(EXPECTED_MANIFEST_LINES) + "\n"
    with open(MANIFEST, "r") as f:
        actual_content = f.read()
    assert actual_content == expected_content, (
        f"MANIFEST.txt content does not match expected.\n"
        f"Expected:\n{expected_content!r}\n"
        f"Got:\n{actual_content!r}"
    )


def test_manifest_lines_in_alphabetical_order():
    with open(MANIFEST, "r") as f:
        lines = f.read().splitlines()
    symlink_names = []
    for line in lines:
        parts = line.split(" -> ", 1)
        assert len(parts) == 2, (
            f"Malformed line in MANIFEST.txt (expected '<name> -> <target>'): {line!r}"
        )
        symlink_names.append(parts[0])
    assert symlink_names == sorted(symlink_names), (
        f"MANIFEST.txt lines are not in alphabetical order by symlink name.\n"
        f"Got order: {symlink_names}\n"
        f"Expected order: {sorted(symlink_names)}"
    )


def test_manifest_line_format():
    with open(MANIFEST, "r") as f:
        lines = f.read().splitlines()
    for line in lines:
        assert " -> " in line, (
            f"Malformed line in MANIFEST.txt (missing ' -> '): {line!r}"
        )
        parts = line.split(" -> ", 1)
        name, target = parts[0], parts[1]
        assert name, f"Empty symlink name in MANIFEST.txt line: {line!r}"
        assert target, f"Empty target in MANIFEST.txt line: {line!r}"
        assert not line.endswith(" "), (
            f"Trailing space found in MANIFEST.txt line: {line!r}"
        )


@pytest.mark.parametrize("symlink_name,expected_target", EXPECTED_SYMLINKS.items())
def test_manifest_contains_correct_entry_for_symlink(symlink_name, expected_target):
    expected_line = f"{symlink_name} -> {expected_target}"
    with open(MANIFEST, "r") as f:
        lines = f.read().splitlines()
    assert expected_line in lines, (
        f"Expected line not found in MANIFEST.txt.\n"
        f"  Expected: {expected_line!r}\n"
        f"  Lines found: {lines}"
    )


def test_manifest_does_not_include_itself():
    with open(MANIFEST, "r") as f:
        content = f.read()
    assert "MANIFEST.txt" not in content, (
        f"MANIFEST.txt should not reference itself in its content.\n"
        f"Content:\n{content!r}"
    )