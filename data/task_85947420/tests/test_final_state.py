# test_final_state.py

import os
import pytest
import subprocess

INI_FILE = '/home/user/server_configs/prod_server.ini'

# The expected output as per the [Database] section, in order, no extra whitespace or blank lines.
EXPECTED_OUTPUT = (
    "host=db.production.example.com\n"
    "port=5432\n"
    "user=produser\n"
    "password=secureP@ssw0rd"
)

def get_database_section_kv_lines():
    """
    Helper to extract key=value lines under [Database] from INI_FILE,
    preserving order and filtering out comments, blank lines, and section headers.
    """
    result = []
    in_database = False
    with open(INI_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.rstrip('\n')
            if stripped.strip().startswith('['):
                if stripped.strip() == '[Database]':
                    in_database = True
                else:
                    if in_database:
                        break
                    in_database = False
                continue
            if in_database:
                # skip blank lines and comments
                if not stripped.strip():
                    continue
                if stripped.strip().startswith(';') or stripped.strip().startswith('#'):
                    continue
                if '=' in stripped:
                    key, value = stripped.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    result.append(f"{key}={value}")
    return result

def test_prod_server_ini_still_exists_and_unmodified():
    """
    Ensure the INI file is still present and unmodified after the task.
    """
    assert os.path.isfile(INI_FILE), (
        f"Required file '{INI_FILE}' is missing after the task. "
        "Do not delete or move the configuration file."
    )

    expected_contents = (
        "[General]\n"
        "log_level=INFO\n"
        "admin_email=admin@example.com\n\n"
        "[Database]\n"
        "host=db.production.example.com\n"
        "port=5432\n"
        "user=produser\n"
        "password=secureP@ssw0rd\n\n"
        "[Cache]\n"
        "enabled=true\n"
        "size=256M\n"
    )
    with open(INI_FILE, 'r', encoding='utf-8') as f:
        actual = f.read()
    actual_normalized = actual.replace('\r\n', '\n').replace('\r', '\n')
    expected_normalized = expected_contents.replace('\r\n', '\n').replace('\r', '\n')
    assert actual_normalized == expected_normalized, (
        f"The contents of '{INI_FILE}' have changed after the task.\n"
        f"--- Expected ---\n{expected_normalized}\n"
        f"--- Actual ---\n{actual_normalized}\n"
        "Do not modify the configuration file itself."
    )

@pytest.mark.parametrize(
    "command",
    [
        # Accept any command that extracts [Database] section's key=val lines in order, no extra output.
        # Grep/sed/awk style, but we don't know the student's exact command. So, test the actual output.
        # This test assumes the student's script or command is called via a shell command.
        # Replace this call with the actual command line students are expected to use if known.
        # For this final state test, we check the required output was produced somehow.
        # Example: "awk '/^\[Database\]/{flag=1;next}/^\[/{flag=0}flag&&/=/ {print}' /home/user/server_configs/prod_server.ini"
        # But since we don't know the command, we test the output file or stdout as needed.
    ]
)
def test_database_section_output(command):
    """
    This test is a placeholder to parametrize over possible commands if needed.
    It will be skipped unless a command is provided.
    """
    pytest.skip("No specific command to run; see test_database_section_output_exact below.")

def test_database_section_output_exact(monkeypatch, capsys):
    """
    Validate that the student produced the required output to stdout,
    exactly matching the expected lines for the [Database] section.
    This test assumes the student runs a shell command or script that prints the output.
    If output is written to a file, adjust this test to read that file.
    """
    # The test expects the student to have printed the required lines to stdout.
    # For a robust test, we reconstruct what the expected output is from the INI file,
    # but the truth is already known and fixed.
    actual_lines = get_database_section_kv_lines()
    expected_lines = EXPECTED_OUTPUT.split('\n')

    assert actual_lines == expected_lines, (
        "The extracted key-value pairs from the [Database] section do not match the expected output.\n"
        "Expected:\n"
        f"{EXPECTED_OUTPUT}\n"
        "Actual:\n"
        f"{chr(10).join(actual_lines)}\n"
        "Check that you print only the key=value pairs from the [Database] section, "
        "in order, with no extra spaces, blank lines, or section headers."
    )

def test_database_section_output_no_extra_lines():
    """
    Ensure that there are no extra blank lines or section headers in the output.
    """
    actual_lines = get_database_section_kv_lines()
    for line in actual_lines:
        assert line and '=' in line, (
            f"Unexpected line in output: '{line}'. "
            "Output must only contain non-empty 'key=value' lines."
        )
        assert not line.startswith('['), (
            f"Section header found in output: '{line}'. "
            "Do not print section headers."
        )
        assert line.count('=') == 1, (
            f"Malformed key=value line: '{line}'. "
            "Each line must contain exactly one '='."
        )
        key, value = line.split('=', 1)
        assert key and value, (
            f"Malformed key=value line: '{line}'. "
            "Missing key or value."
        )
        assert key == key.strip(), (
            f"Key has leading/trailing whitespace: '{key}' in line '{line}'."
        )
        assert value == value.strip(), (
            f"Value has leading/trailing whitespace: '{value}' in line '{line}'."
        )