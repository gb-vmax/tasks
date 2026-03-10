# test_final_state.py

import os
import hashlib
import pytest

INCIDENT_DIR = "/home/user/incident"
CONFIGS_DIR = "/home/user/incident/configs"
MANIFEST_FILE = "/home/user/incident/trusted_checksums.sha256"
REPORT_FILE = "/home/user/incident/integrity_report.txt"

EXPECTED_REPORT = """INTEGRITY CHECK REPORT
======================
FAILED: configs/crontab
FAILED: configs/sshd_config
OK: configs/hosts
OK: configs/nginx.conf
OK: configs/resolv.conf"""


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Integrity report file does not exist: {REPORT_FILE}\n"
        "The task requires writing a report to this path."
    )


def test_report_file_exact_content():
    """The report must match the exact expected format."""
    with open(REPORT_FILE, "r") as f:
        actual = f.read()

    # Strip trailing newline for comparison (allow one trailing newline)
    actual_stripped = actual.rstrip("\n")
    expected_stripped = EXPECTED_REPORT.strip("\n")

    assert actual_stripped == expected_stripped, (
        f"Integrity report content does not match expected.\n\n"
        f"Expected:\n{expected_stripped!r}\n\n"
        f"Actual:\n{actual_stripped!r}\n\n"
        f"Expected (readable):\n{expected_stripped}\n\n"
        f"Actual (readable):\n{actual_stripped}"
    )


def test_report_first_line():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, "Report file is empty."
    assert lines[0] == "INTEGRITY CHECK REPORT", (
        f"First line of report is wrong.\n"
        f"Expected: 'INTEGRITY CHECK REPORT'\n"
        f"Actual:   {lines[0]!r}"
    )


def test_report_second_line():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 2, "Report file has fewer than 2 lines."
    assert lines[1] == "======================", (
        f"Second line of report is wrong.\n"
        f"Expected: '======================'\n"
        f"Actual:   {lines[1]!r}"
    )


def test_report_failed_entries_before_ok_entries():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    # Skip header lines
    entry_lines = [l for l in lines[2:] if l.strip()]

    failed_indices = [i for i, l in enumerate(entry_lines) if l.startswith("FAILED:")]
    ok_indices = [i for i, l in enumerate(entry_lines) if l.startswith("OK:")]

    assert failed_indices, "No FAILED: entries found in report."
    assert ok_indices, "No OK: entries found in report."

    max_failed_idx = max(failed_indices)
    min_ok_idx = min(ok_indices)

    assert max_failed_idx < min_ok_idx, (
        f"All FAILED: entries must appear before all OK: entries.\n"
        f"Entry lines: {entry_lines}"
    )


def test_report_failed_entries():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    entry_lines = [l for l in lines[2:] if l.strip()]
    failed_lines = [l for l in entry_lines if l.startswith("FAILED:")]

    expected_failed = ["FAILED: configs/crontab", "FAILED: configs/sshd_config"]
    assert failed_lines == expected_failed, (
        f"FAILED entries do not match expected.\n"
        f"Expected: {expected_failed}\n"
        f"Actual:   {failed_lines}"
    )


def test_report_ok_entries():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    entry_lines = [l for l in lines[2:] if l.strip()]
    ok_lines = [l for l in entry_lines if l.startswith("OK:")]

    expected_ok = [
        "OK: configs/hosts",
        "OK: configs/nginx.conf",
        "OK: configs/resolv.conf",
    ]
    assert ok_lines == expected_ok, (
        f"OK entries do not match expected.\n"
        f"Expected: {expected_ok}\n"
        f"Actual:   {ok_lines}"
    )


def test_report_failed_entries_sorted_alphabetically():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    entry_lines = [l for l in lines[2:] if l.strip()]
    failed_lines = [l for l in entry_lines if l.startswith("FAILED:")]

    # Extract filenames for sorting check
    failed_filenames = [l[len("FAILED: "):] for l in failed_lines]
    assert failed_filenames == sorted(failed_filenames), (
        f"FAILED entries are not sorted alphabetically by filename.\n"
        f"Actual order: {failed_filenames}\n"
        f"Expected order: {sorted(failed_filenames)}"
    )


def test_report_ok_entries_sorted_alphabetically():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    entry_lines = [l for l in lines[2:] if l.strip()]
    ok_lines = [l for l in entry_lines if l.startswith("OK:")]

    ok_filenames = [l[len("OK: "):] for l in ok_lines]
    assert ok_filenames == sorted(ok_filenames), (
        f"OK entries are not sorted alphabetically by filename.\n"
        f"Actual order: {ok_filenames}\n"
        f"Expected order: {sorted(ok_filenames)}"
    )


def test_report_no_trailing_whitespace():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    for i, line in enumerate(lines):
        assert line == line.rstrip(), (
            f"Line {i + 1} has trailing whitespace: {line!r}"
        )


def test_report_no_blank_lines_between_entries():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    # After the two header lines, there should be no blank lines
    entry_section = lines[2:]
    for i, line in enumerate(entry_section):
        assert line.strip() != "", (
            f"Blank line found at position {i + 3} (1-indexed) in the report.\n"
            f"There should be no blank lines between entries.\n"
            f"Lines: {entry_section}"
        )


def test_report_total_entry_count():
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    entry_lines = [l for l in lines[2:] if l.strip()]
    assert len(entry_lines) == 5, (
        f"Expected 5 entry lines (2 FAILED + 3 OK), got {len(entry_lines)}.\n"
        f"Entry lines: {entry_lines}"
    )


def test_report_uses_relative_paths_not_absolute():
    with open(REPORT_FILE, "r") as f:
        content = f.read()

    assert "/home/user/incident/configs/" not in content, (
        "Report should use relative paths like 'configs/filename', not absolute paths.\n"
        f"Report content:\n{content}"
    )


def test_report_entry_format():
    """Each entry line must start with 'FAILED: ' or 'OK: ' followed by the path."""
    with open(REPORT_FILE, "r") as f:
        lines = f.read().splitlines()

    entry_lines = lines[2:]
    for line in entry_lines:
        assert line.startswith("FAILED: ") or line.startswith("OK: "), (
            f"Entry line has unexpected format: {line!r}\n"
            "Each line must start with 'FAILED: ' or 'OK: '"
        )


def test_configs_directory_still_intact():
    """Verify the config files still exist and have expected content."""
    expected_configs = {
        "nginx.conf": b"worker_processes 4;\nhttp { listen 80; }\n",
        "sshd_config": b"Port 2222\nPermitRootLogin no\n",
        "hosts": b"127.0.0.1 localhost\n",
        "resolv.conf": b"nameserver 8.8.8.8\nnameserver 8.8.4.4\n",
        "crontab": b"*/5 * * * * /usr/bin/backup.sh\n0 3 * * * /usr/bin/cleanup.sh\n",
    }
    for filename, expected_content in expected_configs.items():
        path = os.path.join(CONFIGS_DIR, filename)
        assert os.path.isfile(path), f"Config file missing: {path}"
        actual = open(path, "rb").read()
        assert actual == expected_content, (
            f"Config file {path} has unexpected content.\n"
            f"Expected: {expected_content!r}\n"
            f"Actual:   {actual!r}"
        )


def test_manifest_still_intact():
    """Verify the manifest still exists and has correct hashes."""
    assert os.path.isfile(MANIFEST_FILE), (
        f"Trusted checksum manifest is missing: {MANIFEST_FILE}"
    )

    original_configs = {
        "configs/nginx.conf": b"worker_processes 4;\nhttp { listen 80; }\n",
        "configs/sshd_config": b"Port 22\nPermitRootLogin no\n",
        "configs/hosts": b"127.0.0.1 localhost\n",
        "configs/resolv.conf": b"nameserver 8.8.8.8\nnameserver 8.8.4.4\n",
        "configs/crontab": b"*/5 * * * * /usr/bin/backup.sh\n",
    }

    with open(MANIFEST_FILE, "r") as f:
        lines = [l.strip() for l in f.read().splitlines() if l.strip()]

    manifest_hashes = {}
    for line in lines:
        parts = line.split()
        assert len(parts) == 2, f"Unexpected manifest line format: {line!r}"
        hash_val, filepath = parts
        manifest_hashes[filepath] = hash_val

    for filepath, original_content in original_configs.items():
        expected_hash = hashlib.sha256(original_content).hexdigest()
        assert filepath in manifest_hashes, (
            f"Manifest missing entry for {filepath}"
        )
        assert manifest_hashes[filepath] == expected_hash, (
            f"Manifest hash for {filepath} is wrong.\n"
            f"Expected: {expected_hash}\n"
            f"Actual:   {manifest_hashes[filepath]}"
        )


def test_report_integrity_matches_actual_checksums():
    """
    Cross-check: verify that the FAILED/OK labels in the report actually
    correspond to whether the current file hashes match the manifest.
    """
    with open(MANIFEST_FILE, "r") as f:
        lines = [l.strip() for l in f.read().splitlines() if l.strip()]

    manifest_hashes = {}
    for line in lines:
        parts = line.split()
        hash_val, filepath = parts
        manifest_hashes[filepath] = hash_val

    with open(REPORT_FILE, "r") as f:
        report_lines = f.read().splitlines()

    entry_lines = [l for l in report_lines[2:] if l.strip()]

    for entry in entry_lines:
        if entry.startswith("FAILED: "):
            filepath = entry[len("FAILED: "):]
            status = "FAILED"
        elif entry.startswith("OK: "):
            filepath = entry[len("OK: "):]
            status = "OK"
        else:
            pytest.fail(f"Unexpected entry format: {entry!r}")

        abs_path = os.path.join(INCIDENT_DIR, filepath)
        assert os.path.isfile(abs_path), f"File referenced in report does not exist: {abs_path}"

        current_hash = hashlib.sha256(open(abs_path, "rb").read()).hexdigest()
        manifest_hash = manifest_hashes.get(filepath)
        assert manifest_hash is not None, f"Manifest has no entry for {filepath}"

        if status == "FAILED":
            assert current_hash != manifest_hash, (
                f"Report says {filepath} FAILED, but its current hash matches the manifest.\n"
                f"Current hash:  {current_hash}\n"
                f"Manifest hash: {manifest_hash}"
            )
        else:
            assert current_hash == manifest_hash, (
                f"Report says {filepath} is OK, but its current hash does NOT match the manifest.\n"
                f"Current hash:  {current_hash}\n"
                f"Manifest hash: {manifest_hash}"
            )