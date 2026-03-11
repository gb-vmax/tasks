# test_final_state.py

import os
import pytest

CLEAN_CSV_PATH = "/home/user/ml_project/clean_samples.csv"
REJECTED_CSV_PATH = "/home/user/ml_project/rejected_samples.csv"
RAW_CSV_PATH = "/home/user/ml_project/raw_samples.csv"

EXPECTED_CLEAN_CONTENT = (
    "sample_id,feature1,feature2,label\n"
    "s001,1.5,-2.3,0\n"
    "s002,9.9,10.0,1\n"
    "s008,-10.0,10.0,0\n"
    "s010,4.2,3.8,1"
)

EXPECTED_REJECTED_CONTENT = (
    "sample_id,feature1,feature2,label,error_reason\n"
    "s003,,3.1,0,missing_field\n"
    "s004,11.2,0.5,1,invalid_feature1\n"
    "s005,-3.3,-11.0,0,invalid_feature2\n"
    "s006,0.0,0.0,2,invalid_label\n"
    "s007,2.7,abc,1,invalid_feature2\n"
    "s009,5.5,5.5,,missing_field"
)


# ── Raw file still intact ──────────────────────────────────────────────────────

def test_raw_csv_still_exists():
    assert os.path.isfile(RAW_CSV_PATH), (
        f"Raw file '{RAW_CSV_PATH}' is missing. It must not be deleted or moved."
    )


# ── clean_samples.csv existence & permissions ──────────────────────────────────

def test_clean_csv_exists():
    assert os.path.isfile(CLEAN_CSV_PATH), (
        f"'{CLEAN_CSV_PATH}' does not exist. "
        "The clean output file must be created by the task."
    )


def test_clean_csv_is_readable():
    assert os.access(CLEAN_CSV_PATH, os.R_OK), (
        f"'{CLEAN_CSV_PATH}' is not readable."
    )


# ── rejected_samples.csv existence & permissions ───────────────────────────────

def test_rejected_csv_exists():
    assert os.path.isfile(REJECTED_CSV_PATH), (
        f"'{REJECTED_CSV_PATH}' does not exist. "
        "The rejected output file must be created by the task."
    )


def test_rejected_csv_is_readable():
    assert os.access(REJECTED_CSV_PATH, os.R_OK), (
        f"'{REJECTED_CSV_PATH}' is not readable."
    )


# ── clean_samples.csv content checks ──────────────────────────────────────────

def test_clean_csv_unix_line_endings():
    with open(CLEAN_CSV_PATH, "rb") as f:
        raw = f.read()
    assert b"\r" not in raw, (
        f"'{CLEAN_CSV_PATH}' contains Windows/CR line endings. "
        "Output must use Unix line endings (LF only)."
    )


def test_clean_csv_no_trailing_newline():
    with open(CLEAN_CSV_PATH, "rb") as f:
        raw = f.read()
    assert not raw.endswith(b"\n"), (
        f"'{CLEAN_CSV_PATH}' has a trailing newline after the last data row. "
        "No trailing newline is allowed."
    )


def test_clean_csv_header():
    with open(CLEAN_CSV_PATH, "r", newline="") as f:
        first_line = f.readline().rstrip("\n")
    expected_header = "sample_id,feature1,feature2,label"
    assert first_line == expected_header, (
        f"Header of '{CLEAN_CSV_PATH}' is wrong.\n"
        f"Expected: '{expected_header}'\n"
        f"Got:      '{first_line}'"
    )


def test_clean_csv_row_count():
    with open(CLEAN_CSV_PATH, "r", newline="") as f:
        lines = f.read().split("\n")
    # Should be exactly 5 lines (1 header + 4 data rows), no trailing empty
    assert len(lines) == 5, (
        f"'{CLEAN_CSV_PATH}' should have exactly 5 lines "
        f"(1 header + 4 data rows), but has {len(lines)} lines.\n"
        f"Lines found: {lines}"
    )


def test_clean_csv_exact_content():
    with open(CLEAN_CSV_PATH, "r", newline="") as f:
        content = f.read()
    assert content == EXPECTED_CLEAN_CONTENT, (
        f"Content of '{CLEAN_CSV_PATH}' does not match expected.\n\n"
        f"Expected (repr):\n{repr(EXPECTED_CLEAN_CONTENT)}\n\n"
        f"Got (repr):\n{repr(content)}"
    )


def test_clean_csv_each_row():
    with open(CLEAN_CSV_PATH, "r", newline="") as f:
        lines = f.read().split("\n")
    expected_lines = EXPECTED_CLEAN_CONTENT.split("\n")
    for i, (actual, expected) in enumerate(zip(lines, expected_lines)):
        assert actual == expected, (
            f"Row {i} of '{CLEAN_CSV_PATH}' is wrong.\n"
            f"Expected: '{expected}'\n"
            f"Got:      '{actual}'"
        )


def test_clean_csv_contains_only_valid_rows():
    """Ensure no rejected sample IDs appear in the clean file."""
    rejected_ids = {"s003", "s004", "s005", "s006", "s007", "s009"}
    with open(CLEAN_CSV_PATH, "r", newline="") as f:
        lines = f.read().split("\n")
    for line in lines[1:]:  # skip header
        if not line:
            continue
        sample_id = line.split(",")[0]
        assert sample_id not in rejected_ids, (
            f"Rejected sample '{sample_id}' found in clean file '{CLEAN_CSV_PATH}'. "
            "Only valid rows should appear in the clean file."
        )


# ── rejected_samples.csv content checks ───────────────────────────────────────

def test_rejected_csv_unix_line_endings():
    with open(REJECTED_CSV_PATH, "rb") as f:
        raw = f.read()
    assert b"\r" not in raw, (
        f"'{REJECTED_CSV_PATH}' contains Windows/CR line endings. "
        "Output must use Unix line endings (LF only)."
    )


def test_rejected_csv_no_trailing_newline():
    with open(REJECTED_CSV_PATH, "rb") as f:
        raw = f.read()
    assert not raw.endswith(b"\n"), (
        f"'{REJECTED_CSV_PATH}' has a trailing newline after the last data row. "
        "No trailing newline is allowed."
    )


def test_rejected_csv_header():
    with open(REJECTED_CSV_PATH, "r", newline="") as f:
        first_line = f.readline().rstrip("\n")
    expected_header = "sample_id,feature1,feature2,label,error_reason"
    assert first_line == expected_header, (
        f"Header of '{REJECTED_CSV_PATH}' is wrong.\n"
        f"Expected: '{expected_header}'\n"
        f"Got:      '{first_line}'"
    )


def test_rejected_csv_row_count():
    with open(REJECTED_CSV_PATH, "r", newline="") as f:
        lines = f.read().split("\n")
    # Should be exactly 7 lines (1 header + 6 data rows), no trailing empty
    assert len(lines) == 7, (
        f"'{REJECTED_CSV_PATH}' should have exactly 7 lines "
        f"(1 header + 6 data rows), but has {len(lines)} lines.\n"
        f"Lines found: {lines}"
    )


def test_rejected_csv_exact_content():
    with open(REJECTED_CSV_PATH, "r", newline="") as f:
        content = f.read()
    assert content == EXPECTED_REJECTED_CONTENT, (
        f"Content of '{REJECTED_CSV_PATH}' does not match expected.\n\n"
        f"Expected (repr):\n{repr(EXPECTED_REJECTED_CONTENT)}\n\n"
        f"Got (repr):\n{repr(content)}"
    )


def test_rejected_csv_each_row():
    with open(REJECTED_CSV_PATH, "r", newline="") as f:
        lines = f.read().split("\n")
    expected_lines = EXPECTED_REJECTED_CONTENT.split("\n")
    for i, (actual, expected) in enumerate(zip(lines, expected_lines)):
        assert actual == expected, (
            f"Row {i} of '{REJECTED_CSV_PATH}' is wrong.\n"
            f"Expected: '{expected}'\n"
            f"Got:      '{actual}'"
        )


def test_rejected_csv_error_reasons():
    """Verify each rejected row carries the correct error_reason."""
    expected_reasons = {
        "s003": "missing_field",
        "s004": "invalid_feature1",
        "s005": "invalid_feature2",
        "s006": "invalid_label",
        "s007": "invalid_feature2",
        "s009": "missing_field",
    }
    with open(REJECTED_CSV_PATH, "r", newline="") as f:
        lines = f.read().split("\n")
    for line in lines[1:]:  # skip header
        if not line:
            continue
        parts = line.split(",")
        sample_id = parts[0]
        error_reason = parts[-1]
        if sample_id in expected_reasons:
            assert error_reason == expected_reasons[sample_id], (
                f"Wrong error_reason for '{sample_id}' in '{REJECTED_CSV_PATH}'.\n"
                f"Expected: '{expected_reasons[sample_id]}'\n"
                f"Got:      '{error_reason}'"
            )


def test_rejected_csv_contains_only_invalid_rows():
    """Ensure no valid sample IDs appear in the rejected file."""
    valid_ids = {"s001", "s002", "s008", "s010"}
    with open(REJECTED_CSV_PATH, "r", newline="") as f:
        lines = f.read().split("\n")
    for line in lines[1:]:  # skip header
        if not line:
            continue
        sample_id = line.split(",")[0]
        assert sample_id not in valid_ids, (
            f"Valid sample '{sample_id}' found in rejected file '{REJECTED_CSV_PATH}'. "
            "Only invalid rows should appear in the rejected file."
        )


def test_rejected_csv_original_values_preserved():
    """Spot-check that original field values are not reformatted."""
    with open(REJECTED_CSV_PATH, "r", newline="") as f:
        lines = f.read().split("\n")
    # s003 should have empty feature1 field preserved
    s003_line = next((l for l in lines if l.startswith("s003,")), None)
    assert s003_line is not None, (
        f"Row for s003 not found in '{REJECTED_CSV_PATH}'."
    )
    assert s003_line.startswith("s003,,3.1,0,"), (
        f"Original values for s003 not preserved in '{REJECTED_CSV_PATH}'.\n"
        f"Got: '{s003_line}'"
    )
    # s009 should have empty label field preserved
    s009_line = next((l for l in lines if l.startswith("s009,")), None)
    assert s009_line is not None, (
        f"Row for s009 not found in '{REJECTED_CSV_PATH}'."
    )
    assert s009_line.startswith("s009,5.5,5.5,,"), (
        f"Original values for s009 not preserved in '{REJECTED_CSV_PATH}'.\n"
        f"Got: '{s009_line}'"
    )


# ── Cross-file consistency ─────────────────────────────────────────────────────

def test_all_input_rows_accounted_for():
    """Every data row from the raw file must appear in exactly one output file."""
    with open(RAW_CSV_PATH, "r", newline="") as f:
        raw_lines = f.read().split("\n")
    # Collect raw sample IDs (skip header, skip empty)
    raw_ids = set()
    for line in raw_lines[1:]:
        if line:
            raw_ids.add(line.split(",")[0])

    with open(CLEAN_CSV_PATH, "r", newline="") as f:
        clean_lines = f.read().split("\n")
    clean_ids = {l.split(",")[0] for l in clean_lines[1:] if l}

    with open(REJECTED_CSV_PATH, "r", newline="") as f:
        rej_lines = f.read().split("\n")
    rej_ids = {l.split(",")[0] for l in rej_lines[1:] if l}

    # No overlap
    overlap = clean_ids & rej_ids
    assert not overlap, (
        f"These sample IDs appear in BOTH output files: {overlap}. "
        "Each row must go to exactly one file."
    )

    # Union equals raw
    all_output_ids = clean_ids | rej_ids
    missing = raw_ids - all_output_ids
    assert not missing, (
        f"These sample IDs from the raw file are missing from both outputs: {missing}."
    )

    extra = all_output_ids - raw_ids
    assert not extra, (
        f"These sample IDs appear in outputs but not in the raw file: {extra}."
    )