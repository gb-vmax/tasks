# test_final_state.py

import os
import pytest

SLA_REPORT = "/home/user/monitoring/sla_report.txt"

EXPECTED_CONTENT = """\
=== SLA COMPLIANCE REPORT ===
Generated checks per service: 12

SERVICE SUMMARY
---------------
api-gateway
  Checks: 12 | Up: 11 | Down: 1
  Uptime: 91.67%
  SLA Target: 99.9%
  SLA Status: BREACH
  Avg Response (up checks): 148ms

auth-service
  Checks: 12 | Up: 12 | Down: 0
  Uptime: 100.00%
  SLA Target: 99.5%
  SLA Status: OK
  Avg Response (up checks): 87ms

payments-api
  Checks: 12 | Up: 9 | Down: 3
  Uptime: 75.00%
  SLA Target: 99.95%
  SLA Status: BREACH
  Avg Response (up checks): 310ms

user-service
  Checks: 12 | Up: 12 | Down: 0
  Uptime: 100.00%
  SLA Target: 99.0%
  SLA Status: OK
  Avg Response (up checks): 212ms

=== BREACH SUMMARY ===
Services in breach: 2
api-gateway: 91.67% uptime (target: 99.9%)
payments-api: 75.00% uptime (target: 99.95%)

=== OVERALL STATS ===
Total services: 4
Total checks: 48
Global uptime: 91.67%
Slowest avg response: payments-api (310ms)"""


def read_report():
    with open(SLA_REPORT, "r") as f:
        return f.read()


def test_sla_report_file_exists():
    assert os.path.isfile(SLA_REPORT), (
        f"Report file {SLA_REPORT} does not exist. "
        "The student must generate this file."
    )


def test_sla_report_is_readable():
    assert os.access(SLA_REPORT, os.R_OK), (
        f"Report file {SLA_REPORT} exists but is not readable."
    )


def test_sla_report_exact_content():
    content = read_report()
    # Normalize line endings
    content = content.replace("\r\n", "\n").rstrip("\n")
    expected = EXPECTED_CONTENT.rstrip("\n")
    assert content == expected, (
        f"Report content does not match expected.\n"
        f"--- EXPECTED ---\n{expected}\n"
        f"--- ACTUAL ---\n{content}\n"
        f"--- DIFF (first differing line) ---\n"
        + _first_diff(expected.splitlines(), content.splitlines())
    )


def _first_diff(expected_lines, actual_lines):
    max_lines = max(len(expected_lines), len(actual_lines))
    for i in range(max_lines):
        exp = expected_lines[i] if i < len(expected_lines) else "<missing>"
        act = actual_lines[i] if i < len(actual_lines) else "<missing>"
        if exp != act:
            return f"Line {i+1}:\n  Expected: {exp!r}\n  Actual:   {act!r}"
    return "No differences found (lengths differ?)"


def test_header_line():
    content = read_report()
    lines = content.replace("\r\n", "\n").splitlines()
    assert lines[0] == "=== SLA COMPLIANCE REPORT ===", (
        f"First line should be '=== SLA COMPLIANCE REPORT ===' but got: {lines[0]!r}"
    )


def test_checks_per_service_line():
    content = read_report()
    assert "Generated checks per service: 12" in content, (
        "Report must contain 'Generated checks per service: 12'"
    )


def test_service_summary_header():
    content = read_report()
    assert "SERVICE SUMMARY\n---------------" in content.replace("\r\n", "\n"), (
        "Report must contain 'SERVICE SUMMARY' followed by '---------------'"
    )


def test_api_gateway_block():
    content = read_report()
    assert "api-gateway" in content, "Report must contain 'api-gateway'"
    assert "  Checks: 12 | Up: 11 | Down: 1" in content, (
        "api-gateway block must have 'Checks: 12 | Up: 11 | Down: 1'"
    )
    assert "  Uptime: 91.67%" in content, (
        "api-gateway block must have 'Uptime: 91.67%'"
    )
    assert "  SLA Target: 99.9%" in content, (
        "api-gateway block must have 'SLA Target: 99.9%'"
    )
    assert "  SLA Status: BREACH" in content, (
        "api-gateway block must have 'SLA Status: BREACH'"
    )
    assert "  Avg Response (up checks): 148ms" in content, (
        "api-gateway block must have 'Avg Response (up checks): 148ms'"
    )


def test_auth_service_block():
    content = read_report()
    assert "auth-service" in content, "Report must contain 'auth-service'"
    assert "  Checks: 12 | Up: 12 | Down: 0" in content, (
        "auth-service block must have 'Checks: 12 | Up: 12 | Down: 0'"
    )
    assert "  Uptime: 100.00%" in content, (
        "auth-service block must have 'Uptime: 100.00%'"
    )
    assert "  SLA Target: 99.5%" in content, (
        "auth-service block must have 'SLA Target: 99.5%'"
    )
    assert "  SLA Status: OK" in content, (
        "auth-service block must have 'SLA Status: OK'"
    )
    assert "  Avg Response (up checks): 87ms" in content, (
        "auth-service block must have 'Avg Response (up checks): 87ms'"
    )


def test_payments_api_block():
    content = read_report()
    assert "payments-api" in content, "Report must contain 'payments-api'"
    assert "  Checks: 12 | Up: 9 | Down: 3" in content, (
        "payments-api block must have 'Checks: 12 | Up: 9 | Down: 3'"
    )
    assert "  Uptime: 75.00%" in content, (
        "payments-api block must have 'Uptime: 75.00%'"
    )
    assert "  SLA Target: 99.95%" in content, (
        "payments-api block must have 'SLA Target: 99.95%'"
    )
    # payments-api SLA Status: BREACH is also present; check it appears for payments-api
    # We'll check the full block ordering below
    assert "  Avg Response (up checks): 310ms" in content, (
        "payments-api block must have 'Avg Response (up checks): 310ms'"
    )


def test_user_service_block():
    content = read_report()
    assert "user-service" in content, "Report must contain 'user-service'"
    assert "  Checks: 12 | Up: 12 | Down: 0" in content, (
        "user-service block must have 'Checks: 12 | Up: 12 | Down: 0'"
    )
    assert "  SLA Target: 99.0%" in content, (
        "user-service block must have 'SLA Target: 99.0%'"
    )
    assert "  Avg Response (up checks): 212ms" in content, (
        "user-service block must have 'Avg Response (up checks): 212ms'"
    )


def test_services_in_alphabetical_order():
    content = read_report().replace("\r\n", "\n")
    # Find positions of service names in SERVICE SUMMARY section
    summary_start = content.find("SERVICE SUMMARY")
    breach_start = content.find("=== BREACH SUMMARY ===")
    summary_section = content[summary_start:breach_start]

    api_pos = summary_section.find("api-gateway")
    auth_pos = summary_section.find("auth-service")
    pay_pos = summary_section.find("payments-api")
    user_pos = summary_section.find("user-service")

    assert api_pos != -1, "api-gateway not found in SERVICE SUMMARY section"
    assert auth_pos != -1, "auth-service not found in SERVICE SUMMARY section"
    assert pay_pos != -1, "payments-api not found in SERVICE SUMMARY section"
    assert user_pos != -1, "user-service not found in SERVICE SUMMARY section"

    assert api_pos < auth_pos < pay_pos < user_pos, (
        f"Services in SERVICE SUMMARY are not in alphabetical order. "
        f"Positions: api-gateway={api_pos}, auth-service={auth_pos}, "
        f"payments-api={pay_pos}, user-service={user_pos}"
    )


def test_breach_summary_header():
    content = read_report()
    assert "=== BREACH SUMMARY ===" in content, (
        "Report must contain '=== BREACH SUMMARY ==='"
    )


def test_breach_summary_count():
    content = read_report()
    assert "Services in breach: 2" in content, (
        "BREACH SUMMARY must contain 'Services in breach: 2'"
    )


def test_breach_summary_api_gateway():
    content = read_report()
    assert "api-gateway: 91.67% uptime (target: 99.9%)" in content, (
        "BREACH SUMMARY must contain 'api-gateway: 91.67% uptime (target: 99.9%)'"
    )


def test_breach_summary_payments_api():
    content = read_report()
    assert "payments-api: 75.00% uptime (target: 99.95%)" in content, (
        "BREACH SUMMARY must contain 'payments-api: 75.00% uptime (target: 99.95%)'"
    )


def test_breach_summary_alphabetical_order():
    content = read_report().replace("\r\n", "\n")
    breach_start = content.find("=== BREACH SUMMARY ===")
    overall_start = content.find("=== OVERALL STATS ===")
    breach_section = content[breach_start:overall_start]

    api_pos = breach_section.find("api-gateway:")
    pay_pos = breach_section.find("payments-api:")

    assert api_pos != -1, "api-gateway not found in BREACH SUMMARY"
    assert pay_pos != -1, "payments-api not found in BREACH SUMMARY"
    assert api_pos < pay_pos, (
        "In BREACH SUMMARY, api-gateway must appear before payments-api (alphabetical order)"
    )


def test_no_ok_services_in_breach_summary():
    content = read_report().replace("\r\n", "\n")
    breach_start = content.find("=== BREACH SUMMARY ===")
    overall_start = content.find("=== OVERALL STATS ===")
    breach_section = content[breach_start:overall_start]

    assert "auth-service:" not in breach_section, (
        "auth-service should NOT appear in BREACH SUMMARY (it is OK)"
    )
    assert "user-service:" not in breach_section, (
        "user-service should NOT appear in BREACH SUMMARY (it is OK)"
    )


def test_overall_stats_header():
    content = read_report()
    assert "=== OVERALL STATS ===" in content, (
        "Report must contain '=== OVERALL STATS ==='"
    )


def test_overall_total_services():
    content = read_report()
    assert "Total services: 4" in content, (
        "OVERALL STATS must contain 'Total services: 4'"
    )


def test_overall_total_checks():
    content = read_report()
    assert "Total checks: 48" in content, (
        "OVERALL STATS must contain 'Total checks: 48'"
    )


def test_overall_global_uptime():
    content = read_report()
    assert "Global uptime: 91.67%" in content, (
        "OVERALL STATS must contain 'Global uptime: 91.67%'"
    )


def test_overall_slowest_avg_response():
    content = read_report()
    assert "Slowest avg response: payments-api (310ms)" in content, (
        "OVERALL STATS must contain 'Slowest avg response: payments-api (310ms)'"
    )


def test_blank_lines_between_service_blocks():
    """Check that there is a blank line between each service block in SERVICE SUMMARY."""
    content = read_report().replace("\r\n", "\n")
    summary_start = content.find("SERVICE SUMMARY")
    breach_start = content.find("=== BREACH SUMMARY ===")
    summary_section = content[summary_start:breach_start]

    # Each service block ends with the avg response line, then a blank line
    # Check that "148ms" is followed by a blank line before "auth-service"
    assert "148ms\n\nauth-service" in summary_section, (
        "There must be a blank line between api-gateway block and auth-service block"
    )
    assert "87ms\n\npayments-api" in summary_section, (
        "There must be a blank line between auth-service block and payments-api block"
    )
    assert "310ms\n\nuser-service" in summary_section, (
        "There must be a blank line between payments-api block and user-service block"
    )


def test_report_ends_with_slowest_response_line():
    """The report should end with the slowest avg response line (no trailing blank lines required,
    but the last meaningful line must be the slowest avg response)."""
    content = read_report().replace("\r\n", "\n").rstrip("\n")
    last_line = content.splitlines()[-1]
    assert last_line == "Slowest avg response: payments-api (310ms)", (
        f"The last line of the report must be 'Slowest avg response: payments-api (310ms)', "
        f"got: {last_line!r}"
    )