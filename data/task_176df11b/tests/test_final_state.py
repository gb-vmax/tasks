# test_final_state.py

import os
import pytest
from datetime import date

PROJECT_ROOT = "/home/user/db-backup-utility"
CONFIG_YAML = os.path.join(PROJECT_ROOT, "config.yaml")
CHANGELOG_MD = os.path.join(PROJECT_ROOT, "CHANGELOG.md")
README_MD = os.path.join(PROJECT_ROOT, "README.md")


def get_version_line_from_config(filepath):
    """Return the first non-empty, non-comment line containing 'version'."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped and not stripped.startswith("#") and "version" in stripped:
                    return stripped
    except Exception as e:
        pytest.fail(f"Could not open {filepath}: {e}")
    return None


def get_changelog_lines(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.readlines()
    except Exception as e:
        pytest.fail(f"Could not open {filepath}: {e}")


def get_console_output():
    """
    Return the console output produced by the student's script.
    This is a placeholder. In a real containerized grading scenario,
    the framework would capture stdout for verification.
    Here, we simulate by reading the files directly.
    """
    # Get version line from config.yaml
    version_line = None
    with open(CONFIG_YAML, "r", encoding="utf-8") as f:
        for line in f:
            if 'version' in line:
                version_line = line.rstrip('\n')
                break

    # Get entire changelog contents
    with open(CHANGELOG_MD, "r", encoding="utf-8") as f:
        changelog_content = f.read().rstrip('\n')

    return f"{version_line}\n{changelog_content}"


def test_project_directory_and_files_exist():
    assert os.path.isdir(PROJECT_ROOT), (
        f"Project directory {PROJECT_ROOT} does not exist. "
        "The backup utility project directory must be present."
    )
    for fn in (CONFIG_YAML, CHANGELOG_MD, README_MD):
        assert os.path.isfile(fn), (
            f"Required file {fn} does not exist after task completion."
        )


def test_config_yaml_version_bumped():
    """
    Ensure config.yaml has version: "2.4.0" as its version line (after the bump).
    """
    version_line = get_version_line_from_config(CONFIG_YAML)
    assert version_line is not None, (
        f"{CONFIG_YAML} does not contain a version line after task completion."
    )
    assert version_line == 'version: "2.4.0"', (
        f"config.yaml version not bumped correctly. "
        f"Expected 'version: \"2.4.0\"', found: {version_line!r}."
    )


def test_config_yaml_other_content_untouched():
    """
    Ensure the rest of config.yaml content remains unchanged except for the version bump.
    """
    expected = [
        'version: "2.4.0"\n',
        'backup:\n',
        '  path: "/var/backups"\n',
        '  schedule: "daily"\n',
    ]
    with open(CONFIG_YAML, "r", encoding="utf-8") as f:
        actual = f.readlines()
    assert actual == expected, (
        f"config.yaml content changed unexpectedly after the version bump.\n"
        f"Expected:\n{''.join(expected)}\n"
        f"Found:\n{''.join(actual)}"
    )


def test_changelog_new_entry_at_top():
    """
    Ensure CHANGELOG.md starts with the correct new entry, with today's date,
    and that all prior content is preserved below.
    """
    today = date.today().strftime("%Y-%m-%d")
    expected_new_block = [
        f"## [2.4.0] - {today}\n",
        "### Added\n",
        "- Implemented automatic backup retention checks with alerting (Reliability Improvement).\n",
        "\n",
    ]
    actual_lines = get_changelog_lines(CHANGELOG_MD)
    # Check that the first four lines match the required new block
    assert actual_lines[:4] == expected_new_block, (
        "CHANGELOG.md does not start with the correct new changelog entry.\n"
        f"Expected first 4 lines:\n{''.join(expected_new_block)}\n"
        f"Found:\n{''.join(actual_lines[:4])}"
    )


def test_changelog_prior_entries_preserved_and_ordered():
    """
    Ensure that all previous changelog content remains, and new block is at the very top.
    """
    today = date.today().strftime("%Y-%m-%d")
    expected_full = [
        f"## [2.4.0] - {today}\n",
        "### Added\n",
        "- Implemented automatic backup retention checks with alerting (Reliability Improvement).\n",
        "\n",
        "## [2.3.4] - 2024-05-19\n",
        "### Fixed\n",
        "- Restore job now handles missing file errors (Bugfix).\n",
        "\n",
        "## [2.3.0] - 2024-04-02\n",
        "### Added\n",
        "- Incremental backup mode introduced.\n",
        "- Settings for backup encryption.\n"
    ]
    actual_lines = get_changelog_lines(CHANGELOG_MD)
    assert actual_lines == expected_full, (
        "CHANGELOG.md content is not as expected after adding the new entry.\n"
        "Expected:\n" + ''.join(expected_full) +
        "\nFound:\n" + ''.join(actual_lines)
    )


def test_readme_md_untouched():
    """
    Ensure README.md content remains unchanged.
    """
    expected = [
        "DB Backup Utility\n",
        "=================\n",
        "Simple tool for managing PostgreSQL backups.\n"
    ]
    with open(README_MD, "r", encoding="utf-8") as f:
        actual = f.readlines()
    assert actual[:len(expected)] == expected, (
        f"README.md content was altered. Expected first {len(expected)} lines:\n"
        f"{''.join(expected)}\nFound:\n{''.join(actual[:len(expected)])}"
    )


def test_console_output_matches_files():
    """
    Ensure the console output matches the new version line and new CHANGELOG.md contents exactly.
    """
    # Simulate what should be printed
    today = date.today().strftime("%Y-%m-%d")
    expected_version_line = 'version: "2.4.0"'
    expected_changelog = (
        f"## [2.4.0] - {today}\n"
        "### Added\n"
        "- Implemented automatic backup retention checks with alerting (Reliability Improvement).\n"
        "\n"
        "## [2.3.4] - 2024-05-19\n"
        "### Fixed\n"
        "- Restore job now handles missing file errors (Bugfix).\n"
        "\n"
        "## [2.3.0] - 2024-04-02\n"
        "### Added\n"
        "- Incremental backup mode introduced.\n"
        "- Settings for backup encryption.\n"
    )
    expected_output = f"{expected_version_line}\n{expected_changelog.rstrip()}"
    actual_output = get_console_output().rstrip()
    assert actual_output == expected_output, (
        "Console output does not match the expected output after the task is completed.\n"
        f"Expected:\n{expected_output}\n\nFound:\n{actual_output}"
    )