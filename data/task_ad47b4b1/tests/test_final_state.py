# test_final_state.py

import os
import stat
import pytest

LOGS_DIR = "/home/user/logs"
LOG_FILE = "/home/user/logs/optim-solver.log"
ALERTS_DIR = "/home/user/alerts"
ALERTS_FILE = "/home/user/alerts/optim-solver-alerts.log"

EXPECTED_ALERT_LINES = [
    "[2024-06-03 10:01:19] WARNING Convergence slow",
    "[2024-06-03 10:01:22] ERROR Constraint violation detected",
    "[2024-06-03 10:01:26] WARNING Memory usage high",
]
EXPECTED_ALERT_CONTENT = "\n".join(EXPECTED_ALERT_LINES) + "\n"

def test_alerts_directory_exists_and_is_writable():
    assert os.path.isdir(ALERTS_DIR), (
        f"Required directory '{ALERTS_DIR}' does not exist. "
        "You must create this directory to store alerts."
    )
    # Check that the directory is user-writable
    st = os.stat(ALERTS_DIR)
    mode = st.st_mode
    # Only the user needs to be able to write
    assert mode & stat.S_IWUSR, (
        f"Directory '{ALERTS_DIR}' is not user-writable. "
        "Please ensure you have write permissions for the user."
    )

def test_alerts_file_exists():
    assert os.path.isfile(ALERTS_FILE), (
        f"Alerts file '{ALERTS_FILE}' does not exist. "
        "It must be created by filtering the relevant log lines."
    )

def test_alerts_file_content_exact():
    try:
        with open(ALERTS_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        pytest.fail(f"Could not read '{ALERTS_FILE}': {e}")

    # Check for exact content (including no extra blank lines)
    if content != EXPECTED_ALERT_CONTENT:
        # show difference for debugging
        expected_lines = EXPECTED_ALERT_CONTENT.splitlines(keepends=True)
        found_lines = content.splitlines(keepends=True)
        diff = []
        max_lines = max(len(expected_lines), len(found_lines))
        for i in range(max_lines):
            exp = expected_lines[i] if i < len(expected_lines) else "<MISSING>"
            found = found_lines[i] if i < len(found_lines) else "<MISSING>"
            if exp != found:
                diff.append(f"Line {i+1}:\n  Expected: {repr(exp)}\n  Found:    {repr(found)}")
        diff_msg = "\n".join(diff)
        pytest.fail(
            f"Alerts file '{ALERTS_FILE}' does not contain exactly the expected alert lines.\n"
            f"Expected content:\n{EXPECTED_ALERT_CONTENT!r}\n"
            f"Found content:\n{content!r}\n"
            f"Difference(s):\n{diff_msg if diff else '(order/extra lines)'}\n"
            "Make sure:\n"
            "- Only lines containing 'WARNING' or 'ERROR' (case-sensitive) are present\n"
            "- No extra blank lines or whitespace\n"
            "- Order matches the original log"
        )

def test_alerts_file_contains_only_warning_error_lines():
    # This is a redundancy for clarity: make sure only correct lines are present, and nothing else
    with open(ALERTS_FILE, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]
    # Ensure there are no blank lines
    assert all(line.strip() for line in lines), (
        f"Alerts file '{ALERTS_FILE}' contains blank or whitespace-only lines. "
        "There should be no extra blank lines."
    )
    # Ensure all lines are from the expected set
    for line in lines:
        assert line in EXPECTED_ALERT_LINES, (
            f"Unexpected line in '{ALERTS_FILE}': {line!r}. "
            "Only lines with 'WARNING' or 'ERROR' from the original log should be present."
        )
    # Ensure no lines are missing or extra
    assert lines == EXPECTED_ALERT_LINES, (
        f"Lines in '{ALERTS_FILE}' are not in the correct order or are missing/extra.\n"
        f"Expected:\n{EXPECTED_ALERT_LINES}\n"
        f"Found:\n{lines}\n"
    )

def test_alerts_file_does_not_contain_info_lines():
    # Ensure no INFO or other lines are present
    with open(ALERTS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            assert "WARNING" in line or "ERROR" in line, (
                f"Line in '{ALERTS_FILE}' does not contain 'WARNING' or 'ERROR': {line!r}"
            )

def test_terminal_output_shows_alert_lines(capsys):
    """
    This test assumes that the final output to the terminal is exactly the alert lines.
    The agent should have displayed these lines as the last output.
    We simulate this by running a print, but in reality this test should be run after
    the agent displays the file contents.
    """
    # Simulate what the agent should do:
    # with open(ALERTS_FILE) as f: print(f.read(), end="")
    # Here we just check that if the agent had printed the file, it would be correct.
    with open(ALERTS_FILE, "r", encoding="utf-8") as f:
        expected_output = f.read()
    # Simulate print to stdout
    print(expected_output, end="")
    captured = capsys.readouterr()
    assert captured.out == EXPECTED_ALERT_CONTENT, (
        "Final terminal output does not match the required alert lines.\n"
        f"Expected:\n{EXPECTED_ALERT_CONTENT!r}\n"
        f"Found:\n{captured.out!r}\n"
        "You should display the contents of the alerts file as your final output."
    )