# test_final_state.py

import os
import tarfile
import gzip
import pytest

BACKUPS_DIR = "/home/user/backups"
ARCHIVE_PATH = "/home/user/backups/experiment_42_data.tar.gz"
MANIFEST_PATH = "/home/user/backups/experiment_42_manifest.txt"
EXPERIMENT_DIR = "/home/user/datasets/experiment_42"

EXPECTED_CSV_FILES = ["measurements_a.csv", "measurements_b.csv", "results_final.csv"]
NON_CSV_FILES = ["lab_notes.txt", "run.log"]

EXPECTED_CSV_CONTENTS = {
    "measurements_a.csv": "time,value\n0,1.2\n1,3.4\n2,5.6\n",
    "measurements_b.csv": "time,value\n0,7.8\n1,9.0\n2,1.1\n",
    "results_final.csv": "sample,mean,stddev\nA,2.07,1.83\nB,5.97,0.75\n",
}


def test_backups_directory_exists():
    assert os.path.isdir(BACKUPS_DIR), (
        f"The backups directory '{BACKUPS_DIR}' does not exist. "
        "It should have been created as part of the task."
    )


def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"The archive file '{ARCHIVE_PATH}' does not exist. "
        "It should have been created as part of the task."
    )


def test_archive_is_valid_gzip():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    try:
        with gzip.open(ARCHIVE_PATH, 'rb') as f:
            f.read(10)
    except Exception as e:
        pytest.fail(
            f"The archive '{ARCHIVE_PATH}' is not a valid gzip file. Error: {e}"
        )


def test_archive_is_valid_tar_gz():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    assert tarfile.is_tarfile(ARCHIVE_PATH), (
        f"The file '{ARCHIVE_PATH}' is not a valid tar archive."
    )


def test_archive_contains_exactly_csv_files():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tar:
        members = tar.getnames()
    assert sorted(members) == sorted(EXPECTED_CSV_FILES), (
        f"Archive '{ARCHIVE_PATH}' contains unexpected files.\n"
        f"Expected: {sorted(EXPECTED_CSV_FILES)}\n"
        f"Actual:   {sorted(members)}"
    )


def test_archive_does_not_contain_non_csv_files():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tar:
        members = tar.getnames()
    for non_csv in NON_CSV_FILES:
        assert non_csv not in members, (
            f"Non-CSV file '{non_csv}' was found in the archive '{ARCHIVE_PATH}'. "
            "Only .csv files should be included."
        )


def test_archive_file_paths_are_relative_filenames_only():
    """Files in the archive should be stored as bare filenames, not full or relative paths."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tar:
        members = tar.getnames()
    for member in members:
        # Should not start with '/', './', or contain directory separators
        assert not member.startswith("/"), (
            f"Archive member '{member}' has an absolute path. "
            "Files should be stored with just their filenames."
        )
        assert not member.startswith("./"), (
            f"Archive member '{member}' starts with './'. "
            "Files should be stored with just their filenames (e.g., 'results_final.csv')."
        )
        assert "/" not in member, (
            f"Archive member '{member}' contains a directory separator. "
            "Files should be stored with just their filenames, no directory components."
        )


def test_archive_csv_file_contents_are_correct():
    """Verify the actual content of CSV files inside the archive."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tar:
        for csv_name, expected_content in EXPECTED_CSV_CONTENTS.items():
            try:
                member = tar.getmember(csv_name)
            except KeyError:
                pytest.fail(
                    f"Expected CSV file '{csv_name}' not found in archive '{ARCHIVE_PATH}'."
                )
            f = tar.extractfile(member)
            assert f is not None, (
                f"Could not extract '{csv_name}' from archive '{ARCHIVE_PATH}'."
            )
            actual_content = f.read().decode("utf-8")
            # Normalize: strip trailing newline for comparison
            assert actual_content.rstrip("\n") == expected_content.rstrip("\n"), (
                f"Content of '{csv_name}' in archive does not match expected.\n"
                f"Expected:\n{expected_content}\n"
                f"Actual:\n{actual_content}"
            )


def test_manifest_file_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"The manifest file '{MANIFEST_PATH}' does not exist. "
        "It should have been generated as part of the task."
    )


def test_manifest_contains_exactly_three_csv_entries():
    assert os.path.isfile(MANIFEST_PATH), f"Manifest '{MANIFEST_PATH}' does not exist."
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 3, (
        f"Manifest '{MANIFEST_PATH}' should contain exactly 3 lines (one per CSV file), "
        f"but found {len(lines)} lines.\nContent:\n{content}"
    )


def test_manifest_lists_csv_files_in_correct_order():
    assert os.path.isfile(MANIFEST_PATH), f"Manifest '{MANIFEST_PATH}' does not exist."
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert lines == EXPECTED_CSV_FILES, (
        f"Manifest '{MANIFEST_PATH}' does not list files in the expected order.\n"
        f"Expected lines: {EXPECTED_CSV_FILES}\n"
        f"Actual lines:   {lines}"
    )


def test_manifest_no_extra_lines():
    assert os.path.isfile(MANIFEST_PATH), f"Manifest '{MANIFEST_PATH}' does not exist."
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    # Strip trailing newline (tar -tzf output ends with newline) but no blank lines
    stripped = content.rstrip("\n")
    lines = stripped.split("\n")
    assert lines == EXPECTED_CSV_FILES, (
        f"Manifest '{MANIFEST_PATH}' has unexpected content after stripping trailing newline.\n"
        f"Expected: {EXPECTED_CSV_FILES}\n"
        f"Actual:   {lines}"
    )


def test_manifest_does_not_contain_non_csv_files():
    assert os.path.isfile(MANIFEST_PATH), f"Manifest '{MANIFEST_PATH}' does not exist."
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    for non_csv in NON_CSV_FILES:
        assert non_csv not in content, (
            f"Non-CSV file '{non_csv}' appears in the manifest '{MANIFEST_PATH}'. "
            "Only .csv files should be listed."
        )


def test_manifest_entries_match_archive_contents():
    """The manifest should exactly reflect what tar -tzf reports for the archive."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive '{ARCHIVE_PATH}' does not exist."
    assert os.path.isfile(MANIFEST_PATH), f"Manifest '{MANIFEST_PATH}' does not exist."

    with tarfile.open(ARCHIVE_PATH, "r:gz") as tar:
        archive_members = tar.getnames()

    with open(MANIFEST_PATH, "r") as f:
        manifest_lines = [line for line in f.read().splitlines() if line.strip()]

    assert sorted(manifest_lines) == sorted(archive_members), (
        f"Manifest contents do not match archive contents.\n"
        f"Archive members: {sorted(archive_members)}\n"
        f"Manifest lines:  {sorted(manifest_lines)}"
    )


def test_experiment_directory_still_intact():
    """The original experiment directory should be untouched."""
    assert os.path.isdir(EXPERIMENT_DIR), (
        f"The original experiment directory '{EXPERIMENT_DIR}' no longer exists!"
    )
    all_expected = EXPECTED_CSV_FILES + NON_CSV_FILES
    for filename in all_expected:
        filepath = os.path.join(EXPERIMENT_DIR, filename)
        assert os.path.isfile(filepath), (
            f"Original file '{filepath}' is missing from the experiment directory. "
            "The task should not modify the source directory."
        )