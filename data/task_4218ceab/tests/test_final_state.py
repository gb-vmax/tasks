# test_final_state.py

import os
import pytest

HOME = "/home/user"
DATASETS_DIR = os.path.join(HOME, "datasets")
TRAIN_DIR = os.path.join(DATASETS_DIR, "train")
TEST_DIR = os.path.join(DATASETS_DIR, "test")
VALIDATION_DIR = os.path.join(DATASETS_DIR, "validation")
SUMMARY_FILE = os.path.join(HOME, "dataset_summary.txt")

EXPECTED_SUMMARY_CONTENT = (
    f"{TRAIN_DIR}\n{TEST_DIR}\n{VALIDATION_DIR}"
)

@pytest.mark.parametrize("directory", [DATASETS_DIR])
def test_datasets_directory_exists(directory):
    assert os.path.isdir(directory), (
        f"Directory '{directory}' does not exist, but it must exist after task completion."
    )

@pytest.mark.parametrize(
    "subdir",
    [
        TRAIN_DIR,
        TEST_DIR,
        VALIDATION_DIR,
    ],
)
def test_datasets_subdirectories_exist_and_empty(subdir):
    assert os.path.isdir(subdir), (
        f"Subdirectory '{subdir}' does not exist, but it must exist after task completion."
    )
    entries = os.listdir(subdir)
    assert entries == [], (
        f"Subdirectory '{subdir}' is not empty; found: {entries}. It must be empty."
    )

def test_dataset_summary_file_exists_and_permissions():
    assert os.path.isfile(SUMMARY_FILE), (
        f"Summary file '{SUMMARY_FILE}' does not exist, but it must exist after task completion."
    )
    assert os.access(SUMMARY_FILE, os.R_OK), (
        f"Summary file '{SUMMARY_FILE}' is not readable by the user."
    )
    assert os.access(SUMMARY_FILE, os.W_OK), (
        f"Summary file '{SUMMARY_FILE}' is not writable by the user."
    )

def test_dataset_summary_file_contents_exact():
    assert os.path.isfile(SUMMARY_FILE), (
        f"Summary file '{SUMMARY_FILE}' does not exist, so its contents cannot be checked."
    )
    with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    # Check for extra blank lines at the start or end
    lines = content.splitlines()
    expected_lines = EXPECTED_SUMMARY_CONTENT.splitlines()
    assert lines == expected_lines, (
        f"Contents of '{SUMMARY_FILE}' do not match the required format.\n"
        f"Expected ({len(expected_lines)} lines):\n{EXPECTED_SUMMARY_CONTENT}\n\n"
        f"Found ({len(lines)} lines):\n{content}"
    )