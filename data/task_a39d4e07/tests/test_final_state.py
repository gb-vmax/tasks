# test_final_state.py

import os
import pytest

ENV_FILE = "/home/user/finops/.env"
ENV_PRODUCTION_FILE = "/home/user/finops/.env.production"
ENV_DIR = "/home/user/finops"

EXPECTED_ENV_CONTENT = """AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
COST_ALERT_THRESHOLD_USD=750
MONTHLY_BUDGET_USD=5000
ALERT_EMAIL=finops-team@company.com
ENABLE_COST_EXPLORER=true
REPORT_INTERVAL_DAYS=7
COST_ALLOCATION_TAG=CostCenter
BILLING_API_TOKEN=tok_live_9xKp2mNqRsTuVwXy"""

EXPECTED_PRODUCTION_CONTENT = """AWS_REGION=us-east-1
COST_ALERT_THRESHOLD_USD=750
MONTHLY_BUDGET_USD=5000
ALERT_EMAIL=finops-team@company.com
ENABLE_COST_EXPLORER=true
REPORT_INTERVAL_DAYS=7
COST_ALLOCATION_TAG=CostCenter"""


# ── .env tests ────────────────────────────────────────────────────────────────

def test_finops_directory_exists():
    assert os.path.isdir(ENV_DIR), (
        f"Directory {ENV_DIR} does not exist."
    )


def test_env_file_exists():
    assert os.path.isfile(ENV_FILE), (
        f"File {ENV_FILE} does not exist."
    )


def test_env_file_exact_content():
    with open(ENV_FILE, "r") as f:
        content = f.read().strip()
    expected = EXPECTED_ENV_CONTENT.strip()
    assert content == expected, (
        f"Content of {ENV_FILE} does not match expected final state.\n"
        f"Expected:\n{expected}\n\n"
        f"Got:\n{content}"
    )


def test_env_file_line_count():
    with open(ENV_FILE, "r") as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    non_empty = [l for l in lines if l.strip()]
    assert len(non_empty) == 10, (
        f"Expected 10 non-empty lines in {ENV_FILE}, got {len(non_empty)}.\n"
        f"Lines found: {non_empty}"
    )


def test_cost_alert_threshold_updated():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    assert "COST_ALERT_THRESHOLD_USD=750" in content, (
        f"COST_ALERT_THRESHOLD_USD should be 750 in {ENV_FILE}.\n"
        f"File content:\n{content}"
    )
    assert "COST_ALERT_THRESHOLD_USD=500" not in content, (
        f"Old value COST_ALERT_THRESHOLD_USD=500 still present in {ENV_FILE}.\n"
        f"File content:\n{content}"
    )


def test_monthly_budget_updated():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    assert "MONTHLY_BUDGET_USD=5000" in content, (
        f"MONTHLY_BUDGET_USD should be 5000 in {ENV_FILE}.\n"
        f"File content:\n{content}"
    )
    assert "MONTHLY_BUDGET_USD=3000" not in content, (
        f"Old value MONTHLY_BUDGET_USD=3000 still present in {ENV_FILE}.\n"
        f"File content:\n{content}"
    )


def test_alert_email_updated():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    assert "ALERT_EMAIL=finops-team@company.com" in content, (
        f"ALERT_EMAIL should be finops-team@company.com in {ENV_FILE}.\n"
        f"File content:\n{content}"
    )
    assert "ALERT_EMAIL=old-analyst@company.com" not in content, (
        f"Old value ALERT_EMAIL=old-analyst@company.com still present in {ENV_FILE}.\n"
        f"File content:\n{content}"
    )


def test_stale_variables_removed():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    stale_vars = ["UNUSED_LEGACY_KEY", "OLD_REGION_OVERRIDE", "DEBUG_VERBOSE"]
    for var in stale_vars:
        assert var not in content, (
            f"Stale variable {var} should have been removed from {ENV_FILE} but is still present.\n"
            f"File content:\n{content}"
        )


def test_aws_credentials_retained_in_env():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    assert "AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE" in content, (
        f"AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE should be retained in {ENV_FILE}.\n"
        f"File content:\n{content}"
    )
    assert "AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" in content, (
        f"AWS_SECRET_ACCESS_KEY should be retained in {ENV_FILE}.\n"
        f"File content:\n{content}"
    )
    assert "BILLING_API_TOKEN=tok_live_9xKp2mNqRsTuVwXy" in content, (
        f"BILLING_API_TOKEN should be retained in {ENV_FILE}.\n"
        f"File content:\n{content}"
    )


def test_other_config_variables_retained_in_env():
    with open(ENV_FILE, "r") as f:
        content = f.read()
    expected_vars = {
        "AWS_REGION": "us-east-1",
        "ENABLE_COST_EXPLORER": "true",
        "REPORT_INTERVAL_DAYS": "7",
        "COST_ALLOCATION_TAG": "CostCenter",
    }
    for key, value in expected_vars.items():
        expected_line = f"{key}={value}"
        assert expected_line in content, (
            f"Expected {expected_line} to be present in {ENV_FILE}.\n"
            f"File content:\n{content}"
        )


def test_env_line_order():
    """Verify the lines appear in the correct order in .env."""
    with open(ENV_FILE, "r") as f:
        lines = [line.rstrip('\n') for line in f.readlines() if line.strip()]
    expected_lines = EXPECTED_ENV_CONTENT.strip().splitlines()
    assert lines == expected_lines, (
        f"Lines in {ENV_FILE} are not in the expected order.\n"
        f"Expected order:\n{expected_lines}\n\n"
        f"Got:\n{lines}"
    )


# ── .env.production tests ─────────────────────────────────────────────────────

def test_env_production_file_exists():
    assert os.path.isfile(ENV_PRODUCTION_FILE), (
        f"File {ENV_PRODUCTION_FILE} does not exist. It should have been created."
    )


def test_env_production_exact_content():
    with open(ENV_PRODUCTION_FILE, "r") as f:
        content = f.read().strip()
    expected = EXPECTED_PRODUCTION_CONTENT.strip()
    assert content == expected, (
        f"Content of {ENV_PRODUCTION_FILE} does not match expected.\n"
        f"Expected:\n{expected}\n\n"
        f"Got:\n{content}"
    )


def test_env_production_line_count():
    with open(ENV_PRODUCTION_FILE, "r") as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    non_empty = [l for l in lines if l.strip()]
    assert len(non_empty) == 7, (
        f"Expected 7 lines in {ENV_PRODUCTION_FILE}, got {len(non_empty)}.\n"
        f"Lines found: {non_empty}"
    )


def test_env_production_no_secret_lines():
    """Ensure KEY, SECRET, TOKEN lines are excluded from .env.production."""
    with open(ENV_PRODUCTION_FILE, "r") as f:
        lines = [line.rstrip('\n') for line in f.readlines() if line.strip()]
    excluded_keys = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "BILLING_API_TOKEN"]
    for line in lines:
        key = line.split("=", 1)[0] if "=" in line else line
        assert key not in excluded_keys, (
            f"Secret variable '{key}' should NOT appear in {ENV_PRODUCTION_FILE}.\n"
            f"Found line: {line}"
        )
    # Also check raw substrings to be thorough
    content = "\n".join(lines)
    for forbidden in excluded_keys:
        assert forbidden not in content, (
            f"'{forbidden}' should not appear in {ENV_PRODUCTION_FILE}.\n"
            f"File content:\n{content}"
        )


def test_env_production_no_blank_lines():
    with open(ENV_PRODUCTION_FILE, "r") as f:
        lines = f.readlines()
    blank_lines = [i + 1 for i, l in enumerate(lines) if not l.strip()]
    assert not blank_lines, (
        f"Blank lines found at line numbers {blank_lines} in {ENV_PRODUCTION_FILE}. "
        "No blank lines are allowed."
    )


def test_env_production_no_comment_lines():
    with open(ENV_PRODUCTION_FILE, "r") as f:
        lines = f.readlines()
    comment_lines = [l.rstrip('\n') for l in lines if l.strip().startswith('#')]
    assert not comment_lines, (
        f"Comment lines found in {ENV_PRODUCTION_FILE}: {comment_lines}. "
        "No comment lines are allowed."
    )


def test_env_production_no_export_prefix():
    with open(ENV_PRODUCTION_FILE, "r") as f:
        lines = f.readlines()
    export_lines = [l.rstrip('\n') for l in lines if l.strip().startswith('export ')]
    assert not export_lines, (
        f"Lines with 'export' prefix found in {ENV_PRODUCTION_FILE}: {export_lines}. "
        "No 'export' prefix is allowed."
    )


def test_env_production_no_quoted_values():
    """Values should not have quotes added around them."""
    with open(ENV_PRODUCTION_FILE, "r") as f:
        lines = [l.rstrip('\n') for l in f.readlines() if l.strip()]
    for line in lines:
        if "=" in line:
            value = line.split("=", 1)[1]
            assert not (value.startswith('"') or value.startswith("'")), (
                f"Value in line '{line}' appears to be quoted. "
                f"Values must not have quotes added in {ENV_PRODUCTION_FILE}."
            )


def test_env_production_correct_updated_values():
    """Verify the updated values appear correctly in .env.production."""
    with open(ENV_PRODUCTION_FILE, "r") as f:
        content = f.read()
    assert "COST_ALERT_THRESHOLD_USD=750" in content, (
        f"COST_ALERT_THRESHOLD_USD=750 not found in {ENV_PRODUCTION_FILE}.\n"
        f"File content:\n{content}"
    )
    assert "MONTHLY_BUDGET_USD=5000" in content, (
        f"MONTHLY_BUDGET_USD=5000 not found in {ENV_PRODUCTION_FILE}.\n"
        f"File content:\n{content}"
    )
    assert "ALERT_EMAIL=finops-team@company.com" in content, (
        f"ALERT_EMAIL=finops-team@company.com not found in {ENV_PRODUCTION_FILE}.\n"
        f"File content:\n{content}"
    )


def test_env_production_line_order():
    """Verify the lines appear in the correct order in .env.production."""
    with open(ENV_PRODUCTION_FILE, "r") as f:
        lines = [line.rstrip('\n') for line in f.readlines() if line.strip()]
    expected_lines = EXPECTED_PRODUCTION_CONTENT.strip().splitlines()
    assert lines == expected_lines, (
        f"Lines in {ENV_PRODUCTION_FILE} are not in the expected order.\n"
        f"Expected order:\n{expected_lines}\n\n"
        f"Got:\n{lines}"
    )