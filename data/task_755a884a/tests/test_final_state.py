# test_final_state.py

import os
import pytest

APP_DIR = "/home/user/app"
VERSION_FILE = os.path.join(APP_DIR, "VERSION")
CHANGELOG_FILE = os.path.join(APP_DIR, "CHANGELOG.md")

EXPECTED_VERSION_STRING = "2.4.8"
EXPECTED_VERSION_FILE_CONTENT = "2.4.8\n"

EXPECTED_CHANGELOG_CONTENT = """# Changelog

## [2.4.7] - 2024-10-30

### Fixed
- Resolved race condition in session cleanup worker

## [2.4.6] - 2024-09-18

### Added
- Support for OAuth2 token refresh flows

## [2.4.8] - 2024-11-15

### Security
- Patched critical input validation vulnerability in authentication module
"""


def test_version_file_exists():
    assert os.path.isfile(VERSION_FILE), (
        f"VERSION file '{VERSION_FILE}' does not exist. "
        "The file must be present after completing the task."
    )


def test_version_file_exact_content():
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_VERSION_FILE_CONTENT, (
        f"VERSION file content is incorrect.\n"
        f"Expected (repr): {repr(EXPECTED_VERSION_FILE_CONTENT)}\n"
        f"Got (repr):      {repr(content)}\n"
        "The file must contain exactly '2.4.8' followed by a single newline, "
        "with no trailing spaces, no 'v' prefix, and no extra lines."
    )


def test_version_is_bumped_to_248():
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    version = content.strip()
    assert version == EXPECTED_VERSION_STRING, (
        f"Expected version to be '{EXPECTED_VERSION_STRING}', but got '{version}'. "
        "The patch component of '2.4.7' must be incremented by 1 to '2.4.8'."
    )


def test_version_no_v_prefix():
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    version = content.strip()
    assert not version.startswith("v"), (
        f"VERSION string '{version}' must not start with a 'v' prefix. "
        "The format should be '2.4.8', not 'v2.4.8'."
    )


def test_version_no_trailing_spaces():
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) >= 1, "VERSION file appears to be empty."
    first_line = lines[0]
    assert first_line == first_line.rstrip(), (
        f"VERSION file first line has trailing spaces: {repr(first_line)}. "
        "No trailing spaces are allowed."
    )


def test_version_single_newline_at_end():
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        f"VERSION file does not end with a newline. Got (repr): {repr(content)}"
    )
    assert not content.endswith("\n\n"), (
        f"VERSION file ends with more than one newline. Got (repr): {repr(content)}"
    )


def test_version_exactly_one_line():
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 1, (
        f"VERSION file must contain exactly one line, but found {len(lines)} lines. "
        f"Content (repr): {repr(content)}"
    )


def test_changelog_file_exists():
    assert os.path.isfile(CHANGELOG_FILE), (
        f"CHANGELOG file '{CHANGELOG_FILE}' does not exist. "
        "The file must be present after completing the task."
    )


def test_changelog_exact_content():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_CHANGELOG_CONTENT, (
        f"CHANGELOG.md content does not match the expected final content.\n\n"
        f"Expected (repr):\n{repr(EXPECTED_CHANGELOG_CONTENT)}\n\n"
        f"Got (repr):\n{repr(content)}\n\n"
        "Ensure the new entry is appended with exactly one blank line separating "
        "it from the prior content, and that the format matches exactly."
    )


def test_changelog_contains_new_version_entry():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    assert "## [2.4.8] - 2024-11-15" in content, (
        "CHANGELOG.md is missing the new version heading '## [2.4.8] - 2024-11-15'. "
        "The new entry must be appended to the changelog."
    )


def test_changelog_contains_security_section():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    assert "### Security" in content, (
        "CHANGELOG.md is missing the '### Security' section heading. "
        "The new entry must include this section."
    )


def test_changelog_contains_security_bullet():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    expected_bullet = "- Patched critical input validation vulnerability in authentication module"
    assert expected_bullet in content, (
        f"CHANGELOG.md is missing the security bullet point.\n"
        f"Expected to find: '{expected_bullet}'\n"
        "The exact bullet text must be present in the changelog."
    )


def test_changelog_preserves_existing_content():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()

    existing_entries = [
        "# Changelog",
        "## [2.4.7] - 2024-10-30",
        "### Fixed",
        "- Resolved race condition in session cleanup worker",
        "## [2.4.6] - 2024-09-18",
        "### Added",
        "- Support for OAuth2 token refresh flows",
    ]
    for entry in existing_entries:
        assert entry in content, (
            f"CHANGELOG.md is missing pre-existing content: '{entry}'. "
            "The original changelog entries must be preserved when appending the new entry."
        )


def test_changelog_new_entry_at_end():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    expected_ending = (
        "## [2.4.8] - 2024-11-15\n\n"
        "### Security\n"
        "- Patched critical input validation vulnerability in authentication module\n"
    )
    assert content.endswith(expected_ending), (
        f"CHANGELOG.md does not end with the expected new entry block.\n"
        f"Expected ending (repr): {repr(expected_ending)}\n"
        f"Actual ending (repr):   {repr(content[-len(expected_ending) - 20:])}\n"
        "The new entry must appear at the very end of the changelog."
    )


def test_changelog_single_blank_line_separator():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    # The separator between old content and new entry should be exactly one blank line
    # i.e., the old content ends with the OAuth2 line, then \n\n, then the new entry
    expected_separator = (
        "- Support for OAuth2 token refresh flows\n\n"
        "## [2.4.8] - 2024-11-15"
    )
    assert expected_separator in content, (
        "CHANGELOG.md does not have exactly one blank line separating the existing "
        "content from the new entry.\n"
        f"Expected to find (repr): {repr(expected_separator)}\n"
        "Ensure there is exactly one blank line (not zero, not two) between the last "
        "existing entry and the new '## [2.4.8]' heading."
    )


def test_changelog_no_double_blank_lines_before_new_entry():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    # Should not have two or more blank lines before the new entry
    bad_separator = "- Support for OAuth2 token refresh flows\n\n\n## [2.4.8]"
    assert bad_separator not in content, (
        "CHANGELOG.md has more than one blank line before the new '## [2.4.8]' entry. "
        "There must be exactly one blank line as separator."
    )