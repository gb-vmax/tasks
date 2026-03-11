# test_final_state.py

import os
import tarfile
import pytest

DEPLOY_TAR_GZ = "/home/user/deploy.tar.gz"
ARCHIVE_CONTENTS_TXT = "/home/user/archive_contents.txt"
DEPLOYMENT_DIR = "/home/user/deployment"
WEBPROJECT_DIR = "/home/user/webproject"

EXPECTED_FILES = {"index.html", "style.css", "app.js"}
EXCLUDED_FILES = {"dev.config.json", "notes.txt"}


# ── 1. Archive existence and contents ────────────────────────────────────────

def test_deploy_tar_gz_exists():
    assert os.path.isfile(DEPLOY_TAR_GZ), (
        f"{DEPLOY_TAR_GZ} does not exist. "
        "The gzip-compressed tar archive must be created as part of the task."
    )


def test_deploy_tar_gz_is_valid_gzip_tar():
    assert tarfile.is_tarfile(DEPLOY_TAR_GZ), (
        f"{DEPLOY_TAR_GZ} exists but is not a valid tar archive."
    )
    try:
        with tarfile.open(DEPLOY_TAR_GZ, "r:gz") as tf:
            pass
    except tarfile.TarError as exc:
        pytest.fail(
            f"{DEPLOY_TAR_GZ} cannot be opened as a gzip-compressed tar: {exc}"
        )


def test_deploy_tar_gz_contains_exactly_expected_files():
    with tarfile.open(DEPLOY_TAR_GZ, "r:gz") as tf:
        members = [m.name for m in tf.getmembers() if not m.isdir()]
    member_set = set(members)
    missing = EXPECTED_FILES - member_set
    extra = member_set - EXPECTED_FILES
    assert not missing, (
        f"Archive is missing required files: {sorted(missing)}"
    )
    assert not extra, (
        f"Archive contains unexpected files: {sorted(extra)}"
    )


def test_deploy_tar_gz_has_no_absolute_or_prefixed_paths():
    """Files inside the archive must appear as bare names, not prefixed paths."""
    with tarfile.open(DEPLOY_TAR_GZ, "r:gz") as tf:
        members = [m.name for m in tf.getmembers() if not m.isdir()]
    for name in members:
        assert not name.startswith("/"), (
            f"Archive member '{name}' has an absolute path; expected bare filename."
        )
        assert not name.startswith("home/"), (
            f"Archive member '{name}' contains a path prefix; "
            "expected bare filename like 'index.html'."
        )


def test_deploy_tar_gz_excludes_dev_files():
    with tarfile.open(DEPLOY_TAR_GZ, "r:gz") as tf:
        members = {m.name for m in tf.getmembers()}
    for bad in EXCLUDED_FILES:
        assert bad not in members, (
            f"Archive must NOT contain '{bad}', but it does."
        )


# ── 2. archive_contents.txt ───────────────────────────────────────────────────

def test_archive_contents_txt_exists():
    assert os.path.isfile(ARCHIVE_CONTENTS_TXT), (
        f"{ARCHIVE_CONTENTS_TXT} does not exist. "
        "The archive listing must be saved to this file."
    )


def test_archive_contents_txt_has_exactly_three_lines():
    with open(ARCHIVE_CONTENTS_TXT, "r") as f:
        raw = f.read()
    lines = [l for l in raw.splitlines() if l.strip()]
    assert len(lines) == 3, (
        f"{ARCHIVE_CONTENTS_TXT} should contain exactly 3 non-empty lines, "
        f"but found {len(lines)}:\n{raw}"
    )


def test_archive_contents_txt_lists_correct_files():
    with open(ARCHIVE_CONTENTS_TXT, "r") as f:
        raw = f.read()
    lines = {l.strip() for l in raw.splitlines() if l.strip()}
    missing = EXPECTED_FILES - lines
    extra = lines - EXPECTED_FILES
    assert not missing, (
        f"{ARCHIVE_CONTENTS_TXT} is missing entries: {sorted(missing)}\n"
        f"File contents:\n{raw}"
    )
    assert not extra, (
        f"{ARCHIVE_CONTENTS_TXT} has unexpected entries: {sorted(extra)}\n"
        f"File contents:\n{raw}"
    )


def test_archive_contents_txt_excludes_dev_files():
    with open(ARCHIVE_CONTENTS_TXT, "r") as f:
        raw = f.read()
    lines = {l.strip() for l in raw.splitlines() if l.strip()}
    for bad in EXCLUDED_FILES:
        assert bad not in lines, (
            f"{ARCHIVE_CONTENTS_TXT} must NOT list '{bad}', but it does.\n"
            f"File contents:\n{raw}"
        )


# ── 3. Extracted deployment directory ─────────────────────────────────────────

def test_deployment_directory_exists():
    assert os.path.isdir(DEPLOYMENT_DIR), (
        f"Deployment directory {DEPLOYMENT_DIR} does not exist. "
        "The archive must be extracted into this directory."
    )


@pytest.mark.parametrize("filename", sorted(EXPECTED_FILES))
def test_deployment_file_exists(filename):
    path = os.path.join(DEPLOYMENT_DIR, filename)
    assert os.path.isfile(path), (
        f"{path} does not exist in the deployment directory."
    )


@pytest.mark.parametrize("filename", sorted(EXPECTED_FILES))
def test_deployment_file_matches_source(filename):
    source_path = os.path.join(WEBPROJECT_DIR, filename)
    deployed_path = os.path.join(DEPLOYMENT_DIR, filename)

    assert os.path.isfile(source_path), (
        f"Source file {source_path} does not exist (needed for comparison)."
    )
    assert os.path.isfile(deployed_path), (
        f"Deployed file {deployed_path} does not exist."
    )

    with open(source_path, "rb") as f:
        source_content = f.read()
    with open(deployed_path, "rb") as f:
        deployed_content = f.read()

    assert source_content == deployed_content, (
        f"Content of {deployed_path} does not match {source_path}.\n"
        f"Expected ({len(source_content)} bytes):\n{source_content!r}\n\n"
        f"Actual ({len(deployed_content)} bytes):\n{deployed_content!r}"
    )


@pytest.mark.parametrize("filename", sorted(EXCLUDED_FILES))
def test_deployment_excludes_dev_files(filename):
    path = os.path.join(DEPLOYMENT_DIR, filename)
    assert not os.path.exists(path), (
        f"{path} must NOT exist in the deployment directory, but it does."
    )