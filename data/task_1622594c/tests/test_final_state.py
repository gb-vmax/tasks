# test_final_state.py

import os
import tarfile
import gzip
import pytest

INCIDENT_DIR = "/home/user/incident"
LOGS_DIR = "/home/user/incident/logs"
TARBALL_PATH = "/home/user/incident/incident_errors.tar.gz"
MANIFEST_PATH = "/home/user/incident/archive_manifest.txt"

EXPECTED_ERROR_FILES = {
    "logs/app.error",
    "logs/db.error",
    "logs/nginx.error",
}

NON_ERROR_FILES = {
    "logs/app.log",
    "logs/db.log",
    "logs/system.info",
}


# ── Tarball existence and validity ────────────────────────────────────────────

def test_tarball_exists():
    assert os.path.isfile(TARBALL_PATH), (
        f"Archive {TARBALL_PATH} does not exist. "
        "The agent must create a gzip-compressed tar archive at this path."
    )


def test_tarball_is_gzip_compressed():
    assert os.path.isfile(TARBALL_PATH), f"Archive {TARBALL_PATH} does not exist."
    try:
        with gzip.open(TARBALL_PATH, "rb") as f:
            f.read(1)  # read at least one byte to confirm it's valid gzip
    except (OSError, gzip.BadGzipFile) as exc:
        pytest.fail(
            f"{TARBALL_PATH} is not a valid gzip file: {exc}"
        )


def test_tarball_is_valid_tar():
    assert os.path.isfile(TARBALL_PATH), f"Archive {TARBALL_PATH} does not exist."
    assert tarfile.is_tarfile(TARBALL_PATH), (
        f"{TARBALL_PATH} is not a valid tar archive."
    )


# ── Archive contents ──────────────────────────────────────────────────────────

def _get_archive_members():
    """Return the list of member names inside the tarball."""
    with tarfile.open(TARBALL_PATH, "r:gz") as tf:
        return tf.getnames()


def test_archive_contains_exactly_three_files():
    members = _get_archive_members()
    # Filter out any directory entries (names ending with '/')
    file_members = [m for m in members if not m.endswith("/")]
    assert len(file_members) == 3, (
        f"Archive must contain exactly 3 files, but found {len(file_members)}: "
        f"{file_members}"
    )


def test_archive_contains_app_error():
    members = set(_get_archive_members())
    assert "logs/app.error" in members, (
        f"'logs/app.error' is missing from the archive. "
        f"Archive contains: {members}"
    )


def test_archive_contains_db_error():
    members = set(_get_archive_members())
    assert "logs/db.error" in members, (
        f"'logs/db.error' is missing from the archive. "
        f"Archive contains: {members}"
    )


def test_archive_contains_nginx_error():
    members = set(_get_archive_members())
    assert "logs/nginx.error" in members, (
        f"'logs/nginx.error' is missing from the archive. "
        f"Archive contains: {members}"
    )


def test_archive_does_not_contain_app_log():
    members = set(_get_archive_members())
    assert "logs/app.log" not in members, (
        f"'logs/app.log' must NOT be in the archive, but it was found. "
        f"Archive contains: {members}"
    )


def test_archive_does_not_contain_db_log():
    members = set(_get_archive_members())
    assert "logs/db.log" not in members, (
        f"'logs/db.log' must NOT be in the archive, but it was found. "
        f"Archive contains: {members}"
    )


def test_archive_does_not_contain_system_info():
    members = set(_get_archive_members())
    assert "logs/system.info" not in members, (
        f"'logs/system.info' must NOT be in the archive, but it was found. "
        f"Archive contains: {members}"
    )


def test_archive_uses_relative_paths():
    members = _get_archive_members()
    for member in members:
        assert not member.startswith("/"), (
            f"Archive member '{member}' uses an absolute path. "
            "All paths inside the archive must be relative (e.g., 'logs/app.error')."
        )
        assert not member.startswith("/home/"), (
            f"Archive member '{member}' contains the full host path. "
            "Paths must be relative, like 'logs/app.error'."
        )


def test_archive_members_start_with_logs_prefix():
    members = [m for m in _get_archive_members() if not m.endswith("/")]
    for member in members:
        assert member.startswith("logs/"), (
            f"Archive member '{member}' does not start with 'logs/'. "
            "Paths inside the archive should look like 'logs/app.error'."
        )


# ── Manifest existence and line count ────────────────────────────────────────

def test_manifest_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Manifest file {MANIFEST_PATH} does not exist. "
        "The agent must create this file with the verbose tar listing."
    )


def test_manifest_has_exactly_three_lines():
    assert os.path.isfile(MANIFEST_PATH), f"Manifest {MANIFEST_PATH} does not exist."
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    # Remove any trailing blank lines to be consistent with wc -l behaviour
    # but the spec says "no trailing blank lines" so we assert strictly
    assert content == content.rstrip("\n") + ("\n" if content.endswith("\n") else ""), \
        "Manifest should not have trailing blank lines beyond the final newline."
    non_blank_lines = [l for l in lines if l.strip()]
    assert len(non_blank_lines) == 3, (
        f"Manifest must contain exactly 3 non-blank lines, "
        f"but found {len(non_blank_lines)}.\n"
        f"Manifest content:\n{content}"
    )


def test_manifest_line_count_matches_wc_l():
    """wc -l counts newline characters; verify the file has exactly 3 newlines."""
    assert os.path.isfile(MANIFEST_PATH), f"Manifest {MANIFEST_PATH} does not exist."
    with open(MANIFEST_PATH, "rb") as f:
        raw = f.read()
    newline_count = raw.count(b"\n")
    assert newline_count == 3, (
        f"Expected exactly 3 newline characters in manifest (wc -l == 3), "
        f"but found {newline_count}.\n"
        f"Raw content: {raw!r}"
    )


# ── Manifest content assertions ───────────────────────────────────────────────

def _manifest_lines():
    with open(MANIFEST_PATH, "r") as f:
        return f.read().splitlines()


def test_manifest_contains_app_error_entry():
    lines = _manifest_lines()
    matching = [l for l in lines if "logs/app.error" in l]
    assert len(matching) == 1, (
        f"Expected exactly 1 line containing 'logs/app.error' in manifest, "
        f"found {len(matching)}.\nManifest lines: {lines}"
    )


def test_manifest_contains_db_error_entry():
    lines = _manifest_lines()
    matching = [l for l in lines if "logs/db.error" in l]
    assert len(matching) == 1, (
        f"Expected exactly 1 line containing 'logs/db.error' in manifest, "
        f"found {len(matching)}.\nManifest lines: {lines}"
    )


def test_manifest_contains_nginx_error_entry():
    lines = _manifest_lines()
    matching = [l for l in lines if "logs/nginx.error" in l]
    assert len(matching) == 1, (
        f"Expected exactly 1 line containing 'logs/nginx.error' in manifest, "
        f"found {len(matching)}.\nManifest lines: {lines}"
    )


def test_manifest_does_not_contain_app_log():
    lines = _manifest_lines()
    matching = [l for l in lines if "logs/app.log" in l]
    assert len(matching) == 0, (
        f"Manifest must NOT contain 'logs/app.log', but found: {matching}"
    )


def test_manifest_does_not_contain_db_log():
    lines = _manifest_lines()
    matching = [l for l in lines if "logs/db.log" in l]
    assert len(matching) == 0, (
        f"Manifest must NOT contain 'logs/db.log', but found: {matching}"
    )


def test_manifest_does_not_contain_system_info():
    lines = _manifest_lines()
    matching = [l for l in lines if "logs/system.info" in l]
    assert len(matching) == 0, (
        f"Manifest must NOT contain 'logs/system.info', but found: {matching}"
    )


def test_manifest_lines_are_verbose_format():
    """Each line should look like a 'tar -tvf' verbose entry (starts with permissions field)."""
    lines = _manifest_lines()
    non_blank = [l for l in lines if l.strip()]
    for line in non_blank:
        # verbose tar output starts with a permissions string like -rw-r--r--
        assert len(line) > 10, (
            f"Manifest line appears too short to be a verbose tar entry: {line!r}"
        )
        # The first character should be '-', 'd', 'l', etc. (file type indicator)
        assert line[0] in ("-", "d", "l", "c", "b", "p", "s"), (
            f"Manifest line does not start with a valid file-type character "
            f"(expected verbose tar format): {line!r}"
        )


# ── Original log files still intact ──────────────────────────────────────────

@pytest.mark.parametrize("filename", [
    "app.error", "db.error", "nginx.error",
    "app.log", "db.log", "system.info",
])
def test_original_log_files_still_exist(filename):
    filepath = os.path.join(LOGS_DIR, filename)
    assert os.path.isfile(filepath), (
        f"Original log file {filepath} is missing after the agent ran. "
        "The agent should not delete the source files."
    )