# test_final_state.py

import os
import tarfile
import pytest

BACKUPS_DIR = "/home/user/backups"
ARCHIVE_PATH = "/home/user/backups/app-jan2024.tar.gz"
MANIFEST_PATH = "/home/user/backups/app-jan2024.manifest"
LOGS_DIR = "/home/user/logs"

EXPECTED_ARCHIVE_FILES = [
    "app-2024-01-01.log",
    "app-2024-01-15.log",
    "app-2024-01-31.log",
]

EXCLUDED_FILES = [
    "app-2024-02-01.log",
    "system.log",
]

EXPECTED_MANIFEST_CONTENT = (
    "app-2024-01-01.log\n"
    "app-2024-01-15.log\n"
    "app-2024-01-31.log\n"
)

EXPECTED_LOG_CONTENTS = {
    "app-2024-01-01.log": "2024-01-01 00:00:01 INFO Service started\n2024-01-01 08:32:11 ERROR Disk quota exceeded\n",
    "app-2024-01-15.log": "2024-01-15 14:22:05 WARN Connection timeout\n2024-01-15 14:22:10 INFO Reconnected\n",
    "app-2024-01-31.log": "2024-01-31 23:59:59 INFO Scheduled maintenance\n",
}


def test_backups_directory_exists():
    assert os.path.isdir(BACKUPS_DIR), (
        f"The backups directory '{BACKUPS_DIR}' does not exist. "
        "You need to create it as part of the task."
    )


def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"The archive file '{ARCHIVE_PATH}' does not exist. "
        "Create a gzip-compressed tar archive at this path."
    )


def test_archive_is_valid_gzip_tar():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Cannot validate archive: '{ARCHIVE_PATH}' does not exist."
    )
    assert tarfile.is_tarfile(ARCHIVE_PATH), (
        f"'{ARCHIVE_PATH}' is not a valid tar file."
    )
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            _ = tf.getnames()
    except Exception as e:
        pytest.fail(
            f"'{ARCHIVE_PATH}' could not be opened as a gzip-compressed tar archive: {e}"
        )


def test_archive_contains_exactly_expected_files():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Cannot check archive contents: '{ARCHIVE_PATH}' does not exist."
    )
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        names = tf.getnames()

    names_set = set(names)
    expected_set = set(EXPECTED_ARCHIVE_FILES)

    missing = expected_set - names_set
    extra = names_set - expected_set

    assert not missing, (
        f"Archive '{ARCHIVE_PATH}' is missing expected files: {sorted(missing)}"
    )
    assert not extra, (
        f"Archive '{ARCHIVE_PATH}' contains unexpected files: {sorted(extra)}. "
        "Only January 2024 log files should be included."
    )


def test_archive_does_not_contain_excluded_files():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Cannot check archive contents: '{ARCHIVE_PATH}' does not exist."
    )
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        names = tf.getnames()

    names_set = set(names)
    for excluded in EXCLUDED_FILES:
        assert excluded not in names_set, (
            f"Archive '{ARCHIVE_PATH}' incorrectly contains '{excluded}', "
            "which should be excluded (only app-2024-01-*.log files are allowed)."
        )


def test_archive_files_have_bare_filenames_no_path_prefix():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Cannot check archive contents: '{ARCHIVE_PATH}' does not exist."
    )
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        names = tf.getnames()

    for name in names:
        assert "/" not in name, (
            f"Archive entry '{name}' contains a directory path prefix. "
            "Files should be archived with bare filenames only "
            "(e.g., 'app-2024-01-01.log', not 'home/user/logs/app-2024-01-01.log')."
        )
        assert not name.startswith("./"), (
            f"Archive entry '{name}' starts with './'. "
            "Files should be archived with bare filenames only."
        )


def test_archive_contains_exactly_three_files():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Cannot check archive: '{ARCHIVE_PATH}' does not exist."
    )
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        names = tf.getnames()

    assert len(names) == 3, (
        f"Archive '{ARCHIVE_PATH}' should contain exactly 3 files, "
        f"but contains {len(names)}: {names}"
    )


def test_archive_file_contents_are_correct():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Cannot check archive file contents: '{ARCHIVE_PATH}' does not exist."
    )
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        for filename, expected_content in EXPECTED_LOG_CONTENTS.items():
            try:
                member = tf.getmember(filename)
            except KeyError:
                pytest.fail(
                    f"Archive '{ARCHIVE_PATH}' does not contain '{filename}'."
                )
            f = tf.extractfile(member)
            assert f is not None, (
                f"Could not extract '{filename}' from archive '{ARCHIVE_PATH}'."
            )
            actual_content = f.read().decode("utf-8")
            assert actual_content == expected_content, (
                f"Content of '{filename}' in archive does not match expected.\n"
                f"Expected: {expected_content!r}\n"
                f"Got:      {actual_content!r}"
            )


def test_manifest_file_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"The manifest file '{MANIFEST_PATH}' does not exist. "
        "Create it by running 'tar -tzf' on the archive and redirecting output to this file."
    )


def test_manifest_exact_content():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Cannot check manifest content: '{MANIFEST_PATH}' does not exist."
    )
    with open(MANIFEST_PATH, "r") as f:
        actual_content = f.read()

    assert actual_content == EXPECTED_MANIFEST_CONTENT, (
        f"Manifest file '{MANIFEST_PATH}' has unexpected content.\n"
        f"Expected: {EXPECTED_MANIFEST_CONTENT!r}\n"
        f"Got:      {actual_content!r}\n"
        "The manifest must contain exactly the filenames from the archive, "
        "one per line (alphabetical order), with a trailing newline."
    )


def test_manifest_has_exactly_three_lines():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Cannot check manifest: '{MANIFEST_PATH}' does not exist."
    )
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines()
    assert len(lines) == 3, (
        f"Manifest '{MANIFEST_PATH}' should have exactly 3 lines, "
        f"but has {len(lines)}. Lines: {lines}"
    )


def test_manifest_has_trailing_newline():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Cannot check manifest: '{MANIFEST_PATH}' does not exist."
    )
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()

    assert content.endswith("\n"), (
        f"Manifest '{MANIFEST_PATH}' should end with a trailing newline "
        "(standard shell redirection output), but it does not."
    )


def test_manifest_lines_match_expected_filenames():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Cannot check manifest: '{MANIFEST_PATH}' does not exist."
    )
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines()
    assert lines == EXPECTED_ARCHIVE_FILES, (
        f"Manifest lines do not match expected filenames.\n"
        f"Expected: {EXPECTED_ARCHIVE_FILES}\n"
        f"Got:      {lines}"
    )


def test_manifest_does_not_contain_excluded_files():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Cannot check manifest: '{MANIFEST_PATH}' does not exist."
    )
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines()
    for excluded in EXCLUDED_FILES:
        assert excluded not in lines, (
            f"Manifest '{MANIFEST_PATH}' incorrectly lists '{excluded}'. "
            "Only January 2024 log files should appear in the manifest."
        )


def test_original_log_files_still_exist():
    """Ensure the original log files in /home/user/logs/ were not removed."""
    for filename in EXPECTED_LOG_CONTENTS:
        filepath = os.path.join(LOGS_DIR, filename)
        assert os.path.isfile(filepath), (
            f"Original log file '{filepath}' no longer exists. "
            "The task requires archiving (copying), not moving the files."
        )


def test_manifest_matches_archive_contents():
    """Cross-check: manifest content must exactly match what tar -tzf reports."""
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Cannot cross-check: archive '{ARCHIVE_PATH}' does not exist."
    )
    assert os.path.isfile(MANIFEST_PATH), (
        f"Cannot cross-check: manifest '{MANIFEST_PATH}' does not exist."
    )

    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        archive_names = tf.getnames()

    with open(MANIFEST_PATH, "r") as f:
        manifest_lines = f.read().splitlines()

    assert archive_names == manifest_lines, (
        f"Manifest content does not match archive contents.\n"
        f"Archive contains (in order): {archive_names}\n"
        f"Manifest lists (in order):   {manifest_lines}\n"
        "The manifest must be produced by 'tar -tzf' on the archive."
    )