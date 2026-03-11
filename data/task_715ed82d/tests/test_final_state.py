# test_final_state.py

import os
import pytest

VERSION_PATH = "/home/user/mlops/artifact_registry/VERSION"
CHANGELOG_PATH = "/home/user/mlops/artifact_registry/CHANGELOG.md"

EXPECTED_VERSION_STR = "1.4.8"
EXPECTED_VERSION_FILE_CONTENT = "1.4.8\n"

EXPECTED_CHANGELOG_CONTENT = (
    "## [1.4.8] - 2024-11-15\n"
    "\n"
    "### Fixed\n"
    "- Preprocessing pipeline: reject NaN values during feature normalization step\n"
    "\n"
    "## [1.4.7] - 2024-11-02\n"
    "\n"
    "### Changed\n"
    "- Updated feature extraction to use 128-dim embeddings instead of 64-dim\n"
    "\n"
    "## [1.4.6] - 2024-10-18\n"
    "\n"
    "### Fixed\n"
    "- Corrected label encoding for multi-class targets"
)


def test_version_file_exists():
    assert os.path.isfile(VERSION_PATH), (
        f"VERSION file not found at '{VERSION_PATH}'. "
        "The file must exist after the task is completed."
    )


def test_version_file_exact_content():
    with open(VERSION_PATH, "r") as f:
        content = f.read()
    assert content == EXPECTED_VERSION_FILE_CONTENT, (
        f"VERSION file content is incorrect.\n"
        f"Expected: {EXPECTED_VERSION_FILE_CONTENT!r}\n"
        f"Got:      {content!r}\n"
        "The file must contain exactly '1.4.8' followed by a newline."
    )


def test_version_is_bumped_patch():
    with open(VERSION_PATH, "r") as f:
        content = f.read()
    version_str = content.strip()
    assert version_str == EXPECTED_VERSION_STR, (
        f"VERSION file contains '{version_str}', but expected '{EXPECTED_VERSION_STR}'. "
        "The patch version must be incremented from 1.4.7 to 1.4.8."
    )


def test_version_format():
    with open(VERSION_PATH, "r") as f:
        content = f.read()
    version_str = content.strip()
    parts = version_str.split(".")
    assert len(parts) == 3, (
        f"Version '{version_str}' does not follow MAJOR.MINOR.PATCH format. "
        "Expected exactly 3 dot-separated components."
    )
    for part in parts:
        assert part.isdigit(), (
            f"Version component '{part}' in '{version_str}' is not a valid integer. "
            "All version components must be non-negative integers."
        )
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    assert major == 1, f"Major version should be 1, got {major}."
    assert minor == 4, f"Minor version should be 4, got {minor}."
    assert patch == 8, f"Patch version should be 8 (bumped from 7), got {patch}."


def test_changelog_file_exists():
    assert os.path.isfile(CHANGELOG_PATH), (
        f"CHANGELOG.md not found at '{CHANGELOG_PATH}'. "
        "The file must exist after the task is completed."
    )


def test_changelog_starts_with_new_entry():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    assert content.startswith("## [1.4.8] - 2024-11-15"), (
        f"CHANGELOG.md must start with '## [1.4.8] - 2024-11-15', but got:\n{content[:200]}"
    )


def test_changelog_contains_new_fixed_entry():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    expected_entry = (
        "## [1.4.8] - 2024-11-15\n"
        "\n"
        "### Fixed\n"
        "- Preprocessing pipeline: reject NaN values during feature normalization step\n"
    )
    assert expected_entry in content, (
        f"CHANGELOG.md does not contain the expected new entry.\n"
        f"Expected to find:\n{expected_entry}\n"
        f"Actual content:\n{content}"
    )


def test_changelog_preserves_147_entry():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    assert "## [1.4.7] - 2024-11-02" in content, (
        "CHANGELOG.md must still contain the [1.4.7] entry from before the task."
    )
    assert "- Updated feature extraction to use 128-dim embeddings instead of 64-dim" in content, (
        "CHANGELOG.md must still contain the 128-dim embeddings change from the [1.4.7] entry."
    )


def test_changelog_preserves_146_entry():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    assert "## [1.4.6] - 2024-10-18" in content, (
        "CHANGELOG.md must still contain the [1.4.6] entry from before the task."
    )
    assert "- Corrected label encoding for multi-class targets" in content, (
        "CHANGELOG.md must still contain the label encoding fix from the [1.4.6] entry."
    )


def test_changelog_entry_order():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    pos_148 = content.find("## [1.4.8]")
    pos_147 = content.find("## [1.4.7]")
    pos_146 = content.find("## [1.4.6]")
    assert pos_148 != -1, "CHANGELOG.md must contain the [1.4.8] entry."
    assert pos_147 != -1, "CHANGELOG.md must contain the [1.4.7] entry."
    assert pos_146 != -1, "CHANGELOG.md must contain the [1.4.6] entry."
    assert pos_148 < pos_147, (
        f"[1.4.8] entry (pos {pos_148}) must appear before [1.4.7] entry (pos {pos_147}) "
        "in CHANGELOG.md."
    )
    assert pos_147 < pos_146, (
        f"[1.4.7] entry (pos {pos_147}) must appear before [1.4.6] entry (pos {pos_146}) "
        "in CHANGELOG.md."
    )


def test_changelog_blank_line_between_new_and_old():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    # After the new entry bullet point, there must be a blank line before the old content
    new_entry_end = (
        "- Preprocessing pipeline: reject NaN values during feature normalization step\n"
        "\n"
        "## [1.4.7]"
    )
    assert new_entry_end in content, (
        f"CHANGELOG.md must have a blank line between the new [1.4.8] entry and the "
        f"existing [1.4.7] entry.\n"
        f"Expected to find the sequence:\n{new_entry_end!r}\n"
        f"Actual content:\n{content}"
    )


def test_changelog_exact_content():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    stripped_content = content.strip()
    stripped_expected = EXPECTED_CHANGELOG_CONTENT.strip()
    assert stripped_content == stripped_expected, (
        f"CHANGELOG.md content does not exactly match the expected final state.\n"
        f"Expected (stripped):\n{stripped_expected}\n\n"
        f"Got (stripped):\n{stripped_content}"
    )


def test_changelog_no_extra_content_before_new_entry():
    with open(CHANGELOG_PATH, "r") as f:
        content = f.read()
    # The file should not have any content before the new entry header
    assert content.startswith("## [1.4.8]"), (
        f"CHANGELOG.md must start directly with '## [1.4.8]' with no preceding content. "
        f"Got:\n{content[:100]!r}"
    )


def test_artifact_registry_directory_exists():
    dir_path = "/home/user/mlops/artifact_registry"
    assert os.path.isdir(dir_path), (
        f"Directory '{dir_path}' does not exist. "
        "The artifact registry directory must be present."
    )