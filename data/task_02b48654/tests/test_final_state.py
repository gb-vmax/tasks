# test_final_state.py

import os
import pytest
import re

LOGS_DIR = "/home/user/migration/logs"
DEPLOYMENTS_LOG = "/home/user/migration/logs/deployments.log"
FAILED_SERVICES_LOG = "/home/user/migration/logs/failed_services.log"

EXPECTED_FAILED_SERVICES_LOG_CONTENT = (
    "2024-06-05T10:01:25Z ERROR: auth-service deploy failed\n"
    "2024-06-05T10:02:13Z ERROR: payment-service deploy failed\n"
    "2024-06-05T10:04:22Z ERROR: inventory_service deploy failed"
)

@pytest.mark.describe("Final state: failed_services.log exists and contains only expected filtered entries")
def test_failed_services_log_exists():
    assert os.path.isfile(FAILED_SERVICES_LOG), (
        f"After completing the task, the file '{FAILED_SERVICES_LOG}' must exist. "
        "It was not found. Did you create it in the correct location?"
    )

@pytest.mark.describe("Final state: failed_services.log contains only the expected lines, in order, with exact content")
def test_failed_services_log_content_exact():
    with open(FAILED_SERVICES_LOG, "r", encoding="utf-8") as f:
        actual_content = f.read()

    # Strip only trailing newlines for flexible newline at EOF, but not for blank lines in file
    actual_lines = actual_content.rstrip('\r\n').splitlines()
    expected_lines = EXPECTED_FAILED_SERVICES_LOG_CONTENT.splitlines()

    assert actual_lines == expected_lines, (
        f"The contents of '{FAILED_SERVICES_LOG}' do not match the required filtered output.\n"
        "Expected exactly these lines (in order, with precise whitespace):\n"
        f"{EXPECTED_FAILED_SERVICES_LOG_CONTENT}\n"
        f"Actual contents:\n"
        f"{actual_content}"
    )

@pytest.mark.describe("Final state: failed_services.log does not contain extra lines, blank lines, or formatting")
def test_failed_services_log_no_extra_lines():
    with open(FAILED_SERVICES_LOG, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Remove trailing newlines for comparison, but keep empty lines if present
    stripped_lines = [line.rstrip('\r\n') for line in lines]
    expected_lines = EXPECTED_FAILED_SERVICES_LOG_CONTENT.splitlines()
    assert stripped_lines == expected_lines, (
        f"'{FAILED_SERVICES_LOG}' contains extra lines or blank lines.\n"
        "Only the 3 filtered error entries should appear, with no blank or extra lines.\n"
        f"Actual lines:\n{stripped_lines}"
    )

@pytest.mark.describe("Final state: failed_services.log contains only lines matching the required pattern")
def test_failed_services_log_only_valid_matches():
    """
    Asserts that every line in failed_services.log matches the required pattern:
    ERROR: <service-name> deploy failed
    Where <service-name> is non-empty, composed of alphanumeric, dashes, or underscores.
    """
    required_pattern = re.compile(
        r'^.*ERROR:\s([A-Za-z0-9_-]+)\sdeploy failed$'
    )

    with open(FAILED_SERVICES_LOG, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, 1):
            line = line.rstrip('\r\n')
            match = required_pattern.match(line)
            assert match, (
                f"Line {idx} in '{FAILED_SERVICES_LOG}' is invalid:\n"
                f"  {line}\n"
                "Lines in this file must match: "
                "'...ERROR: <service-name> deploy failed' "
                "where <service-name> is alphanumeric, dash, or underscore."
            )

@pytest.mark.describe("Final state: failed_services.log preserves original order and whitespace")
def test_failed_services_log_preserves_order_and_whitespace():
    """
    Ensures that the lines in failed_services.log appear in the same order and with
    the same whitespace as in deployments.log.
    """
    # The regex for a valid filtered line:
    filter_pattern = re.compile(
        r'^.*ERROR:\s([A-Za-z0-9_-]+)\sdeploy failed$'
    )
    with open(DEPLOYMENTS_LOG, "r", encoding="utf-8") as f:
        deployments_lines = f.readlines()
    with open(FAILED_SERVICES_LOG, "r", encoding="utf-8") as f:
        failed_services_lines = f.readlines()

    # Build list of lines that should have been filtered
    expected_filtered = [line for line in deployments_lines if filter_pattern.match(line.rstrip('\r\n'))]

    assert failed_services_lines == expected_filtered, (
        f"The lines in '{FAILED_SERVICES_LOG}' do not preserve the original order or exact whitespace "
        "from '{DEPLOYMENTS_LOG}'.\n"
        "Expected filtered lines (from deployments.log):\n"
        f"{''.join(expected_filtered)}\n"
        "Actual lines in failed_services.log:\n"
        f"{''.join(failed_services_lines)}"
    )