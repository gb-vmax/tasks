# test_final_state.py

import os
import tarfile
import subprocess
import pytest

ARCHIVE_PATH = "/home/user/submissions/audit_march_2024.tar.gz"
MANIFEST_PATH = "/home/user/submissions/audit_march_2024_manifest.txt"
SUBMISSIONS_DIR = "/home/user/submissions"

EXPECTED_MARCH_FILES = {
    "access_2024-03-01.log",
    "access_2024-03-08.log",
    "access_2024-03-15.log",
    "access_2024-03-22.log",
    "access_2024-03-29.log",
}

EXCLUDED_FILES = {
    "access_2024-02-28.log",
    "access_2024-04-01.log",
}


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _archive_member_basenames():
    """Return the set of bare filenames stored in the archive."""
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        names = tf.getnames()
    # Strip any leading "./" that tar may add
    return {os.path.basename(n.lstrip("./")) for n in names}


# ---------------------------------------------------------------------------
# Tests: submissions directory
# ---------------------------------------------------------------------------

def test_submissions_directory_exists():
    assert os.path.isdir(SUBMISSIONS_DIR), (
        f"The submissions directory '{SUBMISSIONS_DIR}' does not exist. "
        "It must be created as part of the task."
    )


# ---------------------------------------------------------------------------
# Tests: archive existence and validity
# ---------------------------------------------------------------------------

def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive '{ARCHIVE_PATH}' does not exist. "
        "The task requires creating a gzip-compressed tar archive at this path."
    )


def test_archive_is_valid_gzip_tar():
    assert tarfile.is_tarfile(ARCHIVE_PATH), (
        f"'{ARCHIVE_PATH}' is not a valid tar archive."
    )
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            tf.getmembers()
    except Exception as exc:
        pytest.fail(
            f"'{ARCHIVE_PATH}' could not be opened as a gzip-compressed tar archive: {exc}"
        )


# ---------------------------------------------------------------------------
# Tests: archive contents
# ---------------------------------------------------------------------------

def test_archive_contains_exactly_five_members():
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getmembers()
    count = len(members)
    assert count == 5, (
        f"Archive should contain exactly 5 members, but found {count}. "
        f"Members present: {[m.name for m in members]}"
    )


def test_archive_contains_all_expected_march_files():
    basenames = _archive_member_basenames()
    missing = EXPECTED_MARCH_FILES - basenames
    assert not missing, (
        f"The following expected March log files are missing from the archive: {sorted(missing)}. "
        f"Files actually in archive: {sorted(basenames)}"
    )


def test_archive_does_not_contain_excluded_files():
    basenames = _archive_member_basenames()
    unexpected = basenames & EXCLUDED_FILES
    assert not unexpected, (
        f"The archive should NOT contain these files, but does: {sorted(unexpected)}. "
        "Only March 2024 log files should be archived."
    )


def test_archive_members_stored_without_full_path():
    """Members must be stored as bare filenames, not with leading directory paths."""
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        names = tf.getnames()
    for name in names:
        # Strip optional "./" prefix that tar sometimes adds
        stripped = name.lstrip("./")
        assert "/" not in stripped, (
            f"Archive member '{name}' contains a directory path component. "
            "Files must be stored with bare filenames (e.g. 'access_2024-03-01.log'), "
            "not full paths like 'home/user/audit_logs/access_2024-03-01.log'."
        )


def test_archive_member_filenames_match_expected():
    """Each member's basename must exactly match one of the 5 expected filenames."""
    basenames = _archive_member_basenames()
    unexpected = basenames - EXPECTED_MARCH_FILES
    assert not unexpected, (
        f"Archive contains unexpected filenames: {sorted(unexpected)}. "
        f"Only these files are expected: {sorted(EXPECTED_MARCH_FILES)}"
    )


# ---------------------------------------------------------------------------
# Tests: tar -tzf member count (mirrors assertion 1 from truth)
# ---------------------------------------------------------------------------

def test_tar_list_count_equals_five():
    result = subprocess.run(
        ["tar", "-tzf", ARCHIVE_PATH],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"'tar -tzf {ARCHIVE_PATH}' failed with return code {result.returncode}. "
        f"stderr: {result.stderr.strip()}"
    )
    lines = [l for l in result.stdout.splitlines() if l.strip()]
    assert len(lines) == 5, (
        f"'tar -tzf' output should have exactly 5 lines, but got {len(lines)}. "
        f"Output:\n{result.stdout}"
    )


# ---------------------------------------------------------------------------
# Tests: manifest existence and line count
# ---------------------------------------------------------------------------

def test_manifest_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Manifest file '{MANIFEST_PATH}' does not exist. "
        "The task requires generating a table-of-contents manifest."
    )


def test_manifest_has_exactly_five_lines():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    lines = [l for l in content.splitlines() if l.strip()]
    assert len(lines) == 5, (
        f"Manifest '{MANIFEST_PATH}' should have exactly 5 non-blank lines, "
        f"but found {len(lines)}. Content:\n{content}"
    )


def test_manifest_no_blank_lines_or_header():
    """The manifest must contain only the raw tar -tzvf output — no blank lines."""
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    all_lines = content.splitlines()
    blank_lines = [i + 1 for i, l in enumerate(all_lines) if not l.strip()]
    assert not blank_lines, (
        f"Manifest '{MANIFEST_PATH}' contains blank lines at line numbers: {blank_lines}. "
        "The manifest must contain only the raw tar -tzvf output with no blank lines."
    )


# ---------------------------------------------------------------------------
# Tests: manifest content — all 5 March filenames present (assertion 4)
# ---------------------------------------------------------------------------

def test_manifest_contains_all_march_filenames():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    missing = []
    for fname in sorted(EXPECTED_MARCH_FILES):
        if fname not in content:
            missing.append(fname)
    assert not missing, (
        f"The following filenames are missing from the manifest: {missing}. "
        f"Manifest content:\n{content}"
    )


def test_manifest_grep_march_count_equals_five():
    """Mirror assertion 4: grep -c 'access_2024-03' manifest == 5."""
    result = subprocess.run(
        ["grep", "-c", "access_2024-03", MANIFEST_PATH],
        capture_output=True, text=True
    )
    count = int(result.stdout.strip())
    assert count == 5, (
        f"Expected 5 lines containing 'access_2024-03' in the manifest, "
        f"but grep found {count}."
    )


# ---------------------------------------------------------------------------
# Tests: manifest must NOT contain excluded files (assertion 5)
# ---------------------------------------------------------------------------

def test_manifest_does_not_contain_february_file():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "access_2024-02" not in content, (
        f"Manifest '{MANIFEST_PATH}' must NOT contain 'access_2024-02-28.log', "
        "but it does. Only March 2024 files should appear."
    )


def test_manifest_does_not_contain_april_file():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    assert "access_2024-04" not in content, (
        f"Manifest '{MANIFEST_PATH}' must NOT contain 'access_2024-04-01.log', "
        "but it does. Only March 2024 files should appear."
    )


# ---------------------------------------------------------------------------
# Tests: manifest lines look like tar -tzvf verbose output
# ---------------------------------------------------------------------------

def test_manifest_lines_look_like_tar_verbose_output():
    """Each line should resemble a tar -tzvf listing (permissions field present)."""
    with open(MANIFEST_PATH, "r") as f:
        lines = [l for l in f.read().splitlines() if l.strip()]
    for line in lines:
        # tar -tzvf verbose lines start with permission string like -rw-r--r-- or similar
        assert len(line.split()) >= 6, (
            f"Manifest line does not look like tar -tzvf verbose output (expected >= 6 fields): "
            f"'{line}'"
        )


# ---------------------------------------------------------------------------
# Tests: manifest matches live tar -tzvf output
# ---------------------------------------------------------------------------

def test_manifest_matches_tar_tzvf_output():
    """The manifest content should match what 'tar -tzvf' currently produces for the archive."""
    result = subprocess.run(
        ["tar", "-tzvf", ARCHIVE_PATH],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"'tar -tzvf {ARCHIVE_PATH}' failed: {result.stderr.strip()}"
    )
    live_lines = sorted(result.stdout.strip().splitlines())

    with open(MANIFEST_PATH, "r") as f:
        manifest_lines = sorted(f.read().strip().splitlines())

    assert manifest_lines == live_lines, (
        f"Manifest content does not match live 'tar -tzvf' output.\n"
        f"Expected (from tar):\n{chr(10).join(live_lines)}\n"
        f"Found in manifest:\n{chr(10).join(manifest_lines)}"
    )