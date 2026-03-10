# test_final_state.py

import os
import pytest

REPORT_FILE = "/home/user/deployments/rollout_report.txt"
LOG_FILE = "/home/user/deployments/rollout_2024.log"

EXPECTED_REPORT_CONTENT = """\
=== DEPLOYMENT ROLLOUT REPORT ===
Log file: /home/user/deployments/rollout_2024.log
Total services deployed: 8
Successful: 5
Failed: 3

=== SERVICE DETAILS ===
api-gateway [SUCCESS] 4200ms
auth-service [SUCCESS] 9800ms
billing-service [FAILED] 11200ms
config-service [SUCCESS] 6500ms
data-pipeline [SUCCESS] 13100ms
event-broker [FAILED] 8750ms
frontend [SUCCESS] 3300ms
gateway-proxy [FAILED] 15600ms

=== TIMING STATISTICS ===
Fastest deployment: frontend (3300ms)
Slowest deployment: gateway-proxy (15600ms)
Average deployment time: 9056ms

=== FAILED SERVICES ===
billing-service
event-broker
gateway-proxy
"""


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file '{REPORT_FILE}' does not exist. "
        "The agent must generate the deployment summary report."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_FILE, os.R_OK), (
        f"Report file '{REPORT_FILE}' exists but is not readable."
    )


def test_report_file_exact_content():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    assert actual_content == EXPECTED_REPORT_CONTENT, (
        f"Report file '{REPORT_FILE}' does not match expected content.\n"
        f"Expected:\n{repr(EXPECTED_REPORT_CONTENT)}\n\n"
        f"Actual:\n{repr(actual_content)}"
    )


def test_report_ends_with_newline():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    assert actual_content.endswith("\n"), (
        f"Report file '{REPORT_FILE}' must end with a newline character. "
        f"Last 10 chars: {repr(actual_content[-10:])}"
    )


def test_report_header_section():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()
    assert lines[0] == "=== DEPLOYMENT ROLLOUT REPORT ===", (
        f"First line should be '=== DEPLOYMENT ROLLOUT REPORT ===' but got: {repr(lines[0])}"
    )
    assert lines[1] == f"Log file: {LOG_FILE}", (
        f"Second line should be 'Log file: {LOG_FILE}' but got: {repr(lines[1])}"
    )
    assert lines[2] == "Total services deployed: 8", (
        f"Third line should be 'Total services deployed: 8' but got: {repr(lines[2])}"
    )
    assert lines[3] == "Successful: 5", (
        f"Fourth line should be 'Successful: 5' but got: {repr(lines[3])}"
    )
    assert lines[4] == "Failed: 3", (
        f"Fifth line should be 'Failed: 3' but got: {repr(lines[4])}"
    )


def test_report_blank_line_after_header():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()
    assert lines[5] == "", (
        f"Line 6 (index 5) should be blank after header block, but got: {repr(lines[5])}"
    )


def test_report_service_details_section_header():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()
    assert lines[6] == "=== SERVICE DETAILS ===", (
        f"Line 7 (index 6) should be '=== SERVICE DETAILS ===' but got: {repr(lines[6])}"
    )


def test_report_service_details_entries():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()

    expected_service_lines = [
        "api-gateway [SUCCESS] 4200ms",
        "auth-service [SUCCESS] 9800ms",
        "billing-service [FAILED] 11200ms",
        "config-service [SUCCESS] 6500ms",
        "data-pipeline [SUCCESS] 13100ms",
        "event-broker [FAILED] 8750ms",
        "frontend [SUCCESS] 3300ms",
        "gateway-proxy [FAILED] 15600ms",
    ]

    # Service details start at index 7
    actual_service_lines = lines[7:15]
    assert actual_service_lines == expected_service_lines, (
        f"SERVICE DETAILS entries do not match.\n"
        f"Expected:\n{expected_service_lines}\n"
        f"Actual:\n{actual_service_lines}"
    )


def test_report_blank_line_after_service_details():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()
    assert lines[15] == "", (
        f"Line 16 (index 15) should be blank after SERVICE DETAILS, but got: {repr(lines[15])}"
    )


def test_report_timing_statistics_section_header():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()
    assert lines[16] == "=== TIMING STATISTICS ===", (
        f"Line 17 (index 16) should be '=== TIMING STATISTICS ===' but got: {repr(lines[16])}"
    )


def test_report_timing_statistics_fastest():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()
    assert lines[17] == "Fastest deployment: frontend (3300ms)", (
        f"Fastest deployment line is wrong. Expected 'Fastest deployment: frontend (3300ms)' "
        f"but got: {repr(lines[17])}"
    )


def test_report_timing_statistics_slowest():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()
    assert lines[18] == "Slowest deployment: gateway-proxy (15600ms)", (
        f"Slowest deployment line is wrong. Expected 'Slowest deployment: gateway-proxy (15600ms)' "
        f"but got: {repr(lines[18])}"
    )


def test_report_timing_statistics_average():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()
    assert lines[19] == "Average deployment time: 9056ms", (
        f"Average deployment time line is wrong. Expected 'Average deployment time: 9056ms' "
        f"but got: {repr(lines[19])}"
    )


def test_report_blank_line_after_timing_statistics():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()
    assert lines[20] == "", (
        f"Line 21 (index 20) should be blank after TIMING STATISTICS, but got: {repr(lines[20])}"
    )


def test_report_failed_services_section_header():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()
    assert lines[21] == "=== FAILED SERVICES ===", (
        f"Line 22 (index 21) should be '=== FAILED SERVICES ===' but got: {repr(lines[21])}"
    )


def test_report_failed_services_entries():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()

    expected_failed_lines = [
        "billing-service",
        "event-broker",
        "gateway-proxy",
    ]

    actual_failed_lines = lines[22:25]
    assert actual_failed_lines == expected_failed_lines, (
        f"FAILED SERVICES entries do not match.\n"
        f"Expected:\n{expected_failed_lines}\n"
        f"Actual:\n{actual_failed_lines}"
    )


def test_report_total_line_count():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()
    lines = actual_content.splitlines()
    # Expected lines:
    # 0: === DEPLOYMENT ROLLOUT REPORT ===
    # 1: Log file: ...
    # 2: Total services deployed: 8
    # 3: Successful: 5
    # 4: Failed: 3
    # 5: (blank)
    # 6: === SERVICE DETAILS ===
    # 7-14: 8 service lines
    # 15: (blank)
    # 16: === TIMING STATISTICS ===
    # 17: Fastest deployment: ...
    # 18: Slowest deployment: ...
    # 19: Average deployment time: ...
    # 20: (blank)
    # 21: === FAILED SERVICES ===
    # 22-24: 3 failed services
    # Total: 25 lines
    assert len(lines) == 25, (
        f"Expected 25 lines in the report, but found {len(lines)}.\n"
        f"Lines:\n{lines}"
    )


def test_log_file_unchanged():
    """Verify the original log file was not modified."""
    expected_log_content = """\
[2024-04-10T08:01:00Z] [INFO] SERVICE=api-gateway ACTION=START STATUS=running DURATION_MS=-
[2024-04-10T08:01:00Z] [INFO] SERVICE=auth-service ACTION=START STATUS=running DURATION_MS=-
[2024-04-10T08:01:05Z] [INFO] SERVICE=billing-service ACTION=START STATUS=running DURATION_MS=-
[2024-04-10T08:01:05Z] [INFO] SERVICE=config-service ACTION=START STATUS=running DURATION_MS=-
[2024-04-10T08:01:10Z] [INFO] SERVICE=data-pipeline ACTION=START STATUS=running DURATION_MS=-
[2024-04-10T08:01:10Z] [INFO] SERVICE=event-broker ACTION=START STATUS=running DURATION_MS=-
[2024-04-10T08:01:15Z] [INFO] SERVICE=frontend ACTION=START STATUS=running DURATION_MS=-
[2024-04-10T08:01:15Z] [ERROR] SERVICE=gateway-proxy ACTION=START STATUS=running DURATION_MS=-
[2024-04-10T08:02:10Z] [INFO] SERVICE=api-gateway ACTION=END STATUS=success DURATION_MS=4200
[2024-04-10T08:02:30Z] [INFO] SERVICE=auth-service ACTION=END STATUS=success DURATION_MS=9800
[2024-04-10T08:02:45Z] [ERROR] SERVICE=billing-service ACTION=END STATUS=failed DURATION_MS=11200
[2024-04-10T08:03:00Z] [INFO] SERVICE=config-service ACTION=END STATUS=success DURATION_MS=6500
[2024-04-10T08:03:20Z] [INFO] SERVICE=data-pipeline ACTION=END STATUS=success DURATION_MS=13100
[2024-04-10T08:03:35Z] [ERROR] SERVICE=event-broker ACTION=END STATUS=failed DURATION_MS=8750
[2024-04-10T08:03:50Z] [INFO] SERVICE=frontend ACTION=END STATUS=success DURATION_MS=3300
[2024-04-10T08:04:10Z] [ERROR] SERVICE=gateway-proxy ACTION=END STATUS=failed DURATION_MS=15600"""

    assert os.path.isfile(LOG_FILE), (
        f"Log file '{LOG_FILE}' no longer exists after agent ran."
    )
    with open(LOG_FILE, "r") as f:
        actual_content = f.read().rstrip("\n")
    assert actual_content == expected_log_content, (
        f"Log file '{LOG_FILE}' was modified by the agent.\n"
        f"Expected:\n{expected_log_content}\n\n"
        f"Actual:\n{actual_content}"
    )