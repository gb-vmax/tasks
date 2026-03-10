# test_final_state.py

import os
import pytest

SLOW_REQUESTS_PATH = "/home/user/logs/slow_requests.txt"
ACCESS_LOG_PATH = "/home/user/logs/access.log"

EXPECTED_LINES = [
    "[2024-06-01T08:13:45Z] POST /api/orders => 892ms (500)",
    "[2024-06-01T08:19:58Z] GET /api/orders => 415ms (200)",
    "[2024-06-01T08:23:34Z] GET /api/products => 1203ms (503)",
    "[2024-06-01T08:27:17Z] GET /api/reports => 761ms (200)",
    "[2024-06-01T08:29:45Z] POST /api/orders => 512ms (500)",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES)


def test_slow_requests_file_exists():
    assert os.path.isfile(SLOW_REQUESTS_PATH), (
        f"File '{SLOW_REQUESTS_PATH}' does not exist. "
        "The slow requests output file must be created by the task."
    )


def test_slow_requests_file_readable():
    assert os.access(SLOW_REQUESTS_PATH, os.R_OK), (
        f"File '{SLOW_REQUESTS_PATH}' is not readable."
    )


def test_slow_requests_line_count():
    with open(SLOW_REQUESTS_PATH, "r") as f:
        lines = [line for line in f.read().splitlines() if line.strip()]
    assert len(lines) == 5, (
        f"File '{SLOW_REQUESTS_PATH}' should have 5 lines, but has {len(lines)} lines.\n"
        f"Lines found:\n" + "\n".join(lines)
    )


def test_slow_requests_no_blank_lines():
    with open(SLOW_REQUESTS_PATH, "r") as f:
        raw_lines = f.read().splitlines()
    blank_lines = [i + 1 for i, line in enumerate(raw_lines) if line.strip() == ""]
    assert not blank_lines, (
        f"File '{SLOW_REQUESTS_PATH}' contains blank lines at line numbers: {blank_lines}. "
        "No blank lines are allowed."
    )


def test_slow_requests_no_trailing_whitespace():
    with open(SLOW_REQUESTS_PATH, "r") as f:
        raw_lines = f.read().splitlines()
    offending = [(i + 1, repr(line)) for i, line in enumerate(raw_lines) if line != line.rstrip()]
    assert not offending, (
        f"File '{SLOW_REQUESTS_PATH}' has trailing whitespace on the following lines:\n"
        + "\n".join(f"  Line {lineno}: {content}" for lineno, content in offending)
    )


def test_slow_requests_no_header():
    with open(SLOW_REQUESTS_PATH, "r") as f:
        first_line = f.readline().rstrip()
    assert first_line == EXPECTED_LINES[0], (
        f"File '{SLOW_REQUESTS_PATH}' first line is unexpected (possible header or wrong entry).\n"
        f"Expected: '{EXPECTED_LINES[0]}'\n"
        f"Got:      '{first_line}'"
    )


def test_slow_requests_exact_content():
    with open(SLOW_REQUESTS_PATH, "r") as f:
        content = f.read()
    # Strip trailing newline for comparison but ensure no extra blank lines
    stripped = content.strip()
    assert stripped == EXPECTED_CONTENT, (
        f"File '{SLOW_REQUESTS_PATH}' does not have the expected content.\n"
        f"Expected:\n{EXPECTED_CONTENT}\n\n"
        f"Got:\n{stripped}"
    )


def test_slow_requests_each_line_format():
    """Verify each line in the output matches the required format."""
    with open(SLOW_REQUESTS_PATH, "r") as f:
        lines = [line.rstrip() for line in f.read().splitlines() if line.strip()]

    for i, line in enumerate(lines):
        # Format: [<timestamp>] <method> <endpoint> => <response_time_ms>ms (<status_code>)
        assert line.startswith("["), (
            f"Line {i + 1} does not start with '[': '{line}'"
        )
        assert "=>" in line, (
            f"Line {i + 1} does not contain '=>': '{line}'"
        )
        assert "ms (" in line, (
            f"Line {i + 1} does not contain 'ms (': '{line}'"
        )
        assert line.endswith(")"), (
            f"Line {i + 1} does not end with ')': '{line}'"
        )


def test_slow_requests_correct_entries():
    """Verify the correct log entries (response_time > 400) are included."""
    with open(SLOW_REQUESTS_PATH, "r") as f:
        lines = [line.rstrip() for line in f.read().splitlines() if line.strip()]

    assert len(lines) == len(EXPECTED_LINES), (
        f"Expected {len(EXPECTED_LINES)} lines but got {len(lines)}."
    )

    for i, (actual, expected) in enumerate(zip(lines, EXPECTED_LINES)):
        assert actual == expected, (
            f"Line {i + 1} mismatch.\n"
            f"Expected: '{expected}'\n"
            f"Got:      '{actual}'"
        )


def test_slow_requests_excludes_fast_entries():
    """Verify that entries with response_time <= 400 are NOT included."""
    with open(SLOW_REQUESTS_PATH, "r") as f:
        content = f.read()

    # These timestamps correspond to entries with response_time <= 400
    excluded_timestamps = [
        "2024-06-01T08:12:03Z",  # 143ms
        "2024-06-01T08:15:22Z",  # 310ms
        "2024-06-01T08:17:09Z",  # 55ms
        "2024-06-01T08:21:11Z",  # 88ms
        "2024-06-01T08:25:00Z",  # 399ms (NOT > 400)
    ]

    for ts in excluded_timestamps:
        assert ts not in content, (
            f"File '{SLOW_REQUESTS_PATH}' incorrectly includes an entry with timestamp '{ts}', "
            f"which has a response time <= 400ms and should be excluded."
        )


def test_slow_requests_order_preserved():
    """Verify the matching entries appear in the same order as in the original log."""
    with open(SLOW_REQUESTS_PATH, "r") as f:
        lines = [line.rstrip() for line in f.read().splitlines() if line.strip()]

    expected_timestamps_in_order = [
        "2024-06-01T08:13:45Z",
        "2024-06-01T08:19:58Z",
        "2024-06-01T08:23:34Z",
        "2024-06-01T08:27:17Z",
        "2024-06-01T08:29:45Z",
    ]

    actual_timestamps = []
    for line in lines:
        # Extract timestamp from [<timestamp>]
        if line.startswith("["):
            end_bracket = line.index("]")
            ts = line[1:end_bracket]
            actual_timestamps.append(ts)

    assert actual_timestamps == expected_timestamps_in_order, (
        f"Entries in '{SLOW_REQUESTS_PATH}' are not in the correct order.\n"
        f"Expected order: {expected_timestamps_in_order}\n"
        f"Got order:      {actual_timestamps}"
    )


def test_access_log_unchanged():
    """Verify the original access log file was not modified."""
    expected_access_log = (
        "2024-06-01T08:12:03Z 192.168.1.10 GET /api/users 200 143\n"
        "2024-06-01T08:13:45Z 10.0.0.5 POST /api/orders 500 892\n"
        "2024-06-01T08:15:22Z 172.16.0.3 GET /api/products 200 310\n"
        "2024-06-01T08:17:09Z 192.168.1.44 DELETE /api/sessions 204 55\n"
        "2024-06-01T08:19:58Z 10.0.0.8 GET /api/orders 200 415\n"
        "2024-06-01T08:21:11Z 192.168.1.10 POST /api/users 201 88\n"
        "2024-06-01T08:23:34Z 172.16.0.9 GET /api/products 503 1203\n"
        "2024-06-01T08:25:00Z 10.0.0.5 PUT /api/users 200 399\n"
        "2024-06-01T08:27:17Z 192.168.1.77 GET /api/reports 200 761\n"
        "2024-06-01T08:29:45Z 10.0.0.8 POST /api/orders 500 512"
    )
    with open(ACCESS_LOG_PATH, "r") as f:
        content = f.read().strip()
    assert content == expected_access_log.strip(), (
        f"The original access log '{ACCESS_LOG_PATH}' appears to have been modified.\n"
        f"Expected:\n{expected_access_log.strip()}\n\n"
        f"Got:\n{content}"
    )