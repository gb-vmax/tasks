# test_final_state.py

import os
import gzip
import tarfile
import subprocess
import pytest

HOME = "/home/user"
BACKUPS_DIR = os.path.join(HOME, "backups")
ARCHIVE_PATH = os.path.join(BACKUPS_DIR, "alerts_backup.tar.gz")
MANIFEST_PATH = os.path.join(BACKUPS_DIR, "alerts_manifest.txt")
ALERTS_DIR = os.path.join(HOME, "monitoring", "alerts")

EXPECTED_ARCHIVE_ENTRIES = {
    "alerts/",
    "alerts/cpu_high.yml",
    "alerts/disk_full.yml",
    "alerts/memory_low.yml",
}

EXPECTED_FILE_CONTENTS = {
    "alerts/cpu_high.yml": "alert: HighCPU\nthreshold: 90",
    "alerts/disk_full.yml": "alert: DiskFull\nthreshold: 85",
    "alerts/memory_low.yml": "alert: LowMemory\nthreshold: 10",
}


# ── Directory / file existence ────────────────────────────────────────────────

def test_backups_directory_exists():
    assert os.path.isdir(BACKUPS_DIR), (
        f"The backups directory {BACKUPS_DIR} does not exist. "
        "It should have been created as part of the task."
    )


def test_archive_file_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"The archive file {ARCHIVE_PATH} does not exist. "
        "A gzip-compressed tar archive should have been created there."
    )


def test_manifest_file_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"The manifest file {MANIFEST_PATH} does not exist. "
        "A plain-text manifest listing the archive contents should be present."
    )


# ── Archive validity ──────────────────────────────────────────────────────────

def test_archive_is_gzip_compressed():
    """Verify the file starts with the gzip magic bytes."""
    with open(ARCHIVE_PATH, "rb") as fh:
        magic = fh.read(2)
    assert magic == b"\x1f\x8b", (
        f"{ARCHIVE_PATH} does not appear to be gzip-compressed "
        f"(expected magic bytes 0x1f 0x8b, got {magic!r})."
    )


def test_archive_is_valid_tar():
    """tarfile.open should not raise for a valid tar.gz."""
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            _ = tf.getnames()
    except (tarfile.TarError, OSError) as exc:
        pytest.fail(
            f"{ARCHIVE_PATH} is not a valid gzip-compressed tar archive: {exc}"
        )


# ── Archive contents ──────────────────────────────────────────────────────────

def _get_archive_entries():
    """Return the list of names exactly as tar -tzf would output them."""
    result = subprocess.run(
        ["tar", "-tzf", ARCHIVE_PATH],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"`tar -tzf {ARCHIVE_PATH}` failed with return code {result.returncode}.\n"
        f"stderr: {result.stderr}"
    )
    # Split on newlines; drop any trailing empty string from final newline
    entries = result.stdout.split("\n")
    if entries and entries[-1] == "":
        entries = entries[:-1]
    return entries


def test_archive_contains_all_expected_entries():
    entries = set(_get_archive_entries())
    missing = EXPECTED_ARCHIVE_ENTRIES - entries
    assert not missing, (
        f"The archive {ARCHIVE_PATH} is missing the following entries: {missing}.\n"
        f"Actual entries: {entries}"
    )


def test_archive_contains_no_extra_entries():
    entries = set(_get_archive_entries())
    extra = entries - EXPECTED_ARCHIVE_ENTRIES
    assert not extra, (
        f"The archive {ARCHIVE_PATH} contains unexpected entries: {extra}.\n"
        f"Expected only: {EXPECTED_ARCHIVE_ENTRIES}"
    )


def test_archive_top_level_directory_entry():
    """The top-level 'alerts/' directory entry must be present."""
    entries = _get_archive_entries()
    assert "alerts/" in entries, (
        f"The archive does not contain the top-level 'alerts/' directory entry.\n"
        f"Actual entries: {entries}"
    )


def test_archive_entry_count():
    entries = _get_archive_entries()
    assert len(entries) == 4, (
        f"Expected exactly 4 entries in the archive, found {len(entries)}.\n"
        f"Entries: {entries}"
    )


@pytest.mark.parametrize("entry,expected_content", EXPECTED_FILE_CONTENTS.items())
def test_archive_file_content(entry, expected_content):
    """Each yml file inside the archive should have the correct content."""
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        try:
            member = tf.getmember(entry)
        except KeyError:
            pytest.fail(
                f"Entry '{entry}' not found in archive {ARCHIVE_PATH}."
            )
        fh = tf.extractfile(member)
        assert fh is not None, f"Could not extract '{entry}' from archive."
        actual = fh.read().decode("utf-8").strip()
    assert actual == expected_content.strip(), (
        f"Content of '{entry}' in the archive is incorrect.\n"
        f"Expected:\n{expected_content}\n"
        f"Got:\n{actual}"
    )


# ── Manifest file ─────────────────────────────────────────────────────────────

def test_manifest_line_count():
    with open(MANIFEST_PATH, "r") as fh:
        content = fh.read()
    lines = content.split("\n")
    # A file with a trailing newline will have an empty string as the last element
    # wc -l counts newline characters, so 4 newlines == 4 lines
    newline_count = content.count("\n")
    assert newline_count == 4, (
        f"The manifest file {MANIFEST_PATH} should have exactly 4 lines "
        f"(4 newline characters), but `wc -l` equivalent gives {newline_count}.\n"
        f"File content:\n{content!r}"
    )


def test_manifest_contains_all_expected_entries():
    with open(MANIFEST_PATH, "r") as fh:
        content = fh.read()
    lines = [l for l in content.split("\n") if l]  # non-empty lines
    line_set = set(lines)
    missing = EXPECTED_ARCHIVE_ENTRIES - line_set
    assert not missing, (
        f"The manifest {MANIFEST_PATH} is missing the following entries: {missing}.\n"
        f"Actual lines: {lines}"
    )


def test_manifest_contains_no_extra_entries():
    with open(MANIFEST_PATH, "r") as fh:
        content = fh.read()
    lines = [l for l in content.split("\n") if l]
    line_set = set(lines)
    extra = line_set - EXPECTED_ARCHIVE_ENTRIES
    assert not extra, (
        f"The manifest {MANIFEST_PATH} contains unexpected entries: {extra}.\n"
        f"Expected only: {EXPECTED_ARCHIVE_ENTRIES}"
    )


def test_manifest_matches_archive_output():
    """The manifest must contain exactly the same lines as `tar -tzf` output."""
    archive_entries = _get_archive_entries()

    with open(MANIFEST_PATH, "r") as fh:
        content = fh.read()
    # Strip trailing newline for comparison, then split
    manifest_lines = content.rstrip("\n").split("\n")

    assert manifest_lines == archive_entries, (
        f"The manifest file does not match the `tar -tzf` output.\n"
        f"tar -tzf output : {archive_entries}\n"
        f"Manifest lines  : {manifest_lines}"
    )


def test_manifest_has_trailing_newline():
    """The manifest should end with a newline (standard text-file convention)."""
    with open(MANIFEST_PATH, "rb") as fh:
        data = fh.read()
    assert data.endswith(b"\n"), (
        f"The manifest file {MANIFEST_PATH} does not end with a trailing newline."
    )


# ── Cross-check: archive paths start with 'alerts/' not absolute paths ────────

def test_archive_paths_are_relative_and_prefixed():
    """All paths in the archive must start with 'alerts/' (not '/' or './alerts/')."""
    entries = _get_archive_entries()
    bad = [e for e in entries if not e.startswith("alerts")]
    assert not bad, (
        f"Some archive entries do not start with 'alerts/': {bad}.\n"
        "The archive should be created so that paths appear as 'alerts/filename'."
    )