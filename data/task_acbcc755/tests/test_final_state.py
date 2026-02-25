# test_final_state.py

"""
Pytest suite to validate the FINAL state after completing the
docs_project archiving and extraction workflow.

Validates:
- Directory and file structure
- Gzipped file contents
- Tar archive contents and structure
- Extraction to restored directory
- extraction_log.txt content and correctness

Only uses Python standard library and pytest.
"""

import os
import stat
import gzip
import tarfile
import hashlib
import pytest

DOCS_PROJECT = "/home/user/docs_project"
FINAL_DRAFTS = os.path.join(DOCS_PROJECT, "final_drafts")
ARCHIVE = os.path.join(DOCS_PROJECT, "archive")
RESTORED = os.path.join(DOCS_PROJECT, "restored")
EXTRACTION_LOG = os.path.join(DOCS_PROJECT, "extraction_log.txt")

CHAPTERS = [
    ("chapter1.md", "# Chapter 1\nContent of chapter 1.\n"),
    ("chapter2.md", "# Chapter 2\nContent of chapter 2.\n"),
    ("chapter3.md", "# Chapter 3\nContent of chapter 3.\n"),
]

CHAPTER_GZ = [chapter + ".gz" for chapter, _ in CHAPTERS]
TAR_NAME = "project_chapters_backup.tar"
TAR_PATH = os.path.join(ARCHIVE, TAR_NAME)

@pytest.mark.order(1)
def test_archive_directory_exists_and_is_directory():
    assert os.path.isdir(ARCHIVE), (
        f"Expected directory {ARCHIVE} to exist after completion, but it does not."
    )

@pytest.mark.order(2)
@pytest.mark.parametrize("chapter_gz", CHAPTER_GZ)
def test_archive_gz_files_exist_and_are_files(chapter_gz):
    gz_path = os.path.join(ARCHIVE, chapter_gz)
    assert os.path.isfile(gz_path), (
        f"Expected compressed file {gz_path} to exist in archive."
    )

@pytest.mark.order(3)
@pytest.mark.parametrize("chapter, orig_content", CHAPTERS)
def test_archive_gz_files_content_matches_original(chapter, orig_content):
    gz_path = os.path.join(ARCHIVE, chapter + ".gz")
    assert os.path.isfile(gz_path), f"Missing file: {gz_path}"
    try:
        with gzip.open(gz_path, "rt", encoding="utf-8") as f:
            decompressed = f.read()
    except Exception as e:
        pytest.fail(f"Could not decompress {gz_path}: {e}")
    assert decompressed == orig_content, (
        f"Gzipped file {gz_path} does not decompress back to the original content.\n"
        "Expected:\n"
        f"{orig_content!r}\nGot:\n{decompressed!r}"
    )

@pytest.mark.order(4)
def test_archive_tar_exists_and_is_file():
    assert os.path.isfile(TAR_PATH), (
        f"Expected tar archive {TAR_PATH} to exist in archive directory."
    )

@pytest.mark.order(5)
def test_archive_tar_contents_exact_and_flat():
    assert os.path.isfile(TAR_PATH), f"Tar archive {TAR_PATH} is missing!"
    with tarfile.open(TAR_PATH, "r") as tar:
        names = tar.getnames()
        # The files must be present, no directories, and no extra files
        expected = sorted(CHAPTER_GZ)
        actual = sorted(names)
        assert actual == expected, (
            f"Tar archive {TAR_PATH} must contain exactly these files (flat, no subdirs):\n"
            f"{expected}\n"
            f"Found instead:\n{actual}"
        )
        # Ensure each is a file (not a directory)
        for member in tar.getmembers():
            assert member.isfile(), (
                f"Tar archive {TAR_PATH} contains non-file member {member.name}."
            )
        # Check no member has a path or directory component
        for name in names:
            assert os.path.sep not in name and "/" not in name, (
                f"Tar archive {TAR_PATH} contains file with directory path: {name!r}."
            )

@pytest.mark.order(6)
def test_tar_gz_files_are_identical_to_archive_gz_files():
    # For each .gz file in the tar, extract to memory and compare to archive file
    with tarfile.open(TAR_PATH, "r") as tar:
        for gz_name in CHAPTER_GZ:
            tar_member = tar.getmember(gz_name)
            tar_bytes = tar.extractfile(tar_member).read()
            archive_path = os.path.join(ARCHIVE, gz_name)
            with open(archive_path, "rb") as f:
                archive_bytes = f.read()
            assert tar_bytes == archive_bytes, (
                f"File {gz_name} inside {TAR_PATH} does not match the corresponding "
                f"compressed file in archive directory."
            )

@pytest.mark.order(7)
def test_restored_directory_exists_and_is_directory():
    assert os.path.isdir(RESTORED), (
        f"Expected directory {RESTORED} to exist after extraction."
    )

@pytest.mark.order(8)
@pytest.mark.parametrize("chapter_gz", CHAPTER_GZ)
def test_restored_gz_files_exist_and_are_files(chapter_gz):
    gz_path = os.path.join(RESTORED, chapter_gz)
    assert os.path.isfile(gz_path), (
        f"Expected file {gz_path} to exist in restored directory after extraction."
    )

@pytest.mark.order(9)
@pytest.mark.parametrize("chapter_gz", CHAPTER_GZ)
def test_restored_gz_files_identical_to_archive_gz(chapter_gz):
    archive_gz = os.path.join(ARCHIVE, chapter_gz)
    restored_gz = os.path.join(RESTORED, chapter_gz)
    with open(archive_gz, "rb") as f1, open(restored_gz, "rb") as f2:
        b1 = f1.read()
        b2 = f2.read()
    assert b1 == b2, (
        f"Restored file {restored_gz} does not have the same content as archive file {archive_gz}."
    )

@pytest.mark.order(10)
def test_extraction_log_exists_and_is_file():
    assert os.path.isfile(EXTRACTION_LOG), (
        f"Expected extraction log file {EXTRACTION_LOG} to exist after extraction."
    )

@pytest.mark.order(11)
def test_extraction_log_content_is_correct():
    expected_lines = sorted(CHAPTER_GZ)
    with open(EXTRACTION_LOG, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    assert lines == expected_lines, (
        f"{EXTRACTION_LOG} must contain exactly these lines, sorted, no extra whitespace or blank lines:\n"
        f"{expected_lines}\nGot:\n{lines}"
    )

@pytest.mark.order(12)
def test_extraction_log_lists_only_files_in_restored_dir():
    # Ensure that the log file matches exactly the .gz files present in the restored dir
    expected = sorted(CHAPTER_GZ)
    actual = sorted(
        f for f in os.listdir(RESTORED)
        if os.path.isfile(os.path.join(RESTORED, f)) and f.endswith(".gz")
    )
    with open(EXTRACTION_LOG, "r", encoding="utf-8") as f:
        log_lines = f.read().splitlines()
    assert log_lines == expected == actual, (
        f"extraction_log.txt does not match the .gz files actually present in {RESTORED}.\n"
        f"Expected (from restored dir): {expected}\n"
        f"Actual log lines: {log_lines}\n"
        f"Actual files: {actual}"
    )

@pytest.mark.order(13)
def test_no_extra_files_in_archive_directory():
    allowed = set(CHAPTER_GZ + [TAR_NAME])
    actual = set(os.listdir(ARCHIVE))
    extra = actual - allowed
    missing = allowed - actual
    assert not extra, (
        f"Found unexpected extra files in archive dir: {sorted(extra)}.\n"
        f"Allowed: {sorted(allowed)}"
    )
    assert not missing, (
        f"Missing files in archive dir: {sorted(missing)}.\n"
        f"Expected: {sorted(allowed)}"
    )

@pytest.mark.order(14)
def test_no_extra_files_in_restored_directory():
    allowed = set(CHAPTER_GZ)
    actual = set(
        f for f in os.listdir(RESTORED)
        if os.path.isfile(os.path.join(RESTORED, f))
    )
    extra = actual - allowed
    missing = allowed - actual
    assert not extra, (
        f"Found unexpected extra files in restored dir: {sorted(extra)}.\n"
        f"Allowed: {sorted(allowed)}"
    )
    assert not missing, (
        f"Missing files in restored dir: {sorted(missing)}.\n"
        f"Expected: {sorted(allowed)}"
    )