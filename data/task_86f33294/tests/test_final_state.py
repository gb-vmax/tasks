# test_final_state.py

import os
import pytest

DEPLOYMENTS_DIR = "/home/user/deployments"
RELEASES_DIR = "/home/user/deployments/releases"
V231_DIR = "/home/user/deployments/releases/v2.3.1"
V240_DIR = "/home/user/deployments/releases/v2.4.0"
CURRENT_SYMLINK = "/home/user/deployments/current"
PREVIOUS_SYMLINK = "/home/user/deployments/previous"
DEPLOY_LOG = "/home/user/deployments/deploy_log.txt"

EXPECTED_LOG_CONTENTS = (
    "current -> /home/user/deployments/releases/v2.4.0\n"
    "previous -> /home/user/deployments/releases/v2.3.1\n"
)


# --- Pre-existing structure still intact ---

def test_deployments_directory_exists():
    assert os.path.isdir(DEPLOYMENTS_DIR), (
        f"Directory {DEPLOYMENTS_DIR} does not exist"
    )


def test_releases_directory_exists():
    assert os.path.isdir(RELEASES_DIR), (
        f"Directory {RELEASES_DIR} does not exist"
    )


def test_v231_directory_exists():
    assert os.path.isdir(V231_DIR), (
        f"Directory {V231_DIR} does not exist"
    )


def test_v240_directory_exists():
    assert os.path.isdir(V240_DIR), (
        f"Directory {V240_DIR} does not exist"
    )


def test_v231_version_txt_contents():
    path = os.path.join(V231_DIR, "version.txt")
    with open(path, "r") as f:
        contents = f.read().strip()
    assert contents == "2.3.1", (
        f"Expected {path} to contain '2.3.1', got {contents!r}"
    )


def test_v231_app_conf_contents():
    path = os.path.join(V231_DIR, "app.conf")
    with open(path, "r") as f:
        contents = f.read().strip()
    assert contents == "version=2.3.1", (
        f"Expected {path} to contain 'version=2.3.1', got {contents!r}"
    )


def test_v240_version_txt_contents():
    path = os.path.join(V240_DIR, "version.txt")
    with open(path, "r") as f:
        contents = f.read().strip()
    assert contents == "2.4.0", (
        f"Expected {path} to contain '2.4.0', got {contents!r}"
    )


def test_v240_app_conf_contents():
    path = os.path.join(V240_DIR, "app.conf")
    with open(path, "r") as f:
        contents = f.read().strip()
    assert contents == "version=2.4.0", (
        f"Expected {path} to contain 'version=2.4.0', got {contents!r}"
    )


# --- current symlink ---

def test_current_symlink_exists():
    assert os.path.islink(CURRENT_SYMLINK), (
        f"{CURRENT_SYMLINK} does not exist or is not a symlink. "
        "The 'current' symlink must be present after the task."
    )


def test_current_symlink_points_to_v240():
    assert os.path.islink(CURRENT_SYMLINK), (
        f"{CURRENT_SYMLINK} is not a symlink"
    )
    target = os.readlink(CURRENT_SYMLINK)
    assert target == V240_DIR, (
        f"Expected {CURRENT_SYMLINK} to point to {V240_DIR!r}, "
        f"but it points to {target!r}. "
        "The symlink must be updated to the new release v2.4.0."
    )


def test_current_symlink_target_is_absolute():
    assert os.path.islink(CURRENT_SYMLINK), (
        f"{CURRENT_SYMLINK} is not a symlink"
    )
    target = os.readlink(CURRENT_SYMLINK)
    assert os.path.isabs(target), (
        f"Expected {CURRENT_SYMLINK} to use an absolute path target, "
        f"but got {target!r}. The symlink target must be an absolute path."
    )


def test_current_symlink_resolves_to_existing_directory():
    assert os.path.islink(CURRENT_SYMLINK), (
        f"{CURRENT_SYMLINK} is not a symlink"
    )
    resolved = os.path.realpath(CURRENT_SYMLINK)
    assert os.path.isdir(resolved), (
        f"The symlink {CURRENT_SYMLINK} does not resolve to an existing directory. "
        f"Resolved path: {resolved!r}"
    )


# --- previous symlink ---

def test_previous_symlink_exists():
    assert os.path.islink(PREVIOUS_SYMLINK), (
        f"{PREVIOUS_SYMLINK} does not exist or is not a symlink. "
        "The 'previous' symlink must be created pointing to the old release v2.3.1."
    )


def test_previous_symlink_points_to_v231():
    assert os.path.islink(PREVIOUS_SYMLINK), (
        f"{PREVIOUS_SYMLINK} is not a symlink"
    )
    target = os.readlink(PREVIOUS_SYMLINK)
    assert target == V231_DIR, (
        f"Expected {PREVIOUS_SYMLINK} to point to {V231_DIR!r}, "
        f"but it points to {target!r}. "
        "The 'previous' symlink must reference the old release v2.3.1."
    )


def test_previous_symlink_target_is_absolute():
    assert os.path.islink(PREVIOUS_SYMLINK), (
        f"{PREVIOUS_SYMLINK} is not a symlink"
    )
    target = os.readlink(PREVIOUS_SYMLINK)
    assert os.path.isabs(target), (
        f"Expected {PREVIOUS_SYMLINK} to use an absolute path target, "
        f"but got {target!r}. The symlink target must be an absolute path."
    )


def test_previous_symlink_resolves_to_existing_directory():
    assert os.path.islink(PREVIOUS_SYMLINK), (
        f"{PREVIOUS_SYMLINK} is not a symlink"
    )
    resolved = os.path.realpath(PREVIOUS_SYMLINK)
    assert os.path.isdir(resolved), (
        f"The symlink {PREVIOUS_SYMLINK} does not resolve to an existing directory. "
        f"Resolved path: {resolved!r}"
    )


# --- deploy_log.txt ---

def test_deploy_log_exists():
    assert os.path.isfile(DEPLOY_LOG), (
        f"File {DEPLOY_LOG} does not exist. "
        "The deployment log must be created as part of the task."
    )


def test_deploy_log_exact_contents():
    assert os.path.isfile(DEPLOY_LOG), (
        f"File {DEPLOY_LOG} does not exist"
    )
    with open(DEPLOY_LOG, "r") as f:
        contents = f.read()
    assert contents == EXPECTED_LOG_CONTENTS, (
        f"Contents of {DEPLOY_LOG} do not match expected.\n"
        f"Expected:\n{EXPECTED_LOG_CONTENTS!r}\n"
        f"Got:\n{contents!r}\n"
        "The file must contain exactly 2 lines with the symlink targets, "
        "newline-terminated, no trailing spaces or extra blank lines."
    )


def test_deploy_log_line_count():
    assert os.path.isfile(DEPLOY_LOG), (
        f"File {DEPLOY_LOG} does not exist"
    )
    with open(DEPLOY_LOG, "r") as f:
        contents = f.read()
    # Count lines by splitting on newlines; a proper 2-line file ends with \n
    # so split gives ['line1', 'line2', ''] — we count non-empty trailing
    lines = contents.split("\n")
    # The file should end with a newline, giving exactly 2 non-empty lines
    non_empty_lines = [l for l in lines if l != ""]
    assert len(non_empty_lines) == 2, (
        f"Expected exactly 2 non-empty lines in {DEPLOY_LOG}, "
        f"but found {len(non_empty_lines)}. "
        f"File contents: {contents!r}"
    )
    # Also verify the file ends with a newline (wc -l counts newline-terminated lines)
    assert contents.endswith("\n"), (
        f"File {DEPLOY_LOG} does not end with a newline character. "
        f"File contents: {contents!r}"
    )


def test_deploy_log_first_line():
    assert os.path.isfile(DEPLOY_LOG), (
        f"File {DEPLOY_LOG} does not exist"
    )
    with open(DEPLOY_LOG, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 1, (
        f"File {DEPLOY_LOG} is empty or has fewer than 1 line"
    )
    first_line = lines[0].rstrip("\n")
    expected_first = f"current -> {V240_DIR}"
    assert first_line == expected_first, (
        f"First line of {DEPLOY_LOG} is wrong.\n"
        f"Expected: {expected_first!r}\n"
        f"Got:      {first_line!r}"
    )


def test_deploy_log_second_line():
    assert os.path.isfile(DEPLOY_LOG), (
        f"File {DEPLOY_LOG} does not exist"
    )
    with open(DEPLOY_LOG, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 2, (
        f"File {DEPLOY_LOG} has fewer than 2 lines"
    )
    second_line = lines[1].rstrip("\n")
    expected_second = f"previous -> {V231_DIR}"
    assert second_line == expected_second, (
        f"Second line of {DEPLOY_LOG} is wrong.\n"
        f"Expected: {expected_second!r}\n"
        f"Got:      {second_line!r}"
    )


def test_deploy_log_no_trailing_spaces():
    assert os.path.isfile(DEPLOY_LOG), (
        f"File {DEPLOY_LOG} does not exist"
    )
    with open(DEPLOY_LOG, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} of {DEPLOY_LOG} has trailing whitespace: {stripped!r}"
        )


def test_deploy_log_is_not_a_symlink():
    # The deploy log should be a regular file, not a symlink
    assert not os.path.islink(DEPLOY_LOG), (
        f"{DEPLOY_LOG} is a symlink but should be a regular file."
    )