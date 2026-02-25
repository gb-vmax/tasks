# test_final_state.py

import os
import sys
import stat
import pytest
import subprocess

HOME_DIR = "/home/user"
QA_PROJECT_ENV = os.path.join(HOME_DIR, "qa_project_env")
VENV_DIR = os.path.join(QA_PROJECT_ENV, "venv")
BIN_DIR = os.path.join(VENV_DIR, "bin")
LIB_DIR = os.path.join(VENV_DIR, "lib")
PYVENV_CFG = os.path.join(VENV_DIR, "pyvenv.cfg")
PYTHON_VERSION_TXT = os.path.join(QA_PROJECT_ENV, "python_version.txt")

def test_qa_project_env_dir_exists_and_is_dir():
    assert os.path.exists(QA_PROJECT_ENV), (
        f"Directory '{QA_PROJECT_ENV}' does not exist. It must be created in your home directory."
    )
    assert os.path.isdir(QA_PROJECT_ENV), (
        f"'{QA_PROJECT_ENV}' exists but is not a directory."
    )

def test_venv_dir_exists_and_is_dir():
    assert os.path.exists(VENV_DIR), (
        f"Virtual environment directory '{VENV_DIR}' does not exist."
    )
    assert os.path.isdir(VENV_DIR), (
        f"'{VENV_DIR}' exists but is not a directory."
    )

def test_venv_structure():
    # Standard venv subdirectories and files
    assert os.path.isdir(BIN_DIR), (
        f"Virtual environment 'bin' directory '{BIN_DIR}' does not exist."
    )
    assert os.path.isdir(LIB_DIR), (
        f"Virtual environment 'lib' directory '{LIB_DIR}' does not exist."
    )
    assert os.path.isfile(PYVENV_CFG), (
        f"Virtual environment config file '{PYVENV_CFG}' does not exist."
    )
    # Check for python executable in bin
    python_bin = os.path.join(BIN_DIR, "python")
    python3_bin = os.path.join(BIN_DIR, "python3")
    if not (os.path.isfile(python_bin) or os.path.isfile(python3_bin)):
        pytest.fail(
            f"No Python executable found in '{BIN_DIR}'. Expected at least one of: 'python', 'python3'."
        )
    # Check the python binary is executable
    py_exec = python_bin if os.path.isfile(python_bin) else python3_bin
    st = os.stat(py_exec)
    assert st.st_mode & stat.S_IXUSR, (
        f"'{py_exec}' exists but is not marked as executable."
    )

def test_python_version_txt_exists_and_content():
    assert os.path.isfile(PYTHON_VERSION_TXT), (
        f"File '{PYTHON_VERSION_TXT}' does not exist."
    )
    # Get expected version string from venv's python
    venv_python = os.path.join(BIN_DIR, "python")
    if not os.path.isfile(venv_python):
        venv_python = os.path.join(BIN_DIR, "python3")
    assert os.path.isfile(venv_python), (
        f"Cannot find Python executable in '{BIN_DIR}' to check version."
    )
    try:
        completed = subprocess.run(
            [venv_python, "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except Exception as exc:
        pytest.fail(f"Could not execute '{venv_python} --version': {exc}")

    # python --version may output to stderr or stdout
    version_line = completed.stdout.strip() if completed.stdout.strip() else completed.stderr.strip()
    expected_content = version_line + "\n"

    # Read actual file content
    with open(PYTHON_VERSION_TXT, "rb") as f:
        content = f.read()
    try:
        content_str = content.decode("utf-8")
    except Exception:
        pytest.fail(
            f"File '{PYTHON_VERSION_TXT}' is not valid UTF-8 text."
        )
    # Ensure exactly one line, matches expected, and no extra whitespace
    lines = content_str.splitlines(keepends=True)
    assert len(lines) == 1, (
        f"File '{PYTHON_VERSION_TXT}' should contain exactly one line, but has {len(lines)} lines."
    )
    assert content_str == expected_content, (
        f"File '{PYTHON_VERSION_TXT}' content is incorrect.\n"
        f"Expected: {repr(expected_content)}\n"
        f"Actual:   {repr(content_str)}"
    )

def test_venv_is_usable_and_activatable():
    # Check that activation script exists and is readable
    activate_path = os.path.join(BIN_DIR, "activate")
    assert os.path.isfile(activate_path), (
        f"Virtual environment activation script '{activate_path}' does not exist."
    )
    assert os.access(activate_path, os.R_OK), (
        f"Virtual environment activation script '{activate_path}' is not readable."
    )

    # Try running a command using the venv python to check it's functional
    venv_python = os.path.join(BIN_DIR, "python")
    if not os.path.isfile(venv_python):
        venv_python = os.path.join(BIN_DIR, "python3")
    try:
        completed = subprocess.run(
            [venv_python, "-c", "import sys; print(sys.prefix)"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except Exception as exc:
        pytest.fail(f"Python in venv at '{venv_python}' is not callable: {exc}")

    # sys.prefix must point to the venv directory
    sys_prefix = completed.stdout.strip()
    assert sys_prefix == VENV_DIR, (
        f"Virtual environment Python reports sys.prefix='{sys_prefix}', expected '{VENV_DIR}'.\n"
        "This suggests the venv is not set up correctly."
    )