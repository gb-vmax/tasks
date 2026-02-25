# test_final_state.py

import os
import pytest

HOME = "/home/user"
APPDATA_DIR = os.path.join(HOME, "appdata")
DIAGNOSTICS_DIR = os.path.join(HOME, "diagnostics")
APP_LOG = os.path.join(APPDATA_DIR, "app.log")
FILTERED_LOG = os.path.join(DIAGNOSTICS_DIR, "filtered_errors_warnings.log")

EXPECTED_FILTERED_LOG_LINES = [
    "2024-06-10 08:00:00 [ERROR] Startup failed: missing config file.",
    "2024-06-11 13:20:48 [WARN] Deprecated API usage detected.",
    "2024-06-13 20:18:15 [ERROR] Database unavailable.",
    "2024-06-14 03:02:35 [WARN] High memory usage warning.",
    "2024-06-16 22:59:59 [ERROR] Critical failure in processing module.",
]

def test_filtered_log_exists_and_is_file():
    assert os.path.isfile(FILTERED_LOG), (
        f"Expected output file does not exist: {FILTERED_LOG}"
    )

def test_filtered_log_content_exact():
    with open(FILTERED_LOG, "r", encoding="utf-8") as f:
        actual_lines = [line.rstrip('\n') for line in f]
    assert actual_lines == EXPECTED_FILTERED_LOG_LINES, (
        f"{FILTERED_LOG} does not contain the exact expected filtered log lines.\n"
        f"Expected:\n{EXPECTED_FILTERED_LOG_LINES}\n"
        f"Found:\n{actual_lines}\n"
        "Check that:\n"
        "- Only ERROR and WARN entries from 2024-06-10 to 2024-06-16 (inclusive) are included.\n"
        "- Entries are in the original order from the source log.\n"
        "- There are no extra or missing lines, blank lines, headers, or footers."
    )

def test_filtered_log_has_no_blank_lines():
    with open(FILTERED_LOG, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        assert line.strip() != "", (
            f"Blank line found at line {idx} in {FILTERED_LOG}. "
            "There should be no blank lines in the output file."
        )

def test_filtered_log_no_extra_files_in_diagnostics():
    # Only allow expected files in diagnostics dir
    allowed_files = {"filtered_errors_warnings.log"}
    found_files = set(
        entry
        for entry in os.listdir(DIAGNOSTICS_DIR)
        if os.path.isfile(os.path.join(DIAGNOSTICS_DIR, entry))
    )
    extra_files = found_files - allowed_files
    assert not extra_files, (
        f"Unexpected file(s) found in {DIAGNOSTICS_DIR}: {sorted(extra_files)}. "
        "Only filtered_errors_warnings.log should be created as output."
    )

def test_source_log_is_unchanged():
    # The source log should not be modified.
    expected_lines = [
        "2024-06-09 17:45:22 [INFO] Pre-start checks completed.",
        "2024-06-10 08:00:00 [ERROR] Startup failed: missing config file.",
        "2024-06-10 08:00:05 [INFO] Attempting automated repair.",
        "2024-06-11 13:20:48 [WARN] Deprecated API usage detected.",
        "2024-06-11 14:21:00 [DEBUG] Heartbeat received.",
        "2024-06-13 20:18:15 [ERROR] Database unavailable.",
        "2024-06-14 03:02:35 [WARN] High memory usage warning.",
        "2024-06-16 22:59:59 [ERROR] Critical failure in processing module.",
        "2024-06-17 00:10:01 [WARN] Log rotation close failure.",
    ]
    assert os.path.isfile(APP_LOG), (
        f"Source log file missing after task: {APP_LOG}"
    )
    with open(APP_LOG, "r", encoding="utf-8") as f:
        actual_lines = [line.rstrip('\n') for line in f]
    assert actual_lines == expected_lines, (
        f"{APP_LOG} was modified during the task. It must remain unchanged.\n"
        f"Expected:\n{expected_lines}\n"
        f"Found:\n{actual_lines}"
    )