# test_final_state.py

import hashlib
import os
import re
import subprocess

import pytest

ARTIFACTS_DIR = "/home/user/deploy/artifacts"
CHECKSUMS_FILE = "/home/user/deploy/checksums.sha256"

ARTIFACT_FILES = [
    "auth-service-2.1.4.tar.gz",
    "billing-service-1.8.0.tar.gz",
    "gateway-service-3.0.2.tar.gz",
]


def compute_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def test_artifacts_directory_exists():
    assert os.path.isdir(ARTIFACTS_DIR), (
        f"Artifacts directory does not exist: {ARTIFACTS_DIR}"
    )


@pytest.mark.parametrize("filename", ARTIFACT_FILES)
def test_artifact_file_exists(filename):
    filepath = os.path.join(ARTIFACTS_DIR, filename)
    assert os.path.isfile(filepath), (
        f"Artifact file does not exist: {filepath}"
    )


def test_checksums_file_exists():
    assert os.path.isfile(CHECKSUMS_FILE), (
        f"Checksums manifest file does not exist: {CHECKSUMS_FILE}. "
        f"The file must be created as part of the task."
    )


def test_checksums_file_ends_with_newline():
    assert os.path.isfile(CHECKSUMS_FILE), (
        f"Cannot check newline: {CHECKSUMS_FILE} does not exist."
    )
    with open(CHECKSUMS_FILE, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"{CHECKSUMS_FILE} does not end with a newline. "
        f"Last bytes: {content[-10:]!r}"
    )


def test_checksums_file_has_exactly_three_lines():
    assert os.path.isfile(CHECKSUMS_FILE), (
        f"Cannot check line count: {CHECKSUMS_FILE} does not exist."
    )
    with open(CHECKSUMS_FILE, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 3, (
        f"Expected exactly 3 lines in {CHECKSUMS_FILE}, got {len(lines)}. "
        f"Content: {content!r}"
    )


def test_checksums_lines_in_alphabetical_order():
    assert os.path.isfile(CHECKSUMS_FILE), (
        f"Cannot check ordering: {CHECKSUMS_FILE} does not exist."
    )
    with open(CHECKSUMS_FILE, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 3, (
        f"Expected 3 lines, got {len(lines)}. Content: {content!r}"
    )

    expected_order = sorted(ARTIFACT_FILES)
    for i, (line, expected_filename) in enumerate(zip(lines, expected_order)):
        parts = line.split("  ", 1)
        assert len(parts) == 2, (
            f"Line {i+1} does not contain two-space separator: {line!r}"
        )
        actual_filename = parts[1]
        assert actual_filename == expected_filename, (
            f"Line {i+1}: expected filename '{expected_filename}', "
            f"got '{actual_filename}'. Lines must be in alphabetical order "
            f"(auth first, billing second, gateway third)."
        )


def test_checksums_line_format():
    assert os.path.isfile(CHECKSUMS_FILE), (
        f"Cannot check format: {CHECKSUMS_FILE} does not exist."
    )
    line_pattern = re.compile(r"^[0-9a-f]{64}  [a-z0-9.+\-]+\.tar\.gz$")
    with open(CHECKSUMS_FILE, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 3, (
        f"Expected 3 lines, got {len(lines)}. Content: {content!r}"
    )

    for i, line in enumerate(lines):
        assert line_pattern.match(line), (
            f"Line {i+1} does not match expected format "
            f"'^[0-9a-f]{{64}}  <bare-filename>.tar.gz': {line!r}. "
            f"Expected: 64 hex chars, two spaces, bare filename with no path prefix."
        )


def test_checksums_no_path_prefix_in_filenames():
    assert os.path.isfile(CHECKSUMS_FILE), (
        f"Cannot check path prefix: {CHECKSUMS_FILE} does not exist."
    )
    with open(CHECKSUMS_FILE, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    for i, line in enumerate(lines):
        parts = line.split("  ", 1)
        if len(parts) == 2:
            filename_part = parts[1]
            assert "/" not in filename_part, (
                f"Line {i+1} contains a path prefix in the filename: {line!r}. "
                f"Filenames must be bare (no directory prefix)."
            )


def test_hex_digests_match_actual_file_contents():
    assert os.path.isfile(CHECKSUMS_FILE), (
        f"Cannot verify digests: {CHECKSUMS_FILE} does not exist."
    )
    with open(CHECKSUMS_FILE, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 3, (
        f"Expected 3 lines, got {len(lines)}. Content: {content!r}"
    )

    expected_order = sorted(ARTIFACT_FILES)
    for i, (line, filename) in enumerate(zip(lines, expected_order)):
        parts = line.split("  ", 1)
        assert len(parts) == 2, (
            f"Line {i+1} malformed (no two-space separator): {line!r}"
        )
        recorded_hex = parts[0]
        filepath = os.path.join(ARTIFACTS_DIR, filename)
        assert os.path.isfile(filepath), (
            f"Artifact file referenced on line {i+1} does not exist: {filepath}"
        )
        actual_hex = compute_sha256(filepath)
        assert recorded_hex == actual_hex, (
            f"SHA256 mismatch for '{filename}':\n"
            f"  Recorded in manifest: {recorded_hex}\n"
            f"  Actual file hash:     {actual_hex}\n"
            f"  File path: {filepath}\n"
            f"  The manifest hash does not match the actual file contents."
        )


def test_sha256sum_check_passes():
    assert os.path.isfile(CHECKSUMS_FILE), (
        f"Cannot run sha256sum --check: {CHECKSUMS_FILE} does not exist."
    )
    assert os.path.isdir(ARTIFACTS_DIR), (
        f"Cannot run sha256sum --check: artifacts directory does not exist: {ARTIFACTS_DIR}"
    )
    result = subprocess.run(
        ["sha256sum", "--check", CHECKSUMS_FILE],
        capture_output=True,
        text=True,
        cwd=ARTIFACTS_DIR,
    )
    assert result.returncode == 0, (
        f"`sha256sum --check {CHECKSUMS_FILE}` (run from {ARTIFACTS_DIR}) "
        f"failed with exit code {result.returncode}.\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}\n"
        f"Ensure the checksums file was generated from the artifacts directory "
        f"so filenames resolve correctly."
    )
    ok_count = result.stdout.count(": OK")
    assert ok_count == 3, (
        f"Expected 3 'OK' results from sha256sum --check, got {ok_count}.\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )


def test_checksums_file_lists_all_expected_artifacts():
    assert os.path.isfile(CHECKSUMS_FILE), (
        f"Cannot verify artifact listing: {CHECKSUMS_FILE} does not exist."
    )
    with open(CHECKSUMS_FILE, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")

    filenames_in_manifest = []
    for line in lines:
        parts = line.split("  ", 1)
        if len(parts) == 2:
            filenames_in_manifest.append(parts[1])

    for expected_filename in sorted(ARTIFACT_FILES):
        assert expected_filename in filenames_in_manifest, (
            f"Expected artifact '{expected_filename}' not found in manifest "
            f"{CHECKSUMS_FILE}. Found filenames: {filenames_in_manifest}"
        )

    assert len(filenames_in_manifest) == len(ARTIFACT_FILES), (
        f"Manifest contains {len(filenames_in_manifest)} entries but expected "
        f"{len(ARTIFACT_FILES)}. Filenames found: {filenames_in_manifest}"
    )