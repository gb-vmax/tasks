# test_final_state.py

import os
import pytest

CONFIGS_DIR = "/home/user/network/configs"
ACTIVE_DIR = "/home/user/network/active"

CORE_ROUTER_CONF = os.path.join(CONFIGS_DIR, "core-router.conf")
EDGE_ROUTER_CONF = os.path.join(CONFIGS_DIR, "edge-router.conf")

ACTIVE_CORE = os.path.join(ACTIVE_DIR, "core-router.conf")
ACTIVE_EDGE = os.path.join(ACTIVE_DIR, "edge-router.conf")
ACTIVE_PRIMARY = os.path.join(ACTIVE_DIR, "primary.conf")
ACTIVE_LINKS_TXT = os.path.join(ACTIVE_DIR, "links.txt")

EXPECTED_LINKS_CONTENT = (
    "core-router.conf -> /home/user/network/configs/core-router.conf\n"
    "edge-router.conf -> /home/user/network/configs/edge-router.conf\n"
    "primary.conf -> /home/user/network/configs/core-router.conf"
)


# --- Pre-existing source files still intact ---

def test_source_core_router_conf_exists():
    assert os.path.isfile(CORE_ROUTER_CONF), (
        f"Source file {CORE_ROUTER_CONF} does not exist"
    )


def test_source_edge_router_conf_exists():
    assert os.path.isfile(EDGE_ROUTER_CONF), (
        f"Source file {EDGE_ROUTER_CONF} does not exist"
    )


# --- Symlink existence checks ---

def test_active_core_router_is_symlink():
    assert os.path.islink(ACTIVE_CORE), (
        f"{ACTIVE_CORE} should be a symbolic link, but it is not. "
        f"Exists as regular file: {os.path.isfile(ACTIVE_CORE)}"
    )


def test_active_edge_router_is_symlink():
    assert os.path.islink(ACTIVE_EDGE), (
        f"{ACTIVE_EDGE} should be a symbolic link, but it is not. "
        f"Exists as regular file: {os.path.isfile(ACTIVE_EDGE)}"
    )


def test_active_primary_is_symlink():
    assert os.path.islink(ACTIVE_PRIMARY), (
        f"{ACTIVE_PRIMARY} should be a symbolic link, but it is not. "
        f"Exists as regular file: {os.path.isfile(ACTIVE_PRIMARY)}"
    )


# --- Symlink target checks (absolute paths) ---

def test_core_router_symlink_target():
    expected_target = "/home/user/network/configs/core-router.conf"
    actual_target = os.readlink(ACTIVE_CORE)
    assert actual_target == expected_target, (
        f"{ACTIVE_CORE} points to '{actual_target}', "
        f"but should point to '{expected_target}'"
    )


def test_edge_router_symlink_target():
    expected_target = "/home/user/network/configs/edge-router.conf"
    actual_target = os.readlink(ACTIVE_EDGE)
    assert actual_target == expected_target, (
        f"{ACTIVE_EDGE} points to '{actual_target}', "
        f"but should point to '{expected_target}'"
    )


def test_primary_symlink_target():
    expected_target = "/home/user/network/configs/core-router.conf"
    actual_target = os.readlink(ACTIVE_PRIMARY)
    assert actual_target == expected_target, (
        f"{ACTIVE_PRIMARY} points to '{actual_target}', "
        f"but should point to '{expected_target}'"
    )


# --- Symlink targets are absolute paths ---

def test_core_router_symlink_is_absolute():
    target = os.readlink(ACTIVE_CORE)
    assert os.path.isabs(target), (
        f"{ACTIVE_CORE} points to a relative path '{target}'. "
        f"It must point to an absolute path."
    )


def test_edge_router_symlink_is_absolute():
    target = os.readlink(ACTIVE_EDGE)
    assert os.path.isabs(target), (
        f"{ACTIVE_EDGE} points to a relative path '{target}'. "
        f"It must point to an absolute path."
    )


def test_primary_symlink_is_absolute():
    target = os.readlink(ACTIVE_PRIMARY)
    assert os.path.isabs(target), (
        f"{ACTIVE_PRIMARY} points to a relative path '{target}'. "
        f"It must point to an absolute path."
    )


# --- Symlinks resolve to actual files ---

def test_core_router_symlink_resolves():
    assert os.path.exists(ACTIVE_CORE), (
        f"Symlink {ACTIVE_CORE} is broken — target does not exist: "
        f"{os.readlink(ACTIVE_CORE)}"
    )


def test_edge_router_symlink_resolves():
    assert os.path.exists(ACTIVE_EDGE), (
        f"Symlink {ACTIVE_EDGE} is broken — target does not exist: "
        f"{os.readlink(ACTIVE_EDGE)}"
    )


def test_primary_symlink_resolves():
    assert os.path.exists(ACTIVE_PRIMARY), (
        f"Symlink {ACTIVE_PRIMARY} is broken — target does not exist: "
        f"{os.readlink(ACTIVE_PRIMARY)}"
    )


# --- links.txt existence and content ---

def test_links_txt_exists():
    assert os.path.exists(ACTIVE_LINKS_TXT), (
        f"File {ACTIVE_LINKS_TXT} does not exist"
    )


def test_links_txt_is_regular_file():
    assert os.path.isfile(ACTIVE_LINKS_TXT) and not os.path.islink(ACTIVE_LINKS_TXT), (
        f"{ACTIVE_LINKS_TXT} should be a plain text file, not a symlink or directory"
    )


def test_links_txt_content():
    with open(ACTIVE_LINKS_TXT, "r") as f:
        content = f.read()
    # Strip trailing newline for comparison (allow one trailing newline)
    content_stripped = content.rstrip("\n")
    assert content_stripped == EXPECTED_LINKS_CONTENT, (
        f"Content of {ACTIVE_LINKS_TXT} does not match expected.\n"
        f"Got (repr):\n{repr(content)}\n"
        f"Expected (repr):\n{repr(EXPECTED_LINKS_CONTENT + chr(10))}\n"
        f"or\n{repr(EXPECTED_LINKS_CONTENT)}"
    )


def test_links_txt_line_count():
    with open(ACTIVE_LINKS_TXT, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 3, (
        f"{ACTIVE_LINKS_TXT} should contain exactly 3 lines, "
        f"but has {len(lines)} lines: {lines}"
    )


def test_links_txt_line1():
    with open(ACTIVE_LINKS_TXT, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    expected = "core-router.conf -> /home/user/network/configs/core-router.conf"
    assert lines[0] == expected, (
        f"Line 1 of {ACTIVE_LINKS_TXT} is wrong.\n"
        f"Got:      '{lines[0]}'\n"
        f"Expected: '{expected}'"
    )


def test_links_txt_line2():
    with open(ACTIVE_LINKS_TXT, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    expected = "edge-router.conf -> /home/user/network/configs/edge-router.conf"
    assert lines[1] == expected, (
        f"Line 2 of {ACTIVE_LINKS_TXT} is wrong.\n"
        f"Got:      '{lines[1]}'\n"
        f"Expected: '{expected}'"
    )


def test_links_txt_line3():
    with open(ACTIVE_LINKS_TXT, "r") as f:
        lines = f.read().rstrip("\n").split("\n")
    expected = "primary.conf -> /home/user/network/configs/core-router.conf"
    assert lines[2] == expected, (
        f"Line 3 of {ACTIVE_LINKS_TXT} is wrong.\n"
        f"Got:      '{lines[2]}'\n"
        f"Expected: '{expected}'"
    )


def test_links_txt_unix_line_endings():
    with open(ACTIVE_LINKS_TXT, "rb") as f:
        raw = f.read()
    assert b"\r\n" not in raw, (
        f"{ACTIVE_LINKS_TXT} contains Windows-style line endings (CRLF). "
        f"Unix line endings (LF only) are required."
    )


# --- Active directory contains exactly the expected entries ---

def test_active_directory_contains_expected_entries():
    expected_entries = {"core-router.conf", "edge-router.conf", "primary.conf", "links.txt"}
    actual_entries = set(os.listdir(ACTIVE_DIR))
    missing = expected_entries - actual_entries
    extra = actual_entries - expected_entries
    assert not missing and not extra, (
        f"Directory {ACTIVE_DIR} does not contain exactly the expected entries.\n"
        f"Missing: {missing}\n"
        f"Unexpected extra entries: {extra}"
    )