# test_final_state.py

import os
import pytest

API_404S_LOG = "/home/user/logs/api_404s.log"
API_404_SUMMARY = "/home/user/logs/api_404_summary.txt"

EXPECTED_API_404_LINES = [
    '192.168.1.10 - - [15/Mar/2024:10:01:00 +0000] "GET /api/users HTTP/1.1" 404 152 "-" "Mozilla/5.0"',
    '192.168.1.10 - - [15/Mar/2024:10:01:10 +0000] "POST /api/orders HTTP/1.1" 404 148 "-" "Mozilla/5.0"',
    '10.0.0.5 - - [15/Mar/2024:10:01:25 +0000] "DELETE /api/users/42 HTTP/1.1" 404 140 "-" "curl/7.68.0"',
    '192.168.1.20 - - [15/Mar/2024:10:01:35 +0000] "GET /api/orders HTTP/1.1" 404 148 "-" "Mozilla/5.0"',
    '10.0.0.9 - - [15/Mar/2024:10:01:45 +0000] "GET /api/inventory HTTP/1.1" 404 155 "-" "Mozilla/5.0"',
]

EXPECTED_SUMMARY = "Total 404s on /api/: 5\nUnique IPs: 4"


# ---------------------------------------------------------------------------
# api_404s.log tests
# ---------------------------------------------------------------------------

def test_api_404s_log_exists():
    assert os.path.isfile(API_404S_LOG), (
        f"File '{API_404S_LOG}' does not exist. "
        "The student's solution must create this file."
    )


def test_api_404s_log_is_readable():
    assert os.access(API_404S_LOG, os.R_OK), (
        f"File '{API_404S_LOG}' exists but is not readable."
    )


def test_api_404s_log_line_count():
    with open(API_404S_LOG, "r") as f:
        content = f.read()

    # Strip a single trailing newline if present, then split
    lines = content.rstrip("\n").split("\n")
    # Handle the edge case of an empty file
    if lines == [""]:
        lines = []

    assert len(lines) == len(EXPECTED_API_404_LINES), (
        f"'{API_404S_LOG}' has {len(lines)} line(s), expected {len(EXPECTED_API_404_LINES)}.\n"
        f"Actual lines:\n" + "\n".join(repr(l) for l in lines)
    )


def test_api_404s_log_line_content_and_order():
    with open(API_404S_LOG, "r") as f:
        content = f.read()

    lines = content.rstrip("\n").split("\n")
    if lines == [""]:
        lines = []

    for i, (actual, expected) in enumerate(zip(lines, EXPECTED_API_404_LINES), start=1):
        assert actual == expected, (
            f"Line {i} of '{API_404S_LOG}' does not match expected.\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}"
        )


def test_api_404s_log_no_extra_lines():
    """Ensure no non-matching lines crept into the filtered output."""
    with open(API_404S_LOG, "r") as f:
        content = f.read()

    lines = content.rstrip("\n").split("\n")
    if lines == [""]:
        lines = []

    lines_set = set(lines)
    expected_set = set(EXPECTED_API_404_LINES)

    extra_lines = lines_set - expected_set
    assert not extra_lines, (
        f"'{API_404S_LOG}' contains unexpected lines that should not be present:\n"
        + "\n".join(repr(l) for l in sorted(extra_lines))
    )


def test_api_404s_log_excludes_non_api_404():
    """Non-/api/ 404 line must not appear."""
    non_api_404 = '10.0.0.7 - - [15/Mar/2024:10:01:20 +0000] "GET /static/style.css HTTP/1.1" 404 98 "-" "Mozilla/5.0"'
    with open(API_404S_LOG, "r") as f:
        content = f.read()
    assert non_api_404 not in content, (
        f"Non-/api/ 404 line was incorrectly included in '{API_404S_LOG}':\n  {non_api_404!r}"
    )


def test_api_404s_log_excludes_api_non_404():
    """Lines with /api/ path but status != 404 must not appear."""
    non_404_api_lines = [
        '10.0.0.5 - - [15/Mar/2024:10:01:15 +0000] "GET /api/products HTTP/1.1" 200 1024 "-" "Mozilla/5.0"',
        '192.168.1.30 - - [15/Mar/2024:10:01:30 +0000] "GET /api/users HTTP/1.1" 500 200 "-" "Mozilla/5.0"',
        '192.168.1.10 - - [15/Mar/2024:10:01:40 +0000] "PUT /api/settings HTTP/1.1" 200 300 "-" "curl/7.68.0"',
    ]
    with open(API_404S_LOG, "r") as f:
        content = f.read()
    for line in non_404_api_lines:
        assert line not in content, (
            f"Line with /api/ path but non-404 status was incorrectly included in '{API_404S_LOG}':\n  {line!r}"
        )


def test_api_404s_log_excludes_non_api_non_404():
    """Lines that are neither /api/ nor 404 must not appear."""
    irrelevant_line = '192.168.1.20 - - [15/Mar/2024:10:01:05 +0000] "GET /index.html HTTP/1.1" 200 512 "-" "curl/7.68.0"'
    with open(API_404S_LOG, "r") as f:
        content = f.read()
    assert irrelevant_line not in content, (
        f"Irrelevant line was incorrectly included in '{API_404S_LOG}':\n  {irrelevant_line!r}"
    )


# ---------------------------------------------------------------------------
# api_404_summary.txt tests
# ---------------------------------------------------------------------------

def test_api_404_summary_exists():
    assert os.path.isfile(API_404_SUMMARY), (
        f"File '{API_404_SUMMARY}' does not exist. "
        "The student's solution must create this file."
    )


def test_api_404_summary_is_readable():
    assert os.access(API_404_SUMMARY, os.R_OK), (
        f"File '{API_404_SUMMARY}' exists but is not readable."
    )


def test_api_404_summary_exact_content():
    with open(API_404_SUMMARY, "r") as f:
        content = f.read()

    # Strip only a single trailing newline (files often end with one)
    stripped = content.rstrip("\n")

    assert stripped == EXPECTED_SUMMARY, (
        f"Content of '{API_404_SUMMARY}' does not match expected.\n"
        f"  Expected: {EXPECTED_SUMMARY!r}\n"
        f"  Actual:   {stripped!r}"
    )


def test_api_404_summary_total_count_line():
    with open(API_404_SUMMARY, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    assert len(lines) >= 1, (
        f"'{API_404_SUMMARY}' appears to be empty or has too few lines."
    )
    assert lines[0] == "Total 404s on /api/: 5", (
        f"First line of '{API_404_SUMMARY}' is wrong.\n"
        f"  Expected: 'Total 404s on /api/: 5'\n"
        f"  Actual:   {lines[0]!r}"
    )


def test_api_404_summary_unique_ips_line():
    with open(API_404_SUMMARY, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    assert len(lines) >= 2, (
        f"'{API_404_SUMMARY}' has fewer than 2 lines; missing 'Unique IPs' line."
    )
    assert lines[1] == "Unique IPs: 4", (
        f"Second line of '{API_404_SUMMARY}' is wrong.\n"
        f"  Expected: 'Unique IPs: 4'\n"
        f"  Actual:   {lines[1]!r}"
    )


def test_api_404_summary_no_extra_lines():
    with open(API_404_SUMMARY, "r") as f:
        content = f.read()

    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 2, (
        f"'{API_404_SUMMARY}' should have exactly 2 lines, but has {len(lines)}.\n"
        f"Lines: {lines!r}"
    )


def test_api_404_summary_no_trailing_spaces():
    with open(API_404_SUMMARY, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        stripped_line = line.rstrip("\n")
        assert stripped_line == stripped_line.rstrip(), (
            f"Line {i} of '{API_404_SUMMARY}' has trailing whitespace: {stripped_line!r}"
        )