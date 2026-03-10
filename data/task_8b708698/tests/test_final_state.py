# test_final_state.py

import os
import pytest

CHANGES_PATH = "/home/user/configs/changes.txt"
V1_PATH = "/home/user/configs/app.conf.v1"
V2_PATH = "/home/user/configs/app.conf.v2"

EXPECTED_CONTENT = """\
CONFIG CHANGE REPORT
====================
REMOVED:
  - port=8080
  - debug=true
  - timeout=30
  - log_level=info
ADDED:
  - port=9090
  - debug=false
  - timeout=60
  - log_level=warn
  - workers=4
====================
Total changes: 9
"""


def test_output_file_exists():
    assert os.path.isfile(CHANGES_PATH), (
        f"Output file '{CHANGES_PATH}' does not exist. "
        "The task requires generating a change report at this path."
    )


def test_output_file_readable():
    assert os.access(CHANGES_PATH, os.R_OK), (
        f"Output file '{CHANGES_PATH}' exists but is not readable."
    )


def test_output_file_exact_content():
    with open(CHANGES_PATH, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_CONTENT, (
        f"Content of '{CHANGES_PATH}' does not match expected.\n"
        f"Expected:\n{EXPECTED_CONTENT!r}\n"
        f"Got:\n{actual!r}"
    )


def test_output_file_ends_with_newline():
    with open(CHANGES_PATH, "r") as f:
        actual = f.read()
    assert actual.endswith("\n"), (
        f"Output file '{CHANGES_PATH}' must end with a newline character. "
        f"Got:\n{actual!r}"
    )


def test_output_file_header_line():
    with open(CHANGES_PATH, "r") as f:
        lines = f.readlines()
    assert lines[0].rstrip("\n") == "CONFIG CHANGE REPORT", (
        f"First line of '{CHANGES_PATH}' must be 'CONFIG CHANGE REPORT'. "
        f"Got: {lines[0]!r}"
    )


def test_output_file_separator_lines():
    with open(CHANGES_PATH, "r") as f:
        lines = f.readlines()
    assert lines[1].rstrip("\n") == "=" * 20, (
        f"Second line of '{CHANGES_PATH}' must be '====================' (20 equals signs). "
        f"Got: {lines[1]!r}"
    )
    # Find the last separator
    last_sep_index = None
    for i, line in enumerate(lines):
        if line.rstrip("\n") == "=" * 20:
            last_sep_index = i
    assert last_sep_index is not None and last_sep_index > 1, (
        f"There must be a closing '====================' separator line in '{CHANGES_PATH}'."
    )


def test_output_file_removed_section():
    with open(CHANGES_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()

    assert "REMOVED:" in lines, (
        f"'REMOVED:' section header not found in '{CHANGES_PATH}'."
    )

    removed_start = lines.index("REMOVED:") + 1
    removed_lines = []
    for line in lines[removed_start:]:
        if line.startswith("  - "):
            removed_lines.append(line[4:])
        else:
            break

    expected_removed = ["port=8080", "debug=true", "timeout=30", "log_level=info"]
    assert removed_lines == expected_removed, (
        f"REMOVED section in '{CHANGES_PATH}' does not match expected.\n"
        f"Expected entries: {expected_removed}\n"
        f"Got entries: {removed_lines}"
    )


def test_output_file_added_section():
    with open(CHANGES_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()

    assert "ADDED:" in lines, (
        f"'ADDED:' section header not found in '{CHANGES_PATH}'."
    )

    added_start = lines.index("ADDED:") + 1
    added_lines = []
    for line in lines[added_start:]:
        if line.startswith("  - "):
            added_lines.append(line[4:])
        else:
            break

    expected_added = ["port=9090", "debug=false", "timeout=60", "log_level=warn", "workers=4"]
    assert added_lines == expected_added, (
        f"ADDED section in '{CHANGES_PATH}' does not match expected.\n"
        f"Expected entries: {expected_added}\n"
        f"Got entries: {added_lines}"
    )


def test_output_file_total_changes_line():
    with open(CHANGES_PATH, "r") as f:
        lines = f.readlines()

    # The total changes line should be the last non-empty line
    stripped_lines = [line.rstrip("\n") for line in lines]
    # Remove trailing empty strings
    while stripped_lines and stripped_lines[-1] == "":
        stripped_lines.pop()

    last_line = stripped_lines[-1]
    assert last_line == "Total changes: 9", (
        f"Last line of '{CHANGES_PATH}' must be 'Total changes: 9'. "
        f"Got: {last_line!r}"
    )


def test_output_file_section_order():
    with open(CHANGES_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()

    assert "REMOVED:" in lines, f"'REMOVED:' not found in '{CHANGES_PATH}'."
    assert "ADDED:" in lines, f"'ADDED:' not found in '{CHANGES_PATH}'."

    removed_index = lines.index("REMOVED:")
    added_index = lines.index("ADDED:")

    assert removed_index < added_index, (
        f"'REMOVED:' section must appear before 'ADDED:' section in '{CHANGES_PATH}'. "
        f"REMOVED: at line {removed_index + 1}, ADDED: at line {added_index + 1}."
    )


def test_source_files_unchanged():
    """Ensure the source config files were not modified during the task."""
    expected_v1 = (
        "host=localhost\n"
        "port=8080\n"
        "debug=true\n"
        "max_connections=100\n"
        "timeout=30\n"
        "log_level=info\n"
    )
    expected_v2 = (
        "host=localhost\n"
        "port=9090\n"
        "debug=false\n"
        "max_connections=100\n"
        "timeout=60\n"
        "log_level=warn\n"
        "workers=4\n"
    )

    with open(V1_PATH, "r") as f:
        v1_content = f.read()
    assert v1_content.rstrip("\n") == expected_v1.rstrip("\n"), (
        f"Source file '{V1_PATH}' was unexpectedly modified.\n"
        f"Expected:\n{expected_v1!r}\nGot:\n{v1_content!r}"
    )

    with open(V2_PATH, "r") as f:
        v2_content = f.read()
    assert v2_content.rstrip("\n") == expected_v2.rstrip("\n"), (
        f"Source file '{V2_PATH}' was unexpectedly modified.\n"
        f"Expected:\n{expected_v2!r}\nGot:\n{v2_content!r}"
    )