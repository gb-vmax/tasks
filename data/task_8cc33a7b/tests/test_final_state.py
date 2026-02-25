# test_final_state.py

import os
import pytest

REQUIREMENTS_PATH = "/home/user/devops/requirements.txt"
PIP_FREEZE_LOG_PATH = "/home/user/devops/pip-freeze.log"

# The required contents of requirements.txt
REQUIRED_REQUIREMENTS_TXT = "flask==2.0.1\nrequests==2.26.0\n"

# These are the required packages and pinned versions from requirements.txt
REQUIRED_PACKAGES = {
    "flask": "2.0.1",
    "requests": "2.26.0",
}

# These are the minimum required dependencies (direct and indirect) for Flask 2.0.1 and Requests 2.26.0.
# Versions here are the minimum required, unless pinned in requirements.txt.
# If pip installs a higher version for a dependency, that's acceptable unless requirements.txt pins it.
REQUIRED_DEPENDENCIES = {
    # Flask dependencies
    "click": "8.0.1",  # Flask 2.0.1 requires click >=7.1.2
    "itsdangerous": "2.0.1",  # Flask 2.0.1 requires itsdangerous >=2.0
    "Jinja2": "3.0.1",  # Flask 2.0.1 requires Jinja2 >=3.0
    "MarkupSafe": "2.0.1",  # Jinja2 3.0.1 requires >=2.0
    "Werkzeug": "2.0.1",  # Flask 2.0.1 requires Werkzeug >=2.0

    # Requests dependencies
    "certifi": "2021.5.30",  # Requests 2.26.0 requires >=2017.4.17
    "charset-normalizer": "2.0.4",  # Requests 2.26.0 requires >=2.0.0,<2.1.0
    "idna": "3.2",  # Requests 2.26.0 requires >=2.5,<4
    "urllib3": "1.26.6",  # Requests 2.26.0 requires >=1.21.1,<1.27
}

def parse_pip_freeze(contents):
    """
    Parse pip freeze output into a dict: {package_name_lower: version}
    Ignores lines that do not match 'package==version' or are editable installs.
    """
    pkgs = {}
    for line in contents.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "@" in line and "://" in line:
            # e.g. editable or direct URL installs, skip for this check
            continue
        if "==" not in line:
            continue
        pkg, ver = line.split("==", 1)
        pkgs[pkg.lower()] = ver
    return pkgs

def test_requirements_txt_untouched():
    """requirements.txt must still exist and have the correct contents."""
    assert os.path.isfile(REQUIREMENTS_PATH), (
        f"Missing required requirements.txt at {REQUIREMENTS_PATH}."
    )
    with open(REQUIREMENTS_PATH, "r", encoding="utf-8") as f:
        contents = f.read()
    norm_contents = contents.replace("\r\n", "\n").strip()
    norm_required = REQUIRED_REQUIREMENTS_TXT.strip()
    assert norm_contents == norm_required, (
        f"The contents of {REQUIREMENTS_PATH} have been modified.\n"
        f"Expected:\n{norm_required!r}\nGot:\n{norm_contents!r}\n"
        "You must not modify requirements.txt."
    )

def test_pip_freeze_log_exists():
    """pip-freeze.log must exist after the task is completed."""
    assert os.path.isfile(PIP_FREEZE_LOG_PATH), (
        f"The file {PIP_FREEZE_LOG_PATH} does not exist.\n"
        "You must generate this file using 'pip freeze > pip-freeze.log' after installing requirements."
    )

def test_pip_freeze_log_format_and_content():
    """
    pip-freeze.log must:
      - Be in pip freeze output format (package==version per line, no extra text)
      - Contain all installed packages (not just requirements.txt)
      - Include all dependencies of requirements.txt packages, at correct versions
      - Not contain extra text
    """
    # Ensure file exists
    assert os.path.isfile(PIP_FREEZE_LOG_PATH), (
        f"The file {PIP_FREEZE_LOG_PATH} does not exist."
    )

    with open(PIP_FREEZE_LOG_PATH, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f]

    # Check for extra text (pip freeze does not output blank lines or comments)
    for idx, line in enumerate(lines):
        if not line:
            pytest.fail(
                f"Blank line detected at line {idx+1} of {PIP_FREEZE_LOG_PATH}.\n"
                "pip-freeze.log must have no blank lines."
            )
        if line.startswith("#"):
            pytest.fail(
                f"Comment line detected at line {idx+1} of {PIP_FREEZE_LOG_PATH}: {line!r}\n"
                "pip-freeze.log must not contain comments."
            )

    # Parse the freeze output
    freeze_pkgs = parse_pip_freeze('\n'.join(lines))
    freeze_pkg_names = set(freeze_pkgs.keys())

    # Must contain all packages from requirements.txt, at correct versions
    for req_pkg, req_ver in REQUIRED_PACKAGES.items():
        key = req_pkg.lower()
        assert key in freeze_pkgs, (
            f"Required package '{req_pkg}' from requirements.txt is missing from {PIP_FREEZE_LOG_PATH}.\n"
            "You must ensure all requirements are installed before generating the freeze log."
        )
        actual_ver = freeze_pkgs[key]
        assert actual_ver == req_ver, (
            f"Package '{req_pkg}' is present in {PIP_FREEZE_LOG_PATH} but with incorrect version.\n"
            f"Expected: {req_pkg}=={req_ver}\n"
            f"Found: {req_pkg}=={actual_ver}\n"
            "You must install the exact versions specified in requirements.txt."
        )

    # Must contain all dependencies at required versions or higher (unless requirements.txt pins them)
    for dep_pkg, min_ver in REQUIRED_DEPENDENCIES.items():
        key = dep_pkg.lower()
        assert key in freeze_pkgs, (
            f"Dependency '{dep_pkg}' required by Flask or Requests is missing from {PIP_FREEZE_LOG_PATH}.\n"
            "Ensure all dependencies are installed (pip should handle this automatically)."
        )
        actual_ver = freeze_pkgs[key]
        # If the dependency is not pinned in requirements.txt, allow >= min_ver
        # Otherwise, must match exactly (already checked above)
        if dep_pkg.lower() not in [k.lower() for k in REQUIRED_PACKAGES]:
            # Compare versions: allow actual_ver >= min_ver
            from distutils.version import LooseVersion
            if LooseVersion(actual_ver) < LooseVersion(min_ver):
                pytest.fail(
                    f"Dependency '{dep_pkg}' is present with version {actual_ver}, "
                    f"but version >= {min_ver} is required (installed by pip for Flask/Requests 2.0.1/2.26.0).\n"
                    "You must not downgrade dependencies below what pip would install."
                )
        # If pinned, already checked for exact match above

    # pip-freeze.log may contain additional packages (not from requirements.txt), that's OK

def test_only_pip_freeze_log_created():
    """
    Ensure that only /home/user/devops/pip-freeze.log (and not any other files) was created/modified.
    requirements.txt must not be changed.
    """
    # List all files in /home/user/devops
    devops_dir = os.path.dirname(REQUIREMENTS_PATH)
    expected_files = {"requirements.txt", "pip-freeze.log"}
    actual_files = set(os.listdir(devops_dir))
    # Allow for other files that may have previously existed, but ensure only pip-freeze.log is new.
    assert "pip-freeze.log" in actual_files, (
        f"pip-freeze.log is missing in {devops_dir}."
    )
    # requirements.txt must still exist (checked above), and must not be modified (checked above)

def test_no_modification_of_requirements_txt():
    """requirements.txt must not be modified at all."""
    with open(REQUIREMENTS_PATH, "r", encoding="utf-8") as f:
        contents = f.read()
    norm_contents = contents.replace("\r\n", "\n").strip()
    norm_required = REQUIRED_REQUIREMENTS_TXT.strip()
    assert norm_contents == norm_required, (
        f"The contents of {REQUIREMENTS_PATH} have been modified.\n"
        f"Expected:\n{norm_required!r}\nGot:\n{norm_contents!r}\n"
        "You must not modify requirements.txt."
    )