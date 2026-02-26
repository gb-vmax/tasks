# test_final_state.py

import os
import sys
import stat
import subprocess
import pytest

ETL_PROJECT_DIR = "/home/user/etl_project"
VENV_DIR = os.path.join(ETL_PROJECT_DIR, "venv")
REQUIREMENTS_LOCKED = os.path.join(ETL_PROJECT_DIR, "requirements-locked.txt")
ETL_TEST_PY = os.path.join(ETL_PROJECT_DIR, "etl_test.py")
ETL_TEST_OUTPUT = os.path.join(ETL_PROJECT_DIR, "etl_test_output.log")

REQUIRED_FILES = {
    "venv_dir": VENV_DIR,
    "requirements_locked": REQUIREMENTS_LOCKED,
    "etl_test_py": ETL_TEST_PY,
    "etl_test_output": ETL_TEST_OUTPUT,
}

REQUIRED_PACKAGES = {
    "pandas": "1.4.2",
    "requests": "2.27.1",
    "pyarrow": "8.0.0",
}

ETL_TEST_PY_EXPECTED = (
    "import pandas\n"
    "import requests\n"
    "import pyarrow\n"
    "\n"
    "print(f\"pandas: {pandas.__version__}\")\n"
    "print(f\"requests: {requests.__version__}\")\n"
    "print(f\"pyarrow: {pyarrow.__version__}\")\n"
)

ETL_TEST_OUTPUT_EXPECTED = (
    "pandas: 1.4.2\n"
    "requests: 2.27.1\n"
    "pyarrow: 8.0.0\n"
)

def test_etl_project_dir_exists_and_is_dir():
    assert os.path.isdir(ETL_PROJECT_DIR), (
        f"Directory {ETL_PROJECT_DIR} does not exist or is not a directory."
    )

def test_required_files_and_dirs_exist_and_no_extras():
    # Check required files and directories exist
    for key, path in REQUIRED_FILES.items():
        if key == "venv_dir":
            assert os.path.isdir(path), f"Virtual environment directory missing: {path}"
        else:
            assert os.path.isfile(path), f"Required file missing: {path}"

    # Ensure no extra files/directories are present except what is required
    allowed = {"venv", "requirements-locked.txt", "etl_test.py", "etl_test_output.log"}
    found = set(os.listdir(ETL_PROJECT_DIR))
    extras = found - allowed
    assert not extras, (
        f"Found unexpected files or directories in {ETL_PROJECT_DIR}: {sorted(extras)}"
    )

def test_venv_directory_valid():
    # venv directory must contain a bin/python or Scripts/python.exe (for completeness, but Linux expected)
    if sys.platform == "win32":
        python_path = os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        python_path = os.path.join(VENV_DIR, "bin", "python")
    assert os.path.isfile(python_path), (
        f"Virtual environment python interpreter not found at {python_path}"
    )
    # Should be executable
    st = os.stat(python_path)
    assert (st.st_mode & stat.S_IXUSR), (
        f"Virtual environment python interpreter is not executable: {python_path}"
    )

def test_requirements_locked_contains_required_packages():
    # Read requirements-locked.txt
    with open(REQUIREMENTS_LOCKED, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    # Check that the required lines are present (order can vary, other lines can be present)
    for pkg, ver in REQUIRED_PACKAGES.items():
        expected_line = f"{pkg}=={ver}"
        assert any(line.lower() == expected_line for line in lines), (
            f"requirements-locked.txt missing required line: '{expected_line}'"
        )
    # Check for duplicate lines for the same package (should not happen in pip freeze)
    pkgs = [line.split("==")[0].lower() for line in lines if "==" in line]
    for pkg in REQUIRED_PACKAGES:
        assert pkgs.count(pkg) == 1, (
            f"requirements-locked.txt contains duplicate entries for package '{pkg}'"
        )

def test_etl_test_py_content_exact():
    with open(ETL_TEST_PY, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ETL_TEST_PY_EXPECTED, (
        f"The content of etl_test.py is not exactly as specified.\n"
        f"Expected:\n{ETL_TEST_PY_EXPECTED!r}\n"
        f"Found:\n{content!r}\n"
        "Please ensure formatting, spacing, and indentation are exactly as required."
    )

def test_etl_test_output_log_content_exact():
    with open(ETL_TEST_OUTPUT, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ETL_TEST_OUTPUT_EXPECTED, (
        f"The content of etl_test_output.log is not exactly as specified.\n"
        f"Expected:\n{ETL_TEST_OUTPUT_EXPECTED!r}\n"
        f"Found:\n{content!r}\n"
        "Please ensure there are no extra or missing lines, and the output matches exactly."
    )

def _venv_python_path():
    # Returns the absolute path to the venv's python interpreter
    if sys.platform == "win32":
        return os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        return os.path.join(VENV_DIR, "bin", "python")

def test_etl_test_py_runs_and_outputs_expected(monkeypatch):
    # Run the test script with the venv's python and check output matches exactly
    python_exe = _venv_python_path()
    assert os.path.isfile(python_exe), (
        f"Could not find venv python interpreter at {python_exe}"
    )
    # Run: venv/bin/python etl_test.py
    proc = subprocess.run(
        [python_exe, ETL_TEST_PY],
        cwd=ETL_PROJECT_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    )
    output = proc.stdout
    err_output = proc.stderr
    assert proc.returncode == 0, (
        f"Running etl_test.py with the venv python failed with return code {proc.returncode}.\n"
        f"Stdout:\n{output}\nStderr:\n{err_output}"
    )
    assert output == ETL_TEST_OUTPUT_EXPECTED, (
        "Running etl_test.py did not produce the expected output.\n"
        f"Expected:\n{ETL_TEST_OUTPUT_EXPECTED!r}\n"
        f"Found:\n{output!r}\n"
        f"Stderr:\n{err_output!r}"
    )

def test_installed_packages_in_venv_are_correct():
    # Use venv's pip to get freeze output, check required packages and versions are present
    python_exe = _venv_python_path()
    pip_exe = os.path.join(os.path.dirname(python_exe), "pip")
    assert os.path.isfile(pip_exe), (
        f"pip not found in virtual environment at {pip_exe}"
    )
    proc = subprocess.run(
        [pip_exe, "freeze"],
        cwd=ETL_PROJECT_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    )
    output = proc.stdout
    err_output = proc.stderr
    assert proc.returncode == 0, (
        f"pip freeze in venv failed with return code {proc.returncode}.\n"
        f"Stdout:\n{output}\nStderr:\n{err_output}"
    )
    freeze_lines = [line.strip() for line in output.splitlines() if line.strip()]
    for pkg, ver in REQUIRED_PACKAGES.items():
        expected_line = f"{pkg}=={ver}"
        assert any(line.lower() == expected_line for line in freeze_lines), (
            f"pip freeze output from venv missing required package/version: '{expected_line}'\n"
            f"Full freeze output:\n{output}"
        )

def test_only_expected_files_in_etl_project_dir():
    # No extra files or directories except venv, requirements-locked.txt, etl_test.py, etl_test_output.log
    allowed = {"venv", "requirements-locked.txt", "etl_test.py", "etl_test_output.log"}
    found = set(os.listdir(ETL_PROJECT_DIR))
    extras = found - allowed
    assert not extras, (
        f"Found unexpected files or directories in {ETL_PROJECT_DIR}: {sorted(extras)}"
    )