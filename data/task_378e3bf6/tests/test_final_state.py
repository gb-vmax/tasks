# test_final_state.py

import os
import pytest

HOME = "/home/user"
WORKFLOWS_DIR = os.path.join(HOME, "workflows")
BUILD_YML = os.path.join(WORKFLOWS_DIR, "build.yml")
EDIT_LOG = os.path.join(WORKFLOWS_DIR, "edit.log")

EXPECTED_BUILD_YML = (
    "steps:\n"
    "  - name: checkout\n"
    "    run: git checkout .\n"
    "  - name: test\n"
    "    run: ./test.sh\n"
    "  - name: deploy\n"
    "    run: ./deploy.sh\n"
)

EXPECTED_EDIT_LOG = "Step 'deploy' added to build.yml"

def test_workflows_directory_still_exists_and_writable():
    assert os.path.isdir(WORKFLOWS_DIR), (
        f"Directory '{WORKFLOWS_DIR}' does not exist after task completion."
    )
    assert os.access(WORKFLOWS_DIR, os.W_OK), (
        f"Directory '{WORKFLOWS_DIR}' is not writable after task completion."
    )

def test_build_yml_exists_and_content_correct():
    assert os.path.isfile(BUILD_YML), (
        f"File '{BUILD_YML}' does not exist after task completion."
    )
    with open(BUILD_YML, 'r', encoding='utf-8') as f:
        content = f.read()
    # Allow for possible trailing newlines in the file
    content_stripped = content.rstrip('\r\n')
    expected_stripped = EXPECTED_BUILD_YML.rstrip('\r\n')
    assert content_stripped == expected_stripped, (
        f"The file '{BUILD_YML}' does not have the correct final content.\n"
        "Expected (with exact indentation and order):\n"
        f"{EXPECTED_BUILD_YML!r}\n"
        "Got:\n"
        f"{content!r}\n"
        "Check that you appended the new step exactly as specified, without altering other content."
    )

def test_build_yml_step_appended_exactly():
    """Check that the last step is exactly the deploy step, with correct indentation and no extra content."""
    with open(BUILD_YML, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Remove trailing empty lines
    while lines and lines[-1].strip() == '':
        lines.pop()
    # The last two non-empty lines must be:
    #   - "  - name: deploy\n"
    #   - "    run: ./deploy.sh\n"
    assert len(lines) >= 2, (
        f"File '{BUILD_YML}' is too short after editing. Expected at least two new lines for the deploy step."
    )
    last_step_lines = lines[-2:]
    expected_last_step = [
        "  - name: deploy\n",
        "    run: ./deploy.sh\n",
    ]
    # Allow for possible absence of trailing newline on last line
    if not last_step_lines[-1].endswith('\n'):
        last_step_lines[-1] += '\n'
    assert last_step_lines == expected_last_step, (
        f"The last step in '{BUILD_YML}' is not exactly as required.\n"
        "Expected last two lines:\n"
        f"{expected_last_step!r}\n"
        "Got:\n"
        f"{last_step_lines!r}\n"
        "Check indentation, keys, and order."
    )

def test_edit_log_exists_and_content():
    assert os.path.isfile(EDIT_LOG), (
        f"Log file '{EDIT_LOG}' does not exist after task completion."
    )
    with open(EDIT_LOG, 'r', encoding='utf-8') as f:
        log_content = f.read()
    # Should be exactly one line, no extra whitespace or newlines
    if log_content.endswith('\n') or log_content.endswith('\r'):
        assert False, (
            f"Log file '{EDIT_LOG}' contains extra newline at the end. "
            "It must contain exactly one line, no trailing newlines or whitespace."
        )
    if log_content != EXPECTED_EDIT_LOG:
        assert False, (
            f"Log file '{EDIT_LOG}' does not contain the exact required message.\n"
            f"Expected: {EXPECTED_EDIT_LOG!r}\n"
            f"Got: {log_content!r}\n"
            "Do not add extra spaces, newlines, or characters."
        )

def test_edit_log_is_plain_text():
    # Should be a plain ASCII file, not binary or with BOM
    with open(EDIT_LOG, 'rb') as f:
        raw = f.read()
    assert not raw.startswith(b'\xef\xbb\xbf'), (
        f"Log file '{EDIT_LOG}' starts with a UTF-8 BOM. "
        "It must be plain text (ASCII or UTF-8, no BOM)."
    )
    try:
        raw.decode('ascii')
    except UnicodeDecodeError:
        # Allow UTF-8 if only ASCII chars present
        try:
            decoded = raw.decode('utf-8')
        except UnicodeDecodeError:
            assert False, (
                f"Log file '{EDIT_LOG}' is not plain text (ASCII/UTF-8)."
            )
        else:
            assert all(ord(c) < 128 for c in decoded), (
                f"Log file '{EDIT_LOG}' contains non-ASCII characters."
            )