# test_final_state.py

import os
import pytest

BASE = "/home/user/projects/resmon"

def fullpath(*args):
    return os.path.join(BASE, *args)

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def test_version_file_updated():
    version_path = fullpath("resmon", "version.txt")
    assert os.path.isfile(version_path), (
        f"File '{version_path}' is missing. "
        "The version file must exist after the task."
    )
    content = read_file(version_path)
    expected = "1.5.0\n"
    assert content == expected, (
        f"File '{version_path}' has incorrect content.\n"
        f"Expected:\n{expected!r}\n"
        f"Found:\n{content!r}\n"
        "The version must be bumped to exactly '1.5.0' and no extra lines or whitespace."
    )

def test_changelog_content_final():
    changelog_path = fullpath("CHANGELOG.md")
    assert os.path.isfile(changelog_path), (
        f"File '{changelog_path}' is missing. "
        "The changelog must exist after the task."
    )
    content = read_file(changelog_path)
    expected = (
        "## [1.5.0] - 2024-06-02\n"
        "- Added disk I/O statistics collection to the monitoring tool.\n"
        "\n"
        "## [1.4.2] - 2024-06-01\n"
        "- Improved resource usage reporting accuracy.\n"
    )
    assert content == expected, (
        f"File '{changelog_path}' is not in the correct post-task state.\n"
        f"Expected:\n{expected!r}\n"
        f"Found:\n{content!r}\n"
        "Check that:\n"
        "- The section for 1.5.0 is at the top, with today's date (2024-06-02), and the correct entry.\n"
        "- The previous 1.4.2 section is present and unchanged, below.\n"
        "- There are no [Unreleased] sections or extra whitespace.\n"
    )

def test_release_log_created_and_correct():
    release_log_path = fullpath("reports", "release_2024-06-02.log")
    assert os.path.isfile(release_log_path), (
        f"File '{release_log_path}' is missing. "
        "The release log for 2024-06-02 must be created."
    )
    content = read_file(release_log_path)
    expected = (
        "1.5.0\n"
        "- Added disk I/O statistics collection to the monitoring tool.\n"
        "Disk I/O statistics monitoring is now available as part of the resource usage tool.\n"
    )
    assert content == expected, (
        f"File '{release_log_path}' has incorrect content.\n"
        f"Expected:\n{expected!r}\n"
        f"Found:\n{content!r}\n"
        "Release log must have exactly:\n"
        "1. The new version ('1.5.0')\n"
        "2. The changelog entry (verbatim)\n"
        "3. The summary sentence\n"
        "Each on its own line, with no extra lines, comments, or whitespace."
    )

def test_usage_report_unchanged():
    usage_path = fullpath("reports", "usage_2024-06-01.csv")
    assert os.path.isfile(usage_path), (
        f"File '{usage_path}' is missing. "
        "The previous usage report must not be modified or removed."
    )
    expected = (
        "resource,cpu_usage,mem_usage\n"
        "web01,45,78\n"
        "db01,67,85\n"
        "api01,55,72\n"
    )
    content = read_file(usage_path)
    assert content == expected, (
        f"File '{usage_path}' was changed, but it must be left untouched.\n"
        f"Expected:\n{expected!r}\n"
        f"Found:\n{content!r}\n"
        "Ensure the resource usage report remains exactly as it was before the task."
    )

def test_no_unreleased_section_in_changelog():
    changelog_path = fullpath("CHANGELOG.md")
    content = read_file(changelog_path)
    assert "Unreleased" not in content, (
        f"File '{changelog_path}' should not contain an [Unreleased] section after the release.\n"
        "All entries must be moved under the correct version section."
    )

def test_no_extra_files_or_dirs():
    """Ensure no extra files or directories were created in resmon base directory or subdirs."""
    # Expected files and dirs in BASE
    expected_base = {"CHANGELOG.md", "reports", "resmon"}
    found_base = set(os.listdir(BASE))
    assert found_base == expected_base, (
        f"Unexpected files or directories found in '{BASE}'.\n"
        f"Expected: {expected_base}\n"
        f"Found: {found_base}\n"
        "Do not create extra files or folders in the project root."
    )

    # Expected files in reports
    expected_reports = {"usage_2024-06-01.csv", "release_2024-06-02.log"}
    found_reports = set(os.listdir(fullpath("reports")))
    assert found_reports == expected_reports, (
        f"Unexpected files in '{fullpath('reports')}'.\n"
        f"Expected: {expected_reports}\n"
        f"Found: {found_reports}\n"
        "Only the two report files should be present."
    )

    # Expected files in resmon subdir
    expected_resmon = {"version.txt"}
    found_resmon = set(os.listdir(fullpath("resmon")))
    assert found_resmon == expected_resmon, (
        f"Unexpected files in '{fullpath('resmon')}'.\n"
        f"Expected: {expected_resmon}\n"
        f"Found: {found_resmon}\n"
        "Only the version.txt file should be present in 'resmon' subdirectory."
    )