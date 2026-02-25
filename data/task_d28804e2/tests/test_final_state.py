# test_final_state.py

import os
import subprocess
import sys
import pytest

BUILD_CONFIG_DIR = "/home/user/projects/build_config"
ARTIFACTS_INI_PATH = os.path.join(BUILD_CONFIG_DIR, "artifacts.ini")

# The expected output, in order, from the student's script
EXPECTED_OUTPUT = ["libfoo.so", "pluginbaz.so"]


def parse_ini_release_names(ini_path):
    """
    Parse the INI file to extract the 'name' values from sections
    where 'status=release', preserving section order.
    """
    release_names = []
    section = None
    section_lines = []
    if not os.path.isfile(ini_path):
        raise FileNotFoundError(f"INI file '{ini_path}' does not exist.")

    with open(ini_path, encoding="utf-8") as f:
        lines = f.readlines()

    # Add a dummy section marker at the end for logic simplicity
    lines.append("[")

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            # New section starts
            if section is not None and section_lines:
                # Parse previous section
                section_dict = {}
                for sline in section_lines:
                    if "=" in sline:
                        k, v = sline.split("=", 1)
                        section_dict[k.strip()] = v.strip()
                if section_dict.get("status") == "release" and "name" in section_dict:
                    release_names.append(section_dict["name"])
            # Start new section
            section = stripped[1:-1].strip()
            section_lines = []
        elif section is not None:
            if stripped and not stripped.startswith(";") and not stripped.startswith("#"):
                section_lines.append(stripped)
    return release_names


def find_student_script():
    """
    Attempts to locate the student's script in the build config directory.
    Accepts only executable Python scripts (ending with .py).
    Returns the absolute path to the script.
    """
    for entry in os.listdir(BUILD_CONFIG_DIR):
        candidate = os.path.join(BUILD_CONFIG_DIR, entry)
        if (
            os.path.isfile(candidate)
            and entry.endswith(".py")
            and os.access(candidate, os.X_OK | os.R_OK)
        ):
            return candidate
    pytest.skip(
        f"No executable Python script (.py) found in {BUILD_CONFIG_DIR}. "
        "Cannot test student's solution."
    )


def run_student_script(script_path):
    """
    Runs the student's script with the correct working directory.
    Returns (exitcode, stdout, stderr).
    """
    # Use sys.executable to ensure Python 3
    proc = subprocess.run(
        [sys.executable, script_path],
        cwd=BUILD_CONFIG_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        timeout=10,
    )
    return proc.returncode, proc.stdout, proc.stderr


def test_artifacts_ini_unchanged():
    """
    The artifacts.ini file must be unchanged after the task.
    """
    expected_content = (
        "[artifact_alpha]\n"
        "name=libfoo.so\n"
        "type=library\n"
        "status=release\n\n"
        "[artifact_beta]\n"
        "name=appbar\n"
        "type=executable\n"
        "status=staging\n\n"
        "[artifact_gamma]\n"
        "name=pluginbaz.so\n"
        "type=plugin\n"
        "status=release\n"
    )
    assert os.path.isfile(ARTIFACTS_INI_PATH), (
        f"Expected INI file '{ARTIFACTS_INI_PATH}' to exist after the task."
    )
    with open(ARTIFACTS_INI_PATH, encoding="utf-8") as f:
        actual = f.read().replace("\r\n", "\n")
    assert actual.strip() == expected_content.strip(), (
        "The contents of 'artifacts.ini' were changed. "
        "The file must remain exactly as originally provided."
    )


def test_student_script_output_matches_expected():
    """
    The student's script must print the correct artifact names (status=release),
    one per line, in the correct order, with no extra content.
    """
    script_path = find_student_script()
    exitcode, stdout, stderr = run_student_script(script_path)

    # Check script exit code
    assert exitcode == 0, (
        f"Student script '{os.path.basename(script_path)}' did not exit cleanly (exit code {exitcode}).\n"
        f"Stderr:\n{stderr}"
    )

    # Normalize and split output
    output_lines = stdout.replace("\r\n", "\n").split("\n")
    output_lines = [line.strip() for line in output_lines if line.strip() != ""]

    # Check output content
    assert output_lines == EXPECTED_OUTPUT, (
        f"Incorrect output from student script.\n"
        f"Expected:\n{chr(10).join(EXPECTED_OUTPUT)}\n\n"
        f"Found:\n{chr(10).join(output_lines)}\n"
        "The output must contain only the 'name' values of all artifacts where status=release, "
        "one per line, in the correct order, with no extra spaces or lines."
    )


def test_student_script_does_not_print_extra_content():
    """
    The script output must not contain any section names, keys, or values not matching the requirement.
    """
    script_path = find_student_script()
    _, stdout, _ = run_student_script(script_path)
    output = stdout.replace("\r\n", "\n")
    forbidden_substrings = [
        "[artifact_alpha]",
        "[artifact_beta]",
        "[artifact_gamma]",
        "type=",
        "status=",
        "name=",
        "appbar",  # Not a release artifact
    ]
    for forbidden in forbidden_substrings:
        assert forbidden not in output, (
            f"Output contains forbidden content: '{forbidden}'.\n"
            "The output must only include the artifact name(s) for status=release, "
            "one per line, with no extra info."
        )


def test_student_script_output_order():
    """
    The order of artifact names in the output must match their order in the INI file
    (artifact_alpha's name, then artifact_gamma's name).
    """
    script_path = find_student_script()
    _, stdout, _ = run_student_script(script_path)
    output_lines = stdout.replace("\r\n", "\n").split("\n")
    output_lines = [line.strip() for line in output_lines if line.strip() != ""]
    assert output_lines == EXPECTED_OUTPUT, (
        f"Artifact names are not printed in the correct order.\n"
        f"Expected order:\n{chr(10).join(EXPECTED_OUTPUT)}\n"
        f"Found:\n{chr(10).join(output_lines)}"
    )


def test_student_script_handles_multiple_release_sections():
    """
    If the INI file contains multiple sections with status=release, all 'name' values must be output, in order.
    """
    # We already have two in the original file; this test ensures both are present and in order.
    script_path = find_student_script()
    _, stdout, _ = run_student_script(script_path)
    output_lines = stdout.replace("\r\n", "\n").split("\n")
    output_lines = [line.strip() for line in output_lines if line.strip() != ""]
    assert output_lines == EXPECTED_OUTPUT, (
        f"Script did not output all artifact names with status=release.\n"
        f"Expected:\n{chr(10).join(EXPECTED_OUTPUT)}\n"
        f"Found:\n{chr(10).join(output_lines)}"
    )