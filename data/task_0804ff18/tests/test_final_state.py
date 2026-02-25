# test_final_state.py

import os
import pytest
import subprocess

HOME = "/home/user"
DATASET_SETUP_DIR = os.path.join(HOME, "dataset_setup")
PACKAGE_LOG = os.path.join(DATASET_SETUP_DIR, "package_log.txt")


def get_installed_pandas_version():
    """
    Returns the installed pandas version as a string (e.g., '2.1.1').
    Raises AssertionError if pandas is not installed or cannot be imported.
    """
    try:
        output = subprocess.check_output(
            ["python3", "-c", "import pandas; print(pandas.__version__)"],
            universal_newlines=True,
            stderr=subprocess.STDOUT
        )
        version = output.strip()
        # Basic version validation
        assert version.count('.') >= 1 and all(part.isdigit() for part in version.split('.')), (
            f"Invalid pandas version string reported: '{version}'"
        )
        return version
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Could not import pandas in the current environment: {e.output}")
    except Exception as exc:
        pytest.fail(f"Unexpected error when checking pandas version: {exc}")


def test_dataset_setup_directory_exists():
    assert os.path.isdir(DATASET_SETUP_DIR), (
        f"Directory '{DATASET_SETUP_DIR}' does not exist. "
        "It must be created as part of the task."
    )


def test_package_log_file_exists():
    assert os.path.isfile(PACKAGE_LOG), (
        f"Log file '{PACKAGE_LOG}' does not exist. "
        "It must be created as part of the task."
    )


def test_package_log_file_format_and_content():
    # Read the log file lines
    try:
        with open(PACKAGE_LOG, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except Exception as exc:
        pytest.fail(f"Could not read '{PACKAGE_LOG}': {exc}")

    # Must be exactly two lines, no blank lines
    assert len(lines) == 2, (
        f"Log file '{PACKAGE_LOG}' must contain exactly two lines (no blank lines). "
        f"Found {len(lines)} lines: {lines!r}"
    )

    # First line must be strictly correct
    valid_first_lines = {"pandas installed", "pandas already installed"}
    first_line = lines[0]
    assert first_line in valid_first_lines, (
        f"First line of '{PACKAGE_LOG}' must be either 'pandas installed' or 'pandas already installed', "
        f"but found: '{first_line}'"
    )

    # Second line must be strictly correct format and match actual installed version
    second_line = lines[1]
    prefix = "pandas version: "
    assert second_line.startswith(prefix), (
        f"Second line of '{PACKAGE_LOG}' must start with '{prefix}', but found: '{second_line}'"
    )
    version_in_log = second_line[len(prefix):]
    # Validate version string looks like x.y.z
    version_parts = version_in_log.split(".")
    assert (
        len(version_parts) >= 2 and all(part.isdigit() for part in version_parts)
    ), (
        f"Second line of '{PACKAGE_LOG}' must contain a valid pandas version after '{prefix}', "
        f"but found: '{version_in_log}'"
    )

    # Check the actual installed pandas version matches the log
    actual_version = get_installed_pandas_version()
    assert version_in_log == actual_version, (
        f"Version in '{PACKAGE_LOG}' ('{version_in_log}') does not match the "
        f"actual installed pandas version ('{actual_version}')."
    )