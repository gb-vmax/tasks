# test_final_state.py

"""
Pytest suite to validate the final state of /home/user/solver_docs and its required files.

Checks:
- /home/user/solver_docs exists and is a directory.
- Contains exactly the four required files (no more, no less): optifast.md, linearsolve.md, curvefit.md, solvers_summary.csv.
- Each file has the exact required content.
- Directory and files are readable and writable by the current user.
"""

import os
import pytest
import stat
import difflib

DOCS_DIR = "/home/user/solver_docs"
EXPECTED_FILES = {
    "optifast.md": """# Introduction
OptiFast is a high-speed optimization solver designed for real-time applications.

# Usage Example
optifast --input data.csv --max-iterations 1000
""",
    "linearsolve.md": """# Introduction
LinearSolve efficiently solves large linear systems of equations.

# Usage Example
linearsolve --matrix matrix.txt --verbose
""",
    "curvefit.md": """# Introduction
CurveFit provides advanced curve fitting features with robust statistical models.

# Usage Example
curvefit --data points.json --method least_squares
""",
    "solvers_summary.csv": """Solver,Description,ExampleCommand
OptiFast,OptiFast is a high-speed optimization solver designed for real-time applications.,optifast --input data.csv --max-iterations 1000
LinearSolve,LinearSolve efficiently solves large linear systems of equations.,linearsolve --matrix matrix.txt --verbose
CurveFit,CurveFit provides advanced curve fitting features with robust statistical models.,curvefit --data points.json --method least_squares
"""
}

def _read_file_strip_trailing_newline(path):
    """Read file as text, preserving newlines, but remove a single trailing newline for comparison."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return text.rstrip('\n')

def _get_non_hidden_files_in_dir(path):
    """Return sorted list of non-hidden files in a directory."""
    try:
        return sorted([f for f in os.listdir(path) if not f.startswith('.')])
    except FileNotFoundError:
        return []

def _has_rw_access(path):
    """Check if the current user has read and write access to the path."""
    return os.access(path, os.R_OK | os.W_OK)

def _file_diff(expected, actual):
    """Return unified diff string between expected and actual strings."""
    return "\n".join(
        difflib.unified_diff(
            expected.splitlines(),
            actual.splitlines(),
            fromfile="expected",
            tofile="actual",
            lineterm=""
        )
    )

def _fail_with_diff(filename, expected, actual):
    diff = _file_diff(expected, actual)
    pytest.fail(
        f"File {filename} does not have the exact required content.\n"
        f"Diff:\n{diff}"
    )

def _check_no_extra_files():
    """Ensure there are no extra files in the docs dir."""
    present = _get_non_hidden_files_in_dir(DOCS_DIR)
    expected = sorted(EXPECTED_FILES.keys())
    assert present == expected, (
        f"{DOCS_DIR} must contain only these files: {expected}, "
        f"but found: {present}. No extra or missing files are allowed."
    )

def _check_file_permissions_rw_user(path):
    """Check that file/dir at path is readable and writable by the current user."""
    assert _has_rw_access(path), (
        f"{path} is not readable and writable by the current user."
    )

@pytest.mark.order(1)
def test_docs_dir_exists_and_is_dir():
    assert os.path.exists(DOCS_DIR), (
        f"Directory {DOCS_DIR} does not exist. "
        "You must create it before adding documentation files."
    )
    assert os.path.isdir(DOCS_DIR), (
        f"{DOCS_DIR} exists but is not a directory."
    )

@pytest.mark.order(2)
def test_docs_dir_contents_exact():
    _check_no_extra_files()

@pytest.mark.order(3)
@pytest.mark.parametrize("filename", EXPECTED_FILES.keys())
def test_file_exists(filename):
    fullpath = os.path.join(DOCS_DIR, filename)
    assert os.path.isfile(fullpath), (
        f"Required file {fullpath} does not exist."
    )

@pytest.mark.order(4)
@pytest.mark.parametrize("filename", EXPECTED_FILES.keys())
def test_file_content_exact(filename):
    fullpath = os.path.join(DOCS_DIR, filename)
    expected = EXPECTED_FILES[filename].rstrip('\n')
    try:
        actual = _read_file_strip_trailing_newline(fullpath)
    except FileNotFoundError:
        pytest.fail(f"File {fullpath} does not exist for content check.")
    if actual != expected:
        _fail_with_diff(fullpath, expected, actual)

@pytest.mark.order(5)
@pytest.mark.parametrize("filename", EXPECTED_FILES.keys())
def test_file_permissions_rw_user(filename):
    fullpath = os.path.join(DOCS_DIR, filename)
    _check_file_permissions_rw_user(fullpath)

@pytest.mark.order(6)
def test_docs_dir_permissions_rw_user():
    _check_file_permissions_rw_user(DOCS_DIR)

@pytest.mark.order(7)
def test_no_additional_files():
    """Ensure there are no additional (non-hidden) files in the documentation directory."""
    present = set(_get_non_hidden_files_in_dir(DOCS_DIR))
    expected = set(EXPECTED_FILES.keys())
    extra = present - expected
    missing = expected - present
    assert not extra, (
        f"Found extra file(s) in {DOCS_DIR}: {sorted(extra)}. "
        "Only the required four files should exist."
    )
    assert not missing, (
        f"Missing required file(s) in {DOCS_DIR}: {sorted(missing)}."
    )