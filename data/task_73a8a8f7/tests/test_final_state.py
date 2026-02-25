# test_final_state.py

import os
import pytest

HOME = "/home/user"
ENV_FILE = os.path.join(HOME, ".env.capacity")
OUTPUT_FILE = os.path.join(HOME, "capacity_output.log")

ENV_EXPECTED_LINES = [
    "MAX_CPU=8",
    "MAX_MEM_GB=32",
    "STORAGE_TB=10",
]

OUTPUT_EXPECTED_LINE = "Resources: CPU=8 MEM=32GB STORAGE=10TB"


def test_env_file_exists():
    """Check that the dotenv file exists after task completion."""
    assert os.path.isfile(ENV_FILE), (
        f"The dotenv file '{ENV_FILE}' does not exist. "
        "Make sure you created it in /home/user with the correct filename."
    )


def test_env_file_content_exact():
    """Check that the dotenv file has exactly the correct content (no extra lines or spaces)."""
    with open(ENV_FILE, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    assert lines == ENV_EXPECTED_LINES, (
        f"The dotenv file '{ENV_FILE}' does not have the expected content.\n"
        f"Expected:\n" +
        "\n".join(ENV_EXPECTED_LINES) +
        "\n\nActual:\n" +
        "\n".join(lines) +
        "\n\n"
        "Check for missing/extraneous lines, extra whitespace, or trailing newlines."
    )


def test_env_file_no_trailing_newlines():
    """Check that the dotenv file does not have trailing blank lines."""
    with open(ENV_FILE, 'rb') as f:
        content = f.read()
    # Should not end with two newlines or newline+space
    assert not content.endswith(b'\n\n'), (
        f"The dotenv file '{ENV_FILE}' has extra blank lines at the end."
    )
    assert not content.endswith(b'\n '), (
        f"The dotenv file '{ENV_FILE}' has trailing whitespace after the last newline."
    )


def test_capacity_output_log_exists():
    """Check that the output log file exists after task completion."""
    assert os.path.isfile(OUTPUT_FILE), (
        f"The output log file '{OUTPUT_FILE}' does not exist. "
        "You must create this file in /home/user after running the shell command."
    )


def test_capacity_output_log_content_exact():
    """Check that the output log file has exactly the required output (no extra lines or spaces)."""
    with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    assert len(lines) == 1, (
        f"The output log file '{OUTPUT_FILE}' should contain exactly one line, "
        f"but it has {len(lines)} line(s).\n"
        f"Actual content:\n{repr(lines)}"
    )
    assert lines[0] == OUTPUT_EXPECTED_LINE, (
        f"The output log file '{OUTPUT_FILE}' does not contain the expected line.\n"
        f"Expected:\n{OUTPUT_EXPECTED_LINE}\n"
        f"Actual:\n{lines[0]}\n"
        "Check for typos, extra spaces, or incorrect variable substitution."
    )


def test_capacity_output_log_no_trailing_newlines():
    """Check that the output log file does not have trailing blank lines or extra newlines."""
    with open(OUTPUT_FILE, 'rb') as f:
        content = f.read()
    # Should end with the line only, or a single newline (depending on how written)
    # Accept either with or without a single trailing newline, but not more
    if content.endswith(b'\n'):
        assert not content.endswith(b'\n\n'), (
            f"The output log file '{OUTPUT_FILE}' has extra blank lines at the end."
        )
    else:
        # No newline at end is acceptable
        pass