# test_final_state.py

import os
import stat
import subprocess
import sys
import pytest

RESEARCH_DIR = "/home/user/research"
VENV_PATH = os.path.join(RESEARCH_DIR, "venv")
REQUIREMENTS_FILE = os.path.join(RESEARCH_DIR, "requirements.txt")
CHECK_ENV_SCRIPT = os.path.join(RESEARCH_DIR, "check_env.py")
ENV_STATUS_FILE = os.path.join(RESEARCH_DIR, "env_status.txt")
VENV_PYTHON = os.path.join(VENV_PATH, "bin", "python")
VENV_PIP = os.path.join(VENV_PATH, "bin", "pip")

EXPECTED_ENV_STATUS_CONTENT = (
    "numpy: OK (1.26.4)\n"
    "pandas: OK (2.2.1)\n"
    "venv active: True\n"
)


# ── Virtual environment structure ──────────────────────────────────────────────

def test_venv_directory_exists():
    assert os.path.isdir(VENV_PATH), (
        f"Virtual environment directory '{VENV_PATH}' does not exist. "
        "Run: python3 -m venv /home/user/research/venv"
    )


def test_venv_python_exists():
    assert os.path.isfile(VENV_PYTHON), (
        f"Virtual environment Python interpreter '{VENV_PYTHON}' does not exist. "
        "The venv may not have been created correctly."
    )


def test_venv_python_is_executable():
    assert os.access(VENV_PYTHON, os.X_OK), (
        f"Virtual environment Python interpreter '{VENV_PYTHON}' is not executable."
    )


def test_venv_pip_exists():
    assert os.path.isfile(VENV_PIP), (
        f"Virtual environment pip '{VENV_PIP}' does not exist. "
        "The venv may not have been created correctly."
    )


def test_venv_python_prefix():
    """Verify that sys.prefix inside the venv equals VENV_PATH."""
    result = subprocess.run(
        [VENV_PYTHON, "-c", "import sys; print(sys.prefix)"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Failed to run venv Python. stderr: {result.stderr}"
    )
    actual_prefix = result.stdout.strip()
    assert actual_prefix == VENV_PATH, (
        f"sys.prefix inside the venv is '{actual_prefix}', "
        f"expected '{VENV_PATH}'. "
        "Make sure the venv was created at the correct path."
    )


def test_venv_pyvenv_cfg_exists():
    pyvenv_cfg = os.path.join(VENV_PATH, "pyvenv.cfg")
    assert os.path.isfile(pyvenv_cfg), (
        f"pyvenv.cfg not found at '{pyvenv_cfg}'. "
        "The virtual environment structure appears incomplete."
    )


# ── Installed packages ─────────────────────────────────────────────────────────

def test_numpy_installed_in_venv():
    result = subprocess.run(
        [VENV_PYTHON, "-c", "import numpy; print(numpy.__version__)"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"numpy is not importable in the venv. stderr: {result.stderr.strip()}\n"
        "Run: /home/user/research/venv/bin/pip install numpy==1.26.4"
    )
    version = result.stdout.strip()
    assert version == "1.26.4", (
        f"numpy version in venv is '{version}', expected '1.26.4'. "
        "Install the exact version: pip install numpy==1.26.4"
    )


def test_pandas_installed_in_venv():
    result = subprocess.run(
        [VENV_PYTHON, "-c", "import pandas; print(pandas.__version__)"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"pandas is not importable in the venv. stderr: {result.stderr.strip()}\n"
        "Run: /home/user/research/venv/bin/pip install pandas==2.2.1"
    )
    version = result.stdout.strip()
    assert version == "2.2.1", (
        f"pandas version in venv is '{version}', expected '2.2.1'. "
        "Install the exact version: pip install pandas==2.2.1"
    )


def test_packages_installed_via_venv_pip():
    """Check pip show reports packages are installed in the venv site-packages."""
    for package in ("numpy", "pandas"):
        result = subprocess.run(
            [VENV_PIP, "show", package],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"'{package}' is not listed by venv pip. stderr: {result.stderr.strip()}"
        )
        # Location should be inside the venv
        for line in result.stdout.splitlines():
            if line.startswith("Location:"):
                location = line.split(":", 1)[1].strip()
                assert location.startswith(VENV_PATH), (
                    f"'{package}' is installed at '{location}', "
                    f"which is outside the venv '{VENV_PATH}'. "
                    "Use the venv pip to install packages."
                )
                break


# ── env_status.txt existence and content ──────────────────────────────────────

def test_env_status_file_exists():
    assert os.path.isfile(ENV_STATUS_FILE), (
        f"Output file '{ENV_STATUS_FILE}' does not exist. "
        "Run the check_env.py script with the venv Python: "
        "/home/user/research/venv/bin/python /home/user/research/check_env.py"
    )


def test_env_status_file_content_exact():
    with open(ENV_STATUS_FILE, "r") as f:
        actual_content = f.read()
    assert actual_content == EXPECTED_ENV_STATUS_CONTENT, (
        f"Content of '{ENV_STATUS_FILE}' does not match expected.\n"
        f"Expected (repr): {EXPECTED_ENV_STATUS_CONTENT!r}\n"
        f"Actual   (repr): {actual_content!r}\n"
        "Make sure you run the script with the venv Python and that "
        "the correct package versions are installed."
    )


def test_env_status_numpy_line():
    with open(ENV_STATUS_FILE, "r") as f:
        lines = f.read().splitlines()
    assert "numpy: OK (1.26.4)" in lines, (
        f"Expected line 'numpy: OK (1.26.4)' not found in '{ENV_STATUS_FILE}'. "
        f"Actual lines: {lines}"
    )


def test_env_status_pandas_line():
    with open(ENV_STATUS_FILE, "r") as f:
        lines = f.read().splitlines()
    assert "pandas: OK (2.2.1)" in lines, (
        f"Expected line 'pandas: OK (2.2.1)' not found in '{ENV_STATUS_FILE}'. "
        f"Actual lines: {lines}"
    )


def test_env_status_venv_active_line():
    with open(ENV_STATUS_FILE, "r") as f:
        lines = f.read().splitlines()
    assert "venv active: True" in lines, (
        f"Expected line 'venv active: True' not found in '{ENV_STATUS_FILE}'. "
        f"Actual lines: {lines}\n"
        "Make sure the script was run using the venv Python interpreter "
        "(/home/user/research/venv/bin/python), not the system Python."
    )


def test_env_status_no_missing_packages():
    with open(ENV_STATUS_FILE, "r") as f:
        content = f.read()
    assert "MISSING" not in content, (
        f"'{ENV_STATUS_FILE}' contains 'MISSING', indicating a package was not found.\n"
        f"File content:\n{content}"
    )


def test_env_status_line_count():
    with open(ENV_STATUS_FILE, "r") as f:
        lines = [l for l in f.read().splitlines() if l.strip()]
    assert len(lines) == 3, (
        f"Expected exactly 3 non-empty lines in '{ENV_STATUS_FILE}', "
        f"got {len(lines)}.\nLines: {lines}"
    )


# ── Pre-existing files untouched ───────────────────────────────────────────────

def test_requirements_file_still_intact():
    assert os.path.isfile(REQUIREMENTS_FILE), (
        f"requirements.txt '{REQUIREMENTS_FILE}' is missing — it should not have been removed."
    )
    with open(REQUIREMENTS_FILE, "r") as f:
        content = f.read().strip()
    expected_lines = {"numpy==1.26.4", "pandas==2.2.1"}
    actual_lines = {line.strip() for line in content.splitlines() if line.strip()}
    assert actual_lines == expected_lines, (
        f"requirements.txt has been modified.\n"
        f"Expected: {expected_lines}\nActual: {actual_lines}"
    )


def test_check_env_script_still_intact():
    assert os.path.isfile(CHECK_ENV_SCRIPT), (
        f"check_env.py '{CHECK_ENV_SCRIPT}' is missing — it should not have been removed."
    )
    with open(CHECK_ENV_SCRIPT, "r") as f:
        content = f.read()
    for fragment in ("import numpy", "import pandas", "env_status.txt",
                     "/home/user/research/venv", "sys.prefix"):
        assert fragment in content, (
            f"check_env.py appears to have been modified: '{fragment}' not found."
        )