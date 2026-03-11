# test_final_state.py

import os
import stat
import hashlib
import pytest

BASE = "/home/user/artifact-repo"
RELEASES = os.path.join(BASE, "releases")
SNAPSHOTS = os.path.join(BASE, "snapshots")
CACHE = os.path.join(BASE, "cache")
CONF = os.path.join(BASE, "repo.conf")

EXPECTED_CONF_CONTENT = (
    "[repository]\n"
    "name=local-artifact-repo\n"
    "base_path=/home/user/artifact-repo\n"
    "\n"
    "[storage]\n"
    "releases_dir=releases\n"
    "snapshots_dir=snapshots\n"
    "cache_dir=cache\n"
    "\n"
    "[policy]\n"
    "max_cache_size_mb=2048\n"
    "retain_snapshots=10\n"
    "retain_releases=all\n"
)


def get_octal_permissions(path):
    """Return the permission bits as a 3-digit octal string, e.g. '755'."""
    mode = os.stat(path).st_mode
    return oct(stat.S_IMODE(mode))[2:]


# --- Directory existence tests ---

def test_artifact_repo_base_exists():
    assert os.path.isdir(BASE), (
        f"Expected directory '{BASE}' to exist, but it does not."
    )


def test_releases_dir_exists():
    assert os.path.isdir(RELEASES), (
        f"Expected directory '{RELEASES}' to exist, but it does not."
    )


def test_snapshots_dir_exists():
    assert os.path.isdir(SNAPSHOTS), (
        f"Expected directory '{SNAPSHOTS}' to exist, but it does not."
    )


def test_cache_dir_exists():
    assert os.path.isdir(CACHE), (
        f"Expected directory '{CACHE}' to exist, but it does not."
    )


# --- Permission tests ---

def test_releases_permissions():
    perms = get_octal_permissions(RELEASES)
    assert perms == "755", (
        f"Expected '{RELEASES}' to have permissions 755 (drwxr-xr-x), "
        f"but got {perms}."
    )


def test_snapshots_permissions():
    perms = get_octal_permissions(SNAPSHOTS)
    assert perms == "750", (
        f"Expected '{SNAPSHOTS}' to have permissions 750 (drwxr-x---), "
        f"but got {perms}."
    )


def test_cache_permissions():
    perms = get_octal_permissions(CACHE)
    assert perms == "700", (
        f"Expected '{CACHE}' to have permissions 700 (drwx------), "
        f"but got {perms}."
    )


# --- Config file existence ---

def test_repo_conf_exists():
    assert os.path.isfile(CONF), (
        f"Expected configuration file '{CONF}' to exist, but it does not."
    )


# --- Config file content tests ---

def test_repo_conf_line_count():
    with open(CONF, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")
    # A file ending with \n will have an empty string as the last element after split
    # wc -l counts newline characters, so 13 newlines = 13 lines
    newline_count = content.count("\n")
    assert newline_count == 13, (
        f"Expected repo.conf to contain exactly 13 newline characters (13 lines per wc -l), "
        f"but found {newline_count}. File content:\n{content!r}"
    )


def test_repo_conf_ends_with_newline():
    with open(CONF, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"Expected '{CONF}' to end with a newline character, but it does not."
    )


def test_repo_conf_no_bom():
    with open(CONF, "rb") as f:
        start = f.read(3)
    assert not start.startswith(b"\xef\xbb\xbf"), (
        f"Expected '{CONF}' to have no BOM (byte order mark), but a UTF-8 BOM was found."
    )


def test_repo_conf_unix_line_endings():
    with open(CONF, "rb") as f:
        content = f.read()
    assert b"\r\n" not in content, (
        f"Expected '{CONF}' to use Unix line endings (\\n only), "
        f"but Windows-style line endings (\\r\\n) were found."
    )
    assert b"\r" not in content, (
        f"Expected '{CONF}' to use Unix line endings (\\n only), "
        f"but carriage return characters (\\r) were found."
    )


def test_repo_conf_exact_content():
    with open(CONF, "r", encoding="utf-8") as f:
        actual = f.read()
    assert actual == EXPECTED_CONF_CONTENT, (
        f"The content of '{CONF}' does not match the expected content.\n"
        f"Expected:\n{EXPECTED_CONF_CONTENT!r}\n"
        f"Actual:\n{actual!r}"
    )


def test_repo_conf_md5():
    expected_md5 = hashlib.md5(EXPECTED_CONF_CONTENT.encode("utf-8")).hexdigest()
    with open(CONF, "rb") as f:
        actual_bytes = f.read()
    actual_md5 = hashlib.md5(actual_bytes).hexdigest()
    assert actual_md5 == expected_md5, (
        f"MD5 checksum of '{CONF}' does not match expected.\n"
        f"Expected MD5: {expected_md5}\n"
        f"Actual MD5:   {actual_md5}\n"
        f"This indicates the file content differs from the specification."
    )


# --- Spot-check individual config values ---

def test_repo_conf_repository_section():
    with open(CONF, "r", encoding="utf-8") as f:
        content = f.read()
    assert "[repository]" in content, (
        f"Expected '[repository]' section header in '{CONF}', but it was not found."
    )
    assert "name=local-artifact-repo" in content, (
        f"Expected 'name=local-artifact-repo' in '{CONF}', but it was not found."
    )
    assert "base_path=/home/user/artifact-repo" in content, (
        f"Expected 'base_path=/home/user/artifact-repo' in '{CONF}', but it was not found."
    )


def test_repo_conf_storage_section():
    with open(CONF, "r", encoding="utf-8") as f:
        content = f.read()
    assert "[storage]" in content, (
        f"Expected '[storage]' section header in '{CONF}', but it was not found."
    )
    assert "releases_dir=releases" in content, (
        f"Expected 'releases_dir=releases' in '{CONF}', but it was not found."
    )
    assert "snapshots_dir=snapshots" in content, (
        f"Expected 'snapshots_dir=snapshots' in '{CONF}', but it was not found."
    )
    assert "cache_dir=cache" in content, (
        f"Expected 'cache_dir=cache' in '{CONF}', but it was not found."
    )


def test_repo_conf_policy_section():
    with open(CONF, "r", encoding="utf-8") as f:
        content = f.read()
    assert "[policy]" in content, (
        f"Expected '[policy]' section header in '{CONF}', but it was not found."
    )
    assert "max_cache_size_mb=2048" in content, (
        f"Expected 'max_cache_size_mb=2048' in '{CONF}', but it was not found."
    )
    assert "retain_snapshots=10" in content, (
        f"Expected 'retain_snapshots=10' in '{CONF}', but it was not found."
    )
    assert "retain_releases=all" in content, (
        f"Expected 'retain_releases=all' in '{CONF}', but it was not found."
    )