# test_final_state.py

"""
Pytest suite to validate the final state after the storage audit security scan task.

This test checks:
- The presence and correct content of /home/user/storage_audit/security_scan.log.
- Only files larger than 10MB are logged.
- Each entry is correctly formatted and accurate according to file contents.
"""

import os
import re
import pytest

AUDIT_DIR = "/home/user/storage_audit"
SUBDIR1 = os.path.join(AUDIT_DIR, "subdir1")
SUBDIR2 = os.path.join(AUDIT_DIR, "subdir2")
LOG_PATH = os.path.join(AUDIT_DIR, "security_scan.log")

LARGE_FILES_TRUTH = {
    os.path.join(SUBDIR1, "largefile1.bin"): {
        "status": "OK",
        "details": "No sensitive keywords found."
    },
    os.path.join(SUBDIR2, "largefile2.txt"): {
        "status": "ALERT",
        "details": "Keyword 'password' found on line 53"
    },
    os.path.join(SUBDIR2, "largefile3.dat"): {
        "status": "ALERT",
        "details": "Keyword 'password' found on line 1"
    },
}

NOT_LOGGED_FILES = [
    os.path.join(AUDIT_DIR, "smallfile.txt"),
    os.path.join(AUDIT_DIR, "unrelatedfile.log"),
]

def parse_log_line(line):
    """
    Parse a log line into (path, status, details).
    Expected format:
    /abs/path/to/file: OK No sensitive keywords found.
    /abs/path/to/file: ALERT Keyword 'password' found on line X
    """
    # Colon after filename, status, then the rest is details
    m = re.match(r"^(.+): (OK|ALERT) (.+)$", line.strip())
    if not m:
        return None
    path, status, details = m.group(1), m.group(2), m.group(3)
    return path, status, details

def test_log_file_exists():
    """The security_scan.log file must exist in the audit directory."""
    assert os.path.isfile(LOG_PATH), (
        f"Expected log file {LOG_PATH} does not exist. "
        "The audit script did not create the log file as required."
    )

def test_log_file_permissions():
    """The log file should be readable and not world-writable."""
    st = os.stat(LOG_PATH)
    # Readable by owner
    assert st.st_mode & 0o400, (
        f"Log file {LOG_PATH} is not readable by owner."
    )
    # Should not be world-writable
    assert not (st.st_mode & 0o002), (
        f"Log file {LOG_PATH} is world-writable, which is insecure."
    )

def test_log_file_content_exact():
    """The log must contain exactly the correct entries, and nothing else."""
    with open(LOG_PATH, encoding="utf-8", errors="replace") as f:
        lines = [line.rstrip('\n') for line in f if line.strip()]

    seen_files = set()
    errors = []

    # Parse and check each log line
    for line in lines:
        parsed = parse_log_line(line)
        if not parsed:
            errors.append(
                f"Log line is not in the correct format: {line!r}. "
                "Expected: [absolute-path]: [OK|ALERT] [details]"
            )
            continue
        path, status, details = parsed

        # File must be one of the expected large files
        if path not in LARGE_FILES_TRUTH:
            errors.append(
                f"Log contains unexpected file {path!r}. "
                "Only files larger than 10MB under /home/user/storage_audit/ should be present."
            )
            continue

        # File should not be repeated
        if path in seen_files:
            errors.append(
                f"File {path!r} appears multiple times in the log."
            )
            continue
        seen_files.add(path)

        # Status and details must match truth
        true_status = LARGE_FILES_TRUTH[path]["status"]
        true_details = LARGE_FILES_TRUTH[path]["details"]
        if status != true_status:
            errors.append(
                f"Incorrect status for {path!r}: found '{status}', expected '{true_status}'."
            )
        if details != true_details:
            errors.append(
                f"Incorrect details for {path!r}: found '{details}', expected '{true_details}'."
            )

    # All expected files must be present
    missing = set(LARGE_FILES_TRUTH.keys()) - seen_files
    if missing:
        errors.append(
            "Log file is missing entries for the following required large files:\n"
            + "\n".join(sorted(missing))
        )

    # No extra lines allowed (those would have been caught as unexpected files)
    # No entries for small or unrelated files
    for not_logged in NOT_LOGGED_FILES:
        for line in lines:
            if not_logged in line:
                errors.append(
                    f"Log file contains entry for {not_logged!r}, "
                    "but it should NOT be present (file is too small or unrelated)."
                )

    if errors:
        pytest.fail(
            "security_scan.log has the following problems:\n" +
            "\n".join(errors)
        )

def test_log_line_formatting():
    """Each log line must strictly match the required format."""
    with open(LOG_PATH, encoding="utf-8", errors="replace") as f:
        lines = [line.rstrip('\n') for line in f if line.strip()]
    for line in lines:
        parsed = parse_log_line(line)
        assert parsed is not None, (
            f"Line in log file has invalid format: {line!r}.\n"
            "Expected format:\n"
            "[absolute-path]: [OK|ALERT] [details]"
        )
        path, status, details = parsed
        # Path must be absolute
        assert path.startswith("/"), (
            f"Log file entry path is not absolute: {path!r}."
        )
        # Status must be OK or ALERT
        assert status in ("OK", "ALERT"), (
            f"Status in log line must be 'OK' or 'ALERT', found: {status!r}."
        )
        # Details must match expected for that file
        if path in LARGE_FILES_TRUTH:
            expected_details = LARGE_FILES_TRUTH[path]["details"]
            assert details == expected_details, (
                f"Details in log for {path!r} do not match expected.\n"
                f"Found: {details!r}\nExpected: {expected_details!r}"
            )

def test_log_file_line_endings():
    """Log file must use LF line endings only."""
    with open(LOG_PATH, "rb") as f:
        content = f.read()
    assert b"\r" not in content, (
        "Log file contains CR or CRLF line endings. Only LF ('\\n') is allowed."
    )

def test_log_file_no_extra_entries():
    """Log file must not contain entries for small or unrelated files."""
    with open(LOG_PATH, encoding="utf-8", errors="replace") as f:
        log_content = f.read()
    for not_logged in NOT_LOGGED_FILES:
        assert not_logged not in log_content, (
            f"Log file contains entry for {not_logged!r}, "
            "but it should not be present (file is too small or unrelated)."
        )