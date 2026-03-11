# test_final_state.py

import hashlib
import os
import subprocess
import tarfile
import pytest

COMPLIANCE_DIR = "/home/user/compliance"
BACKUPS_DIR = "/home/user/backups"
ARCHIVE_PATH = "/home/user/backups/policies.tar.gz"
CHECKSUM_PATH = "/home/user/backups/policies.tar.gz.sha256"

EXPECTED_POLICY_FILES = {"access_policy.yml", "network_policy.yml", "secrets_policy.yml"}
EXCLUDED_FILES = {"notes.txt", "draft_network.yml", "README.md"}


def test_backups_directory_exists():
    assert os.path.isdir(BACKUPS_DIR), (
        f"Backups directory {BACKUPS_DIR} does not exist. "
        "It should have been created as part of the task."
    )


def test_archive_exists():
    assert os.path.isfile(ARCHIVE_PATH), (
        f"Archive file {ARCHIVE_PATH} does not exist. "
        "The task requires creating a gzip-compressed tar archive at this path."
    )


def test_checksum_file_exists():
    assert os.path.isfile(CHECKSUM_PATH), (
        f"Checksum file {CHECKSUM_PATH} does not exist. "
        "The task requires generating a SHA-256 checksum file at this path."
    )


def test_archive_is_valid_gzip_tar():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    assert tarfile.is_tarfile(ARCHIVE_PATH), (
        f"{ARCHIVE_PATH} is not a valid tar file."
    )
    try:
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
            _ = tf.getmembers()
    except Exception as e:
        pytest.fail(f"Failed to open {ARCHIVE_PATH} as a gzip-compressed tar: {e}")


def test_archive_contains_exactly_policy_files():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getmembers()
        names = {m.name for m in members}

    assert names == EXPECTED_POLICY_FILES, (
        f"Archive members do not match expected policy files.\n"
        f"Expected: {sorted(EXPECTED_POLICY_FILES)}\n"
        f"Actual:   {sorted(names)}\n"
        f"Missing:  {sorted(EXPECTED_POLICY_FILES - names)}\n"
        f"Extra:    {sorted(names - EXPECTED_POLICY_FILES)}"
    )


def test_archive_members_have_no_path_components():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getmembers()

    for member in members:
        basename = os.path.basename(member.name)
        assert member.name == basename, (
            f"Archive member '{member.name}' has path components. "
            f"Expected bare filename '{basename}' with no leading path. "
            "Files should be archived without any leading path components."
        )
        assert not member.name.startswith("/"), (
            f"Archive member '{member.name}' has an absolute path. "
            "Files should be archived as bare filenames."
        )
        assert not member.name.startswith("./"), (
            f"Archive member '{member.name}' starts with './'. "
            "Files should be archived as bare filenames without './' prefix."
        )


def test_excluded_files_not_in_archive():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        names = {m.name for m in tf.getmembers()}

    for excluded in EXCLUDED_FILES:
        assert excluded not in names, (
            f"Excluded file '{excluded}' was found in the archive {ARCHIVE_PATH}. "
            f"Only files matching '*_policy.yml' should be included."
        )


def test_archive_members_are_regular_files():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        members = tf.getmembers()

    for member in members:
        assert member.isfile(), (
            f"Archive member '{member.name}' is not a regular file (type={member.type}). "
            "All archived members should be regular files."
        )


def test_checksum_file_format():
    assert os.path.isfile(CHECKSUM_PATH), f"Checksum file {CHECKSUM_PATH} does not exist."
    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines(keepends=True)
    assert len(lines) == 1, (
        f"Checksum file {CHECKSUM_PATH} should contain exactly one line, "
        f"but found {len(lines)} lines. Content: {repr(content)}"
    )

    line = lines[0]
    assert line.endswith("\n"), (
        f"Checksum file line does not end with a newline. "
        f"Line content: {repr(line)}"
    )

    # Format: <64-char hex>  <filename>
    stripped = line.rstrip("\n")
    parts = stripped.split("  ", 1)
    assert len(parts) == 2, (
        f"Checksum file line does not match expected format '<sha256hex>  policies.tar.gz'. "
        f"Expected two fields separated by two spaces. Line: {repr(stripped)}"
    )

    sha256hex, filename = parts
    assert len(sha256hex) == 64, (
        f"SHA-256 hex digest should be 64 characters, got {len(sha256hex)}. "
        f"Value: {repr(sha256hex)}"
    )
    assert all(c in "0123456789abcdef" for c in sha256hex), (
        f"SHA-256 hex digest contains non-hex characters: {repr(sha256hex)}"
    )
    assert filename == "policies.tar.gz", (
        f"Second field in checksum file should be 'policies.tar.gz' (bare filename), "
        f"but got {repr(filename)}. "
        "Do not use the full path — only the bare filename."
    )


def test_checksum_matches_archive():
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    assert os.path.isfile(CHECKSUM_PATH), f"Checksum file {CHECKSUM_PATH} does not exist."

    # Compute actual SHA-256 of the archive
    sha256 = hashlib.sha256()
    with open(ARCHIVE_PATH, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    actual_hex = sha256.hexdigest()

    # Read the stored checksum
    with open(CHECKSUM_PATH, "r") as f:
        content = f.read()
    line = content.strip()
    parts = line.split("  ", 1)
    assert len(parts) == 2, (
        f"Could not parse checksum file line: {repr(line)}"
    )
    stored_hex = parts[0]

    assert stored_hex == actual_hex, (
        f"SHA-256 checksum in {CHECKSUM_PATH} does not match the actual archive.\n"
        f"Stored:   {stored_hex}\n"
        f"Actual:   {actual_hex}\n"
        "The checksum file must contain the SHA-256 of the exact archive file."
    )


def test_sha256sum_check_command():
    """Verify that `sha256sum --check` passes when run from the backups directory."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    assert os.path.isfile(CHECKSUM_PATH), f"Checksum file {CHECKSUM_PATH} does not exist."

    result = subprocess.run(
        ["sha256sum", "--check", "policies.tar.gz.sha256"],
        cwd=BACKUPS_DIR,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"`sha256sum --check policies.tar.gz.sha256` failed (exit code {result.returncode}) "
        f"when run from {BACKUPS_DIR}.\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}\n"
        "Ensure the checksum file contains the correct SHA-256 of the archive."
    )


def test_tar_list_command():
    """Verify that `tar -tzf` lists exactly the expected policy files."""
    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."

    result = subprocess.run(
        ["tar", "-tzf", ARCHIVE_PATH],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"`tar -tzf {ARCHIVE_PATH}` failed with exit code {result.returncode}.\n"
        f"stderr: {result.stderr}"
    )

    listed_files = {line.strip() for line in result.stdout.splitlines() if line.strip()}
    assert listed_files == EXPECTED_POLICY_FILES, (
        f"`tar -tzf` output does not match expected policy files.\n"
        f"Expected: {sorted(EXPECTED_POLICY_FILES)}\n"
        f"Actual:   {sorted(listed_files)}\n"
        f"Missing:  {sorted(EXPECTED_POLICY_FILES - listed_files)}\n"
        f"Extra:    {sorted(listed_files - EXPECTED_POLICY_FILES)}"
    )


def test_policy_file_contents_in_archive():
    """Verify that the archived policy files have the correct content."""
    expected_contents = {
        "access_policy.yml": "policy: access\nversion: 1\nrules:\n  - deny_all_by_default: true\n",
        "network_policy.yml": (
            "policy: network\nversion: 2\nrules:\n"
            "  - block_inbound: true\n  - allow_egress_443: true\n"
        ),
        "secrets_policy.yml": (
            "policy: secrets\nversion: 1\nrules:\n"
            "  - rotate_every_days: 90\n  - min_length: 32\n"
        ),
    }

    assert os.path.isfile(ARCHIVE_PATH), f"Archive {ARCHIVE_PATH} does not exist."
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tf:
        for filename, expected in expected_contents.items():
            try:
                member = tf.getmember(filename)
            except KeyError:
                pytest.fail(
                    f"Expected member '{filename}' not found in archive {ARCHIVE_PATH}."
                )
            f = tf.extractfile(member)
            assert f is not None, f"Could not extract '{filename}' from archive."
            actual_content = f.read().decode("utf-8")
            assert actual_content.strip() == expected.strip(), (
                f"Content of '{filename}' in archive does not match expected.\n"
                f"Expected:\n{expected}\n"
                f"Actual:\n{actual_content}"
            )