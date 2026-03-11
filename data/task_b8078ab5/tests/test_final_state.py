# test_final_state.py

import os
import pytest

BASHRC_PATH = "/home/user/.bashrc"
ENV_CHECK_PATH = "/home/user/env_check.txt"

APPENDED_BLOCK = (
    "# App deployment config\n"
    "export APP_ENV=production\n"
    "export APP_PORT=8443\n"
    "export APP_LOG_LEVEL=warn\n"
    "export APP_MAX_WORKERS=8\n"
    "export APP_DATA_DIR=/var/app/data\n"
)

EXPECTED_BASHRC_FULL = (
    "# .bashrc\n"
    "\n"
    "# Source global definitions\n"
    "if [ -f /etc/bashrc ]; then\n"
    "    . /etc/bashrc\n"
    "fi\n"
    "\n"
    "# User specific aliases and functions\n"
    "alias ll='ls -la'\n"
    "alias grep='grep --color=auto'\n"
    "\n"
    "PATH=$PATH:$HOME/.local/bin:$HOME/bin\n"
    "export PATH\n"
    "# App deployment config\n"
    "export APP_ENV=production\n"
    "export APP_PORT=8443\n"
    "export APP_LOG_LEVEL=warn\n"
    "export APP_MAX_WORKERS=8\n"
    "export APP_DATA_DIR=/var/app/data\n"
)

EXPECTED_ENV_CHECK_CONTENT = (
    "APP_DATA_DIR=/var/app/data\n"
    "APP_ENV=production\n"
    "APP_LOG_LEVEL=warn\n"
    "APP_MAX_WORKERS=8\n"
    "APP_PORT=8443\n"
)


# ── .bashrc tests ────────────────────────────────────────────────────────────

def test_bashrc_exists():
    assert os.path.isfile(BASHRC_PATH), (
        f"{BASHRC_PATH} does not exist. The .bashrc file must be present."
    )


def test_bashrc_contains_appended_block():
    with open(BASHRC_PATH, "r") as f:
        content = f.read()

    assert "# App deployment config" in content, (
        f"{BASHRC_PATH} is missing the '# App deployment config' comment line.\n"
        f"The appended block was not found."
    )
    for var in ["APP_ENV=production", "APP_PORT=8443", "APP_LOG_LEVEL=warn",
                "APP_MAX_WORKERS=8", "APP_DATA_DIR=/var/app/data"]:
        assert var in content, (
            f"{BASHRC_PATH} is missing the export line containing '{var}'."
        )


def test_bashrc_appended_block_order_and_format():
    """The appended block must appear at the end of .bashrc in the exact order specified."""
    with open(BASHRC_PATH, "r") as f:
        content = f.read()

    assert content.endswith(APPENDED_BLOCK), (
        f"{BASHRC_PATH} does not end with the expected appended block.\n\n"
        f"Expected ending:\n{repr(APPENDED_BLOCK)}\n\n"
        f"Actual ending (last {len(APPENDED_BLOCK) + 20} chars):\n"
        f"{repr(content[-len(APPENDED_BLOCK) - 20:])}"
    )


def test_bashrc_full_content():
    """The full .bashrc content must exactly match the expected content."""
    with open(BASHRC_PATH, "r") as f:
        content = f.read()

    assert content == EXPECTED_BASHRC_FULL, (
        f"{BASHRC_PATH} full content does not match the expected content.\n\n"
        f"Expected:\n{repr(EXPECTED_BASHRC_FULL)}\n\n"
        f"Got:\n{repr(content)}"
    )


def test_bashrc_last_seven_lines():
    """The last 7 lines of .bashrc must be exactly the appended block (6 lines) preceded by
    'export PATH', i.e. the block lines themselves."""
    with open(BASHRC_PATH, "r") as f:
        lines = f.readlines()

    # The appended block is 6 lines; check the last 6
    last_six = lines[-6:]
    expected_lines = APPENDED_BLOCK.splitlines(keepends=True)

    assert last_six == expected_lines, (
        f"The last 6 lines of {BASHRC_PATH} do not match the expected appended block.\n\n"
        f"Expected:\n{''.join(expected_lines)!r}\n\n"
        f"Got:\n{''.join(last_six)!r}"
    )


def test_bashrc_no_extra_blank_lines_in_block():
    """There must be no blank lines within the appended block."""
    with open(BASHRC_PATH, "r") as f:
        content = f.read()

    # Find the start of the appended block
    block_start = content.find("# App deployment config")
    assert block_start != -1, (
        f"Could not find '# App deployment config' in {BASHRC_PATH}."
    )

    block_section = content[block_start:]
    # The block section from the comment to the end should equal APPENDED_BLOCK exactly
    assert block_section == APPENDED_BLOCK, (
        f"The appended block in {BASHRC_PATH} contains unexpected content (e.g., extra blank lines).\n\n"
        f"Expected block section:\n{repr(APPENDED_BLOCK)}\n\n"
        f"Got block section:\n{repr(block_section)}"
    )


def test_bashrc_no_trailing_blank_line_after_last_export():
    """There must be no trailing blank line after the last export line."""
    with open(BASHRC_PATH, "r") as f:
        content = f.read()

    assert not content.endswith("\n\n"), (
        f"{BASHRC_PATH} ends with a blank line. "
        "There must be no trailing blank line after the last export statement."
    )

    assert content.endswith("export APP_DATA_DIR=/var/app/data\n"), (
        f"{BASHRC_PATH} does not end with 'export APP_DATA_DIR=/var/app/data\\n'.\n"
        f"Actual ending: {repr(content[-50:])}"
    )


# ── env_check.txt tests ──────────────────────────────────────────────────────

def test_env_check_txt_exists():
    assert os.path.isfile(ENV_CHECK_PATH), (
        f"{ENV_CHECK_PATH} does not exist. "
        "It must be created by running: env | grep '^APP_' | sort > /home/user/env_check.txt"
    )


def test_env_check_txt_exact_content():
    with open(ENV_CHECK_PATH, "r") as f:
        content = f.read()

    assert content == EXPECTED_ENV_CHECK_CONTENT, (
        f"{ENV_CHECK_PATH} does not contain the expected content.\n\n"
        f"Expected:\n{repr(EXPECTED_ENV_CHECK_CONTENT)}\n\n"
        f"Got:\n{repr(content)}"
    )


def test_env_check_txt_has_exactly_five_lines():
    with open(ENV_CHECK_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines()
    assert len(lines) == 5, (
        f"{ENV_CHECK_PATH} must contain exactly 5 lines, but found {len(lines)}.\n"
        f"Lines found:\n{lines}"
    )


def test_env_check_txt_lines_in_alphabetical_order():
    with open(ENV_CHECK_PATH, "r") as f:
        lines = f.read().splitlines()

    expected_lines = [
        "APP_DATA_DIR=/var/app/data",
        "APP_ENV=production",
        "APP_LOG_LEVEL=warn",
        "APP_MAX_WORKERS=8",
        "APP_PORT=8443",
    ]

    assert lines == expected_lines, (
        f"{ENV_CHECK_PATH} lines are not in the expected alphabetical order.\n\n"
        f"Expected lines:\n{expected_lines}\n\n"
        f"Got lines:\n{lines}"
    )


def test_env_check_txt_no_extra_whitespace():
    with open(ENV_CHECK_PATH, "r") as f:
        content = f.read()

    # Must end with exactly one newline (after the last line)
    assert content.endswith("\n") and not content.endswith("\n\n"), (
        f"{ENV_CHECK_PATH} must end with exactly one newline character (no trailing blank lines).\n"
        f"Actual ending: {repr(content[-10:])}"
    )

    lines = content.splitlines()
    for line in lines:
        assert line == line.strip(), (
            f"{ENV_CHECK_PATH} contains a line with leading/trailing whitespace: {repr(line)}"
        )


def test_env_check_txt_no_blank_lines():
    with open(ENV_CHECK_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines()
    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"{ENV_CHECK_PATH} contains a blank line at line {i}."
        )


def test_env_check_txt_correct_values():
    with open(ENV_CHECK_PATH, "r") as f:
        content = f.read()

    expected_pairs = {
        "APP_DATA_DIR": "/var/app/data",
        "APP_ENV": "production",
        "APP_LOG_LEVEL": "warn",
        "APP_MAX_WORKERS": "8",
        "APP_PORT": "8443",
    }

    for line in content.splitlines():
        assert "=" in line, (
            f"{ENV_CHECK_PATH} contains a line without '=': {repr(line)}"
        )
        key, _, value = line.partition("=")
        assert key in expected_pairs, (
            f"{ENV_CHECK_PATH} contains an unexpected variable: {repr(key)}"
        )
        assert value == expected_pairs[key], (
            f"{ENV_CHECK_PATH}: variable {key} has wrong value.\n"
            f"Expected: {repr(expected_pairs[key])}\n"
            f"Got: {repr(value)}"
        )