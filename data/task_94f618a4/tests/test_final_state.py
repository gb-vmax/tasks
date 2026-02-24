# test_final_state.py

import os
import subprocess
import pytest

HOME = "/home/user"
PYUTILS_DIR = os.path.join(HOME, "pyutils")
VENV_DIR = os.path.join(PYUTILS_DIR, "venv")
PKG_LIST_FILE = os.path.join(PYUTILS_DIR, "package_list.txt")

REQUIRED_PACKAGES = {
    "requests": "2.31.0",
    "pytz": "2024.1",
}
PKG_LIST_EXPECTED = "pytz==2024.1\nrequests==2.31.0\n"


def test_pyutils_dir_exists():
    assert os.path.isdir(PYUTILS_DIR), (
        f"Directory '{PYUTILS_DIR}' does not exist. "
        "You must create it at '/home/user/pyutils'."
    )


def test_venv_dir_exists():
    assert os.path.isdir(VENV_DIR), (
        f"Virtual environment directory '{VENV_DIR}' does not exist. "
        "You must create a Python virtual environment here."
    )


def test_venv_is_valid():
    # Check for 'pyvenv.cfg' in venv directory
    pyvenv_cfg = os.path.join(VENV_DIR, "pyvenv.cfg")
    assert os.path.isfile(pyvenv_cfg), (
        f"'{VENV_DIR}' does not appear to be a valid Python virtual environment "
        "(missing 'pyvenv.cfg')."
    )
    # Check for 'bin/python' (on Unix)
    python_bin = os.path.join(VENV_DIR, "bin", "python")
    assert os.path.isfile(python_bin) and os.access(python_bin, os.X_OK), (
        f"Python executable '{python_bin}' not found or not executable in the virtual environment."
    )


def _run_in_venv(args):
    """Run a command inside the venv and return (stdout, stderr, returncode)."""
    python_bin = os.path.join(VENV_DIR, "bin", "python")
    proc = subprocess.run(
        [python_bin] + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return proc.stdout, proc.stderr, proc.returncode


def test_required_packages_installed_exact_versions():
    # Use pip list to get installed packages in the venv
    pip_bin = os.path.join(VENV_DIR, "bin", "pip")
    if not os.path.isfile(pip_bin) or not os.access(pip_bin, os.X_OK):
        pytest.fail(
            f"'pip' not found or not executable at '{pip_bin}' in the virtual environment."
        )
    proc = subprocess.run(
        [pip_bin, "list", "--format=freeze"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if proc.returncode != 0:
        pytest.fail(f"Failed to run pip list: {proc.stderr}")

    installed = {}
    for line in proc.stdout.strip().splitlines():
        if "==" not in line:
            continue
        name, version = line.strip().split("==", 1)
        installed[name.lower()] = version

    # Check that only the required packages are present in the list (case-insensitive)
    expected = set(REQUIRED_PACKAGES.keys())
    listed = set(installed.keys())
    for pkg in expected:
        assert pkg in installed, (
            f"Package '{pkg}' is not installed in the virtual environment."
        )
        assert installed[pkg] == REQUIRED_PACKAGES[pkg], (
            f"Package '{pkg}' is installed but version is '{installed[pkg]}', "
            f"expected version '{REQUIRED_PACKAGES[pkg]}'."
        )


def test_package_list_txt_exists():
    assert os.path.isfile(PKG_LIST_FILE), (
        f"File '{PKG_LIST_FILE}' does not exist. "
        "You must create it at '/home/user/pyutils/package_list.txt'."
    )


def test_package_list_txt_exact_contents_and_format():
    # Read the file and check exact contents
    with open(PKG_LIST_FILE, "r", encoding="utf-8") as f:
        contents = f.read()
    assert contents == PKG_LIST_EXPECTED, (
        f"'{PKG_LIST_FILE}' does not contain the expected lines.\n"
        "It must contain exactly:\n"
        f"{PKG_LIST_EXPECTED!r}\n"
        f"Current contents:\n{contents!r}\n"
        "Ensure only the direct packages 'pytz' and 'requests' are listed, "
        "sorted alphabetically and matching the specified versions, with no extra lines."
    )


def test_package_list_txt_no_extra_packages():
    # Parse the lines and check only required packages are present
    with open(PKG_LIST_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    expected_lines = [
        f"{name}=={ver}" for name, ver in sorted(REQUIRED_PACKAGES.items())
    ]
    assert lines == expected_lines, (
        f"'{PKG_LIST_FILE}' must only contain the following lines, sorted alphabetically:\n"
        f"{expected_lines}\n"
        f"Current lines:\n{lines}\n"
        "No additional packages (such as pip, setuptools, wheel, etc.) may be listed."
    )


def test_package_list_txt_no_trailing_or_blank_lines():
    with open(PKG_LIST_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Should be exactly two lines, each ending with \n, and no extra blank lines
    assert len(lines) == 2, (
        f"'{PKG_LIST_FILE}' must contain exactly two lines, one for each package. "
        f"Found {len(lines)} lines."
    )
    for i, line in enumerate(lines):
        assert line.endswith('\n'), (
            f"Line {i+1} in '{PKG_LIST_FILE}' does not end with a newline character."
        )
        stripped = line.strip()
        assert stripped in [f"pytz==2024.1", f"requests==2.31.0"], (
            f"Line {i+1} in '{PKG_LIST_FILE}' contains unexpected content: '{stripped}'."
        )


def test_package_list_txt_sorted_alphabetically():
    with open(PKG_LIST_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    sorted_lines = sorted(lines)
    assert lines == sorted_lines, (
        f"Entries in '{PKG_LIST_FILE}' are not sorted alphabetically by package name.\n"
        f"Expected order: {sorted_lines}\nActual order: {lines}"
    )