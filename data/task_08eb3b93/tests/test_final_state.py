# test_final_state.py

import os
import pytest

VERSION_PATH = "/home/user/api-client/VERSION"
CHANGELOG_PATH = "/home/user/api-client/CHANGELOG.md"
API_CLIENT_DIR = "/home/user/api-client"

EXPECTED_VERSION = "2.4.0"

EXPECTED_VERSION_FILE_CONTENT = "2.4.0\n"

EXPECTED_CHANGELOG_CONTENT = (
    "## [2.4.0] - 2024-06-15\n"
    "\n"
    "### Added\n"
    "- OAuth2 token refresh support\n"
    "\n"
    "### Fixed\n"
    "- GET requests no longer fail when query params are empty\n"
    "\n"
    "## [2.3.7] - 2024-05-30\n"
    "\n"
    "### Fixed\n"
    "- Timeout handling on slow connections\n"
    "\n"
    "## [2.3.6] - 2024-05-10\n"
    "\n"
    "### Added\n"
    "- Support for custom headers per request\n"
)

EXPECTED_CHANGELOG_HEAD_12 = (
    "## [2.4.0] - 2024-06-15\n"
    "\n"
    "### Added\n"
    "- OAuth2 token refresh support\n"
    "\n"
    "### Fixed\n"
    "- GET requests no longer fail when query params are empty\n"
    "\n"
    "## [2.3.7] - 2024-05-30\n"
    "\n"
    "### Fixed\n"
    "- Timeout handling on slow connections\n"
)


def test_api_client_directory_exists():
    assert os.path.isdir(API_CLIENT_DIR), (
        f"Directory {API_CLIENT_DIR} does not exist. "
        "The api-client project directory is missing."
    )


def test_version_file_exists():
    assert os.path.isfile(VERSION_PATH), (
        f"File {VERSION_PATH} does not exist. "
        "The VERSION file is required after task completion."
    )


def test_version_file_is_readable():
    assert os.access(VERSION_PATH, os.R_OK), (
        f"File {VERSION_PATH} is not readable."
    )


def test_version_file_exact_content():
    with open(VERSION_PATH, "r") as f:
        content = f.read()
    assert content == EXPECTED_VERSION_FILE_CONTENT, (
        f"VERSION file content is incorrect.\n"
        f"Expected (repr): {EXPECTED_VERSION_FILE_CONTENT!r}\n"
        f"Actual   (repr): {content!r}\n"
        "The VERSION file should contain exactly '2.4.0' followed by a newline."
    )


def test_version_file_stripped_value():
    with open(VERSION_PATH, "r") as f:
        content = f.read().strip()
    assert content == EXPECTED_VERSION, (
        f"VERSION file stripped content is '{content}', expected '{EXPECTED_VERSION}'. "
        "The MINOR version should have been bumped from 2.3.7 to 2.4.0 "
        "and PATCH reset to 0."
    )


def test_version_no_v_prefix():
    with open(VERSION_PATH, "r") as f:
        content = f.read().strip()
    assert not content.startswith("v"), (
        f"VERSION file content '{content}' starts with 'v'. "
        "The version must not have a 'v' prefix."
    )


def test_version_no_leading_trailing_whitespace():
    with open(VERSION_PATH, "r") as f:
        content = f.read()
    # Allow only a trailing newline, no spaces or extra blank lines
    stripped = content.strip()
    assert stripped == EXPECTED_VERSION, (
        f"VERSION file has unexpected whitespace. "
        f"Content (repr): {content!r}. "
        "There should be no leading/trailing whitespace beyond a single newline."
    )


def test_version_format_major_minor_patch():
    with open(VERSION_PATH, "r") as f:
        content = f.read().strip()
    parts = content.split(".")
    assert len(parts) == 3, (
        f"VERSION '{content}' is not in MAJOR.MINOR.PATCH format."
    )
    for part in parts:
        assert part.isdigit(), (
            f"VERSION '{content}' has non-numeric component '{part}'."
        )


def test_version_major_unchanged():
    with open(VERSION_PATH, "r") as f:
        content = f.read().strip()
    parts = content.split(".")
    assert parts[0] == "2", (
        f"MAJOR version should remain '2', but got '{parts[0]}'. "
        "Only the MINOR version should be bumped."
    )


def test_version_minor_bumped():
    with open(VERSION_PATH, "r") as f:
        content = f.read().strip()
    parts = content.split(".")
    assert parts[1] == "4", (
        f"MINOR version should be '4' (bumped from 3), but got '{parts[1]}'. "
        "The MINOR version must be incremented by 1."
    )


def test_version_patch_reset_to_zero():
    with open(VERSION_PATH, "r") as f:
        content = f.read().strip()
    parts = content.split(".")
    assert parts[2] == "0", (
        f"PATCH version should be '0' (reset after minor bump), but got '{parts[2]}'. "
        "After a minor version bump, PATCH must be reset to 0."
    )


def test_changelog_file_exists():
    assert os.path.isfile(CHANGELOG_PATH), (
        f"File {CHANGELOG_PATH} does not exist. "
        "The CHANGELOG.md file is required after task completion."
    )


def test_changelog_file_is_readable():
    assert os.access(CHANGELOG_PATH, os.R_OK), (
        f"File {CHANGELOG_PATH} is not readable."
    )


def test_changelog_starts_with_new_version_entry():
    with open(CHANGELOG_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")
    assert first_line == "## [2.4.0] - 2024-06-15", (
        f"CHANGELOG.md should start with '## [2.4.0] - 2024-06-15', "
        f"but first line is: '{first_line}'. "
        "The new entry must be prepended at the very top of the file."
    )


def test_changelog_contains_new_version_header():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    assert "## [2.4.0] - 2024-06-15" in content, (
        "CHANGELOG.md is missing the new '## [2.4.0] - 2024-06-15' entry."
    )


def test_changelog_contains_oauth2_added():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    assert "- OAuth2 token refresh support" in content, (
        "CHANGELOG.md is missing the '- OAuth2 token refresh support' line "
        "under the ### Added section of the new entry."
    )


def test_changelog_contains_get_request_fix():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    assert "- GET requests no longer fail when query params are empty" in content, (
        "CHANGELOG.md is missing the "
        "'- GET requests no longer fail when query params are empty' line "
        "under the ### Fixed section of the new entry."
    )


def test_changelog_new_entry_has_added_section():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    # The ### Added section should appear before the old content
    new_entry_block = content.split("## [2.3.7]")[0]
    assert "### Added" in new_entry_block, (
        "The new changelog entry is missing the '### Added' section header."
    )


def test_changelog_new_entry_has_fixed_section():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    new_entry_block = content.split("## [2.3.7]")[0]
    assert "### Fixed" in new_entry_block, (
        "The new changelog entry is missing the '### Fixed' section header."
    )


def test_changelog_contains_old_2_3_7_entry():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    assert "## [2.3.7] - 2024-05-30" in content, (
        "CHANGELOG.md is missing the original '## [2.3.7] - 2024-05-30' entry. "
        "Existing content must not be removed or modified."
    )


def test_changelog_contains_old_2_3_6_entry():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    assert "## [2.3.6] - 2024-05-10" in content, (
        "CHANGELOG.md is missing the original '## [2.3.6] - 2024-05-10' entry. "
        "Existing content must not be removed or modified."
    )


def test_changelog_old_content_preserved_verbatim():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    original_content = (
        "## [2.3.7] - 2024-05-30\n"
        "\n"
        "### Fixed\n"
        "- Timeout handling on slow connections\n"
        "\n"
        "## [2.3.6] - 2024-05-10\n"
        "\n"
        "### Added\n"
        "- Support for custom headers per request"
    )
    assert original_content in content, (
        "The original CHANGELOG.md content has been modified or is missing. "
        "Only prepending is allowed; existing content must remain unchanged.\n"
        f"Expected to find (verbatim):\n{original_content}\n\n"
        f"Actual file content:\n{content}"
    )


def test_changelog_new_entry_before_old_entry():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    pos_new = content.find("## [2.4.0]")
    pos_old = content.find("## [2.3.7]")
    assert pos_new != -1, "## [2.4.0] entry not found in CHANGELOG.md."
    assert pos_old != -1, "## [2.3.7] entry not found in CHANGELOG.md."
    assert pos_new < pos_old, (
        f"The new [2.4.0] entry (at position {pos_new}) should appear before "
        f"the old [2.3.7] entry (at position {pos_old}) in CHANGELOG.md."
    )


def test_changelog_blank_line_between_new_and_old_entry():
    with open(CHANGELOG_PATH, "r") as f:
        lines = f.readlines()
    # Find the line index of "## [2.3.7]"
    old_entry_line_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## [2.3.7] - 2024-05-30":
            old_entry_line_idx = i
            break
    assert old_entry_line_idx is not None, (
        "Could not find '## [2.3.7] - 2024-05-30' in CHANGELOG.md."
    )
    assert old_entry_line_idx >= 1, (
        "The [2.3.7] entry is at the very top of the file; "
        "there should be a blank line before it (after the new entry)."
    )
    preceding_line = lines[old_entry_line_idx - 1]
    assert preceding_line.strip() == "", (
        f"There should be exactly one blank line between the new [2.4.0] entry "
        f"and the old [2.3.7] entry, but the line before [2.3.7] is: "
        f"{preceding_line!r}"
    )


def test_changelog_exact_content():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    assert content == EXPECTED_CHANGELOG_CONTENT, (
        f"CHANGELOG.md exact content does not match expected.\n"
        f"Expected (repr):\n{EXPECTED_CHANGELOG_CONTENT!r}\n\n"
        f"Actual (repr):\n{content!r}"
    )


def test_changelog_first_12_lines():
    with open(CHANGELOG_PATH, "r") as f:
        lines = f.readlines()
    first_12 = "".join(lines[:12])
    assert first_12 == EXPECTED_CHANGELOG_HEAD_12, (
        f"First 12 lines of CHANGELOG.md do not match expected output.\n"
        f"Expected (repr):\n{EXPECTED_CHANGELOG_HEAD_12!r}\n\n"
        f"Actual (repr):\n{first_12!r}"
    )


def test_changelog_new_entry_structure():
    """Verify the new entry block has the correct structure."""
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()

    expected_new_entry = (
        "## [2.4.0] - 2024-06-15\n"
        "\n"
        "### Added\n"
        "- OAuth2 token refresh support\n"
        "\n"
        "### Fixed\n"
        "- GET requests no longer fail when query params are empty\n"
        "\n"
    )
    assert content.startswith(expected_new_entry), (
        f"CHANGELOG.md does not start with the expected new entry block.\n"
        f"Expected start (repr):\n{expected_new_entry!r}\n\n"
        f"Actual start (repr):\n{content[:len(expected_new_entry)]!r}"
    )