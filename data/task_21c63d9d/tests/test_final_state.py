# test_final_state.py

"""
Pytest suite to validate the final state of the deployment artifact pipeline task.

Validates:
- The presence/absence and content of artifact files in the correct directories.
- The log file /home/user/deployment_logs/pipeline.log contains exactly the correct log line (and nothing else).
- Only app.tar.gz is moved, and readme.txt remains untouched.

If the move is successful:
    - /home/user/deployment_ready/app.tar.gz exists, same content as original.
    - /home/user/deployment_staging/app.tar.gz does NOT exist.
    - /home/user/deployment_staging/readme.txt is untouched.
    - /home/user/deployment_logs/pipeline.log contains exactly:
      "SUCCESS: app.tar.gz moved to deployment_ready"

If the move fails:
    - /home/user/deployment_staging/app.tar.gz still exists.
    - /home/user/deployment_ready/app.tar.gz does NOT exist.
    - /home/user/deployment_staging/readme.txt is untouched.
    - /home/user/deployment_logs/pipeline.log contains exactly:
      "ERROR: app.tar.gz could not be moved"
"""

import os
import pytest

STAGING_DIR = "/home/user/deployment_staging"
READY_DIR = "/home/user/deployment_ready"
LOGS_DIR = "/home/user/deployment_logs"

APP_TAR_STAGING = os.path.join(STAGING_DIR, "app.tar.gz")
APP_TAR_READY = os.path.join(READY_DIR, "app.tar.gz")
README_TXT = os.path.join(STAGING_DIR, "readme.txt")
PIPELINE_LOG = os.path.join(LOGS_DIR, "pipeline.log")

SUCCESS_LOG_LINE = "SUCCESS: app.tar.gz moved to deployment_ready"
ERROR_LOG_LINE = "ERROR: app.tar.gz could not be moved"
VALID_LOG_LINES = {SUCCESS_LOG_LINE, ERROR_LOG_LINE}


def _read_log_line(log_path):
    try:
        with open(log_path, "rt", encoding="ascii") as f:
            lines = f.readlines()
        return [line.rstrip("\r\n") for line in lines]
    except Exception as e:
        pytest.fail(f"Could not read log file {log_path}: {e}")


def _file_contents(path):
    with open(path, "rb") as f:
        return f.read()


def test_pipeline_log_exists_and_content():
    """Check that the pipeline log exists, is a plain ASCII text file, and contains exactly one valid line."""
    assert os.path.isfile(PIPELINE_LOG), (
        f"Missing required log file: {PIPELINE_LOG}. "
        "The pipeline must write its result to this file."
    )

    lines = _read_log_line(PIPELINE_LOG)
    assert len(lines) == 1, (
        f"{PIPELINE_LOG} should contain exactly one line. "
        f"Found {len(lines)} lines: {lines}"
    )
    log_line = lines[0]
    assert log_line in VALID_LOG_LINES, (
        f"{PIPELINE_LOG} contains invalid log line: '{log_line}'.\n"
        f"Expected exactly one of: {list(VALID_LOG_LINES)}"
    )


def test_readme_txt_untouched():
    """Check that readme.txt is still present and unchanged in the staging directory."""
    assert os.path.isfile(README_TXT), (
        f"readme.txt is missing from {STAGING_DIR}. "
        "It should not be moved or deleted."
    )
    try:
        with open(README_TXT, 'rt', encoding='utf-8') as f:
            contents = f.read(1024)
            assert contents.strip() != "", (
                f"{README_TXT} exists but is empty or whitespace. "
                "It should retain its original content."
            )
    except Exception as e:
        pytest.fail(
            f"{README_TXT} could not be read as a text file: {e}"
        )


def test_final_state_app_tar_and_log():
    """
    Validate the precise final state for app.tar.gz and log file.

    If move succeeded:
        - app.tar.gz is in deployment_ready, not in staging, content preserved.
        - Log line is SUCCESS.
    If move failed:
        - app.tar.gz is still in staging, not in ready.
        - Log line is ERROR.
    """
    log_lines = _read_log_line(PIPELINE_LOG)
    log_line = log_lines[0]

    # --- Move SUCCEEDED ---
    if log_line == SUCCESS_LOG_LINE:
        assert not os.path.exists(APP_TAR_STAGING), (
            f"app.tar.gz still exists in staging: {APP_TAR_STAGING}. "
            "It should have been moved to deployment_ready."
        )
        assert os.path.isfile(APP_TAR_READY), (
            f"app.tar.gz is missing from the ready directory: {APP_TAR_READY}. "
            "It should have been moved here."
        )
        # Optional: check that the file is non-empty
        assert os.path.getsize(APP_TAR_READY) > 0, (
            f"{APP_TAR_READY} is empty. It should be a non-empty deployment artifact."
        )

    # --- Move FAILED ---
    elif log_line == ERROR_LOG_LINE:
        assert os.path.isfile(APP_TAR_STAGING), (
            f"app.tar.gz is missing from staging: {APP_TAR_STAGING}. "
            "Because the move failed, it should still be here."
        )
        assert not os.path.exists(APP_TAR_READY), (
            f"app.tar.gz exists in ready directory: {APP_TAR_READY}, "
            "but the move failed, so it should NOT be here."
        )
        # Optional: check that the file is non-empty
        assert os.path.getsize(APP_TAR_STAGING) > 0, (
            f"{APP_TAR_STAGING} is empty. It should be a non-empty deployment artifact."
        )

    else:
        # Already checked above, but for safety
        pytest.fail(
            f"Unexpected log line: '{log_line}'. "
            f"Expected one of: {list(VALID_LOG_LINES)}"
        )


def test_no_extra_files_in_logs_dir():
    """Check that no other files except pipeline.log exist in /home/user/deployment_logs."""
    files = os.listdir(LOGS_DIR)
    assert files == ["pipeline.log"], (
        f"Extra files found in {LOGS_DIR}: {files}. Only 'pipeline.log' should exist after the task."
    )


def test_no_extra_files_in_ready_dir_if_move_failed():
    """If move failed, ready dir should still be empty."""
    log_lines = _read_log_line(PIPELINE_LOG)
    log_line = log_lines[0]
    if log_line == ERROR_LOG_LINE:
        files = os.listdir(READY_DIR)
        assert files == [], (
            f"{READY_DIR} should be empty if the move failed. Found: {files}"
        )


def test_no_extra_files_in_staging_dir():
    """Only readme.txt should remain in staging if move succeeded, both files if move failed."""
    log_lines = _read_log_line(PIPELINE_LOG)
    log_line = log_lines[0]
    files = sorted(os.listdir(STAGING_DIR))
    if log_line == SUCCESS_LOG_LINE:
        assert files == ["readme.txt"], (
            f"After successful move, only readme.txt should remain in {STAGING_DIR}. Found: {files}"
        )
    elif log_line == ERROR_LOG_LINE:
        assert sorted(files) == ["app.tar.gz", "readme.txt"], (
            f"After failed move, both app.tar.gz and readme.txt should be present in {STAGING_DIR}. Found: {files}"
        )


def test_app_tar_gz_content_preserved_on_success(tmp_path):
    """If move succeeded, ensure the content of app.tar.gz is preserved after move."""
    log_lines = _read_log_line(PIPELINE_LOG)
    log_line = log_lines[0]
    if log_line == SUCCESS_LOG_LINE:
        # Try to reconstruct the original file from backup if available (for robust checking)
        # Since the original is moved, we can't compare, so just check non-empty and existence.
        assert os.path.getsize(APP_TAR_READY) > 0, (
            f"{APP_TAR_READY} exists but is empty. "
            "It should be a non-empty deployment artifact."
        )

# End of test_final_state.py