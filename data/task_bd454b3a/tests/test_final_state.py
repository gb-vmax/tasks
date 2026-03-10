# test_final_state.py

import os
import gzip
import pytest

WEBAPP = "/home/user/webapp"
DEPLOYMENT_MARKER = "<!-- deployed: v2.4.1 -->"


def full(rel):
    return os.path.join(WEBAPP, rel)


# ---------------------------------------------------------------------------
# Task 1: Deleted stale cache and backup files
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rel_path", [
    "tmp/session.cache",
    "tmp/query.cache",
    "tmp/index.html.bak",
    "src/app.js.bak",
])
def test_stale_files_deleted(rel_path):
    path = full(rel_path)
    assert not os.path.exists(path), (
        f"Stale file {path} should have been deleted but still exists."
    )


def test_no_cache_files_anywhere():
    """No .cache files should exist anywhere under /home/user/webapp."""
    found = []
    for dirpath, dirnames, filenames in os.walk(WEBAPP):
        for fname in filenames:
            if fname.endswith(".cache"):
                found.append(os.path.join(dirpath, fname))
    assert found == [], (
        f"Found .cache files that should have been deleted: {found}"
    )


def test_no_bak_files_anywhere():
    """No .bak files should exist anywhere under /home/user/webapp."""
    found = []
    for dirpath, dirnames, filenames in os.walk(WEBAPP):
        for fname in filenames:
            if fname.endswith(".bak"):
                found.append(os.path.join(dirpath, fname))
    assert found == [], (
        f"Found .bak files that should have been deleted: {found}"
    )


# ---------------------------------------------------------------------------
# Task 2: Compress all .log files
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rel_log", [
    "logs/access.log",
    "logs/error.log",
])
def test_original_log_file_gone(rel_log):
    path = full(rel_log)
    assert not os.path.exists(path), (
        f"Original log file {path} should have been compressed (removed) but still exists."
    )


@pytest.mark.parametrize("rel_log_gz", [
    "logs/access.log.gz",
    "logs/error.log.gz",
])
def test_compressed_log_file_exists(rel_log_gz):
    path = full(rel_log_gz)
    assert os.path.isfile(path), (
        f"Compressed log file {path} should exist but does not."
    )


def test_compressed_log_files_are_valid_gzip():
    """Verify the .gz files are valid gzip archives."""
    for rel in ["logs/access.log.gz", "logs/error.log.gz"]:
        path = full(rel)
        assert os.path.isfile(path), f"Compressed log file {path} does not exist."
        try:
            with gzip.open(path, "rb") as f:
                data = f.read()
            assert len(data) > 0, f"Compressed file {path} appears to be empty."
        except Exception as e:
            pytest.fail(f"File {path} is not a valid gzip file: {e}")


def test_no_uncompressed_log_files_anywhere():
    """No .log files (uncompressed) should exist anywhere under /home/user/webapp."""
    found = []
    for dirpath, dirnames, filenames in os.walk(WEBAPP):
        for fname in filenames:
            if fname.endswith(".log") and not fname.endswith(".log.gz"):
                found.append(os.path.join(dirpath, fname))
    assert found == [], (
        f"Found uncompressed .log files that should have been gzipped: {found}"
    )


# ---------------------------------------------------------------------------
# Task 3: Deployment marker injected into every .html file
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rel_path", [
    "index.html",
    "about.html",
    "src/pages/contact.html",
])
def test_html_has_deployment_marker(rel_path):
    path = full(rel_path)
    assert os.path.isfile(path), f"HTML file {path} does not exist."
    content = open(path).read()
    assert DEPLOYMENT_MARKER in content, (
        f"HTML file {path} does not contain the deployment marker '{DEPLOYMENT_MARKER}'."
    )


@pytest.mark.parametrize("rel_path", [
    "index.html",
    "about.html",
    "src/pages/contact.html",
])
def test_html_deployment_marker_is_final_line(rel_path):
    path = full(rel_path)
    assert os.path.isfile(path), f"HTML file {path} does not exist."
    content = open(path).read()
    # The file must end with the marker followed by a newline (complete line)
    lines = content.splitlines()
    assert lines, f"HTML file {path} appears to be empty."
    last_line = lines[-1]
    assert last_line == DEPLOYMENT_MARKER, (
        f"HTML file {path}: expected last line to be '{DEPLOYMENT_MARKER}', "
        f"but got '{last_line}'."
    )
    # Also verify the file ends with a newline (marker is a complete line)
    assert content.endswith(DEPLOYMENT_MARKER + "\n"), (
        f"HTML file {path}: the deployment marker must be followed by a newline. "
        f"File ends with: {content[-50:]!r}"
    )


def test_all_html_files_have_marker():
    """Every .html file under /home/user/webapp must have the deployment marker as last line."""
    html_files = []
    for dirpath, dirnames, filenames in os.walk(WEBAPP):
        for fname in filenames:
            if fname.endswith(".html"):
                html_files.append(os.path.join(dirpath, fname))

    assert html_files, "No .html files found under /home/user/webapp."

    failures = []
    for path in html_files:
        content = open(path).read()
        lines = content.splitlines()
        if not lines or lines[-1] != DEPLOYMENT_MARKER:
            failures.append(path)

    assert failures == [], (
        f"The following HTML files do not have '{DEPLOYMENT_MARKER}' as their final line: {failures}"
    )


# ---------------------------------------------------------------------------
# Task 4: deploy_manifest.txt exists with correct content
# ---------------------------------------------------------------------------

MANIFEST_PATH = full("deploy_manifest.txt")

EXPECTED_MANIFEST = """\
=== Deploy Manifest ===
assets/css/main.css
assets/css/reset.css
assets/js/app.js
assets/js/vendor.js
src/components/widget.js
src/styles/theme.css
=== Total: 6 files ==="""


def test_deploy_manifest_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"deploy_manifest.txt does not exist at {MANIFEST_PATH}."
    )


def test_deploy_manifest_header():
    assert os.path.isfile(MANIFEST_PATH), f"{MANIFEST_PATH} does not exist."
    lines = open(MANIFEST_PATH).read().splitlines()
    assert lines, "deploy_manifest.txt is empty."
    assert lines[0] == "=== Deploy Manifest ===", (
        f"First line of deploy_manifest.txt should be '=== Deploy Manifest ===' "
        f"but got: {lines[0]!r}"
    )


def test_deploy_manifest_footer():
    assert os.path.isfile(MANIFEST_PATH), f"{MANIFEST_PATH} does not exist."
    lines = open(MANIFEST_PATH).read().splitlines()
    assert lines, "deploy_manifest.txt is empty."
    assert lines[-1] == "=== Total: 6 files ===", (
        f"Last line of deploy_manifest.txt should be '=== Total: 6 files ===' "
        f"but got: {lines[-1]!r}"
    )


def test_deploy_manifest_file_list():
    assert os.path.isfile(MANIFEST_PATH), f"{MANIFEST_PATH} does not exist."
    lines = open(MANIFEST_PATH).read().splitlines()
    # Extract the file list (between header and footer)
    assert len(lines) >= 2, "deploy_manifest.txt has too few lines."
    file_lines = lines[1:-1]
    expected_files = [
        "assets/css/main.css",
        "assets/css/reset.css",
        "assets/js/app.js",
        "assets/js/vendor.js",
        "src/components/widget.js",
        "src/styles/theme.css",
    ]
    assert file_lines == expected_files, (
        f"File list in deploy_manifest.txt is incorrect.\n"
        f"Expected:\n{chr(10).join(expected_files)}\n"
        f"Got:\n{chr(10).join(file_lines)}"
    )


def test_deploy_manifest_exact_content():
    assert os.path.isfile(MANIFEST_PATH), f"{MANIFEST_PATH} does not exist."
    actual = open(MANIFEST_PATH).read().strip()
    expected = EXPECTED_MANIFEST.strip()
    assert actual == expected, (
        f"deploy_manifest.txt content does not match expected.\n"
        f"Expected:\n{expected}\n"
        f"Got:\n{actual}"
    )


def test_deploy_manifest_sorted_order():
    """Verify that the file entries in the manifest are sorted alphabetically."""
    assert os.path.isfile(MANIFEST_PATH), f"{MANIFEST_PATH} does not exist."
    lines = open(MANIFEST_PATH).read().splitlines()
    assert len(lines) >= 2, "deploy_manifest.txt has too few lines."
    file_lines = lines[1:-1]
    assert file_lines == sorted(file_lines), (
        f"File entries in deploy_manifest.txt are not sorted alphabetically.\n"
        f"Got: {file_lines}\n"
        f"Expected sorted: {sorted(file_lines)}"
    )


def test_deploy_manifest_count_matches_listed_files():
    """The footer count must match the number of file lines listed."""
    assert os.path.isfile(MANIFEST_PATH), f"{MANIFEST_PATH} does not exist."
    lines = open(MANIFEST_PATH).read().splitlines()
    assert len(lines) >= 2, "deploy_manifest.txt has too few lines."
    file_lines = lines[1:-1]
    footer = lines[-1]
    # Parse N from footer
    import re
    match = re.match(r"=== Total: (\d+) files ===", footer)
    assert match, f"Footer line does not match expected format: {footer!r}"
    n = int(match.group(1))
    assert n == len(file_lines), (
        f"Footer says {n} files but {len(file_lines)} file lines are listed."
    )


def test_deploy_manifest_not_included_in_itself():
    """deploy_manifest.txt should not list itself."""
    assert os.path.isfile(MANIFEST_PATH), f"{MANIFEST_PATH} does not exist."
    lines = open(MANIFEST_PATH).read().splitlines()
    file_lines = lines[1:-1]
    assert "deploy_manifest.txt" not in file_lines, (
        "deploy_manifest.txt should not list itself in the manifest."
    )


# ---------------------------------------------------------------------------
# Verify key source files still exist (not accidentally deleted)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rel_path", [
    "index.html",
    "about.html",
    "assets/css/main.css",
    "assets/css/reset.css",
    "assets/js/app.js",
    "assets/js/vendor.js",
    "src/components/widget.js",
    "src/pages/contact.html",
    "src/styles/theme.css",
])
def test_source_files_still_exist(rel_path):
    path = full(rel_path)
    assert os.path.isfile(path), (
        f"Source file {path} should still exist after cleanup but does not."
    )