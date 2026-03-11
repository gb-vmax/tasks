# test_final_state.py

import os
import pytest

CONFIG_PATH = "/home/user/app/config.env"
AUDIT_LOG_PATH = "/home/user/security/audit.log"

EXPECTED_CONFIG_CONTENT = "APP_ENV=production\nDB_HOST=db.internal.example.com\nDB_PORT=5432\nAPI_KEY=sk-prod-9x2mK7vLqR4nYpW3hJtZ8cBdE1fG6aU0\nLOG_LEVEL=warn\nTIMEOUT=30"

EXPECTED_AUDIT_CONTENT = (
    "ROTATED DB_PASSWORD old=hunter2 new=xK9#mPqL2v by=security-engineer\n"
    "ROTATED S3_SECRET old=wJbN3rTy7z new=vH6kD1sA4f by=security-engineer\n"
    "ROTATED API_KEY old=sk-prod-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX new=sk-prod-9x2mK7vLqR4nYpW3hJtZ8cBdE1fG6aU0 by=security-engineer"
)

NEW_API_KEY = "sk-prod-9x2mK7vLqR4nYpW3hJtZ8cBdE1fG6aU0"
OLD_API_KEY = "sk-prod-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


# ── Directory checks ──────────────────────────────────────────────────────────

def test_app_directory_exists():
    assert os.path.isdir("/home/user/app"), (
        "Directory /home/user/app does not exist"
    )


def test_security_directory_exists():
    assert os.path.isdir("/home/user/security"), (
        "Directory /home/user/security does not exist"
    )


# ── Config file checks ────────────────────────────────────────────────────────

def test_config_file_exists():
    assert os.path.isfile(CONFIG_PATH), (
        f"Config file not found at {CONFIG_PATH}"
    )


def test_config_file_readable():
    assert os.access(CONFIG_PATH, os.R_OK), (
        f"Config file at {CONFIG_PATH} is not readable"
    )


def test_config_file_has_new_api_key():
    with open(CONFIG_PATH, "r") as f:
        lines = f.readlines()
    api_key_lines = [l for l in lines if l.startswith("API_KEY=")]
    assert len(api_key_lines) == 1, (
        f"Expected exactly one API_KEY line in {CONFIG_PATH}, found: {api_key_lines}"
    )
    assert api_key_lines[0].strip() == f"API_KEY={NEW_API_KEY}", (
        f"API_KEY line does not have the expected new value.\n"
        f"Expected: API_KEY={NEW_API_KEY}\n"
        f"Got:      {api_key_lines[0].strip()}"
    )


def test_config_file_does_not_contain_old_api_key():
    with open(CONFIG_PATH, "r") as f:
        content = f.read()
    assert OLD_API_KEY not in content, (
        f"Config file still contains the old API key '{OLD_API_KEY}'.\n"
        f"The old key must be replaced with the new one.\n"
        f"Content:\n{content}"
    )


def test_config_file_has_exactly_six_lines():
    with open(CONFIG_PATH, "r") as f:
        content = f.read()
    lines = content.strip().splitlines()
    assert len(lines) == 6, (
        f"Expected exactly 6 lines in {CONFIG_PATH}, got {len(lines)}.\n"
        f"Lines:\n" + "\n".join(repr(l) for l in lines)
    )


def test_config_file_exact_content():
    with open(CONFIG_PATH, "r") as f:
        content = f.read()
    stripped = content.strip()
    assert stripped == EXPECTED_CONFIG_CONTENT.strip(), (
        f"Config file content does not match expected.\n"
        f"Expected:\n{EXPECTED_CONFIG_CONTENT}\n\n"
        f"Got:\n{stripped}"
    )


def test_config_file_other_lines_unchanged():
    """All lines except API_KEY must remain exactly as they were."""
    expected_other_lines = [
        "APP_ENV=production",
        "DB_HOST=db.internal.example.com",
        "DB_PORT=5432",
        "LOG_LEVEL=warn",
        "TIMEOUT=30",
    ]
    with open(CONFIG_PATH, "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines()]
    non_api_lines = [l for l in lines if not l.startswith("API_KEY=") and l != ""]
    for expected in expected_other_lines:
        assert expected in non_api_lines, (
            f"Expected line '{expected}' not found (or was altered) in {CONFIG_PATH}.\n"
            f"Non-API_KEY lines present: {non_api_lines}"
        )


def test_config_file_no_trailing_blank_line():
    with open(CONFIG_PATH, "r") as f:
        content = f.read()
    # The file should not end with a blank line beyond the final content line
    assert not content.endswith("\n\n"), (
        f"Config file ends with a blank line. "
        f"Last 20 chars (repr): {repr(content[-20:])}"
    )


# ── Audit log checks ──────────────────────────────────────────────────────────

def test_audit_log_exists():
    assert os.path.isfile(AUDIT_LOG_PATH), (
        f"Audit log not found at {AUDIT_LOG_PATH}"
    )


def test_audit_log_readable():
    assert os.access(AUDIT_LOG_PATH, os.R_OK), (
        f"Audit log at {AUDIT_LOG_PATH} is not readable"
    )


def test_audit_log_has_exactly_three_lines():
    with open(AUDIT_LOG_PATH, "r") as f:
        content = f.read()
    lines = content.strip().splitlines()
    assert len(lines) == 3, (
        f"Expected exactly 3 lines in {AUDIT_LOG_PATH}, got {len(lines)}.\n"
        f"Lines:\n" + "\n".join(repr(l) for l in lines)
    )


def test_audit_log_contains_rotation_record():
    expected_line = (
        f"ROTATED API_KEY old={OLD_API_KEY} new={NEW_API_KEY} by=security-engineer"
    )
    with open(AUDIT_LOG_PATH, "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines()]
    assert expected_line in lines, (
        f"Expected rotation record not found in {AUDIT_LOG_PATH}.\n"
        f"Expected line:\n  {expected_line}\n"
        f"Actual lines:\n" + "\n".join(f"  {repr(l)}" for l in lines)
    )


def test_audit_log_rotation_record_is_last_line():
    expected_line = (
        f"ROTATED API_KEY old={OLD_API_KEY} new={NEW_API_KEY} by=security-engineer"
    )
    with open(AUDIT_LOG_PATH, "r") as f:
        content = f.read()
    lines = content.strip().splitlines()
    assert lines[-1] == expected_line, (
        f"The rotation record must be the LAST line in {AUDIT_LOG_PATH}.\n"
        f"Expected last line:\n  {expected_line}\n"
        f"Actual last line:\n  {repr(lines[-1])}"
    )


def test_audit_log_preserves_existing_lines():
    expected_existing = [
        "ROTATED DB_PASSWORD old=hunter2 new=xK9#mPqL2v by=security-engineer",
        "ROTATED S3_SECRET old=wJbN3rTy7z new=vH6kD1sA4f by=security-engineer",
    ]
    with open(AUDIT_LOG_PATH, "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines()]
    for expected in expected_existing:
        assert expected in lines, (
            f"Pre-existing audit log line was removed or altered.\n"
            f"Missing line: {expected}\n"
            f"Actual lines:\n" + "\n".join(f"  {repr(l)}" for l in lines)
        )


def test_audit_log_exact_content():
    with open(AUDIT_LOG_PATH, "r") as f:
        content = f.read()
    stripped = content.strip()
    assert stripped == EXPECTED_AUDIT_CONTENT.strip(), (
        f"Audit log content does not match expected.\n"
        f"Expected:\n{EXPECTED_AUDIT_CONTENT}\n\n"
        f"Got:\n{stripped}"
    )


def test_audit_log_no_trailing_blank_line():
    with open(AUDIT_LOG_PATH, "r") as f:
        content = f.read()
    assert not content.endswith("\n\n"), (
        f"Audit log ends with a blank line. "
        f"Last 20 chars (repr): {repr(content[-20:])}"
    )


def test_audit_log_rotation_record_contains_old_key():
    with open(AUDIT_LOG_PATH, "r") as f:
        content = f.read()
    assert f"old={OLD_API_KEY}" in content, (
        f"Audit log rotation record must contain the original key as old=.\n"
        f"Expected to find: old={OLD_API_KEY}\n"
        f"Audit log content:\n{content}"
    )


def test_audit_log_rotation_record_contains_new_key():
    with open(AUDIT_LOG_PATH, "r") as f:
        content = f.read()
    assert f"new={NEW_API_KEY}" in content, (
        f"Audit log rotation record must contain the new key as new=.\n"
        f"Expected to find: new={NEW_API_KEY}\n"
        f"Audit log content:\n{content}"
    )


def test_audit_log_rotation_record_contains_by_field():
    with open(AUDIT_LOG_PATH, "r") as f:
        content = f.read()
    assert "by=security-engineer" in content, (
        f"Audit log rotation record must contain 'by=security-engineer'.\n"
        f"Audit log content:\n{content}"
    )