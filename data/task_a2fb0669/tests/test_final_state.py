# test_final_state.py

import gzip
import io
import os
import subprocess
import tarfile
import pytest

ARTIFACTS_DIR = "/home/user/artifacts"
ARCHIVE_PATH = "/home/user/artifacts/pipeline_configs.tar.gz"
CONTENTS_TXT_PATH = "/home/user/artifacts/contents.txt"
PIPELINES_DIR = "/home/user/pipelines"

EXPECTED_YML_FILES = sorted(["build.yml", "deploy.yml", "notify.yml"])
NON_YML_FILES = ["README.txt", "debug.log"]


# ---------------------------------------------------------------------------
# Directory / file existence
# ---------------------------------------------------------------------------

def test_artifacts_directory_exists():
    assert os.path.isdir(ARTIFACTS_DIR), (
        f"The directory {ARTIFACTS_DIR} does not exist. "
        "It should have been created as part of the task."
    )


def test_archive_file_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"The archive file {ARCHIVE_PATH} does not exist. "
        "It should have been created as part of the task."
    )


def test_contents_txt_exists():
    assert os.path.isfile(CONTENTS_TXT_PATH), (
        f"The file {CONTENTS_TXT_PATH} does not exist. "
        "It should have been created as part of the task."
    )


# ---------------------------------------------------------------------------
# Archive validity
# ---------------------------------------------------------------------------

def test_archive_is_valid_gzip():
    """The archive must be a valid gzip file."""
    try:
        with gzip.open(ARCHIVE_PATH, "rb") as f:
            f.read(10)  # read a few bytes to confirm it's valid gzip
    except Exception as e:
        pytest.fail(
            f"{ARCHIVE_PATH} is not a valid gzip file: {e}"
        )


def test_archive_is_valid_tar():
    """The archive must be a valid tar archive (readable by tarfile)."""
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            _ = tf.getnames()
    except Exception as e:
        pytest.fail(
            f"{ARCHIVE_PATH} is not a valid gzip-compressed tar archive: {e}"
        )


# ---------------------------------------------------------------------------
# Archive contents — via tarfile
# ---------------------------------------------------------------------------

def _get_archive_members():
    """Return sorted list of member names from the archive."""
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        return sorted(tf.getnames())


def test_archive_contains_exactly_three_yml_files():
    members = _get_archive_members()
    assert len(members) == 3, (
        f"Expected exactly 3 files in the archive, but found {len(members)}: {members}"
    )


def test_archive_contains_correct_yml_files():
    members = _get_archive_members()
    assert members == EXPECTED_YML_FILES, (
        f"Archive contents do not match expected .yml files.\n"
        f"Expected: {EXPECTED_YML_FILES}\n"
        f"Actual:   {members}"
    )


def test_archive_files_have_no_path_prefix():
    """Files inside the archive must be stored as bare filenames (no directory prefix)."""
    members = _get_archive_members()
    for name in members:
        assert "/" not in name, (
            f"Archive member '{name}' contains a path separator. "
            "Files should be stored as bare filenames (e.g., 'build.yml'), "
            "not with a leading path (e.g., 'pipelines/build.yml')."
        )
        assert not name.startswith("./"), (
            f"Archive member '{name}' starts with './'. "
            "Files should be stored as bare filenames."
        )


def test_archive_does_not_contain_non_yml_files():
    members = _get_archive_members()
    for non_yml in NON_YML_FILES:
        assert non_yml not in members, (
            f"Non-YML file '{non_yml}' should NOT be in the archive, but it is. "
            f"Archive contents: {members}"
        )


# ---------------------------------------------------------------------------
# Archive contents — via `tar` command (matches verification commands in spec)
# ---------------------------------------------------------------------------

def test_tar_tzf_output_matches_expected():
    """
    `tar tzf /home/user/artifacts/pipeline_configs.tar.gz | sort`
    should output exactly the three bare yml filenames.
    """
    result = subprocess.run(
        ["tar", "tzf", ARCHIVE_PATH],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"`tar tzf {ARCHIVE_PATH}` failed with return code {result.returncode}.\n"
        f"stderr: {result.stderr}"
    )
    listed = sorted(result.stdout.strip().splitlines())
    assert listed == EXPECTED_YML_FILES, (
        f"`tar tzf {ARCHIVE_PATH} | sort` produced unexpected output.\n"
        f"Expected: {EXPECTED_YML_FILES}\n"
        f"Actual:   {listed}"
    )


# ---------------------------------------------------------------------------
# contents.txt
# ---------------------------------------------------------------------------

def test_contents_txt_exact_content():
    """
    contents.txt should contain exactly the three yml filenames,
    one per line, alphabetically sorted, newline-terminated.
    """
    with open(CONTENTS_TXT_PATH, "r") as f:
        raw = f.read()

    lines = raw.splitlines()

    # Check line count
    assert len(lines) == 3, (
        f"{CONTENTS_TXT_PATH} should have exactly 3 lines, but has {len(lines)}.\n"
        f"Actual content:\n{raw!r}"
    )

    # Check sorted order
    assert lines == sorted(lines), (
        f"Lines in {CONTENTS_TXT_PATH} are not sorted alphabetically.\n"
        f"Actual lines: {lines}"
    )

    # Check exact filenames
    assert lines == EXPECTED_YML_FILES, (
        f"{CONTENTS_TXT_PATH} does not contain the expected filenames.\n"
        f"Expected: {EXPECTED_YML_FILES}\n"
        f"Actual:   {lines}"
    )


def test_contents_txt_no_leading_dot_slash():
    """Filenames in contents.txt must not start with './'."""
    with open(CONTENTS_TXT_PATH, "r") as f:
        lines = f.read().splitlines()
    for line in lines:
        assert not line.startswith("./"), (
            f"Line '{line}' in {CONTENTS_TXT_PATH} starts with './', "
            "which is not allowed. Only bare filenames are expected."
        )


def test_contents_txt_no_extra_metadata():
    """Each line in contents.txt should be a bare filename with no spaces or extra metadata."""
    with open(CONTENTS_TXT_PATH, "r") as f:
        lines = f.read().splitlines()
    for line in lines:
        # A bare filename should not contain spaces (metadata lines do)
        assert " " not in line, (
            f"Line '{line}' in {CONTENTS_TXT_PATH} appears to contain metadata "
            "(spaces detected). Only bare filenames are expected (e.g., 'build.yml')."
        )
        # Should end with .yml
        assert line.endswith(".yml"), (
            f"Line '{line}' in {CONTENTS_TXT_PATH} does not end with '.yml'. "
            "Only .yml filenames are expected."
        )


def test_contents_txt_newline_terminated():
    """The file should be newline-terminated (last character is a newline)."""
    with open(CONTENTS_TXT_PATH, "r") as f:
        raw = f.read()
    assert raw.endswith("\n"), (
        f"{CONTENTS_TXT_PATH} is not newline-terminated. "
        f"Last character is: {raw[-1]!r}"
    )


def test_contents_txt_no_extra_whitespace_per_line():
    """Each line should have no leading or trailing whitespace."""
    with open(CONTENTS_TXT_PATH, "r") as f:
        lines = f.read().splitlines()
    for line in lines:
        assert line == line.strip(), (
            f"Line '{line!r}' in {CONTENTS_TXT_PATH} has leading or trailing whitespace."
        )


# ---------------------------------------------------------------------------
# Cross-check: archive contents match contents.txt
# ---------------------------------------------------------------------------

def test_archive_contents_match_contents_txt():
    """The files listed in contents.txt must exactly match the files in the archive."""
    archive_members = _get_archive_members()

    with open(CONTENTS_TXT_PATH, "r") as f:
        txt_lines = sorted(f.read().splitlines())

    assert archive_members == txt_lines, (
        f"The files in the archive do not match the listing in {CONTENTS_TXT_PATH}.\n"
        f"Archive members: {archive_members}\n"
        f"contents.txt lines: {txt_lines}"
    )


# ---------------------------------------------------------------------------
# Source files untouched
# ---------------------------------------------------------------------------

def test_source_yml_files_still_exist():
    """The original .yml files in /home/user/pipelines/ should still exist."""
    for filename in EXPECTED_YML_FILES:
        filepath = os.path.join(PIPELINES_DIR, filename)
        assert os.path.isfile(filepath), (
            f"Original source file {filepath} no longer exists. "
            "The task should archive, not move, the files."
        )


def test_source_non_yml_files_still_exist():
    """The non-YML files in /home/user/pipelines/ should still exist."""
    for filename in NON_YML_FILES:
        filepath = os.path.join(PIPELINES_DIR, filename)
        assert os.path.isfile(filepath), (
            f"Original source file {filepath} no longer exists. "
            "It should not have been removed."
        )