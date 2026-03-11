# test_final_state.py

import os
import re
import stat
import tarfile
import pytest

APPDATA_DIR = "/home/user/appdata"
BACKUPS_DIR = "/home/user/backups"
DB_CONF = "/home/user/appdata/db.conf"
API_KEYS_CONF = "/home/user/appdata/api_keys.conf"
APP_LOG = "/home/user/appdata/app.log"
ARCHIVE = "/home/user/backups/appdata_backup.tar.gz"
MANIFEST = "/home/user/backups/archive_manifest.txt"


def get_octal_permissions(path):
    """Return the octal permission bits for a file."""
    return stat.S_IMODE(os.stat(path).st_mode)


# ── Step 1: File permission tests ────────────────────────────────────────────

def test_db_conf_exists():
    assert os.path.isfile(DB_CONF), f"File {DB_CONF} does not exist"


def test_api_keys_conf_exists():
    assert os.path.isfile(API_KEYS_CONF), f"File {API_KEYS_CONF} does not exist"


def test_app_log_exists():
    assert os.path.isfile(APP_LOG), f"File {APP_LOG} does not exist"


def test_db_conf_permissions():
    perms = get_octal_permissions(DB_CONF)
    assert perms == 0o600, (
        f"{DB_CONF} should have permissions 600 (owner read/write only), "
        f"but has {oct(perms)}. "
        "Run: chmod 600 /home/user/appdata/db.conf"
    )


def test_api_keys_conf_permissions():
    perms = get_octal_permissions(API_KEYS_CONF)
    assert perms == 0o600, (
        f"{API_KEYS_CONF} should have permissions 600 (owner read/write only), "
        f"but has {oct(perms)}. "
        "Run: chmod 600 /home/user/appdata/api_keys.conf"
    )


def test_app_log_permissions():
    perms = get_octal_permissions(APP_LOG)
    assert perms == 0o640, (
        f"{APP_LOG} should have permissions 640 (owner rw, group r, others none), "
        f"but has {oct(perms)}. "
        "Run: chmod 640 /home/user/appdata/app.log"
    )


# ── Step 2: Archive tests ─────────────────────────────────────────────────────

def test_archive_exists():
    assert os.path.isfile(ARCHIVE), (
        f"Archive {ARCHIVE} does not exist. "
        "Run: cd /home/user && tar -czvf /home/user/backups/appdata_backup.tar.gz appdata/"
    )


def test_archive_is_valid_gzip_tar():
    assert tarfile.is_tarfile(ARCHIVE), (
        f"{ARCHIVE} is not a valid tar archive."
    )
    try:
        with tarfile.open(ARCHIVE, "r:gz") as tf:
            names = tf.getnames()
    except Exception as e:
        pytest.fail(f"{ARCHIVE} could not be opened as a gzip-compressed tar: {e}")


def test_archive_contains_expected_members():
    with tarfile.open(ARCHIVE, "r:gz") as tf:
        names = tf.getnames()
    expected = {"appdata/db.conf", "appdata/api_keys.conf", "appdata/app.log"}
    # Filter out directory entries (e.g. "appdata/")
    file_names = {n for n in names if not n.endswith("/")}
    missing = expected - file_names
    assert not missing, (
        f"Archive {ARCHIVE} is missing expected members: {missing}. "
        f"Members found: {file_names}"
    )


def test_archive_uses_relative_paths():
    with tarfile.open(ARCHIVE, "r:gz") as tf:
        names = tf.getnames()
    absolute = [n for n in names if n.startswith("/")]
    assert not absolute, (
        f"Archive contains absolute paths (should be relative): {absolute}. "
        "Make sure you ran tar from /home/user, not from /."
    )


def test_archive_db_conf_permissions():
    with tarfile.open(ARCHIVE, "r:gz") as tf:
        try:
            member = tf.getmember("appdata/db.conf")
        except KeyError:
            pytest.fail("appdata/db.conf not found in archive")
    actual = stat.S_IMODE(member.mode)
    assert actual == 0o600, (
        f"appdata/db.conf inside archive has permissions {oct(actual)}, "
        f"expected 0o600. Make sure you chmod 600 before creating the archive."
    )


def test_archive_api_keys_conf_permissions():
    with tarfile.open(ARCHIVE, "r:gz") as tf:
        try:
            member = tf.getmember("appdata/api_keys.conf")
        except KeyError:
            pytest.fail("appdata/api_keys.conf not found in archive")
    actual = stat.S_IMODE(member.mode)
    assert actual == 0o600, (
        f"appdata/api_keys.conf inside archive has permissions {oct(actual)}, "
        f"expected 0o600. Make sure you chmod 600 before creating the archive."
    )


def test_archive_app_log_permissions():
    with tarfile.open(ARCHIVE, "r:gz") as tf:
        try:
            member = tf.getmember("appdata/app.log")
        except KeyError:
            pytest.fail("appdata/app.log not found in archive")
    actual = stat.S_IMODE(member.mode)
    assert actual == 0o640, (
        f"appdata/app.log inside archive has permissions {oct(actual)}, "
        f"expected 0o640. Make sure you chmod 640 before creating the archive."
    )


# ── Step 3: Manifest tests ────────────────────────────────────────────────────

def test_manifest_exists():
    assert os.path.isfile(MANIFEST), (
        f"Manifest file {MANIFEST} does not exist. "
        "Run: tar -tzvf /home/user/backups/appdata_backup.tar.gz > /home/user/backups/archive_manifest.txt"
    )


def _get_manifest_data_lines():
    """Return non-empty, non-directory lines from the manifest."""
    with open(MANIFEST, "r") as f:
        lines = f.read().splitlines()
    # Keep only lines that look like file entries (not blank, not directory-only entries)
    data_lines = [l for l in lines if l.strip() and not l.strip().endswith("/")]
    return data_lines


def test_manifest_has_exactly_three_data_lines():
    data_lines = _get_manifest_data_lines()
    assert len(data_lines) == 3, (
        f"archive_manifest.txt should contain exactly 3 data lines (one per file), "
        f"but found {len(data_lines)}:\n" + "\n".join(data_lines)
    )


def test_manifest_db_conf_line():
    data_lines = _get_manifest_data_lines()
    pattern = re.compile(
        r'^-rw-------\s+\w+/\w+\s+\d+\s+\S+\s+\S+\s+appdata/db\.conf$'
    )
    matching = [l for l in data_lines if pattern.match(l)]
    assert matching, (
        "No line in archive_manifest.txt matches the expected pattern for appdata/db.conf.\n"
        "Expected pattern: -rw-------  user/group  <size>  <date>  <time>  appdata/db.conf\n"
        "Manifest lines found:\n" + "\n".join(data_lines)
    )


def test_manifest_api_keys_conf_line():
    data_lines = _get_manifest_data_lines()
    pattern = re.compile(
        r'^-rw-------\s+\w+/\w+\s+\d+\s+\S+\s+\S+\s+appdata/api_keys\.conf$'
    )
    matching = [l for l in data_lines if pattern.match(l)]
    assert matching, (
        "No line in archive_manifest.txt matches the expected pattern for appdata/api_keys.conf.\n"
        "Expected pattern: -rw-------  user/group  <size>  <date>  <time>  appdata/api_keys.conf\n"
        "Manifest lines found:\n" + "\n".join(data_lines)
    )


def test_manifest_app_log_line():
    data_lines = _get_manifest_data_lines()
    pattern = re.compile(
        r'^-rw-r-----\s+\w+/\w+\s+\d+\s+\S+\s+\S+\s+appdata/app\.log$'
    )
    matching = [l for l in data_lines if pattern.match(l)]
    assert matching, (
        "No line in archive_manifest.txt matches the expected pattern for appdata/app.log.\n"
        "Expected pattern: -rw-r-----  user/group  <size>  <date>  <time>  appdata/app.log\n"
        "Manifest lines found:\n" + "\n".join(data_lines)
    )


def test_manifest_db_conf_permission_string_exact():
    """The permission column for db.conf must be exactly -rw-------."""
    data_lines = _get_manifest_data_lines()
    db_lines = [l for l in data_lines if "appdata/db.conf" in l]
    assert db_lines, "No line mentioning appdata/db.conf found in manifest."
    for line in db_lines:
        perm_field = line.split()[0]
        assert perm_field == "-rw-------", (
            f"Permission string for appdata/db.conf in manifest is '{perm_field}', "
            f"expected '-rw-------'.\nFull line: {line}"
        )


def test_manifest_api_keys_conf_permission_string_exact():
    """The permission column for api_keys.conf must be exactly -rw-------."""
    data_lines = _get_manifest_data_lines()
    api_lines = [l for l in data_lines if "appdata/api_keys.conf" in l]
    assert api_lines, "No line mentioning appdata/api_keys.conf found in manifest."
    for line in api_lines:
        perm_field = line.split()[0]
        assert perm_field == "-rw-------", (
            f"Permission string for appdata/api_keys.conf in manifest is '{perm_field}', "
            f"expected '-rw-------'.\nFull line: {line}"
        )


def test_manifest_app_log_permission_string_exact():
    """The permission column for app.log must be exactly -rw-r-----."""
    data_lines = _get_manifest_data_lines()
    log_lines = [l for l in data_lines if "appdata/app.log" in l]
    assert log_lines, "No line mentioning appdata/app.log found in manifest."
    for line in log_lines:
        perm_field = line.split()[0]
        assert perm_field == "-rw-r-----", (
            f"Permission string for appdata/app.log in manifest is '{perm_field}', "
            f"expected '-rw-r-----'.\nFull line: {line}"
        )