# test_final_state.py

import os
import pytest

LOG_FILE = "/home/user/logs/microservice-app.log"
SUMMARY_FILE = "/home/user/logs/error_summary.txt"

EXPECTED_LOG_CONTENT = """2024-06-21T14:11:03Z auth INFO User logged in: id=74
2024-06-21T14:11:07Z payment ERROR Payment failed: code=500
2024-06-21T14:11:09Z auth WARN Token expired for user: id=74
2024-06-21T14:11:10Z shipping INFO Package sent: id=134
2024-06-21T14:11:14Z payment ERROR Invalid account number: id=315
2024-06-21T14:11:17Z auth ERROR Authentication failed: id=74
2024-06-21T14:11:21Z shipping ERROR API timeout: endpoint=track
"""

EXPECTED_SUMMARY_CONTENT = """auth 1
payment 2
shipping 1
"""

def normalize(s):
    """Normalize newlines and strip trailing newlines."""
    return s.strip().replace('\r\n', '\n').replace('\r', '\n')

def test_log_file_unchanged():
    """The original log file must not be changed in any way."""
    assert os.path.isfile(LOG_FILE), (
        f"Log file {LOG_FILE} is missing after the task. It must be preserved."
    )
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    expected = normalize(EXPECTED_LOG_CONTENT)
    actual = normalize(content)
    assert actual == expected, (
        f"The log file {LOG_FILE} was modified. It must be left unchanged.\n"
        "Expected content:\n"
        f"{EXPECTED_LOG_CONTENT}\n"
        "Actual content:\n"
        f"{content}"
    )

def test_error_summary_file_created_and_correct():
    """The summary file must exist and contain the correct error summary."""
    assert os.path.isfile(SUMMARY_FILE), (
        f"The summary file {SUMMARY_FILE} was not created."
    )
    with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
        summary_content = f.read()
    expected = normalize(EXPECTED_SUMMARY_CONTENT)
    actual = normalize(summary_content)
    assert actual == expected, (
        f"The summary file {SUMMARY_FILE} is not correct.\n"
        f"Expected:\n{EXPECTED_SUMMARY_CONTENT}\n"
        f"Actual:\n{summary_content}"
    )

def test_summary_file_format_and_content_strict():
    """
    The summary file must:
      - List only services with at least one ERROR entry
      - List services in alphabetical order
      - Have exactly one space between service and count
      - Not include extra lines or other log levels
      - Not include extra whitespace
    """
    with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]

    # No blank lines
    assert all(line.strip() != "" for line in lines), (
        f"The summary file {SUMMARY_FILE} contains blank lines. Only non-blank lines are allowed."
    )

    # Check format and gather entries
    entries = []
    for line in lines:
        parts = line.split()
        assert len(parts) == 2, (
            f"Line '{line}' in {SUMMARY_FILE} is not in 'SERVICE_NAME ERROR_COUNT' format."
        )
        service, count_str = parts
        assert service.isidentifier(), (
            f"Service name '{service}' in summary is not a valid identifier."
        )
        try:
            count = int(count_str)
        except ValueError:
            pytest.fail(f"ERROR_COUNT '{count_str}' for service '{service}' is not an integer in {SUMMARY_FILE}.")
        assert count >= 1, (
            f"ERROR_COUNT {count} for service '{service}' is less than 1 in {SUMMARY_FILE}."
        )
        entries.append((service, count))

    # Alphabetical order
    service_names = [service for service, _ in entries]
    assert service_names == sorted(service_names), (
        f"Services in {SUMMARY_FILE} are not in alphabetical order: {service_names}"
    )

    # Check that only the correct services/counts are present
    expected = [("auth", 1), ("payment", 2), ("shipping", 1)]
    assert entries == expected, (
        f"The summary file {SUMMARY_FILE} lists incorrect services or counts.\n"
        f"Expected: {expected}\n"
        f"Actual: {entries}"
    )