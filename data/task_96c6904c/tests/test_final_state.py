# test_final_state.py

import os
import pytest

TRAIN_READY_FILE = "/home/user/data/train_ready.csv"

EXPECTED_HEADER = "id,feat_a,feat_b,feat_c,target"

EXPECTED_CONTENT = """id,feat_a,feat_b,feat_c,target
S001,0.12,0.87,0.45,1
S003,0.55,1.20,0.88,1
S005,0.81,0.45,0.63,0
S007,0.68,0.33,0.91,1
S009,0.09,0.52,0.38,0"""

EXPECTED_DATA_ROWS = [
    "S001,0.12,0.87,0.45,1",
    "S003,0.55,1.20,0.88,1",
    "S005,0.81,0.45,0.63,0",
    "S007,0.68,0.33,0.91,1",
    "S009,0.09,0.52,0.38,0",
]


def read_lines():
    """Read the output file and return non-empty lines."""
    with open(TRAIN_READY_FILE, "r") as f:
        return [line.rstrip("\n") for line in f.readlines()]


def test_output_file_exists():
    assert os.path.isfile(TRAIN_READY_FILE), (
        f"Output file not found: {TRAIN_READY_FILE}. "
        "The transformation has not been run yet."
    )


def test_output_file_is_readable():
    assert os.access(TRAIN_READY_FILE, os.R_OK), (
        f"Output file is not readable: {TRAIN_READY_FILE}"
    )


def test_output_file_exact_content():
    with open(TRAIN_READY_FILE, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_CONTENT, (
        f"Output file content does not match expected.\n"
        f"Expected:\n{EXPECTED_CONTENT}\n\n"
        f"Got:\n{content}"
    )


def test_output_file_header():
    lines = read_lines()
    assert len(lines) >= 1, "Output file is empty — no header found."
    assert lines[0] == EXPECTED_HEADER, (
        f"Header line mismatch.\n"
        f"Expected: {EXPECTED_HEADER!r}\n"
        f"Got:      {lines[0]!r}"
    )


def test_output_file_line_count():
    lines = [l for l in read_lines() if l.strip()]
    assert len(lines) == 6, (
        f"Expected 6 lines (1 header + 5 data rows), got {len(lines)}.\n"
        f"Lines found: {lines}"
    )


def test_no_blank_lines():
    with open(TRAIN_READY_FILE, "r") as f:
        all_lines = f.readlines()
    blank_lines = [i + 1 for i, l in enumerate(all_lines) if l.strip() == ""]
    assert not blank_lines, (
        f"Found blank lines at line numbers: {blank_lines}. "
        "The output must have no blank lines."
    )


def test_no_trailing_whitespace():
    with open(TRAIN_READY_FILE, "r") as f:
        all_lines = f.readlines()
    offending = []
    for i, line in enumerate(all_lines):
        stripped = line.rstrip("\n")
        if stripped != stripped.rstrip():
            offending.append((i + 1, repr(stripped)))
    assert not offending, (
        f"Found trailing whitespace on the following lines: {offending}"
    )


def test_data_rows_content():
    lines = [l for l in read_lines() if l.strip()]
    data_rows = lines[1:]  # skip header
    assert data_rows == EXPECTED_DATA_ROWS, (
        f"Data rows do not match expected.\n"
        f"Expected: {EXPECTED_DATA_ROWS}\n"
        f"Got:      {data_rows}"
    )


def test_only_train_rows_included():
    """Verify that only sample IDs from the train split are present."""
    lines = [l for l in read_lines() if l.strip()]
    data_rows = lines[1:]
    expected_ids = {"S001", "S003", "S005", "S007", "S009"}
    excluded_ids = {"S002", "S004", "S006", "S008", "S010"}
    found_ids = {row.split(",")[0] for row in data_rows}

    assert found_ids == expected_ids, (
        f"Sample IDs in output do not match expected train IDs.\n"
        f"Expected: {sorted(expected_ids)}\n"
        f"Found:    {sorted(found_ids)}"
    )

    for exc_id in excluded_ids:
        assert exc_id not in found_ids, (
            f"Non-train sample {exc_id!r} should not appear in the output "
            f"but was found."
        )


def test_labels_are_numeric():
    """Verify that labels have been converted from strings to 0/1."""
    lines = [l for l in read_lines() if l.strip()]
    data_rows = lines[1:]
    for row in data_rows:
        parts = row.split(",")
        assert len(parts) == 5, (
            f"Row does not have exactly 5 columns: {row!r}"
        )
        label = parts[4]
        assert label in ("0", "1"), (
            f"Label column must be '0' or '1', got {label!r} in row: {row!r}. "
            "Ensure 'positive' → '1' and 'negative' → '0'."
        )


def test_label_mapping_positive_to_1():
    """S001, S003, S007 had label=positive → should be 1."""
    lines = [l for l in read_lines() if l.strip()]
    data_rows = lines[1:]
    row_map = {row.split(",")[0]: row.split(",")[4] for row in data_rows}

    for sample_id in ("S001", "S003", "S007"):
        assert sample_id in row_map, (
            f"Expected sample {sample_id} to be in output but it was missing."
        )
        assert row_map[sample_id] == "1", (
            f"Sample {sample_id} had label 'positive' in raw data; "
            f"expected target='1' but got {row_map[sample_id]!r}."
        )


def test_label_mapping_negative_to_0():
    """S005, S009 had label=negative → should be 0."""
    lines = [l for l in read_lines() if l.strip()]
    data_rows = lines[1:]
    row_map = {row.split(",")[0]: row.split(",")[4] for row in data_rows}

    for sample_id in ("S005", "S009"):
        assert sample_id in row_map, (
            f"Expected sample {sample_id} to be in output but it was missing."
        )
        assert row_map[sample_id] == "0", (
            f"Sample {sample_id} had label 'negative' in raw data; "
            f"expected target='0' but got {row_map[sample_id]!r}."
        )


def test_split_column_dropped():
    """Verify the split column value does not appear in any data row."""
    lines = [l for l in read_lines() if l.strip()]
    data_rows = lines[1:]
    for row in data_rows:
        parts = row.split(",")
        assert len(parts) == 5, (
            f"Row has {len(parts)} columns instead of 5 — "
            f"the 'split' column may not have been dropped: {row!r}"
        )
        assert "train" not in parts, (
            f"The word 'train' (split column value) still appears in row: {row!r}. "
            "The split column must be dropped."
        )


def test_row_order_preserved():
    """Rows must appear in the same order as in the raw file."""
    lines = [l for l in read_lines() if l.strip()]
    data_rows = lines[1:]
    ids_in_output = [row.split(",")[0] for row in data_rows]
    expected_order = ["S001", "S003", "S005", "S007", "S009"]
    assert ids_in_output == expected_order, (
        f"Row order mismatch.\n"
        f"Expected order: {expected_order}\n"
        f"Got:            {ids_in_output}"
    )


def test_column_count_in_header():
    lines = read_lines()
    assert len(lines) >= 1, "Output file is empty."
    header_cols = lines[0].split(",")
    assert len(header_cols) == 5, (
        f"Header must have exactly 5 columns, got {len(header_cols)}: {lines[0]!r}"
    )


def test_header_column_names():
    lines = read_lines()
    assert len(lines) >= 1, "Output file is empty."
    header_cols = lines[0].split(",")
    expected_cols = ["id", "feat_a", "feat_b", "feat_c", "target"]
    assert header_cols == expected_cols, (
        f"Header column names mismatch.\n"
        f"Expected: {expected_cols}\n"
        f"Got:      {header_cols}"
    )


def test_raw_file_unchanged():
    """The raw source file must not have been modified."""
    RAW_FILE = "/home/user/data/raw_samples.csv"
    EXPECTED_RAW = (
        "sample_id,feature_a,feature_b,feature_c,label,split\n"
        "S001,0.12,0.87,0.45,positive,train\n"
        "S002,0.93,0.11,0.76,negative,test\n"
        "S003,0.55,1.20,0.88,positive,train\n"
        "S004,0.37,0.64,0.29,negative,val\n"
        "S005,0.81,0.45,0.63,negative,train\n"
        "S006,0.22,0.99,0.14,positive,test\n"
        "S007,0.68,0.33,0.91,positive,train\n"
        "S008,0.44,0.77,0.55,negative,val\n"
        "S009,0.09,0.52,0.38,negative,train\n"
        "S010,0.76,0.18,0.82,positive,test"
    )
    assert os.path.isfile(RAW_FILE), f"Raw file missing: {RAW_FILE}"
    with open(RAW_FILE, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_RAW, (
        f"Raw file has been modified! Its content no longer matches the original.\n"
        f"Expected:\n{EXPECTED_RAW}\n\nGot:\n{content}"
    )