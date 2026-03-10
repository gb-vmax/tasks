# test_final_state.py

import os
import stat
import pytest

REPORT_PATH = "/home/user/iot_deploy/security_report.txt"

EXPECTED_REPORT = """\
=== IOT SECURITY AUDIT REPORT ===
Scanned directory: /home/user/iot_deploy

--- SECTION 1: HARDCODED CREDENTIALS ---
Total findings: 4
device.conf:5: password=admin123
mqtt.conf:4: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
startup.sh:6: api_key=AKIAIOSFODNN7EXAMPLE
watchdog.service:6: secret=watchdog_secret_key_9x2k

--- SECTION 2: FILE PERMISSION AUDIT ---
startup.sh: UNSAFE
device.conf: OK
mqtt.conf: UNSAFE
watchdog.service: OK
Total unsafe files: 2

--- SECTION 3: INSECURE PROTOCOLS ---
Total findings: 4
device.conf:7: management_protocol=telnet
device.conf:8: backup_url=ftp://backup.internal.example.com/configs
startup.sh:7: update_server=http://updates.internal.example.com/firmware
startup.sh:8: telnet_fallback=disabled

--- SUMMARY ---
Total issues found: 10
Risk level: CRITICAL"""


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def read_report():
    with open(REPORT_PATH, "r") as f:
        return f.read()


# ---------------------------------------------------------------------------
# 1. Report file existence
# ---------------------------------------------------------------------------

def test_security_report_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Security report not found at {REPORT_PATH}. "
        "The task requires generating this file."
    )


# ---------------------------------------------------------------------------
# 2. Exact content match
# ---------------------------------------------------------------------------

def test_security_report_exact_content():
    actual = read_report().rstrip("\n")
    expected = EXPECTED_REPORT.rstrip("\n")
    assert actual == expected, (
        f"Security report content does not match expected.\n"
        f"--- EXPECTED ---\n{expected}\n"
        f"--- ACTUAL ---\n{actual}\n"
    )


# ---------------------------------------------------------------------------
# 3. Line-by-line structural checks (provide clear failure messages)
# ---------------------------------------------------------------------------

def _report_lines():
    return read_report().splitlines()


def test_report_header():
    lines = _report_lines()
    assert lines[0] == "=== IOT SECURITY AUDIT REPORT ===", (
        f"Line 1 should be '=== IOT SECURITY AUDIT REPORT ===' but got: '{lines[0]}'"
    )


def test_report_scanned_directory():
    lines = _report_lines()
    assert lines[1] == "Scanned directory: /home/user/iot_deploy", (
        f"Line 2 should be 'Scanned directory: /home/user/iot_deploy' but got: '{lines[1]}'"
    )


def test_section1_header():
    lines = _report_lines()
    assert "--- SECTION 1: HARDCODED CREDENTIALS ---" in lines, (
        "Section 1 header '--- SECTION 1: HARDCODED CREDENTIALS ---' not found in report."
    )


def test_section1_total_findings():
    lines = _report_lines()
    idx = lines.index("--- SECTION 1: HARDCODED CREDENTIALS ---")
    total_line = lines[idx + 1]
    assert total_line == "Total findings: 4", (
        f"Section 1 total findings line should be 'Total findings: 4' but got: '{total_line}'"
    )


def test_section1_finding_device_conf_password():
    lines = _report_lines()
    expected = "device.conf:5: password=admin123"
    assert expected in lines, (
        f"Expected credential finding '{expected}' not found in report."
    )


def test_section1_finding_mqtt_conf_token():
    lines = _report_lines()
    expected = "mqtt.conf:4: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    assert expected in lines, (
        f"Expected credential finding '{expected}' not found in report."
    )


def test_section1_finding_startup_sh_api_key():
    lines = _report_lines()
    expected = "startup.sh:6: api_key=AKIAIOSFODNN7EXAMPLE"
    assert expected in lines, (
        f"Expected credential finding '{expected}' not found in report."
    )


def test_section1_finding_watchdog_service_secret():
    lines = _report_lines()
    expected = "watchdog.service:6: secret=watchdog_secret_key_9x2k"
    assert expected in lines, (
        f"Expected credential finding '{expected}' not found in report."
    )


def test_section1_no_comment_lines_included():
    lines = _report_lines()
    # Commented-out credentials must NOT appear as findings
    bad = [
        "startup.sh:3: # password=ignored_because_comment",
        "device.conf:4: # secret=this_is_a_comment_ignore_me",
        "mqtt.conf:5: # token=old_token_do_not_use",
    ]
    for bad_line in bad:
        assert bad_line not in lines, (
            f"Comment line '{bad_line}' should NOT appear as a finding in the report."
        )


def test_section1_findings_sorted():
    lines = _report_lines()
    idx = lines.index("--- SECTION 1: HARDCODED CREDENTIALS ---")
    # skip "Total findings: N"
    finding_lines = []
    for line in lines[idx + 2:]:
        if line.startswith("---"):
            break
        if line.strip():
            finding_lines.append(line)
    assert finding_lines == sorted(finding_lines, key=lambda l: (l.split(":")[0], int(l.split(":")[1]))), (
        f"Section 1 findings are not sorted by filename then line number. Got: {finding_lines}"
    )


def test_section2_header():
    lines = _report_lines()
    assert "--- SECTION 2: FILE PERMISSION AUDIT ---" in lines, (
        "Section 2 header '--- SECTION 2: FILE PERMISSION AUDIT ---' not found in report."
    )


def test_section2_startup_sh_unsafe():
    lines = _report_lines()
    assert "startup.sh: UNSAFE" in lines, (
        "startup.sh should be listed as UNSAFE in Section 2 (it is world-writable 0777)."
    )


def test_section2_device_conf_ok():
    lines = _report_lines()
    assert "device.conf: OK" in lines, (
        "device.conf should be listed as OK in Section 2 (permissions 0644)."
    )


def test_section2_mqtt_conf_unsafe():
    lines = _report_lines()
    assert "mqtt.conf: UNSAFE" in lines, (
        "mqtt.conf should be listed as UNSAFE in Section 2 (it is world-writable 0666)."
    )


def test_section2_watchdog_service_ok():
    lines = _report_lines()
    assert "watchdog.service: OK" in lines, (
        "watchdog.service should be listed as OK in Section 2 (permissions 0644)."
    )


def test_section2_total_unsafe_files():
    lines = _report_lines()
    assert "Total unsafe files: 2" in lines, (
        "Section 2 should report 'Total unsafe files: 2' (startup.sh and mqtt.conf)."
    )


def test_section3_header():
    lines = _report_lines()
    assert "--- SECTION 3: INSECURE PROTOCOLS ---" in lines, (
        "Section 3 header '--- SECTION 3: INSECURE PROTOCOLS ---' not found in report."
    )


def test_section3_total_findings():
    lines = _report_lines()
    idx = lines.index("--- SECTION 3: INSECURE PROTOCOLS ---")
    total_line = lines[idx + 1]
    assert total_line == "Total findings: 4", (
        f"Section 3 total findings line should be 'Total findings: 4' but got: '{total_line}'"
    )


def test_section3_finding_device_conf_telnet():
    lines = _report_lines()
    expected = "device.conf:7: management_protocol=telnet"
    assert expected in lines, (
        f"Expected insecure protocol finding '{expected}' not found in report."
    )


def test_section3_finding_device_conf_ftp():
    lines = _report_lines()
    expected = "device.conf:8: backup_url=ftp://backup.internal.example.com/configs"
    assert expected in lines, (
        f"Expected insecure protocol finding '{expected}' not found in report."
    )


def test_section3_finding_startup_sh_http():
    lines = _report_lines()
    expected = "startup.sh:7: update_server=http://updates.internal.example.com/firmware"
    assert expected in lines, (
        f"Expected insecure protocol finding '{expected}' not found in report."
    )


def test_section3_finding_startup_sh_telnet():
    lines = _report_lines()
    expected = "startup.sh:8: telnet_fallback=disabled"
    assert expected in lines, (
        f"Expected insecure protocol finding '{expected}' not found in report."
    )


def test_section3_findings_sorted():
    lines = _report_lines()
    idx = lines.index("--- SECTION 3: INSECURE PROTOCOLS ---")
    finding_lines = []
    for line in lines[idx + 2:]:
        if line.startswith("---"):
            break
        if line.strip():
            finding_lines.append(line)
    assert finding_lines == sorted(finding_lines, key=lambda l: (l.split(":")[0], int(l.split(":")[1]))), (
        f"Section 3 findings are not sorted by filename then line number. Got: {finding_lines}"
    )


def test_summary_header():
    lines = _report_lines()
    assert "--- SUMMARY ---" in lines, (
        "'--- SUMMARY ---' header not found in report."
    )


def test_summary_total_issues():
    lines = _report_lines()
    assert "Total issues found: 10" in lines, (
        "Summary should state 'Total issues found: 10' "
        "(4 credential findings + 2 unsafe files + 4 insecure protocol findings = 10)."
    )


def test_summary_risk_level():
    lines = _report_lines()
    assert "Risk level: CRITICAL" in lines, (
        "Summary should state 'Risk level: CRITICAL' (10 total issues >= 8 threshold)."
    )


# ---------------------------------------------------------------------------
# 4. Verify underlying file permissions are still as expected
# ---------------------------------------------------------------------------

def test_startup_sh_still_world_writable():
    path = "/home/user/iot_deploy/startup.sh"
    mode = os.stat(path).st_mode
    assert mode & stat.S_IWOTH, (
        f"{path} should be world-writable (0777) but mode is {oct(mode)}. "
        "The task should not have changed file permissions."
    )


def test_mqtt_conf_still_world_writable():
    path = "/home/user/iot_deploy/configs/mqtt.conf"
    mode = os.stat(path).st_mode
    assert mode & stat.S_IWOTH, (
        f"{path} should be world-writable (0666) but mode is {oct(mode)}. "
        "The task should not have changed file permissions."
    )


def test_device_conf_still_not_world_writable():
    path = "/home/user/iot_deploy/configs/device.conf"
    mode = os.stat(path).st_mode
    assert not (mode & stat.S_IWOTH), (
        f"{path} should NOT be world-writable (0644) but mode is {oct(mode)}."
    )


def test_watchdog_service_still_not_world_writable():
    path = "/home/user/iot_deploy/services/watchdog.service"
    mode = os.stat(path).st_mode
    assert not (mode & stat.S_IWOTH), (
        f"{path} should NOT be world-writable (0644) but mode is {oct(mode)}."
    )


# ---------------------------------------------------------------------------
# 5. Report should not contain false positives (commented-out lines)
# ---------------------------------------------------------------------------

def test_report_does_not_contain_commented_password():
    content = read_report()
    assert "# password=ignored_because_comment" not in content, (
        "The report must not include the commented-out password line from startup.sh."
    )


def test_report_does_not_contain_commented_secret():
    content = read_report()
    assert "# secret=this_is_a_comment_ignore_me" not in content, (
        "The report must not include the commented-out secret line from device.conf."
    )


def test_report_does_not_contain_commented_token():
    content = read_report()
    assert "# token=old_token_do_not_use" not in content, (
        "The report must not include the commented-out token line from mqtt.conf."
    )