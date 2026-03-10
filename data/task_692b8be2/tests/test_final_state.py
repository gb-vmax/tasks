# test_final_state.py

import os
import pytest

TEMPLATE_PATH = "/home/user/provisioning/server.conf.tmpl"
OUTPUT_PATH = "/home/user/provisioning/server.conf"
PROVISIONING_DIR = "/home/user/provisioning"

EXPECTED_TEMPLATE_CONTENT = """\
# Server Configuration
hostname = {{HOSTNAME}}
bind_address = {{IP_ADDRESS}}
environment = {{ENVIRONMENT}}

[connection]
max_connections = {{MAX_CONNECTIONS}}
timeout = {{TIMEOUT_SECONDS}}

[logging]
log_file = /var/log/{{HOSTNAME}}/app.log
log_level = info

[tags]
env = {{ENVIRONMENT}}
host = {{HOSTNAME}}"""

EXPECTED_OUTPUT_CONTENT = """\
# Server Configuration
hostname = prod-web-04
bind_address = 10.0.1.44
environment = production

[connection]
max_connections = 512
timeout = 30

[logging]
log_file = /var/log/prod-web-04/app.log
log_level = info

[tags]
env = production
host = prod-web-04"""

SUBSTITUTIONS = {
    "{{HOSTNAME}}": "prod-web-04",
    "{{IP_ADDRESS}}": "10.0.1.44",
    "{{MAX_CONNECTIONS}}": "512",
    "{{TIMEOUT_SECONDS}}": "30",
    "{{ENVIRONMENT}}": "production",
}


def test_output_file_exists():
    assert os.path.isfile(OUTPUT_PATH), (
        f"Output config file does not exist: {OUTPUT_PATH}\n"
        "The task requires generating the final server.conf from the template."
    )


def test_output_file_is_readable():
    assert os.access(OUTPUT_PATH, os.R_OK), (
        f"Output config file is not readable: {OUTPUT_PATH}"
    )


def test_output_file_exact_contents():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_OUTPUT_CONTENT, (
        f"Output file contents do not match expected.\n"
        f"Expected:\n{EXPECTED_OUTPUT_CONTENT}\n\n"
        f"Got:\n{content}"
    )


def test_output_file_no_remaining_placeholders():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    for placeholder in SUBSTITUTIONS.keys():
        assert placeholder not in content, (
            f"Output file still contains unsubstituted placeholder: {placeholder}\n"
            f"Output path: {OUTPUT_PATH}"
        )


def test_output_file_contains_substituted_values():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    for placeholder, value in SUBSTITUTIONS.items():
        assert value in content, (
            f"Output file is missing expected substituted value '{value}' "
            f"(was placeholder: {placeholder})\n"
            f"Output path: {OUTPUT_PATH}"
        )


def test_output_hostname_substituted():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    assert "hostname = prod-web-04" in content, (
        "Output file does not contain 'hostname = prod-web-04'.\n"
        f"Output path: {OUTPUT_PATH}"
    )


def test_output_ip_address_substituted():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    assert "bind_address = 10.0.1.44" in content, (
        "Output file does not contain 'bind_address = 10.0.1.44'.\n"
        f"Output path: {OUTPUT_PATH}"
    )


def test_output_max_connections_substituted():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    assert "max_connections = 512" in content, (
        "Output file does not contain 'max_connections = 512'.\n"
        f"Output path: {OUTPUT_PATH}"
    )


def test_output_timeout_substituted():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    assert "timeout = 30" in content, (
        "Output file does not contain 'timeout = 30'.\n"
        f"Output path: {OUTPUT_PATH}"
    )


def test_output_environment_substituted():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    assert "environment = production" in content, (
        "Output file does not contain 'environment = production'.\n"
        f"Output path: {OUTPUT_PATH}"
    )


def test_output_log_file_path_substituted():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    assert "log_file = /var/log/prod-web-04/app.log" in content, (
        "Output file does not contain 'log_file = /var/log/prod-web-04/app.log'.\n"
        "The {{HOSTNAME}} placeholder in the log_file path was not substituted.\n"
        f"Output path: {OUTPUT_PATH}"
    )


def test_output_tags_env_substituted():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    assert "env = production" in content, (
        "Output file does not contain 'env = production' in [tags] section.\n"
        f"Output path: {OUTPUT_PATH}"
    )


def test_output_tags_host_substituted():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    assert "host = prod-web-04" in content, (
        "Output file does not contain 'host = prod-web-04' in [tags] section.\n"
        f"Output path: {OUTPUT_PATH}"
    )


def test_template_file_still_exists():
    assert os.path.isfile(TEMPLATE_PATH), (
        f"Original template file no longer exists: {TEMPLATE_PATH}\n"
        "The task requires the template to remain unmodified."
    )


def test_template_file_unchanged():
    with open(TEMPLATE_PATH, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_TEMPLATE_CONTENT, (
        f"Original template file has been modified!\n"
        f"Expected (original):\n{EXPECTED_TEMPLATE_CONTENT}\n\n"
        f"Got:\n{content}\n\n"
        "The task requires the template to remain unmodified."
    )


def test_template_still_contains_all_placeholders():
    with open(TEMPLATE_PATH, "r") as f:
        content = f.read()
    for placeholder in SUBSTITUTIONS.keys():
        assert placeholder in content, (
            f"Original template file is missing placeholder: {placeholder}\n"
            f"Template path: {TEMPLATE_PATH}\n"
            "The template file must remain unmodified."
        )


def test_output_and_template_are_different_files():
    assert OUTPUT_PATH != TEMPLATE_PATH, (
        "Output path and template path are the same file — they must be different."
    )
    with open(OUTPUT_PATH, "r") as f:
        output_content = f.read()
    with open(TEMPLATE_PATH, "r") as f:
        template_content = f.read()
    assert output_content != template_content, (
        "Output file and template file have identical contents.\n"
        "The output file should have placeholders replaced with real values."
    )