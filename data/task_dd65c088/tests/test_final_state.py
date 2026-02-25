# test_final_state.py

import os
import pytest

MIGRATION_SUMMARY = '/home/user/migration/migration_summary.txt'
EXPECTED_SUMMARY_LINES = [
    "Total SUCCESS: 3",
    "Total FAILURE: 2",
]

def test_migration_summary_exists():
    assert os.path.exists(MIGRATION_SUMMARY), (
        f"Expected summary file {MIGRATION_SUMMARY} does not exist. "
        "The summary file must be present after completing the task."
    )
    assert os.path.isfile(MIGRATION_SUMMARY), (
        f"{MIGRATION_SUMMARY} exists but is not a file."
    )

def test_migration_summary_content_and_format():
    with open(MIGRATION_SUMMARY, encoding='utf-8') as f:
        lines = f.readlines()

    # Strip trailing newlines for comparison
    stripped_lines = [line.rstrip('\r\n') for line in lines]

    # Check line count
    if len(stripped_lines) != 2:
        raise AssertionError(
            f"{MIGRATION_SUMMARY} must contain exactly 2 lines. "
            f"Found {len(stripped_lines)} lines."
        )

    # Check exact content and order
    for idx, (expected, actual) in enumerate(zip(EXPECTED_SUMMARY_LINES, stripped_lines)):
        if actual != expected:
            raise AssertionError(
                f"Line {idx+1} of {MIGRATION_SUMMARY} is incorrect.\n"
                f"Expected: {expected!r}\nGot:      {actual!r}\n"
                "The summary file must match the required format and values exactly."
            )

def test_migration_summary_no_extra_content():
    """Ensure there are no extra lines or trailing blank lines in the summary file."""
    with open(MIGRATION_SUMMARY, encoding='utf-8') as f:
        raw_content = f.read()

    # The file must end with a single newline (POSIX text file)
    if not raw_content.endswith('\n'):
        raise AssertionError(
            f"{MIGRATION_SUMMARY} must end with a single newline character."
        )

    # There must not be any extra blank lines after the required two lines
    lines = raw_content.splitlines()
    if len(lines) > 2:
        raise AssertionError(
            f"{MIGRATION_SUMMARY} contains extra lines beyond the required two lines."
        )