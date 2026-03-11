# test_final_state.py

import json
import os
import pytest

BACKUPS_DIR = "/home/user/backups"
MANIFEST_PATH = "/home/user/backups/manifest.json"
VALID_BACKUPS_PATH = "/home/user/backups/valid_backups.json"
INTEGRITY_REPORT_PATH = "/home/user/backups/integrity_report.txt"

EXPECTED_VALID_BACKUPS = [
    {"id": "bkp-001", "filename": "db_full_20240301.tar.gz"},
    {"id": "bkp-005", "filename": "db_full_20240305.tar.gz"},
    {"id": "bkp-006", "filename": "db_incremental_20240306.tar.gz"},
]

EXPECTED_INTEGRITY_REPORT = "Valid backups: 3/7\n"

EXPECTED_VALID_BACKUPS_JSON = (
    '[\n'
    '  {\n'
    '    "id": "bkp-001",\n'
    '    "filename": "db_full_20240301.tar.gz"\n'
    '  },\n'
    '  {\n'
    '    "id": "bkp-005",\n'
    '    "filename": "db_full_20240305.tar.gz"\n'
    '  },\n'
    '  {\n'
    '    "id": "bkp-006",\n'
    '    "filename": "db_incremental_20240306.tar.gz"\n'
    '  }\n'
    ']\n'
)


# ── valid_backups.json tests ──────────────────────────────────────────────────

def test_valid_backups_file_exists():
    assert os.path.isfile(VALID_BACKUPS_PATH), (
        f"{VALID_BACKUPS_PATH} does not exist. "
        "Step 1 of the task requires creating this file."
    )


def test_valid_backups_file_is_readable():
    assert os.access(VALID_BACKUPS_PATH, os.R_OK), (
        f"{VALID_BACKUPS_PATH} exists but is not readable."
    )


def test_valid_backups_is_valid_json():
    with open(VALID_BACKUPS_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as exc:
            pytest.fail(
                f"{VALID_BACKUPS_PATH} does not contain valid JSON: {exc}"
            )


def test_valid_backups_is_json_array():
    with open(VALID_BACKUPS_PATH, "r") as f:
        data = json.load(f)
    assert isinstance(data, list), (
        f"{VALID_BACKUPS_PATH} should be a JSON array at the top level, "
        f"but got {type(data).__name__}."
    )


def test_valid_backups_has_correct_count():
    with open(VALID_BACKUPS_PATH, "r") as f:
        data = json.load(f)
    assert len(data) == 3, (
        f"{VALID_BACKUPS_PATH} should contain exactly 3 valid backup entries, "
        f"but contains {len(data)}: {data}"
    )


def test_valid_backups_entries_have_only_id_and_filename():
    with open(VALID_BACKUPS_PATH, "r") as f:
        data = json.load(f)
    for i, entry in enumerate(data):
        keys = set(entry.keys())
        assert keys == {"id", "filename"}, (
            f"Entry at index {i} in {VALID_BACKUPS_PATH} should have exactly "
            f"the keys 'id' and 'filename', but has: {keys}. "
            "Extra fields like 'size_bytes', 'checksum', 'status' must be removed."
        )


def test_valid_backups_correct_ids_in_order():
    with open(VALID_BACKUPS_PATH, "r") as f:
        data = json.load(f)
    actual_ids = [entry.get("id") for entry in data]
    expected_ids = ["bkp-001", "bkp-005", "bkp-006"]
    assert actual_ids == expected_ids, (
        f"The 'id' values in {VALID_BACKUPS_PATH} are incorrect or out of order. "
        f"Expected {expected_ids}, got {actual_ids}."
    )


def test_valid_backups_correct_filenames():
    with open(VALID_BACKUPS_PATH, "r") as f:
        data = json.load(f)
    for expected in EXPECTED_VALID_BACKUPS:
        match = next((e for e in data if e.get("id") == expected["id"]), None)
        assert match is not None, (
            f"Entry with id '{expected['id']}' is missing from {VALID_BACKUPS_PATH}."
        )
        assert match.get("filename") == expected["filename"], (
            f"Entry '{expected['id']}' has wrong filename. "
            f"Expected '{expected['filename']}', got '{match.get('filename')}'."
        )


def test_valid_backups_entry_bkp001():
    with open(VALID_BACKUPS_PATH, "r") as f:
        data = json.load(f)
    entry = next((e for e in data if e.get("id") == "bkp-001"), None)
    assert entry is not None, (
        "bkp-001 should be in valid_backups.json (size_bytes=1048576, checksum present, status=complete)."
    )
    assert entry.get("filename") == "db_full_20240301.tar.gz", (
        f"bkp-001 filename should be 'db_full_20240301.tar.gz', got '{entry.get('filename')}'."
    )


def test_valid_backups_entry_bkp005():
    with open(VALID_BACKUPS_PATH, "r") as f:
        data = json.load(f)
    entry = next((e for e in data if e.get("id") == "bkp-005"), None)
    assert entry is not None, (
        "bkp-005 should be in valid_backups.json (size_bytes=4194304, checksum present, status=complete)."
    )
    assert entry.get("filename") == "db_full_20240305.tar.gz", (
        f"bkp-005 filename should be 'db_full_20240305.tar.gz', got '{entry.get('filename')}'."
    )


def test_valid_backups_entry_bkp006():
    with open(VALID_BACKUPS_PATH, "r") as f:
        data = json.load(f)
    entry = next((e for e in data if e.get("id") == "bkp-006"), None)
    assert entry is not None, (
        "bkp-006 should be in valid_backups.json (size_bytes=512000, checksum present, status=complete)."
    )
    assert entry.get("filename") == "db_incremental_20240306.tar.gz", (
        f"bkp-006 filename should be 'db_incremental_20240306.tar.gz', got '{entry.get('filename')}'."
    )


def test_valid_backups_no_invalid_entries():
    """Ensure none of the known-invalid IDs appear in valid_backups.json."""
    with open(VALID_BACKUPS_PATH, "r") as f:
        data = json.load(f)
    actual_ids = {entry.get("id") for entry in data}
    invalid_ids = {"bkp-002", "bkp-003", "bkp-004", "bkp-007"}
    found_invalid = actual_ids & invalid_ids
    assert not found_invalid, (
        f"The following invalid backup IDs should NOT appear in {VALID_BACKUPS_PATH}: "
        f"{found_invalid}. "
        "bkp-002: size_bytes=0; bkp-003: checksum=null; "
        "bkp-004: status=partial; bkp-007: size=0, checksum=null, partial."
    )


def test_valid_backups_exact_jq_formatting():
    """Check that the file matches the exact jq pretty-print output (2-space indent, trailing newline)."""
    with open(VALID_BACKUPS_PATH, "r") as f:
        raw = f.read()
    assert raw == EXPECTED_VALID_BACKUPS_JSON, (
        f"{VALID_BACKUPS_PATH} does not match the expected jq pretty-print format.\n"
        f"Expected:\n{EXPECTED_VALID_BACKUPS_JSON!r}\n"
        f"Got:\n{raw!r}"
    )


# ── integrity_report.txt tests ────────────────────────────────────────────────

def test_integrity_report_file_exists():
    assert os.path.isfile(INTEGRITY_REPORT_PATH), (
        f"{INTEGRITY_REPORT_PATH} does not exist. "
        "Step 2 of the task requires creating this file."
    )


def test_integrity_report_file_is_readable():
    assert os.access(INTEGRITY_REPORT_PATH, os.R_OK), (
        f"{INTEGRITY_REPORT_PATH} exists but is not readable."
    )


def test_integrity_report_exact_content():
    with open(INTEGRITY_REPORT_PATH, "r") as f:
        content = f.read()
    assert content == EXPECTED_INTEGRITY_REPORT, (
        f"{INTEGRITY_REPORT_PATH} does not have the expected content.\n"
        f"Expected: {EXPECTED_INTEGRITY_REPORT!r}\n"
        f"Got:      {content!r}\n"
        "The file must contain exactly one line: 'Valid backups: 3/7' followed by a newline."
    )


def test_integrity_report_single_line():
    with open(INTEGRITY_REPORT_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 1, (
        f"{INTEGRITY_REPORT_PATH} should contain exactly one line, "
        f"but found {len(lines)} lines: {lines!r}"
    )


def test_integrity_report_ends_with_newline():
    with open(INTEGRITY_REPORT_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"{INTEGRITY_REPORT_PATH} must end with a newline character, "
        f"but the last byte is {content[-1:]!r}."
    )


def test_integrity_report_correct_counts():
    with open(INTEGRITY_REPORT_PATH, "r") as f:
        content = f.read().strip()
    assert content == "Valid backups: 3/7", (
        f"{INTEGRITY_REPORT_PATH} has wrong content (ignoring trailing whitespace). "
        f"Expected 'Valid backups: 3/7', got {content!r}. "
        "N=3 valid entries, M=7 total entries."
    )


def test_integrity_report_format():
    with open(INTEGRITY_REPORT_PATH, "r") as f:
        line = f.readline()
    stripped = line.rstrip("\n")
    assert stripped.startswith("Valid backups: "), (
        f"The line in {INTEGRITY_REPORT_PATH} must start with 'Valid backups: ', "
        f"got: {stripped!r}"
    )
    parts = stripped.split(": ", 1)
    assert len(parts) == 2, (
        f"Cannot parse 'Valid backups: N/M' from line: {stripped!r}"
    )
    fraction = parts[1]
    assert "/" in fraction, (
        f"The count portion should be in 'N/M' format, got: {fraction!r}"
    )
    n_str, m_str = fraction.split("/", 1)
    assert n_str.isdigit() and m_str.isdigit(), (
        f"N and M in 'Valid backups: N/M' must be integers, got N={n_str!r}, M={m_str!r}"
    )
    assert int(n_str) == 3, (
        f"N (valid count) should be 3, got {int(n_str)}."
    )
    assert int(m_str) == 7, (
        f"M (total count) should be 7, got {int(m_str)}."
    )


# ── cross-check: output files are consistent with manifest ────────────────────

def test_manifest_still_intact():
    """The original manifest.json must not have been modified."""
    with open(MANIFEST_PATH, "r") as f:
        data = json.load(f)
    assert "backups" in data, "manifest.json lost its 'backups' key."
    assert len(data["backups"]) == 7, (
        f"manifest.json should still have 7 entries, got {len(data['backups'])}."
    )


def test_valid_backups_consistent_with_manifest():
    """Every entry in valid_backups.json must correspond to a truly valid entry in manifest.json."""
    with open(MANIFEST_PATH, "r") as f:
        manifest = json.load(f)
    with open(VALID_BACKUPS_PATH, "r") as f:
        valid = json.load(f)

    manifest_by_id = {e["id"]: e for e in manifest["backups"]}

    for entry in valid:
        entry_id = entry.get("id")
        assert entry_id in manifest_by_id, (
            f"Entry id '{entry_id}' in {VALID_BACKUPS_PATH} does not exist in manifest.json."
        )
        source = manifest_by_id[entry_id]
        assert source["size_bytes"] > 0, (
            f"Entry '{entry_id}' is in valid_backups.json but has size_bytes={source['size_bytes']} (must be > 0)."
        )
        assert source["checksum"] is not None, (
            f"Entry '{entry_id}' is in valid_backups.json but has checksum=null."
        )
        assert source["status"] == "complete", (
            f"Entry '{entry_id}' is in valid_backups.json but has status='{source['status']}' (must be 'complete')."
        )
        assert entry.get("filename") == source["filename"], (
            f"Entry '{entry_id}' filename mismatch: "
            f"valid_backups.json has '{entry.get('filename')}', "
            f"manifest.json has '{source['filename']}'."
        )