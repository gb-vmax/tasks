# test_final_state.py

import os
import re
import datetime
import pytest

ARTIFACTS = "/home/user/artifacts"
BUILDS = "/home/user/artifacts/builds"
RELEASES = "/home/user/artifacts/releases"
MANIFEST = "/home/user/artifacts/manifest.txt"

VERSIONS = ["2.1.0", "2.2.0", "2.3.0-beta", "2.3.1"]
HIGHEST_STABLE = "2.3.1"
HIGHEST_BETA = "2.3.0-beta"


# ---------------------------------------------------------------------------
# Symlink existence tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("version", VERSIONS)
def test_release_symlink_exists(version):
    path = os.path.join(RELEASES, version)
    assert os.path.islink(path), (
        f"Expected a symlink at {path}, but it does not exist or is not a symlink"
    )


def test_current_symlink_exists():
    path = os.path.join(RELEASES, "current")
    assert os.path.islink(path), (
        f"Expected a symlink at {path}, but it does not exist or is not a symlink"
    )


def test_latest_stable_symlink_exists():
    path = os.path.join(ARTIFACTS, "latest-stable")
    assert os.path.islink(path), (
        f"Expected a symlink at {path}, but it does not exist or is not a symlink"
    )


def test_latest_beta_symlink_exists():
    path = os.path.join(ARTIFACTS, "latest-beta")
    assert os.path.islink(path), (
        f"Expected a symlink at {path}, but it does not exist or is not a symlink"
    )


# ---------------------------------------------------------------------------
# Symlink target tests (readlink)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("version", VERSIONS)
def test_release_symlink_target(version):
    path = os.path.join(RELEASES, version)
    expected_target = os.path.join(BUILDS, version)
    actual_target = os.readlink(path)
    assert actual_target == expected_target, (
        f"Symlink {path} should point to {expected_target}, "
        f"but readlink returned {actual_target}"
    )


def test_current_symlink_target():
    path = os.path.join(RELEASES, "current")
    expected_target = os.path.join(BUILDS, HIGHEST_STABLE)
    actual_target = os.readlink(path)
    assert actual_target == expected_target, (
        f"Symlink {path} should point to {expected_target}, "
        f"but readlink returned {actual_target}"
    )


def test_latest_stable_symlink_target():
    path = os.path.join(ARTIFACTS, "latest-stable")
    expected_target = os.path.join(RELEASES, "current")
    actual_target = os.readlink(path)
    assert actual_target == expected_target, (
        f"Symlink {path} should point to {expected_target}, "
        f"but readlink returned {actual_target}"
    )


def test_latest_beta_symlink_target():
    path = os.path.join(ARTIFACTS, "latest-beta")
    expected_target = os.path.join(BUILDS, HIGHEST_BETA)
    actual_target = os.readlink(path)
    assert actual_target == expected_target, (
        f"Symlink {path} should point to {expected_target}, "
        f"but readlink returned {actual_target}"
    )


# ---------------------------------------------------------------------------
# Resolved path tests (realpath)
# ---------------------------------------------------------------------------

def test_latest_stable_resolves():
    path = os.path.join(ARTIFACTS, "latest-stable")
    expected_resolved = os.path.join(BUILDS, HIGHEST_STABLE)
    actual_resolved = os.path.realpath(path)
    assert actual_resolved == expected_resolved, (
        f"realpath({path}) should resolve to {expected_resolved}, "
        f"but got {actual_resolved}"
    )


def test_latest_beta_resolves():
    path = os.path.join(ARTIFACTS, "latest-beta")
    expected_resolved = os.path.join(BUILDS, HIGHEST_BETA)
    actual_resolved = os.path.realpath(path)
    assert actual_resolved == expected_resolved, (
        f"realpath({path}) should resolve to {expected_resolved}, "
        f"but got {actual_resolved}"
    )


# ---------------------------------------------------------------------------
# Manifest file tests
# ---------------------------------------------------------------------------

def _read_manifest_lines():
    with open(MANIFEST, "r") as f:
        content = f.read()
    # Split into lines, preserving blank lines
    lines = content.split("\n")
    # If the file ends with a newline, the last element will be ''
    # We want exactly 17 lines of content (no trailing newline producing an extra empty string)
    return lines


def test_manifest_file_exists():
    assert os.path.isfile(MANIFEST), (
        f"Expected manifest file at {MANIFEST}, but it does not exist"
    )


def test_manifest_line_count():
    lines = _read_manifest_lines()
    # The file should have exactly 17 lines of content.
    # If file ends with newline: split gives 18 elements with last being ''
    # If file does not end with newline: split gives 17 elements
    # We accept either (strip trailing empty string if present)
    if lines and lines[-1] == "":
        lines = lines[:-1]
    assert len(lines) == 17, (
        f"manifest.txt should have exactly 17 lines, but has {len(lines)}. "
        f"Content:\n" + "\n".join(f"{i+1}: {repr(l)}" for i, l in enumerate(lines))
    )


def test_manifest_line_1():
    lines = _read_manifest_lines()
    assert lines[0] == "=== ARTIFACT MANIFEST ===", (
        f"Line 1 should be '=== ARTIFACT MANIFEST ===', got {repr(lines[0])}"
    )


def test_manifest_line_2_generated():
    lines = _read_manifest_lines()
    line = lines[1]
    assert line.startswith("generated: "), (
        f"Line 2 should start with 'generated: ', got {repr(line)}"
    )
    date_str = line[len("generated: "):]
    # Validate it's a valid YYYY-MM-DD date
    assert re.match(r"^\d{4}-\d{2}-\d{2}$", date_str), (
        f"Date in line 2 should be YYYY-MM-DD format, got {repr(date_str)}"
    )
    # Validate it matches today's date
    today = datetime.date.today().strftime("%Y-%m-%d")
    assert date_str == today, (
        f"Date in manifest should be today ({today}), got {repr(date_str)}"
    )


def test_manifest_line_3_blank():
    lines = _read_manifest_lines()
    assert lines[2] == "", (
        f"Line 3 should be blank, got {repr(lines[2])}"
    )


def test_manifest_line_4_releases_header():
    lines = _read_manifest_lines()
    assert lines[3] == "[releases]", (
        f"Line 4 should be '[releases]', got {repr(lines[3])}"
    )


def test_manifest_line_5():
    lines = _read_manifest_lines()
    expected = f"2.1.0: {BUILDS}/2.1.0"
    assert lines[4] == expected, (
        f"Line 5 should be {repr(expected)}, got {repr(lines[4])}"
    )


def test_manifest_line_6():
    lines = _read_manifest_lines()
    expected = f"2.2.0: {BUILDS}/2.2.0"
    assert lines[5] == expected, (
        f"Line 6 should be {repr(expected)}, got {repr(lines[5])}"
    )


def test_manifest_line_7():
    lines = _read_manifest_lines()
    expected = f"2.3.0-beta: {BUILDS}/2.3.0-beta"
    assert lines[6] == expected, (
        f"Line 7 should be {repr(expected)}, got {repr(lines[6])}"
    )


def test_manifest_line_8():
    lines = _read_manifest_lines()
    expected = f"2.3.1: {BUILDS}/2.3.1"
    assert lines[7] == expected, (
        f"Line 8 should be {repr(expected)}, got {repr(lines[7])}"
    )


def test_manifest_line_9_blank():
    lines = _read_manifest_lines()
    assert lines[8] == "", (
        f"Line 9 should be blank, got {repr(lines[8])}"
    )


def test_manifest_line_10_special_header():
    lines = _read_manifest_lines()
    assert lines[9] == "[special]", (
        f"Line 10 should be '[special]', got {repr(lines[9])}"
    )


def test_manifest_line_11_current():
    lines = _read_manifest_lines()
    expected = f"current -> {BUILDS}/{HIGHEST_STABLE}"
    assert lines[10] == expected, (
        f"Line 11 should be {repr(expected)}, got {repr(lines[10])}"
    )


def test_manifest_line_12_latest_stable():
    lines = _read_manifest_lines()
    expected = f"latest-stable -> {RELEASES}/current"
    assert lines[11] == expected, (
        f"Line 12 should be {repr(expected)}, got {repr(lines[11])}"
    )


def test_manifest_line_13_latest_beta():
    lines = _read_manifest_lines()
    expected = f"latest-beta -> {BUILDS}/{HIGHEST_BETA}"
    assert lines[12] == expected, (
        f"Line 13 should be {repr(expected)}, got {repr(lines[12])}"
    )


def test_manifest_line_14_blank():
    lines = _read_manifest_lines()
    assert lines[13] == "", (
        f"Line 14 should be blank, got {repr(lines[13])}"
    )


def test_manifest_line_15_resolution_header():
    lines = _read_manifest_lines()
    assert lines[14] == "[resolution]", (
        f"Line 15 should be '[resolution]', got {repr(lines[14])}"
    )


def test_manifest_line_16_latest_stable_resolves():
    lines = _read_manifest_lines()
    expected = f"latest-stable resolves to: {BUILDS}/{HIGHEST_STABLE}"
    assert lines[15] == expected, (
        f"Line 16 should be {repr(expected)}, got {repr(lines[15])}"
    )


def test_manifest_line_17_latest_beta_resolves():
    lines = _read_manifest_lines()
    expected = f"latest-beta resolves to: {BUILDS}/{HIGHEST_BETA}"
    assert lines[16] == expected, (
        f"Line 17 should be {repr(expected)}, got {repr(lines[16])}"
    )


def test_manifest_no_extra_content():
    """Ensure there's no content beyond line 17."""
    with open(MANIFEST, "r") as f:
        content = f.read()
    lines = content.split("\n")
    # Accept trailing newline (one empty string at end) but nothing more
    if lines and lines[-1] == "":
        lines = lines[:-1]
    assert len(lines) == 17, (
        f"manifest.txt should have exactly 17 lines (with optional trailing newline), "
        f"but found {len(lines)} lines."
    )