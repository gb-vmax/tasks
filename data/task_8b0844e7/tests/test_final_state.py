# test_final_state.py

import os
import pytest

# Paths
VERSIONS_DIR = "/home/user/configs/versions"
ACTIVE_DIR = "/home/user/configs/active"
V1_FILE = "/home/user/configs/versions/nginx.conf.v1"
V2_FILE = "/home/user/configs/versions/nginx.conf.v2"
ACTIVE_SYMLINK = "/home/user/configs/active/nginx.conf"
PROVISION_LOG = "/home/user/configs/provision.log"


def test_versions_directory_still_exists():
    assert os.path.isdir(VERSIONS_DIR), (
        f"Versions directory '{VERSIONS_DIR}' does not exist. "
        "It should not have been removed."
    )


def test_v1_file_still_exists():
    assert os.path.isfile(V1_FILE), (
        f"Versioned config file '{V1_FILE}' does not exist. "
        "The old version file should not have been removed."
    )


def test_v2_file_still_exists():
    assert os.path.isfile(V2_FILE), (
        f"Versioned config file '{V2_FILE}' does not exist. "
        "The new version file should still be present."
    )


def test_active_directory_still_exists():
    assert os.path.isdir(ACTIVE_DIR), (
        f"Active directory '{ACTIVE_DIR}' does not exist. "
        "It should not have been removed."
    )


def test_active_symlink_exists():
    assert os.path.islink(ACTIVE_SYMLINK), (
        f"'{ACTIVE_SYMLINK}' does not exist or is not a symlink. "
        "The symlink must exist after the update."
    )


def test_active_symlink_points_to_v2():
    target = os.readlink(ACTIVE_SYMLINK)
    assert target == V2_FILE, (
        f"Symlink '{ACTIVE_SYMLINK}' should point to '{V2_FILE}', "
        f"but currently points to '{target}'. "
        "The symlink must be updated to point to the v2 config file."
    )


def test_active_symlink_is_absolute():
    target = os.readlink(ACTIVE_SYMLINK)
    assert os.path.isabs(target), (
        f"Symlink '{ACTIVE_SYMLINK}' target '{target}' is not an absolute path. "
        "The symlink must use an absolute path target."
    )


def test_active_symlink_does_not_point_to_v1():
    target = os.readlink(ACTIVE_SYMLINK)
    assert target != V1_FILE, (
        f"Symlink '{ACTIVE_SYMLINK}' still points to the old version '{V1_FILE}'. "
        "The symlink must be updated to point to v2."
    )


def test_only_one_nginx_conf_in_active():
    entries = os.listdir(ACTIVE_DIR)
    nginx_entries = [e for e in entries if e == "nginx.conf"]
    assert len(nginx_entries) == 1, (
        f"Expected exactly one 'nginx.conf' entry in '{ACTIVE_DIR}', "
        f"found {len(nginx_entries)}: {nginx_entries}. "
        "There should be only one symlink named 'nginx.conf' in the active directory."
    )


def test_symlink_target_is_accessible():
    assert os.path.exists(ACTIVE_SYMLINK), (
        f"The symlink '{ACTIVE_SYMLINK}' exists but its target is not accessible. "
        f"Target '{os.readlink(ACTIVE_SYMLINK)}' may be broken."
    )


def test_provision_log_exists():
    assert os.path.exists(PROVISION_LOG), (
        f"Provision log '{PROVISION_LOG}' does not exist. "
        "A log entry must be written after updating the symlink."
    )


def test_provision_log_is_a_file():
    assert os.path.isfile(PROVISION_LOG), (
        f"'{PROVISION_LOG}' exists but is not a regular file."
    )


def test_provision_log_exact_contents():
    expected = "nginx.conf -> /home/user/configs/versions/nginx.conf.v2\n"
    with open(PROVISION_LOG, "r") as f:
        contents = f.read()
    assert contents == expected, (
        f"'{PROVISION_LOG}' has unexpected contents.\n"
        f"Expected: {expected!r}\n"
        f"Actual:   {contents!r}\n"
        "The log must contain exactly one line in the format: "
        "'nginx.conf -> /home/user/configs/versions/nginx.conf.v2\\n'"
    )


def test_provision_log_single_line():
    with open(PROVISION_LOG, "r") as f:
        contents = f.read()
    lines = contents.splitlines()
    assert len(lines) == 1, (
        f"'{PROVISION_LOG}' should contain exactly one line, "
        f"but found {len(lines)} lines. Contents: {contents!r}"
    )


def test_provision_log_correct_format():
    with open(PROVISION_LOG, "r") as f:
        contents = f.read()
    line = contents.rstrip("\n")
    expected_line = "nginx.conf -> /home/user/configs/versions/nginx.conf.v2"
    assert line == expected_line, (
        f"The line in '{PROVISION_LOG}' does not match the expected format.\n"
        f"Expected: {expected_line!r}\n"
        f"Actual:   {line!r}\n"
        "Format must be: 'nginx.conf -> /home/user/configs/versions/nginx.conf.v2'"
    )


def test_provision_log_ends_with_newline():
    with open(PROVISION_LOG, "rb") as f:
        contents = f.read()
    assert contents.endswith(b"\n"), (
        f"'{PROVISION_LOG}' does not end with a newline character. "
        f"File contents (bytes): {contents!r}"
    )


def test_provision_log_no_trailing_extra_newlines():
    with open(PROVISION_LOG, "r") as f:
        contents = f.read()
    # Should end with exactly one newline
    assert not contents.endswith("\n\n"), (
        f"'{PROVISION_LOG}' ends with more than one newline. "
        f"Contents: {contents!r}"
    )