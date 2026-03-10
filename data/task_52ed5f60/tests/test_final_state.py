# test_final_state.py

import os
import pytest

MKDOCS_PATH = "/home/user/docs/mkdocs.yml"
SITE_TOML_PATH = "/home/user/docs/site.toml"


def read_file(path):
    assert os.path.isfile(path), f"File not found: {path}"
    with open(path, "r") as f:
        return f.read()


# ---------------------------------------------------------------------------
# mkdocs.yml — existence
# ---------------------------------------------------------------------------

def test_mkdocs_yml_exists():
    assert os.path.isfile(MKDOCS_PATH), (
        f"File not found: {MKDOCS_PATH}. The mkdocs configuration file must exist."
    )


# ---------------------------------------------------------------------------
# mkdocs.yml — updated fields
# ---------------------------------------------------------------------------

def test_mkdocs_yml_site_name_updated():
    content = read_file(MKDOCS_PATH)
    assert 'site_name: "Procyon Docs v2.1.0"' in content, (
        f"Expected 'site_name: \"Procyon Docs v2.1.0\"' in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_mkdocs_yml_site_description_updated():
    content = read_file(MKDOCS_PATH)
    assert 'site_description: "Official documentation for Procyon 2.1.0"' in content, (
        f"Expected 'site_description: \"Official documentation for Procyon 2.1.0\"' in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_mkdocs_yml_extra_version_updated():
    content = read_file(MKDOCS_PATH)
    assert '  version: "2.1.0"' in content, (
        f"Expected '  version: \"2.1.0\"' (indented, under extra) in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_mkdocs_yml_extra_release_stage_updated():
    content = read_file(MKDOCS_PATH)
    assert '  release_stage: "stable"' in content, (
        f"Expected '  release_stage: \"stable\"' (indented, under extra) in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )


# ---------------------------------------------------------------------------
# mkdocs.yml — old values must be gone
# ---------------------------------------------------------------------------

def test_mkdocs_yml_no_old_version():
    content = read_file(MKDOCS_PATH)
    assert "2.0.0" not in content, (
        f"Found old version string '2.0.0' in {MKDOCS_PATH}. It should have been replaced.\n"
        f"Current content:\n{content}"
    )


def test_mkdocs_yml_no_beta():
    content = read_file(MKDOCS_PATH)
    assert "beta" not in content, (
        f"Found old release_stage 'beta' in {MKDOCS_PATH}. It should have been replaced with 'stable'.\n"
        f"Current content:\n{content}"
    )


# ---------------------------------------------------------------------------
# mkdocs.yml — unchanged fields still present
# ---------------------------------------------------------------------------

def test_mkdocs_yml_site_url_unchanged():
    content = read_file(MKDOCS_PATH)
    assert 'site_url: "https://docs.procyon.io"' in content, (
        f"Expected 'site_url: \"https://docs.procyon.io\"' to remain unchanged in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_mkdocs_yml_repo_url_unchanged():
    content = read_file(MKDOCS_PATH)
    assert 'repo_url: "https://github.com/procyon/procyon"' in content, (
        f"Expected 'repo_url: \"https://github.com/procyon/procyon\"' to remain unchanged in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_mkdocs_yml_docs_dir_unchanged():
    content = read_file(MKDOCS_PATH)
    assert "docs_dir: docs" in content, (
        f"Expected 'docs_dir: docs' to remain unchanged in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_mkdocs_yml_theme_unchanged():
    content = read_file(MKDOCS_PATH)
    assert "theme:" in content, (
        f"Expected 'theme:' section to remain in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )
    assert "name: material" in content, (
        f"Expected 'name: material' to remain in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_mkdocs_yml_analytics_unchanged():
    content = read_file(MKDOCS_PATH)
    assert "analytics:" in content, (
        f"Expected 'analytics:' section to remain in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )
    assert "provider: google" in content, (
        f"Expected 'provider: google' to remain in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )
    assert "property: UA-000000-0" in content, (
        f"Expected 'property: UA-000000-0' to remain in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_mkdocs_yml_nav_unchanged():
    content = read_file(MKDOCS_PATH)
    assert "nav:" in content, (
        f"Expected 'nav:' section to remain in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )
    assert "index.md" in content, (
        f"Expected 'index.md' nav entry to remain in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )
    assert "getting-started.md" in content, (
        f"Expected 'getting-started.md' nav entry to remain in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )
    assert "api.md" in content, (
        f"Expected 'api.md' nav entry to remain in {MKDOCS_PATH}.\n"
        f"Current content:\n{content}"
    )


# ---------------------------------------------------------------------------
# site.toml — existence
# ---------------------------------------------------------------------------

def test_site_toml_exists():
    assert os.path.isfile(SITE_TOML_PATH), (
        f"File not found: {SITE_TOML_PATH}. The site metadata TOML file must exist."
    )


# ---------------------------------------------------------------------------
# site.toml — updated fields
# ---------------------------------------------------------------------------

def test_site_toml_version_updated():
    content = read_file(SITE_TOML_PATH)
    assert 'version = "2.1.0"' in content, (
        f"Expected 'version = \"2.1.0\"' in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_last_updated_updated():
    content = read_file(SITE_TOML_PATH)
    assert 'last_updated = "2024-11-15"' in content, (
        f"Expected 'last_updated = \"2024-11-15\"' in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_status_updated():
    content = read_file(SITE_TOML_PATH)
    assert 'status = "stable"' in content, (
        f"Expected 'status = \"stable\"' in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_output_dir_updated():
    content = read_file(SITE_TOML_PATH)
    assert 'output_dir = "dist/2.1.0"' in content, (
        f"Expected 'output_dir = \"dist/2.1.0\"' in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


# ---------------------------------------------------------------------------
# site.toml — old values must be gone
# ---------------------------------------------------------------------------

def test_site_toml_no_old_version():
    content = read_file(SITE_TOML_PATH)
    assert "2.0.0" not in content, (
        f"Found old version string '2.0.0' in {SITE_TOML_PATH}. It should have been replaced.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_no_beta():
    content = read_file(SITE_TOML_PATH)
    assert "beta" not in content, (
        f"Found old status 'beta' in {SITE_TOML_PATH}. It should have been replaced with 'stable'.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_no_old_last_updated():
    content = read_file(SITE_TOML_PATH)
    assert "2024-09-30" not in content, (
        f"Found old last_updated '2024-09-30' in {SITE_TOML_PATH}. It should have been replaced.\n"
        f"Current content:\n{content}"
    )


# ---------------------------------------------------------------------------
# site.toml — unchanged fields still present
# ---------------------------------------------------------------------------

def test_site_toml_title_unchanged():
    content = read_file(SITE_TOML_PATH)
    assert 'title = "Procyon Documentation"' in content, (
        f"Expected 'title = \"Procyon Documentation\"' to remain unchanged in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_author_unchanged():
    content = read_file(SITE_TOML_PATH)
    assert 'author = "Procyon Technical Writing Team"' in content, (
        f"Expected 'author = \"Procyon Technical Writing Team\"' to remain unchanged in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_minify_unchanged():
    content = read_file(SITE_TOML_PATH)
    assert "minify = true" in content, (
        f"Expected 'minify = true' to remain unchanged in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_search_index_unchanged():
    content = read_file(SITE_TOML_PATH)
    assert "search_index = true" in content, (
        f"Expected 'search_index = true' to remain unchanged in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_homepage_unchanged():
    content = read_file(SITE_TOML_PATH)
    assert 'homepage = "https://procyon.io"' in content, (
        f"Expected 'homepage = \"https://procyon.io\"' to remain unchanged in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_support_unchanged():
    content = read_file(SITE_TOML_PATH)
    assert 'support = "https://support.procyon.io"' in content, (
        f"Expected 'support = \"https://support.procyon.io\"' to remain unchanged in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_metadata_section_present():
    content = read_file(SITE_TOML_PATH)
    assert "[metadata]" in content, (
        f"Expected '[metadata]' section to remain in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_build_section_present():
    content = read_file(SITE_TOML_PATH)
    assert "[build]" in content, (
        f"Expected '[build]' section to remain in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )


def test_site_toml_links_section_present():
    content = read_file(SITE_TOML_PATH)
    assert "[links]" in content, (
        f"Expected '[links]' section to remain in {SITE_TOML_PATH}.\n"
        f"Current content:\n{content}"
    )