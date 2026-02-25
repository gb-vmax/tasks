# test_final_state.py

import os
import pytest

LOGS_DIR = "/home/user/logs"
ACCESS_LOG = "/home/user/logs/access.log"
ANALYSIS_REPORT = "/home/user/logs/analysis_report.txt"

# The expected contents of the access.log file (should NOT be modified)
ACCESS_LOG_CONTENT = """127.0.0.1 - - [15/Feb/2023:09:12:01 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.10 - - [15/Feb/2023:09:15:34 +0000] "GET /about.html HTTP/1.1" 404 512
10.0.0.2 - - [15/Feb/2023:10:05:21 +0000] "GET /contact.html HTTP/1.1" 200 2048
192.168.1.11 - - [15/Feb/2023:10:35:24 +0000] "POST /login HTTP/1.1" 200 512
127.0.0.1 - - [15/Feb/2023:10:50:12 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.10 - - [15/Feb/2023:10:58:07 +0000] "GET /missing.html HTTP/1.1" 404 512
10.0.0.2 - - [15/Feb/2023:11:03:10 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.12 - - [15/Feb/2023:11:33:45 +0000] "GET /index.html HTTP/1.1" 404 1024
192.168.1.11 - - [15/Feb/2023:11:51:19 +0000] "POST /login HTTP/1.1" 200 512
127.0.0.1 - - [15/Feb/2023:11:58:01 +0000] "GET /contact.html HTTP/1.1" 200 2048
"""

# The exact expected contents of the analysis_report.txt file
ANALYSIS_REPORT_CONTENT = (
    "Total Requests: 10\n"
    "404 Errors: 3\n"
    "Unique IPs: 10.0.0.2,127.0.0.1,192.168.1.10,192.168.1.11,192.168.1.12\n"
    "Peak Hour: 11 (4 requests)\n"
)

@pytest.mark.describe("Final state: logs directory exists")
def test_logs_dir_exists():
    assert os.path.isdir(LOGS_DIR), (
        f"Required directory '{LOGS_DIR}' does not exist. "
        f"Please ensure the logs directory is present at /home/user/logs."
    )

@pytest.mark.describe("Final state: access.log file exists and is unmodified")
def test_access_log_exists_and_unmodified():
    assert os.path.isfile(ACCESS_LOG), (
        f"Required log file '{ACCESS_LOG}' does not exist. "
        f"Please ensure access.log is present at /home/user/logs/access.log."
    )
    try:
        with open(ACCESS_LOG, "r", encoding="utf-8") as f:
            actual = f.read()
    except Exception as e:
        pytest.fail(f"Could not read {ACCESS_LOG}: {e}")
    expected = ACCESS_LOG_CONTENT.replace("\r\n", "\n").strip()
    actual = actual.replace("\r\n", "\n").strip()
    assert actual == expected, (
        f"The contents of '{ACCESS_LOG}' have been modified and are incorrect.\n"
        "Expected the following content:\n"
        f"{expected}\n"
        "But got:\n"
        f"{actual}\n"
        "Do not modify the original log file."
    )

@pytest.mark.describe("Final state: analysis_report.txt exists with correct contents")
def test_analysis_report_exists_and_correct():
    assert os.path.isfile(ANALYSIS_REPORT), (
        f"Report file '{ANALYSIS_REPORT}' does not exist. "
        "You must write the summary report at /home/user/logs/analysis_report.txt."
    )
    try:
        with open(ANALYSIS_REPORT, "r", encoding="utf-8") as f:
            actual = f.read()
    except Exception as e:
        pytest.fail(f"Could not read {ANALYSIS_REPORT}: {e}")
    expected = ANALYSIS_REPORT_CONTENT.replace("\r\n", "\n").strip()
    actual = actual.replace("\r\n", "\n").strip()
    assert actual == expected, (
        f"The contents of '{ANALYSIS_REPORT}' are incorrect.\n"
        "Expected EXACTLY:\n"
        f"{expected}\n"
        "But got:\n"
        f"{actual}\n"
        "Check formatting, blank lines, and field order."
    )

@pytest.mark.describe("Final state: No extra files in logs directory")
def test_no_extra_files_in_logs_dir():
    allowed_files = {"access.log", "analysis_report.txt"}
    try:
        entries = set(os.listdir(LOGS_DIR))
    except Exception as e:
        pytest.fail(f"Could not list directory {LOGS_DIR}: {e}")
    extra = entries - allowed_files
    assert extra == set() or extra == {'.'} or extra == {'..'}, (
        f"Unexpected files or directories found in {LOGS_DIR}: {extra}. "
        "Only 'access.log' and 'analysis_report.txt' should be present after the task."
    )