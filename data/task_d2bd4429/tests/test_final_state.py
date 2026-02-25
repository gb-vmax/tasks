# test_final_state.py

"""
Pytest suite to validate the final state after serving /home/user/ml_data/raw_images
over HTTP on port 8080 and downloading cat1.jpg as /home/user/ml_data/fetched/cat1_copy.jpg,
with proper logging.

Assumptions:
- The test is run after the HTTP server has been started, the file downloaded, and the log created.
- Only the Python standard library and pytest are used.
"""

import os
import pytest

RAW_IMAGES_DIR = "/home/user/ml_data/raw_images"
FETCHED_DIR = "/home/user/ml_data/fetched"
CAT1_PATH = os.path.join(RAW_IMAGES_DIR, "cat1.jpg")
CAT1_COPY_PATH = os.path.join(FETCHED_DIR, "cat1_copy.jpg")
LOG_PATH = "/home/user/ml_data/download_log.txt"

EXPECTED_LOG = (
    "Original file: /home/user/ml_data/raw_images/cat1.jpg\n"
    "Downloaded file: /home/user/ml_data/fetched/cat1_copy.jpg\n"
    "Status: SUCCESS\n"
)
EXPECTED_CAT1_CONTENT = b"dummyimagecontent"

def test_cat1_copy_exists():
    assert os.path.isfile(CAT1_COPY_PATH), (
        f"Downloaded file '{CAT1_COPY_PATH}' does not exist. "
        f"Ensure you have downloaded 'cat1.jpg' from the server to this location."
    )

def test_cat1_copy_content_matches_original():
    assert os.path.isfile(CAT1_PATH), (
        f"Source file '{CAT1_PATH}' does not exist. Cannot compare contents."
    )
    with open(CAT1_PATH, "rb") as f:
        original = f.read()
    with open(CAT1_COPY_PATH, "rb") as f:
        copy = f.read()
    assert copy == original == EXPECTED_CAT1_CONTENT, (
        f"The contents of '{CAT1_COPY_PATH}' do not exactly match the expected original file. "
        f"Expected: {EXPECTED_CAT1_CONTENT!r}, Found: {copy!r}"
    )

def test_log_file_exists():
    assert os.path.isfile(LOG_PATH), (
        f"Log file '{LOG_PATH}' does not exist. "
        "Create this file with the required log message."
    )

def test_log_file_exact_contents():
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        log_content = f.read()
    # Check exact match to expected log (including newlines)
    assert log_content == EXPECTED_LOG, (
        f"Log file '{LOG_PATH}' does not have the exact expected content.\n"
        f"Expected:\n{EXPECTED_LOG!r}\nFound:\n{log_content!r}"
    )

def test_no_leading_or_trailing_spaces_in_log():
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        # Remove newline for checking leading/trailing spaces
        stripped = line.rstrip('\n')
        assert stripped == stripped.strip(), (
            f"Line {i+1} in '{LOG_PATH}' has leading or trailing spaces: {repr(line)}"
        )

def test_http_server_was_running_on_8080(monkeypatch):
    """
    Check that a process was or is serving /home/user/ml_data/raw_images on port 8080.

    This test checks if *any* process is listening on port 8080, and tries to fetch
    http://localhost:8080/cat1.jpg to confirm that the HTTP server is (or was) correctly serving.
    """
    import socket
    import http.client

    # First, check if anything is listening on 8080
    sock = socket.socket()
    try:
        sock.settimeout(1)
        sock.connect(("127.0.0.1", 8080))
        connected = True
    except Exception:
        connected = False
    finally:
        sock.close()

    if not connected:
        pytest.skip(
            "No process is currently listening on port 8080. "
            "Cannot verify server is still running, but other tests check for successful completion."
        )

    # If something is listening, try HTTP GET /cat1.jpg
    conn = http.client.HTTPConnection("localhost", 8080, timeout=2)
    try:
        conn.request("GET", "/cat1.jpg")
        resp = conn.getresponse()
        content = resp.read()
        assert resp.status == 200, (
            f"HTTP server on port 8080 did not return 200 OK for /cat1.jpg, "
            f"got status {resp.status}."
        )
        assert content == EXPECTED_CAT1_CONTENT, (
            f"HTTP GET /cat1.jpg returned unexpected content. "
            f"Expected: {EXPECTED_CAT1_CONTENT!r}, Found: {content!r}"
        )
    finally:
        conn.close()