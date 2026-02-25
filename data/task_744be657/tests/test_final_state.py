# test_final_state.py

import os
import json
import pytest

DOCS_DIR = "/home/user/docs"
ARTICLES_JSON = os.path.join(DOCS_DIR, "articles.json")
ARTICLE_SUMMARIES_JSON = os.path.join(DOCS_DIR, "article_summaries.json")
VALIDATION_LOG = os.path.join(DOCS_DIR, "validation.log")

EXPECTED_ARTICLES = [
    {
        "id": 1,
        "title": "Getting Started with Linux",
        "author": "Alice Smith",
        "published": True,
    },
    {
        "id": 2,
        "title": "Understanding Shell Scripts",
        "author": "Bob Lee",
        "published": False,
    },
    {
        "id": 3,
        "title": "Mastering JSON Processing",
        "author": "Cara Zhu",
        "published": True,
    },
]

EXPECTED_SUMMARIES = [
    {"title": "Getting Started with Linux", "author": "Alice Smith"},
    {"title": "Understanding Shell Scripts", "author": "Bob Lee"},
    {"title": "Mastering JSON Processing", "author": "Cara Zhu"},
]

SCHEMA_VALID = "SCHEMA VALID"
INVALID_SCHEMA = "INVALID SCHEMA"


def test_docs_directory_still_exists():
    assert os.path.isdir(DOCS_DIR), f"Required directory {DOCS_DIR} does not exist."


def test_articles_json_untouched():
    assert os.path.isfile(ARTICLES_JSON), (
        f"Required file {ARTICLES_JSON} does not exist after task."
    )
    with open(ARTICLES_JSON, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            pytest.fail(f"{ARTICLES_JSON} is not valid JSON after task: {e}")

    assert isinstance(data, dict), f"{ARTICLES_JSON} should contain a JSON object at top level."
    assert "articles" in data, f"{ARTICLES_JSON} must contain a top-level 'articles' property."
    articles = data["articles"]
    assert isinstance(articles, list), "'articles' must be a list."
    assert articles == EXPECTED_ARTICLES, (
        f"The contents of {ARTICLES_JSON} have been altered. "
        f"Expected: {EXPECTED_ARTICLES!r} Got: {articles!r}"
    )


def test_validation_log_exists_and_content():
    assert os.path.isfile(VALIDATION_LOG), (
        f"{VALIDATION_LOG} does not exist after the task. "
        f"Validation log is required to indicate schema validation result."
    )
    with open(VALIDATION_LOG, "r", encoding="utf-8") as f:
        log_content = f.read().strip()

    if log_content == SCHEMA_VALID:
        # The schema was valid, so article_summaries.json must exist and be correct
        assert os.path.isfile(ARTICLE_SUMMARIES_JSON), (
            f"{ARTICLE_SUMMARIES_JSON} does not exist, but schema was valid. "
            "You must generate the summary file."
        )
        # Check summary file content
        with open(ARTICLE_SUMMARIES_JSON, "r", encoding="utf-8") as fsum:
            try:
                summaries = json.load(fsum)
            except Exception as e:
                pytest.fail(
                    f"{ARTICLE_SUMMARIES_JSON} is not valid JSON: {e}"
                )
        assert isinstance(summaries, list), (
            f"{ARTICLE_SUMMARIES_JSON} should contain a JSON array of summaries."
        )
        assert summaries == EXPECTED_SUMMARIES, (
            f"{ARTICLE_SUMMARIES_JSON} does not contain the required summaries.\n"
            f"Expected: {EXPECTED_SUMMARIES!r}\nGot: {summaries!r}"
        )
    elif log_content == INVALID_SCHEMA:
        # The schema was invalid, so summary file must not exist
        assert not os.path.exists(ARTICLE_SUMMARIES_JSON), (
            f"{ARTICLE_SUMMARIES_JSON} exists, but schema was invalid. "
            "You must not create a summary file if schema validation fails."
        )
    else:
        pytest.fail(
            f"{VALIDATION_LOG} contains unexpected content: {log_content!r}. "
            f"Expected either '{SCHEMA_VALID}' or '{INVALID_SCHEMA}'."
        )


def test_no_extra_files_created():
    """Ensure that only the specified output files exist in /home/user/docs/ after the task."""
    expected_files = {
        "articles.json",
        "validation.log",
        # Only present if schema valid:
        "article_summaries.json",
    }
    present_files = set(os.listdir(DOCS_DIR))
    if os.path.isfile(ARTICLE_SUMMARIES_JSON):
        assert expected_files <= present_files, (
            f"Unexpected files present in {DOCS_DIR}: {present_files - expected_files}"
        )
    else:
        expected_files.remove("article_summaries.json")
        assert expected_files <= present_files, (
            f"Unexpected files present in {DOCS_DIR}: {present_files - expected_files}"
        )
    # There should be no files other than the expected ones
    extra_files = present_files - expected_files
    assert not extra_files, (
        f"Extra files found in {DOCS_DIR}: {extra_files}. "
        "Only articles.json, validation.log, and (if schema valid) article_summaries.json should exist."
    )