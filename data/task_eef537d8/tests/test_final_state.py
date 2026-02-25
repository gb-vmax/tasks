# test_final_state.py

import os
import pytest

PAYMENT_LOG_PATH = "/home/user/services/payment-service/payment.log"
SUMMARY_PATH = "/home/user/services/payment-service/payment-error-summary.txt"
PAYMENT_SERVICE_DIR = "/home/user/services/payment-service"

EXPECTED_LOG_LINES = [
    "[2024-06-13 09:04:01] [INFO] [init] Payment service starting",
    "[2024-06-13 09:04:02] [ERROR] [transactions] Failed to process payment",
    "[2024-06-13 09:04:03] [WARN] [db] Connection slow",
    "[2024-06-13 09:04:04] [ERROR] [transactions] Invalid payment method",
    "[2024-06-13 09:04:05] [ERROR] [api] Unexpected status code",
    "[2024-06-13 09:04:06] [INFO] [monitor] Health check OK",
]

EXPECTED_SUMMARY_LINES = [
    "---",
    "ERROR COUNT: 3",
    "UNIQUE COMPONENTS: 2",
    "COMPONENTS LIST:",
    "transactions",
    "api",
    "---",
]

@pytest.mark.describe("Final state validation after log analysis task")
class TestFinalState:

    def test_payment_service_directory_still_exists(self):
        assert os.path.isdir(PAYMENT_SERVICE_DIR), (
            f"Directory {PAYMENT_SERVICE_DIR} is missing after the task. "
            "The payment-service directory must still exist at the specified path."
        )

    def test_payment_log_still_exists_and_unchanged(self):
        assert os.path.isfile(PAYMENT_LOG_PATH), (
            f"Log file {PAYMENT_LOG_PATH} is missing after the task. "
            "Expected payment.log to still exist for future analysis."
        )
        try:
            with open(PAYMENT_LOG_PATH, "r", encoding="utf-8") as f:
                contents = f.read().splitlines()
        except Exception as e:
            pytest.fail(f"Could not read {PAYMENT_LOG_PATH}: {e}")

        assert contents == EXPECTED_LOG_LINES, (
            f"The contents of {PAYMENT_LOG_PATH} have changed. "
            "The log file must remain unmodified after analysis."
        )

    def test_payment_error_summary_exists(self):
        assert os.path.isfile(SUMMARY_PATH), (
            f"Summary file {SUMMARY_PATH} is missing. "
            "You must create the summary file at the exact required path after analysis."
        )

    def test_payment_error_summary_contents_exact(self):
        try:
            with open(SUMMARY_PATH, "r", encoding="utf-8") as f:
                actual_lines = f.read().splitlines()
        except Exception as e:
            pytest.fail(f"Could not read {SUMMARY_PATH}: {e}")

        # Check the summary has the correct number of lines (should be 7)
        assert len(actual_lines) == len(EXPECTED_SUMMARY_LINES), (
            f"Summary file {SUMMARY_PATH} has {len(actual_lines)} lines, "
            f"but {len(EXPECTED_SUMMARY_LINES)} were expected.\n"
            "Expected summary format:\n"
            + "\n".join(EXPECTED_SUMMARY_LINES)
        )

        # Check the static lines for exact match
        assert actual_lines[0] == "---", (
            f"The first line of {SUMMARY_PATH} must be '---'.\n"
            f"Found: {actual_lines[0]!r}"
        )
        assert actual_lines[1] == "ERROR COUNT: 3", (
            f"ERROR COUNT line is incorrect in {SUMMARY_PATH}.\n"
            f"Expected: 'ERROR COUNT: 3'\nFound: {actual_lines[1]!r}"
        )
        assert actual_lines[2] == "UNIQUE COMPONENTS: 2", (
            f"UNIQUE COMPONENTS line is incorrect in {SUMMARY_PATH}.\n"
            f"Expected: 'UNIQUE COMPONENTS: 2'\nFound: {actual_lines[2]!r}"
        )
        assert actual_lines[3] == "COMPONENTS LIST:", (
            f"The fourth line of {SUMMARY_PATH} must be 'COMPONENTS LIST:'.\n"
            f"Found: {actual_lines[3]!r}"
        )
        assert actual_lines[-1] == "---", (
            f"The last line of {SUMMARY_PATH} must be '---'.\n"
            f"Found: {actual_lines[-1]!r}"
        )

        # Check the components list (lines 5 and 6) - must be 'transactions' and 'api' in any order, and only those two
        components_section = actual_lines[4:-1]
        expected_components = {"transactions", "api"}
        actual_components = set(components_section)
        missing = expected_components - actual_components
        extra = actual_components - expected_components
        assert not missing, (
            f"Missing component(s) in COMPONENTS LIST in {SUMMARY_PATH}: {', '.join(missing)}.\n"
            f"Expected components: {', '.join(expected_components)}"
        )
        assert not extra, (
            f"Unexpected component(s) in COMPONENTS LIST in {SUMMARY_PATH}: {', '.join(extra)}.\n"
            f"Expected only: {', '.join(expected_components)}"
        )
        assert len(components_section) == 2, (
            f"COMPONENTS LIST in {SUMMARY_PATH} should contain exactly 2 lines (one per component), "
            f"but found {len(components_section)}: {components_section!r}"
        )