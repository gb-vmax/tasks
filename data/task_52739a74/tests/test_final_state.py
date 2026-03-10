# test_final_state.py

import os
import pytest

BASE_DIR = "/home/user/api_diagnostics"
REPORT_FILE = os.path.join(BASE_DIR, "diagnostic_report.txt")

EXPECTED_REPORT = """\
=== API DIAGNOSTIC REPORT ===

--- AUTH EVENTS ---
Total events: 15
Successful: 7
Failed: 8
Top failing user: bob (4 failures)

--- LATENCY (ms) ---
Min: 45
Max: 1100
Mean: 428.7
Slowest endpoint: /api/products (avg 975.0ms)
HTTP 200 count: 12

--- ERROR COUNTS ---
Total errors: 84
Most errors endpoint: /api/orders (34 errors)
Worst minute: 2024-05-01T10:02Z (14 errors)

--- SYSTEM METRICS ---
Peak CPU: 91.3%
Peak Memory: 76.3%
High CPU samples (>80%): 4"""


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file does not exist at {REPORT_FILE}. "
        "The student must create this file as part of the task."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_FILE, os.R_OK), (
        f"Report file {REPORT_FILE} exists but is not readable."
    )


def test_report_exact_content():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()

    # Strip trailing newline for comparison (allow one trailing newline)
    actual_stripped = actual_content.rstrip("\n")
    expected_stripped = EXPECTED_REPORT.rstrip("\n")

    assert actual_stripped == expected_stripped, (
        f"Report content does not match expected.\n\n"
        f"EXPECTED:\n{expected_stripped!r}\n\n"
        f"ACTUAL:\n{actual_stripped!r}"
    )


def test_report_line_by_line():
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()

    actual_lines = actual_content.rstrip("\n").splitlines()
    expected_lines = EXPECTED_REPORT.rstrip("\n").splitlines()

    assert len(actual_lines) == len(expected_lines), (
        f"Report has {len(actual_lines)} lines, expected {len(expected_lines)} lines.\n"
        f"Actual lines:\n" + "\n".join(repr(l) for l in actual_lines)
    )

    for i, (actual_line, expected_line) in enumerate(zip(actual_lines, expected_lines), start=1):
        assert actual_line == expected_line, (
            f"Line {i} mismatch in diagnostic_report.txt:\n"
            f"  Expected: {expected_line!r}\n"
            f"  Got:      {actual_line!r}"
        )


def test_report_header():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()
    assert lines[0] == "=== API DIAGNOSTIC REPORT ===", (
        f"First line should be '=== API DIAGNOSTIC REPORT ===' but got: {lines[0]!r}"
    )


def test_report_auth_section():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    assert "--- AUTH EVENTS ---" in content, "Missing '--- AUTH EVENTS ---' section header"
    assert "Total events: 15" in content, (
        "Auth section: 'Total events: 15' not found. "
        "Expected 15 total authentication events."
    )
    assert "Successful: 7" in content, (
        "Auth section: 'Successful: 7' not found. "
        "Expected 7 successful authentications."
    )
    assert "Failed: 8" in content, (
        "Auth section: 'Failed: 8' not found. "
        "Expected 8 failed authentications."
    )
    assert "Top failing user: bob (4 failures)" in content, (
        "Auth section: 'Top failing user: bob (4 failures)' not found. "
        "Bob had 4 FAIL events, the most of any user."
    )


def test_report_latency_section():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    assert "--- LATENCY (ms) ---" in content, "Missing '--- LATENCY (ms) ---' section header"
    assert "Min: 45" in content, (
        "Latency section: 'Min: 45' not found. "
        "Minimum latency across all requests should be 45ms."
    )
    assert "Max: 1100" in content, (
        "Latency section: 'Max: 1100' not found. "
        "Maximum latency across all requests should be 1100ms."
    )
    assert "Mean: 428.7" in content, (
        "Latency section: 'Mean: 428.7' not found. "
        "Mean latency = 6430/15 = 428.666... rounded to 428.7."
    )
    assert "Slowest endpoint: /api/products (avg 975.0ms)" in content, (
        "Latency section: 'Slowest endpoint: /api/products (avg 975.0ms)' not found. "
        "/api/products has mean latency of (870+940+1100+990)/4 = 975.0ms."
    )
    assert "HTTP 200 count: 12" in content, (
        "Latency section: 'HTTP 200 count: 12' not found. "
        "12 requests had status_code 200."
    )


def test_report_error_counts_section():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    assert "--- ERROR COUNTS ---" in content, "Missing '--- ERROR COUNTS ---' section header"
    assert "Total errors: 84" in content, (
        "Error counts section: 'Total errors: 84' not found. "
        "Sum of all error counts = 84."
    )
    assert "Most errors endpoint: /api/orders (34 errors)" in content, (
        "Error counts section: 'Most errors endpoint: /api/orders (34 errors)' not found. "
        "/api/orders accumulated 7+9+14+4=34 errors total."
    )
    assert "Worst minute: 2024-05-01T10:02Z (14 errors)" in content, (
        "Error counts section: 'Worst minute: 2024-05-01T10:02Z (14 errors)' not found. "
        "The highest single error count was 14 at 2024-05-01T10:02Z."
    )


def test_report_system_metrics_section():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    assert "--- SYSTEM METRICS ---" in content, "Missing '--- SYSTEM METRICS ---' section header"
    assert "Peak CPU: 91.3%" in content, (
        "System metrics section: 'Peak CPU: 91.3%' not found. "
        "The highest CPU percentage observed was 91.3%."
    )
    assert "Peak Memory: 76.3%" in content, (
        "System metrics section: 'Peak Memory: 76.3%' not found. "
        "The highest memory percentage observed was 76.3%."
    )
    assert "High CPU samples (>80%): 4" in content, (
        "System metrics section: 'High CPU samples (>80%): 4' not found. "
        "4 samples had cpu_pct > 80.0 (88.5, 91.3, 84.1, 81.9)."
    )


def test_report_no_trailing_spaces():
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} has trailing whitespace: {stripped!r}"
        )


def test_report_section_order():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    header_pos = content.find("=== API DIAGNOSTIC REPORT ===")
    auth_pos = content.find("--- AUTH EVENTS ---")
    latency_pos = content.find("--- LATENCY (ms) ---")
    error_pos = content.find("--- ERROR COUNTS ---")
    metrics_pos = content.find("--- SYSTEM METRICS ---")

    assert header_pos != -1, "Missing '=== API DIAGNOSTIC REPORT ===' header"
    assert auth_pos != -1, "Missing '--- AUTH EVENTS ---' section"
    assert latency_pos != -1, "Missing '--- LATENCY (ms) ---' section"
    assert error_pos != -1, "Missing '--- ERROR COUNTS ---' section"
    assert metrics_pos != -1, "Missing '--- SYSTEM METRICS ---' section"

    assert header_pos < auth_pos, "Header must come before AUTH EVENTS section"
    assert auth_pos < latency_pos, "AUTH EVENTS section must come before LATENCY section"
    assert latency_pos < error_pos, "LATENCY section must come before ERROR COUNTS section"
    assert error_pos < metrics_pos, "ERROR COUNTS section must come before SYSTEM METRICS section"


def test_source_files_unchanged():
    """Verify the original source files were not modified."""
    auth_log = os.path.join(BASE_DIR, "auth_events.log")
    with open(auth_log, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    assert len(lines) == 15, (
        f"auth_events.log was modified: expected 15 lines, got {len(lines)}"
    )

    latency_csv = os.path.join(BASE_DIR, "latency_samples.csv")
    with open(latency_csv, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    assert len(lines) == 16, (
        f"latency_samples.csv was modified: expected 16 lines, got {len(lines)}"
    )

    error_tsv = os.path.join(BASE_DIR, "error_counts.tsv")
    with open(error_tsv, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    assert len(lines) == 12, (
        f"error_counts.tsv was modified: expected 12 lines, got {len(lines)}"
    )

    metrics_log = os.path.join(BASE_DIR, "system_metrics.log")
    with open(metrics_log, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    assert len(lines) == 10, (
        f"system_metrics.log was modified: expected 10 lines, got {len(lines)}"
    )