# test_final_state.py
"""
Pytest suite to validate the final state of the OS/container after the
server provisioning directory structure and report task is completed.

This test checks:
- Directory and file existence
- File contents (single line, exact content)
- Relative symlink existence and correctness
- Report file correctness (content, order, formatting)
"""

import os
import pytest

HOME = "/home/user"
PROVISIONING = os.path.join(HOME, "provisioning")
CONFIGS = os.path.join(PROVISIONING, "configs")
ACTIVE = os.path.join(PROVISIONING, "active")
REPORT = os.path.join(PROVISIONING, "symlink_report.txt")

CONFIG_FILES = [
    ("web.conf", "WEB.CONF"),
    ("db.conf", "DB.CONF"),
    ("cache.conf", "CACHE.CONF"),
]

SYMLINKS = [
    ("web_active.conf", "../configs/web.conf", "WEB.CONF"),
    ("db_active.conf", "../configs/db.conf", "DB.CONF"),
    ("cache_active.conf", "../configs/cache.conf", "CACHE.CONF"),
]


def abs_config_file(filename):
    return os.path.join(CONFIGS, filename)


def abs_symlink_file(symlink_name):
    return os.path.join(ACTIVE, symlink_name)


@pytest.mark.describe("Final provisioning directory structure and report")
class TestFinalProvisioning:

    def test_configs_directory_exists(self):
        assert os.path.isdir(CONFIGS), (
            f"Directory missing: {CONFIGS}. You must create it."
        )

    @pytest.mark.parametrize("filename,expected_content", CONFIG_FILES)
    def test_config_file_exists_and_content(self, filename, expected_content):
        file_path = abs_config_file(filename)
        assert os.path.isfile(file_path), (
            f"Missing config file: {file_path}"
        )
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        assert len(lines) == 1, (
            f"{file_path} should contain exactly one line, but contains {len(lines)} lines."
        )
        content = lines[0].rstrip('\n')
        assert content == expected_content, (
            f"{file_path} should contain exactly '{expected_content}', but found '{content}'."
        )
        assert lines[0].endswith('\n') or lines[0] == content, (
            f"{file_path} must not have trailing whitespace or extra blank lines."
        )

    def test_active_directory_exists(self):
        assert os.path.isdir(ACTIVE), (
            f"Directory missing: {ACTIVE}. You must create it."
        )

    @pytest.mark.parametrize("symlink_name,relative_target,expected_content", SYMLINKS)
    def test_symlink_exists_and_properties(self, symlink_name, relative_target, expected_content):
        symlink_path = abs_symlink_file(symlink_name)
        assert os.path.islink(symlink_path), (
            f"Missing symlink: {symlink_path}. You must create it."
        )
        link_target = os.readlink(symlink_path)
        assert link_target == relative_target, (
            f"Symlink {symlink_path} should point to '{relative_target}', but points to '{link_target}'."
        )
        assert not os.path.isabs(link_target), (
            f"Symlink {symlink_path} must be relative, but points to absolute path '{link_target}'."
        )
        assert link_target.startswith("../"), (
            f"Symlink {symlink_path} must be a relative path starting with '../', but points to '{link_target}'."
        )
        # Check that the resolved path points to the correct config file
        resolved_target = os.path.realpath(symlink_path)
        expected_file = os.path.realpath(os.path.join(ACTIVE, relative_target))
        assert resolved_target == expected_file, (
            f"Symlink {symlink_path} resolves to {resolved_target}, expected {expected_file}."
        )
        # The target file must exist and have correct content
        assert os.path.isfile(resolved_target), (
            f"Symlink {symlink_path} points to non-existent file: {resolved_target}"
        )
        with open(resolved_target, "r", encoding="utf-8") as f:
            lines = f.readlines()
        assert len(lines) == 1, (
            f"Target file {resolved_target} should contain exactly one line, but contains {len(lines)}."
        )
        content = lines[0].rstrip('\n')
        assert content == expected_content, (
            f"Target file {resolved_target} should contain '{expected_content}', but found '{content}'."
        )

    def test_symlink_report_exists_and_content(self):
        assert os.path.isfile(REPORT), (
            f"Missing report file: {REPORT}. You must create it."
        )
        with open(REPORT, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Remove any trailing newlines and blank lines
        stripped_lines = [line.rstrip('\n') for line in lines if line.strip() != ""]
        assert len(stripped_lines) == 3, (
            f"{REPORT} must contain exactly three non-blank lines, found {len(stripped_lines)}."
        )
        expected_lines = [
            f"{symlink_name},{relative_target},{expected_content}"
            for (symlink_name, relative_target, expected_content) in SYMLINKS
        ]
        for idx, (expected, actual) in enumerate(zip(expected_lines, stripped_lines)):
            assert actual == expected, (
                f"Line {idx+1} of {REPORT} is incorrect.\nExpected: '{expected}'\nFound:    '{actual}'"
            )
        # Check for no extra blank lines or trailing whitespace
        assert lines[-1].endswith('\n'), (
            f"{REPORT} must end with a single newline at the end of the last line."
        )
        for i, line in enumerate(stripped_lines):
            assert line.strip() == line, (
                f"Line {i+1} of {REPORT} has leading or trailing whitespace: '{line}'"
            )