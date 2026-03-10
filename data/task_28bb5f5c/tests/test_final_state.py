# test_final_state.py

import os
import subprocess
import pytest

DATASETS_PROJECT_DIR = "/home/user/datasets_project"
VENV_DIR = "/home/user/datasets_project/venv"
VENV_PYTHON = "/home/user/datasets_project/venv/bin/python"
VENV_PIP = "/home/user/datasets_project/venv/bin/pip"
REQUIREMENTS_TXT = "/home/user/datasets_project/requirements.txt"


def test_datasets_project_directory_exists():
    """The datasets_project directory must exist."""
    assert os.path.isdir(DATASETS_PROJECT_DIR), (
        f"Directory '{DATASETS_PROJECT_DIR}' does not exist. "
        "The project directory must be present after task completion."
    )


def test_venv_directory_exists():
    """The virtual environment directory must exist at the expected path."""
    assert os.path.isdir(VENV_DIR), (
        f"Virtual environment directory '{VENV_DIR}' does not exist. "
        "The student must create a venv named 'venv' inside the project directory."
    )


def test_venv_python_exists_and_is_executable():
    """The venv must contain a Python executable."""
    assert os.path.isfile(VENV_PYTHON), (
        f"Python executable not found at '{VENV_PYTHON}'. "
        "The virtual environment may not have been created correctly."
    )
    assert os.access(VENV_PYTHON, os.X_OK), (
        f"Python executable at '{VENV_PYTHON}' is not executable. "
        "Check the virtual environment setup."
    )


def test_venv_pip_exists_and_is_executable():
    """The venv must contain a pip executable."""
    assert os.path.isfile(VENV_PIP), (
        f"pip executable not found at '{VENV_PIP}'. "
        "The virtual environment may not have been created correctly."
    )
    assert os.access(VENV_PIP, os.X_OK), (
        f"pip executable at '{VENV_PIP}' is not executable. "
        "Check the virtual environment setup."
    )


def test_venv_lib_directory_exists():
    """The venv must contain a lib directory (standard venv structure)."""
    lib_dir = os.path.join(VENV_DIR, "lib")
    assert os.path.isdir(lib_dir), (
        f"lib directory not found at '{lib_dir}'. "
        "The virtual environment structure appears to be incomplete or invalid."
    )


def test_venv_is_valid_python_environment():
    """The venv Python executable must be functional."""
    result = subprocess.run(
        [VENV_PYTHON, "--version"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Running '{VENV_PYTHON} --version' failed with return code {result.returncode}. "
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )
    assert "Python" in result.stdout or "Python" in result.stderr, (
        f"Unexpected output from '{VENV_PYTHON} --version': "
        f"stdout='{result.stdout}', stderr='{result.stderr}'"
    )


def test_requirements_txt_exists():
    """The requirements.txt file must exist at the expected path."""
    assert os.path.isfile(REQUIREMENTS_TXT), (
        f"File '{REQUIREMENTS_TXT}' does not exist. "
        "The student must generate a requirements.txt using 'pip freeze' from the venv."
    )


def test_requirements_txt_is_not_empty():
    """The requirements.txt file must not be empty."""
    size = os.path.getsize(REQUIREMENTS_TXT)
    assert size > 0, (
        f"File '{REQUIREMENTS_TXT}' is empty. "
        "The requirements.txt must contain pip freeze output with installed packages."
    )


def test_requirements_txt_contains_numpy():
    """The requirements.txt must contain the exact line 'numpy==1.26.4'."""
    with open(REQUIREMENTS_TXT, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    assert "numpy==1.26.4" in lines, (
        f"'numpy==1.26.4' not found as an exact line in '{REQUIREMENTS_TXT}'. "
        f"Current contents:\n{chr(10).join(lines)}\n"
        "Make sure numpy==1.26.4 was installed using the venv's pip."
    )


def test_requirements_txt_contains_pandas():
    """The requirements.txt must contain the exact line 'pandas==2.2.2'."""
    with open(REQUIREMENTS_TXT, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    assert "pandas==2.2.2" in lines, (
        f"'pandas==2.2.2' not found as an exact line in '{REQUIREMENTS_TXT}'. "
        f"Current contents:\n{chr(10).join(lines)}\n"
        "Make sure pandas==2.2.2 was installed using the venv's pip."
    )


def test_requirements_txt_has_more_than_two_lines():
    """The requirements.txt must have more than 2 lines (pip freeze includes dependencies)."""
    with open(REQUIREMENTS_TXT, "r") as f:
        non_empty_lines = [line.strip() for line in f.readlines() if line.strip()]
    assert len(non_empty_lines) > 2, (
        f"'{REQUIREMENTS_TXT}' has only {len(non_empty_lines)} non-empty line(s). "
        "Expected more than 2 lines since pip freeze should include numpy, pandas, "
        "and their dependencies (e.g., python-dateutil, pytz, six, tzdata, etc.). "
        f"Current contents:\n{chr(10).join(non_empty_lines)}"
    )


def test_requirements_txt_lines_are_package_version_format():
    """All non-empty lines in requirements.txt must be in 'package==version' format."""
    with open(REQUIREMENTS_TXT, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    invalid_lines = []
    for line in lines:
        # pip freeze output lines should be in 'package==version' format
        # (ignoring comment lines starting with #)
        if line.startswith("#"):
            continue
        if "==" not in line:
            invalid_lines.append(line)

    assert len(invalid_lines) == 0, (
        f"The following lines in '{REQUIREMENTS_TXT}' are not in 'package==version' format: "
        f"{invalid_lines}\n"
        "The requirements.txt must be the direct output of 'pip freeze' without manual editing."
    )


def test_numpy_installed_in_venv():
    """numpy==1.26.4 must be importable from the venv's Python."""
    result = subprocess.run(
        [VENV_PYTHON, "-c", "import numpy; print(numpy.__version__)"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Failed to import numpy in the venv. "
        f"stdout: {result.stdout}\nstderr: {result.stderr}\n"
        "Make sure numpy was installed using the venv's pip."
    )
    version = result.stdout.strip()
    assert version == "1.26.4", (
        f"numpy version in venv is '{version}', expected '1.26.4'. "
        "Make sure numpy==1.26.4 was installed."
    )


def test_pandas_installed_in_venv():
    """pandas==2.2.2 must be importable from the venv's Python."""
    result = subprocess.run(
        [VENV_PYTHON, "-c", "import pandas; print(pandas.__version__)"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Failed to import pandas in the venv. "
        f"stdout: {result.stdout}\nstderr: {result.stderr}\n"
        "Make sure pandas was installed using the venv's pip."
    )
    version = result.stdout.strip()
    assert version == "2.2.2", (
        f"pandas version in venv is '{version}', expected '2.2.2'. "
        "Make sure pandas==2.2.2 was installed."
    )


def test_pip_list_shows_numpy_and_pandas():
    """The venv's pip list must show both numpy and pandas at the correct versions."""
    result = subprocess.run(
        [VENV_PIP, "list", "--format=freeze"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Running '{VENV_PIP} list --format=freeze' failed. "
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )
    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    assert "numpy==1.26.4" in lines, (
        f"'numpy==1.26.4' not found in venv pip list output. "
        f"pip list output:\n{result.stdout}"
    )
    assert "pandas==2.2.2" in lines, (
        f"'pandas==2.2.2' not found in venv pip list output. "
        f"pip list output:\n{result.stdout}"
    )


def test_requirements_txt_matches_pip_freeze_output():
    """The requirements.txt content must match what pip freeze currently outputs from the venv."""
    result = subprocess.run(
        [VENV_PIP, "freeze"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Running '{VENV_PIP} freeze' failed. "
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )
    pip_freeze_lines = set(line.strip() for line in result.stdout.splitlines() if line.strip())

    with open(REQUIREMENTS_TXT, "r") as f:
        req_lines = set(line.strip() for line in f.readlines() if line.strip())

    # The requirements.txt should contain at least numpy and pandas
    # (it was generated from pip freeze at the time of creation)
    assert "numpy==1.26.4" in req_lines, (
        f"'numpy==1.26.4' missing from '{REQUIREMENTS_TXT}'. "
        f"File contents: {req_lines}"
    )
    assert "pandas==2.2.2" in req_lines, (
        f"'pandas==2.2.2' missing from '{REQUIREMENTS_TXT}'. "
        f"File contents: {req_lines}"
    )

    # Both should have the same packages (pip freeze output should match the file)
    missing_from_file = pip_freeze_lines - req_lines
    extra_in_file = req_lines - pip_freeze_lines

    assert not missing_from_file, (
        f"The following packages are in current pip freeze output but missing from "
        f"'{REQUIREMENTS_TXT}': {missing_from_file}\n"
        "The requirements.txt must be the complete output of pip freeze."
    )
    assert not extra_in_file, (
        f"The following lines are in '{REQUIREMENTS_TXT}' but not in current pip freeze output: "
        f"{extra_in_file}\n"
        "The requirements.txt must not contain manually added entries."
    )