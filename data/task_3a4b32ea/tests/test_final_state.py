# test_final_state.py

import os
import stat
import pytest

PROJECT_DIR = "/home/user/project"

# ---------------------------------------------------------------------------
# Expected files with their subdirectory and octal permission bits
# ---------------------------------------------------------------------------

EXPECTED_FILES = {
    "src/main.c":              0o644,
    "src/utils.c":             0o644,
    "src/parser.c":            0o644,
    "src/utils.h":             0o644,
    "src/parser.h":            0o644,
    "src/config.h":            0o644,
    "scripts/build.py":        0o755,
    "scripts/deploy.py":       0o755,
    "scripts/test_runner.py":  0o755,
    "docs/README.md":          0o644,
    "docs/CHANGELOG.md":       0o644,
    "docs/API.md":             0o644,
    "config/app.conf":         0o600,
    "config/db.conf":          0o600,
    "config/logging.conf":     0o600,
    "logs/app.log":            0o640,
    "logs/error.log":          0o640,
    "logs/debug.log":          0o640,
    "data/seed.sql":           0o644,
    "data/schema.sql":         0o644,
    "data/fixtures.json":      0o644,
}

EXPECTED_SYMLINKS = {
    "project.conf": "config/app.conf",
    "run.py":       "scripts/build.py",
    "latest.log":   "logs/app.log",
}

EXPECTED_SUBDIRS = ["src", "scripts", "docs", "config", "logs", "data"]

EXPECTED_MANIFEST_LINES = [
    "config/app.conf 600",
    "config/db.conf 600",
    "config/logging.conf 600",
    "data/fixtures.json 644",
    "data/schema.sql 644",
    "data/seed.sql 644",
    "docs/API.md 644",
    "docs/CHANGELOG.md 644",
    "docs/README.md 644",
    "logs/app.log 640",
    "logs/debug.log 640",
    "logs/error.log 640",
    "scripts/build.py 755",
    "scripts/deploy.py 755",
    "scripts/test_runner.py 755",
    "src/config.h 644",
    "src/main.c 644",
    "src/parser.c 644",
    "src/parser.h 644",
    "src/utils.c 644",
    "src/utils.h 644",
]


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def octal_perms(path):
    """Return the lower 9 permission bits of a path as an integer."""
    return stat.S_IMODE(os.lstat(path).st_mode)


# ---------------------------------------------------------------------------
# Tests: subdirectory existence
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("subdir", EXPECTED_SUBDIRS)
def test_subdirectory_exists(subdir):
    path = os.path.join(PROJECT_DIR, subdir)
    assert os.path.isdir(path), (
        f"Expected subdirectory '{path}' does not exist. "
        "Make sure you created it and moved the appropriate files into it."
    )


# ---------------------------------------------------------------------------
# Tests: files exist in correct locations with correct permissions
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rel_path,expected_mode", EXPECTED_FILES.items())
def test_file_exists(rel_path, expected_mode):
    abs_path = os.path.join(PROJECT_DIR, rel_path)
    assert os.path.isfile(abs_path) and not os.path.islink(abs_path), (
        f"Expected regular file '{abs_path}' does not exist (or is a symlink). "
        "Make sure the file was moved to the correct subdirectory."
    )


@pytest.mark.parametrize("rel_path,expected_mode", EXPECTED_FILES.items())
def test_file_permissions(rel_path, expected_mode):
    abs_path = os.path.join(PROJECT_DIR, rel_path)
    if not os.path.exists(abs_path):
        pytest.skip(f"File '{abs_path}' does not exist; skipping permission check.")
    actual = octal_perms(abs_path)
    assert actual == expected_mode, (
        f"File '{abs_path}' has permissions {oct(actual)} "
        f"but expected {oct(expected_mode)}. "
        "Please set the correct permissions."
    )


# ---------------------------------------------------------------------------
# Tests: no original loose files remain in project root
# ---------------------------------------------------------------------------

ORIGINAL_FILES = [
    "main.c", "utils.c", "parser.c", "utils.h", "parser.h", "config.h",
    "build.py", "deploy.py", "test_runner.py",
    "README.md", "CHANGELOG.md", "API.md",
    "app.conf", "db.conf", "logging.conf",
    "app.log", "error.log", "debug.log",
    "seed.sql", "schema.sql", "fixtures.json",
]


@pytest.mark.parametrize("filename", ORIGINAL_FILES)
def test_original_file_not_in_root(filename):
    path = os.path.join(PROJECT_DIR, filename)
    assert not os.path.exists(path) and not os.path.islink(path), (
        f"Original file '{path}' still exists in the project root. "
        "It should have been moved to the appropriate subdirectory."
    )


# ---------------------------------------------------------------------------
# Tests: symlinks
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("link_name,expected_target", EXPECTED_SYMLINKS.items())
def test_symlink_exists(link_name, expected_target):
    link_path = os.path.join(PROJECT_DIR, link_name)
    assert os.path.islink(link_path), (
        f"Expected symlink '{link_path}' does not exist. "
        "Make sure you created the symlink."
    )


@pytest.mark.parametrize("link_name,expected_target", EXPECTED_SYMLINKS.items())
def test_symlink_target(link_name, expected_target):
    link_path = os.path.join(PROJECT_DIR, link_name)
    if not os.path.islink(link_path):
        pytest.skip(f"Symlink '{link_path}' does not exist; skipping target check.")
    actual_target = os.readlink(link_path)
    assert actual_target == expected_target, (
        f"Symlink '{link_path}' points to '{actual_target}' "
        f"but should point to '{expected_target}' (relative path). "
        "Please recreate the symlink with the correct relative target."
    )


@pytest.mark.parametrize("link_name,expected_target", EXPECTED_SYMLINKS.items())
def test_symlink_resolves(link_name, expected_target):
    link_path = os.path.join(PROJECT_DIR, link_name)
    if not os.path.islink(link_path):
        pytest.skip(f"Symlink '{link_path}' does not exist; skipping resolution check.")
    assert os.path.exists(link_path), (
        f"Symlink '{link_path}' -> '{os.readlink(link_path)}' is broken "
        "(the target does not exist). "
        "Make sure the target file is in place."
    )


# ---------------------------------------------------------------------------
# Tests: project root contains exactly the right entries
# ---------------------------------------------------------------------------

def test_project_root_contents():
    """Project root should contain only: subdirs, three symlinks, and manifest.txt."""
    allowed = set(EXPECTED_SUBDIRS) | set(EXPECTED_SYMLINKS.keys()) | {"manifest.txt"}
    entries = set(os.listdir(PROJECT_DIR))
    unexpected = entries - allowed
    assert not unexpected, (
        f"Unexpected entries found in '{PROJECT_DIR}': {sorted(unexpected)}. "
        "The project root should only contain the six subdirectories, "
        "three symlinks (project.conf, run.py, latest.log), and manifest.txt."
    )


# ---------------------------------------------------------------------------
# Tests: manifest.txt
# ---------------------------------------------------------------------------

def test_manifest_exists():
    manifest_path = os.path.join(PROJECT_DIR, "manifest.txt")
    assert os.path.isfile(manifest_path) and not os.path.islink(manifest_path), (
        f"'{manifest_path}' does not exist or is not a regular file. "
        "Please generate the manifest file."
    )


def test_manifest_content():
    manifest_path = os.path.join(PROJECT_DIR, "manifest.txt")
    if not os.path.isfile(manifest_path):
        pytest.skip("manifest.txt does not exist; skipping content check.")

    with open(manifest_path, "r") as f:
        content = f.read()

    # Strip trailing newline and split into lines
    actual_lines = content.rstrip("\n").split("\n")
    # Remove any blank lines
    actual_lines = [line for line in actual_lines if line.strip()]

    assert actual_lines == EXPECTED_MANIFEST_LINES, (
        f"manifest.txt content does not match expected.\n"
        f"Expected ({len(EXPECTED_MANIFEST_LINES)} lines):\n"
        + "\n".join(EXPECTED_MANIFEST_LINES)
        + f"\n\nActual ({len(actual_lines)} lines):\n"
        + "\n".join(actual_lines)
        + "\n\nMake sure:\n"
        "  - Paths are relative to /home/user/project/ and use forward slashes\n"
        "  - Permissions are 3-digit octal (e.g., 644, not 0o644)\n"
        "  - Entries are sorted strictly alphabetically by path\n"
        "  - manifest.txt itself is NOT listed\n"
        "  - Symlinks are NOT listed\n"
        "  - Only regular files are listed"
    )


def test_manifest_excludes_itself():
    manifest_path = os.path.join(PROJECT_DIR, "manifest.txt")
    if not os.path.isfile(manifest_path):
        pytest.skip("manifest.txt does not exist; skipping self-exclusion check.")
    with open(manifest_path, "r") as f:
        content = f.read()
    assert "manifest.txt" not in content, (
        "manifest.txt should NOT list itself inside the manifest."
    )


def test_manifest_excludes_symlinks():
    manifest_path = os.path.join(PROJECT_DIR, "manifest.txt")
    if not os.path.isfile(manifest_path):
        pytest.skip("manifest.txt does not exist; skipping symlink-exclusion check.")
    with open(manifest_path, "r") as f:
        content = f.read()
    for link_name in EXPECTED_SYMLINKS:
        assert link_name not in content, (
            f"manifest.txt should NOT include the symlink '{link_name}'. "
            "Only regular files should be listed."
        )


def test_manifest_line_count():
    manifest_path = os.path.join(PROJECT_DIR, "manifest.txt")
    if not os.path.isfile(manifest_path):
        pytest.skip("manifest.txt does not exist; skipping line-count check.")
    with open(manifest_path, "r") as f:
        content = f.read()
    actual_lines = [line for line in content.rstrip("\n").split("\n") if line.strip()]
    assert len(actual_lines) == 21, (
        f"manifest.txt should have exactly 21 lines (one per regular file), "
        f"but found {len(actual_lines)} lines."
    )


def test_manifest_format():
    """Each line in manifest.txt must be '<relative/path> <3-digit-octal>'."""
    manifest_path = os.path.join(PROJECT_DIR, "manifest.txt")
    if not os.path.isfile(manifest_path):
        pytest.skip("manifest.txt does not exist; skipping format check.")
    with open(manifest_path, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    import re
    pattern = re.compile(r'^[a-zA-Z0-9_./-]+ [0-7]{3}$')
    bad_lines = [line for line in lines if not pattern.match(line)]
    assert not bad_lines, (
        f"The following lines in manifest.txt do not match the expected format "
        f"'<path> <3-digit-octal>':\n" + "\n".join(bad_lines)
    )


def test_manifest_no_leading_dot_slash():
    manifest_path = os.path.join(PROJECT_DIR, "manifest.txt")
    if not os.path.isfile(manifest_path):
        pytest.skip("manifest.txt does not exist; skipping path-format check.")
    with open(manifest_path, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    bad = [line for line in lines if line.startswith("./")]
    assert not bad, (
        f"Paths in manifest.txt must NOT start with './'. Offending lines:\n"
        + "\n".join(bad)
    )