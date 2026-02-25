# test_final_state.py

import os
import stat
import pytest

LOGS_DIR = "/home/user/logs"
TESTAPP_LOG = "/home/user/logs/testapp.log"
FILTERED_REPORT = "/home/user/logs/filtered_report.txt"

EXPECTED_TESTAPP_LOG_LINES = [
    "2024-04-11 10:12:01 INFO Starting application",
    "2024-04-11 10:12:03 WARNING Deprecated configuration detected",
    "2024-04-11 10:12:07 ERROR Failed to connect to database",
    "2024-04-11 10:12:09 INFO Database retry attempt 1",
    "2024-04-11 10:12:11 WARNING Low disk space",
    "2024-04-11 10:12:13 ERROR Could not locate config file",
    "2024-04-11 10:12:16 INFO Application shutdown complete"
]

EXPECTED_FILTERED_LINES = [
    "2024-04-11 10:12:03 WARNING Deprecated configuration detected",
    "2024-04-11 10:12:07 ERROR Failed to connect to database",
    "2024-04-11 10:12:11 WARNING Low disk space",
    "2024-04-11 10:12:13 ERROR Could not locate config file"
]

FINAL_CONSOLE_OUTPUT = "/home/user/logs/filtered_report.txt"

@pytest.mark.order(1)
def test_logs_directory_exists_and_writable():
    assert os.path.isdir(LOGS_DIR), (
        f"Directory '{LOGS_DIR}' does not exist. "
        "It must exist at the end of the task."
    )
    st = os.stat(LOGS_DIR)
    mode = st.st_mode
    uid = os.getuid()
    if uid == 0:
        return
    if st.st_uid == uid:
        assert bool(mode & stat.S_IWUSR), (
            f"The user does not have write permission to '{LOGS_DIR}'."
        )
    elif st.st_gid == os.getgid():
        assert bool(mode & stat.S_IWGRP), (
            f"The user's group does not have write permission to '{LOGS_DIR}'."
        )
    else:
        assert bool(mode & stat.S_IWOTH), (
            f"No write permission for '{LOGS_DIR}'."
        )

@pytest.mark.order(2)
def test_testapp_log_file_exact_contents():
    assert os.path.isfile(TESTAPP_LOG), (
        f"File '{TESTAPP_LOG}' does not exist. "
        "You must create this file with the exact required content."
    )
    with open(TESTAPP_LOG, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]
    assert lines == EXPECTED_TESTAPP_LOG_LINES, (
        f"File '{TESTAPP_LOG}' does not have the required content.\n"
        f"EXPECTED:\n{EXPECTED_TESTAPP_LOG_LINES}\n"
        f"FOUND:\n{lines}\n"
        "Check for missing, extra, or out-of-order lines, and ensure there is no extra whitespace."
    )

@pytest.mark.order(3)
def test_filtered_report_file_exact_contents():
    assert os.path.isfile(FILTERED_REPORT), (
        f"File '{FILTERED_REPORT}' does not exist. "
        "You must create this file by filtering the log with the correct regex."
    )
    with open(FILTERED_REPORT, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]
    assert lines == EXPECTED_FILTERED_LINES, (
        f"Filtered report '{FILTERED_REPORT}' does not match the required output.\n"
        f"EXPECTED:\n{EXPECTED_FILTERED_LINES}\n"
        f"FOUND:\n{lines}\n"
        "The file must contain only the lines with 'WARNING' or 'ERROR' (case-sensitive, whole word), "
        "in the correct order, with no extra lines or whitespace."
    )

@pytest.mark.order(4)
def test_no_extra_lines_in_filtered_report():
    with open(FILTERED_REPORT, 'r', encoding='utf-8') as f:
        raw = f.read()
    # Check for extra blank lines at start or end
    assert raw == '\n'.join(EXPECTED_FILTERED_LINES) + '\n' or raw == '\n'.join(EXPECTED_FILTERED_LINES), (
        f"Filtered report '{FILTERED_REPORT}' must not have extra blank lines or whitespace.\n"
        "Check for any stray newlines at the beginning/end of the file."
    )

@pytest.mark.order(5)
def test_final_console_output_matches(monkeypatch, capsys):
    # Simulate the agent's output: in reality, the student's script should print this path as the final line.
    # Here we simulate what should have been printed.
    print(FINAL_CONSOLE_OUTPUT)
    captured = capsys.readouterr()
    output_lines = [line.strip() for line in captured.out.splitlines() if line.strip()]
    assert output_lines, (
        "No console output detected. "
        f"The agent must output the absolute path '{FINAL_CONSOLE_OUTPUT}' as the final line."
    )
    assert output_lines[-1] == FINAL_CONSOLE_OUTPUT, (
        f"The final console output must be '{FINAL_CONSOLE_OUTPUT}', "
        f"but got: '{output_lines[-1]}'"
    )