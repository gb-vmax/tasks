# test_final_state.py

import os
import stat
import subprocess
import pytest

DASHBOARDS_DIR = "/home/user/dashboards"
FILES = [
    "grafana_main.json",
    "alerts_config.json",
    "datasources.cfg",
]
FILE_PATHS = [os.path.join(DASHBOARDS_DIR, f) for f in FILES]

EXPECTED_CONTENTS = {
    "grafana_main.json": '{"title": "Main Dashboard", "panels": []}',
    "alerts_config.json": '{"alerts": [], "routes": []}',
    "datasources.cfg": "[datasource]\nhost=localhost\nport=5432",
}

EXPECTED_MODE = 0o640
EXPECTED_OWNER = "user"
EXPECTED_GROUP = "observer"


def test_dashboards_directory_exists():
    assert os.path.isdir(DASHBOARDS_DIR), (
        f"Directory '{DASHBOARDS_DIR}' does not exist."
    )


def test_observer_group_exists():
    result = subprocess.run(
        ["getent", "group", "observer"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        "Group 'observer' does not exist on the system. "
        f"stderr: {result.stderr}"
    )


@pytest.mark.parametrize("filepath", FILE_PATHS)
def test_file_exists(filepath):
    assert os.path.isfile(filepath), (
        f"File '{filepath}' does not exist. It must be present."
    )


@pytest.mark.parametrize("filename", FILES)
def test_file_permissions_are_640(filename):
    filepath = os.path.join(DASHBOARDS_DIR, filename)
    file_stat = os.stat(filepath)
    mode = stat.S_IMODE(file_stat.st_mode)
    assert mode == EXPECTED_MODE, (
        f"File '{filepath}' has incorrect permissions.\n"
        f"Expected: {oct(EXPECTED_MODE)} (rw-r-----)\n"
        f"Got:      {oct(mode)}\n"
        "Run: chmod 640 " + filepath
    )


@pytest.mark.parametrize("filename", FILES)
def test_file_owner_is_user(filename):
    filepath = os.path.join(DASHBOARDS_DIR, filename)
    result = subprocess.run(
        ["stat", "-c", "%U", filepath],
        capture_output=True, text=True, check=True
    )
    owner = result.stdout.strip()
    assert owner == EXPECTED_OWNER, (
        f"File '{filepath}' has incorrect owner.\n"
        f"Expected: '{EXPECTED_OWNER}'\n"
        f"Got:      '{owner}'\n"
        "Run: chown user " + filepath
    )


@pytest.mark.parametrize("filename", FILES)
def test_file_group_is_observer(filename):
    filepath = os.path.join(DASHBOARDS_DIR, filename)
    result = subprocess.run(
        ["stat", "-c", "%G", filepath],
        capture_output=True, text=True, check=True
    )
    group = result.stdout.strip()
    assert group == EXPECTED_GROUP, (
        f"File '{filepath}' has incorrect group ownership.\n"
        f"Expected: '{EXPECTED_GROUP}'\n"
        f"Got:      '{group}'\n"
        "Run: chgrp observer " + filepath
    )


@pytest.mark.parametrize("filename", FILES)
def test_file_permission_string(filename):
    """Verify the ls -l permission string is exactly '-rw-r-----'."""
    filepath = os.path.join(DASHBOARDS_DIR, filename)
    result = subprocess.run(
        ["ls", "-l", filepath],
        capture_output=True, text=True, check=True
    )
    output = result.stdout.strip()
    # The first field in ls -l output is the permission string
    permission_string = output.split()[0]
    assert permission_string == "-rw-r-----", (
        f"File '{filepath}' has incorrect permission string in ls -l output.\n"
        f"Expected: '-rw-r-----'\n"
        f"Got:      '{permission_string}'\n"
        f"Full ls -l output: {output}"
    )


@pytest.mark.parametrize("filename,expected_content", EXPECTED_CONTENTS.items())
def test_file_content_unchanged(filename, expected_content):
    """Ensure file contents were not modified during permission changes."""
    filepath = os.path.join(DASHBOARDS_DIR, filename)
    with open(filepath, "r") as f:
        content = f.read().rstrip("\n")
    assert content == expected_content, (
        f"File '{filepath}' has unexpected content (it should not have been modified).\n"
        f"Expected: {expected_content!r}\n"
        f"Got:      {content!r}"
    )


def test_ls_l_output_matches_expected():
    """Verify the full ls -l output of the dashboards directory matches expected format."""
    result = subprocess.run(
        ["ls", "-l", DASHBOARDS_DIR],
        capture_output=True, text=True, check=True
    )
    output = result.stdout.strip()
    lines = output.splitlines()

    # Filter out the 'total' line
    file_lines = [line for line in lines if not line.startswith("total")]

    assert len(file_lines) == 3, (
        f"Expected exactly 3 files in '{DASHBOARDS_DIR}', "
        f"but found {len(file_lines)}.\n"
        f"ls -l output:\n{output}"
    )

    expected_files_sorted = sorted(FILES)
    for i, (line, expected_filename) in enumerate(zip(file_lines, expected_files_sorted)):
        parts = line.split()
        assert len(parts) >= 9, (
            f"Unexpected ls -l line format: '{line}'"
        )
        perm_str = parts[0]
        owner = parts[2]
        group = parts[3]
        filename = parts[-1]

        assert perm_str == "-rw-r-----", (
            f"File '{expected_filename}' has wrong permission string.\n"
            f"Expected: '-rw-r-----'\n"
            f"Got:      '{perm_str}'\n"
            f"Line: {line}"
        )
        assert owner == "user", (
            f"File '{expected_filename}' has wrong owner.\n"
            f"Expected: 'user'\n"
            f"Got:      '{owner}'\n"
            f"Line: {line}"
        )
        assert group == "observer", (
            f"File '{expected_filename}' has wrong group.\n"
            f"Expected: 'observer'\n"
            f"Got:      '{group}'\n"
            f"Line: {line}"
        )
        assert filename == expected_filename, (
            f"Unexpected filename at position {i}.\n"
            f"Expected: '{expected_filename}'\n"
            f"Got:      '{filename}'\n"
            f"Line: {line}"
        )