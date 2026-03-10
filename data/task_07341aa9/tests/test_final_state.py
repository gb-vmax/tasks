# test_final_state.py

import hashlib
import os
import stat
import subprocess
import pytest

STAGING = "/home/user/iot_staging"

# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def get_octal_permissions(filepath):
    """Return the permission bits of a file as an integer (e.g. 0o640)."""
    return stat.S_IMODE(os.stat(filepath).st_mode)


def sha256_of_file(filepath):
    """Compute the SHA-256 hex digest of a file's contents."""
    h = hashlib.sha256()
    with open(filepath, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Step 1 – No .tmp or .bak files should remain
# ---------------------------------------------------------------------------

DELETED_FILES = [
    f"{STAGING}/devices/sensor_a/old_firmware.bak",
    f"{STAGING}/devices/sensor_a/build_temp.tmp",
    f"{STAGING}/devices/sensor_b/calibration.tmp",
    f"{STAGING}/devices/gateway/gateway_old.bak",
    f"{STAGING}/scratch.tmp",
]


@pytest.mark.parametrize("filepath", DELETED_FILES)
def test_deleted_file_does_not_exist(filepath):
    assert not os.path.exists(filepath), (
        f"File should have been deleted but still exists: {filepath}"
    )


def test_no_tmp_files_remain():
    result = subprocess.run(
        ["find", STAGING, "-type", "f", "-name", "*.tmp"],
        capture_output=True, text=True
    )
    found = result.stdout.strip()
    assert found == "", (
        f"Found unexpected .tmp files under {STAGING}:\n{found}"
    )


def test_no_bak_files_remain():
    result = subprocess.run(
        ["find", STAGING, "-type", "f", "-name", "*.bak"],
        capture_output=True, text=True
    )
    found = result.stdout.strip()
    assert found == "", (
        f"Found unexpected .bak files under {STAGING}:\n{found}"
    )


# ---------------------------------------------------------------------------
# Step 2 – .conf files should have mode 640
# ---------------------------------------------------------------------------

CONF_FILES = [
    f"{STAGING}/devices/sensor_a/device.conf",
    f"{STAGING}/devices/sensor_b/device.conf",
    f"{STAGING}/devices/gateway/gateway.conf",
    f"{STAGING}/shared/base.conf",
]


@pytest.mark.parametrize("filepath", CONF_FILES)
def test_conf_file_exists(filepath):
    assert os.path.isfile(filepath), (
        f"Config file should exist but does not: {filepath}"
    )


@pytest.mark.parametrize("filepath", CONF_FILES)
def test_conf_file_permission_640(filepath):
    assert os.path.isfile(filepath), f"Config file does not exist: {filepath}"
    actual = get_octal_permissions(filepath)
    assert actual == 0o640, (
        f"Permission mismatch for {filepath}:\n"
        f"  Expected: 640 (0o640)\n"
        f"  Actual:   {oct(actual)}"
    )


# ---------------------------------------------------------------------------
# Step 3 – .bin files should have mode 750
# ---------------------------------------------------------------------------

BIN_FILES = [
    f"{STAGING}/devices/gateway/gateway.bin",
    f"{STAGING}/devices/sensor_a/firmware_v2.bin",
    f"{STAGING}/devices/sensor_b/firmware_v2.bin",
    f"{STAGING}/shared/loader.bin",
]


@pytest.mark.parametrize("filepath", BIN_FILES)
def test_bin_file_exists(filepath):
    assert os.path.isfile(filepath), (
        f"Binary file should exist but does not: {filepath}"
    )


@pytest.mark.parametrize("filepath", BIN_FILES)
def test_bin_file_permission_750(filepath):
    assert os.path.isfile(filepath), f"Binary file does not exist: {filepath}"
    actual = get_octal_permissions(filepath)
    assert actual == 0o750, (
        f"Permission mismatch for {filepath}:\n"
        f"  Expected: 750 (0o750)\n"
        f"  Actual:   {oct(actual)}"
    )


# ---------------------------------------------------------------------------
# Step 4 – checksums.sha256
# ---------------------------------------------------------------------------

CHECKSUMS_FILE = f"{STAGING}/checksums.sha256"

# Sorted alphabetically by full path (as the task requires)
EXPECTED_BIN_ORDER = [
    f"{STAGING}/devices/gateway/gateway.bin",
    f"{STAGING}/devices/sensor_a/firmware_v2.bin",
    f"{STAGING}/devices/sensor_b/firmware_v2.bin",
    f"{STAGING}/shared/loader.bin",
]


def test_checksums_file_exists():
    assert os.path.isfile(CHECKSUMS_FILE), (
        f"Checksum file does not exist: {CHECKSUMS_FILE}"
    )


def test_checksums_file_line_count():
    assert os.path.isfile(CHECKSUMS_FILE), f"Checksum file does not exist: {CHECKSUMS_FILE}"
    with open(CHECKSUMS_FILE) as fh:
        lines = [l for l in fh.read().splitlines() if l.strip()]
    assert len(lines) == 4, (
        f"Expected exactly 4 lines in checksums.sha256, got {len(lines)}:\n"
        + "\n".join(lines)
    )


def test_checksums_file_content():
    """Each line must match sha256sum output for the correct .bin file, in alphabetical path order."""
    assert os.path.isfile(CHECKSUMS_FILE), f"Checksum file does not exist: {CHECKSUMS_FILE}"

    with open(CHECKSUMS_FILE) as fh:
        lines = [l for l in fh.read().splitlines() if l.strip()]

    assert len(lines) == 4, (
        f"Expected 4 non-empty lines in checksums.sha256, got {len(lines)}"
    )

    for i, (expected_path, line) in enumerate(zip(EXPECTED_BIN_ORDER, lines), start=1):
        expected_hash = sha256_of_file(expected_path)
        expected_line = f"{expected_hash}  {expected_path}"
        assert line == expected_line, (
            f"Line {i} of checksums.sha256 is incorrect:\n"
            f"  Expected: {expected_line!r}\n"
            f"  Actual:   {line!r}"
        )


def test_checksums_sorted_alphabetically():
    """Verify the paths in checksums.sha256 are in alphabetical order."""
    assert os.path.isfile(CHECKSUMS_FILE), f"Checksum file does not exist: {CHECKSUMS_FILE}"

    with open(CHECKSUMS_FILE) as fh:
        lines = [l for l in fh.read().splitlines() if l.strip()]

    paths_in_file = []
    for line in lines:
        parts = line.split("  ", 1)
        assert len(parts) == 2, (
            f"Checksum line does not have expected format '<hash>  <path>': {line!r}"
        )
        paths_in_file.append(parts[1])

    assert paths_in_file == sorted(paths_in_file), (
        f"Paths in checksums.sha256 are not sorted alphabetically:\n"
        f"  Found order:    {paths_in_file}\n"
        f"  Expected order: {sorted(paths_in_file)}"
    )


# ---------------------------------------------------------------------------
# Step 5 – manifest.txt
# ---------------------------------------------------------------------------

MANIFEST_FILE = f"{STAGING}/manifest.txt"

EXPECTED_MANIFEST = """\
=== IoT Deployment Manifest ===
Generated by: edge-deploy-prep

[CONFIG FILES]
devices/gateway/gateway.conf: 640
devices/sensor_a/device.conf: 640
devices/sensor_b/device.conf: 640
shared/base.conf: 640

[BINARY FILES]
devices/gateway/gateway.bin: 750
devices/sensor_a/firmware_v2.bin: 750
devices/sensor_b/firmware_v2.bin: 750
shared/loader.bin: 750

[CHECKSUM FILE]
checksums.sha256: present
"""


def test_manifest_file_exists():
    assert os.path.isfile(MANIFEST_FILE), (
        f"Manifest file does not exist: {MANIFEST_FILE}"
    )


def test_manifest_file_exact_content():
    assert os.path.isfile(MANIFEST_FILE), f"Manifest file does not exist: {MANIFEST_FILE}"

    with open(MANIFEST_FILE) as fh:
        actual = fh.read()

    assert actual == EXPECTED_MANIFEST, (
        f"manifest.txt content does not match expected.\n"
        f"--- Expected ---\n{EXPECTED_MANIFEST!r}\n"
        f"--- Actual ---\n{actual!r}"
    )


def test_manifest_does_not_contain_checksums_in_sections():
    """checksums.sha256 must not appear in [CONFIG FILES] or [BINARY FILES] sections."""
    assert os.path.isfile(MANIFEST_FILE), f"Manifest file does not exist: {MANIFEST_FILE}"

    with open(MANIFEST_FILE) as fh:
        lines = fh.readlines()

    in_config_or_binary = False
    for line in lines:
        stripped = line.strip()
        if stripped in ("[CONFIG FILES]", "[BINARY FILES]"):
            in_config_or_binary = True
        elif stripped.startswith("["):
            in_config_or_binary = False
        if in_config_or_binary and "checksums.sha256" in stripped:
            pytest.fail(
                "checksums.sha256 should not appear in [CONFIG FILES] or [BINARY FILES] sections "
                f"of manifest.txt, but found line: {line!r}"
            )


def test_manifest_does_not_contain_manifest_in_sections():
    """manifest.txt must not appear in [CONFIG FILES] or [BINARY FILES] sections."""
    assert os.path.isfile(MANIFEST_FILE), f"Manifest file does not exist: {MANIFEST_FILE}"

    with open(MANIFEST_FILE) as fh:
        lines = fh.readlines()

    in_config_or_binary = False
    for line in lines:
        stripped = line.strip()
        if stripped in ("[CONFIG FILES]", "[BINARY FILES]"):
            in_config_or_binary = True
        elif stripped.startswith("["):
            in_config_or_binary = False
        if in_config_or_binary and "manifest.txt" in stripped:
            pytest.fail(
                "manifest.txt should not appear in [CONFIG FILES] or [BINARY FILES] sections, "
                f"but found line: {line!r}"
            )


def test_manifest_no_dotslash_prefix_in_paths():
    """Relative paths in manifest must not start with './'."""
    assert os.path.isfile(MANIFEST_FILE), f"Manifest file does not exist: {MANIFEST_FILE}"

    with open(MANIFEST_FILE) as fh:
        content = fh.read()

    for line in content.splitlines():
        if line.startswith("./"):
            pytest.fail(
                f"Relative path in manifest starts with './' which is not allowed: {line!r}"
            )


# ---------------------------------------------------------------------------
# Sanity – original .conf and .bin files still present with correct content
# ---------------------------------------------------------------------------

CONF_CONTENTS = {
    f"{STAGING}/devices/sensor_a/device.conf": "[sensor_a]\ntype=temperature\ninterval=30\n",
    f"{STAGING}/devices/sensor_b/device.conf": "[sensor_b]\ntype=humidity\ninterval=60\n",
    f"{STAGING}/devices/gateway/gateway.conf": "[gateway]\nport=8883\ntls=true\n",
    f"{STAGING}/shared/base.conf": "[base]\nversion=2.1\nregion=us-east\n",
}

BIN_CONTENTS = {
    f"{STAGING}/devices/sensor_a/firmware_v2.bin": "FWBIN_SENSOR_A_V2\n",
    f"{STAGING}/devices/sensor_b/firmware_v2.bin": "FWBIN_SENSOR_B_V2\n",
    f"{STAGING}/devices/gateway/gateway.bin": "FWBIN_GATEWAY\n",
    f"{STAGING}/shared/loader.bin": "FWBIN_LOADER\n",
}


@pytest.mark.parametrize("filepath,expected_content", list(CONF_CONTENTS.items()))
def test_conf_file_content_unchanged(filepath, expected_content):
    assert os.path.isfile(filepath), f"Config file missing: {filepath}"
    with open(filepath) as fh:
        actual = fh.read()
    assert actual == expected_content, (
        f"Content of {filepath} was unexpectedly changed:\n"
        f"  Expected: {expected_content!r}\n"
        f"  Actual:   {actual!r}"
    )


@pytest.mark.parametrize("filepath,expected_content", list(BIN_CONTENTS.items()))
def test_bin_file_content_unchanged(filepath, expected_content):
    assert os.path.isfile(filepath), f"Binary file missing: {filepath}"
    with open(filepath) as fh:
        actual = fh.read()
    assert actual == expected_content, (
        f"Content of {filepath} was unexpectedly changed:\n"
        f"  Expected: {expected_content!r}\n"
        f"  Actual:   {actual!r}"
    )