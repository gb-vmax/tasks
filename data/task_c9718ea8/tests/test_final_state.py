# test_final_state.py

import os
import pytest

SAMPLE_CONFIG_PATH = "/home/user/sample_config.txt"
CONVERTED_CONFIG_PATH = "/home/user/sample_config_iso8859-1.txt"
LOG_PATH = "/home/user/encoding_conversion_log.txt"

EXPECTED_CONTENT = (
    "ServerName=ExempleServeur\n"
    "Location=Europe\n"
    "ContactName=René Durand\n"
)

EXPECTED_LOG_LINES = [
    "Original Encoding: UTF-8",
    "Converted Encoding: ISO-8859-1"
]


def test_converted_file_exists():
    assert os.path.isfile(CONVERTED_CONFIG_PATH), (
        f"Converted file not found at {CONVERTED_CONFIG_PATH}."
    )


def test_converted_file_is_valid_iso8859_1():
    assert os.path.isfile(CONVERTED_CONFIG_PATH), (
        f"Converted file not found at {CONVERTED_CONFIG_PATH}."
    )
    try:
        with open(CONVERTED_CONFIG_PATH, "rb") as f:
            raw = f.read()
        # Try decoding as ISO-8859-1
        decoded = raw.decode("iso-8859-1")
    except UnicodeDecodeError:
        pytest.fail(
            f"The file at {CONVERTED_CONFIG_PATH} is not valid ISO-8859-1 encoding."
        )

    assert decoded == EXPECTED_CONTENT, (
        f"The content of {CONVERTED_CONFIG_PATH} does not match the expected content.\n"
        "Expected:\n"
        f"{repr(EXPECTED_CONTENT)}\n"
        "Found:\n"
        f"{repr(decoded)}"
    )

    # Check that the special character "é" is encoded as 0xE9 at the correct position
    expected_bytes = EXPECTED_CONTENT.encode("iso-8859-1")
    if raw != expected_bytes:
        # Find the first difference
        for i, (b1, b2) in enumerate(zip(raw, expected_bytes)):
            if b1 != b2:
                pytest.fail(
                    f"Byte mismatch at position {i}: expected 0x{b2:02x}, found 0x{b1:02x}."
                )
        if len(raw) != len(expected_bytes):
            pytest.fail(
                f"File length mismatch: expected {len(expected_bytes)} bytes, found {len(raw)} bytes."
            )
        pytest.fail(
            f"The byte content of {CONVERTED_CONFIG_PATH} does not match the expected ISO-8859-1 encoding."
        )


def test_conversion_log_exists():
    assert os.path.isfile(LOG_PATH), (
        f"Log file not found at {LOG_PATH}."
    )


def test_conversion_log_content_and_format():
    assert os.path.isfile(LOG_PATH), (
        f"Log file not found at {LOG_PATH}."
    )
    with open(LOG_PATH, "rb") as f:
        raw = f.read()
    # Check for CRLF vs LF
    if b'\r\n' in raw:
        lines = raw.decode("utf-8").split("\r\n")
        line_ending = '\\r\\n'
    else:
        lines = raw.decode("utf-8").split("\n")
        line_ending = '\\n'
    # Remove any trailing blank lines
    while lines and lines[-1] == '':
        lines.pop()
    assert len(lines) == 2, (
        f"Log file at {LOG_PATH} must contain exactly two lines, but contains {len(lines)} lines."
    )
    for i, (expected, actual) in enumerate(zip(EXPECTED_LOG_LINES, lines)):
        assert expected == actual, (
            f"Log file line {i+1} incorrect.\n"
            f"Expected: {repr(expected)}\n"
            f"Found:    {repr(actual)}"
        )
        assert actual.strip() == actual, (
            f"Log file line {i+1} has unexpected leading or trailing whitespace."
        )
    # Check that there are no extra blank lines or trailing whitespace
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) == 2, (
        f"Log file at {LOG_PATH} must contain exactly two lines, but contains {len(lines)} lines."
    )
    for i, line in enumerate(lines):
        assert not line.endswith(' \n') and not line.endswith('\t\n') and not line.rstrip('\n').endswith(' '), (
            f"Log file line {i+1} has unexpected trailing whitespace."
        )
        assert line.rstrip('\n') == line.strip('\n'), (
            f"Log file line {i+1} has unexpected leading or trailing whitespace."
        )
    # Check that there is no extra blank line at the end of the file
    with open(LOG_PATH, "rb") as f:
        content = f.read()
    if content.endswith(b"\n\n") or content.endswith(b"\r\n\r\n"):
        pytest.fail(f"Log file at {LOG_PATH} has extra blank lines at the end.")