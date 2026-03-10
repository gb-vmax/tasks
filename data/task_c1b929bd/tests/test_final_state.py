# test_final_state.py

import gzip
import io
import os
import tarfile
import pytest

ARCHIVE_PATH = "/home/user/backups/manifests_backup.tar.gz"
TXT_PATH = "/home/user/backups/manifests_backup.txt"
BACKUPS_DIR = "/home/user/backups"

EXPECTED_PATHS = {
    "operators/cert-manager/cert-manager.yaml",
    "operators/cert-manager/webhook.yaml",
    "operators/nginx-ingress/ingress-controller.yaml",
    "operators/prometheus/operator.yaml",
    "operators/prometheus/rbac.yaml",
}


def test_backups_directory_exists():
    assert os.path.isdir(BACKUPS_DIR), (
        f"Backups directory does not exist: {BACKUPS_DIR}"
    )


def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive file does not exist: {ARCHIVE_PATH}"
    )


def test_txt_file_exists():
    assert os.path.isfile(TXT_PATH), (
        f"Verification text file does not exist: {TXT_PATH}"
    )


def test_archive_is_valid_gzip():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive not found: {ARCHIVE_PATH}"
    try:
        with gzip.open(ARCHIVE_PATH, 'rb') as gz:
            gz.read(1)
    except Exception as e:
        pytest.fail(f"Archive is not valid gzip: {ARCHIVE_PATH} — {e}")


def test_archive_is_valid_tar():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive not found: {ARCHIVE_PATH}"
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            members = tf.getmembers()
    except Exception as e:
        pytest.fail(f"Archive is not a valid tar.gz: {ARCHIVE_PATH} — {e}")
    assert len(members) > 0, "Archive is empty (no members found)"


def test_archive_contains_expected_files():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive not found: {ARCHIVE_PATH}"
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getnames()
    found = set(members)
    assert found == EXPECTED_PATHS, (
        f"Archive contents do not match expected.\n"
        f"Expected: {sorted(EXPECTED_PATHS)}\n"
        f"Found:    {sorted(found)}"
    )


def test_archive_has_no_absolute_paths():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive not found: {ARCHIVE_PATH}"
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getnames()
    absolute = [m for m in members if m.startswith("/")]
    assert len(absolute) == 0, (
        f"Archive contains absolute paths (should be relative): {absolute}"
    )


def test_archive_paths_start_with_operators():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive not found: {ARCHIVE_PATH}"
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getnames()
    bad = [m for m in members if not m.startswith("operators/")]
    assert len(bad) == 0, (
        f"Archive contains paths not starting with 'operators/': {bad}"
    )


def test_txt_file_contains_expected_paths():
    assert os.path.isfile(TXT_PATH), f"Text file not found: {TXT_PATH}"
    with open(TXT_PATH, "r") as f:
        content = f.read()
    lines = [line for line in content.splitlines() if line.strip()]
    found = set(lines)
    assert found == EXPECTED_PATHS, (
        f"Text file contents do not match expected paths.\n"
        f"Expected: {sorted(EXPECTED_PATHS)}\n"
        f"Found:    {sorted(found)}"
    )


def test_txt_file_has_no_absolute_paths():
    assert os.path.isfile(TXT_PATH), f"Text file not found: {TXT_PATH}"
    with open(TXT_PATH, "r") as f:
        lines = f.read().splitlines()
    absolute = [line for line in lines if line.startswith("/")]
    assert len(absolute) == 0, (
        f"Text file contains absolute paths (should be relative): {absolute}"
    )


def test_txt_file_has_no_extra_metadata():
    """Lines should be plain paths only — no permissions, timestamps, sizes."""
    assert os.path.isfile(TXT_PATH), f"Text file not found: {TXT_PATH}"
    with open(TXT_PATH, "r") as f:
        lines = [line for line in f.read().splitlines() if line.strip()]
    for line in lines:
        # A plain path line should not contain spaces (metadata lines typically do)
        assert " " not in line, (
            f"Text file line appears to contain metadata (has spaces): {repr(line)}"
        )
        # Should end with .yaml
        assert line.endswith(".yaml"), (
            f"Text file line does not end with .yaml: {repr(line)}"
        )


def test_txt_file_matches_tar_contents():
    """The .txt file should list exactly the same paths as tar -tf outputs."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive not found: {ARCHIVE_PATH}"
    assert os.path.isfile(TXT_PATH), f"Text file not found: {TXT_PATH}"

    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        tar_members = tf.getnames()

    with open(TXT_PATH, "r") as f:
        txt_lines = [line for line in f.read().splitlines() if line.strip()]

    assert set(tar_members) == set(txt_lines), (
        f"Tar contents and .txt file do not match.\n"
        f"In tar but not in txt: {sorted(set(tar_members) - set(txt_lines))}\n"
        f"In txt but not in tar: {sorted(set(txt_lines) - set(tar_members))}"
    )


def test_txt_file_line_count():
    assert os.path.isfile(TXT_PATH), f"Text file not found: {TXT_PATH}"
    with open(TXT_PATH, "r") as f:
        lines = [line for line in f.read().splitlines() if line.strip()]
    assert len(lines) == 5, (
        f"Expected exactly 5 lines in {TXT_PATH}, found {len(lines)}: {lines}"
    )


def test_archive_file_contents_are_valid_yaml_text():
    """Each file inside the archive should contain readable YAML-like content."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive not found: {ARCHIVE_PATH}"
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        for member in tf.getmembers():
            if member.isfile():
                f = tf.extractfile(member)
                assert f is not None, f"Could not extract member: {member.name}"
                content = f.read().decode("utf-8")
                assert "apiVersion" in content, (
                    f"File {member.name} in archive does not look like valid YAML "
                    f"(missing 'apiVersion'). Content:\n{content}"
                )


def test_archive_can_be_extracted():
    """Verify the archive can be fully extracted without errors."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive not found: {ARCHIVE_PATH}"
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            # Read all member data to verify integrity
            for member in tf.getmembers():
                if member.isfile():
                    f = tf.extractfile(member)
                    if f:
                        f.read()
    except Exception as e:
        pytest.fail(f"Failed to fully read archive {ARCHIVE_PATH}: {e}")