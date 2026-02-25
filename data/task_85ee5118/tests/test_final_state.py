# test_final_state.py
"""
Pytest suite to validate the FINAL state of the /home/user/k8s-manifests directory
after manifest reorganization and symlink setup.

Checks:
- Manifest files moved to /home/user/k8s-manifests/releases/v1/
- Symlinks created in /home/user/k8s-manifests/current/ pointing to those files
- Symlinks are valid and absolute
- /home/user/k8s-manifests/link-status.log exists and is exactly correct

Failures explain exactly what is still wrong.
"""

import os
import pytest

K8S_MANIFESTS = "/home/user/k8s-manifests"
RELEASES_V1 = os.path.join(K8S_MANIFESTS, "releases", "v1")
CURRENT = os.path.join(K8S_MANIFESTS, "current")
LINK_STATUS_LOG = os.path.join(K8S_MANIFESTS, "link-status.log")

# Map: symlink_name -> (target_filename, expected absolute target)
SYMLINKS = [
    ("frontend.yaml", "frontend-deployment.yaml"),
    ("backend.yaml", "backend-deployment.yaml"),
    ("database.yaml", "database-deployment.yaml"),
]

@pytest.mark.describe("Final state: Manifest files in releases/v1/")
@pytest.mark.parametrize("filename", [t for _, t in SYMLINKS])
def test_manifest_files_moved_to_releases_v1(filename):
    original_path = os.path.join(K8S_MANIFESTS, filename)
    new_path = os.path.join(RELEASES_V1, filename)
    assert not os.path.exists(original_path), (
        f"Manifest file {original_path} should have been moved to {new_path}."
    )
    assert os.path.isfile(new_path), (
        f"Manifest file {new_path} is missing. "
        "It must exist in releases/v1/ after completion."
    )

@pytest.mark.describe("Final state: releases/v1/ directory structure")
def test_releases_v1_directory_exists():
    assert os.path.isdir(RELEASES_V1), (
        f"Directory {RELEASES_V1} does not exist. "
        "You must create the releases/v1/ directory."
    )

@pytest.mark.describe("Final state: Symlinks in current/")
@pytest.mark.parametrize("symlink_name,target_filename", SYMLINKS)
def test_symlink_exists_and_points_correctly(symlink_name, target_filename):
    symlink_path = os.path.join(CURRENT, symlink_name)
    expected_target = os.path.join(RELEASES_V1, target_filename)

    assert os.path.lexists(symlink_path), (
        f"Symlink {symlink_path} does not exist. "
        "You must create this symlink in current/."
    )
    assert os.path.islink(symlink_path), (
        f"{symlink_path} exists but is not a symbolic link. "
        "It must be a symlink, not a file or directory."
    )
    # The link must be absolute and point to the correct file
    link_target = os.readlink(symlink_path)
    if not os.path.isabs(link_target):
        link_target_abs = os.path.abspath(os.path.join(os.path.dirname(symlink_path), link_target))
    else:
        link_target_abs = link_target

    assert link_target_abs == expected_target, (
        f"Symlink {symlink_path} points to {link_target_abs}, "
        f"but should point to {expected_target}."
    )
    assert os.path.isfile(expected_target), (
        f"The symlink target {expected_target} does not exist or is not a file."
    )

@pytest.mark.describe("Final state: No extra files in current/")
def test_no_extra_files_in_current():
    present = set(os.listdir(CURRENT))
    expected = {symlink for symlink, _ in SYMLINKS}
    extra = present - expected
    missing = expected - present
    assert not missing, (
        f"Missing expected symlinks in current/: {sorted(missing)}"
    )
    assert not extra, (
        f"Found unexpected files or links in current/: {sorted(extra)}"
    )

@pytest.mark.describe("Final state: link-status.log is correct")
def test_link_status_log_exists():
    assert os.path.isfile(LINK_STATUS_LOG), (
        f"Log file {LINK_STATUS_LOG} does not exist. "
        "You must generate link-status.log after creating symlinks."
    )

def _expected_log_lines():
    # Returns a set of the expected lines (order not enforced)
    lines = []
    for symlink, target in SYMLINKS:
        abs_target = os.path.join(RELEASES_V1, target)
        # The file must exist, so -> yes
        lines.append(f"{symlink}: {abs_target} -> yes")
    return set(lines)

def test_link_status_log_contents():
    expected_lines = _expected_log_lines()
    try:
        with open(LINK_STATUS_LOG, "r") as f:
            actual_lines = [line.rstrip("\n") for line in f]
    except Exception as e:
        pytest.fail(f"Could not read {LINK_STATUS_LOG}: {e}")

    # Remove empty lines if present
    actual_lines = [line for line in actual_lines if line.strip() != ""]

    actual_set = set(actual_lines)
    missing = expected_lines - actual_set
    extra = actual_set - expected_lines

    assert not missing, (
        f"link-status.log is missing lines: {sorted(missing)}"
    )
    assert not extra, (
        f"link-status.log contains unexpected extra lines: {sorted(extra)}"
    )
    assert len(actual_lines) == len(expected_lines), (
        f"link-status.log should have exactly {len(expected_lines)} lines, found {len(actual_lines)}."
    )

@pytest.mark.describe("Final state: Manifest files only in releases/v1/, not in root")
@pytest.mark.parametrize("filename", [t for _, t in SYMLINKS])
def test_no_manifest_files_left_in_root(filename):
    original_path = os.path.join(K8S_MANIFESTS, filename)
    assert not os.path.exists(original_path), (
        f"Manifest file {original_path} should have been moved to releases/v1/ and not remain in the root directory."
    )