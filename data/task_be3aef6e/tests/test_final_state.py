# test_final_state.py

import os
import pytest

INFRA_DIR = "/home/user/infra-modules"
VERSION_FILE = os.path.join(INFRA_DIR, "VERSION")
CHANGELOG_FILE = os.path.join(INFRA_DIR, "CHANGELOG.md")
RELEASE_NOTES_FILE = os.path.join(INFRA_DIR, "RELEASE_NOTES.txt")

EXPECTED_NEW_VERSION = "2.7.5"

EXPECTED_VERSION_CONTENT = "2.7.5\n"

EXPECTED_CHANGELOG_CONTENT = (
    "# Changelog\n"
    "\n"
    "## [2.7.5] - 2024-11-15\n"
    "### Changed\n"
    "- Bumped patch version for provisioning pipeline release\n"
    "\n"
    "## [2.7.4] - 2024-10-30\n"
    "### Changed\n"
    "- Updated AWS provider version to 5.x\n"
    "- Refactored VPC subnet allocation logic\n"
    "\n"
    "## [2.7.3] - 2024-09-12\n"
    "### Fixed\n"
    "- Corrected IAM role ARN output in ECS module\n"
)

EXPECTED_RELEASE_NOTES_CONTENT = (
    "Release: 2.7.5\n"
    "Date: 2024-11-15\n"
    "Type: patch\n"
    "Description: Bumped patch version for provisioning pipeline release\n"
)


# --- VERSION file tests ---

def test_version_file_exists():
    assert os.path.isfile(VERSION_FILE), (
        f"VERSION file does not exist at {VERSION_FILE}. "
        "The task requires this file to be present and updated."
    )


def test_version_file_exact_content():
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_VERSION_CONTENT, (
        f"VERSION file content is incorrect.\n"
        f"Expected: {EXPECTED_VERSION_CONTENT!r}\n"
        f"Got:      {content!r}\n"
        "The file should contain exactly '2.7.5' followed by a single newline, "
        "with no extra whitespace or blank lines."
    )


def test_version_is_bumped_patch():
    with open(VERSION_FILE, "r") as f:
        content = f.read().strip()
    assert content == EXPECTED_NEW_VERSION, (
        f"Expected version to be '{EXPECTED_NEW_VERSION}' (patch bumped from 2.7.4), "
        f"but got {content!r}."
    )


def test_version_is_newline_terminated():
    with open(VERSION_FILE, "rb") as f:
        raw = f.read()
    assert raw.endswith(b"\n"), (
        f"VERSION file is not newline-terminated. "
        f"Raw bytes: {raw!r}"
    )


def test_version_has_no_extra_content():
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 1, (
        f"VERSION file should contain exactly one line, but found {len(lines)} lines. "
        f"Content: {content!r}"
    )
    assert lines[0] == EXPECTED_NEW_VERSION, (
        f"The single line in VERSION should be '{EXPECTED_NEW_VERSION}', "
        f"but got {lines[0]!r}."
    )


# --- CHANGELOG file tests ---

def test_changelog_file_exists():
    assert os.path.isfile(CHANGELOG_FILE), (
        f"CHANGELOG.md does not exist at {CHANGELOG_FILE}. "
        "The task requires this file to be present and updated."
    )


def test_changelog_exact_content():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_CHANGELOG_CONTENT, (
        f"CHANGELOG.md content does not match expected.\n"
        f"Expected:\n{EXPECTED_CHANGELOG_CONTENT!r}\n"
        f"Got:\n{content!r}\n"
        "Check for extra/missing blank lines, incorrect version numbers, or wrong dates."
    )


def test_changelog_starts_with_header():
    with open(CHANGELOG_FILE, "r") as f:
        first_line = f.readline()
    assert first_line == "# Changelog\n", (
        f"CHANGELOG.md must start with '# Changelog\\n', got {first_line!r}."
    )


def test_changelog_new_entry_present():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    assert "## [2.7.5] - 2024-11-15" in content, (
        "CHANGELOG.md must contain the new entry '## [2.7.5] - 2024-11-15'. "
        "The new version entry was not found."
    )


def test_changelog_new_entry_before_old_entries():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    pos_new = content.find("## [2.7.5] - 2024-11-15")
    pos_old = content.find("## [2.7.4] - 2024-10-30")
    assert pos_new != -1, (
        "New entry '## [2.7.5] - 2024-11-15' not found in CHANGELOG.md."
    )
    assert pos_old != -1, (
        "Old entry '## [2.7.4] - 2024-10-30' not found in CHANGELOG.md."
    )
    assert pos_new < pos_old, (
        f"New entry (pos {pos_new}) should appear before old entry (pos {pos_old}) "
        "in CHANGELOG.md, but it does not."
    )


def test_changelog_new_entry_after_header():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    pos_header = content.find("# Changelog")
    pos_new = content.find("## [2.7.5] - 2024-11-15")
    assert pos_header < pos_new, (
        "The '# Changelog' header should appear before the new entry '## [2.7.5]', "
        "but it does not."
    )


def test_changelog_contains_new_entry_description():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    assert "- Bumped patch version for provisioning pipeline release" in content, (
        "CHANGELOG.md is missing the required description line: "
        "'- Bumped patch version for provisioning pipeline release'."
    )


def test_changelog_preserves_existing_entries():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    assert "## [2.7.4] - 2024-10-30" in content, (
        "CHANGELOG.md is missing the existing entry '## [2.7.4] - 2024-10-30'."
    )
    assert "## [2.7.3] - 2024-09-12" in content, (
        "CHANGELOG.md is missing the existing entry '## [2.7.3] - 2024-09-12'."
    )
    assert "- Updated AWS provider version to 5.x" in content, (
        "CHANGELOG.md is missing existing content: '- Updated AWS provider version to 5.x'."
    )
    assert "- Refactored VPC subnet allocation logic" in content, (
        "CHANGELOG.md is missing existing content: '- Refactored VPC subnet allocation logic'."
    )
    assert "- Corrected IAM role ARN output in ECS module" in content, (
        "CHANGELOG.md is missing existing content: '- Corrected IAM role ARN output in ECS module'."
    )


def test_changelog_blank_line_after_header():
    with open(CHANGELOG_FILE, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 2, (
        "CHANGELOG.md has fewer than 2 lines; expected at least '# Changelog' and a blank line."
    )
    assert lines[0] == "# Changelog\n", (
        f"First line of CHANGELOG.md should be '# Changelog\\n', got {lines[0]!r}."
    )
    assert lines[1] == "\n", (
        f"Second line of CHANGELOG.md should be a blank line ('\\n'), got {lines[1]!r}. "
        "There must be exactly one blank line between '# Changelog' and the new entry."
    )


def test_changelog_new_entry_starts_on_third_line():
    with open(CHANGELOG_FILE, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 3, (
        "CHANGELOG.md has fewer than 3 lines."
    )
    assert lines[2] == "## [2.7.5] - 2024-11-15\n", (
        f"Third line of CHANGELOG.md should be '## [2.7.5] - 2024-11-15\\n', "
        f"got {lines[2]!r}. The new entry must appear right after the blank line following the header."
    )


def test_changelog_is_newline_terminated():
    with open(CHANGELOG_FILE, "rb") as f:
        raw = f.read()
    assert raw.endswith(b"\n"), (
        "CHANGELOG.md is not newline-terminated. "
        f"Last bytes: {raw[-10:]!r}"
    )


def test_changelog_blank_line_between_new_and_old_entry():
    with open(CHANGELOG_FILE, "r") as f:
        lines = f.readlines()
    # Find the line with the new entry description and check blank line follows
    new_entry_desc_line = None
    for i, line in enumerate(lines):
        if line.strip() == "- Bumped patch version for provisioning pipeline release":
            new_entry_desc_line = i
            break
    assert new_entry_desc_line is not None, (
        "Could not find '- Bumped patch version for provisioning pipeline release' in CHANGELOG.md."
    )
    # The line after the description should be blank
    assert len(lines) > new_entry_desc_line + 1, (
        "CHANGELOG.md ends unexpectedly after the new entry description."
    )
    assert lines[new_entry_desc_line + 1] == "\n", (
        f"Expected a blank line after the new entry description, "
        f"but got {lines[new_entry_desc_line + 1]!r}. "
        "There must be exactly one blank line between the new entry and the next existing entry."
    )


# --- RELEASE_NOTES.txt tests ---

def test_release_notes_file_exists():
    assert os.path.isfile(RELEASE_NOTES_FILE), (
        f"RELEASE_NOTES.txt does not exist at {RELEASE_NOTES_FILE}. "
        "The task requires this file to be created."
    )


def test_release_notes_exact_content():
    with open(RELEASE_NOTES_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_RELEASE_NOTES_CONTENT, (
        f"RELEASE_NOTES.txt content does not match expected.\n"
        f"Expected:\n{EXPECTED_RELEASE_NOTES_CONTENT!r}\n"
        f"Got:\n{content!r}\n"
        "Check for incorrect version, date, type, or description, "
        "as well as extra/missing newlines."
    )


def test_release_notes_release_line():
    with open(RELEASE_NOTES_FILE, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 1, "RELEASE_NOTES.txt is empty."
    assert lines[0] == f"Release: {EXPECTED_NEW_VERSION}\n", (
        f"First line of RELEASE_NOTES.txt should be 'Release: {EXPECTED_NEW_VERSION}\\n', "
        f"got {lines[0]!r}."
    )


def test_release_notes_date_line():
    with open(RELEASE_NOTES_FILE, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 2, "RELEASE_NOTES.txt has fewer than 2 lines."
    assert lines[1] == "Date: 2024-11-15\n", (
        f"Second line of RELEASE_NOTES.txt should be 'Date: 2024-11-15\\n', "
        f"got {lines[1]!r}."
    )


def test_release_notes_type_line():
    with open(RELEASE_NOTES_FILE, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 3, "RELEASE_NOTES.txt has fewer than 3 lines."
    assert lines[2] == "Type: patch\n", (
        f"Third line of RELEASE_NOTES.txt should be 'Type: patch\\n', "
        f"got {lines[2]!r}."
    )


def test_release_notes_description_line():
    with open(RELEASE_NOTES_FILE, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 4, "RELEASE_NOTES.txt has fewer than 4 lines."
    assert lines[3] == "Description: Bumped patch version for provisioning pipeline release\n", (
        f"Fourth line of RELEASE_NOTES.txt should be "
        f"'Description: Bumped patch version for provisioning pipeline release\\n', "
        f"got {lines[3]!r}."
    )


def test_release_notes_no_trailing_blank_lines():
    with open(RELEASE_NOTES_FILE, "r") as f:
        lines = f.readlines()
    assert len(lines) == 4, (
        f"RELEASE_NOTES.txt should have exactly 4 lines, but has {len(lines)}. "
        f"Content: {lines!r}. "
        "There should be no trailing blank lines."
    )


def test_release_notes_is_newline_terminated():
    with open(RELEASE_NOTES_FILE, "rb") as f:
        raw = f.read()
    assert raw.endswith(b"\n"), (
        "RELEASE_NOTES.txt is not newline-terminated. "
        f"Last bytes: {raw[-10:]!r}"
    )


def test_release_notes_ends_after_last_line():
    with open(RELEASE_NOTES_FILE, "rb") as f:
        raw = f.read()
    # Should end with exactly one newline after the last line (no double newline)
    assert not raw.endswith(b"\n\n"), (
        "RELEASE_NOTES.txt ends with more than one newline. "
        "The file should end right after the last line with a single newline."
    )