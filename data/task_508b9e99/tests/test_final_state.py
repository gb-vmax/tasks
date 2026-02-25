# test_final_state.py

import os
import stat
import pytest
import pwd
import grp

HOME = "/home/user"
DATABASE_DIR = os.path.join(HOME, "database")
LOGS_DIR = os.path.join(DATABASE_DIR, "logs")
QUERY_LOG = os.path.join(LOGS_DIR, "query.log")
SYMLINK = os.path.join(HOME, "latest_queries.log")
SYMLINK_OUTPUT = os.path.join(HOME, "symlink_creation_output.txt")


def get_ls_l_symlink_line(path):
    """
    Replicate the output of 'ls -l <path>' for a symlink.
    Returns the single line output as a string.
    """
    st = os.lstat(path)
    # File mode string (e.g., lrwxrwxrwx)
    mode_str = stat.filemode(st.st_mode)
    # Number of hard links (for symlinks is always 1)
    nlink = st.st_nlink
    # Owner and group names
    try:
        owner = pwd.getpwuid(st.st_uid).pw_name
    except KeyError:
        owner = str(st.st_uid)
    try:
        group = grp.getgrgid(st.st_gid).gr_name
    except KeyError:
        group = str(st.st_gid)
    # File size (length of link target, not the target file size)
    size = st.st_size
    # Modification time
    import time
    mtime = st.st_mtime
    tm = time.localtime(mtime)
    # Format: if mtime is within last 6 months, show HH:MM, else show year
    now = time.time()
    six_months = 6 * 30 * 24 * 60 * 60
    if abs(now - mtime) > six_months:
        # Show year
        time_str = time.strftime("%b %e  %Y", tm)
    else:
        # Show HH:MM
        time_str = time.strftime("%b %e %H:%M", tm)
    # The symlink target shown in ls -l: relative if possible, else absolute
    link_target = os.readlink(path)
    # ls -l shows the argument path as given, so use the absolute path
    file_display = path
    line = (
        f"{mode_str} {nlink} {owner} {group} {size} {time_str} {file_display} -> {link_target}"
    )
    return line


def test_symlink_exists_and_is_correct():
    assert os.path.lexists(SYMLINK), (
        f"The symlink {SYMLINK} does not exist. "
        "You must create a symlink at this exact path."
    )
    st = os.lstat(SYMLINK)
    assert stat.S_ISLNK(st.st_mode), (
        f"{SYMLINK} exists but is not a symbolic link. "
        "Ensure you created a symlink, not a regular file."
    )
    actual_target = os.readlink(SYMLINK)
    expected_target = QUERY_LOG
    assert actual_target == expected_target, (
        f"{SYMLINK} does not point to the correct target.\n"
        f"Expected: {expected_target}\n"
        f"Actual:   {actual_target}\n"
        "Ensure the symlink points exactly to /home/user/database/logs/query.log."
    )


def test_symlink_output_file_contents_exact_ls_l():
    assert os.path.isfile(SYMLINK_OUTPUT), (
        f"The output file {SYMLINK_OUTPUT} does not exist. "
        "You must write the output of 'ls -l /home/user/latest_queries.log' to this file."
    )
    # Read the file contents, strip only trailing newlines
    with open(SYMLINK_OUTPUT, "r", encoding="utf-8") as f:
        output_content = f.read().rstrip('\n')

    # Generate the expected output using the real current file state
    expected_line = get_ls_l_symlink_line(SYMLINK)
    # The output must be exactly one line, no extra text or blank lines
    assert output_content == expected_line, (
        f"The contents of {SYMLINK_OUTPUT} do not match the expected output of "
        f"'ls -l {SYMLINK}'.\n"
        "Expected exactly:\n"
        f"{expected_line!r}\n"
        "But found:\n"
        f"{output_content!r}\n"
        "Ensure you ran the command as specified and wrote only the command's output, "
        "with no extra text or blank lines."
    )


def test_symlink_is_absolute_and_not_broken():
    # This test ensures the symlink is not broken and the target exists
    assert os.path.exists(QUERY_LOG), (
        f"The symlink target {QUERY_LOG} does not exist. "
        "Symlink must point to an existing file."
    )
    # Optionally, check that the symlink resolves to the right file
    resolved = os.path.realpath(SYMLINK)
    assert resolved == QUERY_LOG, (
        f"The symlink {SYMLINK} does not resolve to the expected file.\n"
        f"Expected: {QUERY_LOG}\n"
        f"Resolved: {resolved}\n"
        "Ensure the symlink points to the correct absolute path."
    )