# test_final_state.py

import os
import pytest

PIPELINE_YML = "/home/user/ci/pipeline.yml"
SUMMARY_TXT = "/home/user/ci/pipeline_summary.txt"
CI_DIR = "/home/user/ci"

EXPECTED_PIPELINE_CONTENT = """\
stages:
  - build
  - test
  - deploy

variables:
  REGISTRY: registry.example.com

build:
  stage: build
  image: docker:24.0
  timeout: 30 minutes
  script:
    - docker build -t $REGISTRY/app:$CI_COMMIT_SHA .
    - docker push $REGISTRY/app:$CI_COMMIT_SHA

unit_test:
  stage: test
  image: python:3.11
  timeout: 20 minutes
  script:
    - pip install -r requirements.txt
    - pytest tests/unit

integration_test:
  stage: test
  image: python:3.11
  timeout: 30 minutes
  script:
    - pip install -r requirements.txt
    - pytest tests/integration

deploy_staging:
  stage: deploy
  image: alpine:3.18
  timeout: 15 minutes
  script:
    - ./deploy.sh staging
"""

EXPECTED_SUMMARY_CONTENT = """\
Pipeline Summary
================
Stages: build, test, deploy
Jobs: build, unit_test, integration_test, deploy_staging
Build image: docker:24.0
Build timeout: 30 minutes
"""


# ── pipeline.yml checks ───────────────────────────────────────────────────────

def test_pipeline_yml_exists():
    assert os.path.isfile(PIPELINE_YML), (
        f"File '{PIPELINE_YML}' does not exist. "
        "The pipeline configuration file must be present after the task."
    )


def test_pipeline_yml_is_readable():
    assert os.access(PIPELINE_YML, os.R_OK), (
        f"File '{PIPELINE_YML}' is not readable."
    )


def test_pipeline_yml_exact_content():
    with open(PIPELINE_YML, "r") as f:
        content = f.read()
    assert content == EXPECTED_PIPELINE_CONTENT, (
        f"File '{PIPELINE_YML}' does not match the expected content.\n"
        f"Expected:\n{EXPECTED_PIPELINE_CONTENT!r}\n\n"
        f"Got:\n{content!r}"
    )


def test_pipeline_yml_updated_image():
    with open(PIPELINE_YML, "r") as f:
        content = f.read()
    assert "image: docker:24.0" in content, (
        f"File '{PIPELINE_YML}' should contain 'image: docker:24.0' "
        f"(the updated image). Actual content:\n{content}"
    )


def test_pipeline_yml_old_image_removed():
    with open(PIPELINE_YML, "r") as f:
        content = f.read()
    assert "docker:20.10" not in content, (
        f"File '{PIPELINE_YML}' still contains the old image 'docker:20.10'. "
        "It should have been replaced with 'docker:24.0'."
    )


def test_pipeline_yml_updated_timeout():
    with open(PIPELINE_YML, "r") as f:
        content = f.read()
    # The build job should now have 30 minutes; the old 10 minutes must be gone
    assert "timeout: 30 minutes" in content, (
        f"File '{PIPELINE_YML}' should contain 'timeout: 30 minutes' "
        f"for the build job. Actual content:\n{content}"
    )


def test_pipeline_yml_old_build_timeout_removed():
    with open(PIPELINE_YML, "r") as f:
        content = f.read()
    assert "timeout: 10 minutes" not in content, (
        f"File '{PIPELINE_YML}' still contains 'timeout: 10 minutes'. "
        "The build job timeout should have been updated to '30 minutes'."
    )


def test_pipeline_yml_other_jobs_unchanged():
    """Verify that the other jobs' images and timeouts were not altered."""
    with open(PIPELINE_YML, "r") as f:
        content = f.read()

    # unit_test and integration_test still use python:3.11
    assert content.count("image: python:3.11") == 2, (
        "Expected exactly 2 occurrences of 'image: python:3.11' "
        "(unit_test and integration_test). Something else was changed."
    )
    # deploy_staging still uses alpine:3.18
    assert "image: alpine:3.18" in content, (
        "Expected 'image: alpine:3.18' for the deploy_staging job. "
        "Something else was changed."
    )
    # unit_test timeout 20 minutes unchanged
    assert "timeout: 20 minutes" in content, (
        "Expected 'timeout: 20 minutes' for the unit_test job. "
        "Something else was changed."
    )
    # deploy_staging timeout 15 minutes unchanged
    assert "timeout: 15 minutes" in content, (
        "Expected 'timeout: 15 minutes' for the deploy_staging job. "
        "Something else was changed."
    )


def test_pipeline_yml_stages_block_unchanged():
    with open(PIPELINE_YML, "r") as f:
        content = f.read()
    for stage in ["  - build", "  - test", "  - deploy"]:
        assert stage in content, (
            f"Stage entry '{stage}' is missing from '{PIPELINE_YML}'. "
            "The stages block should not have been modified."
        )


def test_pipeline_yml_all_jobs_present():
    with open(PIPELINE_YML, "r") as f:
        content = f.read()
    for job in ["build:", "unit_test:", "integration_test:", "deploy_staging:"]:
        assert job in content, (
            f"Job definition '{job}' is missing from '{PIPELINE_YML}'."
        )


def test_pipeline_yml_ends_with_single_newline():
    with open(PIPELINE_YML, "rb") as f:
        raw = f.read()
    assert raw.endswith(b"\n"), (
        f"File '{PIPELINE_YML}' does not end with a newline character."
    )
    assert not raw.endswith(b"\n\n"), (
        f"File '{PIPELINE_YML}' ends with more than one newline character."
    )


# ── pipeline_summary.txt checks ───────────────────────────────────────────────

def test_summary_file_exists():
    assert os.path.isfile(SUMMARY_TXT), (
        f"Summary file '{SUMMARY_TXT}' does not exist. "
        "It should have been created as part of the task."
    )


def test_summary_file_is_readable():
    assert os.access(SUMMARY_TXT, os.R_OK), (
        f"Summary file '{SUMMARY_TXT}' is not readable."
    )


def test_summary_file_exact_content():
    with open(SUMMARY_TXT, "r") as f:
        content = f.read()
    assert content == EXPECTED_SUMMARY_CONTENT, (
        f"File '{SUMMARY_TXT}' does not match the expected content.\n"
        f"Expected:\n{EXPECTED_SUMMARY_CONTENT!r}\n\n"
        f"Got:\n{content!r}"
    )


def test_summary_header_line():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 1 and lines[0].rstrip("\n") == "Pipeline Summary", (
        f"First line of '{SUMMARY_TXT}' should be 'Pipeline Summary'. "
        f"Got: {lines[0]!r}"
    )


def test_summary_separator_line():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 2 and lines[1].rstrip("\n") == "================", (
        f"Second line of '{SUMMARY_TXT}' should be '================'. "
        f"Got: {lines[1]!r}"
    )


def test_summary_stages_line():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    stages_line = next(
        (l.rstrip("\n") for l in lines if l.startswith("Stages:")), None
    )
    assert stages_line is not None, (
        f"No 'Stages:' line found in '{SUMMARY_TXT}'."
    )
    assert stages_line == "Stages: build, test, deploy", (
        f"'Stages:' line is incorrect.\n"
        f"Expected: 'Stages: build, test, deploy'\n"
        f"Got:      {stages_line!r}"
    )


def test_summary_jobs_line():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    jobs_line = next(
        (l.rstrip("\n") for l in lines if l.startswith("Jobs:")), None
    )
    assert jobs_line is not None, (
        f"No 'Jobs:' line found in '{SUMMARY_TXT}'."
    )
    assert jobs_line == "Jobs: build, unit_test, integration_test, deploy_staging", (
        f"'Jobs:' line is incorrect.\n"
        f"Expected: 'Jobs: build, unit_test, integration_test, deploy_staging'\n"
        f"Got:      {jobs_line!r}"
    )


def test_summary_build_image_line():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    image_line = next(
        (l.rstrip("\n") for l in lines if l.startswith("Build image:")), None
    )
    assert image_line is not None, (
        f"No 'Build image:' line found in '{SUMMARY_TXT}'."
    )
    assert image_line == "Build image: docker:24.0", (
        f"'Build image:' line is incorrect.\n"
        f"Expected: 'Build image: docker:24.0'\n"
        f"Got:      {image_line!r}"
    )


def test_summary_build_timeout_line():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    timeout_line = next(
        (l.rstrip("\n") for l in lines if l.startswith("Build timeout:")), None
    )
    assert timeout_line is not None, (
        f"No 'Build timeout:' line found in '{SUMMARY_TXT}'."
    )
    assert timeout_line == "Build timeout: 30 minutes", (
        f"'Build timeout:' line is incorrect.\n"
        f"Expected: 'Build timeout: 30 minutes'\n"
        f"Got:      {timeout_line!r}"
    )


def test_summary_no_trailing_spaces():
    with open(SUMMARY_TXT, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} of '{SUMMARY_TXT}' has trailing whitespace: {line!r}"
        )


def test_summary_ends_with_single_newline():
    with open(SUMMARY_TXT, "rb") as f:
        raw = f.read()
    assert raw.endswith(b"\n"), (
        f"File '{SUMMARY_TXT}' does not end with a newline character."
    )
    assert not raw.endswith(b"\n\n"), (
        f"File '{SUMMARY_TXT}' ends with more than one newline character."
    )


def test_summary_line_count():
    with open(SUMMARY_TXT, "r") as f:
        content = f.read()
    # 6 non-empty lines + trailing newline → split gives 7 items, last is ''
    lines = content.split("\n")
    # Last element after split on trailing newline should be empty string
    assert lines[-1] == "", (
        f"File '{SUMMARY_TXT}' does not end with exactly one newline. "
        f"Split result tail: {lines[-3:]!r}"
    )
    non_empty = [l for l in lines if l != ""]
    assert len(non_empty) == 6, (
        f"Expected 6 non-empty lines in '{SUMMARY_TXT}', got {len(non_empty)}.\n"
        f"Lines: {non_empty!r}"
    )