# test_final_state.py

import os
import stat
import pytest

UPTIME_CHECK_DIR = '/home/user/uptime_check'
V1_PATH = os.path.join(UPTIME_CHECK_DIR, 'status_page_v1.html')
V2_PATH = os.path.join(UPTIME_CHECK_DIR, 'status_page_v2.html')
BACKUP_PATH = os.path.join(UPTIME_CHECK_DIR, 'status_page_v1_backup.html')
PATCH_PATH = os.path.join(UPTIME_CHECK_DIR, 'status_page.patch')
LOG_PATH = os.path.join(UPTIME_CHECK_DIR, 'patch_verification.log')

ORIGINAL_V1_CONTENT = """<!DOCTYPE html>
<html>
<head>
    <title>Site Status</title>
</head>
<body>
    <h1>Website Uptime Monitor</h1>
    <p>Status: Operational</p>
    <p>Last updated: 2024-06-10 15:00 UTC</p>
</body>
</html>
"""

FINAL_V2_CONTENT = """<!DOCTYPE html>
<html>
<head>
    <title>Site Status</title>
</head>
<body>
    <h1>Website Uptime Monitor</h1>
    <p>Status: <strong>Operational</strong></p>
    <p>Last updated: 2024-06-10 16:00 UTC</p>
    <p>Next scheduled update: 2024-06-11 00:00 UTC</p>
</body>
</html>
"""

SUCCESS_LOG_LINE = "Patching successful: Files are identical after patch application."

@pytest.mark.describe("Final state: after patching and verification")
class TestFinalState:

    def test_backup_exists_and_is_identical_to_original_v1(self):
        """Check that the backup file exists and is byte-for-byte identical to the original v1 content."""
        assert os.path.isfile(BACKUP_PATH), (
            f"Backup file {BACKUP_PATH} does not exist. "
            "You must create a backup of the original status_page_v1.html."
        )
        with open(BACKUP_PATH, 'r', encoding='utf-8') as f:
            backup_content = f.read()
        assert backup_content == ORIGINAL_V1_CONTENT, (
            f"Backup file {BACKUP_PATH} does not exactly match the original status_page_v1.html content.\n"
            "Ensure you created the backup *before* patching."
        )

    def test_patch_file_exists_and_is_correct_unified_diff(self):
        """Check that the patch file exists, is a unified diff, and accurately represents the changes."""
        assert os.path.isfile(PATCH_PATH), (
            f"Patch file {PATCH_PATH} does not exist. "
            "You must generate a unified diff as described."
        )
        with open(PATCH_PATH, 'r', encoding='utf-8') as f:
            patch_lines = f.readlines()
        # Check for unified diff headers
        assert patch_lines, "Patch file is empty."
        assert patch_lines[0].startswith('--- status_page_v1.html'), (
            "Patch file does not start with '--- status_page_v1.html'.\n"
            "Ensure you used relative paths in the diff headers."
        )
        assert patch_lines[1].startswith('+++ status_page_v2.html'), (
            "Patch file does not have '+++ status_page_v2.html' as the second line.\n"
            "Ensure you used relative paths in the diff headers."
        )
        # Check for at least one chunk header (unified diff format)
        chunk_headers = [line for line in patch_lines if line.startswith('@@')]
        assert chunk_headers, (
            "Patch file does not contain any chunk headers (lines starting with '@@').\n"
            "Ensure the patch is in unified diff format."
        )
        # Check that the patch contains the expected changes for all three edits
        # a) <p>Status: Operational</p> → <p>Status: <strong>Operational</strong></p>
        # b) <p>Last updated: ...15:00...> → ...16:00...
        # c) Added line: <p>Next scheduled update: 2024-06-11 00:00 UTC</p>
        patch_text = ''.join(patch_lines)
        assert '-    <p>Status: Operational</p>' in patch_text, (
            "Patch file does not show removal of the original 'Status: Operational' line."
        )
        assert '+    <p>Status: <strong>Operational</strong></p>' in patch_text, (
            "Patch file does not show addition of the updated 'Status: <strong>Operational</strong>' line."
        )
        assert '-    <p>Last updated: 2024-06-10 15:00 UTC</p>' in patch_text, (
            "Patch file does not show removal of the old 'Last updated' line."
        )
        assert '+    <p>Last updated: 2024-06-10 16:00 UTC</p>' in patch_text, (
            "Patch file does not show addition of the new 'Last updated' line."
        )
        assert '+    <p>Next scheduled update: 2024-06-11 00:00 UTC</p>' in patch_text, (
            "Patch file does not show addition of the 'Next scheduled update' line."
        )

    def test_v1_file_is_patched_and_matches_v2(self):
        """Check that status_page_v1.html is now identical to v2.html."""
        assert os.path.isfile(V1_PATH), (
            f"{V1_PATH} does not exist after patching. "
            "The original file should remain, patched to match v2."
        )
        assert os.path.isfile(V2_PATH), (
            f"{V2_PATH} does not exist. "
            "Reference file required for comparison."
        )
        with open(V1_PATH, 'r', encoding='utf-8') as f:
            v1_content = f.read()
        with open(V2_PATH, 'r', encoding='utf-8') as f:
            v2_content = f.read()
        assert v1_content == FINAL_V2_CONTENT, (
            f"{V1_PATH} does not have the expected final content after patching."
        )
        assert v1_content == v2_content, (
            f"{V1_PATH} and {V2_PATH} are not identical after patching."
        )

    def test_patch_verification_log_exists_and_is_success(self):
        """Check that the verification log exists and contains the required success line only."""
        assert os.path.isfile(LOG_PATH), (
            f"Verification log {LOG_PATH} does not exist. "
            "You must generate a log file after patching."
        )
        with open(LOG_PATH, 'r', encoding='utf-8') as f:
            log_content = f.read().strip()
        assert log_content == SUCCESS_LOG_LINE, (
            f"patch_verification.log does not contain the required success line or has extra output.\n"
            f"Expected:\n{SUCCESS_LOG_LINE!r}\n"
            f"Actual:\n{log_content!r}\n"
            "If there are any differences in the files after patching, "
            "the log should contain the diff output, otherwise only the success line."
        )

    def test_no_extra_files(self):
        """Check that no unexpected files were created in the directory."""
        expected_files = {
            'status_page_v1.html',
            'status_page_v2.html',
            'status_page_v1_backup.html',
            'status_page.patch',
            'patch_verification.log'
        }
        actual_files = set(os.listdir(UPTIME_CHECK_DIR))
        extra_files = actual_files - expected_files
        assert not extra_files, (
            f"Unexpected extra files found in {UPTIME_CHECK_DIR}: {extra_files}.\n"
            "Only the specified files should exist after patching."
        )

    def test_permissions(self):
        """Check that all files are still writable by the user."""
        for path in [V1_PATH, V2_PATH, BACKUP_PATH, PATCH_PATH, LOG_PATH]:
            st = os.stat(path)
            assert bool(st.st_mode & stat.S_IWUSR), (
                f"{path} is not writable by the user."
            )