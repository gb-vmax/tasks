# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/deploys/deploy_report.txt"
LOG_PATH = "/home/user/deploys/deployment.log"

EXPECTED_REPORT = """\
=== DEPLOYMENT HEALTH REPORT ===
Generated: 2024-06-10

Total deployments: 14
Successful: 11
Failed/Rolled back: 3
Overall success rate: 78.6%

=== PER-SERVICE SUMMARY ===
auth-service: 4/4 succeeded, avg duration 41s
inventory-service: 1/3 succeeded, avg duration 44s
notification-service: 3/3 succeeded, avg duration 29s
payment-service: 3/4 succeeded, avg duration 98s

=== REGIONAL BREAKDOWN ===
ap-south: 3/4 deployments succeeded
eu-west: 3/4 deployments succeeded
us-east: 5/6 deployments succeeded

=== ALERTS ===
DEGRADED SERVICES (success rate < 100%):
  inventory-service: 33.3% success rate
  payment-service: 75.0% success rate
SLOWEST DEPLOYMENT: payment-service v1.9.0 in ap-south took 120s
FASTEST DEPLOYMENT: inventory-service v3.1.2 in us-east took 15s"""


def read_report():
    with open(REPORT_PATH, "r") as f:
        return f.read()


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The student's solution must create this file."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file '{REPORT_PATH}' exists but is not readable."
    )


def test_log_file_unchanged():
    """Ensure the original log file was not modified."""
    assert os.path.isfile(LOG_PATH), (
        f"Log file '{LOG_PATH}' no longer exists — it must not be removed."
    )
    with open(LOG_PATH, "r") as f:
        content = f.read()
    assert "STATUS=DEPLOYED" in content, (
        f"Log file '{LOG_PATH}' appears to have been modified (missing STATUS=DEPLOYED)."
    )


def test_report_header():
    content = read_report()
    assert "=== DEPLOYMENT HEALTH REPORT ===" in content, (
        "Report is missing the header '=== DEPLOYMENT HEALTH REPORT ==='."
    )


def test_report_generated_date():
    content = read_report()
    assert "Generated: 2024-06-10" in content, (
        "Report is missing or has incorrect 'Generated:' date. "
        "Expected: 'Generated: 2024-06-10'"
    )


def test_report_total_deployments():
    content = read_report()
    assert "Total deployments: 14" in content, (
        "Report has incorrect total deployments count. Expected: 'Total deployments: 14'"
    )


def test_report_successful_count():
    content = read_report()
    assert "Successful: 11" in content, (
        "Report has incorrect successful count. Expected: 'Successful: 11'"
    )


def test_report_failed_rolled_back_count():
    content = read_report()
    assert "Failed/Rolled back: 3" in content, (
        "Report has incorrect failed/rolled back count. Expected: 'Failed/Rolled back: 3'"
    )


def test_report_success_rate():
    content = read_report()
    assert "Overall success rate: 78.6%" in content, (
        "Report has incorrect overall success rate. Expected: 'Overall success rate: 78.6%'"
    )


def test_report_per_service_section_header():
    content = read_report()
    assert "=== PER-SERVICE SUMMARY ===" in content, (
        "Report is missing the '=== PER-SERVICE SUMMARY ===' section header."
    )


def test_report_auth_service_summary():
    content = read_report()
    expected = "auth-service: 4/4 succeeded, avg duration 41s"
    assert expected in content, (
        f"Report is missing or incorrect auth-service summary.\n"
        f"Expected line: {expected!r}"
    )


def test_report_inventory_service_summary():
    content = read_report()
    expected = "inventory-service: 1/3 succeeded, avg duration 44s"
    assert expected in content, (
        f"Report is missing or incorrect inventory-service summary.\n"
        f"Expected line: {expected!r}"
    )


def test_report_notification_service_summary():
    content = read_report()
    expected = "notification-service: 3/3 succeeded, avg duration 29s"
    assert expected in content, (
        f"Report is missing or incorrect notification-service summary.\n"
        f"Expected line: {expected!r}"
    )


def test_report_payment_service_summary():
    content = read_report()
    expected = "payment-service: 3/4 succeeded, avg duration 98s"
    assert expected in content, (
        f"Report is missing or incorrect payment-service summary.\n"
        f"Expected line: {expected!r}"
    )


def test_report_per_service_alphabetical_order():
    content = read_report()
    lines = content.splitlines()
    # Find the per-service section
    start = None
    end = None
    for i, line in enumerate(lines):
        if "=== PER-SERVICE SUMMARY ===" in line:
            start = i + 1
        elif start is not None and line.startswith("==="):
            end = i
            break
    assert start is not None, "Could not find '=== PER-SERVICE SUMMARY ===' section."
    service_lines = [l for l in lines[start:end] if l.strip()]
    service_names = []
    for line in service_lines:
        name = line.split(":")[0].strip()
        service_names.append(name)
    assert service_names == sorted(service_names), (
        f"Services in PER-SERVICE SUMMARY are not in alphabetical order.\n"
        f"Got: {service_names}\n"
        f"Expected alphabetical: {sorted(service_names)}"
    )


def test_report_regional_breakdown_section_header():
    content = read_report()
    assert "=== REGIONAL BREAKDOWN ===" in content, (
        "Report is missing the '=== REGIONAL BREAKDOWN ===' section header."
    )


def test_report_ap_south_region():
    content = read_report()
    expected = "ap-south: 3/4 deployments succeeded"
    assert expected in content, (
        f"Report is missing or incorrect ap-south regional breakdown.\n"
        f"Expected line: {expected!r}"
    )


def test_report_eu_west_region():
    content = read_report()
    expected = "eu-west: 3/4 deployments succeeded"
    assert expected in content, (
        f"Report is missing or incorrect eu-west regional breakdown.\n"
        f"Expected line: {expected!r}"
    )


def test_report_us_east_region():
    content = read_report()
    expected = "us-east: 5/6 deployments succeeded"
    assert expected in content, (
        f"Report is missing or incorrect us-east regional breakdown.\n"
        f"Expected line: {expected!r}"
    )


def test_report_regional_alphabetical_order():
    content = read_report()
    lines = content.splitlines()
    start = None
    end = None
    for i, line in enumerate(lines):
        if "=== REGIONAL BREAKDOWN ===" in line:
            start = i + 1
        elif start is not None and line.startswith("==="):
            end = i
            break
    assert start is not None, "Could not find '=== REGIONAL BREAKDOWN ===' section."
    region_lines = [l for l in lines[start:end] if l.strip()]
    region_names = []
    for line in region_lines:
        name = line.split(":")[0].strip()
        region_names.append(name)
    assert region_names == sorted(region_names), (
        f"Regions in REGIONAL BREAKDOWN are not in alphabetical order.\n"
        f"Got: {region_names}\n"
        f"Expected alphabetical: {sorted(region_names)}"
    )


def test_report_alerts_section_header():
    content = read_report()
    assert "=== ALERTS ===" in content, (
        "Report is missing the '=== ALERTS ===' section header."
    )


def test_report_degraded_services_header():
    content = read_report()
    assert "DEGRADED SERVICES (success rate < 100%):" in content, (
        "Report is missing the 'DEGRADED SERVICES (success rate < 100%):' header."
    )


def test_report_inventory_degraded():
    content = read_report()
    expected = "  inventory-service: 33.3% success rate"
    assert expected in content, (
        f"Report is missing or incorrect degraded service entry for inventory-service.\n"
        f"Expected line: {expected!r}"
    )


def test_report_payment_degraded():
    content = read_report()
    expected = "  payment-service: 75.0% success rate"
    assert expected in content, (
        f"Report is missing or incorrect degraded service entry for payment-service.\n"
        f"Expected line: {expected!r}"
    )


def test_report_auth_not_degraded():
    content = read_report()
    assert "  auth-service:" not in content, (
        "auth-service should NOT appear in the DEGRADED SERVICES list "
        "(it has 100% success rate)."
    )


def test_report_notification_not_degraded():
    content = read_report()
    assert "  notification-service:" not in content, (
        "notification-service should NOT appear in the DEGRADED SERVICES list "
        "(it has 100% success rate)."
    )


def test_report_slowest_deployment():
    content = read_report()
    expected = "SLOWEST DEPLOYMENT: payment-service v1.9.0 in ap-south took 120s"
    assert expected in content, (
        f"Report has missing or incorrect SLOWEST DEPLOYMENT.\n"
        f"Expected: {expected!r}"
    )


def test_report_fastest_deployment():
    content = read_report()
    expected = "FASTEST DEPLOYMENT: inventory-service v3.1.2 in us-east took 15s"
    assert expected in content, (
        f"Report has missing or incorrect FASTEST DEPLOYMENT.\n"
        f"Expected: {expected!r}"
    )


def test_report_exact_content():
    """Check the entire report matches the expected content exactly (ignoring trailing newline)."""
    content = read_report().rstrip("\n")
    expected = EXPECTED_REPORT.rstrip("\n")
    assert content == expected, (
        "Report content does not exactly match the expected output.\n"
        "Differences found:\n"
        + _diff_lines(expected, content)
    )


def _diff_lines(expected: str, actual: str) -> str:
    """Return a simple line-by-line diff string for diagnostic purposes."""
    exp_lines = expected.splitlines()
    act_lines = actual.splitlines()
    result = []
    max_lines = max(len(exp_lines), len(act_lines))
    for i in range(max_lines):
        e = exp_lines[i] if i < len(exp_lines) else "<missing>"
        a = act_lines[i] if i < len(act_lines) else "<missing>"
        if e != a:
            result.append(f"  Line {i+1}:")
            result.append(f"    Expected: {e!r}")
            result.append(f"    Actual:   {a!r}")
    return "\n".join(result) if result else "(no line-level differences found)"