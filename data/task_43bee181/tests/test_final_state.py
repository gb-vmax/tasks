# test_final_state.py

import hashlib
import os
import re
import tarfile
import pytest

ARCHIVE_PATH = "/home/user/releases/translations_v2.tar.gz"
MANIFEST_PATH = "/home/user/releases/translations_v2.manifest"
RELEASES_DIR = "/home/user/releases"

EXPECTED_PO_FILES = [
    "translations/de_DE/app.po",
    "translations/en_US/app.po",
    "translations/en_US/errors.po",
    "translations/es_ES/app.po",
    "translations/fr_FR/app.po",
]


def compute_md5(filepath):
    h = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ── Archive tests ─────────────────────────────────────────────────────────────

def test_releases_directory_exists():
    assert os.path.isdir(RELEASES_DIR), (
        f"Releases directory {RELEASES_DIR} does not exist."
    )


def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive {ARCHIVE_PATH} does not exist."
    )


def test_archive_is_valid_gzip_tar():
    assert tarfile.is_tarfile(ARCHIVE_PATH), (
        f"{ARCHIVE_PATH} is not a valid tar archive."
    )
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            _ = tf.getmembers()
    except Exception as exc:
        pytest.fail(f"{ARCHIVE_PATH} could not be opened as a gzip-compressed tar: {exc}")


def test_archive_contains_all_expected_po_files():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        names = tf.getnames()
    file_names = [n for n in names if not n.endswith("/")]
    po_files_in_archive = [n for n in file_names if n.endswith(".po")]
    missing = [p for p in EXPECTED_PO_FILES if p not in po_files_in_archive]
    assert not missing, (
        f"The following .po files are missing from the archive:\n"
        + "\n".join(missing)
        + f"\nActual .po entries in archive: {sorted(po_files_in_archive)}"
    )


def test_archive_has_no_absolute_paths():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        names = tf.getnames()
    absolute = [n for n in names if n.startswith("/")]
    assert not absolute, (
        f"Archive contains absolute paths (must use relative paths):\n"
        + "\n".join(absolute)
    )


def test_archive_paths_start_with_translations_prefix():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        names = tf.getnames()
    bad = [n for n in names if not n.startswith("translations")]
    assert not bad, (
        f"Archive contains entries that do not start with 'translations/':\n"
        + "\n".join(bad)
    )


# ── Manifest tests ────────────────────────────────────────────────────────────

def test_manifest_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Manifest file {MANIFEST_PATH} does not exist."
    )


def test_manifest_has_no_blank_lines():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    blank_line_numbers = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_line_numbers, (
        f"Manifest contains blank lines at line numbers: {blank_line_numbers}"
    )


def test_manifest_first_five_lines_are_sorted_po_paths():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    assert len(lines) >= 5, (
        f"Manifest has fewer than 5 lines (expected at least 5 .po paths + MD5 line). "
        f"Got {len(lines)} lines."
    )

    actual_first_five = lines[:5]
    assert actual_first_five == EXPECTED_PO_FILES, (
        f"First 5 lines of manifest do not match expected sorted .po paths.\n"
        f"Expected:\n" + "\n".join(EXPECTED_PO_FILES) + "\n"
        f"Got:\n" + "\n".join(actual_first_five)
    )


def test_manifest_last_line_is_md5_format():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    last_line = lines[-1]
    pattern = re.compile(r"^MD5: [0-9a-f]{32}$")
    assert pattern.match(last_line), (
        f"Last line of manifest does not match 'MD5: <32-hex-chars>' format.\n"
        f"Got: {last_line!r}"
    )


def test_manifest_md5_matches_archive():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    last_line = lines[-1]
    pattern = re.compile(r"^MD5: ([0-9a-f]{32})$")
    match = pattern.match(last_line)
    assert match, (
        f"Cannot extract MD5 from last line of manifest: {last_line!r}"
    )
    manifest_checksum = match.group(1)

    actual_checksum = compute_md5(ARCHIVE_PATH)
    assert manifest_checksum == actual_checksum, (
        f"MD5 checksum in manifest does not match actual MD5 of {ARCHIVE_PATH}.\n"
        f"Manifest says: {manifest_checksum}\n"
        f"Actual MD5:    {actual_checksum}"
    )


def test_manifest_has_exactly_six_lines():
    """5 .po file paths + 1 MD5 line = 6 lines total."""
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    assert len(lines) == 6, (
        f"Manifest should have exactly 6 lines (5 .po paths + 1 MD5 line). "
        f"Got {len(lines)} lines:\n" + "\n".join(repr(l) for l in lines)
    )


def test_manifest_no_trailing_whitespace():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    bad_lines = []
    for i, line in enumerate(raw_lines):
        stripped = line.rstrip("\n")
        if stripped != stripped.rstrip():
            bad_lines.append((i + 1, repr(line)))

    assert not bad_lines, (
        f"Manifest lines have trailing whitespace:\n"
        + "\n".join(f"  Line {ln}: {content}" for ln, content in bad_lines)
    )