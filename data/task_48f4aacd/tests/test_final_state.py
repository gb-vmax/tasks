# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/diagnostics/report.txt"

EXPECTED_CONTENT = """\
=== DIAGNOSTICS REPORT ===

--- ACCESS LOG ---
Total requests: 15
Status codes:
  200: 9
  401: 1
  403: 1
  404: 2
  500: 2
Top endpoints:
  /api/users: 6
  /api/products: 3
  /api/login: 2
Total bandwidth: 19161 bytes

--- APPLICATION LOG ---
Log levels:
  ERROR: 3
  INFO: 5
  WARN: 2
Errors:
  - Unhandled exception in product handler: NullPointerException
  - Database query timeout after 30s on table orders
  - Failed to connect to cache: Connection refused
First log entry: 2024-03-15 08:55:01
Last log entry: 2024-03-15 09:01:15

--- SYSTEM LOG ---
Unique processes: 4
Error-related lines: 3
Top processes:
  systemd: 5
  cron: 3
"""


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The task requires generating this diagnostics report."
    )


def test_report_ends_with_newline():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        "The report file must end with a newline character."
    )


def test_report_no_trailing_spaces():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped_line = line.rstrip("\n")
        assert stripped_line == stripped_line.rstrip(), (
            f"Line {i} has trailing spaces: {repr(stripped_line)}"
        )


def test_report_exact_content():
    with open(REPORT_PATH, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_CONTENT, (
        f"Report content does not match expected.\n"
        f"--- EXPECTED ---\n{EXPECTED_CONTENT!r}\n"
        f"--- ACTUAL ---\n{actual!r}"
    )


def test_report_header():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    assert lines[0].rstrip("\n") == "=== DIAGNOSTICS REPORT ===", (
        f"First line should be '=== DIAGNOSTICS REPORT ===', got: {lines[0]!r}"
    )


def test_report_access_log_section():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert "--- ACCESS LOG ---" in content, (
        "Report is missing the '--- ACCESS LOG ---' section header."
    )
    assert "Total requests: 15" in content, (
        "Report should contain 'Total requests: 15'."
    )
    assert "  200: 9" in content, (
        "Report should contain '  200: 9' in status codes."
    )
    assert "  401: 1" in content, (
        "Report should contain '  401: 1' in status codes."
    )
    assert "  403: 1" in content, (
        "Report should contain '  403: 1' in status codes."
    )
    assert "  404: 2" in content, (
        "Report should contain '  404: 2' in status codes."
    )
    assert "  500: 2" in content, (
        "Report should contain '  500: 2' in status codes."
    )
    assert "  /api/users: 6" in content, (
        "Report should contain '  /api/users: 6' in top endpoints."
    )
    assert "  /api/products: 3" in content, (
        "Report should contain '  /api/products: 3' in top endpoints."
    )
    assert "  /api/login: 2" in content, (
        "Report should contain '  /api/login: 2' as the 3rd top endpoint."
    )
    assert "Total bandwidth: 19161 bytes" in content, (
        "Report should contain 'Total bandwidth: 19161 bytes'."
    )


def test_report_access_log_top_endpoints_order():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    lines = [l.rstrip("\n") for l in lines]

    # Find "Top endpoints:" line
    top_ep_idx = None
    for i, line in enumerate(lines):
        if line == "Top endpoints:":
            top_ep_idx = i
            break
    assert top_ep_idx is not None, "Could not find 'Top endpoints:' line in report."

    ep_lines = []
    for line in lines[top_ep_idx + 1:]:
        if line.startswith("  ") and not line.startswith("   "):
            ep_lines.append(line.strip())
        else:
            break

    assert len(ep_lines) == 3, (
        f"Expected exactly 3 top endpoint lines, got {len(ep_lines)}: {ep_lines}"
    )
    assert ep_lines[0] == "/api/users: 6", (
        f"First top endpoint should be '/api/users: 6', got '{ep_lines[0]}'"
    )
    assert ep_lines[1] == "/api/products: 3", (
        f"Second top endpoint should be '/api/products: 3', got '{ep_lines[1]}'"
    )
    assert ep_lines[2] == "/api/login: 2", (
        f"Third top endpoint should be '/api/login: 2', got '{ep_lines[2]}'"
    )


def test_report_status_codes_order():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    lines = [l.rstrip("\n") for l in lines]

    sc_idx = None
    for i, line in enumerate(lines):
        if line == "Status codes:":
            sc_idx = i
            break
    assert sc_idx is not None, "Could not find 'Status codes:' line in report."

    sc_lines = []
    for line in lines[sc_idx + 1:]:
        if line.startswith("  ") and not line.startswith("   "):
            sc_lines.append(line.strip())
        else:
            break

    assert sc_lines == ["200: 9", "401: 1", "403: 1", "404: 2", "500: 2"], (
        f"Status codes not in correct order or values wrong: {sc_lines}"
    )


def test_report_application_log_section():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert "--- APPLICATION LOG ---" in content, (
        "Report is missing the '--- APPLICATION LOG ---' section header."
    )
    assert "  ERROR: 3" in content, (
        "Report should contain '  ERROR: 3' in log levels."
    )
    assert "  INFO: 5" in content, (
        "Report should contain '  INFO: 5' in log levels."
    )
    assert "  WARN: 2" in content, (
        "Report should contain '  WARN: 2' in log levels."
    )
    assert "  - Unhandled exception in product handler: NullPointerException" in content, (
        "Report should contain the first ERROR message."
    )
    assert "  - Database query timeout after 30s on table orders" in content, (
        "Report should contain the second ERROR message."
    )
    assert "  - Failed to connect to cache: Connection refused" in content, (
        "Report should contain the third ERROR message."
    )
    assert "First log entry: 2024-03-15 08:55:01" in content, (
        "Report should contain 'First log entry: 2024-03-15 08:55:01'."
    )
    assert "Last log entry: 2024-03-15 09:01:15" in content, (
        "Report should contain 'Last log entry: 2024-03-15 09:01:15'."
    )


def test_report_app_log_levels_order():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    lines = [l.rstrip("\n") for l in lines]

    ll_idx = None
    for i, line in enumerate(lines):
        if line == "Log levels:":
            ll_idx = i
            break
    assert ll_idx is not None, "Could not find 'Log levels:' line in report."

    ll_lines = []
    for line in lines[ll_idx + 1:]:
        if line.startswith("  ") and not line.startswith("   "):
            ll_lines.append(line.strip())
        else:
            break

    assert ll_lines == ["ERROR: 3", "INFO: 5", "WARN: 2"], (
        f"Log levels not in correct alphabetical order or values wrong: {ll_lines}"
    )


def test_report_app_log_errors_order():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    lines = [l.rstrip("\n") for l in lines]

    errors_idx = None
    for i, line in enumerate(lines):
        if line == "Errors:":
            errors_idx = i
            break
    assert errors_idx is not None, "Could not find 'Errors:' line in report."

    error_lines = []
    for line in lines[errors_idx + 1:]:
        if line.startswith("  - "):
            error_lines.append(line[4:])  # strip "  - "
        else:
            break

    assert len(error_lines) == 3, (
        f"Expected 3 error message lines, got {len(error_lines)}: {error_lines}"
    )
    assert error_lines[0] == "Unhandled exception in product handler: NullPointerException", (
        f"First error message wrong: '{error_lines[0]}'"
    )
    assert error_lines[1] == "Database query timeout after 30s on table orders", (
        f"Second error message wrong: '{error_lines[1]}'"
    )
    assert error_lines[2] == "Failed to connect to cache: Connection refused", (
        f"Third error message wrong: '{error_lines[2]}'"
    )


def test_report_system_log_section():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert "--- SYSTEM LOG ---" in content, (
        "Report is missing the '--- SYSTEM LOG ---' section header."
    )
    assert "Unique processes: 4" in content, (
        "Report should contain 'Unique processes: 4'."
    )
    assert "Error-related lines: 3" in content, (
        "Report should contain 'Error-related lines: 3'."
    )
    assert "  systemd: 5" in content, (
        "Report should contain '  systemd: 5' in top processes."
    )
    assert "  cron: 3" in content, (
        "Report should contain '  cron: 3' in top processes."
    )


def test_report_top_processes_order():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    lines = [l.rstrip("\n") for l in lines]

    tp_idx = None
    for i, line in enumerate(lines):
        if line == "Top processes:":
            tp_idx = i
            break
    assert tp_idx is not None, "Could not find 'Top processes:' line in report."

    tp_lines = []
    for line in lines[tp_idx + 1:]:
        if line.startswith("  ") and not line.startswith("   "):
            tp_lines.append(line.strip())
        else:
            break

    assert len(tp_lines) == 2, (
        f"Expected exactly 2 top process lines, got {len(tp_lines)}: {tp_lines}"
    )
    assert tp_lines[0] == "systemd: 5", (
        f"First top process should be 'systemd: 5', got '{tp_lines[0]}'"
    )
    assert tp_lines[1] == "cron: 3", (
        f"Second top process should be 'cron: 3', got '{tp_lines[1]}'"
    )


def test_report_section_separators():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    lines = [l.rstrip("\n") for l in lines]

    assert "--- ACCESS LOG ---" in lines, (
        "Report must have '--- ACCESS LOG ---' as a standalone line."
    )
    assert "--- APPLICATION LOG ---" in lines, (
        "Report must have '--- APPLICATION LOG ---' as a standalone line."
    )
    assert "--- SYSTEM LOG ---" in lines, (
        "Report must have '--- SYSTEM LOG ---' as a standalone line."
    )


def test_report_blank_line_after_header():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    lines = [l.rstrip("\n") for l in lines]

    assert lines[0] == "=== DIAGNOSTICS REPORT ===", (
        f"Line 1 should be '=== DIAGNOSTICS REPORT ===', got: {lines[0]!r}"
    )
    assert lines[1] == "", (
        f"Line 2 should be blank after the header, got: {lines[1]!r}"
    )


def test_report_line_count():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    # The expected content has a trailing newline, so split gives an empty string at end
    # Count non-trailing lines
    expected_lines = EXPECTED_CONTENT.split("\n")
    assert lines == expected_lines, (
        f"Report has {len(lines)} lines (after split on newline) but expected {len(expected_lines)}.\n"
        f"Actual lines: {lines}\nExpected lines: {expected_lines}"
    )