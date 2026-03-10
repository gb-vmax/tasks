# test_final_state.py

import os
import pytest

WORKSPACE_DIR = "/home/user/workspace"
MANIFEST_FILE = "/home/user/workspace/manifest.txt"

SYMLINKS = [
    ("sales_q1.csv", "/home/user/data/quarterly/q1_sales_data.csv"),
    ("sales_q2.csv", "/home/user/data/quarterly/q2_sales_data.csv"),
    ("customers.csv", "/home/user/data/customers/master_customers.csv"),
]

EXPECTED_MANIFEST_LINES = [
    "sales_q1.csv -> /home/user/data/quarterly/q1_sales_data.csv",
    "sales_q2.csv -> /home/user/data/quarterly/q2_sales_data.csv",
    "customers.csv -> /home/user/data/customers/master_customers.csv",
]


# ---------------------------------------------------------------------------
# 1. Workspace directory
# ---------------------------------------------------------------------------

def test_workspace_directory_exists():
    """The workspace directory must exist."""
    assert os.path.isdir(WORKSPACE_DIR), (
        f"Workspace directory does not exist: {WORKSPACE_DIR}\n"
        "Create it with: mkdir -p /home/user/workspace"
    )


# ---------------------------------------------------------------------------
# 2. Symlinks – existence, type, target, and resolution
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("link_name,target", SYMLINKS)
def test_symlink_exists(link_name, target):
    """Each expected symlink must exist inside the workspace."""
    link_path = os.path.join(WORKSPACE_DIR, link_name)
    assert os.path.lexists(link_path), (
        f"Symlink does not exist: {link_path}\n"
        f"Expected a symlink pointing to {target}"
    )


@pytest.mark.parametrize("link_name,target", SYMLINKS)
def test_symlink_is_symlink(link_name, target):
    """Each entry must be a symbolic link (not a regular file or directory)."""
    link_path = os.path.join(WORKSPACE_DIR, link_name)
    assert os.path.islink(link_path), (
        f"{link_path} exists but is NOT a symbolic link.\n"
        "Remove the file/directory and create a proper symlink."
    )


@pytest.mark.parametrize("link_name,target", SYMLINKS)
def test_symlink_target_is_absolute(link_name, target):
    """The symlink target must be an absolute path."""
    link_path = os.path.join(WORKSPACE_DIR, link_name)
    actual_target = os.readlink(link_path)
    assert os.path.isabs(actual_target), (
        f"Symlink {link_path} uses a relative target: '{actual_target}'\n"
        f"Expected absolute target: {target}"
    )


@pytest.mark.parametrize("link_name,target", SYMLINKS)
def test_symlink_points_to_correct_target(link_name, target):
    """Each symlink must point to the exact absolute target path specified."""
    link_path = os.path.join(WORKSPACE_DIR, link_name)
    actual_target = os.readlink(link_path)
    assert actual_target == target, (
        f"Symlink {link_path} points to wrong target.\n"
        f"  Expected: {target}\n"
        f"  Actual:   {actual_target}"
    )


@pytest.mark.parametrize("link_name,target", SYMLINKS)
def test_symlink_resolves_to_real_file(link_name, target):
    """Each symlink must resolve to an existing regular file (test -f equivalent)."""
    link_path = os.path.join(WORKSPACE_DIR, link_name)
    assert os.path.isfile(link_path), (
        f"Symlink {link_path} does not resolve to a real file.\n"
        f"Target path '{target}' may not exist or may not be a regular file."
    )


@pytest.mark.parametrize("link_name,target", SYMLINKS)
def test_symlink_target_is_readable(link_name, target):
    """The file referenced by each symlink must be readable."""
    link_path = os.path.join(WORKSPACE_DIR, link_name)
    assert os.access(link_path, os.R_OK), (
        f"Symlink {link_path} resolves to a file that is not readable: {target}"
    )


# ---------------------------------------------------------------------------
# 3. Manifest file
# ---------------------------------------------------------------------------

def test_manifest_file_exists():
    """The manifest file must exist at the specified path."""
    assert os.path.isfile(MANIFEST_FILE), (
        f"Manifest file does not exist: {MANIFEST_FILE}\n"
        "Create it with the required 3-line format."
    )


def test_manifest_file_is_regular_file():
    """The manifest must be a regular file, not a symlink or directory."""
    assert not os.path.islink(MANIFEST_FILE), (
        f"{MANIFEST_FILE} is a symlink; it must be a regular plain-text file."
    )
    assert os.path.isfile(MANIFEST_FILE), (
        f"{MANIFEST_FILE} is not a regular file."
    )


def test_manifest_line_count():
    """The manifest file must contain exactly 3 lines."""
    with open(MANIFEST_FILE, "r") as f:
        content = f.read()
    # Strip a single trailing newline if present, then split
    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 3, (
        f"manifest.txt must have exactly 3 lines, found {len(lines)}.\n"
        f"Actual content:\n{content!r}"
    )


def test_manifest_no_blank_lines():
    """The manifest file must not contain blank lines."""
    with open(MANIFEST_FILE, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"manifest.txt contains blank lines at positions: {blank_lines}\n"
        "No blank lines are allowed."
    )


def test_manifest_exact_content():
    """The manifest file must contain exactly the expected 3 lines in order."""
    with open(MANIFEST_FILE, "r") as f:
        content = f.read()
    actual_lines = content.rstrip("\n").split("\n")
    expected_content = "\n".join(EXPECTED_MANIFEST_LINES)
    assert actual_lines == EXPECTED_MANIFEST_LINES, (
        f"manifest.txt content does not match expected.\n"
        f"Expected:\n{expected_content}\n\n"
        f"Actual:\n{chr(10).join(actual_lines)}"
    )


@pytest.mark.parametrize("line_index,expected_line", enumerate(EXPECTED_MANIFEST_LINES))
def test_manifest_individual_line(line_index, expected_line):
    """Each line of the manifest must match exactly (including spacing and arrow)."""
    with open(MANIFEST_FILE, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    if line_index >= len(lines):
        pytest.fail(
            f"manifest.txt has fewer than {line_index + 1} lines.\n"
            f"Missing line {line_index + 1}: '{expected_line}'"
        )
    actual_line = lines[line_index]
    assert actual_line == expected_line, (
        f"manifest.txt line {line_index + 1} is incorrect.\n"
        f"  Expected: '{expected_line}'\n"
        f"  Actual:   '{actual_line}'"
    )


def test_manifest_no_trailing_blank_line():
    """The manifest file must not end with a blank line (no extra newlines)."""
    with open(MANIFEST_FILE, "rb") as f:
        raw = f.read()
    # Decode and check: acceptable endings are no newline or exactly one \n
    text = raw.decode("utf-8")
    # After stripping exactly one trailing newline, there should be no more
    stripped = text.rstrip("\n")
    # Reconstruct: stripped + at most one newline
    assert text == stripped or text == stripped + "\n", (
        f"manifest.txt has unexpected trailing whitespace/blank lines.\n"
        f"Raw ending bytes: {raw[-10:]!r}"
    )
    lines_after_strip = stripped.split("\n")
    assert len(lines_after_strip) == 3, (
        f"After stripping trailing newline, expected 3 lines but got "
        f"{len(lines_after_strip)}.\nContent: {text!r}"
    )


# ---------------------------------------------------------------------------
# 4. No unexpected files in workspace (optional integrity check)
# ---------------------------------------------------------------------------

def test_workspace_contains_expected_entries():
    """
    The workspace must contain at least the 3 symlinks and the manifest.
    Extra files are allowed but the required entries must all be present.
    """
    required_names = {"sales_q1.csv", "sales_q2.csv", "customers.csv", "manifest.txt"}
    actual_names = set(os.listdir(WORKSPACE_DIR))
    missing = required_names - actual_names
    assert not missing, (
        f"The following required entries are missing from {WORKSPACE_DIR}:\n"
        + "\n".join(f"  - {name}" for name in sorted(missing))
    )