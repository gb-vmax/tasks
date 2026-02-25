# test_final_state.py

import os
import pytest

HOME = "/home/user"
ARCHIVE = os.path.join(HOME, "locales_update.tar.gz")
LOCALES_DIR = os.path.join(HOME, "locales")
EXPECTED_LOCALE_FILES = {"en_US.po", "fr_FR.po", "de_DE.po"}
EXTRACTION_LOG = os.path.join(HOME, "locales_extraction.log")


def test_locales_directory_exists():
    assert os.path.isdir(LOCALES_DIR), (
        f"Directory {LOCALES_DIR} does not exist. "
        "You must extract the archive so that this directory is created."
    )


def test_locales_directory_contents_exact():
    """
    The /home/user/locales directory must contain exactly the three .po files and nothing else.
    """
    try:
        entries = os.listdir(LOCALES_DIR)
    except FileNotFoundError:
        pytest.fail(f"Directory {LOCALES_DIR} does not exist, so cannot check its contents.")

    files = [f for f in entries if os.path.isfile(os.path.join(LOCALES_DIR, f))]
    dirs = [f for f in entries if os.path.isdir(os.path.join(LOCALES_DIR, f))]

    files_set = set(files)
    missing = EXPECTED_LOCALE_FILES - files_set
    extra = files_set - EXPECTED_LOCALE_FILES

    assert not missing, (
        f"Missing file(s) in {LOCALES_DIR}: {', '.join(sorted(missing))}."
    )
    assert not extra, (
        f"Unexpected extra file(s) in {LOCALES_DIR}: {', '.join(sorted(extra))}."
    )
    assert not dirs, (
        f"Directory {LOCALES_DIR} contains unexpected subdirectories: {', '.join(sorted(dirs))}."
    )


@pytest.mark.parametrize("fname", sorted(EXPECTED_LOCALE_FILES))
def test_each_locale_file_exists(fname):
    fpath = os.path.join(LOCALES_DIR, fname)
    assert os.path.isfile(fpath), (
        f"Expected file missing: {fpath}."
    )


def test_locales_extraction_log_exists():
    assert os.path.isfile(EXTRACTION_LOG), (
        f"Extraction log file {EXTRACTION_LOG} does not exist. "
        "You must create this file after extraction."
    )


def test_locales_extraction_log_contents():
    """
    The extraction log must list exactly the three .po file names (not paths), one per line, no extra whitespace,
    no additional lines, and lines may be in any order.
    """
    try:
        with open(EXTRACTION_LOG, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        pytest.fail(f"Extraction log file {EXTRACTION_LOG} not found.")

    lines_set = set(lines)
    missing = EXPECTED_LOCALE_FILES - lines_set
    extra = lines_set - EXPECTED_LOCALE_FILES

    assert not missing, (
        f"Extraction log {EXTRACTION_LOG} is missing entries for: {', '.join(sorted(missing))}."
    )
    assert not extra, (
        f"Extraction log {EXTRACTION_LOG} contains unexpected entries: {', '.join(sorted(extra))}."
    )
    # Check for duplicates
    if len(lines) != len(lines_set):
        dupes = set([x for x in lines if lines.count(x) > 1])
        pytest.fail(
            f"Extraction log {EXTRACTION_LOG} contains duplicate entries: {', '.join(sorted(dupes))}."
        )
    # Check for empty lines or whitespace
    bad_lines = [i+1 for i, l in enumerate(lines) if l.strip() != l or not l]
    assert not bad_lines, (
        f"Extraction log {EXTRACTION_LOG} contains empty or whitespace-padded lines at: {', '.join(map(str, bad_lines))}."
    )
    # Check for correct number of lines
    assert len(lines) == 3, (
        f"Extraction log {EXTRACTION_LOG} should contain exactly 3 lines, found {len(lines)}."
    )


def test_no_other_files_in_locales_dir():
    """
    Ensure there are no extra files or directories in /home/user/locales.
    """
    entries = os.listdir(LOCALES_DIR)
    allowed = EXPECTED_LOCALE_FILES
    extra = [e for e in entries if e not in allowed]
    assert not extra, (
        f"Directory {LOCALES_DIR} contains unexpected files or directories: {', '.join(sorted(extra))}."
    )