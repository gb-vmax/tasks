# test_final_state.py

import os
import pytest

BUILD_TOML_PATH = "/home/user/build/build.toml"
ARTIFACTS_YAML_PATH = "/home/user/build/artifacts.yaml"

EXPECTED_BUILD_TOML = """\
[package]
name = "myapp"
version = "2.4.1"
authors = ["build-team@example.com"]

[release]
channel = "stable"
checksum_required = true
target = "linux-x86_64"\
"""

EXPECTED_ARTIFACTS_YAML = """\
version: "2.4.1"
metadata:
  environment: "production"
  owner: "build-team"
artifacts:
  - name: myapp-binary
    path: dist/myapp-2.4.1-linux-x86_64
    type: executable
  - name: myapp-config
    path: dist/myapp-config.tar.gz
    type: archive\
"""


# --- Directory and file existence ---

def test_build_dir_exists():
    build_dir = "/home/user/build"
    assert os.path.isdir(build_dir), (
        f"Expected directory '{build_dir}' to exist, but it does not."
    )


def test_build_toml_exists():
    assert os.path.isfile(BUILD_TOML_PATH), (
        f"Expected file '{BUILD_TOML_PATH}' to exist, but it does not."
    )


def test_artifacts_yaml_exists():
    assert os.path.isfile(ARTIFACTS_YAML_PATH), (
        f"Expected file '{ARTIFACTS_YAML_PATH}' to exist, but it does not."
    )


# --- Exact content checks ---

def test_build_toml_exact_contents():
    with open(BUILD_TOML_PATH, "r") as f:
        contents = f.read().rstrip("\n")
    assert contents == EXPECTED_BUILD_TOML, (
        f"File '{BUILD_TOML_PATH}' does not match the expected final contents.\n"
        f"Expected:\n{EXPECTED_BUILD_TOML}\n\n"
        f"Actual:\n{contents}"
    )


def test_artifacts_yaml_exact_contents():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read().rstrip("\n")
    assert contents == EXPECTED_ARTIFACTS_YAML, (
        f"File '{ARTIFACTS_YAML_PATH}' does not match the expected final contents.\n"
        f"Expected:\n{EXPECTED_ARTIFACTS_YAML}\n\n"
        f"Actual:\n{contents}"
    )


# --- Individual field checks for build.toml ---

def test_build_toml_version_updated():
    with open(BUILD_TOML_PATH, "r") as f:
        contents = f.read()
    assert 'version = "2.4.1"' in contents, (
        f"Expected '{BUILD_TOML_PATH}' to contain 'version = \"2.4.1\"', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_build_toml_old_version_absent():
    with open(BUILD_TOML_PATH, "r") as f:
        contents = f.read()
    assert 'version = "2.3.9"' not in contents, (
        f"Expected '{BUILD_TOML_PATH}' to NOT contain old version '2.3.9', "
        f"but it was still found. Actual contents:\n{contents}"
    )


def test_build_toml_channel_is_stable():
    with open(BUILD_TOML_PATH, "r") as f:
        contents = f.read()
    assert 'channel = "stable"' in contents, (
        f"Expected '{BUILD_TOML_PATH}' to contain 'channel = \"stable\"', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_build_toml_channel_not_beta():
    with open(BUILD_TOML_PATH, "r") as f:
        contents = f.read()
    assert 'channel = "beta"' not in contents, (
        f"Expected '{BUILD_TOML_PATH}' to NOT contain 'channel = \"beta\"', "
        f"but it was still found. Actual contents:\n{contents}"
    )


def test_build_toml_checksum_required_present():
    with open(BUILD_TOML_PATH, "r") as f:
        contents = f.read()
    assert "checksum_required = true" in contents, (
        f"Expected '{BUILD_TOML_PATH}' to contain 'checksum_required = true', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_build_toml_package_name_preserved():
    with open(BUILD_TOML_PATH, "r") as f:
        contents = f.read()
    assert 'name = "myapp"' in contents, (
        f"Expected '{BUILD_TOML_PATH}' to contain 'name = \"myapp\"', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_build_toml_authors_preserved():
    with open(BUILD_TOML_PATH, "r") as f:
        contents = f.read()
    assert 'authors = ["build-team@example.com"]' in contents, (
        f"Expected '{BUILD_TOML_PATH}' to contain 'authors = [\"build-team@example.com\"]', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_build_toml_target_preserved():
    with open(BUILD_TOML_PATH, "r") as f:
        contents = f.read()
    assert 'target = "linux-x86_64"' in contents, (
        f"Expected '{BUILD_TOML_PATH}' to contain 'target = \"linux-x86_64\"', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_build_toml_package_section_present():
    with open(BUILD_TOML_PATH, "r") as f:
        contents = f.read()
    assert "[package]" in contents, (
        f"Expected '{BUILD_TOML_PATH}' to contain '[package]' section header, "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_build_toml_release_section_present():
    with open(BUILD_TOML_PATH, "r") as f:
        contents = f.read()
    assert "[release]" in contents, (
        f"Expected '{BUILD_TOML_PATH}' to contain '[release]' section header, "
        f"but it was not found. Actual contents:\n{contents}"
    )


# --- Individual field checks for artifacts.yaml ---

def test_artifacts_yaml_version_updated():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert 'version: "2.4.1"' in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to contain 'version: \"2.4.1\"', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_artifacts_yaml_old_version_absent():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert 'version: "2.3.9"' not in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to NOT contain old version '2.3.9', "
        f"but it was still found. Actual contents:\n{contents}"
    )


def test_artifacts_yaml_environment_is_production():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert 'environment: "production"' in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to contain 'environment: \"production\"', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_artifacts_yaml_environment_not_staging():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert 'environment: "staging"' not in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to NOT contain 'environment: \"staging\"', "
        f"but it was still found. Actual contents:\n{contents}"
    )


def test_artifacts_yaml_binary_path_updated():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert "path: dist/myapp-2.4.1-linux-x86_64" in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to contain "
        f"'path: dist/myapp-2.4.1-linux-x86_64', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_artifacts_yaml_old_binary_path_absent():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert "path: dist/myapp-2.3.9-linux-x86_64" not in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to NOT contain old binary path "
        f"'dist/myapp-2.3.9-linux-x86_64', but it was still found. "
        f"Actual contents:\n{contents}"
    )


def test_artifacts_yaml_owner_preserved():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert 'owner: "build-team"' in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to contain 'owner: \"build-team\"', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_artifacts_yaml_config_artifact_preserved():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert "path: dist/myapp-config.tar.gz" in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to contain 'path: dist/myapp-config.tar.gz', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_artifacts_yaml_myapp_binary_name_present():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert "name: myapp-binary" in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to contain 'name: myapp-binary', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_artifacts_yaml_myapp_config_name_present():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert "name: myapp-config" in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to contain 'name: myapp-config', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_artifacts_yaml_executable_type_present():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert "type: executable" in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to contain 'type: executable', "
        f"but it was not found. Actual contents:\n{contents}"
    )


def test_artifacts_yaml_archive_type_present():
    with open(ARTIFACTS_YAML_PATH, "r") as f:
        contents = f.read()
    assert "type: archive" in contents, (
        f"Expected '{ARTIFACTS_YAML_PATH}' to contain 'type: archive', "
        f"but it was not found. Actual contents:\n{contents}"
    )