# test_final_state.py

import os
import pytest

HOME = "/home/user"
LOGS_DIR = os.path.join(HOME, "app", "logs")
SUMMARY_PATH = os.path.join(HOME, "error_log_summary.txt")

def rel_path(absolute_path):
    """Return the path relative to /home/user/app/logs."""
    return os.path.relpath(absolute_path, LOGS_DIR)

def test_summary_file_exists():
    assert os.path.isfile(SUMMARY_PATH), (
        f"Summary file is missing: {SUMMARY_PATH}"
    )

def test_summary_file_contents_exact():
    """
    The summary file must contain ONLY the expected lines, in any order.
    """
    expected_lines = {
        "server1/server.log ERROR_COUNT:3",
        "api/debug.log ERROR_COUNT:0",
        "app.log ERROR_COUNT:2",
    }

    with open(SUMMARY_PATH, encoding="utf-8") as f:
        actual_lines = set(line.rstrip('\r\n') for line in f if line.strip() != "")

    missing = expected_lines - actual_lines
    extra = actual_lines - expected_lines

    assert not missing, (
        f"Summary file is missing the following line(s):\n" +
        "\n".join(sorted(missing))
    )
    assert not extra, (
        f"Summary file contains unexpected extra line(s):\n" +
        "\n".join(sorted(extra))
    )

def test_summary_file_no_extra_content():
    """
    The summary file must not contain blank lines or lines not matching the format.
    """
    with open(SUMMARY_PATH, encoding="utf-8") as f:
        lines = [line.rstrip('\r\n') for line in f]
    for line in lines:
        if line.strip() == "":
            pytest.fail("Summary file contains a blank line.")
        # Should match the format: <rel-path> ERROR_COUNT:<int>
        if " ERROR_COUNT:" not in line:
            pytest.fail(f"Summary file contains line not matching required format: {line}")
        rel, count = line.split(" ERROR_COUNT:", 1)
        assert rel, (
            f"Summary file line does not have a relative path before ERROR_COUNT: {line}"
        )
        try:
            c = int(count)
        except Exception:
            pytest.fail(f"Summary file line does not have integer error count: {line}")
        assert c >= 0, f"Summary file line has negative error count: {line}"

def test_summary_file_only_expected_files():
    """
    The summary file must not contain files that:
      - Do not end with .log
      - Are not under /home/user/app/logs
      - Are not older than 7 days
    """
    # The only eligible files (older than 7 days and .log) are:
    eligible = {
        "server1/server.log",
        "api/debug.log",
        "app.log",
    }
    with open(SUMMARY_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rel = line.split(" ERROR_COUNT:", 1)[0]
            assert rel in eligible, (
                f"Summary file lists a file that should NOT be included: {rel}"
            )

def test_summary_file_relative_paths():
    """
    Paths in the summary file must be strictly relative to /home/user/app/logs.
    """
    with open(SUMMARY_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rel = line.split(" ERROR_COUNT:", 1)[0]
            assert not rel.startswith("/"), (
                f"Summary file path is not relative: {rel}"
            )
            # Must not contain '..'
            assert ".." not in rel, (
                f"Summary file path must not traverse upwards: {rel}"
            )
            # Must point to a .log file under LOGS_DIR
            abs_path = os.path.join(LOGS_DIR, rel)
            assert abs_path.startswith(LOGS_DIR), (
                f"Summary file path does not resolve inside logs dir: {rel}"
            )
            assert abs_path.endswith(".log"), (
                f"Summary file path does not end with .log: {rel}"
            )
            assert os.path.isfile(abs_path), (
                f"Summary file path does not exist as a file: {abs_path}"
            )

def test_summary_file_error_counts_precise():
    """
    The error counts in the summary file must match the actual number of lines
    containing 'ERROR' (case-sensitive) in the corresponding file.
    """
    # Ground truth for each eligible file
    ground_truth = {
        "server1/server.log": 3,
        "api/debug.log": 0,
        "app.log": 2,
    }
    with open(SUMMARY_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rel, rest = line.split(" ERROR_COUNT:", 1)
            expected_count = ground_truth[rel]
            try:
                actual_count = int(rest)
            except Exception:
                pytest.fail(f"Summary file line does not have integer error count: {line}")
            assert actual_count == expected_count, (
                f"ERROR count for {rel} is {actual_count}, expected {expected_count}"
            )

def test_summary_file_is_not_empty():
    """
    Since there are eligible log files, summary file must not be empty.
    """
    size = os.stat(SUMMARY_PATH).st_size
    assert size > 0, (
        "Summary file is empty, but should contain lines for eligible .log files."
    )

def test_non_eligible_files_not_included():
    """
    Files that do not end with .log or are not older than 7 days MUST NOT be present.
    """
    ineligible = {
        "server2/current.log",  # only 3 days old
        "README.txt",           # not a .log file
    }
    with open(SUMMARY_PATH, encoding="utf-8") as f:
        contents = f.read()
    for bad in ineligible:
        assert bad not in contents, (
            f"Summary file must NOT mention ineligible file: {bad}"
        )