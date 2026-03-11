# test_final_state.py

import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"
LOGS_ARCHIVE_DIR = "/home/user/project/logs_archive"
MANIFEST_PATH = "/home/user/project/py_manifest.txt"

EXPECTED_LOG_FILES_IN_ARCHIVE = {
    "/home/user/project/logs_archive/debug.log",
    "/home/user/project/logs_archive/auth.log",
    "/home/user/project/logs_archive/output.log",
    "/home/user/project/logs_archive/errors.log",
}

EXPECTED_TMP_FILES_DELETED = [
    "/home/user/project/src/session.tmp",
    "/home/user/project/src/auth/cache.tmp",
    "/home/user/project/src/api/request.tmp",
    "/home/user/project/build/build.tmp",
]

EXPECTED_MANIFEST_CONTENTS = (
    "/home/user/project/src/api/routes.py\n"
    "/home/user/project/src/auth/login.py\n"
    "/home/user/project/src/main.py\n"
    "/home/user/project/src/utils.py\n"
)

EXPECTED_MANIFEST_LINES = [
    "/home/user/project/src/api/routes.py",
    "/home/user/project/src/auth/login.py",
    "/home/user/project/src/main.py",
    "/home/user/project/src/utils.py",
]


# ---------------------------------------------------------------------------
# Step 1: .log files moved to logs_archive
# ---------------------------------------------------------------------------

def test_logs_archive_contains_exactly_four_log_files():
    result = subprocess.run(
        ["find", LOGS_ARCHIVE_DIR, "-name", "*.log"],
        capture_output=True, text=True, check=True
    )
    found = [f for f in result.stdout.strip().split("\n") if f]
    assert len(found) == 4, (
        f"Expected exactly 4 .log files in {LOGS_ARCHIVE_DIR}, "
        f"but found {len(found)}: {found}"
    )


@pytest.mark.parametrize("log_file", sorted(EXPECTED_LOG_FILES_IN_ARCHIVE))
def test_expected_log_file_exists_in_archive(log_file):
    assert os.path.isfile(log_file), (
        f"Expected .log file {log_file} is missing from logs_archive. "
        "It should have been moved there during Step 1."
    )


def test_no_log_files_outside_logs_archive():
    result = subprocess.run(
        ["find", PROJECT_DIR, "-name", "*.log",
         "-not", "-path", "*/logs_archive/*"],
        capture_output=True, text=True, check=True
    )
    stray_logs = [f for f in result.stdout.strip().split("\n") if f]
    assert len(stray_logs) == 0, (
        f"Found .log files outside of logs_archive (they should have been moved): "
        f"{stray_logs}"
    )


def test_logs_archive_has_no_extra_log_files():
    result = subprocess.run(
        ["find", LOGS_ARCHIVE_DIR, "-name", "*.log"],
        capture_output=True, text=True, check=True
    )
    found = set(f for f in result.stdout.strip().split("\n") if f)
    extra = found - EXPECTED_LOG_FILES_IN_ARCHIVE
    assert len(extra) == 0, (
        f"logs_archive contains unexpected .log files: {extra}"
    )


# ---------------------------------------------------------------------------
# Step 2: .tmp files deleted
# ---------------------------------------------------------------------------

def test_no_tmp_files_exist_anywhere_under_project():
    result = subprocess.run(
        ["find", PROJECT_DIR, "-name", "*.tmp"],
        capture_output=True, text=True, check=True
    )
    tmp_files = [f for f in result.stdout.strip().split("\n") if f]
    assert len(tmp_files) == 0, (
        f"Found .tmp files that should have been deleted: {tmp_files}"
    )


@pytest.mark.parametrize("tmp_file", EXPECTED_TMP_FILES_DELETED)
def test_specific_tmp_file_is_deleted(tmp_file):
    assert not os.path.exists(tmp_file), (
        f".tmp file {tmp_file} still exists but should have been deleted in Step 2."
    )


# ---------------------------------------------------------------------------
# Step 3: py_manifest.txt exists with correct contents
# ---------------------------------------------------------------------------

def test_py_manifest_file_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Manifest file {MANIFEST_PATH} does not exist. "
        "It should have been created during Step 3."
    )


def test_py_manifest_has_exactly_four_lines():
    with open(MANIFEST_PATH, "r") as f:
        contents = f.read()
    lines = contents.splitlines()
    assert len(lines) == 4, (
        f"Expected exactly 4 lines in {MANIFEST_PATH}, "
        f"but found {len(lines)}. Lines: {lines}"
    )


def test_py_manifest_no_trailing_blank_line():
    with open(MANIFEST_PATH, "r") as f:
        contents = f.read()
    # Should end with a single newline after last path (not a blank line)
    assert not contents.endswith("\n\n"), (
        f"{MANIFEST_PATH} ends with a trailing blank line, which is not allowed."
    )
    assert contents.endswith("\n"), (
        f"{MANIFEST_PATH} should end with a newline character after the last path."
    )


def test_py_manifest_lines_are_sorted_alphabetically():
    with open(MANIFEST_PATH, "r") as f:
        contents = f.read()
    lines = contents.splitlines()
    assert lines == sorted(lines), (
        f"Lines in {MANIFEST_PATH} are not sorted alphabetically.\n"
        f"Actual order:    {lines}\n"
        f"Expected order:  {sorted(lines)}"
    )


@pytest.mark.parametrize("expected_line", EXPECTED_MANIFEST_LINES)
def test_py_manifest_contains_expected_path(expected_line):
    with open(MANIFEST_PATH, "r") as f:
        lines = [l.strip() for l in f.readlines()]
    assert expected_line in lines, (
        f"Expected path '{expected_line}' not found in {MANIFEST_PATH}. "
        f"Actual contents: {lines}"
    )


def test_py_manifest_exact_contents():
    with open(MANIFEST_PATH, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_MANIFEST_CONTENTS, (
        f"Contents of {MANIFEST_PATH} do not match expected.\n"
        f"Expected: {repr(EXPECTED_MANIFEST_CONTENTS)}\n"
        f"Actual:   {repr(actual)}"
    )


def test_py_manifest_contains_only_absolute_paths():
    with open(MANIFEST_PATH, "r") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    for line in lines:
        assert line.startswith("/"), (
            f"Line '{line}' in {MANIFEST_PATH} is not an absolute path."
        )


def test_py_manifest_contains_only_py_files():
    with open(MANIFEST_PATH, "r") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    for line in lines:
        assert line.endswith(".py"), (
            f"Line '{line}' in {MANIFEST_PATH} does not refer to a .py file."
        )


def test_py_manifest_paths_all_exist():
    with open(MANIFEST_PATH, "r") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    for line in lines:
        assert os.path.isfile(line), (
            f"Path '{line}' listed in {MANIFEST_PATH} does not exist on disk."
        )


def test_py_manifest_matches_actual_py_files_on_disk():
    """Cross-check: manifest must list exactly the .py files found under project."""
    result = subprocess.run(
        ["find", PROJECT_DIR, "-name", "*.py"],
        capture_output=True, text=True, check=True
    )
    actual_py_files = sorted(f for f in result.stdout.strip().split("\n") if f)

    with open(MANIFEST_PATH, "r") as f:
        manifest_lines = sorted(l.strip() for l in f.readlines() if l.strip())

    assert manifest_lines == actual_py_files, (
        f"Manifest contents do not match actual .py files on disk.\n"
        f"Manifest: {manifest_lines}\n"
        f"On disk:  {actual_py_files}"
    )


# ---------------------------------------------------------------------------
# Sanity checks: original .py source files still intact
# ---------------------------------------------------------------------------

EXPECTED_PY_FILES = {
    "/home/user/project/src/main.py": "# main\n",
    "/home/user/project/src/utils.py": "# utils\n",
    "/home/user/project/src/auth/login.py": "# login\n",
    "/home/user/project/src/api/routes.py": "# routes\n",
}


@pytest.mark.parametrize("py_file,expected_content", list(EXPECTED_PY_FILES.items()))
def test_py_source_file_still_intact(py_file, expected_content):
    assert os.path.isfile(py_file), (
        f"Python source file {py_file} is missing. It should not have been deleted."
    )
    with open(py_file, "r") as f:
        actual = f.read()
    assert actual == expected_content, (
        f"Python source file {py_file} has unexpected content.\n"
        f"Expected: {repr(expected_content)}\n"
        f"Actual:   {repr(actual)}"
    )