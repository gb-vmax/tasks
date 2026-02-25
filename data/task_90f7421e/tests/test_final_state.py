# test_final_state.py

import os
import stat
import pwd
import pytest

HOME = "/home/user"
SSH_DIR = os.path.join(HOME, ".ssh")
PRIVKEY = os.path.join(SSH_DIR, "iot_edge_ssh")
PUBKEY = PRIVKEY + ".pub"
LOGFILE = os.path.join(HOME, "edge_ssh_keygen.log")
USER = "user"
KEY_COMMENT = "edge-iot-access"


def get_owner(path):
    """
    Returns the username of the owner of the file at 'path'.
    """
    try:
        return pwd.getpwuid(os.stat(path).st_uid).pw_name
    except Exception:
        return None

def is_writable_dir(path, user=USER):
    """
    Checks if the directory exists and is writable by the specified user.
    """
    if not os.path.isdir(path):
        return False
    st = os.stat(path)
    try:
        pw = pwd.getpwnam(user)
    except KeyError:
        return False
    # Owner
    if st.st_uid == pw.pw_uid:
        return bool(st.st_mode & stat.S_IWUSR)
    # Group
    if st.st_gid == pw.pw_gid:
        return bool(st.st_mode & stat.S_IWGRP)
    # Others
    return bool(st.st_mode & stat.S_IWOTH)

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def read_file_bytes(path):
    with open(path, 'rb') as f:
        return f.read()

def file_mode(path):
    return stat.S_IMODE(os.stat(path).st_mode)

def describe_final_filesystem_state():
    pass

def test_ssh_dir_exists_and_is_writable():
    assert os.path.isdir(SSH_DIR), (
        f"Required directory {SSH_DIR} does not exist."
    )
    assert is_writable_dir(SSH_DIR), (
        f"Directory {SSH_DIR} is not writable by '{USER}'."
    )
    assert get_owner(SSH_DIR) == USER, (
        f"Directory {SSH_DIR} is not owned by '{USER}'."
    )

def test_private_key_exists_and_is_valid():
    assert os.path.isfile(PRIVKEY), (
        f"Private key file {PRIVKEY} does not exist."
    )
    # Check permissions: no more permissive than 600
    mode = file_mode(PRIVKEY)
    assert mode <= 0o600, (
        f"Private key file {PRIVKEY} permissions are too permissive: {oct(mode)}. "
        "Set to 600 (rw-------) or less."
    )
    # Check ownership
    owner = get_owner(PRIVKEY)
    assert owner == USER, (
        f"Private key file {PRIVKEY} is not owned by '{USER}' (owner: {owner})."
    )
    # Check file content: starts with correct header
    content = read_file(PRIVKEY)
    assert content.startswith("-----BEGIN OPENSSH PRIVATE KEY-----"), (
        f"Private key file {PRIVKEY} does not start with the expected header."
    )
    # Check key type: ed25519 (OpenSSH format)
    # The second line of the private key (after header) is base64-encoded, but
    # we can check the corresponding public key file for actual type.

def test_public_key_exists_and_matches():
    assert os.path.isfile(PUBKEY), (
        f"Public key file {PUBKEY} does not exist."
    )
    # Check ownership
    owner = get_owner(PUBKEY)
    assert owner == USER, (
        f"Public key file {PUBKEY} is not owned by '{USER}' (owner: {owner})."
    )
    # Check file content: starts and ends as required, single line
    lines = read_file(PUBKEY).splitlines()
    assert len(lines) == 1, (
        f"Public key file {PUBKEY} must contain exactly one line."
    )
    line = lines[0]
    assert line.startswith("ssh-ed25519 "), (
        f"Public key file {PUBKEY} does not start with 'ssh-ed25519 '."
    )
    assert line.endswith(KEY_COMMENT), (
        f"Public key file {PUBKEY} does not end with the required comment '{KEY_COMMENT}'."
    )
    # Optionally: Ensure the public key corresponds to the private key,
    # but with only stdlib and no 3rd-party, we can't robustly parse and check that.

def test_logfile_exists_and_contents():
    assert os.path.isfile(LOGFILE), (
        f"Log file {LOGFILE} does not exist."
    )
    # Check ownership
    owner = get_owner(LOGFILE)
    assert owner == USER, (
        f"Log file {LOGFILE} is not owned by '{USER}' (owner: {owner})."
    )
    # Check exact log contents
    expected_lines = [
        "Key Type: ed25519",
        f"Public Key Path: {PUBKEY}",
        f"Private Key Path: {PRIVKEY}",
        f"Comment: {KEY_COMMENT}"
    ]
    log_content = read_file(LOGFILE)
    log_lines = log_content.rstrip('\n').split('\n')
    assert log_lines == expected_lines, (
        f"Log file {LOGFILE} does not contain the expected lines.\n"
        f"Expected:\n{expected_lines}\nActual:\n{log_lines}"
    )

def test_key_files_and_logfile_locations():
    assert os.path.abspath(PRIVKEY) == PRIVKEY, (
        f"Private key file path is not absolute: {PRIVKEY}"
    )
    assert os.path.abspath(PUBKEY) == PUBKEY, (
        f"Public key file path is not absolute: {PUBKEY}"
    )
    assert os.path.abspath(LOGFILE) == LOGFILE, (
        f"Log file path is not absolute: {LOGFILE}"
    )
    # All files must be in their exact required locations
    assert os.path.dirname(PRIVKEY) == SSH_DIR, (
        f"Private key file is not in {SSH_DIR}"
    )
    assert os.path.dirname(PUBKEY) == SSH_DIR, (
        f"Public key file is not in {SSH_DIR}"
    )
    assert os.path.dirname(LOGFILE) == HOME, (
        f"Log file is not in {HOME}"
    )

def test_private_key_permissions_are_not_too_permissive():
    mode = file_mode(PRIVKEY)
    assert mode & 0o077 == 0, (
        f"Private key file {PRIVKEY} permissions are too permissive: {oct(mode)}. "
        "No group/other access allowed."
    )

def test_key_files_newly_generated():
    # This test assumes it is only run after the task is completed, so can't
    # check historical existence, but can check for plausible creation time.
    # We can check that the ctime/mtime are recent, but that's not robust in
    # a container, so we'll just check file size > 0.
    priv_size = os.path.getsize(PRIVKEY)
    pub_size = os.path.getsize(PUBKEY)
    assert priv_size > 0, (
        f"Private key file {PRIVKEY} is empty."
    )
    assert pub_size > 0, (
        f"Public key file {PUBKEY} is empty."
    )

def test_no_extra_files_created():
    # There should be no extra files matching iot_edge_ssh* in .ssh except the required ones
    for fname in os.listdir(SSH_DIR):
        if fname.startswith("iot_edge_ssh"):
            abspath = os.path.join(SSH_DIR, fname)
            assert abspath in [PRIVKEY, PUBKEY], (
                f"Unexpected file found in {SSH_DIR}: {abspath}"
            )