# test_final_state.py

"""
Pytest suite to validate the FINAL state after artifact moving task.

This checks that:
- Files from /home/user/builds/output were moved to /home/user/artifacts if no conflict.
- Conflicting files (by name) were NOT overwritten, and are logged in /home/user/artifacts/move_errors.log.
- The move_errors.log contains exactly the set of conflicting file names, one per line, no extra whitespace.
- File contents are exactly as expected.
"""

import os
import pytest

HOME = "/home/user"
BUILD_OUTPUT_DIR = os.path.join(HOME, "builds", "output")
ARTIFACTS_DIR = os.path.join(HOME, "artifacts")
MOVE_ERRORS_LOG = os.path.join(ARTIFACTS_DIR, "move_errors.log")

BUILD1 = "build1.tar.gz"
BUILD2 = "build2.tar.gz"
BUILD3 = "build3.tar.gz"

@pytest.mark.describe("Final filesystem state after artifact move operation")
class TestFinalState:

    def test_artifacts_directory_contains_expected_files(self):
        """
        After the move:
        - /home/user/artifacts should contain build1.tar.gz, build2.tar.gz, build3.tar.gz, move_errors.log
        - No extra or missing files (other than possibly . or ..).
        """
        expected_files = {BUILD1, BUILD2, BUILD3, "move_errors.log"}
        actual_files = set(
            f for f in os.listdir(ARTIFACTS_DIR)
            if os.path.isfile(os.path.join(ARTIFACTS_DIR, f))
        )
        missing = expected_files - actual_files
        extra = actual_files - expected_files
        assert not missing, (
            f"Missing files in {ARTIFACTS_DIR}: {', '.join(sorted(missing))}. "
            f"Expected files: {', '.join(sorted(expected_files))}."
        )
        assert not extra, (
            f"Unexpected extra files in {ARTIFACTS_DIR}: {', '.join(sorted(extra))}. "
            "There should be no extra files in the artifacts directory after the move."
        )

    def test_artifacts_file_contents(self):
        """
        Check contents of each file in /home/user/artifacts.
        """
        expected_contents = {
            BUILD1: b"foo build content",
            BUILD2: b"old archived build",
            BUILD3: b"baz build content",
        }
        for fname, expected in expected_contents.items():
            fpath = os.path.join(ARTIFACTS_DIR, fname)
            assert os.path.isfile(fpath), (
                f"Expected file {fpath} to exist in artifacts directory."
            )
            with open(fpath, "rb") as f:
                actual = f.read()
            assert actual == expected, (
                f"File {fpath} has unexpected contents.\n"
                f"Expected: {expected!r}\nGot:      {actual!r}\n"
                "Check that you moved the correct file and did not overwrite existing files."
            )

    def test_move_errors_log_exists(self):
        """
        The move_errors.log must exist in /home/user/artifacts.
        """
        assert os.path.isfile(MOVE_ERRORS_LOG), (
            f"Missing required log file: {MOVE_ERRORS_LOG}. "
            "This file must be created if any move conflicts were encountered."
        )

    def test_move_errors_log_contents(self):
        """
        The move_errors.log must contain exactly one line: build2.tar.gz
        """
        with open(MOVE_ERRORS_LOG, "rt", encoding="utf-8") as f:
            data = f.read()
        # Should be exactly the file name, no leading/trailing whitespace, no extra lines
        expected = "build2.tar.gz"
        lines = data.splitlines()
        assert len(lines) == 1, (
            f"{MOVE_ERRORS_LOG} should contain exactly one line, but got {len(lines)} lines.\n"
            f"Contents:\n{data!r}"
        )
        assert lines[0] == expected, (
            f"{MOVE_ERRORS_LOG} should contain exactly '{expected}' as its only line.\n"
            f"Actual line: {lines[0]!r}"
        )

    def test_no_moved_file_was_overwritten(self):
        """
        Ensure that build2.tar.gz in /home/user/artifacts has not been overwritten.
        """
        artifacts_build2_path = os.path.join(ARTIFACTS_DIR, BUILD2)
        assert os.path.isfile(artifacts_build2_path), (
            f"Expected {artifacts_build2_path} to exist in artifacts directory."
        )
        with open(artifacts_build2_path, "rb") as f:
            actual = f.read()
        expected = b"old archived build"
        assert actual == expected, (
            f"{artifacts_build2_path} was not supposed to be overwritten.\n"
            f"Expected contents: {expected!r}\nGot: {actual!r}.\n"
            "Do not overwrite files that already exist in the destination."
        )

    def test_builds_output_directory_contains_only_conflicted_file(self):
        """
        After the move, /home/user/builds/output should contain only build2.tar.gz
        """
        expected_files = {BUILD2}
        actual_files = set(
            f for f in os.listdir(BUILD_OUTPUT_DIR)
            if os.path.isfile(os.path.join(BUILD_OUTPUT_DIR, f))
        )
        missing = expected_files - actual_files
        extra = actual_files - expected_files
        assert not missing, (
            f"Missing {BUILD2} in {BUILD_OUTPUT_DIR}. "
            f"After the move, build2.tar.gz should remain in the output directory since it could not be moved."
        )
        assert not extra, (
            f"Unexpected files in {BUILD_OUTPUT_DIR}: {', '.join(sorted(extra))}. "
            "Only build2.tar.gz should remain in output after the move operation."
        )

    def test_builds_output_build2_content_is_unchanged(self):
        """
        build2.tar.gz in /home/user/builds/output should still have its original content.
        """
        fpath = os.path.join(BUILD_OUTPUT_DIR, BUILD2)
        assert os.path.isfile(fpath), (
            f"Expected {fpath} to exist in output directory."
        )
        with open(fpath, "rb") as f:
            actual = f.read()
        expected = b"bar build content"
        assert actual == expected, (
            f"File {fpath} has unexpected contents after the move operation.\n"
            f"Expected: {expected!r}\nGot: {actual!r}."
        )

    def test_builds_output_does_not_contain_moved_files(self):
        """
        build1.tar.gz and build3.tar.gz should have been moved out of /home/user/builds/output.
        """
        forbidden = {BUILD1, BUILD3}
        actual_files = set(
            f for f in os.listdir(BUILD_OUTPUT_DIR)
            if os.path.isfile(os.path.join(BUILD_OUTPUT_DIR, f))
        )
        present_forbidden = forbidden & actual_files
        assert not present_forbidden, (
            f"Files {', '.join(sorted(present_forbidden))} should have been moved out of {BUILD_OUTPUT_DIR}, "
            "but are still present. Only build2.tar.gz should remain."
        )