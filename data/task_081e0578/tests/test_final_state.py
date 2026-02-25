# test_final_state.py

import os
import pytest

NETWORK_DIAG_LOG_PATH = "/home/user/appconfig/network_diagnostics.log"

EXPECTED_LOG_CONTENT = (
    "hostname = app-host\n"
    "port = 443\n"
    "ssl_enabled = true\n"
    "proxy = enabled\n"
    "proxy_port = 3128\n"
    "Total network parameters: 5\n"
)

def test_network_diagnostics_log_exists():
    assert os.path.isfile(NETWORK_DIAG_LOG_PATH), (
        f"Expected log file does not exist: {NETWORK_DIAG_LOG_PATH}"
    )

def test_network_diagnostics_log_content_and_format():
    """
    Check that the log file contains exactly the expected lines in order,
    with correct formatting, no extra or missing lines, and correct summary.
    """
    with open(NETWORK_DIAG_LOG_PATH, "r", encoding="utf-8") as f:
        actual = f.read()
    # Normalize line endings to Unix
    actual_unix = actual.replace('\r\n', '\n').replace('\r', '\n')

    # Compare full file contents
    if actual_unix != EXPECTED_LOG_CONTENT:
        actual_lines = actual_unix.splitlines()
        expected_lines = EXPECTED_LOG_CONTENT.splitlines()
        diff_lines = [
            f"- {e}" if i >= len(actual_lines) else f"  {e}" if e == actual_lines[i] else f"! expected: {e} | actual: {actual_lines[i]}"
            for i, e in enumerate(expected_lines)
        ]
        extra_actual = actual_lines[len(expected_lines):]
        if extra_actual:
            diff_lines += [f"! unexpected extra line: {line}" for line in extra_actual]
        pytest.fail(
            f"{NETWORK_DIAG_LOG_PATH} content does not match expected result.\n"
            f"--- Actual content ---\n{actual_unix}\n"
            f"--- Expected content ---\n{EXPECTED_LOG_CONTENT}\n"
            f"--- Differences ---\n" +
            "\n".join(diff_lines)
        )

def test_network_diagnostics_log_no_blank_lines_or_comments():
    """
    Ensure there are no blank lines or comments in the log file.
    """
    with open(NETWORK_DIAG_LOG_PATH, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            stripped = line.strip()
            assert stripped != "", (
                f"Blank line found in {NETWORK_DIAG_LOG_PATH} at line {lineno}."
            )
            assert not stripped.startswith("#"), (
                f"Comment line found in {NETWORK_DIAG_LOG_PATH} at line {lineno}."
            )
            assert not (stripped.startswith("[") and stripped.endswith("]")), (
                f"Section header found in {NETWORK_DIAG_LOG_PATH} at line {lineno}."
            )

def test_network_diagnostics_log_contains_only_network_keys():
    """
    Ensure that only the expected network keys are present in the log file,
    and no keys from other sections are included.
    """
    expected_keys = [
        "hostname",
        "port",
        "ssl_enabled",
        "proxy",
        "proxy_port",
    ]
    found_keys = []
    with open(NETWORK_DIAG_LOG_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\r\n")
            if line.startswith("Total network parameters:"):
                continue
            if "=" in line:
                key = line.split("=", 1)[0].strip()
                found_keys.append(key)
    missing = [k for k in expected_keys if k not in found_keys]
    unexpected = [k for k in found_keys if k not in expected_keys]
    assert not missing, (
        f"The following expected keys are missing from the log: {missing}"
    )
    assert not unexpected, (
        f"The following unexpected keys are present in the log: {unexpected}"
    )
    # Check for keys from [user] or [database]
    forbidden_keys = {"username", "email", "db_name", "db_port", "timeout"}
    forbidden_found = forbidden_keys & set(found_keys)
    assert not forbidden_found, (
        f"Keys from non-network sections found in log: {forbidden_found}"
    )

def test_network_diagnostics_log_summary_line_correct():
    """
    Ensure that the summary line is present, exactly formatted, and correct.
    """
    with open(NETWORK_DIAG_LOG_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\r\n') for line in f]
    assert lines, f"{NETWORK_DIAG_LOG_PATH} is empty."
    summary = lines[-1]
    assert summary == "Total network parameters: 5", (
        f"Summary line incorrect or missing in {NETWORK_DIAG_LOG_PATH}.\n"
        f"Expected: 'Total network parameters: 5'\n"
        f"Actual:   '{summary}'"
    )