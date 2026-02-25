# test_final_state.py

import os
import re
import pytest

LEGACY_APP_DIR = "/home/user/legacy_app"
COLLECT_INFO = "/home/user/legacy_app/collect_info.py"
DIAGNOSTICS_LOG = "/home/user/legacy_app/diagnostics.log"

def test_diagnostics_log_exists_and_is_file():
    """Check that diagnostics.log exists and is a regular file."""
    assert os.path.exists(DIAGNOSTICS_LOG), (
        f"Expected diagnostics log at {DIAGNOSTICS_LOG}, but it does not exist."
    )
    assert os.path.isfile(DIAGNOSTICS_LOG), (
        f"{DIAGNOSTICS_LOG} exists but is not a file."
    )

def test_diagnostics_log_not_empty():
    """Check that diagnostics.log is not empty."""
    size = os.stat(DIAGNOSTICS_LOG).st_size
    assert size > 0, (
        f"{DIAGNOSTICS_LOG} is empty after collect_info.py was run."
    )

def test_diagnostics_log_first_line_format():
    """
    The first line must start with 'System Diagnostics Report -'
    followed by a timestamp in YYYY-MM-DD HH:MM:SS format.
    """
    with open(DIAGNOSTICS_LOG, "r") as f:
        lines = f.readlines()
    assert lines, "diagnostics.log is empty, expected at least one line."
    first_line = lines[0].rstrip("\n")
    m = re.match(r"^System Diagnostics Report - (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})$", first_line)
    assert m is not None, (
        f"The first line of diagnostics.log is not in the expected format.\n"
        f"Expected: System Diagnostics Report - YYYY-MM-DD HH:MM:SS\n"
        f"Found: {first_line}"
    )

def test_diagnostics_log_next_three_lines_format():
    """
    The next three lines must each start with 'Hostname:', 'OS Version:', or 'Uptime:'
    in any order. Their values can vary.
    """
    with open(DIAGNOSTICS_LOG, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 4, (
        f"diagnostics.log should have at least 4 lines for validation, found {len(lines)}."
    )
    next_three = [line.rstrip("\n") for line in lines[1:4]]
    headers_found = set()
    expected_headers = {"Hostname:", "OS Version:", "Uptime:"}
    for line in next_three:
        for header in expected_headers:
            if line.startswith(header):
                headers_found.add(header)
                break
        else:
            pytest.fail(
                f"Line does not start with any of the required headers ('Hostname:', 'OS Version:', 'Uptime:'):\n"
                f"  {line}"
            )
    missing = expected_headers - headers_found
    assert not missing, (
        f"Missing required diagnostic lines in diagnostics.log: {', '.join(sorted(missing))}\n"
        f"First four lines:\n" +
        "".join(lines[:4])
    )

def test_no_unexpected_files_created():
    """
    Ensure that only /home/user/legacy_app/diagnostics.log is created as a result of the task.
    No other new files or directories should appear.
    """
    expected_files = {"collect_info.py", "diagnostics.log"}
    actual_files = set(os.listdir(LEGACY_APP_DIR))
    unexpected = actual_files - expected_files
    assert not unexpected, (
        f"Unexpected files or directories found in {LEGACY_APP_DIR}: {', '.join(sorted(unexpected))}\n"
        f"Only collect_info.py and diagnostics.log should be present after the task."
    )

def test_collect_info_py_untouched():
    """
    Ensure that collect_info.py still exists after the task and is still a file.
    """
    assert os.path.exists(COLLECT_INFO), (
        f"collect_info.py is missing after the diagnostics collection task."
    )
    assert os.path.isfile(COLLECT_INFO), (
        f"collect_info.py exists but is not a file after the task."
    )