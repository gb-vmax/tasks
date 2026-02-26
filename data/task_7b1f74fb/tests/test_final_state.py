# test_final_state.py

import os
import pytest

SQL_OPTIMIZER_DIR = "/home/user/sql-optimizer"
VERSION_FILE = os.path.join(SQL_OPTIMIZER_DIR, "VERSION")
CHANGELOG_FILE = os.path.join(SQL_OPTIMIZER_DIR, "CHANGELOG.md")

EXPECTED_NEW_VERSION = "1.5.0"
EXPECTED_OLD_VERSION = "1.4.0"
EXPECTED_DATE = "2024-06-05"

EXPECTED_CHANGELOG = (
    f"## [{EXPECTED_NEW_VERSION}] - {EXPECTED_DATE}\n"
    "- Optimized SELECT queries for faster execution.\n\n"
    f"## [{EXPECTED_OLD_VERSION}] - 2024-05-30\n"
    "- Initial release."
)


def test_version_file_exists_and_contains_new_version():
    assert os.path.isfile(VERSION_FILE), (
        f"File {VERSION_FILE} does not exist. The version file is missing."
    )
    with open(VERSION_FILE, "r") as f:
        version_content = f.read().strip()
    assert version_content == EXPECTED_NEW_VERSION, (
        f"{VERSION_FILE} should contain '{EXPECTED_NEW_VERSION}' but contains: '{version_content}'"
    )
    # Ensure there are no extra lines or spaces
    with open(VERSION_FILE, "r") as f:
        lines = f.readlines()
    assert len(lines) == 1, (
        f"{VERSION_FILE} should only contain a single line with the version number, "
        f"but has {len(lines)} lines."
    )
    assert lines[0].strip() == EXPECTED_NEW_VERSION, (
        f"The only line in {VERSION_FILE} should be '{EXPECTED_NEW_VERSION}', "
        f"but is '{lines[0].strip()}'."
    )


def test_changelog_file_exists_and_has_expected_entry():
    assert os.path.isfile(CHANGELOG_FILE), (
        f"File {CHANGELOG_FILE} does not exist. The changelog file is missing."
    )
    with open(CHANGELOG_FILE, "r") as f:
        changelog_content = f.read()
    # Normalize line endings for robustness
    normalized_actual = changelog_content.replace('\r\n', '\n').strip()
    normalized_expected = EXPECTED_CHANGELOG.replace('\r\n', '\n').strip()

    assert normalized_actual == normalized_expected, (
        f"{CHANGELOG_FILE} is not correctly updated.\n\n"
        f"Expected content:\n\n{EXPECTED_CHANGELOG}\n\n"
        f"But found:\n\n{changelog_content}\n\n"
        "Make sure you:\n"
        "- Inserted the new version section at the very top (after any intro, if present).\n"
        "- Used the correct version and date in the header: '## [{EXPECTED_NEW_VERSION}] - {EXPECTED_DATE}'.\n"
        "- Prefixed the description with '- ' and used the exact wording: "
        "'Optimized SELECT queries for faster execution.'\n"
        "- Left the rest of the changelog unchanged except for this new entry.\n"
        "- Used blank lines between sections as shown."
    )