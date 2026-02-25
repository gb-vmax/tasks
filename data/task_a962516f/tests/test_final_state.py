# test_final_state.py

import os
import pytest

LOG_PATH = '/home/user/traceroute_status.log'
TRACEROUTE_PATH = '/usr/bin/traceroute'
EXPECTED_LOG_CONTENT = 'Installed: no'

def test_traceroute_binary_still_absent():
    assert not os.path.exists(TRACEROUTE_PATH), (
        f"Expected '{TRACEROUTE_PATH}' to NOT exist after task completion, "
        "but it does. 'traceroute' should NOT be installed."
    )

def test_traceroute_status_log_exists():
    assert os.path.isfile(LOG_PATH), (
        f"Expected log file '{LOG_PATH}' to exist after task completion, "
        "but it does not."
    )

def test_traceroute_status_log_content():
    assert os.path.isfile(LOG_PATH), (
        f"Log file '{LOG_PATH}' does not exist to check its content."
    )
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    assert len(lines) == 1, (
        f"Log file '{LOG_PATH}' must contain exactly one line, "
        f"but it has {len(lines)} lines."
    )
    content = lines[0].rstrip('\n')
    assert content == EXPECTED_LOG_CONTENT, (
        f"Log file '{LOG_PATH}' must contain exactly:\n"
        f"  {EXPECTED_LOG_CONTENT!r}\n"
        f"but it contains:\n"
        f"  {content!r}\n"
        "Content must match exactly, with no extra spaces or lines."
    )