# test_final_state.py

import os
import pytest

HOME = "/home/user"
WEBAPP_UPDATES = os.path.join(HOME, "webapp_updates")
DEPLOYMENTS_V2_1 = os.path.join(HOME, "deployments", "v2_1_release")
UPDATE_LOG = os.path.join(HOME, "update_log.txt")

MOVED_FILENAMES = ["app.js", "index.html", "style.css"]
MOVED_FILES_ABS = [os.path.join(DEPLOYMENTS_V2_1, fname) for fname in MOVED_FILENAMES]
ORIGINAL_FILES_ABS = [os.path.join(WEBAPP_UPDATES, fname) for fname in MOVED_FILENAMES]
OPTIONAL_SUBDIR = os.path.join(WEBAPP_UPDATES, "old_versions")

LOG_EXPECTED = "Moved files:\n" + "\n".join(sorted(MOVED_FILENAMES))

def test_deployments_v2_1_release_dir_exists():
    assert os.path.isdir(DEPLOYMENTS_V2_1), (
        f"Missing directory: {DEPLOYMENTS_V2_1}\n"
        "The directory was not created as required."
    )

@pytest.mark.parametrize("file_abs", MOVED_FILES_ABS)
def test_files_moved_to_new_directory(file_abs):
    assert os.path.isfile(file_abs), (
        f"Missing file in deployment directory: {file_abs}\n"
        "File was not moved to the new deployment directory."
    )

@pytest.mark.parametrize("file_abs", ORIGINAL_FILES_ABS)
def test_files_no_longer_in_webapp_updates(file_abs):
    assert not os.path.exists(file_abs), (
        f"File still exists in original location: {file_abs}\n"
        "This file should have been moved, not copied or left behind."
    )

def test_old_versions_subdir_untouched_if_exists():
    if os.path.exists(OPTIONAL_SUBDIR):
        assert os.path.isdir(OPTIONAL_SUBDIR), (
            f"{OPTIONAL_SUBDIR} exists but is not a directory.\n"
            "This subdirectory must remain untouched and as a directory."
        )
        # Ensure the directory was not moved
        expected_path = os.path.join(DEPLOYMENTS_V2_1, "old_versions")
        assert not os.path.exists(expected_path), (
            f"Directory {OPTIONAL_SUBDIR} was incorrectly moved to {expected_path}.\n"
            "Subdirectories must NOT be moved."
        )

def test_no_extra_files_moved():
    deployment_files = set(os.listdir(DEPLOYMENTS_V2_1))
    expected_files = set(MOVED_FILENAMES)
    unexpected_files = deployment_files - expected_files
    assert not unexpected_files, (
        f"Unexpected files found in {DEPLOYMENTS_V2_1}: {unexpected_files}\n"
        "Only the required files should be moved; no directories or extra files."
    )

def test_update_log_exists():
    assert os.path.isfile(UPDATE_LOG), (
        f"Missing log file: {UPDATE_LOG}\n"
        "The log file must be created as specified."
    )

def test_update_log_contents():
    if not os.path.isfile(UPDATE_LOG):
        pytest.skip("Log file does not exist; see previous test for details.")
    with open(UPDATE_LOG, encoding="utf-8") as f:
        contents = f.read()
    # Remove any trailing newline for strict matching
    contents_stripped = contents.rstrip('\n')
    assert contents_stripped == LOG_EXPECTED, (
        f"Log file contents are incorrect.\n"
        f"Expected exactly:\n\n{LOG_EXPECTED}\n\nBut got:\n\n{contents}\n"
        "The log file must contain the header 'Moved files:' followed by the "
        "alphabetically sorted file names, one per line, with no extra whitespace or blank lines."
    )

def test_log_no_extra_lines():
    with open(UPDATE_LOG, encoding="utf-8") as f:
        lines = f.readlines()
    # Remove trailing newlines for comparison
    stripped_lines = [line.rstrip('\n') for line in lines]
    expected_lines = ["Moved files:"] + sorted(MOVED_FILENAMES)
    assert stripped_lines == expected_lines, (
        f"Log file lines incorrect.\n"
        f"Expected lines:\n{expected_lines}\nGot lines:\n{stripped_lines}\n"
        "The log file must have exactly one header line and one line per moved file (names only), no extra or missing lines."
    )