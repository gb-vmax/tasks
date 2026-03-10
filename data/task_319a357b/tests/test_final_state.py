# test_final_state.py

import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/automation_project"
VENV_DIR = os.path.join(PROJECT_DIR, "venv")
VENV_PYTHON = os.path.join(VENV_DIR, "bin", "python")
VENV_PIP = os.path.join(VENV_DIR, "bin", "pip")
REQUIREMENTS_TXT = os.path.join(PROJECT_DIR, "requirements.txt")
SCRIPT_PATH = os.path.join(PROJECT_DIR, "run_workflow.py")


# ---------------------------------------------------------------------------
# Virtual environment structure
# ---------------------------------------------------------------------------

def test_venv_directory_exists():
    assert os.path.isdir(VENV_DIR), (
        f"Virtual environment directory {VENV_DIR!r} does not exist. "
        "Run: python3 -m venv /home/user/automation_project/venv"
    )


def test_venv_python_executable_exists():
    assert os.path.isfile(VENV_PYTHON), (
        f"Virtual environment Python interpreter not found at {VENV_PYTHON!r}. "
        "The venv may not have been created correctly."
    )


def test_venv_python_is_executable():
    assert os.access(VENV_PYTHON, os.X_OK), (
        f"{VENV_PYTHON!r} exists but is not executable."
    )


def test_venv_pip_executable_exists():
    assert os.path.isfile(VENV_PIP), (
        f"Virtual environment pip not found at {VENV_PIP!r}. "
        "The venv may not have been created correctly."
    )


def test_venv_pip_is_executable():
    assert os.access(VENV_PIP, os.X_OK), (
        f"{VENV_PIP!r} exists but is not executable."
    )


def test_venv_lib_directory_exists():
    lib_dir = os.path.join(VENV_DIR, "lib")
    assert os.path.isdir(lib_dir), (
        f"Expected 'lib/' directory inside the venv at {lib_dir!r} but it was not found. "
        "The virtual environment may be incomplete."
    )


def test_venv_pyvenv_cfg_exists():
    cfg_file = os.path.join(VENV_DIR, "pyvenv.cfg")
    assert os.path.isfile(cfg_file), (
        f"Expected 'pyvenv.cfg' inside the venv at {cfg_file!r} but it was not found. "
        "The directory may not be a valid Python virtual environment."
    )


# ---------------------------------------------------------------------------
# Installed packages (checked via pip show)
# ---------------------------------------------------------------------------

def _pip_show(package_name):
    """Run `pip show <package>` inside the venv and return (returncode, stdout)."""
    result = subprocess.run(
        [VENV_PIP, "show", package_name],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout


def test_requests_installed_correct_version():
    rc, out = _pip_show("requests")
    assert rc == 0, (
        "Package 'requests' is not installed in the virtual environment. "
        f"Run: {VENV_PIP} install requests==2.28.2"
    )
    assert "2.28.2" in out, (
        f"'requests' is installed but not at version 2.28.2.\n"
        f"pip show output:\n{out}"
    )


def test_schedule_installed_correct_version():
    rc, out = _pip_show("schedule")
    assert rc == 0, (
        "Package 'schedule' is not installed in the virtual environment. "
        f"Run: {VENV_PIP} install schedule==1.2.0"
    )
    assert "1.2.0" in out, (
        f"'schedule' is installed but not at version 1.2.0.\n"
        f"pip show output:\n{out}"
    )


def test_python_dotenv_installed_correct_version():
    rc, out = _pip_show("python-dotenv")
    assert rc == 0, (
        "Package 'python-dotenv' is not installed in the virtual environment. "
        f"Run: {VENV_PIP} install python-dotenv==1.0.0"
    )
    assert "1.0.0" in out, (
        f"'python-dotenv' is installed but not at version 1.0.0.\n"
        f"pip show output:\n{out}"
    )


# ---------------------------------------------------------------------------
# requirements.txt
# ---------------------------------------------------------------------------

def test_requirements_txt_exists():
    assert os.path.isfile(REQUIREMENTS_TXT), (
        f"requirements.txt not found at {REQUIREMENTS_TXT!r}. "
        f"Generate it with: {VENV_PIP} freeze > {REQUIREMENTS_TXT}"
    )


def _read_requirements():
    with open(REQUIREMENTS_TXT, "r") as f:
        return f.read()


def test_requirements_txt_contains_requests():
    content = _read_requirements()
    # pip freeze uses lowercase; accept case-insensitive match for robustness
    lines_lower = [line.strip().lower() for line in content.splitlines()]
    assert "requests==2.28.2" in lines_lower, (
        f"requirements.txt does not contain 'requests==2.28.2'.\n"
        f"File contents:\n{content}"
    )


def test_requirements_txt_contains_schedule():
    content = _read_requirements()
    lines_lower = [line.strip().lower() for line in content.splitlines()]
    assert "schedule==1.2.0" in lines_lower, (
        f"requirements.txt does not contain 'schedule==1.2.0'.\n"
        f"File contents:\n{content}"
    )


def test_requirements_txt_contains_python_dotenv():
    content = _read_requirements()
    lines_lower = [line.strip().lower() for line in content.splitlines()]
    assert "python-dotenv==1.0.0" in lines_lower, (
        f"requirements.txt does not contain 'python-dotenv==1.0.0'.\n"
        f"File contents:\n{content}"
    )


def test_requirements_txt_is_not_empty():
    content = _read_requirements()
    assert content.strip(), (
        f"requirements.txt at {REQUIREMENTS_TXT!r} is empty. "
        "It should contain the output of `pip freeze`."
    )


# ---------------------------------------------------------------------------
# Running the project script
# ---------------------------------------------------------------------------

def test_run_workflow_script_exists():
    assert os.path.isfile(SCRIPT_PATH), (
        f"Project script not found at {SCRIPT_PATH!r}."
    )


def test_run_workflow_exits_with_code_zero():
    result = subprocess.run(
        [VENV_PYTHON, SCRIPT_PATH],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Running the workflow script exited with code {result.returncode} (expected 0).\n"
        f"stdout: {result.stdout!r}\n"
        f"stderr: {result.stderr!r}\n"
        "Check that all required packages are installed in the venv and the script has no errors."
    )


def test_run_workflow_prints_correct_output():
    result = subprocess.run(
        [VENV_PYTHON, SCRIPT_PATH],
        capture_output=True,
        text=True,
    )
    expected_output = "Workflow environment OK"
    actual_stdout = result.stdout.strip()
    assert actual_stdout == expected_output, (
        f"Script stdout does not match expected output.\n"
        f"Expected: {expected_output!r}\n"
        f"Got:      {actual_stdout!r}\n"
        f"(stderr: {result.stderr!r})"
    )


def test_run_workflow_no_stderr():
    result = subprocess.run(
        [VENV_PYTHON, SCRIPT_PATH],
        capture_output=True,
        text=True,
    )
    # Warn if there is unexpected stderr (but only fail on import errors / tracebacks)
    if result.returncode != 0:
        pytest.fail(
            f"Script failed with stderr:\n{result.stderr}"
        )
    # Check for import errors specifically
    assert "ImportError" not in result.stderr and "ModuleNotFoundError" not in result.stderr, (
        f"Script produced import-related errors on stderr:\n{result.stderr}"
    )