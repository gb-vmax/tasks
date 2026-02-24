# test_final_state.py

import os
import sys
import stat
import subprocess
import re
import pytest

HOME_DIR = "/home/user"
VENV_DIR = "/home/user/diskmon-env"
PIP_FREEZE_LOG = "/home/user/diskmon-env/pip-freeze.log"

REQUIRED_PACKAGES = {
    "psutil": "5.9.8",
    "click": "8.1.7",
}

def _find_venv_python(venv_dir):
    """
    Return the path to the python executable inside the venv.
    Works for both Unix and Windows venvs.
    """
    candidates = [
        os.path.join(venv_dir, "bin", "python"),
        os.path.join(venv_dir, "Scripts", "python.exe"),
        os.path.join(venv_dir, "Scripts", "python"),
    ]
    for c in candidates:
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    return None

def _find_venv_pip(venv_dir):
    """
    Return the path to the pip executable inside the venv.
    """
    candidates = [
        os.path.join(venv_dir, "bin", "pip"),
        os.path.join(venv_dir, "Scripts", "pip.exe"),
        os.path.join(venv_dir, "Scripts", "pip"),
    ]
    for c in candidates:
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    return None

def _is_venv_dir(venv_dir):
    """
    Checks if the given directory appears to be a Python venv.
    Looks for pyvenv.cfg and bin/python (Unix) or Scripts/python.exe (Windows).
    """
    pyvenv_cfg = os.path.join(venv_dir, "pyvenv.cfg")
    python_exe = _find_venv_python(venv_dir)
    return os.path.isfile(pyvenv_cfg) and python_exe is not None

def _read_pip_freeze_file(filepath):
    """
    Reads the pip-freeze.log file and returns a dict: {package: version}
    Ignores comments and blank lines.
    """
    pkgs = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            m = re.match(r"^([A-Za-z0-9_.\-]+)==([^\s]+)$", line)
            if not m:
                raise AssertionError(
                    f"Line {lineno} in '{filepath}' is not a valid 'package==version' entry: {line!r}"
                )
            pkg, ver = m.group(1), m.group(2)
            pkgs[pkg.lower()] = ver
    return pkgs

def _run_in_venv(venv_python, args):
    """
    Runs a command using the venv's python executable.
    Returns (exitcode, stdout, stderr)
    """
    proc = subprocess.run(
        [venv_python] + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    )
    return proc.returncode, proc.stdout, proc.stderr

def test_venv_directory_exists_and_is_venv():
    assert os.path.isdir(VENV_DIR), (
        f"Virtual environment directory '{VENV_DIR}' does not exist."
    )
    # Check for pyvenv.cfg and python executable
    assert _is_venv_dir(VENV_DIR), (
        f"Directory '{VENV_DIR}' does not appear to be a valid Python virtual environment."
    )

def test_venv_python_and_pip_exist_and_work():
    python_path = _find_venv_python(VENV_DIR)
    pip_path = _find_venv_pip(VENV_DIR)
    assert python_path is not None, (
        f"Could not find Python executable in virtual environment at '{VENV_DIR}'."
    )
    assert pip_path is not None, (
        f"Could not find pip executable in virtual environment at '{VENV_DIR}'."
    )
    # Check that python --version works
    rc, out, err = subprocess.run(
        [python_path, "--version"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    ).returncode, None, None
    assert rc == 0, (
        f"Python in venv at '{python_path}' does not run successfully."
    )
    # Check that pip --version works
    rc, out, err = subprocess.run(
        [pip_path, "--version"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    ).returncode, None, None
    assert rc == 0, (
        f"Pip in venv at '{pip_path}' does not run successfully."
    )

def test_pip_freeze_log_exists_and_format():
    assert os.path.isfile(PIP_FREEZE_LOG), (
        f"pip-freeze.log file '{PIP_FREEZE_LOG}' does not exist after task completion."
    )
    # Check readable and not empty
    st = os.stat(PIP_FREEZE_LOG)
    assert st.st_size > 0, (
        f"pip-freeze.log file '{PIP_FREEZE_LOG}' is empty."
    )
    # Check format: only lines of package==version
    with open(PIP_FREEZE_LOG, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    assert lines, (
        f"pip-freeze.log file '{PIP_FREEZE_LOG}' is empty."
    )
    for lineno, line in enumerate(lines, 1):
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^[A-Za-z0-9_.\-]+==[^\s]+$", line)
        assert m, (
            f"Line {lineno} in '{PIP_FREEZE_LOG}' is not a valid 'package==version' entry: {line!r}"
        )

def test_pip_freeze_log_contains_required_packages_and_versions():
    pkgs = _read_pip_freeze_file(PIP_FREEZE_LOG)
    missing = []
    wrong_version = []
    for pkg, ver in REQUIRED_PACKAGES.items():
        found = pkgs.get(pkg)
        if found is None:
            missing.append(pkg)
        elif found != ver:
            wrong_version.append(f"{pkg}=={found} (expected {ver})")
    msg = ""
    if missing:
        msg += (
            f"pip-freeze.log is missing required packages: {', '.join(missing)}. "
        )
    if wrong_version:
        msg += (
            f"pip-freeze.log has incorrect versions: {', '.join(wrong_version)}. "
        )
    assert not missing and not wrong_version, msg

def test_pip_freeze_log_matches_actual_venv_state():
    """
    Ensure the contents of pip-freeze.log match the actual output of 'pip freeze' in the venv.
    """
    python_path = _find_venv_python(VENV_DIR)
    assert python_path, "Could not find Python executable in venv."
    rc, pip_freeze_out, pip_freeze_err = _run_in_venv(python_path, ["-m", "pip", "freeze"])
    assert rc == 0, (
        f"Failed to run 'pip freeze' in the virtual environment:\n{pip_freeze_err}"
    )
    actual_pkgs = {}
    for lineno, line in enumerate(pip_freeze_out.strip().splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_.\-]+)==([^\s]+)$", line)
        if not m:
            continue
        pkg, ver = m.group(1), m.group(2)
        actual_pkgs[pkg.lower()] = ver
    file_pkgs = _read_pip_freeze_file(PIP_FREEZE_LOG)
    # Compare
    if actual_pkgs != file_pkgs:
        # Provide a diff-like output
        missing = sorted(set(actual_pkgs) - set(file_pkgs))
        extra = sorted(set(file_pkgs) - set(actual_pkgs))
        mismatched = sorted(
            pkg for pkg in set(actual_pkgs) & set(file_pkgs)
            if actual_pkgs[pkg] != file_pkgs[pkg]
        )
        msg = []
        if missing:
            msg.append(f"pip-freeze.log is missing packages: {', '.join(missing)}")
        if extra:
            msg.append(f"pip-freeze.log has extra/unexpected packages: {', '.join(extra)}")
        if mismatched:
            msg.append("pip-freeze.log has version mismatches:\n" + "\n".join(
                f"  {pkg}: file has {file_pkgs[pkg]}, but venv has {actual_pkgs[pkg]}"
                for pkg in mismatched
            ))
        raise AssertionError(
            f"pip-freeze.log does not match the actual state of the virtual environment:\n" +
            "\n".join(msg)
        )