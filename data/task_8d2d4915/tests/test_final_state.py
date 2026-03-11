# test_final_state.py

import os
import pytest

COMPLIANT_FILE = "/home/user/services/api-gateway/config.compliant.env"
AUDIT_LOG = "/home/user/services/api-gateway/audit.log"
SOURCE_FILE = "/home/user/services/api-gateway/config.env"

EXPECTED_COMPLIANT_CONTENT = """\
# compliant-env-v1 policy=strict

API_KEY=public-facing-key-ok
APP_NAME=api-gateway
APP_PORT=8080
DB_HOST=postgres.internal
DB_PASSWORD=***REDACTED***
DB_PORT=5432
DB_USER=gateway_user
JWT_SECRET=***REDACTED***
LOG_LEVEL=info
MAX_CONNECTIONS=100
STRIPE_TOKEN=***REDACTED***
"""

EXPECTED_AUDIT_CONTENT = """\
AUDIT: config.env policy enforcement
banned_removed: 3
secrets_redacted: 3
lines_written: 11
"""


# ── source file still intact ──────────────────────────────────────────────────

def test_source_file_still_exists():
    assert os.path.isfile(SOURCE_FILE), (
        f"Source file '{SOURCE_FILE}' no longer exists. "
        "It must not be removed or renamed."
    )


# ── compliant file existence & permissions ────────────────────────────────────

def test_compliant_file_exists():
    assert os.path.isfile(COMPLIANT_FILE), (
        f"Compliant output file '{COMPLIANT_FILE}' does not exist. "
        "The task requires creating this file."
    )


def test_compliant_file_is_readable():
    assert os.access(COMPLIANT_FILE, os.R_OK), (
        f"Compliant file '{COMPLIANT_FILE}' exists but is not readable."
    )


# ── compliant file exact content ──────────────────────────────────────────────

def test_compliant_file_exact_content():
    with open(COMPLIANT_FILE, "r") as f:
        content = f.read()
    assert content == EXPECTED_COMPLIANT_CONTENT, (
        f"'{COMPLIANT_FILE}' does not match the expected content.\n"
        f"Expected:\n{EXPECTED_COMPLIANT_CONTENT!r}\n\n"
        f"Got:\n{content!r}"
    )


def test_compliant_file_ends_with_newline():
    with open(COMPLIANT_FILE, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        f"'{COMPLIANT_FILE}' must end with a newline character, but it does not."
    )


def test_compliant_file_first_line_is_header():
    with open(COMPLIANT_FILE, "r") as f:
        first_line = f.readline()
    assert first_line == "# compliant-env-v1 policy=strict\n", (
        f"First line of '{COMPLIANT_FILE}' must be exactly "
        f"'# compliant-env-v1 policy=strict\\n', got {first_line!r}"
    )


def test_compliant_file_second_line_is_blank():
    with open(COMPLIANT_FILE, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 2, (
        f"'{COMPLIANT_FILE}' has fewer than 2 lines."
    )
    assert lines[1] == "\n", (
        f"Second line of '{COMPLIANT_FILE}' must be a blank line, got {lines[1]!r}"
    )


def test_compliant_file_no_extra_blank_lines_between_entries():
    with open(COMPLIANT_FILE, "r") as f:
        lines = f.readlines()
    # After the header (line 0) and blank line (line 1), no blank lines should appear
    data_section = lines[2:]
    for i, line in enumerate(data_section):
        assert line.strip() != "", (
            f"Unexpected blank line at position {i + 3} (1-based) in '{COMPLIANT_FILE}'. "
            "No extra blank lines are allowed between key=value entries."
        )


def test_compliant_file_no_trailing_spaces():
    with open(COMPLIANT_FILE, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} of '{COMPLIANT_FILE}' has trailing whitespace: {line!r}"
        )


def test_compliant_file_header_no_extra_lines():
    """Only one blank line separates the header from the first key=value line."""
    with open(COMPLIANT_FILE, "r") as f:
        lines = f.readlines()
    # line index 0 = header, index 1 = blank, index 2 = first kv line
    assert len(lines) >= 3, (
        f"'{COMPLIANT_FILE}' must have at least 3 lines (header, blank, first entry)."
    )
    assert lines[2].strip() != "", (
        f"There must be exactly one blank line after the header in '{COMPLIANT_FILE}', "
        f"but line 3 is also blank: {lines[2]!r}"
    )


# ── compliant file key=value correctness ─────────────────────────────────────

def _get_kv_lines(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    return [ln.rstrip("\n") for ln in lines[2:] if ln.strip()]


def test_compliant_file_kv_line_count():
    kv_lines = _get_kv_lines(COMPLIANT_FILE)
    assert len(kv_lines) == 11, (
        f"Expected 11 key=value lines in '{COMPLIANT_FILE}', found {len(kv_lines)}.\n"
        f"Lines: {kv_lines}"
    )


def test_compliant_file_banned_variables_absent():
    kv_lines = _get_kv_lines(COMPLIANT_FILE)
    keys = [ln.split("=", 1)[0] for ln in kv_lines if "=" in ln]
    banned = {"DEBUG", "DEV_MODE", "LEGACY_AUTH_TOKEN"}
    found_banned = banned.intersection(keys)
    assert not found_banned, (
        f"Banned variable(s) {found_banned} found in '{COMPLIANT_FILE}'. "
        "They must be removed."
    )


def test_compliant_file_secrets_redacted():
    kv_lines = _get_kv_lines(COMPLIANT_FILE)
    secret_substrings = ("SECRET", "PASSWORD", "TOKEN")
    for line in kv_lines:
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        if any(sub in key for sub in secret_substrings):
            assert value == "***REDACTED***", (
                f"Key '{key}' in '{COMPLIANT_FILE}' contains a secret substring "
                f"but value is {value!r} instead of '***REDACTED***'."
            )


def test_compliant_file_non_secret_values_unchanged():
    expected_non_secret = {
        "API_KEY": "public-facing-key-ok",
        "APP_NAME": "api-gateway",
        "APP_PORT": "8080",
        "DB_HOST": "postgres.internal",
        "DB_PORT": "5432",
        "DB_USER": "gateway_user",
        "LOG_LEVEL": "info",
        "MAX_CONNECTIONS": "100",
    }
    kv_lines = _get_kv_lines(COMPLIANT_FILE)
    kv_dict = {}
    for line in kv_lines:
        if "=" in line:
            k, v = line.split("=", 1)
            kv_dict[k] = v

    for key, expected_value in expected_non_secret.items():
        assert key in kv_dict, (
            f"Expected key '{key}' not found in '{COMPLIANT_FILE}'."
        )
        assert kv_dict[key] == expected_value, (
            f"Key '{key}' in '{COMPLIANT_FILE}': expected value {expected_value!r}, "
            f"got {kv_dict[key]!r}."
        )


def test_compliant_file_sorted_alphabetically():
    kv_lines = _get_kv_lines(COMPLIANT_FILE)
    keys = [ln.split("=", 1)[0] for ln in kv_lines if "=" in ln]
    assert keys == sorted(keys), (
        f"Key=value lines in '{COMPLIANT_FILE}' are not sorted alphabetically.\n"
        f"Current order: {keys}\n"
        f"Expected order: {sorted(keys)}"
    )


def test_compliant_file_expected_keys_present():
    expected_keys = [
        "API_KEY", "APP_NAME", "APP_PORT", "DB_HOST", "DB_PASSWORD",
        "DB_PORT", "DB_USER", "JWT_SECRET", "LOG_LEVEL", "MAX_CONNECTIONS",
        "STRIPE_TOKEN",
    ]
    kv_lines = _get_kv_lines(COMPLIANT_FILE)
    keys = [ln.split("=", 1)[0] for ln in kv_lines if "=" in ln]
    for key in expected_keys:
        assert key in keys, (
            f"Expected key '{key}' is missing from '{COMPLIANT_FILE}'."
        )


# ── audit log existence & permissions ─────────────────────────────────────────

def test_audit_log_exists():
    assert os.path.isfile(AUDIT_LOG), (
        f"Audit log '{AUDIT_LOG}' does not exist. "
        "The task requires creating this file."
    )


def test_audit_log_is_readable():
    assert os.access(AUDIT_LOG, os.R_OK), (
        f"Audit log '{AUDIT_LOG}' exists but is not readable."
    )


# ── audit log exact content ───────────────────────────────────────────────────

def test_audit_log_exact_content():
    with open(AUDIT_LOG, "r") as f:
        content = f.read()
    assert content == EXPECTED_AUDIT_CONTENT, (
        f"'{AUDIT_LOG}' does not match the expected content.\n"
        f"Expected:\n{EXPECTED_AUDIT_CONTENT!r}\n\n"
        f"Got:\n{content!r}"
    )


def test_audit_log_ends_with_newline():
    with open(AUDIT_LOG, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        f"'{AUDIT_LOG}' must end with a newline character, but it does not."
    )


def test_audit_log_no_extra_lines():
    with open(AUDIT_LOG, "r") as f:
        lines = f.readlines()
    assert len(lines) == 4, (
        f"'{AUDIT_LOG}' must have exactly 4 lines, found {len(lines)}.\n"
        f"Lines: {lines!r}"
    )


def test_audit_log_first_line():
    with open(AUDIT_LOG, "r") as f:
        first_line = f.readline()
    assert first_line == "AUDIT: config.env policy enforcement\n", (
        f"First line of '{AUDIT_LOG}' is incorrect.\n"
        f"Expected: 'AUDIT: config.env policy enforcement\\n'\n"
        f"Got: {first_line!r}"
    )


def test_audit_log_banned_removed_count():
    with open(AUDIT_LOG, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 2, f"'{AUDIT_LOG}' has fewer than 2 lines."
    line = lines[1].rstrip("\n")
    assert line == "banned_removed: 3", (
        f"Second line of '{AUDIT_LOG}' must be 'banned_removed: 3', got {line!r}"
    )


def test_audit_log_secrets_redacted_count():
    with open(AUDIT_LOG, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 3, f"'{AUDIT_LOG}' has fewer than 3 lines."
    line = lines[2].rstrip("\n")
    assert line == "secrets_redacted: 3", (
        f"Third line of '{AUDIT_LOG}' must be 'secrets_redacted: 3', got {line!r}"
    )


def test_audit_log_lines_written_count():
    with open(AUDIT_LOG, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 4, f"'{AUDIT_LOG}' has fewer than 4 lines."
    line = lines[3].rstrip("\n")
    assert line == "lines_written: 11", (
        f"Fourth line of '{AUDIT_LOG}' must be 'lines_written: 11', got {line!r}"
    )


# ── cross-check: lines_written matches actual compliant file ──────────────────

def test_audit_lines_written_matches_compliant_file():
    kv_lines = _get_kv_lines(COMPLIANT_FILE)
    actual_count = len(kv_lines)
    with open(AUDIT_LOG, "r") as f:
        audit_lines = f.readlines()
    # Parse lines_written from audit log
    lines_written_line = audit_lines[3].rstrip("\n") if len(audit_lines) >= 4 else ""
    try:
        reported = int(lines_written_line.split(": ")[1])
    except (IndexError, ValueError):
        pytest.fail(
            f"Could not parse lines_written from audit log line: {lines_written_line!r}"
        )
    assert reported == actual_count, (
        f"Audit log reports lines_written={reported}, but '{COMPLIANT_FILE}' "
        f"actually contains {actual_count} key=value lines."
    )