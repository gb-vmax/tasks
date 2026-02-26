# test_final_state.py

import os
import pytest

TRIAGE_DIR = "/home/user/triage"
SUMMARY_FILE = "/home/user/triage/404_summary.txt"

EXPECTED_SUMMARY_LINES = [
    "404 count: 4",
    "Unique URLs:",
    "/notfound.html",
    "/missing.png",
    "/favicon.ico"
]


def test_triage_directory_exists():
    assert os.path.isdir(TRIAGE_DIR), (
        f"Required directory '{TRIAGE_DIR}' does not exist. "
        "You must create /home/user/triage/ as part of the task."
    )


def test_404_summary_file_exists():
    assert os.path.isfile(SUMMARY_FILE), (
        f"Required summary file '{SUMMARY_FILE}' does not exist. "
        "You must create /home/user/triage/404_summary.txt as part of the task."
    )


def test_404_summary_file_content_exact():
    """
    Check that /home/user/triage/404_summary.txt exactly matches the required format and values.
    """
    try:
        with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
            lines = [line.rstrip('\n') for line in f]
    except Exception as e:
        pytest.fail(f"Could not read {SUMMARY_FILE}: {e}")

    assert lines == EXPECTED_SUMMARY_LINES, (
        f"File '{SUMMARY_FILE}' does not exactly match the required format and content.\n"
        f"Expected ({len(EXPECTED_SUMMARY_LINES)} lines):\n"
        + "\n".join(EXPECTED_SUMMARY_LINES)
        + "\nActual ({0} lines):\n".format(len(lines))
        + "\n".join(lines)
        + "\n\n"
        "Please ensure:\n"
        "- The first line is '404 count: 4'\n"
        "- The second line is 'Unique URLs:'\n"
        "- The next lines are the unique URLs that returned 404, one per line, in order of first appearance\n"
        "- There are no extra blank lines, extra whitespace, or additional content."
    )


def test_404_summary_file_no_extra_lines():
    """
    Ensure there are no extra lines (blank or otherwise) at the end or in the content.
    """
    with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Check for trailing blank lines
    if lines and lines[-1].endswith('\n'):
        # Remove the last newline for comparison
        stripped_last = lines[-1].rstrip('\n')
        if stripped_last == "" and len(lines) > len(EXPECTED_SUMMARY_LINES):
            pytest.fail(
                f"File '{SUMMARY_FILE}' has extraneous blank lines at the end. "
                "There must be exactly 5 lines, no more."
            )
    assert len(lines) == len(EXPECTED_SUMMARY_LINES), (
        f"File '{SUMMARY_FILE}' must have exactly {len(EXPECTED_SUMMARY_LINES)} lines, "
        f"but has {len(lines)} lines."
    )


def test_404_summary_file_404_count_correct():
    """
    Ensure the 404 count line has the correct format and value.
    """
    with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
        first_line = f.readline().rstrip('\n')
    assert first_line == "404 count: 4", (
        f"The first line of '{SUMMARY_FILE}' must be '404 count: 4', but got '{first_line}'."
    )


def test_404_summary_file_unique_urls_correct_and_ordered():
    """
    Ensure that the unique URLs listed are correct and in the order of first appearance.
    """
    with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]

    # Defensive: already checked in previous tests, but for isolation:
    assert len(lines) >= 3, (
        f"File '{SUMMARY_FILE}' must have at least 3 lines (count, header, at least one URL)."
    )

    urls = lines[2:]
    expected_urls = ["/notfound.html", "/missing.png", "/favicon.ico"]
    assert urls == expected_urls, (
        f"The URLs listed in '{SUMMARY_FILE}' are incorrect or not in the order of first 404 appearance.\n"
        f"Expected URLs (in order):\n" + "\n".join(expected_urls) +
        "\nActual URLs:\n" + "\n".join(urls)
    )