# test_final_state.py

import os
import stat
import json
import pytest

MANIFEST_PATH = "/home/user/manifests/nginx-deployment.json"
SCHEMA_PATH = "/home/user/schemas/deployment-schema.json"
OUTPUT_DIR = "/home/user/output"
SUMMARY_FILE = os.path.join(OUTPUT_DIR, "manifest_summary.txt")
VALIDATION_ERRORS_FILE = os.path.join(OUTPUT_DIR, "validation_errors.txt")

EXPECTED_SUMMARY_CONTENT = (
    "Name: nginx-deployment\n"
    "Replicas: 3\n"
    "Image: nginx:1.21.1"
)


def is_dir_writeable(path):
    """Check if a directory is writeable by the current user."""
    return os.access(path, os.W_OK | os.X_OK)


def test_output_directory_exists_and_is_writeable():
    assert os.path.exists(OUTPUT_DIR), (
        f"Output directory {OUTPUT_DIR} does not exist after the task. "
        "It must be created by the agent."
    )
    assert os.path.isdir(OUTPUT_DIR), (
        f"{OUTPUT_DIR} exists but is not a directory."
    )
    assert is_dir_writeable(OUTPUT_DIR), (
        f"Output directory {OUTPUT_DIR} is not writeable by the current user."
    )


def test_exactly_one_output_file_exists():
    files = os.listdir(OUTPUT_DIR)
    allowed = {"manifest_summary.txt", "validation_errors.txt"}
    actual = set(files)
    assert actual.issubset(allowed), (
        f"Output directory {OUTPUT_DIR} contains unexpected files: {actual - allowed}"
    )
    assert len(actual) == 1, (
        f"Exactly one of manifest_summary.txt or validation_errors.txt should exist in {OUTPUT_DIR}. "
        f"Found: {', '.join(files) if files else '(none)'}"
    )


def test_manifest_summary_contents_if_present():
    """If manifest_summary.txt exists, check its exact contents and that validation_errors.txt does not exist."""
    if os.path.exists(SUMMARY_FILE):
        # It must be a file, not a directory
        assert os.path.isfile(SUMMARY_FILE), (
            f"{SUMMARY_FILE} exists but is not a file."
        )
        # It must be readable
        assert os.access(SUMMARY_FILE, os.R_OK), (
            f"{SUMMARY_FILE} is not readable."
        )
        # It must have exact contents (no extra whitespace)
        with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
            summary_contents = f.read().rstrip("\n")
        assert summary_contents == EXPECTED_SUMMARY_CONTENT, (
            f"manifest_summary.txt contents are incorrect.\n"
            f"Expected:\n{EXPECTED_SUMMARY_CONTENT!r}\n"
            f"Got:\n{summary_contents!r}"
        )
        # validation_errors.txt must NOT exist
        assert not os.path.exists(VALIDATION_ERRORS_FILE), (
            f"{VALIDATION_ERRORS_FILE} should NOT exist when manifest_summary.txt is present."
        )


def test_validation_errors_contents_if_present():
    """If validation_errors.txt exists, check it is a file, is readable, and manifest_summary.txt does not exist."""
    if os.path.exists(VALIDATION_ERRORS_FILE):
        assert os.path.isfile(VALIDATION_ERRORS_FILE), (
            f"{VALIDATION_ERRORS_FILE} exists but is not a file."
        )
        assert os.access(VALIDATION_ERRORS_FILE, os.R_OK), (
            f"{VALIDATION_ERRORS_FILE} is not readable."
        )
        # manifest_summary.txt must NOT exist
        assert not os.path.exists(SUMMARY_FILE), (
            f"{SUMMARY_FILE} should NOT exist when validation_errors.txt is present."
        )
        # The file should not be empty (at least one error)
        with open(VALIDATION_ERRORS_FILE, "r", encoding="utf-8") as f:
            errors = [line.rstrip("\n") for line in f]
        assert any(line.strip() for line in errors), (
            f"{VALIDATION_ERRORS_FILE} exists but contains no error messages."
        )
        # Each line should be a non-empty string, no extra formatting
        for line in errors:
            assert line.strip() == line, (
                f"Each line in {VALIDATION_ERRORS_FILE} should not have leading or trailing whitespace: {line!r}"
            )
            assert line, (
                f"Found empty line in {VALIDATION_ERRORS_FILE}."
            )


def test_manifest_summary_matches_manifest_json_if_present():
    """If manifest_summary.txt is present, ensure the values match those in the manifest JSON."""
    if os.path.exists(SUMMARY_FILE):
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        # Extract required values
        try:
            name = manifest["metadata"]["name"]
            replicas = manifest["spec"]["replicas"]
            image = manifest["spec"]["template"]["spec"]["containers"][0]["image"]
        except Exception as e:
            pytest.fail(f"Could not extract required fields from manifest: {e}")
        # Compare to summary
        with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]
        expected_lines = [
            f"Name: {name}",
            f"Replicas: {replicas}",
            f"Image: {image}",
        ]
        assert lines == expected_lines, (
            f"manifest_summary.txt contents do not match the manifest values.\n"
            f"Expected lines:\n{expected_lines}\n"
            f"Actual lines:\n{lines}"
        )


def test_no_extra_files_in_output_directory():
    """No other files should exist in the output directory."""
    files = set(os.listdir(OUTPUT_DIR))
    allowed = {"manifest_summary.txt", "validation_errors.txt"}
    extra = files - allowed
    assert not extra, (
        f"Unexpected extra files found in {OUTPUT_DIR}: {extra}"
    )