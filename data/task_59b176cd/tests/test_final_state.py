# test_final_state.py

import os
import pytest

OPERATOR_DIR = "/home/user/operator"
VERSION_FILE = os.path.join(OPERATOR_DIR, "VERSION")
PENDING_COMMITS_FILE = os.path.join(OPERATOR_DIR, "pending_commits.txt")
CHANGELOG_FILE = os.path.join(OPERATOR_DIR, "CHANGELOG.md")

EXPECTED_NEW_VERSION = "1.4.0"

EXPECTED_VERSION_CONTENTS = "1.4.0"  # no trailing newline

EXPECTED_CHANGELOG_CONTENTS = (
    "## [1.4.0] - 2024-11-15\n"
    "\n"
    "### Changed\n"
    "- feat: add leader election support\n"
    "- fix: handle nil pointer in reconcile loop\n"
    "- fix: correct RBAC permissions for CRD watcher\n"
    "- feat: support multi-namespace watch mode\n"
    "\n"
    "---\n"
    "## [1.3.2] - 2024-10-20\n"
    "\n"
    "### Changed\n"
    "- fix: retry on transient API errors\n"
    "- fix: bump controller-runtime to v0.16.1\n"
    "\n"
    "---\n"
    "## [1.3.1] - 2024-09-14\n"
    "\n"
    "### Changed\n"
    "- fix: correct status subresource patch logic\n"
    "\n"
    "---\n"
    "## [1.3.0] - 2024-09-01\n"
    "\n"
    "### Changed\n"
    "- feat: add finalizer support for cleanup on deletion\n"
    "- fix: resolve race condition in cache sync\n"
    "\n"
    "---\n"
)


def test_operator_directory_exists():
    assert os.path.isdir(OPERATOR_DIR), (
        f"Operator directory {OPERATOR_DIR} does not exist."
    )


def test_version_file_exists():
    assert os.path.isfile(VERSION_FILE), (
        f"VERSION file {VERSION_FILE} does not exist."
    )


def test_version_file_contains_new_version_exactly():
    with open(VERSION_FILE, "r") as f:
        contents = f.read()
    assert contents == EXPECTED_VERSION_CONTENTS, (
        f"VERSION file must contain exactly '{EXPECTED_VERSION_CONTENTS}' (no trailing newline, no extra whitespace).\n"
        f"Got: {repr(contents)}"
    )


def test_version_is_1_4_0():
    with open(VERSION_FILE, "r") as f:
        version = f.read().strip()
    assert version == "1.4.0", (
        f"Expected version '1.4.0' after minor bump from '1.3.2', but got: {repr(version)}.\n"
        "Check that the bump logic correctly identifies 'feat:' commits and bumps the minor version."
    )


def test_version_has_no_trailing_newline():
    with open(VERSION_FILE, "rb") as f:
        raw = f.read()
    assert not raw.endswith(b"\n"), (
        f"VERSION file must NOT have a trailing newline. Raw bytes: {repr(raw)}"
    )


def test_version_is_semantic():
    with open(VERSION_FILE, "r") as f:
        version = f.read().strip()
    parts = version.split(".")
    assert len(parts) == 3, (
        f"VERSION must be in 'major.minor.patch' format, got: {repr(version)}"
    )
    for part in parts:
        assert part.isdigit(), (
            f"Each part of the version must be numeric, got: {repr(part)} in {repr(version)}"
        )


def test_version_major_unchanged():
    with open(VERSION_FILE, "r") as f:
        version = f.read().strip()
    major = version.split(".")[0]
    assert major == "1", (
        f"Major version should remain '1' (no breaking commits), got: {repr(major)}"
    )


def test_version_minor_bumped():
    with open(VERSION_FILE, "r") as f:
        version = f.read().strip()
    minor = version.split(".")[1]
    assert minor == "4", (
        f"Minor version should be bumped to '4' (was '3', feat: commits present), got: {repr(minor)}"
    )


def test_version_patch_reset_to_zero():
    with open(VERSION_FILE, "r") as f:
        version = f.read().strip()
    patch = version.split(".")[2]
    assert patch == "0", (
        f"Patch version should be reset to '0' when minor is bumped, got: {repr(patch)}"
    )


def test_changelog_file_exists():
    assert os.path.isfile(CHANGELOG_FILE), (
        f"CHANGELOG.md file {CHANGELOG_FILE} does not exist."
    )


def test_changelog_contents_exact():
    with open(CHANGELOG_FILE, "r") as f:
        contents = f.read()
    assert contents == EXPECTED_CHANGELOG_CONTENTS, (
        f"CHANGELOG.md does not match the expected content.\n\n"
        f"Expected:\n{repr(EXPECTED_CHANGELOG_CONTENTS)}\n\n"
        f"Got:\n{repr(contents)}"
    )


def test_changelog_starts_with_new_version_header():
    with open(CHANGELOG_FILE, "r") as f:
        contents = f.read()
    expected_header = "## [1.4.0] - 2024-11-15"
    assert contents.startswith(expected_header), (
        f"CHANGELOG.md must start with '{expected_header}'.\n"
        f"Actual start: {repr(contents[:80])}"
    )


def test_changelog_new_entry_date_is_correct():
    with open(CHANGELOG_FILE, "r") as f:
        first_line = f.readline().strip()
    assert "2024-11-15" in first_line, (
        f"The new changelog entry must use date '2024-11-15', but first line is: {repr(first_line)}"
    )


def test_changelog_new_entry_has_changed_section():
    with open(CHANGELOG_FILE, "r") as f:
        contents = f.read()
    # The new entry should contain "### Changed" before the first "---"
    first_separator = contents.index("---")
    new_entry = contents[:first_separator]
    assert "### Changed\n" in new_entry, (
        f"New changelog entry must contain '### Changed' section.\n"
        f"New entry portion:\n{repr(new_entry)}"
    )


def test_changelog_new_entry_contains_all_commits():
    expected_commits = [
        "- feat: add leader election support",
        "- fix: handle nil pointer in reconcile loop",
        "- fix: correct RBAC permissions for CRD watcher",
        "- feat: support multi-namespace watch mode",
    ]
    with open(CHANGELOG_FILE, "r") as f:
        contents = f.read()
    # Only check within the new entry (before first ---)
    first_separator_idx = contents.index("---")
    new_entry = contents[:first_separator_idx]
    for commit_line in expected_commits:
        assert commit_line in new_entry, (
            f"Expected commit line '{commit_line}' not found in new changelog entry.\n"
            f"New entry:\n{new_entry}"
        )


def test_changelog_commits_in_correct_order():
    with open(CHANGELOG_FILE, "r") as f:
        contents = f.read()
    first_separator_idx = contents.index("---")
    new_entry = contents[:first_separator_idx]

    commit_lines = [
        "- feat: add leader election support",
        "- fix: handle nil pointer in reconcile loop",
        "- fix: correct RBAC permissions for CRD watcher",
        "- feat: support multi-namespace watch mode",
    ]
    positions = []
    for line in commit_lines:
        idx = new_entry.find(line)
        assert idx != -1, (
            f"Commit line '{line}' not found in new changelog entry."
        )
        positions.append(idx)

    assert positions == sorted(positions), (
        f"Commit lines are not in the correct order in the new changelog entry.\n"
        f"Expected order: {commit_lines}\n"
        f"Positions found: {positions}"
    )


def test_changelog_old_content_preserved():
    with open(CHANGELOG_FILE, "r") as f:
        contents = f.read()
    old_entries = [
        "## [1.3.2] - 2024-10-20",
        "## [1.3.1] - 2024-09-14",
        "## [1.3.0] - 2024-09-01",
        "- fix: retry on transient API errors",
        "- fix: bump controller-runtime to v0.16.1",
        "- fix: correct status subresource patch logic",
        "- feat: add finalizer support for cleanup on deletion",
        "- fix: resolve race condition in cache sync",
    ]
    for entry in old_entries:
        assert entry in contents, (
            f"Old changelog content '{entry}' is missing from CHANGELOG.md.\n"
            f"The old content must be preserved after the new entry."
        )


def test_changelog_old_content_comes_after_new_entry():
    with open(CHANGELOG_FILE, "r") as f:
        contents = f.read()
    new_entry_idx = contents.index("## [1.4.0]")
    old_entry_idx = contents.index("## [1.3.2]")
    assert new_entry_idx < old_entry_idx, (
        f"New entry for 1.4.0 must appear before old entry for 1.3.2.\n"
        f"New entry position: {new_entry_idx}, Old entry position: {old_entry_idx}"
    )


def test_changelog_separator_between_new_and_old():
    with open(CHANGELOG_FILE, "r") as f:
        contents = f.read()
    # After the new entry's commit list, there should be a "---" separator before old content
    new_entry_end = contents.index("---\n")
    old_content_start = contents.index("## [1.3.2]")
    assert new_entry_end < old_content_start, (
        f"The '---' separator must appear between the new entry and the old content.\n"
        f"Separator position: {new_entry_end}, Old content position: {old_content_start}"
    )


def test_no_extra_files_created():
    """Ensure only VERSION and CHANGELOG.md were modified; no extra files were created."""
    expected_files = {"VERSION", "pending_commits.txt", "CHANGELOG.md"}
    actual_files = set(os.listdir(OPERATOR_DIR))
    extra_files = actual_files - expected_files
    assert not extra_files, (
        f"Unexpected extra files found in {OPERATOR_DIR}: {extra_files}\n"
        "The task should only modify VERSION and CHANGELOG.md, not create new files."
    )


def test_pending_commits_file_unchanged():
    """The pending_commits.txt file should not be modified."""
    expected_contents = (
        "feat: add leader election support\n"
        "fix: handle nil pointer in reconcile loop\n"
        "fix: correct RBAC permissions for CRD watcher\n"
        "feat: support multi-namespace watch mode\n"
    )
    with open(PENDING_COMMITS_FILE, "r") as f:
        contents = f.read()
    assert contents == expected_contents, (
        f"pending_commits.txt should not have been modified.\n"
        f"Expected:\n{repr(expected_contents)}\n\nGot:\n{repr(contents)}"
    )