# test_final_state.py

import os
import pytest

LOGS_DIR = "/home/user/logs"
NGINX_APP_LOG = "/home/user/logs/nginx_app.log"
NGINX_ERROR_LINES = "/home/user/logs/nginx_error_lines.txt"

EXPECTED_LOG_CONTENT = (
    "2024-06-10 10:00:01 [INFO] nginx service starting.\n"
    "2024-06-10 10:00:03 [ERROR] nginx failed to start: Address already in use.\n"
    "2024-06-10 10:00:10 [WARN] retrying nginx start.\n"
    "2024-06-10 10:00:12 [ERROR] nginx configuration file /etc/nginx/nginx.conf not found.\n"
    "2024-06-10 10:01:00 [INFO] nginx service stopped.\n"
)

EXPECTED_ERROR_LINES = [
    "2024-06-10 10:00:03 [ERROR] nginx failed to start: Address already in use.\n",
    "2024-06-10 10:00:12 [ERROR] nginx configuration file /etc/nginx/nginx.conf not found.\n"
]

def test_logs_directory_still_exists():
    assert os.path.isdir(LOGS_DIR), (
        f"Required directory missing: {LOGS_DIR}. "
        "It must exist after the task is complete."
    )

def test_nginx_app_log_untouched():
    assert os.path.isfile(NGINX_APP_LOG), (
        f"Missing original log file: {NGINX_APP_LOG}. "
        "This file must not be deleted or renamed."
    )
    with open(NGINX_APP_LOG, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == EXPECTED_LOG_CONTENT, (
        f"The file {NGINX_APP_LOG} was modified. "
        "It must remain unchanged after the task.\n\n"
        "Expected:\n"
        f"{EXPECTED_LOG_CONTENT!r}\n\n"
        "Actual:\n"
        f"{content!r}"
    )

def test_nginx_error_lines_file_exists():
    assert os.path.isfile(NGINX_ERROR_LINES), (
        f"Output file {NGINX_ERROR_LINES} was not created. "
        "It must be present after the task is completed."
    )

def test_nginx_error_lines_content_exact():
    with open(NGINX_ERROR_LINES, 'r', encoding='utf-8') as f:
        error_lines = f.readlines()
    assert error_lines == EXPECTED_ERROR_LINES, (
        f"{NGINX_ERROR_LINES} does not contain exactly the expected lines with 'ERROR' from {NGINX_APP_LOG}.\n\n"
        "Expected lines:\n"
        f"{''.join(EXPECTED_ERROR_LINES)!r}\n\n"
        "Actual lines:\n"
        f"{''.join(error_lines)!r}\n"
        "Check for extra/missing lines, blank lines, or formatting changes."
    )

def test_nginx_error_lines_no_extra_blank_lines():
    with open(NGINX_ERROR_LINES, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        assert line.strip() != "", (
            f"Line {idx+1} in {NGINX_ERROR_LINES} is blank or only whitespace. "
            "No extra blank or whitespace-only lines are allowed."
        )

def test_nginx_error_lines_no_leading_trailing_spaces():
    with open(NGINX_ERROR_LINES, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, 1):
            if not line.endswith('\n'):
                # If last line doesn't end with newline, check as-is
                line_to_check = line
            else:
                line_to_check = line[:-1]
            assert line_to_check == line_to_check.strip(), (
                f"Line {idx} in {NGINX_ERROR_LINES} has leading or trailing whitespace. "
                "Lines must match the original formatting without added spaces."
            )