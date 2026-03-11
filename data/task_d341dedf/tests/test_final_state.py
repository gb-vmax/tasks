# test_final_state.py

import os
import pytest

REPORT_FILE = "/home/user/containers/report.txt"
STATS_FILE = "/home/user/containers/stats.txt"

EXPECTED_REPORT_CONTENT = (
    "Container Memory Optimization Report\n"
    "=====================================\n"
    "Top memory consumer: order-service\n"
    "Memory usage: 410MiB / 512MiB\n"
    "Memory percent: 80.08%\n"
    "Recommendation: ACTION REQUIRED: Increase memory limit or scale horizontally.\n"
)


def test_report_file_exists():
    """The report.txt file must exist at /home/user/containers/report.txt."""
    assert os.path.isfile(REPORT_FILE), (
        f"Report file {REPORT_FILE} does not exist. "
        "The task requires creating this file."
    )


def test_report_file_is_readable():
    """The report.txt file must be readable."""
    assert os.access(REPORT_FILE, os.R_OK), (
        f"Report file {REPORT_FILE} exists but is not readable."
    )


def test_report_file_exact_content():
    """The report.txt file must contain exactly the expected content."""
    with open(REPORT_FILE, "r") as f:
        actual_content = f.read()

    assert actual_content == EXPECTED_REPORT_CONTENT, (
        f"Content of {REPORT_FILE} does not match expected.\n"
        f"Expected:\n{EXPECTED_REPORT_CONTENT!r}\n"
        f"Actual:\n{actual_content!r}"
    )


def test_report_file_header_line():
    """The report must start with 'Container Memory Optimization Report'."""
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 1, (
        f"Report file {REPORT_FILE} is empty."
    )
    assert lines[0].rstrip("\n") == "Container Memory Optimization Report", (
        f"First line of report is wrong.\n"
        f"Expected: 'Container Memory Optimization Report'\n"
        f"Got: {lines[0]!r}"
    )


def test_report_file_separator_line():
    """The report must have '=====================================' as the second line."""
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 2, (
        f"Report file {REPORT_FILE} has fewer than 2 lines."
    )
    assert lines[1].rstrip("\n") == "=====================================", (
        f"Second line of report is wrong.\n"
        f"Expected: '====================================='\n"
        f"Got: {lines[1]!r}"
    )


def test_report_file_top_memory_consumer():
    """The report must identify order-service as the top memory consumer."""
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 3, (
        f"Report file {REPORT_FILE} has fewer than 3 lines."
    )
    assert lines[2].rstrip("\n") == "Top memory consumer: order-service", (
        f"Third line of report is wrong.\n"
        f"Expected: 'Top memory consumer: order-service'\n"
        f"Got: {lines[2]!r}"
    )


def test_report_file_memory_usage():
    """The report must show '410MiB / 512MiB' as memory usage for order-service."""
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 4, (
        f"Report file {REPORT_FILE} has fewer than 4 lines."
    )
    assert lines[3].rstrip("\n") == "Memory usage: 410MiB / 512MiB", (
        f"Fourth line of report is wrong.\n"
        f"Expected: 'Memory usage: 410MiB / 512MiB'\n"
        f"Got: {lines[3]!r}"
    )


def test_report_file_memory_percent():
    """The report must show '80.08%' as the memory percent."""
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 5, (
        f"Report file {REPORT_FILE} has fewer than 5 lines."
    )
    assert lines[4].rstrip("\n") == "Memory percent: 80.08%", (
        f"Fifth line of report is wrong.\n"
        f"Expected: 'Memory percent: 80.08%'\n"
        f"Got: {lines[4]!r}"
    )


def test_report_file_recommendation():
    """The report must have 'ACTION REQUIRED' recommendation since MEM% >= 80."""
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 6, (
        f"Report file {REPORT_FILE} has fewer than 6 lines."
    )
    expected_rec = "Recommendation: ACTION REQUIRED: Increase memory limit or scale horizontally."
    assert lines[5].rstrip("\n") == expected_rec, (
        f"Sixth line of report is wrong.\n"
        f"Expected: {expected_rec!r}\n"
        f"Got: {lines[5]!r}"
    )


def test_report_file_line_count():
    """The report must have exactly 6 lines (with a trailing newline after the last)."""
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    lines = content.split("\n")
    # With exactly one trailing newline, split gives 7 elements where last is ''
    assert len(lines) == 7 and lines[-1] == "", (
        f"Report file must have exactly 6 lines followed by a single newline.\n"
        f"Got {len(lines) - 1} lines (split result: {lines!r})\n"
        f"Full content: {content!r}"
    )


def test_report_file_ends_with_single_newline():
    """The report file must end with exactly one newline character."""
    with open(REPORT_FILE, "rb") as f:
        content = f.read()

    assert content.endswith(b"\n"), (
        f"Report file {REPORT_FILE} does not end with a newline.\n"
        f"Last 10 bytes: {content[-10:]!r}"
    )
    assert not content.endswith(b"\n\n"), (
        f"Report file {REPORT_FILE} ends with more than one newline.\n"
        f"Last 10 bytes: {content[-10:]!r}"
    )


def test_report_file_no_trailing_whitespace():
    """No line in the report file must have trailing whitespace."""
    with open(REPORT_FILE, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} of report file has trailing whitespace.\n"
            f"Got: {line!r}"
        )


def test_stats_file_unchanged():
    """The stats.txt file must remain unchanged after the task is completed."""
    expected_content = (
        "CONTAINER_ID   NAME              CPU%    MEM_USAGE/LIMIT       MEM%    NET_I/O         BLOCK_I/O\n"
        "a1b2c3d4e5f6   api-gateway       12.34%  256MiB / 512MiB       50.00%  1.2MB / 800kB   45MB / 12MB\n"
        "b2c3d4e5f6a7   auth-service      3.10%   180MiB / 512MiB       35.16%  500kB / 200kB   10MB / 4MB\n"
        "c3d4e5f6a7b8   payment-service   45.67%  748MiB / 1GiB         73.05%  8.3MB / 5.1MB   200MB / 90MB\n"
        "d4e5f6a7b8c9   user-service      8.90%   95MiB / 512MiB        18.55%  300kB / 100kB   5MB / 2MB\n"
        "e5f6a7b8c9d0   order-service     22.11%  410MiB / 512MiB       80.08%  3.4MB / 2.1MB   80MB / 30MB\n"
        "f6a7b8c9d0e1   notification-svc  1.05%   60MiB / 256MiB        23.44%  100kB / 50kB    2MB / 1MB\n"
    )

    assert os.path.isfile(STATS_FILE), (
        f"Stats file {STATS_FILE} no longer exists after the task was completed."
    )

    with open(STATS_FILE, "r") as f:
        actual_content = f.read()

    assert actual_content.rstrip("\n") == expected_content.rstrip("\n"), (
        f"Stats file {STATS_FILE} was modified during the task.\n"
        f"Expected:\n{expected_content!r}\n"
        f"Actual:\n{actual_content!r}"
    )