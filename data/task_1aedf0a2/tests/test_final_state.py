# test_final_state.py

import os
import pytest
import re

SERVICE_API_LOG = "/home/user/microservices/logs/service-api.log"
ERROR_SUMMARY = "/home/user/microservices/logs/error_summary.txt"
LOGS_DIR = "/home/user/microservices/logs"

# The expected lines containing 'ERROR' as a whole word, in order
EXPECTED_ERROR_LINES = [
    "2024-06-10 08:12:45 ERROR Failed to connect to Redis",
    "2024-06-10 08:15:01 ERROR Service unavailable",
    "2024-06-10 08:18:12 ERROR Payment gateway timeout",
]

EXPECTED_ERROR_COUNT = len(EXPECTED_ERROR_LINES)
EXPECTED_SUMMARY_CONTENT = (
    "\n".join(EXPECTED_ERROR_LINES) + f"\nTotal ERROR lines: {EXPECTED_ERROR_COUNT}\n"
)

def test_error_summary_file_exists():
    assert os.path.isfile(ERROR_SUMMARY), (
        f"The summary file {ERROR_SUMMARY} does not exist. "
        "You must create this file with the required error summary."
    )

def test_error_summary_content_exact():
    try:
        with open(ERROR_SUMMARY, "r", encoding="utf-8") as f:
            summary_content = f.read()
    except Exception as e:
        pytest.fail(f"Could not read {ERROR_SUMMARY}: {e}")

    # Check for exact match, including trailing newline
    if summary_content != EXPECTED_SUMMARY_CONTENT:
        # Find specific differences for a more helpful message
        expected_lines = EXPECTED_SUMMARY_CONTENT.splitlines()
        actual_lines = summary_content.splitlines()
        # Compare line by line
        diffs = []
        for idx, (exp, act) in enumerate(zip(expected_lines, actual_lines)):
            if exp != act:
                diffs.append(
                    f"Line {idx+1} mismatch:\n  Expected: {exp!r}\n  Got:      {act!r}"
                )
        # Check for extra/missing lines
        if len(actual_lines) < len(expected_lines):
            diffs.append(f"Missing {len(expected_lines) - len(actual_lines)} lines at end.")
        elif len(actual_lines) > len(expected_lines):
            diffs.append(f"Found {len(actual_lines) - len(expected_lines)} extra lines at end.")
        # Check for trailing newline
        if not summary_content.endswith('\n'):
            diffs.append("Missing trailing newline at end of file.")

        # Compose helpful error message
        pytest.fail(
            f"The content of {ERROR_SUMMARY} does not match the required format.\n"
            f"Expected content (repr):\n{EXPECTED_SUMMARY_CONTENT!r}\n"
            f"Actual content (repr):\n{summary_content!r}\n"
            + ("\n".join(diffs) if diffs else "")
        )

def test_error_summary_only_error_lines():
    """
    Validate that only lines containing 'ERROR' as a whole word (case-sensitive)
    are present before the 'Total ERROR lines' line.
    """
    with open(ERROR_SUMMARY, "r", encoding="utf-8") as f:
        summary_lines = f.read().splitlines()

    # All lines except the last must be error lines
    error_lines = summary_lines[:-1]
    # Regular expression for 'ERROR' as a whole word
    error_regex = re.compile(r"\bERROR\b")

    for idx, line in enumerate(error_lines, 1):
        assert error_regex.search(line), (
            f"Line {idx} in {ERROR_SUMMARY} does not contain 'ERROR' as a whole word:\n"
            f"  {line!r}\n"
            f"Only lines with the keyword 'ERROR' as a whole word should be included."
        )

def test_error_summary_total_count_line():
    """
    Validate that the last line is formatted as 'Total ERROR lines: X' and X matches the number of error lines.
    """
    with open(ERROR_SUMMARY, "r", encoding="utf-8") as f:
        summary_lines = f.read().splitlines()

    assert summary_lines, (
        f"{ERROR_SUMMARY} is empty. It must contain all error lines and the total count line."
    )

    count_line = summary_lines[-1]
    match = re.match(r"^Total ERROR lines: (\d+)$", count_line)
    assert match is not None, (
        f"The last line of {ERROR_SUMMARY} must be formatted exactly as 'Total ERROR lines: X'. "
        f"Got: {count_line!r}"
    )
    count_in_file = int(match.group(1))
    actual_error_lines = summary_lines[:-1]
    assert count_in_file == len(actual_error_lines), (
        f"The number in the total line (X={count_in_file}) does not match the number of error lines ({len(actual_error_lines)})."
    )

def test_error_summary_no_extra_lines_or_whitespace():
    """
    Ensure there are no extra blank lines or whitespace at start/end or between lines.
    """
    with open(ERROR_SUMMARY, "r", encoding="utf-8") as f:
        content = f.read()

    # No leading/trailing whitespace or blank lines
    assert not content.startswith("\n"), (
        f"{ERROR_SUMMARY} starts with a blank line or leading newline. "
        "There should be no blank lines at the start."
    )
    # Should end with a single newline (already checked by previous test)
    # No blank lines in the middle
    lines = content.splitlines()
    for idx, line in enumerate(lines, 1):
        assert line.strip() == line, (
            f"Line {idx} in {ERROR_SUMMARY} has unexpected leading/trailing whitespace:\n"
            f"{line!r}\n"
            "Lines must not have leading or trailing spaces."
        )
        assert line != "", (
            f"Line {idx} in {ERROR_SUMMARY} is blank. "
            "There should be no blank lines in the summary file."
        )