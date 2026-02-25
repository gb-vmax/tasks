# test_final_state.py

import os
import pytest

HOME = "/home/user"
DATA = os.path.join(HOME, "data")
RAW_IMAGES = os.path.join(DATA, "raw_images")
OLD = os.path.join(DATA, "old")
TEMP = os.path.join(DATA, "temp")
ORGANIZED = os.path.join(DATA, "organized")
ORG_CATS = os.path.join(ORGANIZED, "cats")
ORG_DOGS = os.path.join(ORGANIZED, "dogs")
ORG_BIRDS = os.path.join(ORGANIZED, "birds")
ARCHIVE = os.path.join(DATA, "archive")
ARCHIVE_OLD = os.path.join(ARCHIVE, "old")
ORG_LOG = os.path.join(DATA, "organization_log.txt")

# Expected filenames
CATS_IMAGES = {"cats_001.jpg", "cats_002.jpg"}
DOGS_IMAGES = {"dogs_001.jpg"}
BIRDS_IMAGES = {"birds_001.jpg"}
UNMOVED_IMAGES = {"testpic.jpg"}
OLD_FILES = {"notes.txt", "oldfile.csv"}
TEMP_FILES = {"tempdata1.txt", "tempdata2.csv"}

EXPECTED_LOG = """---
Datasets Organized: 2 cats images, 1 dogs images, 1 birds images
Old files archived to: /home/user/data/archive/old
Temporary files deleted: /home/user/data/temp
Directories created under /home/user/data/organized:
- cats
- dogs
- birds
---
"""


def test_organized_directory_structure_and_contents():
    # Check /home/user/data/organized exists with correct subdirectories
    assert os.path.isdir(ORGANIZED), (
        f"Directory {ORGANIZED} does not exist. It must be created."
    )
    for subdir, expected_files in [
        (ORG_CATS, CATS_IMAGES),
        (ORG_DOGS, DOGS_IMAGES),
        (ORG_BIRDS, BIRDS_IMAGES),
    ]:
        assert os.path.isdir(subdir), (
            f"Directory {subdir} does not exist. It must be created."
        )
        actual_files = set(os.listdir(subdir))
        missing = expected_files - actual_files
        extra = actual_files - expected_files
        assert not missing, (
            f"Missing files in {subdir}: {missing}. All expected images must be present."
        )
        assert not extra, (
            f"Unexpected files in {subdir}: {extra}. Only correct images should be present."
        )

def test_raw_images_directory_only_unmoved_remains():
    # Only testpic.jpg should be left
    assert os.path.isdir(RAW_IMAGES), (
        f"Directory {RAW_IMAGES} does not exist after task. It should remain."
    )
    actual_files = set(os.listdir(RAW_IMAGES))
    missing = UNMOVED_IMAGES - actual_files
    extra = actual_files - UNMOVED_IMAGES
    assert not missing, (
        f"File(s) {missing} missing from {RAW_IMAGES}. Only testpic.jpg should remain."
    )
    assert not extra, (
        f"Unexpected files in {RAW_IMAGES}: {extra}. Only testpic.jpg should remain."
    )

def test_organization_log_exists_and_content_exact():
    assert os.path.isfile(ORG_LOG), (
        f"File {ORG_LOG} does not exist. The summary log must be created."
    )
    with open(ORG_LOG, "r", encoding="utf-8") as f:
        content = f.read()
    # Compare exactly including dashes and newlines
    if content != EXPECTED_LOG:
        diff_lines = []
        expected_lines = EXPECTED_LOG.splitlines()
        actual_lines = content.splitlines()
        for i, (e, a) in enumerate(zip(expected_lines, actual_lines)):
            if e != a:
                diff_lines.append(f"Line {i+1} expected: {repr(e)} but got: {repr(a)}")
        if len(expected_lines) != len(actual_lines):
            diff_lines.append(f"Expected {len(expected_lines)} lines, got {len(actual_lines)} lines.")
        details = "\n".join(diff_lines)
        pytest.fail(
            f"Content of {ORG_LOG} does not match exactly.\n"
            f"Expected:\n{EXPECTED_LOG!r}\nActual:\n{content!r}\n"
            f"Difference(s):\n{details}"
        )

def test_old_directory_moved_to_archive():
    assert not os.path.exists(OLD), (
        f"Directory {OLD} should not exist after task. It must be moved to archive."
    )
    assert os.path.isdir(ARCHIVE_OLD), (
        f"Directory {ARCHIVE_OLD} does not exist. The 'old' directory must be moved here."
    )
    actual_files = set(os.listdir(ARCHIVE_OLD))
    missing = OLD_FILES - actual_files
    extra = actual_files - OLD_FILES
    assert not missing, (
        f"Missing file(s) in {ARCHIVE_OLD}: {missing}. All old files must be preserved."
    )
    assert not extra, (
        f"Unexpected files in {ARCHIVE_OLD}: {extra}. Only expected files should be present."
    )

def test_temp_directory_deleted():
    assert not os.path.exists(TEMP), (
        f"Directory {TEMP} should be deleted after task completion."
    )

def test_archive_directory_structure():
    assert os.path.isdir(ARCHIVE), (
        f"Directory {ARCHIVE} does not exist. It should contain the archived old directory."
    )
    # Only 'old' should be present in archive
    archive_contents = set(os.listdir(ARCHIVE))
    assert archive_contents == {"old"}, (
        f"Archive directory {ARCHIVE} should only contain 'old', but contains: {archive_contents}."
    )

def test_no_extra_files_or_dirs_created():
    # Check that only the specified new files/directories exist under /home/user/data
    expected_dirs = {"raw_images", "organized", "archive"}
    expected_files = {"organization_log.txt"}
    actual_items = set(os.listdir(DATA))
    actual_dirs = {item for item in actual_items if os.path.isdir(os.path.join(DATA, item))}
    actual_files = actual_items - actual_dirs
    missing_dirs = expected_dirs - actual_dirs
    missing_files = expected_files - actual_files
    extra_dirs = actual_dirs - expected_dirs
    extra_files = actual_files - expected_files
    assert not missing_dirs, (
        f"Missing expected directory(ies) under {DATA}: {missing_dirs}."
    )
    assert not missing_files, (
        f"Missing expected file(s) under {DATA}: {missing_files}."
    )
    assert not extra_dirs, (
        f"Unexpected directory(ies) under {DATA}: {extra_dirs}. Only raw_images, organized, archive should be present."
    )
    assert not extra_files, (
        f"Unexpected file(s) under {DATA}: {extra_files}. Only organization_log.txt should be present."
    )