# test_final_state.py

import os
import pytest

TOML_PATH = "/home/user/docs/site_config.toml"
YAML_PATH = "/home/user/docs/metadata.yaml"

EXPECTED_TOML_CONTENT = """\
[site]
title = "My Docs"
base_url = "https://docs.example.com"

[release]
version = "2.4.0"
status = "stable"
draft = false

[theme]
name = "default"
highlight = true"""

EXPECTED_YAML_CONTENT = """\
title: "Documentation Portal"
author: "Tech Writing Team"
publication:
  version: "2.4.0"
  stage: "stable"
  last_updated: "2024-06-01"
language: "en\""""


# --- File existence tests ---

def test_docs_directory_exists():
    docs_dir = "/home/user/docs"
    assert os.path.isdir(docs_dir), (
        f"Directory '{docs_dir}' does not exist. "
        "The /home/user/docs directory must be present after the task."
    )


def test_site_config_toml_exists():
    assert os.path.isfile(TOML_PATH), (
        f"File '{TOML_PATH}' does not exist. "
        "The site_config.toml file must remain at its original path after the task."
    )


def test_metadata_yaml_exists():
    assert os.path.isfile(YAML_PATH), (
        f"File '{YAML_PATH}' does not exist. "
        "The metadata.yaml file must remain at its original path after the task."
    )


# --- Full content tests ---

def test_site_config_toml_full_content():
    with open(TOML_PATH, "r") as f:
        content = f.read().rstrip("\n")

    assert content == EXPECTED_TOML_CONTENT, (
        f"File '{TOML_PATH}' does not match the expected final content.\n"
        f"Expected:\n{EXPECTED_TOML_CONTENT}\n\n"
        f"Got:\n{content}"
    )


def test_metadata_yaml_full_content():
    with open(YAML_PATH, "r") as f:
        content = f.read().rstrip("\n")

    assert content == EXPECTED_YAML_CONTENT, (
        f"File '{YAML_PATH}' does not match the expected final content.\n"
        f"Expected:\n{EXPECTED_YAML_CONTENT}\n\n"
        f"Got:\n{content}"
    )


# --- Targeted field tests for site_config.toml ---

def test_site_config_toml_version_updated():
    with open(TOML_PATH, "r") as f:
        content = f.read()

    assert 'version = "2.4.0"' in content, (
        f"Expected 'version = \"2.4.0\"' in '{TOML_PATH}', but it was not found.\n"
        f"Current content:\n{content}"
    )


def test_site_config_toml_status_updated():
    with open(TOML_PATH, "r") as f:
        content = f.read()

    assert 'status = "stable"' in content, (
        f"Expected 'status = \"stable\"' in '{TOML_PATH}', but it was not found.\n"
        f"Current content:\n{content}"
    )


def test_site_config_toml_draft_updated():
    with open(TOML_PATH, "r") as f:
        content = f.read()

    assert "draft = false" in content, (
        f"Expected 'draft = false' in '{TOML_PATH}', but it was not found.\n"
        f"Current content:\n{content}"
    )


def test_site_config_toml_old_version_gone():
    with open(TOML_PATH, "r") as f:
        content = f.read()

    assert 'version = "2.3.1"' not in content, (
        f"Old value 'version = \"2.3.1\"' still present in '{TOML_PATH}'. "
        "It should have been replaced with '2.4.0'.\n"
        f"Current content:\n{content}"
    )


def test_site_config_toml_old_status_gone():
    with open(TOML_PATH, "r") as f:
        content = f.read()

    assert 'status = "beta"' not in content, (
        f"Old value 'status = \"beta\"' still present in '{TOML_PATH}'. "
        "It should have been replaced with 'stable'.\n"
        f"Current content:\n{content}"
    )


def test_site_config_toml_draft_true_gone():
    with open(TOML_PATH, "r") as f:
        content = f.read()

    assert "draft = true" not in content, (
        f"Old value 'draft = true' still present in '{TOML_PATH}'. "
        "It should have been replaced with 'false'.\n"
        f"Current content:\n{content}"
    )


# --- Targeted field tests for metadata.yaml ---

def test_metadata_yaml_version_updated():
    with open(YAML_PATH, "r") as f:
        content = f.read()

    assert 'version: "2.4.0"' in content, (
        f"Expected 'version: \"2.4.0\"' in '{YAML_PATH}', but it was not found.\n"
        f"Current content:\n{content}"
    )


def test_metadata_yaml_stage_updated():
    with open(YAML_PATH, "r") as f:
        content = f.read()

    assert 'stage: "stable"' in content, (
        f"Expected 'stage: \"stable\"' in '{YAML_PATH}', but it was not found.\n"
        f"Current content:\n{content}"
    )


def test_metadata_yaml_last_updated_updated():
    with open(YAML_PATH, "r") as f:
        content = f.read()

    assert 'last_updated: "2024-06-01"' in content, (
        f"Expected 'last_updated: \"2024-06-01\"' in '{YAML_PATH}', but it was not found.\n"
        f"Current content:\n{content}"
    )


def test_metadata_yaml_old_version_gone():
    with open(YAML_PATH, "r") as f:
        content = f.read()

    assert 'version: "2.3.1"' not in content, (
        f"Old value 'version: \"2.3.1\"' still present in '{YAML_PATH}'. "
        "It should have been replaced with '2.4.0'.\n"
        f"Current content:\n{content}"
    )


def test_metadata_yaml_old_stage_gone():
    with open(YAML_PATH, "r") as f:
        content = f.read()

    assert 'stage: "beta"' not in content, (
        f"Old value 'stage: \"beta\"' still present in '{YAML_PATH}'. "
        "It should have been replaced with 'stable'.\n"
        f"Current content:\n{content}"
    )


def test_metadata_yaml_old_last_updated_gone():
    with open(YAML_PATH, "r") as f:
        content = f.read()

    assert 'last_updated: "2024-03-15"' not in content, (
        f"Old value 'last_updated: \"2024-03-15\"' still present in '{YAML_PATH}'. "
        "It should have been replaced with '2024-06-01'.\n"
        f"Current content:\n{content}"
    )


# --- Unchanged fields tests for site_config.toml ---

def test_site_config_toml_site_section_unchanged():
    with open(TOML_PATH, "r") as f:
        content = f.read()

    assert '[site]' in content, (
        f"Section '[site]' is missing from '{TOML_PATH}'.\n"
        f"Current content:\n{content}"
    )
    assert 'title = "My Docs"' in content, (
        f"Field 'title = \"My Docs\"' is missing from '{TOML_PATH}'.\n"
        f"Current content:\n{content}"
    )
    assert 'base_url = "https://docs.example.com"' in content, (
        f"Field 'base_url = \"https://docs.example.com\"' is missing from '{TOML_PATH}'.\n"
        f"Current content:\n{content}"
    )


def test_site_config_toml_theme_section_unchanged():
    with open(TOML_PATH, "r") as f:
        content = f.read()

    assert '[theme]' in content, (
        f"Section '[theme]' is missing from '{TOML_PATH}'.\n"
        f"Current content:\n{content}"
    )
    assert 'name = "default"' in content, (
        f"Field 'name = \"default\"' is missing from '{TOML_PATH}'.\n"
        f"Current content:\n{content}"
    )
    assert 'highlight = true' in content, (
        f"Field 'highlight = true' is missing from '{TOML_PATH}'.\n"
        f"Current content:\n{content}"
    )


def test_site_config_toml_release_section_present():
    with open(TOML_PATH, "r") as f:
        content = f.read()

    assert '[release]' in content, (
        f"Section '[release]' is missing from '{TOML_PATH}'.\n"
        f"Current content:\n{content}"
    )


# --- Unchanged fields tests for metadata.yaml ---

def test_metadata_yaml_title_unchanged():
    with open(YAML_PATH, "r") as f:
        content = f.read()

    assert 'title: "Documentation Portal"' in content, (
        f"Field 'title: \"Documentation Portal\"' is missing from '{YAML_PATH}'.\n"
        f"Current content:\n{content}"
    )


def test_metadata_yaml_author_unchanged():
    with open(YAML_PATH, "r") as f:
        content = f.read()

    assert 'author: "Tech Writing Team"' in content, (
        f"Field 'author: \"Tech Writing Team\"' is missing from '{YAML_PATH}'.\n"
        f"Current content:\n{content}"
    )


def test_metadata_yaml_language_unchanged():
    with open(YAML_PATH, "r") as f:
        content = f.read()

    assert 'language: "en"' in content, (
        f"Field 'language: \"en\"' is missing from '{YAML_PATH}'.\n"
        f"Current content:\n{content}"
    )


def test_metadata_yaml_publication_key_present():
    with open(YAML_PATH, "r") as f:
        content = f.read()

    assert 'publication:' in content, (
        f"Key 'publication:' is missing from '{YAML_PATH}'.\n"
        f"Current content:\n{content}"
    )