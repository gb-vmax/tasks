# test_final_state.py

import os
import stat
import pwd
import grp
import pytest

SEC_AUDIT_DIR = '/home/user/security_audit'
REPORT_PATH = '/home/user/permission_audit_report.txt'

# The "truth" about the files in /home/user/security_audit/
EXPECTED_FILES = {
    'readme.txt': {
        'mode': 0o100644,
        'owner': 'user',
        'group': 'user',
    },
    'report.log': {
        'mode': 0o100600,
        'owner': 'user',
        'group': 'user',
    },
    'confidential.md': {
        'mode': 0o100400,
        'owner': 'user',
        'group': 'user',
    },
}

EXPECTED_REPORT_LINES = {
    '-rw-r--r-- user user readme.txt',
    '-rw------- user user report.log',
    '-r-------- user user confidential.md',
}

def get_symbolic_permissions(mode):
    """Return the symbolic permissions string for a file mode."""
    return stat.filemode(mode)

def get_file_report_line(path, filename):
    """Return the report line for a given file as specified."""
    st = os.stat(path)
    perms = get_symbolic_permissions(st.st_mode)
    owner = pwd.getpwuid(st.st_uid).pw_name
    group = grp.getgrgid(st.st_gid).gr_name
    return f"{perms} {owner} {group} {filename}"

@pytest.mark.describe("Final state: permission_audit_report.txt exists with correct contents")
def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Expected report file does not exist: {REPORT_PATH}"
    )

@pytest.mark.describe("Final state: permission_audit_report.txt content and format")
def test_report_file_contents():
    assert os.path.isfile(REPORT_PATH), (
        f"Expected report file does not exist: {REPORT_PATH}"
    )
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip('\n') for line in f]

    # Check for blank lines or extra whitespace
    for idx, line in enumerate(lines):
        assert line.strip() == line, (
            f"Line {idx+1} in report file has leading/trailing whitespace: '{line}'"
        )
        assert line, (
            f"Line {idx+1} in report file is blank"
        )

    # Check the set of lines matches exactly
    actual_lines = set(lines)
    missing = EXPECTED_REPORT_LINES - actual_lines
    extra = actual_lines - EXPECTED_REPORT_LINES
    assert not missing, (
        f"Report is missing expected lines: {sorted(missing)}"
    )
    assert not extra, (
        f"Report contains unexpected lines: {sorted(extra)}"
    )
    assert len(lines) == len(EXPECTED_REPORT_LINES), (
        f"Report file should have {len(EXPECTED_REPORT_LINES)} lines, found {len(lines)}"
    )

    # Check line format: [PERMISSIONS] [OWNER] [GROUP] [FILENAME]
    for idx, line in enumerate(lines):
        parts = line.split()
        assert len(parts) >= 4, (
            f"Line {idx+1} does not have at least 4 fields: '{line}'"
        )
        perms, owner, group = parts[0], parts[1], parts[2]
        filename = ' '.join(parts[3:])
        # Permissions string should be 10 chars and start with "-"
        assert len(perms) == 10 and perms[0] == '-', (
            f"Line {idx+1}: Permissions string '{perms}' is not valid (should be like '-rw-r--r--')"
        )
        # Owner and group should be 'user'
        assert owner == 'user', (
            f"Line {idx+1}: Owner should be 'user', got '{owner}'"
        )
        assert group == 'user', (
            f"Line {idx+1}: Group should be 'user', got '{group}'"
        )
        # Filename should be one of the expected files
        assert filename in EXPECTED_FILES, (
            f"Line {idx+1}: Filename '{filename}' is not expected"
        )

@pytest.mark.describe("Final state: Report only lists files directly in /home/user/security_audit/")
def test_report_does_not_list_directories_or_subdir_files():
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip('\n') for line in f]
    reported_filenames = set(line.split(None, 3)[-1] for line in lines)
    # Only expected filenames should appear
    expected_filenames = set(EXPECTED_FILES.keys())
    extra = reported_filenames - expected_filenames
    missing = expected_filenames - reported_filenames
    assert not extra, (
        f"Report lists unexpected file(s): {sorted(extra)}"
    )
    assert not missing, (
        f"Report missing expected file(s): {sorted(missing)}"
    )

@pytest.mark.describe("Final state: No directories listed in the report")
def test_report_has_no_directories():
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip('\n') for line in f]
    for idx, line in enumerate(lines):
        perms = line.split()[0]
        assert perms[0] == '-', (
            f"Line {idx+1}: Report includes a non-regular file (permissions: '{perms}'), should only include regular files"
        )

@pytest.mark.describe("Final state: Report permissions/ownership matches actual files")
def test_report_matches_actual_file_state():
    with open(REPORT_PATH, "r") as f:
        lines = [line.rstrip('\n') for line in f]
    for idx, line in enumerate(lines):
        parts = line.split()
        perms, owner, group = parts[0], parts[1], parts[2]
        filename = ' '.join(parts[3:])
        file_path = os.path.join(SEC_AUDIT_DIR, filename)
        assert os.path.isfile(file_path), (
            f"Line {idx+1}: File '{file_path}' listed in report but does not exist"
        )
        st = os.stat(file_path)
        actual_perms = stat.filemode(st.st_mode)
        actual_owner = pwd.getpwuid(st.st_uid).pw_name
        actual_group = grp.getgrgid(st.st_gid).gr_name
        assert perms == actual_perms, (
            f"Line {idx+1}: Permissions for '{filename}' in report ('{perms}') do not match actual ('{actual_perms}')"
        )
        assert owner == actual_owner, (
            f"Line {idx+1}: Owner for '{filename}' in report ('{owner}') does not match actual ('{actual_owner}')"
        )
        assert group == actual_group, (
            f"Line {idx+1}: Group for '{filename}' in report ('{group}') does not match actual ('{actual_group}')"
        )