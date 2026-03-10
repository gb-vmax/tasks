# test_final_state.py

import os
import pytest

CONFIG_PATH = "/home/user/finops/cost_alerts.cfg"
SUMMARY_PATH = "/home/user/finops/budget_summary.txt"
FINOPS_DIR = "/home/user/finops"

EXPECTED_CONFIG_LINES = [
    "environment=production",
    "cloud_provider=aws",
    "monthly_budget_usd=12500",
    "alert_threshold_pct=80",
    "currency=USD",
    "owner_email=finops-team@company.com",
    "notify_slack=true",
    "slack_channel=#cloud-costs",
]

EXPECTED_SUMMARY_LINE = "BUDGET: $12500 | ALERT AT: 80% | CONTACT: finops-team@company.com"


# --- Config file tests ---

def test_finops_directory_exists():
    assert os.path.isdir(FINOPS_DIR), (
        f"Directory {FINOPS_DIR} does not exist. "
        "The finops working directory must be present."
    )


def test_config_file_exists():
    assert os.path.isfile(CONFIG_PATH), (
        f"Configuration file {CONFIG_PATH} does not exist. "
        "The cost_alerts.cfg file must be present after the task."
    )


def test_config_file_is_readable():
    assert os.access(CONFIG_PATH, os.R_OK), (
        f"Configuration file {CONFIG_PATH} is not readable."
    )


def test_config_file_line_count():
    with open(CONFIG_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    assert len(lines) == 8, (
        f"Expected exactly 8 lines in {CONFIG_PATH}, "
        f"found {len(lines)} lines. "
        "No lines should be added or removed, only values updated."
    )


def test_config_file_exact_content():
    with open(CONFIG_PATH, "r") as f:
        content = f.read()
    actual_lines = content.rstrip("\n").splitlines()
    assert actual_lines == EXPECTED_CONFIG_LINES, (
        f"Configuration file {CONFIG_PATH} does not match expected content.\n"
        f"Expected:\n" + "\n".join(EXPECTED_CONFIG_LINES) + "\n\n"
        f"Actual:\n" + "\n".join(actual_lines)
    )


def test_config_monthly_budget_updated():
    with open(CONFIG_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    budget_lines = [l for l in lines if l.startswith("monthly_budget_usd=")]
    assert len(budget_lines) == 1, (
        f"Expected exactly one 'monthly_budget_usd' key in {CONFIG_PATH}, "
        f"found: {budget_lines}"
    )
    assert budget_lines[0] == "monthly_budget_usd=12500", (
        f"'monthly_budget_usd' should be '12500', got: '{budget_lines[0]}'. "
        "The value must be updated from 9000 to 12500."
    )


def test_config_alert_threshold_updated():
    with open(CONFIG_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    threshold_lines = [l for l in lines if l.startswith("alert_threshold_pct=")]
    assert len(threshold_lines) == 1, (
        f"Expected exactly one 'alert_threshold_pct' key in {CONFIG_PATH}, "
        f"found: {threshold_lines}"
    )
    assert threshold_lines[0] == "alert_threshold_pct=80", (
        f"'alert_threshold_pct' should be '80', got: '{threshold_lines[0]}'. "
        "The value must be updated from 75 to 80."
    )


def test_config_owner_email_updated():
    with open(CONFIG_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    email_lines = [l for l in lines if l.startswith("owner_email=")]
    assert len(email_lines) == 1, (
        f"Expected exactly one 'owner_email' key in {CONFIG_PATH}, "
        f"found: {email_lines}"
    )
    assert email_lines[0] == "owner_email=finops-team@company.com", (
        f"'owner_email' should be 'finops-team@company.com', got: '{email_lines[0]}'. "
        "The value must be updated from analyst@company.com to finops-team@company.com."
    )


def test_config_unchanged_lines_preserved():
    with open(CONFIG_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    unchanged = [
        "environment=production",
        "cloud_provider=aws",
        "currency=USD",
        "notify_slack=true",
        "slack_channel=#cloud-costs",
    ]
    for expected_line in unchanged:
        assert expected_line in lines, (
            f"Line '{expected_line}' is missing from {CONFIG_PATH}. "
            "Lines that were not supposed to be changed must remain intact."
        )


def test_config_line_order():
    with open(CONFIG_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()
    assert lines == EXPECTED_CONFIG_LINES, (
        f"Lines in {CONFIG_PATH} are not in the correct order.\n"
        f"Expected order:\n" + "\n".join(EXPECTED_CONFIG_LINES) + "\n\n"
        f"Actual order:\n" + "\n".join(lines)
    )


# --- Summary file tests ---

def test_summary_file_exists():
    assert os.path.isfile(SUMMARY_PATH), (
        f"Summary file {SUMMARY_PATH} does not exist. "
        "The budget_summary.txt file must be created as part of the task."
    )


def test_summary_file_is_readable():
    assert os.access(SUMMARY_PATH, os.R_OK), (
        f"Summary file {SUMMARY_PATH} is not readable."
    )


def test_summary_file_exact_content():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()
    # Strip trailing newline(s) for comparison but ensure content matches
    stripped = content.strip("\n")
    assert stripped == EXPECTED_SUMMARY_LINE, (
        f"Summary file {SUMMARY_PATH} does not contain the expected content.\n"
        f"Expected: '{EXPECTED_SUMMARY_LINE}'\n"
        f"Actual:   '{stripped}'"
    )


def test_summary_file_has_exactly_one_line():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()
    lines = content.strip("\n").splitlines()
    assert len(lines) == 1, (
        f"Summary file {SUMMARY_PATH} should contain exactly one line, "
        f"but found {len(lines)} lines:\n" + "\n".join(repr(l) for l in lines)
    )


def test_summary_file_budget_value():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read().strip("\n")
    assert "$12500" in content, (
        f"Summary file {SUMMARY_PATH} should contain '$12500' for the budget, "
        f"but got: '{content}'"
    )


def test_summary_file_alert_threshold_value():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read().strip("\n")
    assert "80%" in content, (
        f"Summary file {SUMMARY_PATH} should contain '80%' for the alert threshold, "
        f"but got: '{content}'"
    )


def test_summary_file_contact_email():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read().strip("\n")
    assert "finops-team@company.com" in content, (
        f"Summary file {SUMMARY_PATH} should contain 'finops-team@company.com' as the contact, "
        f"but got: '{content}'"
    )


def test_summary_file_format():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read().strip("\n")
    assert content.startswith("BUDGET: $"), (
        f"Summary file {SUMMARY_PATH} should start with 'BUDGET: $', "
        f"but got: '{content}'"
    )
    assert "| ALERT AT:" in content, (
        f"Summary file {SUMMARY_PATH} should contain '| ALERT AT:', "
        f"but got: '{content}'"
    )
    assert "| CONTACT:" in content, (
        f"Summary file {SUMMARY_PATH} should contain '| CONTACT:', "
        f"but got: '{content}'"
    )