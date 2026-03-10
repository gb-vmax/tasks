# test_final_state.py

import os
import subprocess
import pytest

REPORT_PATH = "/home/user/analysis/report.txt"
SCRIPT_PATH = "/home/user/analysis/scan_log.py"
ANALYSIS_DIR = "/home/user/analysis"

EXPECTED_IPS = ["10.0.0.7", "192.168.1.1"]
EXPECTED_COUNT = 2


def test_analysis_directory_exists():
    assert os.path.isdir(ANALYSIS_DIR), (
        f"Directory '{ANALYSIS_DIR}' does not exist. "
        "The analysis directory must exist."
    )


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file '{REPORT_PATH}' does not exist. "
        "The task requires creating this file with the summary."
    )


def test_report_file_not_empty():
    assert os.path.getsize(REPORT_PATH) > 0, (
        f"Report file '{REPORT_PATH}' is empty. "
        "It must contain the summary of suspicious IPs."
    )


def test_report_first_line_format():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, (
        f"Report file '{REPORT_PATH}' has no lines. "
        "Expected at least the 'Suspicious IPs found: <count>' header line."
    )

    first_line = lines[0]
    assert first_line.startswith("Suspicious IPs found: "), (
        f"First line of '{REPORT_PATH}' does not start with 'Suspicious IPs found: '.\n"
        f"Actual first line: '{first_line}'"
    )

    count_str = first_line[len("Suspicious IPs found: "):]
    assert count_str.isdigit(), (
        f"The count in the first line is not an integer. "
        f"Got: '{count_str}' from first line: '{first_line}'"
    )


def test_report_ip_count_correct():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    first_line = lines[0]
    count_str = first_line[len("Suspicious IPs found: "):]
    count = int(count_str)

    assert count == EXPECTED_COUNT, (
        f"Report says 'Suspicious IPs found: {count}', but expected {EXPECTED_COUNT}. "
        f"Full report content:\n" + open(REPORT_PATH).read()
    )


def test_report_has_correct_number_of_ip_lines():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    # First line is the header; remaining lines should be IPs
    ip_lines = lines[1:]

    # Strip any trailing empty lines
    while ip_lines and ip_lines[-1].strip() == "":
        ip_lines.pop()

    assert len(ip_lines) == EXPECTED_COUNT, (
        f"Expected {EXPECTED_COUNT} IP lines after the header, "
        f"but found {len(ip_lines)}.\n"
        f"IP lines found: {ip_lines}\n"
        f"Full report content:\n" + open(REPORT_PATH).read()
    )


def test_report_contains_expected_ips():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    ip_lines = [l.strip() for l in lines[1:] if l.strip()]

    for ip in EXPECTED_IPS:
        assert ip in ip_lines, (
            f"Expected IP '{ip}' not found in report IP lines.\n"
            f"IP lines found: {ip_lines}\n"
            f"Full report content:\n" + open(REPORT_PATH).read()
        )


def test_report_ips_sorted_lexicographically():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    ip_lines = [l.strip() for l in lines[1:] if l.strip()]

    sorted_ips = sorted(ip_lines)
    assert ip_lines == sorted_ips, (
        f"IPs in the report are not sorted in ascending lexicographic order.\n"
        f"Found order: {ip_lines}\n"
        f"Expected order: {sorted_ips}\n"
        f"Full report content:\n" + open(REPORT_PATH).read()
    )


def test_report_no_duplicate_ips():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    ip_lines = [l.strip() for l in lines[1:] if l.strip()]

    unique_ips = list(dict.fromkeys(ip_lines))
    assert ip_lines == unique_ips, (
        f"Report contains duplicate IP addresses.\n"
        f"IP lines found: {ip_lines}\n"
        f"Full report content:\n" + open(REPORT_PATH).read()
    )


def test_report_exact_content():
    expected_content = "Suspicious IPs found: 2\n10.0.0.7\n192.168.1.1\n"
    # Also accept without trailing newline
    expected_content_no_newline = "Suspicious IPs found: 2\n10.0.0.7\n192.168.1.1"

    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    # Normalize: strip trailing newline for comparison
    actual_stripped = actual_content.rstrip("\n")
    expected_stripped = expected_content_no_newline

    assert actual_stripped == expected_stripped, (
        f"Report file content does not match expected.\n"
        f"Expected (stripped):\n{repr(expected_stripped)}\n"
        f"Actual (stripped):\n{repr(actual_stripped)}\n"
        f"Full actual content:\n{repr(actual_content)}"
    )


def test_report_no_extra_blank_lines():
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines()

    # Check there are no blank lines within the content
    blank_lines = [i for i, line in enumerate(lines) if line.strip() == ""]
    assert len(blank_lines) == 0, (
        f"Report file contains blank lines at positions (0-indexed): {blank_lines}.\n"
        f"Full report content:\n{repr(content)}"
    )


def test_report_no_trailing_spaces():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    lines_with_trailing_spaces = [
        (i, repr(line)) for i, line in enumerate(lines) if line != line.rstrip()
    ]
    assert len(lines_with_trailing_spaces) == 0, (
        f"Report file has lines with trailing spaces:\n"
        + "\n".join(f"  Line {i}: {l}" for i, l in lines_with_trailing_spaces)
    )


def test_script_was_not_modified():
    """Verify the script still contains expected original content (not modified)."""
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()

    assert "SUSPICIOUS" in content, (
        f"Script '{SCRIPT_PATH}' no longer contains 'SUSPICIOUS' — it may have been modified."
    )
    assert "/home/user/analysis/access.log" in content, (
        f"Script '{SCRIPT_PATH}' no longer references the log path — it may have been modified."
    )
    assert "count >= 1" in content, (
        f"Script '{SCRIPT_PATH}' no longer contains 'count >= 1' threshold — it may have been modified."
    )


def test_script_still_produces_correct_output():
    """Run the script and verify it still produces the expected SUSPICIOUS lines."""
    result = subprocess.run(
        ["python3", SCRIPT_PATH],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Script '{SCRIPT_PATH}' failed to run.\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )

    lines = result.stdout.splitlines()
    suspicious_lines = [l for l in lines if l.startswith("SUSPICIOUS ")]

    assert len(suspicious_lines) == EXPECTED_COUNT, (
        f"Expected {EXPECTED_COUNT} SUSPICIOUS lines from script, "
        f"got {len(suspicious_lines)}.\n"
        f"Full stdout:\n{result.stdout}"
    )

    ips_from_script = set()
    for line in suspicious_lines:
        parts = line.split()
        assert len(parts) >= 6, (
            f"SUSPICIOUS line has unexpected format: '{line}'\n"
            f"Expected: SUSPICIOUS <ip> <count> requests to <path>"
        )
        ips_from_script.add(parts[1])

    for ip in EXPECTED_IPS:
        assert ip in ips_from_script, (
            f"Expected IP '{ip}' not found in script SUSPICIOUS output.\n"
            f"IPs found: {ips_from_script}\n"
            f"Full stdout:\n{result.stdout}"
        )