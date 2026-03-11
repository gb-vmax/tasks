# test_final_state.py

import os
import pytest

VENV_DIR = "/home/user/profiling_env"
REQUIREMENTS_TXT = "/home/user/profiling_env/requirements.txt"
VENV_PYTHON = "/home/user/profiling_env/bin/python"
VENV_PIP = "/home/user/profiling_env/bin/pip"


def test_venv_directory_exists():
    """The virtual environment directory must exist."""
    assert os.path.isdir(VENV_DIR), (
        f"Virtual environment directory {VENV_DIR} does not exist. "
        "Run: python3 -m venv /home/user/profiling_env"
    )


def test_venv_python_exists():
    """The virtual environment Python binary must exist."""
    assert os.path.isfile(VENV_PYTHON), (
        f"Virtual environment Python binary not found at {VENV_PYTHON}. "
        "The virtual environment may not have been created correctly."
    )


def test_venv_pip_exists():
    """The virtual environment pip binary must exist."""
    assert os.path.isfile(VENV_PIP), (
        f"Virtual environment pip not found at {VENV_PIP}. "
        "The virtual environment may not have been created correctly."
    )


def test_requirements_txt_exists():
    """The requirements.txt file must exist at the expected path."""
    assert os.path.isfile(REQUIREMENTS_TXT), (
        f"requirements.txt not found at {REQUIREMENTS_TXT}. "
        "Run: /home/user/profiling_env/bin/pip freeze > /home/user/profiling_env/requirements.txt"
    )


def _get_requirements_lines():
    """Helper to read and return stripped non-empty lines from requirements.txt."""
    with open(REQUIREMENTS_TXT, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return [line for line in lines if line]


def test_requirements_txt_is_not_empty():
    """The requirements.txt file must not be empty."""
    lines = _get_requirements_lines()
    assert len(lines) > 0, (
        f"{REQUIREMENTS_TXT} is empty. "
        "Run pip freeze and redirect output to the file."
    )


def test_memory_profiler_in_requirements():
    """requirements.txt must contain the exact line 'memory-profiler==0.61.0'."""
    lines = _get_requirements_lines()
    assert "memory-profiler==0.61.0" in lines, (
        f"'memory-profiler==0.61.0' not found in {REQUIREMENTS_TXT}. "
        f"Current contents:\n" + "\n".join(lines)
    )


def test_pyinstrument_in_requirements():
    """requirements.txt must contain the exact line 'pyinstrument==4.6.1'."""
    lines = _get_requirements_lines()
    assert "pyinstrument==4.6.1" in lines, (
        f"'pyinstrument==4.6.1' not found in {REQUIREMENTS_TXT}. "
        f"Current contents:\n" + "\n".join(lines)
    )


def test_psutil_in_requirements():
    """requirements.txt must contain a psutil entry (transitive dep of memory-profiler)."""
    lines = _get_requirements_lines()
    psutil_lines = [line for line in lines if line.startswith("psutil==")]
    assert len(psutil_lines) > 0, (
        f"No 'psutil==<version>' line found in {REQUIREMENTS_TXT}. "
        "psutil is a required transitive dependency of memory-profiler. "
        f"Current contents:\n" + "\n".join(lines)
    )


def test_requirements_format_is_valid():
    """Every non-empty line in requirements.txt must follow 'package==version' format."""
    lines = _get_requirements_lines()
    invalid_lines = []
    for line in lines:
        # pip freeze output lines should be in package==version format
        # (ignoring comment lines starting with #)
        if line.startswith("#"):
            continue
        if "==" not in line:
            invalid_lines.append(line)
    assert len(invalid_lines) == 0, (
        f"Some lines in {REQUIREMENTS_TXT} do not follow 'package==version' format:\n"
        + "\n".join(invalid_lines)
    )


def test_memory_profiler_installed_in_venv():
    """memory-profiler must be importable from the virtual environment."""
    import subprocess
    result = subprocess.run(
        [VENV_PYTHON, "-c", "import memory_profiler; print(memory_profiler.__version__)"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"memory_profiler could not be imported from the virtual environment. "
        f"stderr: {result.stderr.strip()}"
    )
    version = result.stdout.strip()
    assert version == "0.61.0", (
        f"memory-profiler version mismatch: expected '0.61.0', got '{version}'"
    )


def test_pyinstrument_installed_in_venv():
    """pyinstrument must be importable from the virtual environment."""
    import subprocess
    result = subprocess.run(
        [VENV_PYTHON, "-c", "import pyinstrument; print(pyinstrument.__version__)"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"pyinstrument could not be imported from the virtual environment. "
        f"stderr: {result.stderr.strip()}"
    )
    version = result.stdout.strip()
    assert version == "4.6.1", (
        f"pyinstrument version mismatch: expected '4.6.1', got '{version}'"
    )


def test_requirements_txt_matches_pip_freeze():
    """The requirements.txt content must match what pip freeze currently outputs."""
    import subprocess
    result = subprocess.run(
        [VENV_PIP, "freeze"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"pip freeze failed: {result.stderr.strip()}"
    )
    freeze_lines = set(line.strip() for line in result.stdout.splitlines() if line.strip())
    with open(REQUIREMENTS_TXT, "r") as f:
        file_lines = set(line.strip() for line in f.readlines() if line.strip())

    missing_from_file = freeze_lines - file_lines
    extra_in_file = file_lines - freeze_lines

    assert not missing_from_file and not extra_in_file, (
        f"requirements.txt does not match current pip freeze output.\n"
        f"Lines in pip freeze but missing from file: {missing_from_file}\n"
        f"Lines in file but not in pip freeze: {extra_in_file}"
    )