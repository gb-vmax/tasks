# test_final_state.py

import os
import pytest

ACCESS_LOG_PATH = "/home/user/investigation/access.log"
IP_REPORT_PATH = "/home/user/investigation/ip_report.txt"

EXPECTED_IP_REPORT = """192.168.1.101 5
203.0.113.4 4
203.0.113.42 3
10.0.0.1 2
"""

@pytest.mark.describe("Final OS state after Apache log investigation task")
def test_ip_report_exists():
    assert os.path.isfile(IP_REPORT_PATH), (
        f"Missing required report file: {IP_REPORT_PATH!r}. "
        "You must produce this report at the specified location."
    )

def test_ip_report_content_exact():
    """
    Ensure the IP report file exists and contains exactly the expected output,
    with correct sorting, format, and only valid IPv4s.
    """
    with open(IP_REPORT_PATH, encoding="utf-8") as f:
        content = f.read()
    # Normalize line endings and strip trailing whitespace
    actual_lines = [line.rstrip() for line in content.strip("\r\n").splitlines()]
    expected_lines = [line.rstrip() for line in EXPECTED_IP_REPORT.strip("\r\n").splitlines()]

    assert actual_lines == expected_lines, (
        f"The contents of {IP_REPORT_PATH!r} do not match the expected report.\n"
        "Expected:\n"
        f"{EXPECTED_IP_REPORT}"
        "\nFound:\n"
        f"{content}"
        "\nCheck that:\n"
        "- Only valid IPv4 addresses are included (no malformed entries).\n"
        "- The count for each IP is correct.\n"
        "- The sorting order is correct: descending by count, then lexicographically by IP.\n"
        "- There are no extra or missing lines, and no blank lines at start/end."
    )

def test_ip_report_no_extra_blank_lines():
    """
    Ensure there are no leading/trailing blank lines and no extra lines.
    """
    with open(IP_REPORT_PATH, encoding="utf-8") as f:
        lines = f.readlines()
    # Remove possible trailing newlines and count non-empty lines
    non_empty_lines = [line.rstrip("\r\n") for line in lines if line.strip("\r\n")]
    expected_lines = [line for line in EXPECTED_IP_REPORT.strip("\r\n").splitlines()]
    assert non_empty_lines == expected_lines, (
        f"{IP_REPORT_PATH!r} has extra blank lines or missing lines.\n"
        "Ensure the report contains exactly the expected lines, with no extra newlines at the beginning or end."
    )

def test_access_log_untouched():
    """
    Ensure the original access log still exists and was not modified.
    """
    assert os.path.isfile(ACCESS_LOG_PATH), (
        f"The original log file {ACCESS_LOG_PATH!r} is missing after the task. "
        "Do not remove or rename the log file."
    )
    # Optionally (robust): we could check the file content still matches the initial state,
    # but the main requirement is that it is not deleted/overwritten.

@pytest.mark.describe("No unexpected files created")
def test_no_unexpected_files_created(tmp_path_factory):
    """
    Ensure only the required report exists in the investigation directory (apart from the access log).
    """
    investigation_dir = "/home/user/investigation"
    allowed_files = {"access.log", "ip_report.txt"}
    try:
        listed = set(os.listdir(investigation_dir))
    except Exception as exc:
        pytest.skip(f"Cannot list {investigation_dir!r}: {exc}")
        return
    extra = listed - allowed_files
    assert not extra, (
        f"Unexpected files found in {investigation_dir!r}: {sorted(extra)}\n"
        "Only 'access.log' and 'ip_report.txt' should be present after the task."
    )