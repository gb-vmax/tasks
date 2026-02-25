# test_final_state.py

import os
import pytest

DEV_PROJECT = "/home/user/dev_project"

# Expected subdirectories and their expected files
EXPECTED_STRUCTURE = {
    "src": ["main.py", "utils.py"],
    "tests": ["test_main.py"],
    "docs": ["README.md"],
    "data": ["data.csv"],
}

# Files that must remain in the root
EXPECTED_ROOT_FILES = [
    "requirements.txt",
    "organization_log.txt",
]

# The log file and its expected exact contents
ORGANIZATION_LOG = os.path.join(DEV_PROJECT, "organization_log.txt")
EXPECTED_LOG_LINES = [
    "Moved /home/user/dev_project/main.py to /home/user/dev_project/src/main.py",
    "Moved /home/user/dev_project/utils.py to /home/user/dev_project/src/utils.py",
    "Moved /home/user/dev_project/test_main.py to /home/user/dev_project/tests/test_main.py",
    "Moved /home/user/dev_project/README.md to /home/user/dev_project/docs/README.md",
    "Moved /home/user/dev_project/data.csv to /home/user/dev_project/data/data.csv",
]


def abs_path(filename):
    return os.path.join(DEV_PROJECT, filename)


def test_expected_subdirectories_exist_and_are_directories():
    for subdir in EXPECTED_STRUCTURE:
        path = os.path.join(DEV_PROJECT, subdir)
        assert os.path.isdir(path), (
            f"Missing subdirectory: {path}. "
            "Make sure you created all required subdirectories: src, tests, docs, data."
        )


@pytest.mark.parametrize("subdir,files", EXPECTED_STRUCTURE.items())
def test_expected_files_in_subdirectories(subdir, files):
    subdir_path = os.path.join(DEV_PROJECT, subdir)
    for fname in files:
        file_path = os.path.join(subdir_path, fname)
        assert os.path.isfile(file_path), (
            f"Expected file {file_path} not found in subdirectory {subdir}. "
            "Make sure you moved the correct files to their designated subdirectories."
        )


def test_no_extra_files_in_subdirectories():
    # Ensure only expected files are present in each subdir
    for subdir, expected_files in EXPECTED_STRUCTURE.items():
        subdir_path = os.path.join(DEV_PROJECT, subdir)
        actual_files = sorted([
            f for f in os.listdir(subdir_path)
            if os.path.isfile(os.path.join(subdir_path, f))
        ])
        expected_files_sorted = sorted(expected_files)
        assert actual_files == expected_files_sorted, (
            f"Subdirectory {subdir_path} contains unexpected files: {actual_files}. "
            f"Expected only: {expected_files_sorted}."
        )


def test_root_files_correct():
    root_files = [
        f for f in os.listdir(DEV_PROJECT)
        if os.path.isfile(os.path.join(DEV_PROJECT, f))
    ]
    # Only expected root files should remain (requirements.txt and organization_log.txt)
    for fname in EXPECTED_ROOT_FILES:
        assert fname in root_files, (
            f"Expected file {fname} not found in project root."
        )
    # No other files should be present in root except the subdirs and these two files
    allowed = set(EXPECTED_ROOT_FILES + list(EXPECTED_STRUCTURE.keys()))
    unexpected = [f for f in root_files if f not in EXPECTED_ROOT_FILES]
    assert not unexpected, (
        f"Unexpected files found in project root: {unexpected}. "
        "Only requirements.txt and organization_log.txt should remain in the root."
    )


def test_files_not_duplicated():
    # Ensure each file appears only in its new location, not duplicated elsewhere
    moved_files = {
        "main.py": os.path.join(DEV_PROJECT, "src", "main.py"),
        "utils.py": os.path.join(DEV_PROJECT, "src", "utils.py"),
        "test_main.py": os.path.join(DEV_PROJECT, "tests", "test_main.py"),
        "README.md": os.path.join(DEV_PROJECT, "docs", "README.md"),
        "data.csv": os.path.join(DEV_PROJECT, "data", "data.csv"),
    }
    for fname, expected_path in moved_files.items():
        # Should not exist in root
        root_path = os.path.join(DEV_PROJECT, fname)
        assert not os.path.exists(root_path), (
            f"File {fname} still exists in project root. "
            "It should only be present in its designated subdirectory."
        )
        # Should exist in new location
        assert os.path.isfile(expected_path), (
            f"File {fname} not found at expected location {expected_path}."
        )


def test_requirements_txt_not_moved():
    req_path = os.path.join(DEV_PROJECT, "requirements.txt")
    assert os.path.isfile(req_path), (
        "requirements.txt not found in project root. "
        "It should remain in /home/user/dev_project and not be moved."
    )
    # Should not exist in any subdirectory
    for subdir in EXPECTED_STRUCTURE:
        subdir_path = os.path.join(DEV_PROJECT, subdir)
        assert not os.path.exists(os.path.join(subdir_path, "requirements.txt")), (
            f"requirements.txt should not be present in {subdir_path}."
        )


def test_organization_log_exists():
    assert os.path.isfile(ORGANIZATION_LOG), (
        "organization_log.txt not found in project root. "
        "Ensure you created the log file at /home/user/dev_project/organization_log.txt."
    )


def test_organization_log_contents_exact():
    with open(ORGANIZATION_LOG, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]
    assert lines == EXPECTED_LOG_LINES, (
        "organization_log.txt contents are incorrect.\n"
        "Expected:\n" +
        "\n".join(EXPECTED_LOG_LINES) +
        "\n\nFound:\n" +
        "\n".join(lines)
    )


def test_files_contents_preserved():
    """
    Ensure that the contents of each file have not changed after moving.
    This test can only check that files exist and are non-empty (since contents are arbitrary),
    but it helps catch overwriting or truncation mistakes.
    """
    # All files except organization_log.txt (which is generated) must be non-empty
    for subdir, files in EXPECTED_STRUCTURE.items():
        for fname in files:
            fpath = os.path.join(DEV_PROJECT, subdir, fname)
            assert os.path.getsize(fpath) > 0, (
                f"File {fpath} is empty after moving. Ensure you preserved its original contents."
            )
    req_path = os.path.join(DEV_PROJECT, "requirements.txt")
    assert os.path.getsize(req_path) > 0, (
        "requirements.txt is empty after organizing. Ensure its contents were not changed."
    )


def test_no_extra_directories_in_project_root():
    # Only expected subdirectories and files in root
    entries = set(os.listdir(DEV_PROJECT))
    allowed = set(EXPECTED_ROOT_FILES + list(EXPECTED_STRUCTURE.keys()))
    extra_dirs = [
        e for e in entries
        if os.path.isdir(os.path.join(DEV_PROJECT, e)) and e not in EXPECTED_STRUCTURE
    ]
    assert not extra_dirs, (
        f"Unexpected directories found in project root: {extra_dirs}. "
        f"Only {list(EXPECTED_STRUCTURE.keys())} should be present."
    )