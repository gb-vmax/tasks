# test_final_state.py

import os
import pytest

AUDIT_FILE = "/home/user/pipeline/ci_audit.txt"
ENV_FILE = "/home/user/pipeline/.env"

EXPECTED_LINES = [
    "CI_API_TOKEN=****",
    "CI_ARTIFACT_PATH=/tmp/artifacts",
    "CI_BUILD_DIR=/workspace/build",
    "CI_DEPLOY_SECRET=****",
    "CI_PARALLEL_JOBS=8",
    "CI_REGISTRY_PASSWORD=****",
    "CI_REGISTRY_URL=registry.internal.example.com",
    "CI_RETRY_COUNT=3",
    "CI_TIMEOUT=120",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES) + "\n"


def test_audit_file_exists():
    assert os.path.isfile(AUDIT_FILE), (
        f"Audit file '{AUDIT_FILE}' does not exist. "
        "The task requires creating this file with the sanitized CI_ variable summary."
    )


def test_audit_file_is_readable():
    assert os.access(AUDIT_FILE, os.R_OK), (
        f"Audit file '{AUDIT_FILE}' exists but is not readable."
    )


def test_audit_file_exact_contents():
    with open(AUDIT_FILE, "r") as f:
        contents = f.read()
    assert contents == EXPECTED_CONTENT, (
        f"Audit file '{AUDIT_FILE}' does not have the expected exact contents.\n"
        f"Expected:\n{EXPECTED_CONTENT!r}\n"
        f"Got:\n{contents!r}"
    )


def test_audit_file_line_count():
    with open(AUDIT_FILE, "r") as f:
        contents = f.read()
    lines = contents.splitlines()
    assert len(lines) == 9, (
        f"Expected exactly 9 lines in '{AUDIT_FILE}', but found {len(lines)}.\n"
        f"Lines found: {lines}"
    )


def test_audit_file_ends_with_newline():
    with open(AUDIT_FILE, "rb") as f:
        contents = f.read()
    assert contents.endswith(b"\n"), (
        f"Audit file '{AUDIT_FILE}' must end with a newline character, but it does not.\n"
        f"Last 10 bytes: {contents[-10:]!r}"
    )


def test_audit_file_no_blank_lines():
    with open(AUDIT_FILE, "r") as f:
        contents = f.read()
    lines = contents.splitlines()
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"Audit file '{AUDIT_FILE}' must not contain blank lines, "
        f"but found blank lines at line numbers: {blank_lines}"
    )


def test_audit_file_no_comments():
    with open(AUDIT_FILE, "r") as f:
        lines = f.readlines()
    comment_lines = [line.rstrip() for line in lines if line.strip().startswith("#")]
    assert not comment_lines, (
        f"Audit file '{AUDIT_FILE}' must not contain comment lines, "
        f"but found: {comment_lines}"
    )


def test_audit_file_no_trailing_spaces():
    with open(AUDIT_FILE, "r") as f:
        lines = f.readlines()
    lines_with_trailing = [
        (i + 1, repr(line)) for i, line in enumerate(lines)
        if line.rstrip("\n") != line.rstrip("\n").rstrip()
    ]
    assert not lines_with_trailing, (
        f"Audit file '{AUDIT_FILE}' must not have trailing spaces, "
        f"but found them on lines: {lines_with_trailing}"
    )


def test_audit_file_only_ci_prefix_lines():
    with open(AUDIT_FILE, "r") as f:
        lines = f.readlines()
    non_ci_lines = [
        (i + 1, line.rstrip()) for i, line in enumerate(lines)
        if not line.strip().startswith("CI_")
    ]
    assert not non_ci_lines, (
        f"Audit file '{AUDIT_FILE}' must only contain lines starting with 'CI_', "
        f"but found non-CI_ lines: {non_ci_lines}"
    )


def test_audit_file_alphabetically_sorted():
    with open(AUDIT_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    sorted_lines = sorted(lines)
    assert lines == sorted_lines, (
        f"Audit file '{AUDIT_FILE}' lines are not sorted alphabetically by variable name.\n"
        f"Current order: {lines}\n"
        f"Expected order: {sorted_lines}"
    )


def test_audit_file_sensitive_vars_masked():
    with open(AUDIT_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    sensitive_keywords = ("SECRET", "TOKEN", "PASSWORD")
    for line in lines:
        if "=" not in line:
            continue
        var_name, value = line.split("=", 1)
        if any(kw in var_name.upper() for kw in sensitive_keywords):
            assert value == "****", (
                f"Variable '{var_name}' in '{AUDIT_FILE}' contains a sensitive keyword "
                f"(SECRET, TOKEN, or PASSWORD) and must have its value masked as '****', "
                f"but found value: {value!r}"
            )


def test_audit_file_non_sensitive_vars_not_masked():
    with open(AUDIT_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    sensitive_keywords = ("SECRET", "TOKEN", "PASSWORD")
    for line in lines:
        if "=" not in line:
            continue
        var_name, value = line.split("=", 1)
        if not any(kw in var_name.upper() for kw in sensitive_keywords):
            assert value != "****", (
                f"Variable '{var_name}' in '{AUDIT_FILE}' does not contain a sensitive keyword "
                f"and should NOT be masked, but its value is '****'."
            )


def test_audit_file_specific_masked_variables():
    with open(AUDIT_FILE, "r") as f:
        contents = f.read()
    lines = contents.splitlines()
    line_dict = {}
    for line in lines:
        if "=" in line:
            k, v = line.split("=", 1)
            line_dict[k] = v

    masked_vars = ["CI_API_TOKEN", "CI_DEPLOY_SECRET", "CI_REGISTRY_PASSWORD"]
    for var in masked_vars:
        assert var in line_dict, (
            f"Expected variable '{var}' to be present in '{AUDIT_FILE}', but it was not found."
        )
        assert line_dict[var] == "****", (
            f"Variable '{var}' in '{AUDIT_FILE}' should be masked as '****', "
            f"but found value: {line_dict[var]!r}"
        )


def test_audit_file_specific_non_masked_variables():
    with open(AUDIT_FILE, "r") as f:
        contents = f.read()
    lines = contents.splitlines()
    line_dict = {}
    for line in lines:
        if "=" in line:
            k, v = line.split("=", 1)
            line_dict[k] = v

    non_masked_expected = {
        "CI_ARTIFACT_PATH": "/tmp/artifacts",
        "CI_BUILD_DIR": "/workspace/build",
        "CI_PARALLEL_JOBS": "8",
        "CI_REGISTRY_URL": "registry.internal.example.com",
        "CI_RETRY_COUNT": "3",
        "CI_TIMEOUT": "120",
    }
    for var, expected_value in non_masked_expected.items():
        assert var in line_dict, (
            f"Expected variable '{var}' to be present in '{AUDIT_FILE}', but it was not found."
        )
        assert line_dict[var] == expected_value, (
            f"Variable '{var}' in '{AUDIT_FILE}' should have value {expected_value!r}, "
            f"but found: {line_dict[var]!r}"
        )


def test_audit_file_excludes_non_ci_variables():
    with open(AUDIT_FILE, "r") as f:
        contents = f.read()

    excluded_vars = ["APP_NAME", "APP_ENV", "DB_HOST", "DB_PASSWORD", "DB_PORT"]
    for var in excluded_vars:
        assert var not in contents, (
            f"Non-CI_ variable '{var}' should NOT appear in '{AUDIT_FILE}', "
            f"but it was found in the file contents."
        )


def test_audit_file_has_exactly_9_variables():
    with open(AUDIT_FILE, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    var_lines = [line for line in lines if "=" in line and line.startswith("CI_")]
    assert len(var_lines) == 9, (
        f"Expected exactly 9 CI_ variable entries in '{AUDIT_FILE}', "
        f"but found {len(var_lines)}.\nLines: {var_lines}"
    )


def test_env_file_unchanged():
    """Verify the original .env file has not been modified."""
    assert os.path.isfile(ENV_FILE), (
        f"Original .env file '{ENV_FILE}' no longer exists — it must not be deleted."
    )
    with open(ENV_FILE, "r") as f:
        contents = f.read()

    # Check original CI_ variables with their real (unmasked) values are still present
    original_ci_lines = [
        "CI_BUILD_DIR=/workspace/build",
        "CI_ARTIFACT_PATH=/tmp/artifacts",
        "CI_API_TOKEN=ghp_xK92mNpQr7sLvT3wYbZd",
        "CI_RETRY_COUNT=3",
        "CI_TIMEOUT=120",
        "CI_DEPLOY_SECRET=s3cr3t-deploy-key-xyz",
        "CI_REGISTRY_URL=registry.internal.example.com",
        "CI_REGISTRY_PASSWORD=hunter2abc",
        "CI_PARALLEL_JOBS=8",
    ]
    for line in original_ci_lines:
        assert line in contents, (
            f"Original .env file '{ENV_FILE}' appears to have been modified. "
            f"Expected line '{line}' not found.\nCurrent contents:\n{contents}"
        )