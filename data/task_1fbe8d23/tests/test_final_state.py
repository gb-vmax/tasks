# test_final_state.py

import os
import stat
import tarfile
import pytest
import re
from datetime import datetime

HOME = "/home/user"
NETWORK_DIR = os.path.join(HOME, "network")
BACKUP_DIR = os.path.join(NETWORK_DIR, "backup")
PING_OUTPUT = os.path.join(NETWORK_DIR, "ping_output.txt")
TARBALL = os.path.join(BACKUP_DIR, "network_logs.tar.gz")
LOGFILE = os.path.join(BACKUP_DIR, "backup_log.txt")

def _check_file_exists_and_readable(path):
    if not os.path.isfile(path):
        return False, f"File does not exist: {path}"
    # Check user read permission
    st = os.stat(path)
    if not (st.st_mode & stat.S_IRUSR):
        return False, f"File is not readable by user: {path}"
    return True, None

def _check_dir_exists_and_writable(path):
    if not os.path.isdir(path):
        return False, f"Directory does not exist: {path}"
    st = os.stat(path)
    if not (st.st_mode & stat.S_IWUSR):
        return False, f"Directory is not writable by user: {path}"
    return True, None

def _is_valid_iso8601_utc(s):
    # Must match YYYY-MM-DDTHH:MM:SSZ
    try:
        dt = datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
        return True
    except Exception:
        return False

@pytest.mark.parametrize(
    "path,desc",
    [
        (NETWORK_DIR, "network directory"),
        (BACKUP_DIR, "backup directory"),
    ]
)
def test_required_directories_exist_and_writable(path, desc):
    ok, msg = _check_dir_exists_and_writable(path)
    assert ok, msg

@pytest.mark.parametrize(
    "path,desc",
    [
        (PING_OUTPUT, "ping output file"),
        (TARBALL, "network logs tarball"),
        (LOGFILE, "backup log file"),
    ]
)
def test_required_files_exist_and_readable(path, desc):
    ok, msg = _check_file_exists_and_readable(path)
    assert ok, msg

def test_ping_output_format_and_count():
    """
    Validate that ping_output.txt exists, is non-empty, and contains valid output for 'ping -c 5 8.8.8.8'.
    """
    assert os.path.isfile(PING_OUTPUT), f"ping_output.txt does not exist at {PING_OUTPUT}"
    with open(PING_OUTPUT, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
        content = "".join(lines)
    assert len(content.strip()) > 0, "ping_output.txt is empty."

    # Look for at least 5 lines that look like ping replies
    # We'll accept both classic Linux and Busybox/MacOS output formats
    # e.g.:
    # 64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=10.4 ms
    # 64 bytes from 8.8.8.8: icmp_seq=2 ttl=117 time=10.3 ms
    reply_pat = re.compile(r"^(\d+ bytes from|64 bytes from)\s+8\.8\.8\.8.*icmp_seq=\d+.*time=[0-9.]+\s*ms", re.MULTILINE)
    matches = reply_pat.findall(content)
    assert len(matches) == 5, (
        f"ping_output.txt must contain exactly 5 ping replies; found {len(matches)}. "
        "Check that the ping command was run with '-c 5' and output captured correctly."
    )

    # Check summary lines at the end (packet statistics)
    # e.g.:
    # 5 packets transmitted, 5 received, 0% packet loss, time 4006ms
    summary_pat = re.compile(r"(\d+) packets transmitted, (\d+) (packets )?received")
    summary_match = summary_pat.search(content)
    assert summary_match, (
        "ping_output.txt is missing summary statistics at the end (e.g. '5 packets transmitted, 5 received...')."
    )
    tx, rx = int(summary_match.group(1)), int(summary_match.group(2))
    assert tx == 5, f"ping_output.txt should show 5 packets transmitted, found {tx}."
    assert rx >= 0, "ping_output.txt: received packets could not be determined."
    # Optionally, check that 8.8.8.8 appears in every reply
    assert content.count("8.8.8.8") >= 5, "ping_output.txt should contain at least 5 references to 8.8.8.8."

def test_tarball_contains_exactly_ping_output_txt_at_root():
    """
    Validate that the tarball exists, is gzip-compressed, and contains only ping_output.txt at the root.
    """
    assert os.path.isfile(TARBALL), f"Tarball does not exist at {TARBALL}"
    try:
        with tarfile.open(TARBALL, "r:gz") as tar:
            members = tar.getmembers()
            names = [m.name for m in members]
            assert len(names) == 1, (
                f"Tarball should contain exactly one file, found: {names}"
            )
            assert names[0] == "ping_output.txt", (
                f"Tarball must contain only 'ping_output.txt' at root, but found: {names[0]}"
            )
            # Check that it is a regular file
            assert members[0].isfile(), "ping_output.txt in tarball is not a regular file."
            # Optionally, check that file size is >0
            assert members[0].size > 0, "ping_output.txt in tarball is empty."
    except Exception as e:
        pytest.fail(f"Failed to open or inspect tarball: {e}")

def test_log_file_contents_and_format():
    """
    Validate that backup_log.txt exists, contains exactly 2 lines:
    - 'Backup created: network_logs.tar.gz'
    - UTC ISO8601 timestamp ending in 'Z'
    """
    assert os.path.isfile(LOGFILE), f"backup_log.txt does not exist at {LOGFILE}"
    with open(LOGFILE, "r", encoding="utf-8", errors="replace") as f:
        lines = [line.rstrip("\r\n") for line in f.readlines()]
    assert len(lines) == 2, (
        f"backup_log.txt must contain exactly two lines, found {len(lines)} lines."
    )
    assert lines[0] == "Backup created: network_logs.tar.gz", (
        f"First line of backup_log.txt should be exactly 'Backup created: network_logs.tar.gz', "
        f"but got: {lines[0]!r}"
    )
    # Validate timestamp
    ts = lines[1]
    assert ts.endswith("Z"), (
        f"Second line of backup_log.txt should be a UTC ISO8601 timestamp ending in 'Z', but got: {ts!r}"
    )
    assert _is_valid_iso8601_utc(ts), (
        f"Second line of backup_log.txt is not a valid ISO8601 UTC timestamp: {ts!r}"
    )

def test_tarball_mtime_matches_logfile_timestamp():
    """
    The UTC timestamp in the log file should match the tarball creation time (mtime), within a few seconds.
    """
    # Get log file timestamp
    with open(LOGFILE, "r", encoding="utf-8", errors="replace") as f:
        lines = [line.rstrip("\r\n") for line in f.readlines()]
    ts = lines[1]
    log_dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")
    # Get tarball mtime (convert from epoch to UTC)
    tar_stat = os.stat(TARBALL)
    tar_mtime_utc = datetime.utcfromtimestamp(tar_stat.st_mtime)
    # Allow up to 10 seconds difference (filesystem rounding, clock skew, etc.)
    delta = abs((tar_mtime_utc - log_dt).total_seconds())
    assert delta <= 10, (
        f"Timestamp in backup_log.txt ({ts}) and tarball mtime ({tar_mtime_utc.isoformat()}Z) "
        f"differ by more than 10 seconds ({delta:.1f}s)."
    )