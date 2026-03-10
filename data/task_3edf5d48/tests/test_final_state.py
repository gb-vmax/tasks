# test_final_state.py

import os
import pytest

ERROR_TXT = "/home/user/incident/error.txt"
SUMMARY_TXT = "/home/user/incident/summary.txt"
SCRIPT_PATH = "/home/user/incident/analyze_log.py"
LOG_PATH = "/home/user/incident/server.log"

EXPECTED_ERROR_TXT = (
    "Traceback (most recent call last):\n"
    '  File "/home/user/incident/analyze_log.py", line 10, in <module>\n'
    '    threshold = int(os.environ["LOG_THRESHOLD"])\n'
    "KeyError: 'LOG_THRESHOLD'\n"
)

EXPECTED_SUMMARY_TXT = (
    "Lines above threshold: 4\n"
    "Flagged entries:\n"
    "  [ERROR] disk quota exceeded\n"
    "  [ERROR] connection timeout\n"
    "  [ERROR] failed to write to socket\n"
    "  [ERROR] null pointer in handler\n"
)


# ---------------------------------------------------------------------------
# error.txt checks
# ---------------------------------------------------------------------------

def test_error_txt_exists():
    assert os.path.isfile(ERROR_TXT), (
        f"{ERROR_TXT} does not exist. "
        "You must run the script without LOG_THRESHOLD set and redirect stderr to this file."
    )


def test_error_txt_is_not_empty():
    assert os.path.getsize(ERROR_TXT) > 0, (
        f"{ERROR_TXT} exists but is empty. "
        "The file should contain the Python traceback from the failed run."
    )


def test_error_txt_exact_content():
    with open(ERROR_TXT, "r") as f:
        content = f.read()
    assert content == EXPECTED_ERROR_TXT, (
        f"{ERROR_TXT} does not contain the expected content.\n"
        f"Expected:\n{EXPECTED_ERROR_TXT!r}\n"
        f"Got:\n{content!r}\n"
        "Make sure you captured stderr from the first (failing) run of the script."
    )


def test_error_txt_contains_traceback_header():
    with open(ERROR_TXT, "r") as f:
        content = f.read()
    assert "Traceback (most recent call last):" in content, (
        f"{ERROR_TXT} does not contain 'Traceback (most recent call last):'. "
        "The file must contain the Python traceback from the failed run."
    )


def test_error_txt_references_correct_file_and_line():
    with open(ERROR_TXT, "r") as f:
        content = f.read()
    expected_file_ref = '  File "/home/user/incident/analyze_log.py", line 10, in <module>'
    assert expected_file_ref in content, (
        f"{ERROR_TXT} does not contain the expected file/line reference.\n"
        f"Expected line: {expected_file_ref!r}\n"
        f"Got content:\n{content!r}"
    )


def test_error_txt_contains_key_error():
    with open(ERROR_TXT, "r") as f:
        content = f.read()
    assert "KeyError: 'LOG_THRESHOLD'" in content, (
        f"{ERROR_TXT} does not contain \"KeyError: 'LOG_THRESHOLD'\". "
        "The traceback must end with the KeyError for the missing environment variable."
    )


def test_error_txt_contains_offending_line():
    with open(ERROR_TXT, "r") as f:
        content = f.read()
    assert 'threshold = int(os.environ["LOG_THRESHOLD"])' in content, (
        f"{ERROR_TXT} does not contain the offending source line "
        "'threshold = int(os.environ[\"LOG_THRESHOLD\"])'. "
        "The traceback should include the source line that caused the error."
    )


def test_error_txt_no_extra_content():
    """error.txt should contain exactly the traceback — no stdout mixed in."""
    with open(ERROR_TXT, "r") as f:
        content = f.read()
    # Ensure stdout output is NOT present in error.txt
    assert "Lines above threshold" not in content, (
        f"{ERROR_TXT} contains stdout output ('Lines above threshold'). "
        "Only stderr should be captured in error.txt."
    )
    assert "Flagged entries" not in content, (
        f"{ERROR_TXT} contains stdout output ('Flagged entries'). "
        "Only stderr should be captured in error.txt."
    )


# ---------------------------------------------------------------------------
# summary.txt checks
# ---------------------------------------------------------------------------

def test_summary_txt_exists():
    assert os.path.isfile(SUMMARY_TXT), (
        f"{SUMMARY_TXT} does not exist. "
        "You must run the script with LOG_THRESHOLD=3 and capture stdout to this file."
    )


def test_summary_txt_is_not_empty():
    assert os.path.getsize(SUMMARY_TXT) > 0, (
        f"{SUMMARY_TXT} exists but is empty. "
        "The file should contain the successful output of the script."
    )


def test_summary_txt_exact_content():
    with open(SUMMARY_TXT, "r") as f:
        content = f.read()
    assert content == EXPECTED_SUMMARY_TXT, (
        f"{SUMMARY_TXT} does not contain the expected content.\n"
        f"Expected:\n{EXPECTED_SUMMARY_TXT!r}\n"
        f"Got:\n{content!r}\n"
        "Make sure you ran the script with LOG_THRESHOLD=3 and captured stdout."
    )


def test_summary_txt_first_line():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 1, (
        f"{SUMMARY_TXT} has no lines."
    )
    assert lines[0].rstrip("\n") == "Lines above threshold: 4", (
        f"First line of {SUMMARY_TXT} is {lines[0]!r}, "
        "expected 'Lines above threshold: 4'."
    )


def test_summary_txt_second_line():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 2, (
        f"{SUMMARY_TXT} has fewer than 2 lines."
    )
    assert lines[1].rstrip("\n") == "Flagged entries:", (
        f"Second line of {SUMMARY_TXT} is {lines[1]!r}, "
        "expected 'Flagged entries:'."
    )


def test_summary_txt_flagged_entry_1():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 3, (
        f"{SUMMARY_TXT} has fewer than 3 lines; missing flagged entries."
    )
    assert lines[2].rstrip("\n") == "  [ERROR] disk quota exceeded", (
        f"Line 3 of {SUMMARY_TXT} is {lines[2]!r}, "
        "expected '  [ERROR] disk quota exceeded'."
    )


def test_summary_txt_flagged_entry_2():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 4, (
        f"{SUMMARY_TXT} has fewer than 4 lines; missing flagged entries."
    )
    assert lines[3].rstrip("\n") == "  [ERROR] connection timeout", (
        f"Line 4 of {SUMMARY_TXT} is {lines[3]!r}, "
        "expected '  [ERROR] connection timeout'."
    )


def test_summary_txt_flagged_entry_3():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 5, (
        f"{SUMMARY_TXT} has fewer than 5 lines; missing flagged entries."
    )
    assert lines[4].rstrip("\n") == "  [ERROR] failed to write to socket", (
        f"Line 5 of {SUMMARY_TXT} is {lines[4]!r}, "
        "expected '  [ERROR] failed to write to socket'."
    )


def test_summary_txt_flagged_entry_4():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 6, (
        f"{SUMMARY_TXT} has fewer than 6 lines; missing flagged entries."
    )
    assert lines[5].rstrip("\n") == "  [ERROR] null pointer in handler", (
        f"Line 6 of {SUMMARY_TXT} is {lines[5]!r}, "
        "expected '  [ERROR] null pointer in handler'."
    )


def test_summary_txt_line_count():
    with open(SUMMARY_TXT, "r") as f:
        content = f.read()
    # Expected: 6 lines of text + trailing newline → split gives 6 non-empty parts
    lines = content.splitlines()
    assert len(lines) == 6, (
        f"{SUMMARY_TXT} has {len(lines)} lines (after splitlines), expected 6.\n"
        f"Content: {content!r}"
    )


def test_summary_txt_no_traceback():
    """summary.txt should not contain any Python traceback."""
    with open(SUMMARY_TXT, "r") as f:
        content = f.read()
    assert "Traceback" not in content, (
        f"{SUMMARY_TXT} contains 'Traceback', which suggests stderr was mixed into stdout. "
        "Only the successful stdout output should be in summary.txt."
    )
    assert "KeyError" not in content, (
        f"{SUMMARY_TXT} contains 'KeyError'. "
        "Only the successful stdout output should be in summary.txt."
    )


# ---------------------------------------------------------------------------
# Pre-existing file integrity checks
# ---------------------------------------------------------------------------

def test_script_still_exists_and_unchanged_line_10():
    """Verify the script still has LOG_THRESHOLD on line 10 (not modified by the student)."""
    assert os.path.isfile(SCRIPT_PATH), (
        f"{SCRIPT_PATH} no longer exists. The script should not have been deleted."
    )
    with open(SCRIPT_PATH, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 10, (
        f"{SCRIPT_PATH} has fewer than 10 lines; it may have been modified."
    )
    line_10 = lines[9].strip()
    assert "LOG_THRESHOLD" in line_10, (
        f"Line 10 of {SCRIPT_PATH} is {line_10!r}; "
        "expected it to still contain 'LOG_THRESHOLD'. "
        "The script should not have been modified."
    )


def test_server_log_still_exists():
    assert os.path.isfile(LOG_PATH), (
        f"{LOG_PATH} no longer exists. The log file should not have been deleted."
    )


def test_server_log_still_has_four_errors():
    with open(LOG_PATH, "r") as f:
        lines = f.readlines()
    error_lines = [l.strip() for l in lines if l.strip().startswith("[ERROR]")]
    assert len(error_lines) == 4, (
        f"Expected 4 [ERROR] lines in {LOG_PATH}, found {len(error_lines)}. "
        "The log file should not have been modified."
    )