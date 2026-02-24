# test_final_state.py

import os
import stat
import pytest
import subprocess
import re
from datetime import datetime

BINMGR_DIR = "/home/user/repos/binmgr"
ARTIFACT_CLIENT_SH = "/home/user/repos/binmgr/artifact_client.sh"
PROCESS_LOG = "/home/user/repos/binmgr/process_log.txt"

# ---------------------
# Helper functions
# ---------------------

def get_user_uid():
    return os.getuid()

def is_user_owned(pid):
    """Return True if process is owned by the current user."""
    try:
        stat_info = os.stat(f"/proc/{pid}")
        return stat_info.st_uid == get_user_uid()
    except Exception:
        return False

def get_process_cmdline(pid):
    try:
        with open(f"/proc/{pid}/cmdline", "rb") as f:
            # cmdline is NUL-separated
            cmd = f.read().replace(b'\x00', b' ').strip()
            return cmd.decode("utf-8")
    except Exception:
        return ""

def find_user_owned_artifact_clients():
    """Return a list of PIDs of user-owned artifact_client.sh processes."""
    pids = []
    proc_root = "/proc"
    if not os.path.isdir(proc_root):
        # Not a Linux system, skip process checks
        return pids
    for pid in os.listdir(proc_root):
        if not pid.isdigit():
            continue
        if not is_user_owned(pid):
            continue
        cmdline = get_process_cmdline(pid)
        # We want the exact command path
        if cmdline.startswith(ARTIFACT_CLIENT_SH):
            pids.append(int(pid))
    return pids

def file_readlines(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

def check_script_content(path):
    expected = [
        "#!/bin/bash",
        'echo "artifact-client running on PID $$"',
        "sleep 120"
    ]
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    # Remove blank lines at end, if any
    while lines and not lines[-1].strip():
        lines.pop()
    return lines == expected

def check_executable(path):
    st = os.stat(path)
    # Check user executable
    return bool(st.st_mode & stat.S_IXUSR)

def parse_log_lines(lines):
    """
    Parse process_log.txt lines.
    Returns:
        entries: list of dicts, each entry is either a START or TERMINATED line.
    """
    start_re = re.compile(
        r"^PID: (\d+) \| CMD: (/home/user/repos/binmgr/artifact_client\.sh) \| START: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})$"
    )
    term_re = re.compile(
        r"^PID: (\d+) \| STATUS: TERMINATED \| END: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})$"
    )
    parsed = []
    for line in lines:
        m = start_re.match(line)
        if m:
            parsed.append({
                "type": "start",
                "pid": int(m.group(1)),
                "cmd": m.group(2),
                "start": m.group(3),
                "line": line,
            })
            continue
        m = term_re.match(line)
        if m:
            parsed.append({
                "type": "terminated",
                "pid": int(m.group(1)),
                "end": m.group(2),
                "line": line,
            })
            continue
        parsed.append({
            "type": "unknown",
            "line": line,
        })
    return parsed

def is_valid_datetime(dtstr):
    try:
        datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")
        return True
    except Exception:
        return False

# ---------------------
# Pytest tests
# ---------------------

def test_binmgr_directory_exists_and_writable():
    assert os.path.isdir(BINMGR_DIR), \
        f"Directory {BINMGR_DIR} does not exist after task completion."
    assert os.access(BINMGR_DIR, os.W_OK), \
        f"Directory {BINMGR_DIR} is not writable by the user."

def test_artifact_client_sh_content_and_permissions():
    assert os.path.isfile(ARTIFACT_CLIENT_SH), \
        f"Script {ARTIFACT_CLIENT_SH} does not exist after task completion."
    # Content exactness
    assert check_script_content(ARTIFACT_CLIENT_SH), (
        f"{ARTIFACT_CLIENT_SH} does not contain the expected content:\n"
        "#!/bin/bash\n"
        'echo \"artifact-client running on PID $$\"\n'
        "sleep 120"
    )
    # Is executable by user
    assert check_executable(ARTIFACT_CLIENT_SH), (
        f"{ARTIFACT_CLIENT_SH} is not marked as executable by the user."
    )

def test_process_log_exists_and_format():
    assert os.path.isfile(PROCESS_LOG), \
        f"Process log {PROCESS_LOG} does not exist after task completion."
    lines = file_readlines(PROCESS_LOG)
    assert len(lines) == 6, (
        f"{PROCESS_LOG} should contain exactly 6 lines (3 START + 3 TERMINATED entries), "
        f"but contains {len(lines)}."
    )
    parsed = parse_log_lines(lines)
    unknowns = [e for e in parsed if e["type"] == "unknown"]
    assert not unknowns, (
        f"{PROCESS_LOG} contains lines with invalid format:\n" +
        "\n".join(e["line"] for e in unknowns)
    )

    # Now check interleaving and consistency
    # Each START immediately followed by its own TERMINATED, for 3 unique PIDs
    pids_seen = set()
    i = 0
    while i < len(parsed):
        entry = parsed[i]
        assert entry["type"] == "start", (
            f"Line {i+1} of {PROCESS_LOG} should be a START entry, but got: {entry['line']}"
        )
        pid = entry["pid"]
        cmd = entry["cmd"]
        start = entry["start"]
        assert cmd == ARTIFACT_CLIENT_SH, (
            f"START entry on line {i+1} has incorrect CMD: '{cmd}', expected '{ARTIFACT_CLIENT_SH}'."
        )
        assert is_valid_datetime(start), (
            f"START entry on line {i+1} has invalid datetime: '{start}'."
        )
        assert pid not in pids_seen, (
            f"PID {pid} appears more than once in START entries."
        )
        pids_seen.add(pid)
        # Check next line is the corresponding TERMINATED entry
        assert i+1 < len(parsed), (
            f"START entry for PID {pid} at line {i+1} is not followed by a TERMINATED entry."
        )
        entry2 = parsed[i+1]
        assert entry2["type"] == "terminated", (
            f"Line {i+2} of {PROCESS_LOG} should be a TERMINATED entry, but got: {entry2['line']}"
        )
        assert entry2["pid"] == pid, (
            f"TERMINATED entry (line {i+2}) for PID {entry2['pid']} does not match preceding START entry PID {pid}."
        )
        assert is_valid_datetime(entry2["end"]), (
            f"TERMINATED entry on line {i+2} has invalid datetime: '{entry2['end']}'."
        )
        i += 2
    assert len(pids_seen) == 3, (
        f"{PROCESS_LOG} should contain entries for exactly 3 unique PIDs, but found: {sorted(pids_seen)}"
    )

def test_no_artifact_client_processes_running_after_cleanup():
    pids = find_user_owned_artifact_clients()
    assert not pids, (
        f"After cleanup, no user-owned processes running '{ARTIFACT_CLIENT_SH}' should remain. "
        f"Found PIDs: {pids}"
    )