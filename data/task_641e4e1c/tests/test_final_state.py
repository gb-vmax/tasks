# test_final_state.py

import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/migration_project"
VENV_DIR = os.path.join(PROJECT_DIR, "venv")
VENV_PYTHON = os.path.join(VENV_DIR, "bin", "python")
VENV_PIP = os.path.join(VENV_DIR, "bin", "pip")
FROZEN_REQUIREMENTS = os.path.join(PROJECT_DIR, "requirements_frozen.txt")
VENV_INFO = os.path.join(PROJECT_DIR, "venv_info.txt")

EXPECTED_VENV_INFO = (
    "venv_path=/home/user/migration_project/venv\n"
    "packages=requests,boto3,click\n"
)


def test_venv_directory_exists():
    assert os.path.isdir(VENV_DIR), (
        f"Virtual environment directory '{VENV_DIR}' does not exist. "
        "The venv must be created at this path."
    )


def test_venv_python_exists():
    assert os.path.isfile(VENV_PYTHON), (
        f"Python interpreter '{VENV_PYTHON}' does not exist. "
        "The virtual environment must have a valid Python interpreter."
    )


def test_venv_python_is_executable():
    assert os.access(VENV_PYTHON, os.X_OK), (
        f"Python interpreter '{VENV_PYTHON}' exists but is not executable. "
        "The interpreter must have executable permissions."
    )


def test_venv_pip_exists():
    assert os.path.isfile(VENV_PIP), (
        f"pip executable '{VENV_PIP}' does not exist. "
        "The virtual environment must have pip installed."
    )


def test_venv_pip_is_executable():
    assert os.access(VENV_PIP, os.X_OK), (
        f"pip executable '{VENV_PIP}' exists but is not executable. "
        "The pip executable must have executable permissions."
    )


def _get_pip_show_version(package_name):
    """Run pip show for a package and return the version string, or None on failure."""
    result = subprocess.run(
        [VENV_PIP, "show", package_name],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    for line in result.stdout.splitlines():
        if line.startswith("Version:"):
            return line.split(":", 1)[1].strip()
    return None


def test_requests_installed_correct_version():
    assert os.path.isfile(VENV_PIP), (
        f"pip not found at '{VENV_PIP}'; cannot check package versions."
    )
    version = _get_pip_show_version("requests")
    assert version is not None, (
        "Package 'requests' is not installed in the virtual environment. "
        f"Run: {VENV_PIP} install requests==2.28.2"
    )
    assert version == "2.28.2", (
        f"Package 'requests' has version '{version}', expected '2.28.2'. "
        "Install the exact version: requests==2.28.2"
    )


def test_boto3_installed_correct_version():
    assert os.path.isfile(VENV_PIP), (
        f"pip not found at '{VENV_PIP}'; cannot check package versions."
    )
    version = _get_pip_show_version("boto3")
    assert version is not None, (
        "Package 'boto3' is not installed in the virtual environment. "
        f"Run: {VENV_PIP} install boto3==1.26.90"
    )
    assert version == "1.26.90", (
        f"Package 'boto3' has version '{version}', expected '1.26.90'. "
        "Install the exact version: boto3==1.26.90"
    )


def test_click_installed_correct_version():
    assert os.path.isfile(VENV_PIP), (
        f"pip not found at '{VENV_PIP}'; cannot check package versions."
    )
    version = _get_pip_show_version("click")
    assert version is not None, (
        "Package 'click' is not installed in the virtual environment. "
        f"Run: {VENV_PIP} install click==8.1.3"
    )
    assert version == "8.1.3", (
        f"Package 'click' has version '{version}', expected '8.1.3'. "
        "Install the exact version: click==8.1.3"
    )


def test_frozen_requirements_file_exists():
    assert os.path.isfile(FROZEN_REQUIREMENTS), (
        f"Frozen requirements file '{FROZEN_REQUIREMENTS}' does not exist. "
        f"Generate it by running: {VENV_PIP} freeze > {FROZEN_REQUIREMENTS}"
    )


def test_frozen_requirements_contains_requests():
    assert os.path.isfile(FROZEN_REQUIREMENTS), (
        f"Cannot check contents: '{FROZEN_REQUIREMENTS}' does not exist."
    )
    with open(FROZEN_REQUIREMENTS, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert "requests==2.28.2" in lines, (
        f"'requests==2.28.2' not found as a line in '{FROZEN_REQUIREMENTS}'. "
        f"File contents:\n" + "\n".join(lines)
    )


def test_frozen_requirements_contains_boto3():
    assert os.path.isfile(FROZEN_REQUIREMENTS), (
        f"Cannot check contents: '{FROZEN_REQUIREMENTS}' does not exist."
    )
    with open(FROZEN_REQUIREMENTS, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert "boto3==1.26.90" in lines, (
        f"'boto3==1.26.90' not found as a line in '{FROZEN_REQUIREMENTS}'. "
        f"File contents:\n" + "\n".join(lines)
    )


def test_frozen_requirements_contains_click():
    assert os.path.isfile(FROZEN_REQUIREMENTS), (
        f"Cannot check contents: '{FROZEN_REQUIREMENTS}' does not exist."
    )
    with open(FROZEN_REQUIREMENTS, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert "click==8.1.3" in lines, (
        f"'click==8.1.3' not found as a line in '{FROZEN_REQUIREMENTS}'. "
        f"File contents:\n" + "\n".join(lines)
    )


def test_frozen_requirements_has_multiple_lines():
    """The frozen requirements should have more than 3 lines due to transitive deps."""
    assert os.path.isfile(FROZEN_REQUIREMENTS), (
        f"Cannot check contents: '{FROZEN_REQUIREMENTS}' does not exist."
    )
    with open(FROZEN_REQUIREMENTS, "r") as f:
        lines = [line for line in f.readlines() if line.strip()]
    assert len(lines) > 3, (
        f"'{FROZEN_REQUIREMENTS}' has only {len(lines)} non-empty line(s). "
        "Expected more lines due to transitive dependencies from boto3/requests/click. "
        "Ensure the file was generated by 'pip freeze', not written manually."
    )


def test_venv_info_file_exists():
    assert os.path.isfile(VENV_INFO), (
        f"venv_info.txt file '{VENV_INFO}' does not exist. "
        "Create this file with the required content."
    )


def test_venv_info_file_exact_content():
    assert os.path.isfile(VENV_INFO), (
        f"Cannot check contents: '{VENV_INFO}' does not exist."
    )
    with open(VENV_INFO, "rb") as f:
        raw_content = f.read()
    # Decode and check exact content
    try:
        content = raw_content.decode("utf-8")
    except UnicodeDecodeError:
        pytest.fail(
            f"'{VENV_INFO}' is not valid UTF-8. "
            "The file must be a plain text file with UTF-8 encoding."
        )
    assert content == EXPECTED_VENV_INFO, (
        f"'{VENV_INFO}' does not have the exact expected content.\n"
        f"Expected (repr): {EXPECTED_VENV_INFO!r}\n"
        f"Got (repr):      {content!r}\n\n"
        "Ensure: exactly two lines, each ending with '\\n', no trailing spaces, no blank lines."
    )


def test_venv_info_line1():
    assert os.path.isfile(VENV_INFO), (
        f"Cannot check contents: '{VENV_INFO}' does not exist."
    )
    with open(VENV_INFO, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 1, (
        f"'{VENV_INFO}' is empty or has no lines."
    )
    assert lines[0] == "venv_path=/home/user/migration_project/venv\n", (
        f"First line of '{VENV_INFO}' is incorrect.\n"
        f"Expected: 'venv_path=/home/user/migration_project/venv\\n'\n"
        f"Got:      {lines[0]!r}"
    )


def test_venv_info_line2():
    assert os.path.isfile(VENV_INFO), (
        f"Cannot check contents: '{VENV_INFO}' does not exist."
    )
    with open(VENV_INFO, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 2, (
        f"'{VENV_INFO}' has fewer than 2 lines. "
        f"Got {len(lines)} line(s): {lines!r}"
    )
    assert lines[1] == "packages=requests,boto3,click\n", (
        f"Second line of '{VENV_INFO}' is incorrect.\n"
        f"Expected: 'packages=requests,boto3,click\\n'\n"
        f"Got:      {lines[1]!r}"
    )


def test_venv_info_exactly_two_lines():
    assert os.path.isfile(VENV_INFO), (
        f"Cannot check contents: '{VENV_INFO}' does not exist."
    )
    with open(VENV_INFO, "r") as f:
        lines = f.readlines()
    assert len(lines) == 2, (
        f"'{VENV_INFO}' must have exactly 2 lines, but has {len(lines)} line(s).\n"
        f"Lines: {lines!r}"
    )


def test_venv_is_valid_python_environment():
    """Verify the venv Python can actually run and reports a sane version."""
    assert os.path.isfile(VENV_PYTHON), (
        f"Cannot validate: Python interpreter '{VENV_PYTHON}' does not exist."
    )
    result = subprocess.run(
        [VENV_PYTHON, "--version"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Running '{VENV_PYTHON} --version' failed with return code {result.returncode}.\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )
    output = (result.stdout + result.stderr).strip()
    assert output.startswith("Python 3"), (
        f"Expected the venv Python to be Python 3, but got: '{output}'"
    )


def test_packages_not_installed_in_system_python():
    """
    Verify that the packages are installed in the venv, not leaked into system Python.
    We check that the venv pip's site-packages path is under the venv directory.
    """
    assert os.path.isfile(VENV_PIP), (
        f"Cannot check: pip not found at '{VENV_PIP}'."
    )
    result = subprocess.run(
        [VENV_PIP, "show", "requests"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        "'requests' is not installed in the venv pip."
    )
    location = None
    for line in result.stdout.splitlines():
        if line.startswith("Location:"):
            location = line.split(":", 1)[1].strip()
            break
    assert location is not None, (
        "Could not determine install location from 'pip show requests' output."
    )
    assert location.startswith(VENV_DIR), (
        f"'requests' appears to be installed at '{location}', "
        f"which is NOT inside the virtual environment '{VENV_DIR}'. "
        "Packages must only be installed into the virtual environment."
    )