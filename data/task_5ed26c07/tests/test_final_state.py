# test_final_state.py

import os
import pytest

RELEASES_DIR = "/home/user/releases"
PENDING_DEPLOYMENTS_CSV = os.path.join(RELEASES_DIR, "pending_deployments.csv")
DEPLOYMENTS_READY_TXT = os.path.join(RELEASES_DIR, "deployments_ready.txt")

@pytest.mark.describe("Final OS/filesystem state after student action")
class TestFinalState:
    def test_releases_directory_still_exists(self):
        assert os.path.isdir(RELEASES_DIR), (
            f"Required directory missing after task: {RELEASES_DIR}"
        )

    def test_pending_deployments_csv_still_exists_and_unchanged(self):
        assert os.path.isfile(PENDING_DEPLOYMENTS_CSV), (
            f"{PENDING_DEPLOYMENTS_CSV} is missing after the task. It must not be deleted or moved."
        )
        expected_lines = [
            "1042,Inventory,2.3.5,2024-07-01,no",
            "1043,Checkout,1.4.1,2024-07-02,yes",
            "1044,Warehouse,1.2.9,2024-07-05,no",
        ]
        try:
            with open(PENDING_DEPLOYMENTS_CSV, "r", encoding="utf-8") as f:
                lines = [line.rstrip("\r\n") for line in f]
        except Exception as e:
            pytest.fail(f"Could not read {PENDING_DEPLOYMENTS_CSV}: {e}")

        assert lines == expected_lines, (
            f"The file {PENDING_DEPLOYMENTS_CSV} was modified. It must remain unchanged.\n"
            f"Expected:\n{expected_lines}\nActual:\n{lines}"
        )

    def test_deployments_ready_txt_exists(self):
        assert os.path.isfile(DEPLOYMENTS_READY_TXT), (
            f"Output file {DEPLOYMENTS_READY_TXT} does not exist after the task. "
            "You must create this file with the approved deployments."
        )

    def test_deployments_ready_txt_contents(self):
        expected_lines = [
            "RELEASE 1043: Checkout v1.4.1 scheduled for 2024-07-02"
        ]
        try:
            with open(DEPLOYMENTS_READY_TXT, "r", encoding="utf-8") as f:
                lines = [line.rstrip("\r\n") for line in f]
        except Exception as e:
            pytest.fail(f"Could not read {DEPLOYMENTS_READY_TXT}: {e}")

        assert lines == expected_lines, (
            f"The file {DEPLOYMENTS_READY_TXT} does not have the correct contents.\n"
            f"Expected:\n{expected_lines}\nActual:\n{lines}\n"
            "Ensure that only approved deployments are included, each in the specified format, "
            "with no headers or extra lines."
        )

    def test_deployments_ready_txt_no_extra_lines(self):
        # This is redundant given the above, but ensures no blank or trailing lines.
        try:
            with open(DEPLOYMENTS_READY_TXT, "rb") as f:
                content = f.read()
        except Exception as e:
            pytest.fail(f"Could not read {DEPLOYMENTS_READY_TXT} as bytes: {e}")

        # Should end exactly with the last character of the line, not a blank line
        assert content.endswith(b"2024-07-02") or content.endswith(b"2024-07-02\n"), (
            "The output file appears to have trailing blank lines or extra space at the end. "
            "It must end with the last character of the deployment line."
        )
        # Should not start with a newline
        assert not content.startswith(b"\n"), (
            "The output file appears to have a leading blank line. It must not."
        )