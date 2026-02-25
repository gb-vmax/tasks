# test_final_state.py

import os
import stat
import pytest

ERRORS_EXTRACTED_LOG = "/home/user/errors_extracted.log"

@pytest.mark.describe("Final OS/filesystem state after log extraction task")
class TestFinalState:

    def test_errors_extracted_log_exists(self):
        assert os.path.isfile(ERRORS_EXTRACTED_LOG), (
            f"'{ERRORS_EXTRACTED_LOG}' does not exist. "
            "You must create this file by extracting ERROR-level log entries."
        )

    def test_errors_extracted_log_contents(self):
        expected_lines = [
            "2024-06-11 10:45:23 | Failed to connect to database\n",
            "2024-06-11 10:47:10 | Application crashed due to timeout\n",
            "2024-06-11 10:47:13 | Recovery process started\n",
        ]
        with open(ERRORS_EXTRACTED_LOG, encoding="utf-8") as f:
            actual_lines = f.readlines()
        assert actual_lines == expected_lines, (
            f"Contents of '{ERRORS_EXTRACTED_LOG}' are incorrect.\n"
            "Expected exactly these lines (no extra whitespace or blank lines):\n"
            + "".join(expected_lines) +
            "\nActual contents:\n"
            + "".join(actual_lines)
        )

    def test_errors_extracted_log_no_extra_lines(self):
        """Ensure there are exactly three lines and no extra blank lines or whitespace."""
        with open(ERRORS_EXTRACTED_LOG, encoding="utf-8") as f:
            lines = f.readlines()
        for idx, line in enumerate(lines):
            assert not line.endswith("  \n") and not line.endswith("\t\n"), (
                f"Line {idx+1} in '{ERRORS_EXTRACTED_LOG}' has trailing whitespace. "
                "Lines must not have extra spaces or tabs at the end."
            )
        assert len(lines) == 3, (
            f"'{ERRORS_EXTRACTED_LOG}' should have exactly 3 lines, "
            f"but has {len(lines)}. Extra or missing lines detected."
        )

    def test_errors_extracted_log_permissions(self):
        """Check that the file is readable and writable by the user."""
        st = os.stat(ERRORS_EXTRACTED_LOG)
        # Owner must have read and write permission
        owner_perms = stat.S_IMODE(st.st_mode) & 0o600
        assert owner_perms == 0o600 or owner_perms == 0o660 or owner_perms == 0o666 or owner_perms == 0o640 or owner_perms == 0o644, (
            f"'{ERRORS_EXTRACTED_LOG}' permissions are too restrictive. "
            "The owner (user) must have at least read and write permissions (rw------- or more permissive). "
            f"Current mode: {oct(stat.S_IMODE(st.st_mode))}"
        )
        # File must not be world-writable
        assert not (stat.S_IMODE(st.st_mode) & 0o002), (
            f"'{ERRORS_EXTRACTED_LOG}' is world-writable, which is not allowed. "
            "Remove write permission for 'others'."
        )

    def test_errors_extracted_log_not_directory(self):
        assert not os.path.isdir(ERRORS_EXTRACTED_LOG), (
            f"'{ERRORS_EXTRACTED_LOG}' is a directory, but should be a regular file."
        )