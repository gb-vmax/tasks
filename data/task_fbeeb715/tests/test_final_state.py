# test_final_state.py

import os
import stat
import pytest

CREDS_DIR = '/home/user/creds'
USERS_CSV = os.path.join(CREDS_DIR, 'users.csv')
NEW_KEYS_TXT = os.path.join(CREDS_DIR, 'new_keys.txt')
USERS_ROTATED_CSV = os.path.join(CREDS_DIR, 'users_rotated.csv')
ROTATION_LOG = os.path.join(CREDS_DIR, 'rotation_check.log')

EXPECTED_USERS_ROTATED = (
    "user_id,username,email,api_key\n"
    "1,alice,alice@example.com,newkey-ab1\n"
    "2,bob,bob@example.com,newkey-cd2\n"
    "3,charlie,charlie@example.com,newkey-ef3\n"
)

EXPECTED_ROTATION_LOG = (
    "users_rotated.csv exists\n"
    "4 columns in header\n"
    "All api_keys are new\n"
    "Row count: 3\n"
)

EXPECTED_HEADER = "user_id,username,email,api_key"


def read_file_exact(path):
    """Read file and normalize line endings to \n for comparison."""
    with open(path, encoding="utf-8") as f:
        content = f.read()
    return content.replace('\r\n', '\n').replace('\r', '\n')


def test_creds_directory_exists_and_is_writable():
    assert os.path.isdir(CREDS_DIR), f"Directory {CREDS_DIR} does not exist."
    st = os.stat(CREDS_DIR)
    mode = st.st_mode
    is_owner = (st.st_uid == os.getuid())
    if is_owner:
        assert bool(mode & stat.S_IWUSR), f"Directory {CREDS_DIR} exists but is not writable by the user."
    else:
        assert os.access(CREDS_DIR, os.W_OK), f"Directory {CREDS_DIR} exists but is not writable by the user."


def test_users_rotated_csv_exists():
    assert os.path.isfile(USERS_ROTATED_CSV), (
        f"File {USERS_ROTATED_CSV} does not exist. "
        "You must create the rotated credentials file with the correct name and location."
    )


def test_users_rotated_csv_content_and_format():
    # Ensure file exists
    assert os.path.isfile(USERS_ROTATED_CSV), (
        f"File {USERS_ROTATED_CSV} does not exist. "
        "You must create the rotated credentials file with the correct name and location."
    )
    content = read_file_exact(USERS_ROTATED_CSV)
    lines = content.split('\n')
    # Remove any empty last line (from trailing newline)
    if lines and lines[-1] == '':
        lines = lines[:-1]

    # 1. Check line count (1 header + 3 users)
    assert len(lines) == 4, (
        f"{USERS_ROTATED_CSV} should have exactly 4 lines (1 header + 3 users), found {len(lines)} lines."
    )

    # 2. Check header
    header = lines[0]
    assert header == EXPECTED_HEADER, (
        f"Header of {USERS_ROTATED_CSV} is incorrect.\n"
        f"Expected: {EXPECTED_HEADER}\n"
        f"Found:    {header}"
    )
    assert header.count(',') == 3, (
        f"Header should have exactly 4 columns separated by 3 commas, found: {header}"
    )

    # 3. Check each user row
    expected_rows = [
        "1,alice,alice@example.com,newkey-ab1",
        "2,bob,bob@example.com,newkey-cd2",
        "3,charlie,charlie@example.com,newkey-ef3",
    ]
    for idx, expected_row in enumerate(expected_rows, start=1):
        row = lines[idx]
        assert row == expected_row, (
            f"Row {idx} of {USERS_ROTATED_CSV} is incorrect.\n"
            f"Expected: {expected_row}\n"
            f"Found:    {row}"
        )
        # Check for extra spaces
        assert row == row.strip(), (
            f"Row {idx} has leading or trailing whitespace: '{row}'"
        )
        for field in row.split(','):
            assert field == field.strip(), (
                f"Row {idx} has field with leading/trailing whitespace: '{field}'"
            )
        assert row.count(',') == 3, (
            f"Row {idx} should have exactly 4 columns separated by 3 commas, found: {row}"
        )

    # 4. No extra lines
    assert len(lines) == 4, (
        f"{USERS_ROTATED_CSV} has extra lines. Expected 4 lines (1 header + 3 users), found {len(lines)}."
    )


def test_users_rotated_csv_api_keys_are_new_and_in_order():
    """Ensure api_key column comes from new_keys.txt, in order, and no old keys remain."""
    # Get the expected new keys
    with open(NEW_KEYS_TXT, encoding="utf-8") as f:
        new_keys = [line.strip() for line in f if line.strip()]
    assert len(new_keys) == 3, "new_keys.txt must contain exactly 3 API keys, one per line."

    content = read_file_exact(USERS_ROTATED_CSV)
    lines = content.split('\n')
    if lines and lines[-1] == '':
        lines = lines[:-1]
    user_rows = lines[1:]

    found_keys = []
    for idx, row in enumerate(user_rows):
        fields = row.split(',')
        assert len(fields) == 4, f"Row {idx+1} does not have exactly 4 columns: {row}"
        found_keys.append(fields[3])

    assert found_keys == new_keys, (
        f"The api_key values in {USERS_ROTATED_CSV} do not match the new_keys.txt in order.\n"
        f"Expected: {new_keys}\n"
        f"Found:    {found_keys}"
    )

    # Ensure no old keys remain
    old_keys = {"oldkey-123", "oldkey-456", "oldkey-789"}
    overlap = set(found_keys) & old_keys
    assert not overlap, (
        f"The following old api_keys are still present in {USERS_ROTATED_CSV}: {overlap}"
    )


def test_rotation_log_exists_and_has_expected_content():
    assert os.path.isfile(ROTATION_LOG), (
        f"File {ROTATION_LOG} does not exist. "
        "You must create the rotation verification log."
    )
    content = read_file_exact(ROTATION_LOG)
    # Remove any trailing whitespace and normalize
    lines = content.split('\n')
    if lines and lines[-1] == '':
        lines = lines[:-1]

    expected_lines = EXPECTED_ROTATION_LOG.split('\n')
    if expected_lines and expected_lines[-1] == '':
        expected_lines = expected_lines[:-1]

    assert lines == expected_lines, (
        f"{ROTATION_LOG} content is incorrect.\n"
        f"Expected lines:\n{EXPECTED_ROTATION_LOG}\n"
        f"Found lines:\n{content}"
    )

    # Check line count
    assert len(lines) == 4, (
        f"{ROTATION_LOG} should have exactly 4 lines, found {len(lines)}."
    )
    # Check each line for extra spaces
    for idx, line in enumerate(lines, start=1):
        assert line == line.strip(), (
            f"Line {idx} in {ROTATION_LOG} has leading or trailing whitespace: '{line}'"
        )