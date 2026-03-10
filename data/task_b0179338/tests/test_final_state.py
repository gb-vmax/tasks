# test_final_state.py

import os
import pytest

SOURCE_FILE = "/home/user/docs/api_endpoints.txt"
INDEX_FILE = "/home/user/docs/endpoints_index.txt"
GET_FILE = "/home/user/docs/get_endpoints.txt"
SUMMARY_FILE = "/home/user/docs/endpoints_summary.txt"

EXPECTED_INDEX_CONTENT = """\
/api/orders
/api/orders/{id}
/api/products
/api/products/{id}
/api/users
/api/users/{id}"""

EXPECTED_GET_CONTENT = """\
[GET] /api/users - Retrieve list of all users
[GET] /api/products - List all products
[GET] /api/orders - List all orders
[GET] /api/orders/{id} - Retrieve a specific order
[GET] /api/users/{id} - Retrieve a specific user"""

EXPECTED_SUMMARY_CONTENT = """\
DELETE: 2
GET: 5
POST: 3
PUT: 2"""


# ── helpers ──────────────────────────────────────────────────────────────────

def read_stripped(path):
    """Read a file and strip a single trailing newline (if present)."""
    with open(path, "r") as fh:
        return fh.read().rstrip("\n")


# ── source file still intact ─────────────────────────────────────────────────

def test_source_file_still_exists():
    assert os.path.isfile(SOURCE_FILE), (
        f"Source file '{SOURCE_FILE}' has been removed or is no longer a regular file."
    )


# ── endpoints_index.txt ───────────────────────────────────────────────────────

def test_index_file_exists():
    assert os.path.isfile(INDEX_FILE), (
        f"Index file '{INDEX_FILE}' does not exist. "
        "The task requires creating this file with sorted, unique endpoint paths."
    )


def test_index_file_is_readable():
    assert os.access(INDEX_FILE, os.R_OK), (
        f"Index file '{INDEX_FILE}' exists but is not readable."
    )


def test_index_file_content():
    actual = read_stripped(INDEX_FILE)
    assert actual == EXPECTED_INDEX_CONTENT, (
        f"Content of '{INDEX_FILE}' is incorrect.\n\n"
        f"Expected:\n{EXPECTED_INDEX_CONTENT}\n\n"
        f"Got:\n{actual}"
    )


def test_index_file_line_count():
    with open(INDEX_FILE, "r") as fh:
        lines = [ln.rstrip("\n") for ln in fh if ln.strip()]
    assert len(lines) == 6, (
        f"Expected 6 unique paths in '{INDEX_FILE}', but found {len(lines)}.\n"
        f"Lines found: {lines}"
    )


def test_index_file_no_duplicates():
    with open(INDEX_FILE, "r") as fh:
        lines = [ln.strip() for ln in fh if ln.strip()]
    assert len(lines) == len(set(lines)), (
        f"'{INDEX_FILE}' contains duplicate paths.\nLines: {lines}"
    )


def test_index_file_sorted():
    with open(INDEX_FILE, "r") as fh:
        lines = [ln.strip() for ln in fh if ln.strip()]
    assert lines == sorted(lines), (
        f"Paths in '{INDEX_FILE}' are not in alphabetical order.\n"
        f"Found:    {lines}\n"
        f"Expected: {sorted(lines)}"
    )


def test_index_file_paths_only():
    """Each line must be a bare path (starts with '/'), no method or description."""
    with open(INDEX_FILE, "r") as fh:
        lines = [ln.strip() for ln in fh if ln.strip()]
    for line in lines:
        assert line.startswith("/"), (
            f"Line in '{INDEX_FILE}' does not look like a bare path: {line!r}"
        )
        assert "[" not in line and "]" not in line, (
            f"Line in '{INDEX_FILE}' still contains method brackets: {line!r}"
        )
        assert " - " not in line, (
            f"Line in '{INDEX_FILE}' still contains a description separator: {line!r}"
        )


def test_index_file_expected_paths():
    expected_paths = {
        "/api/orders",
        "/api/orders/{id}",
        "/api/products",
        "/api/products/{id}",
        "/api/users",
        "/api/users/{id}",
    }
    with open(INDEX_FILE, "r") as fh:
        actual_paths = {ln.strip() for ln in fh if ln.strip()}
    assert actual_paths == expected_paths, (
        f"Paths in '{INDEX_FILE}' do not match expected unique paths.\n"
        f"Expected: {sorted(expected_paths)}\n"
        f"Got:      {sorted(actual_paths)}"
    )


# ── get_endpoints.txt ─────────────────────────────────────────────────────────

def test_get_file_exists():
    assert os.path.isfile(GET_FILE), (
        f"GET endpoints file '{GET_FILE}' does not exist. "
        "The task requires creating this file with only GET lines from the source."
    )


def test_get_file_is_readable():
    assert os.access(GET_FILE, os.R_OK), (
        f"GET endpoints file '{GET_FILE}' exists but is not readable."
    )


def test_get_file_content():
    actual = read_stripped(GET_FILE)
    assert actual == EXPECTED_GET_CONTENT, (
        f"Content of '{GET_FILE}' is incorrect.\n\n"
        f"Expected:\n{EXPECTED_GET_CONTENT}\n\n"
        f"Got:\n{actual}"
    )


def test_get_file_line_count():
    with open(GET_FILE, "r") as fh:
        lines = [ln.rstrip("\n") for ln in fh if ln.strip()]
    assert len(lines) == 5, (
        f"Expected 5 GET lines in '{GET_FILE}', but found {len(lines)}.\n"
        f"Lines: {lines}"
    )


def test_get_file_only_get_methods():
    with open(GET_FILE, "r") as fh:
        lines = [ln.strip() for ln in fh if ln.strip()]
    for line in lines:
        assert line.startswith("[GET]"), (
            f"Non-GET line found in '{GET_FILE}': {line!r}"
        )


def test_get_file_preserves_original_format():
    """Lines must match the full original format: [METHOD] /path - Description."""
    with open(GET_FILE, "r") as fh:
        lines = [ln.strip() for ln in fh if ln.strip()]
    for line in lines:
        assert " - " in line, (
            f"Line in '{GET_FILE}' is missing the ' - ' separator (format changed?): {line!r}"
        )
        assert line.startswith("[GET] /"), (
            f"Line in '{GET_FILE}' does not start with '[GET] /': {line!r}"
        )


def test_get_file_order_matches_source():
    """GET lines must appear in the same relative order as in the source file."""
    with open(SOURCE_FILE, "r") as fh:
        source_get_lines = [ln.rstrip("\n") for ln in fh if ln.startswith("[GET]")]
    with open(GET_FILE, "r") as fh:
        get_file_lines = [ln.rstrip("\n") for ln in fh if ln.strip()]
    assert get_file_lines == source_get_lines, (
        f"GET lines in '{GET_FILE}' are not in the same order as in the source.\n"
        f"Expected order: {source_get_lines}\n"
        f"Got:            {get_file_lines}"
    )


# ── endpoints_summary.txt ─────────────────────────────────────────────────────

def test_summary_file_exists():
    assert os.path.isfile(SUMMARY_FILE), (
        f"Summary file '{SUMMARY_FILE}' does not exist. "
        "The task requires creating this file with per-method counts."
    )


def test_summary_file_is_readable():
    assert os.access(SUMMARY_FILE, os.R_OK), (
        f"Summary file '{SUMMARY_FILE}' exists but is not readable."
    )


def test_summary_file_content():
    actual = read_stripped(SUMMARY_FILE)
    assert actual == EXPECTED_SUMMARY_CONTENT, (
        f"Content of '{SUMMARY_FILE}' is incorrect.\n\n"
        f"Expected:\n{EXPECTED_SUMMARY_CONTENT}\n\n"
        f"Got:\n{actual}"
    )


def test_summary_file_line_count():
    with open(SUMMARY_FILE, "r") as fh:
        lines = [ln.rstrip("\n") for ln in fh if ln.strip()]
    assert len(lines) == 4, (
        f"Expected 4 lines in '{SUMMARY_FILE}' (one per method present), "
        f"but found {len(lines)}.\nLines: {lines}"
    )


def test_summary_file_format():
    """Every line must match 'METHOD: N' with no extra spaces."""
    with open(SUMMARY_FILE, "r") as fh:
        lines = [ln.rstrip("\n") for ln in fh if ln.strip()]
    import re
    pattern = re.compile(r'^[A-Z]+: \d+$')
    for line in lines:
        assert pattern.match(line), (
            f"Line in '{SUMMARY_FILE}' does not match 'METHOD: N' format: {line!r}"
        )


def test_summary_file_counts():
    expected = {"DELETE": 2, "GET": 5, "POST": 3, "PUT": 2}
    with open(SUMMARY_FILE, "r") as fh:
        lines = [ln.strip() for ln in fh if ln.strip()]
    actual = {}
    for line in lines:
        method, count = line.split(": ")
        actual[method] = int(count)
    assert actual == expected, (
        f"Method counts in '{SUMMARY_FILE}' are wrong.\n"
        f"Expected: {expected}\n"
        f"Got:      {actual}"
    )


def test_summary_file_alphabetical_order():
    with open(SUMMARY_FILE, "r") as fh:
        lines = [ln.strip() for ln in fh if ln.strip()]
    methods = [ln.split(": ")[0] for ln in lines]
    assert methods == sorted(methods), (
        f"Methods in '{SUMMARY_FILE}' are not in alphabetical order.\n"
        f"Found:    {methods}\n"
        f"Expected: {sorted(methods)}"
    )


def test_summary_file_no_zero_counts():
    with open(SUMMARY_FILE, "r") as fh:
        lines = [ln.strip() for ln in fh if ln.strip()]
    for line in lines:
        method, count = line.split(": ")
        assert int(count) > 0, (
            f"Method '{method}' in '{SUMMARY_FILE}' has a count of 0; "
            "methods with zero occurrences should be omitted."
        )