# test_final_state.py
"""
Pytest suite to validate the FINAL state of the OS/container after the markdown summary task.

Checks:
- /home/user/doc_summary.txt exists.
- It contains, in sorted ascending order, one per line, each unique base name of every .md file
  found anywhere under /home/user/docs and subdirectories.
- No extra or missing entries, no duplicates, no blank lines, correct order and content.
- /home/user/docs and all original .md files still exist.
- Permissions for read/write on summary file and docs directory.
"""

import os
import pytest

DOCS_DIR = "/home/user/docs"
DOC_SUMMARY = "/home/user/doc_summary.txt"

# The ground-truth markdown files and their base names:
expected_md_files = [
    "/home/user/docs/overview.md",
    "/home/user/docs/guide/introduction.md",
    "/home/user/docs/guide/getting_started.md",
    "/home/user/docs/faq.md",
    "/home/user/docs/reference/api.md",
    "/home/user/docs/reference/overview.md",
]

expected_base_names_sorted = [
    "api",
    "faq",
    "getting_started",
    "introduction",
    "overview",
]

def test_docs_directory_exists():
    assert os.path.isdir(DOCS_DIR), (
        f"Missing documentation directory: {DOCS_DIR}"
    )

@pytest.mark.parametrize("path", expected_md_files)
def test_markdown_files_still_exist(path):
    assert os.path.isfile(path), (
        f"Markdown file missing after task: {path}\n"
        f"Do not remove or rename the original markdown files."
    )

def test_no_extra_markdown_files_created():
    # Walk /home/user/docs and ensure only the expected files are present
    found = []
    for root, dirs, files in os.walk(DOCS_DIR):
        for f in files:
            if f.endswith(".md"):
                found.append(os.path.join(root, f))
    found_set = set(found)
    expected_set = set(expected_md_files)
    extra = found_set - expected_set
    missing = expected_set - found_set
    assert not missing, (
        f"The following expected markdown files are missing: {sorted(missing)}"
    )
    assert not extra, (
        f"The following unexpected markdown files are present: {sorted(extra)}"
    )

def test_doc_summary_txt_exists():
    assert os.path.isfile(DOC_SUMMARY), (
        f"{DOC_SUMMARY} does not exist.\n"
        f"You must create this file at the required absolute path."
    )

def test_doc_summary_txt_permissions():
    assert os.access(DOC_SUMMARY, os.R_OK), (
        f"No read permission for {DOC_SUMMARY}."
    )
    assert os.access(DOC_SUMMARY, os.W_OK), (
        f"No write permission for {DOC_SUMMARY}."
    )

def test_docs_directory_permissions():
    # Check that agent has read/write/execute permissions on /home/user/docs
    assert os.access(DOCS_DIR, os.R_OK | os.W_OK | os.X_OK), (
        f"Insufficient permissions on {DOCS_DIR}.\n"
        f"Ensure read, write, and execute permissions."
    )

def test_doc_summary_txt_content_exact():
    """
    Validates that /home/user/doc_summary.txt contains exactly the expected entries:
    - Each line contains only a unique base name (no path, no .md)
    - Sorted ascending, one per line, no blanks, no duplicates, no extra/missing entries
    """
    with open(DOC_SUMMARY, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # Check for blank lines
    assert all(line.strip() != "" for line in lines), (
        f"{DOC_SUMMARY} should not contain blank lines."
    )

    # Check for duplicates
    if len(lines) != len(set(lines)):
        # Find which are duplicated
        from collections import Counter
        dupes = [item for item, count in Counter(lines).items() if count > 1]
        assert False, (
            f"{DOC_SUMMARY} contains duplicate base names: {dupes}"
        )

    # Check for extra or missing entries
    lines_set = set(lines)
    expected_set = set(expected_base_names_sorted)
    missing = expected_set - lines_set
    extra = lines_set - expected_set
    assert not missing, (
        f"{DOC_SUMMARY} is missing the following base names: {sorted(missing)}"
    )
    assert not extra, (
        f"{DOC_SUMMARY} contains unexpected extra base names: {sorted(extra)}"
    )

    # Check for correct sorted order
    if lines != expected_base_names_sorted:
        # Find the first ordering error, if any
        for i, (got, exp) in enumerate(zip(lines, expected_base_names_sorted)):
            if got != exp:
                break
        else:
            i = None
        msg = (
            f"{DOC_SUMMARY} lines are not sorted as required.\n"
            f"Expected order:\n{expected_base_names_sorted}\n"
            f"Found order:\n{lines}\n"
        )
        if i is not None:
            msg += f"First mismatch at line {i+1}: expected '{expected_base_names_sorted[i]}', got '{lines[i]}'."
        assert False, msg

def test_doc_summary_txt_formatting():
    """
    Ensures that each line in doc_summary.txt contains only a valid base name:
    - No whitespace, no path, no extension, no blank lines.
    """
    with open(DOC_SUMMARY, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    for i, line in enumerate(lines, 1):
        assert "/" not in line and "\\" not in line, (
            f"Line {i} in {DOC_SUMMARY} contains a path separator: '{line}'"
        )
        assert line == line.strip(), (
            f"Line {i} in {DOC_SUMMARY} contains leading/trailing whitespace: '{line}'"
        )
        assert not line.endswith(".md"), (
            f"Line {i} in {DOC_SUMMARY} contains file extension: '{line}'"
        )
        assert line, (
            f"Line {i} in {DOC_SUMMARY} is blank."
        )
        # Only valid base names allowed
        assert line in expected_base_names_sorted, (
            f"Line {i} in {DOC_SUMMARY} ('{line}') is not a recognized base name."
        )