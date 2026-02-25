# test_final_state.py

import os
import pytest

REPORT_FILE = "/home/user/kube-manifests/reports/error_summary.log"

EXPECTED_ERROR_SUMMARY = (
    "could not pull image registry.example.com/base:latest: 3\n"
    "insufficient permissions to modify resource: 2\n"
    "pod crashloop detected for app-backend: 2\n"
)


@pytest.mark.describe("Final state: Kubernetes onboarding error summary report")
class TestFinalState:
    def test_error_summary_file_exists_and_readable(self):
        assert os.path.isfile(REPORT_FILE), (
            f"Required report file does not exist: {REPORT_FILE}"
        )
        assert os.access(REPORT_FILE, os.R_OK), (
            f"Report file exists but is not readable: {REPORT_FILE}"
        )

    def test_error_summary_contents_exact(self):
        try:
            with open(REPORT_FILE, "r", encoding="utf-8") as f:
                actual_contents = f.read()
        except Exception as e:
            pytest.fail(f"Could not read {REPORT_FILE}: {e}")

        if actual_contents != EXPECTED_ERROR_SUMMARY:
            # Provide detailed diff in error message
            expected_lines = EXPECTED_ERROR_SUMMARY.splitlines(keepends=False)
            actual_lines = actual_contents.splitlines(keepends=False)
            diff = []
            max_lines = max(len(expected_lines), len(actual_lines))
            for i in range(max_lines):
                exp = expected_lines[i] if i < len(expected_lines) else "<missing>"
                act = actual_lines[i] if i < len(actual_lines) else "<missing>"
                if exp != act:
                    diff.append(f"Line {i+1}:\n  Expected: {exp}\n  Actual:   {act}")
            diff_msg = "\n".join(diff) if diff else "No linewise difference found."
            pytest.fail(
                f"The contents of {REPORT_FILE} do not match the required error summary.\n"
                f"Expected:\n{EXPECTED_ERROR_SUMMARY}\n"
                f"Actual:\n{actual_contents}\n"
                f"Difference:\n{diff_msg}"
            )

    def test_error_summary_no_extra_lines(self):
        """Ensure there are no extra lines (empty or otherwise) in the report file."""
        with open(REPORT_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        expected_lines = [
            "could not pull image registry.example.com/base:latest: 3\n",
            "insufficient permissions to modify resource: 2\n",
            "pod crashloop detected for app-backend: 2\n",
        ]
        assert lines == expected_lines, (
            f"{REPORT_FILE} contains extra or missing lines.\n"
            f"Expected lines:\n{''.join(expected_lines)}\n"
            f"Actual lines:\n{''.join(lines)}"
        )