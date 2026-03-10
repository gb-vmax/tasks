# test_final_state.py

import os
import grp
import pwd
import stat
import subprocess
import pytest

REPORTS_DIR = "/home/user/finops/reports"
CSV_FILES = ["q1_budget.csv", "q2_budget.csv", "q3_budget.csv"]

FILE_CONTENTS = {
    "q1_budget.csv": "service,cost\nEC2,1200\nS3,340",
    "q2_budget.csv": "service,cost\nEC2,1500\nRDS,890",
    "q3_budget.csv": "service,cost\nLambda,200\nS3,410",
}


def get_group_name(gid):
    try:
        return grp.getgrgid(gid).gr_name
    except KeyError:
        return str(gid)


def get_owner_name(uid):
    try:
        return pwd.getpwuid(uid).pw_name
    except KeyError:
        return str(uid)


# ── 1. Group membership ──────────────────────────────────────────────────────

def test_analyst_in_finops_group():
    """analyst must be a member of the finops group."""
    try:
        finops_grp = grp.getgrnam("finops")
    except KeyError:
        pytest.fail("Group 'finops' does not exist on the system.")

    # grp.getgrnam reflects /etc/group; also verify via `groups` command
    # so that NSS / getent is consulted as well.
    result = subprocess.run(
        ["groups", "analyst"],
        capture_output=True, text=True
    )
    groups_output = result.stdout.strip()

    # Check both sources
    in_grp_file = "analyst" in finops_grp.gr_mem
    in_cmd_output = "finops" in groups_output.split()

    assert in_grp_file or in_cmd_output, (
        f"User 'analyst' is NOT in group 'finops'.\n"
        f"  /etc/group members: {finops_grp.gr_mem}\n"
        f"  `groups analyst` output: {groups_output!r}\n"
        "Run: usermod -aG finops analyst"
    )


def test_groups_command_includes_finops():
    """The `groups analyst` command output must include 'finops'."""
    result = subprocess.run(
        ["groups", "analyst"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"`groups analyst` failed with return code {result.returncode}.\n"
        f"stderr: {result.stderr.strip()}"
    )
    output = result.stdout.strip()
    # Output format: "analyst : analyst finops"
    # Split on ':' to get the groups portion
    parts = output.split(":")
    if len(parts) >= 2:
        group_list = parts[1].split()
    else:
        group_list = output.split()

    assert "finops" in group_list, (
        f"`groups analyst` output does not contain 'finops'.\n"
        f"  Actual output: {output!r}\n"
        "Run: usermod -aG finops analyst"
    )


# ── 2. Directory existence and ownership ─────────────────────────────────────

def test_reports_directory_exists():
    assert os.path.isdir(REPORTS_DIR), (
        f"Directory '{REPORTS_DIR}' does not exist."
    )


def test_reports_directory_group_is_finops():
    """The group ownership of the reports directory must be 'finops'."""
    st = os.stat(REPORTS_DIR)
    group_name = get_group_name(st.st_gid)
    assert group_name == "finops", (
        f"Directory '{REPORTS_DIR}' has group '{group_name}', expected 'finops'.\n"
        "Run: chown :finops /home/user/finops/reports"
    )


def test_reports_directory_owner_is_user():
    """The owner of the reports directory should remain 'user'."""
    st = os.stat(REPORTS_DIR)
    owner_name = get_owner_name(st.st_uid)
    assert owner_name == "user", (
        f"Directory '{REPORTS_DIR}' is owned by '{owner_name}', expected 'user'."
    )


# ── 3. Directory permissions ──────────────────────────────────────────────────

def test_reports_directory_permissions_750():
    """The reports directory must have permissions 750 (drwxr-x---)."""
    st = os.stat(REPORTS_DIR)
    mode = stat.S_IMODE(st.st_mode)
    assert mode == 0o750, (
        f"Directory '{REPORTS_DIR}' has permissions {oct(mode)}, expected 0o750 (750).\n"
        "Run: chmod 750 /home/user/finops/reports"
    )


# ── 4. CSV files existence, ownership, and permissions ───────────────────────

def test_csv_files_exist():
    for fname in CSV_FILES:
        fpath = os.path.join(REPORTS_DIR, fname)
        assert os.path.isfile(fpath), (
            f"Expected file '{fpath}' does not exist."
        )


def test_csv_files_group_is_finops():
    """Every CSV file must have group ownership 'finops'."""
    for fname in CSV_FILES:
        fpath = os.path.join(REPORTS_DIR, fname)
        st = os.stat(fpath)
        group_name = get_group_name(st.st_gid)
        assert group_name == "finops", (
            f"File '{fpath}' has group '{group_name}', expected 'finops'.\n"
            f"Run: chown :finops {fpath}"
        )


def test_csv_files_owner_is_user():
    """Every CSV file must be owned by 'user'."""
    for fname in CSV_FILES:
        fpath = os.path.join(REPORTS_DIR, fname)
        st = os.stat(fpath)
        owner_name = get_owner_name(st.st_uid)
        assert owner_name == "user", (
            f"File '{fpath}' is owned by '{owner_name}', expected 'user'."
        )


def test_csv_files_permissions_640():
    """Every CSV file must have permissions 640 (-rw-r-----)."""
    for fname in CSV_FILES:
        fpath = os.path.join(REPORTS_DIR, fname)
        st = os.stat(fpath)
        mode = stat.S_IMODE(st.st_mode)
        assert mode == 0o640, (
            f"File '{fpath}' has permissions {oct(mode)}, expected 0o640 (640).\n"
            f"Run: chmod 640 {fpath}"
        )


# ── 5. File contents preserved ───────────────────────────────────────────────

def test_csv_file_contents_preserved():
    """File contents must not have been altered."""
    for fname, expected_content in FILE_CONTENTS.items():
        fpath = os.path.join(REPORTS_DIR, fname)
        # Read as root (tests run as root in this context)
        with open(fpath, "r") as f:
            actual = f.read().rstrip("\n")
        assert actual == expected_content, (
            f"File '{fpath}' has unexpected content.\n"
            f"  Expected: {repr(expected_content)}\n"
            f"  Got:      {repr(actual)}"
        )


# ── 6. No unexpected files ───────────────────────────────────────────────────

def test_only_expected_files_in_reports_dir():
    """No extra files should have been introduced into the reports directory."""
    entries = [
        e for e in os.listdir(REPORTS_DIR)
        if os.path.isfile(os.path.join(REPORTS_DIR, e))
    ]
    extra = set(entries) - set(CSV_FILES)
    assert not extra, (
        f"Unexpected files found in '{REPORTS_DIR}': {extra}"
    )


# ── 7. ls -la output sanity check ────────────────────────────────────────────

def test_ls_la_output_directory_line():
    """`ls -la` on the reports dir must show drwxr-x--- with group finops."""
    result = subprocess.run(
        ["ls", "-la", REPORTS_DIR],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"`ls -la {REPORTS_DIR}` failed.\nstderr: {result.stderr.strip()}"
    )
    output = result.stdout

    # Find the line for the directory itself (starts with 'd' and contains '.')
    dir_line = None
    for line in output.splitlines():
        # The directory entry in `ls -la <dir>` is shown as "."
        parts = line.split()
        if len(parts) >= 9 and parts[-1] == ".":
            dir_line = line
            break

    assert dir_line is not None, (
        f"Could not find the directory entry line ('.') in `ls -la` output:\n{output}"
    )

    assert dir_line.startswith("drwxr-x---"), (
        f"Directory permission string is wrong.\n"
        f"  Expected to start with: 'drwxr-x---'\n"
        f"  Actual line: {dir_line!r}"
    )
    assert "finops" in dir_line, (
        f"Group 'finops' not found in directory entry line.\n"
        f"  Actual line: {dir_line!r}"
    )


def test_ls_la_output_csv_files():
    """`ls -la` on the reports dir must show -rw-r----- with group finops for each CSV."""
    result = subprocess.run(
        ["ls", "-la", REPORTS_DIR],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"`ls -la {REPORTS_DIR}` failed.\nstderr: {result.stderr.strip()}"
    )
    output = result.stdout

    for fname in CSV_FILES:
        file_line = None
        for line in output.splitlines():
            if line.endswith(fname):
                file_line = line
                break

        assert file_line is not None, (
            f"Could not find entry for '{fname}' in `ls -la` output:\n{output}"
        )
        assert file_line.startswith("-rw-r-----"), (
            f"File '{fname}' permission string is wrong.\n"
            f"  Expected to start with: '-rw-r-----'\n"
            f"  Actual line: {file_line!r}"
        )
        assert "finops" in file_line, (
            f"Group 'finops' not found in file entry line for '{fname}'.\n"
            f"  Actual line: {file_line!r}"
        )