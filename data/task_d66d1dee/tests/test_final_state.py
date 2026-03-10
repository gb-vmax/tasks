# test_final_state.py

import os
import pytest

REPORT_FILE = "/home/user/policy/compliance_report.txt"

EXPECTED_CONTENT = """\
=== SECURITY BENCHMARK COMPLIANCE REPORT ===

CONTROL RESULTS:
  [FAIL] CIS-1.1: Ensure password expiry is 90 days or less (expected lte 90, got 120)
  [PASS] CIS-1.2: Ensure minimum password length is 12 or more (expected gte 12, got 14)
  [PASS] CIS-2.1: Ensure SSH MaxAuthTries is 4 or less (expected lte 4, got 3)
  [PASS] CIS-2.2: Ensure SSH protocol version is 2 (expected gte 2, got 2)
  [PASS] CIS-3.1: Ensure core dump hard limit is 0 (expected lte 0, got 0)

SUMMARY:
Total controls: 5
Passed: 4
Failed: 1
Compliance: 80%

OVERALL STATUS: NON-COMPLIANT
"""


def test_compliance_report_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Compliance report '{REPORT_FILE}' does not exist. "
        "The task requires generating this file."
    )


def test_compliance_report_not_empty():
    assert os.path.getsize(REPORT_FILE) > 0, (
        f"Compliance report '{REPORT_FILE}' exists but is empty. "
        "The report must contain compliance results."
    )


def test_compliance_report_exact_content():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()

    assert actual_content == EXPECTED_CONTENT, (
        f"Compliance report content does not match expected.\n\n"
        f"--- EXPECTED ---\n{EXPECTED_CONTENT!r}\n\n"
        f"--- ACTUAL ---\n{actual_content!r}\n\n"
        f"Differences detected. Please verify formatting, spacing, and values."
    )


def test_compliance_report_header():
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 1, (
        f"Compliance report '{REPORT_FILE}' has no lines."
    )
    assert lines[0].rstrip("\n") == "=== SECURITY BENCHMARK COMPLIANCE REPORT ===", (
        f"First line of report is incorrect.\n"
        f"  Expected: '=== SECURITY BENCHMARK COMPLIANCE REPORT ==='\n"
        f"  Got:      {lines[0].rstrip()!r}"
    )


def test_compliance_report_control_results_section():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    assert "CONTROL RESULTS:" in content, (
        "Compliance report is missing the 'CONTROL RESULTS:' section header."
    )


def test_compliance_report_fail_line():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    expected_fail_line = "  [FAIL] CIS-1.1: Ensure password expiry is 90 days or less (expected lte 90, got 120)"
    assert expected_fail_line in content, (
        f"Compliance report is missing or has incorrect FAIL line for CIS-1.1.\n"
        f"  Expected line: {expected_fail_line!r}\n"
        f"  Report content:\n{content}"
    )


def test_compliance_report_pass_lines():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    expected_pass_lines = [
        "  [PASS] CIS-1.2: Ensure minimum password length is 12 or more (expected gte 12, got 14)",
        "  [PASS] CIS-2.1: Ensure SSH MaxAuthTries is 4 or less (expected lte 4, got 3)",
        "  [PASS] CIS-2.2: Ensure SSH protocol version is 2 (expected gte 2, got 2)",
        "  [PASS] CIS-3.1: Ensure core dump hard limit is 0 (expected lte 0, got 0)",
    ]

    for line in expected_pass_lines:
        assert line in content, (
            f"Compliance report is missing or has incorrect PASS line.\n"
            f"  Expected line: {line!r}\n"
            f"  Report content:\n{content}"
        )


def test_compliance_report_summary_section():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    assert "SUMMARY:" in content, (
        "Compliance report is missing the 'SUMMARY:' section."
    )
    assert "Total controls: 5" in content, (
        "Compliance report summary has incorrect 'Total controls' value. Expected: 'Total controls: 5'"
    )
    assert "Passed: 4" in content, (
        "Compliance report summary has incorrect 'Passed' value. Expected: 'Passed: 4'"
    )
    assert "Failed: 1" in content, (
        "Compliance report summary has incorrect 'Failed' value. Expected: 'Failed: 1'"
    )
    assert "Compliance: 80%" in content, (
        "Compliance report summary has incorrect 'Compliance' percentage. Expected: 'Compliance: 80%'"
    )


def test_compliance_report_overall_status():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    assert "OVERALL STATUS: NON-COMPLIANT" in content, (
        "Compliance report has incorrect or missing OVERALL STATUS.\n"
        "Expected: 'OVERALL STATUS: NON-COMPLIANT'\n"
        f"Report content:\n{content}"
    )


def test_compliance_report_no_decimal_values():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    # Check that numeric values in control lines don't have decimal points
    import re
    control_lines = [line for line in content.splitlines() if "[PASS]" in line or "[FAIL]" in line]
    for line in control_lines:
        # Extract the "got <value>" and "expected <op> <threshold>" parts
        match = re.search(r'expected \w+ (\S+), got (\S+)\)', line)
        assert match, (
            f"Could not parse threshold/value from control line: {line!r}"
        )
        threshold_str, value_str = match.group(1), match.group(2)
        assert "." not in threshold_str, (
            f"Threshold '{threshold_str}' in line {line!r} should be an integer (no decimal point)."
        )
        assert "." not in value_str, (
            f"Value '{value_str}' in line {line!r} should be an integer (no decimal point)."
        )


def test_compliance_report_control_order():
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    control_ids_in_order = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("[PASS]") or stripped.startswith("[FAIL]"):
            # Extract control_id (first token after [PASS] or [FAIL])
            parts = stripped.split("] ", 1)
            if len(parts) == 2:
                control_id = parts[1].split(":")[0].strip()
                control_ids_in_order.append(control_id)

    expected_order = ["CIS-1.1", "CIS-1.2", "CIS-2.1", "CIS-2.2", "CIS-3.1"]
    assert control_ids_in_order == expected_order, (
        f"Controls are not listed in the correct order.\n"
        f"  Expected order: {expected_order}\n"
        f"  Actual order:   {control_ids_in_order}"
    )


def test_compliance_report_indentation():
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    for line in lines:
        stripped = line.rstrip("\n")
        if "[PASS]" in stripped or "[FAIL]" in stripped:
            assert stripped.startswith("  "), (
                f"Control result line does not start with exactly two spaces of indentation.\n"
                f"  Line: {stripped!r}"
            )
            assert not stripped.startswith("   "), (
                f"Control result line has more than two spaces of indentation.\n"
                f"  Line: {stripped!r}"
            )


def test_compliance_report_no_compliant_status():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    # Make sure it says NON-COMPLIANT, not COMPLIANT (without NON-)
    lines = content.splitlines()
    for line in lines:
        if "OVERALL STATUS:" in line:
            assert "NON-COMPLIANT" in line, (
                f"OVERALL STATUS line should say 'NON-COMPLIANT' but got: {line!r}"
            )
            assert line.strip() == "OVERALL STATUS: NON-COMPLIANT", (
                f"OVERALL STATUS line format is incorrect.\n"
                f"  Expected: 'OVERALL STATUS: NON-COMPLIANT'\n"
                f"  Got:      {line.strip()!r}"
            )