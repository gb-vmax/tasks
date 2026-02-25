# test_final_state.py

"""
Pytest suite to validate the final state of the system after completion of the changelog and linting task.

Validates:
- /home/user/project/CHANGELOG.md exists with exact required content.
- /home/user/project/CHANGELOG_lint.log exists and contains exactly "No issues found" if the markdown is correct.
- If markdownlint emits any warnings, the lint log must match the actual output of markdownlint-cli for the file.
"""

import os
import pytest
import subprocess

CHANGELOG_MD = "/home/user/project/CHANGELOG.md"
CHANGELOG_LINT_LOG = "/home/user/project/CHANGELOG_lint.log"

EXPECTED_CHANGELOG_MD = """# Changelog

## [1.0.1] - 2024-05-21
### Added
- New module for API integrations

### Fixed
- Issue with database connections

### Changed
- Documentation for the install process
"""

EXPECTED_LINT_LOG = "No issues found"


def test_changelog_md_exists():
    assert os.path.isfile(CHANGELOG_MD), (
        f"Expected changelog file '{CHANGELOG_MD}' does not exist. "
        "Please ensure it is created at the correct location."
    )


def test_changelog_md_content_exact():
    with open(CHANGELOG_MD, "r", encoding="utf-8") as f:
        contents = f.read()
    # Use repr in message to show invisible whitespace issues
    assert contents == EXPECTED_CHANGELOG_MD, (
        f"The content of '{CHANGELOG_MD}' does not match the required format.\n"
        f"--- Expected content ---\n{repr(EXPECTED_CHANGELOG_MD)}\n"
        f"--- Actual content ---\n{repr(contents)}\n"
        "Please ensure the content, formatting, and whitespace are exactly as specified."
    )


def test_changelog_lint_log_exists():
    assert os.path.isfile(CHANGELOG_LINT_LOG), (
        f"Expected lint log '{CHANGELOG_LINT_LOG}' does not exist. "
        "Please ensure it is created at the correct location."
    )


def test_changelog_lint_log_content_matches_linter():
    """
    This test verifies that the lint log matches the actual output of markdownlint-cli.
    - If the markdown file is perfect, the log must be exactly 'No issues found'.
    - Otherwise, the log must match the output of running markdownlint-cli on the file.
    """
    # Try to run markdownlint-cli on the file
    try:
        # markdownlint-cli returns 0 if no issues, 1 if issues
        # Output is sent to stdout
        result = subprocess.run(
            ["markdownlint", CHANGELOG_MD],
            capture_output=True,
            text=True,
            check=False
        )
        linter_output = result.stdout.strip()
    except FileNotFoundError:
        pytest.skip(
            "markdownlint-cli is not installed in the test environment; "
            "cannot verify actual linter output for comparison."
        )

    with open(CHANGELOG_LINT_LOG, "r", encoding="utf-8") as f:
        lint_log_content = f.read().strip()

    if linter_output == "":
        # No issues found: log must say exactly "No issues found"
        assert lint_log_content == EXPECTED_LINT_LOG, (
            f"Lint log at '{CHANGELOG_LINT_LOG}' should contain exactly 'No issues found', "
            f"but contains:\n{repr(lint_log_content)}"
        )
    else:
        # There are lint issues, so log must match linter output exactly
        assert lint_log_content == linter_output, (
            f"Lint log at '{CHANGELOG_LINT_LOG}' does not match markdownlint's output.\n"
            f"--- Expected (from markdownlint) ---\n{linter_output}\n"
            f"--- Actual log content ---\n{lint_log_content}\n"
            "Please ensure the log matches the markdownlint diagnostic output exactly."
        )