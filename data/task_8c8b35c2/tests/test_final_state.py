# test_final_state.py

import os
import pytest

VERSION_FILE = "/home/user/accounttool/VERSION"
COMMITS_FILE = "/home/user/accounttool/COMMITS"
CHANGELOG_FILE = "/home/user/accounttool/CHANGELOG.md"

EXPECTED_VERSION = "3.2.0"

EXPECTED_CHANGELOG = (
    "## v3.1.6\n"
    "\n"
    "**Bug Fixes**\n"
    "- fix: resolve race condition in session cleanup\n"
    "\n"
    "**Other**\n"
    "- chore: bump lodash to 4.17.21\n"
    "\n"
    "## v3.2.0\n"
    "\n"
    "**Features**\n"
    "- feat: allow admins to reset user passwords in bulk\n"
    "\n"
    "**Bug Fixes**\n"
    "- fix: correct typo in account suspension email\n"
    "- fix: prevent login with expired tokens\n"
    "\n"
    "**Other**\n"
    "- chore: update dependency versions\n"
    "- docs: update API reference for user endpoints"
)


def test_version_file_exists():
    assert os.path.isfile(VERSION_FILE), (
        f"VERSION file does not exist at {VERSION_FILE}. "
        "The task requires this file to be present."
    )


def test_version_file_content():
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    # Must not have a trailing newline
    assert content == EXPECTED_VERSION, (
        f"VERSION file content is wrong.\n"
        f"Expected (no trailing newline): {EXPECTED_VERSION!r}\n"
        f"Actual: {content!r}\n"
        "The version should have been bumped from 3.1.7 to 3.2.0 (minor bump due to feat: commit)."
    )


def test_version_no_trailing_newline():
    with open(VERSION_FILE, "rb") as f:
        raw = f.read()
    assert not raw.endswith(b"\n"), (
        f"VERSION file must not have a trailing newline, but it does.\n"
        f"Raw bytes at end: {raw[-5:]!r}"
    )


def test_version_is_valid_semver():
    with open(VERSION_FILE, "r") as f:
        content = f.read().strip()
    parts = content.split(".")
    assert len(parts) == 3, (
        f"VERSION file '{content}' is not valid semver (expected X.Y.Z format)."
    )
    for part in parts:
        assert part.isdigit(), (
            f"VERSION file '{content}' — part '{part}' is not a valid integer."
        )


def test_version_major_unchanged():
    with open(VERSION_FILE, "r") as f:
        content = f.read().strip()
    parts = content.split(".")
    assert parts[0] == "3", (
        f"Major version should remain 3, but got '{parts[0]}'. "
        "No breaking changes were present in COMMITS."
    )


def test_version_minor_bumped():
    with open(VERSION_FILE, "r") as f:
        content = f.read().strip()
    parts = content.split(".")
    assert parts[1] == "2", (
        f"Minor version should be 2 (bumped from 1), but got '{parts[1]}'. "
        "A 'feat:' commit was present, requiring a minor bump."
    )


def test_version_patch_reset():
    with open(VERSION_FILE, "r") as f:
        content = f.read().strip()
    parts = content.split(".")
    assert parts[2] == "0", (
        f"Patch version should be reset to 0 after a minor bump, but got '{parts[2]}'."
    )


def test_changelog_file_exists():
    assert os.path.isfile(CHANGELOG_FILE), (
        f"CHANGELOG.md does not exist at {CHANGELOG_FILE}. "
        "The task requires this file to be present."
    )


def test_changelog_content_exact():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    # Strip trailing newline for comparison (task says no trailing newline in expected)
    content_stripped = content.rstrip("\n")
    assert content_stripped == EXPECTED_CHANGELOG, (
        f"CHANGELOG.md content does not match expected.\n"
        f"Expected:\n{EXPECTED_CHANGELOG!r}\n\n"
        f"Actual:\n{content_stripped!r}"
    )


def test_changelog_preserves_existing_content():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    existing_block = (
        "## v3.1.6\n"
        "\n"
        "**Bug Fixes**\n"
        "- fix: resolve race condition in session cleanup\n"
        "\n"
        "**Other**\n"
        "- chore: bump lodash to 4.17.21"
    )
    assert content.startswith(existing_block), (
        f"CHANGELOG.md does not start with the original content.\n"
        f"Expected start:\n{existing_block!r}\n\n"
        f"Actual start:\n{content[:len(existing_block)]!r}\n"
        "The existing content must not be modified."
    )


def test_changelog_new_version_header_present():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    assert "## v3.2.0" in content, (
        f"CHANGELOG.md does not contain '## v3.2.0' header.\n"
        "The new version entry must be appended."
    )


def test_changelog_features_section():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    assert "**Features**\n- feat: allow admins to reset user passwords in bulk" in content, (
        "CHANGELOG.md is missing the Features section with the expected commit.\n"
        "Expected: '**Features**\\n- feat: allow admins to reset user passwords in bulk'"
    )


def test_changelog_bug_fixes_section():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    expected_bug_fixes = (
        "**Bug Fixes**\n"
        "- fix: correct typo in account suspension email\n"
        "- fix: prevent login with expired tokens"
    )
    assert expected_bug_fixes in content, (
        f"CHANGELOG.md is missing or has incorrect Bug Fixes section.\n"
        f"Expected to find:\n{expected_bug_fixes!r}\n"
        f"In content:\n{content!r}"
    )


def test_changelog_other_section():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    # Find the new version block
    new_version_idx = content.find("## v3.2.0")
    assert new_version_idx != -1, "## v3.2.0 not found in CHANGELOG.md"
    new_block = content[new_version_idx:]
    expected_other = (
        "**Other**\n"
        "- chore: update dependency versions\n"
        "- docs: update API reference for user endpoints"
    )
    assert expected_other in new_block, (
        f"CHANGELOG.md new entry is missing or has incorrect Other section.\n"
        f"Expected to find:\n{expected_other!r}\n"
        f"In new block:\n{new_block!r}"
    )


def test_changelog_no_breaking_changes_section():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    new_version_idx = content.find("## v3.2.0")
    assert new_version_idx != -1, "## v3.2.0 not found in CHANGELOG.md"
    new_block = content[new_version_idx:]
    assert "**Breaking Changes**" not in new_block, (
        "CHANGELOG.md new entry contains a 'Breaking Changes' section, "
        "but there were no breaking changes in COMMITS."
    )


def test_changelog_blank_line_before_new_entry():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    # The new entry should be preceded by a blank line after existing content
    assert "\n\n## v3.2.0" in content, (
        "CHANGELOG.md does not have a blank line before the new '## v3.2.0' entry.\n"
        "The new entry must be separated from existing content by a blank line."
    )


def test_changelog_section_order_in_new_entry():
    with open(CHANGELOG_FILE, "r") as f:
        content = f.read()
    new_version_idx = content.find("## v3.2.0")
    assert new_version_idx != -1, "## v3.2.0 not found in CHANGELOG.md"
    new_block = content[new_version_idx:]

    features_idx = new_block.find("**Features**")
    bug_fixes_idx = new_block.find("**Bug Fixes**")
    other_idx = new_block.find("**Other**")

    assert features_idx != -1, "**Features** section not found in new changelog entry."
    assert bug_fixes_idx != -1, "**Bug Fixes** section not found in new changelog entry."
    assert other_idx != -1, "**Other** section not found in new changelog entry."

    assert features_idx < bug_fixes_idx, (
        "**Features** section must appear before **Bug Fixes** section in the new entry."
    )
    assert bug_fixes_idx < other_idx, (
        "**Bug Fixes** section must appear before **Other** section in the new entry."
    )


def test_commits_file_unchanged():
    """COMMITS file should not be modified by the task."""
    expected_lines = [
        "feat: allow admins to reset user passwords in bulk",
        "fix: correct typo in account suspension email",
        "chore: update dependency versions",
        "fix: prevent login with expired tokens",
        "docs: update API reference for user endpoints",
    ]
    with open(COMMITS_FILE, "r") as f:
        content = f.read()
    actual_lines = [line for line in content.splitlines() if line.strip()]
    assert actual_lines == expected_lines, (
        f"COMMITS file was unexpectedly modified.\n"
        f"Expected lines: {expected_lines}\n"
        f"Actual lines: {actual_lines}"
    )