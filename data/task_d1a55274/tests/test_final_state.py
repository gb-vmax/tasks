# test_final_state.py

import os
import subprocess
import tarfile
import gzip
import pytest

ARCHIVE_PATH = "/home/user/backups/website_backup.tar.gz"
MANIFEST_PATH = "/home/user/backups/website_backup.manifest"
BACKUPS_DIR = "/home/user/backups"

EXPECTED_FILES = {
    "website/index.html",
    "website/style.css",
    "website/src/app.js",
    "website/src/utils.js",
    "website/config/nginx.conf",
    "website/config/env.cfg",
}

EXPECTED_DIRS = {
    "website/",
    "website/src/",
    "website/config/",
}

EXPECTED_ALL_ENTRIES = EXPECTED_FILES | EXPECTED_DIRS


def test_backups_directory_exists():
    assert os.path.isdir(BACKUPS_DIR), (
        f"Backups directory {BACKUPS_DIR} does not exist. "
        "It should have been created as part of the task."
    )


def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive {ARCHIVE_PATH} does not exist. "
        "The gzip-compressed tar archive must be created at this path."
    )


def test_manifest_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Manifest file {MANIFEST_PATH} does not exist. "
        "The verification manifest must be created at this path."
    )


def test_archive_is_valid_gzip():
    """Verify the archive is a valid gzip file."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    try:
        with gzip.open(ARCHIVE_PATH, 'rb') as f:
            f.read(10)  # Read a few bytes to confirm it's valid gzip
    except (OSError, gzip.BadGzipFile) as e:
        pytest.fail(
            f"Archive {ARCHIVE_PATH} is not a valid gzip file: {e}"
        )


def test_archive_is_valid_tar():
    """Verify the archive is a valid gzip-compressed tar archive."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            members = tf.getnames()
    except tarfile.TarError as e:
        pytest.fail(
            f"Archive {ARCHIVE_PATH} is not a valid tar archive: {e}"
        )
    assert len(members) > 0, (
        f"Archive {ARCHIVE_PATH} is empty — no members found."
    )


def get_archive_entries():
    """Return list of entries from the archive using tar -tzf."""
    result = subprocess.run(
        ["tar", "-tzf", ARCHIVE_PATH],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, (
        f"'tar -tzf {ARCHIVE_PATH}' failed with return code {result.returncode}.\n"
        f"stderr: {result.stderr}"
    )
    return result.stdout


def test_archive_listable_with_tar():
    """Verify the archive can be listed with tar -tzf."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    output = get_archive_entries()
    assert output.strip(), (
        f"'tar -tzf {ARCHIVE_PATH}' produced empty output — archive may be corrupt or empty."
    )


def test_manifest_matches_tar_output():
    """Verify the manifest file exactly matches the output of tar -tzf."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    assert os.path.isfile(MANIFEST_PATH), f"Manifest {MANIFEST_PATH} does not exist."

    tar_output = get_archive_entries()

    with open(MANIFEST_PATH, "r") as f:
        manifest_content = f.read()

    assert manifest_content == tar_output, (
        f"Manifest file content does not exactly match 'tar -tzf' output.\n"
        f"Expected (tar output):\n{tar_output!r}\n"
        f"Got (manifest content):\n{manifest_content!r}"
    )


def test_all_expected_files_in_archive():
    """Verify all 6 expected files are present in the archive."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    tar_output = get_archive_entries()
    entries = set(tar_output.strip().splitlines())

    missing_files = EXPECTED_FILES - entries
    assert not missing_files, (
        f"The following expected files are missing from the archive:\n"
        + "\n".join(sorted(missing_files))
    )


def test_all_expected_dirs_in_archive():
    """Verify expected directory entries are present in the archive."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    tar_output = get_archive_entries()
    entries = set(tar_output.strip().splitlines())

    missing_dirs = EXPECTED_DIRS - entries
    assert not missing_dirs, (
        f"The following expected directory entries are missing from the archive:\n"
        + "\n".join(sorted(missing_dirs))
    )


def test_no_absolute_paths_in_archive():
    """Verify no entries in the archive use absolute paths."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    tar_output = get_archive_entries()
    entries = tar_output.strip().splitlines()

    absolute_entries = [e for e in entries if e.startswith("/")]
    assert not absolute_entries, (
        f"Archive contains entries with absolute paths (should be relative, starting with 'website/'):\n"
        + "\n".join(absolute_entries)
    )


def test_no_home_paths_in_archive():
    """Verify no entries contain /home or similar absolute prefixes."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    tar_output = get_archive_entries()
    entries = tar_output.strip().splitlines()

    bad_entries = [e for e in entries if "home" in e.lower() and e.startswith("/")]
    assert not bad_entries, (
        f"Archive contains absolute paths referencing /home:\n"
        + "\n".join(bad_entries)
    )


def test_all_entries_start_with_website():
    """Verify all archive entries start with 'website/' (relative paths)."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    tar_output = get_archive_entries()
    entries = tar_output.strip().splitlines()

    bad_entries = [e for e in entries if not e.startswith("website/") and e != "website"]
    assert not bad_entries, (
        f"Archive contains entries that do not start with 'website/':\n"
        + "\n".join(bad_entries)
        + "\nAll paths must be relative and start with 'website/'."
    )


def test_archive_file_contents_correct():
    """Verify the actual file contents inside the archive are correct."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."

    expected_contents = {
        "website/index.html": "<html><body>Hello</body></html>\n",
        "website/style.css": "body { margin: 0; }\n",
        "website/src/app.js": "console.log('app');\n",
        "website/src/utils.js": "function helper() {}\n",
        "website/config/nginx.conf": "server { listen 80; }\n",
        "website/config/env.cfg": "ENV=production\n",
    }

    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        for member_path, expected_content in expected_contents.items():
            try:
                member = tf.getmember(member_path)
            except KeyError:
                pytest.fail(
                    f"Expected member '{member_path}' not found in archive {ARCHIVE_PATH}."
                )
            f = tf.extractfile(member)
            assert f is not None, (
                f"Could not extract file '{member_path}' from archive."
            )
            actual_content = f.read().decode("utf-8")
            assert actual_content == expected_content, (
                f"File '{member_path}' in archive has wrong content.\n"
                f"Expected: {expected_content!r}\n"
                f"Got:      {actual_content!r}"
            )


def test_manifest_contains_no_extra_content():
    """Verify the manifest has no headers, footers, or commentary — just file listing."""
    assert os.path.isfile(MANIFEST_PATH), f"Manifest {MANIFEST_PATH} does not exist."

    with open(MANIFEST_PATH, "r") as f:
        lines = f.readlines()

    for line in lines:
        stripped = line.rstrip("\n")
        # Each line should look like a path entry (starts with website/ or is empty at end)
        if stripped == "":
            continue
        assert stripped.startswith("website/") or stripped == "website", (
            f"Manifest contains an unexpected line that doesn't look like a tar entry:\n"
            f"  {stripped!r}\n"
            "The manifest should contain only the raw output of 'tar -tzf', "
            "with no headers, footers, or commentary."
        )


def test_archive_entry_count():
    """Verify the archive contains the expected number of entries (files + dirs)."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    tar_output = get_archive_entries()
    entries = [e for e in tar_output.strip().splitlines() if e]

    # We expect at minimum: website/, website/src/, website/config/, and 6 files = 9 entries
    assert len(entries) >= 9, (
        f"Archive has fewer entries than expected. "
        f"Expected at least 9 (3 dirs + 6 files), got {len(entries)}.\n"
        f"Entries found: {entries}"
    )