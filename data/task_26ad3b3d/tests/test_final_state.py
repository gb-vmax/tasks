# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/audit/report.txt"

EXPECTED_CONTENT = """\
=== COMPLIANCE AUDIT REPORT ===
Generated for: /home/user/audit/configs

--- database.ini ---
ssl_enabled: PASS
max_connections: PASS
log_level: PASS
auth_required: FAIL
timeout_seconds: FAIL
Status: NON-COMPLIANT

--- mailrelay.ini ---
ssl_enabled: PASS
max_connections: PASS
log_level: PASS
auth_required: PASS
timeout_seconds: PASS
Status: COMPLIANT

--- webserver.ini ---
ssl_enabled: PASS
max_connections: FAIL
log_level: FAIL
auth_required: PASS
timeout_seconds: PASS
Status: NON-COMPLIANT

=== SUMMARY ===
Total files checked: 3
Compliant: 1
Non-compliant: 2
Compliance rate: 33%

=== FAILED RULES ACROSS ALL FILES ===
max_connections: webserver.ini
log_level: webserver.ini
auth_required: database.ini
timeout_seconds: database.ini
"""


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file does not exist at {REPORT_PATH}. "
        "The task requires writing the audit report to this path."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file at {REPORT_PATH} exists but is not readable."
    )


def test_report_exact_content():
    with open(REPORT_PATH, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_CONTENT, (
        f"Report file content does not match expected.\n"
        f"--- EXPECTED ---\n{repr(EXPECTED_CONTENT)}\n"
        f"--- ACTUAL ---\n{repr(actual)}"
    )


def test_report_header():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert content.startswith("=== COMPLIANCE AUDIT REPORT ===\n"), (
        "Report must start with '=== COMPLIANCE AUDIT REPORT ===\\n'. "
        f"Actual start: {repr(content[:50])}"
    )


def test_report_generated_for_line():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert "Generated for: /home/user/audit/configs\n" in content, (
        "Report must contain 'Generated for: /home/user/audit/configs'. "
        f"Content:\n{content}"
    )


def test_report_files_in_alphabetical_order():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    db_pos = content.find("--- database.ini ---")
    mail_pos = content.find("--- mailrelay.ini ---")
    web_pos = content.find("--- webserver.ini ---")
    assert db_pos != -1, "Report missing '--- database.ini ---' block."
    assert mail_pos != -1, "Report missing '--- mailrelay.ini ---' block."
    assert web_pos != -1, "Report missing '--- webserver.ini ---' block."
    assert db_pos < mail_pos < web_pos, (
        f"Files must appear in alphabetical order (database, mailrelay, webserver). "
        f"Positions: database={db_pos}, mailrelay={mail_pos}, webserver={web_pos}"
    )


def test_database_ini_block():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_block = (
        "--- database.ini ---\n"
        "ssl_enabled: PASS\n"
        "max_connections: PASS\n"
        "log_level: PASS\n"
        "auth_required: FAIL\n"
        "timeout_seconds: FAIL\n"
        "Status: NON-COMPLIANT"
    )
    assert expected_block in content, (
        f"database.ini block is incorrect.\nExpected block:\n{expected_block}\n"
        f"Actual content:\n{content}"
    )


def test_mailrelay_ini_block():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_block = (
        "--- mailrelay.ini ---\n"
        "ssl_enabled: PASS\n"
        "max_connections: PASS\n"
        "log_level: PASS\n"
        "auth_required: PASS\n"
        "timeout_seconds: PASS\n"
        "Status: COMPLIANT"
    )
    assert expected_block in content, (
        f"mailrelay.ini block is incorrect.\nExpected block:\n{expected_block}\n"
        f"Actual content:\n{content}"
    )


def test_webserver_ini_block():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_block = (
        "--- webserver.ini ---\n"
        "ssl_enabled: PASS\n"
        "max_connections: FAIL\n"
        "log_level: FAIL\n"
        "auth_required: PASS\n"
        "timeout_seconds: PASS\n"
        "Status: NON-COMPLIANT"
    )
    assert expected_block in content, (
        f"webserver.ini block is incorrect.\nExpected block:\n{expected_block}\n"
        f"Actual content:\n{content}"
    )


def test_summary_section():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_summary = (
        "=== SUMMARY ===\n"
        "Total files checked: 3\n"
        "Compliant: 1\n"
        "Non-compliant: 2\n"
        "Compliance rate: 33%"
    )
    assert expected_summary in content, (
        f"Summary section is incorrect.\nExpected:\n{expected_summary}\n"
        f"Actual content:\n{content}"
    )


def test_failed_rules_section():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    expected_failed = (
        "=== FAILED RULES ACROSS ALL FILES ===\n"
        "max_connections: webserver.ini\n"
        "log_level: webserver.ini\n"
        "auth_required: database.ini\n"
        "timeout_seconds: database.ini\n"
    )
    assert expected_failed in content, (
        f"Failed rules section is incorrect.\nExpected:\n{expected_failed}\n"
        f"Actual content:\n{content}"
    )


def test_ssl_enabled_not_in_failed_rules():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    # Find the failed rules section
    failed_section_start = content.find("=== FAILED RULES ACROSS ALL FILES ===")
    assert failed_section_start != -1, "Missing '=== FAILED RULES ACROSS ALL FILES ===' section."
    failed_section = content[failed_section_start:]
    assert "ssl_enabled" not in failed_section, (
        "ssl_enabled passed in all files and should NOT appear in the failed rules section. "
        f"Failed section:\n{failed_section}"
    )


def test_blank_line_before_summary():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    # There should be a blank line between the last file block and === SUMMARY ===
    assert "Status: NON-COMPLIANT\n\n=== SUMMARY ===" in content, (
        "There must be exactly one blank line between the last file block (webserver.ini NON-COMPLIANT) "
        "and '=== SUMMARY ==='.\n"
        f"Actual content around that area:\n{content[content.find('=== SUMMARY ===') - 60:content.find('=== SUMMARY ===') + 20]}"
    )


def test_blank_line_between_summary_and_failed_rules():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    # There should be a blank line between the summary block and the failed rules section
    assert "Compliance rate: 33%\n\n=== FAILED RULES ACROSS ALL FILES ===" in content, (
        "There must be exactly one blank line between the summary block and "
        "'=== FAILED RULES ACROSS ALL FILES ==='.\n"
        f"Actual content:\n{content}"
    )


def test_report_ends_with_trailing_newline():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        "Report file must end with a trailing newline. "
        f"Last 20 chars: {repr(content[-20:])}"
    )


def test_report_line_count():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()
    expected_lines = EXPECTED_CONTENT.splitlines(keepends=True)
    assert len(lines) == len(expected_lines), (
        f"Report has {len(lines)} lines, expected {len(expected_lines)} lines.\n"
        f"Actual content:\n{''.join(lines)}"
    )


def test_no_full_path_in_file_headers():
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    # File blocks should use just the filename, not full path
    assert "--- /home/user/audit/configs/database.ini ---" not in content, (
        "File headers must use just the filename, not the full path."
    )
    assert "--- /home/user/audit/configs/mailrelay.ini ---" not in content, (
        "File headers must use just the filename, not the full path."
    )
    assert "--- /home/user/audit/configs/webserver.ini ---" not in content, (
        "File headers must use just the filename, not the full path."
    )