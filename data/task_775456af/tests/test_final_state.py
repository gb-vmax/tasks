# test_final_state.py

import os
import stat
import pytest

ACCESS_LOG = "/home/user/logs/access.log"
DIAG_DIR = "/home/user/diagnostics"
UNIQUE_IPS = os.path.join(DIAG_DIR, "unique_ips.txt")
HTTP_STATUS_COUNT = os.path.join(DIAG_DIR, "http_status_count.txt")

EXPECTED_UNIQUE_IPS = (
    "10.0.0.5\n"
    "10.0.0.7\n"
    "192.168.1.10\n"
    "192.168.1.11\n"
    "192.168.1.20\n"
)

EXPECTED_ACCESS_LOG = (
    '192.168.1.10 - - [01/Apr/2024:10:01:23 +0000] "GET /index.html HTTP/1.1" 200 532\n'
    '192.168.1.11 - - [01/Apr/2024:10:02:17 +0000] "GET /logo.png HTTP/1.1" NOT_FOUND 102\n'
    '10.0.0.5 - - [01/Apr/2024:10:03:11 +0000] "POST /submit HTTP/1.1" 500 12\n'
    '192.168.1.10 - - [01/Apr/2024:10:05:44 +0000] "GET /contact HTTP/1.1" NOT_FOUND 102\n'
    '10.0.0.7 - - [01/Apr/2024:10:06:50 +0000] "GET /about HTTP/1.1" 200 198\n'
    '192.168.1.20 - - [01/Apr/2024:10:08:02 +0000] "GET /index.html HTTP/1.1" 301 68\n'
    '192.168.1.11 - - [01/Apr/2024:10:09:33 +0000] "GET /missing HTTP/1.1" NOT_FOUND 102\n'
    '10.0.0.5 - - [01/Apr/2024:10:12:18 +0000] "GET /error HTTP/1.1" 500 12\n'
)

EXPECTED_HTTP_STATUS_COUNT = (
    "200: 2\n"
    "301: 1\n"
    "500: 2\n"
    "NOT_FOUND: 3\n"
)

@pytest.mark.describe("Final state after all diagnostics tasks are completed")
class TestFinalState:

    def test_unique_ips_file_exists_and_correct(self):
        """unique_ips.txt exists, has correct sorted unique IPs, UNIX line endings only, and nothing else."""
        assert os.path.isfile(UNIQUE_IPS), (
            f"Missing required output file: {UNIQUE_IPS}"
        )
        with open(UNIQUE_IPS, "rb") as f:
            content_bytes = f.read()
        # Check for CR (no CRLF allowed)
        assert b'\r' not in content_bytes, (
            f"{UNIQUE_IPS} contains non-UNIX line endings (CR detected)"
        )
        # File must end with LF
        assert content_bytes.endswith(b'\n'), (
            f"{UNIQUE_IPS} does not end with UNIX line ending (LF)"
        )
        content_str = content_bytes.decode('utf-8')
        assert content_str == EXPECTED_UNIQUE_IPS, (
            f"{UNIQUE_IPS} does not have the expected unique, sorted IP addresses.\n"
            f"Expected:\n{repr(EXPECTED_UNIQUE_IPS)}\n"
            f"Found:\n{repr(content_str)}"
        )

    def test_access_log_inplace_404_replacement(self):
        """access.log should have all '404' replaced with 'NOT_FOUND', nothing else changed, UNIX line endings preserved."""
        assert os.path.isfile(ACCESS_LOG), (
            f"Missing required log file: {ACCESS_LOG}"
        )
        with open(ACCESS_LOG, "rb") as f:
            content_bytes = f.read()
        # No CR (no CRLF allowed)
        assert b'\r' not in content_bytes, (
            f"{ACCESS_LOG} contains non-UNIX line endings (CR detected)"
        )
        # File must end with LF
        assert content_bytes.endswith(b'\n'), (
            f"{ACCESS_LOG} does not end with UNIX line ending (LF)"
        )
        content_str = content_bytes.decode('utf-8')
        assert content_str == EXPECTED_ACCESS_LOG, (
            f"{ACCESS_LOG} does not match expected contents after 404 replacement.\n"
            f"Expected:\n{repr(EXPECTED_ACCESS_LOG)}\n"
            f"Found:\n{repr(content_str)}\n"
            "Check that only '404' status codes are replaced with 'NOT_FOUND', and all other content is unchanged."
        )

    def test_http_status_count_file_exists_and_correct(self):
        """http_status_count.txt exists, has correct status/count summary, sorted, UNIX line endings only, and nothing else."""
        assert os.path.isfile(HTTP_STATUS_COUNT), (
            f"Missing required output file: {HTTP_STATUS_COUNT}"
        )
        with open(HTTP_STATUS_COUNT, "rb") as f:
            content_bytes = f.read()
        # No CR (no CRLF allowed)
        assert b'\r' not in content_bytes, (
            f"{HTTP_STATUS_COUNT} contains non-UNIX line endings (CR detected)"
        )
        # File must end with LF
        assert content_bytes.endswith(b'\n'), (
            f"{HTTP_STATUS_COUNT} does not end with UNIX line ending (LF)"
        )
        content_str = content_bytes.decode('utf-8')
        assert content_str == EXPECTED_HTTP_STATUS_COUNT, (
            f"{HTTP_STATUS_COUNT} does not have the expected status code/count summary.\n"
            f"Expected:\n{repr(EXPECTED_HTTP_STATUS_COUNT)}\n"
            f"Found:\n{repr(content_str)}\n"
            "Check that the file lists each unique status code (including 'NOT_FOUND'), with correct counts, "
            "in the required format and sorted order."
        )

    def test_no_extra_files_created(self):
        """No extra files should be present in /home/user/diagnostics."""
        expected_files = {"unique_ips.txt", "http_status_count.txt"}
        actual_files = set(os.listdir(DIAG_DIR))
        extra = actual_files - expected_files
        missing = expected_files - actual_files
        assert not missing, (
            f"Missing expected diagnostics files: {missing}"
        )
        assert not extra, (
            f"Unexpected extra files in diagnostics directory: {extra}"
        )

    def test_permissions_preserved(self):
        """Check that permissions for diagnostics files and access.log are at least readable by user."""
        # Check access.log
        st_log = os.stat(ACCESS_LOG)
        assert st_log.st_mode & stat.S_IRUSR, (
            f"{ACCESS_LOG} is not readable by user after modification"
        )
        # Check diagnostics files
        for f in [UNIQUE_IPS, HTTP_STATUS_COUNT]:
            st = os.stat(f)
            assert st.st_mode & stat.S_IRUSR, (
                f"{f} is not readable by user"
            )