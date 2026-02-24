# test_final_state.py

import os
import stat
import pytest

HOME = "/home/user"
SRC_DIR = os.path.join(HOME, "source_configs")
DST_DIR = os.path.join(HOME, "hardened_configs")

SRC_FILES = {
    "db.conf": "db_user=admin\ndb_pass=secret\n",
    "web.conf": "server_name=example.com\nlisten=80\n",
    "bad.conf": "config_break\n",
}

EXPECTED_HARDENED_SUFFIX = "# Hardened"
ERROR_LOG = os.path.join(DST_DIR, "error_log.txt")

def read_file_strip_trailing_newlines(path):
    """Read file, return list of lines, stripping trailing newlines."""
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return lines

def get_dst_conf_files():
    """Return set of .conf file names in DST_DIR"""
    return {f for f in os.listdir(DST_DIR)
            if os.path.isfile(os.path.join(DST_DIR, f)) and f.endswith(".conf")}

def get_error_log_entries():
    """Return list of error log entries, or None if file does not exist"""
    if not os.path.exists(ERROR_LOG):
        return None
    with open(ERROR_LOG, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    # Remove empty lines at end (if any)
    while lines and lines[-1] == "":
        lines.pop()
    return lines

def test_all_expected_conf_files_present():
    """All .conf files from source must appear in hardened_configs/"""
    dst_files = get_dst_conf_files()
    missing = set(SRC_FILES.keys()) - dst_files
    extra = dst_files - set(SRC_FILES.keys())
    assert not missing, (
        f"Missing .conf file(s) in {DST_DIR}: {', '.join(sorted(missing))}"
    )
    assert not extra, (
        f"Unexpected extra .conf file(s) in {DST_DIR}: {', '.join(sorted(extra))}"
    )

@pytest.mark.parametrize("fname,original_content", SRC_FILES.items())
def test_conf_file_content_and_hardened(fname, original_content):
    """
    Each .conf file must:
      - exist in DST_DIR
      - have original content (lines), then a line with exactly '# Hardened'
      - not have extra lines after '# Hardened'
      - preserve all content unless an error occurred (in which case, see error_log)
    """
    dst_path = os.path.join(DST_DIR, fname)
    assert os.path.isfile(dst_path), f"Expected {dst_path} to exist."
    # Check for error for this file (copy or append)
    error_entries = get_error_log_entries()
    errors_for_this = []
    if error_entries:
        for entry in error_entries:
            parts = entry.split(":", 2)
            if len(parts) != 3:
                continue
            ename, estep, emsg = parts
            if ename == fname:
                errors_for_this.append((estep, emsg))
    if errors_for_this:
        # If copy failed, file may not be present, but we already checked above.
        # If append failed, the file should not end with '# Hardened'.
        # We'll check that.
        lines = read_file_strip_trailing_newlines(dst_path)
        if any(estep == "append" for estep, _ in errors_for_this):
            assert lines[-1] != EXPECTED_HARDENED_SUFFIX, (
                f"{dst_path} should NOT end with '{EXPECTED_HARDENED_SUFFIX}' because append failed."
            )
        # No further checks for error case for this file
        return
    # No errors for this file: must be fully correct
    lines = read_file_strip_trailing_newlines(dst_path)
    orig_lines = original_content.splitlines()
    assert lines[:-1] == orig_lines, (
        f"{dst_path} content is incorrect before '# Hardened'.\n"
        f"Expected lines: {orig_lines}\nActual lines: {lines[:-1]}"
    )
    assert lines[-1] == EXPECTED_HARDENED_SUFFIX, (
        f"{dst_path} must end with a line containing exactly '{EXPECTED_HARDENED_SUFFIX}', "
        f"but last line is: {lines[-1]!r}"
    )
    # Should be no extra lines after '# Hardened'
    # (splitlines() removes trailing blank lines, so this is sufficient)

def test_no_extra_files_in_hardened_configs():
    """
    Only the expected .conf files and (optionally) error_log.txt may exist in DST_DIR.
    """
    allowed = set(SRC_FILES.keys())
    allowed.add("error_log.txt")
    files = [f for f in os.listdir(DST_DIR) if os.path.isfile(os.path.join(DST_DIR, f))]
    extra = set(files) - allowed
    assert not extra, (
        f"Unexpected extra file(s) in {DST_DIR}: {', '.join(sorted(extra))}"
    )

def test_hardened_conf_files_permissions():
    """
    All files in DST_DIR must be user-readable and user-writable.
    """
    for fname in SRC_FILES.keys():
        fpath = os.path.join(DST_DIR, fname)
        st = os.stat(fpath)
        mode = st.st_mode
        assert mode & stat.S_IRUSR, f"{fpath} is not user-readable"
        assert mode & stat.S_IWUSR, f"{fpath} is not user-writable"

def test_hardened_configs_dir_permissions():
    """
    DST_DIR must be user-readable and user-writable.
    """
    st = os.stat(DST_DIR)
    mode = st.st_mode
    assert mode & stat.S_IRUSR, f"{DST_DIR} is not user-readable"
    assert mode & stat.S_IWUSR, f"{DST_DIR} is not user-writable"

def test_error_log_absence_or_empty_on_success():
    """
    If all files were processed successfully, error_log.txt should not exist, or must be empty.
    If it exists and has content, fail and show the errors.
    """
    entries = get_error_log_entries()
    if entries is None:
        # error_log.txt does not exist: OK
        return
    # error_log.txt exists: must be empty
    assert entries == [] or all(line.strip() == "" for line in entries), (
        f"error_log.txt exists at {ERROR_LOG} but is not empty. "
        f"Entries:\n" + "\n".join(entries)
    )

def test_error_log_entries_format_if_present():
    """
    If error_log.txt exists, each entry must be of the form:
        [filename]:[step]:[error_message]
    - filename must be one of the expected .conf files
    - step is either 'copy' or 'append'
    - error_message is non-empty
    """
    entries = get_error_log_entries()
    if not entries:
        # No error log or empty: OK
        return
    for line in entries:
        parts = line.split(":", 2)
        assert len(parts) == 3, (
            f"Malformed error log entry: {line!r} (expected 3 colon-separated fields)"
        )
        fname, step, errmsg = parts
        assert fname in SRC_FILES, (
            f"Error log entry refers to unknown file: {fname!r} in line: {line!r}"
        )
        assert step in ("copy", "append"), (
            f"Error log entry step must be 'copy' or 'append', found: {step!r} in line: {line!r}"
        )
        assert errmsg.strip(), (
            f"Error log entry must include a non-empty error message in line: {line!r}"
        )