# test_final_state.py

import os
import pytest

HOME = "/home/user"
PROJECT_DIR = os.path.join(HOME, "my_python_project")
SRC_DIR = os.path.join(PROJECT_DIR, "src")
TESTS_DIR = os.path.join(PROJECT_DIR, "tests")
STRUCTURE_FILE = os.path.join(PROJECT_DIR, "project_structure.txt")
EXPECTED_STRUCTURE_LINES = [
    ".",
    "./src",
    "./tests",
    "./project_structure.txt",
]

def test_project_directory_exists_and_is_directory():
    assert os.path.exists(PROJECT_DIR), (
        f"The directory '{PROJECT_DIR}' does not exist. "
        "You must create 'my_python_project' in '/home/user'."
    )
    assert os.path.isdir(PROJECT_DIR), (
        f"'{PROJECT_DIR}' exists but is not a directory."
    )

def test_src_directory_exists_and_empty():
    assert os.path.exists(SRC_DIR), (
        f"The directory '{SRC_DIR}' does not exist. "
        "You must create an empty 'src' subdirectory."
    )
    assert os.path.isdir(SRC_DIR), (
        f"'{SRC_DIR}' exists but is not a directory."
    )
    contents = os.listdir(SRC_DIR)
    assert contents == [], (
        f"'{SRC_DIR}' is not empty. It should be empty but contains: {contents}"
    )

def test_tests_directory_exists_and_empty():
    assert os.path.exists(TESTS_DIR), (
        f"The directory '{TESTS_DIR}' does not exist. "
        "You must create an empty 'tests' subdirectory."
    )
    assert os.path.isdir(TESTS_DIR), (
        f"'{TESTS_DIR}' exists but is not a directory."
    )
    contents = os.listdir(TESTS_DIR)
    assert contents == [], (
        f"'{TESTS_DIR}' is not empty. It should be empty but contains: {contents}"
    )

def test_project_structure_txt_exists_and_correct_content():
    assert os.path.exists(STRUCTURE_FILE), (
        f"The file '{STRUCTURE_FILE}' does not exist. "
        "You must create 'project_structure.txt' in the project directory."
    )
    assert os.path.isfile(STRUCTURE_FILE), (
        f"'{STRUCTURE_FILE}' exists but is not a file."
    )
    with open(STRUCTURE_FILE, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert lines == EXPECTED_STRUCTURE_LINES, (
        f"The contents of '{STRUCTURE_FILE}' are incorrect.\n"
        "Expected exactly:\n"
        + "\n".join(EXPECTED_STRUCTURE_LINES)
        + "\nBut got:\n"
        + "\n".join(lines)
    )

def test_no_extra_files_or_directories_in_project_dir():
    expected = {"src", "tests", "project_structure.txt"}
    actual = set(os.listdir(PROJECT_DIR))
    extra = actual - expected
    missing = expected - actual
    assert not missing, (
        f"The following required items are missing from '{PROJECT_DIR}': {sorted(missing)}"
    )
    assert not extra, (
        f"The following unexpected items are present in '{PROJECT_DIR}': {sorted(extra)}"
    )