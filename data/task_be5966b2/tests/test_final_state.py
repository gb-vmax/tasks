# test_final_state.py

import os
import pytest

OUTPUT_PATH = "/home/user/ml_data/training_ready.csv"
RAW_CSV_PATH = "/home/user/ml_data/raw_samples.csv"

EXPECTED_CONTENT = (
    "sample_id,feature_a,feature_b,label\n"
    "1,3.400,1.020,dog\n"
    "3,0.512,1.837,cat\n"
    "6,1.111,1.111,cat\n"
    "8,0.761,4.112,cat\n"
    "12,2.871,3.142,cat\n"
    "22,1.847,2.930,dog\n"
)

EXPECTED_LINES = EXPECTED_CONTENT.splitlines()
EXPECTED_HEADER = "sample_id,feature_a,feature_b,label"
EXPECTED_DATA_ROWS = [
    "1,3.400,1.020,dog",
    "3,0.512,1.837,cat",
    "6,1.111,1.111,cat",
    "8,0.761,4.112,cat",
    "12,2.871,3.142,cat",
    "22,1.847,2.930,dog",
]


def test_output_file_exists():
    assert os.path.isfile(OUTPUT_PATH), (
        f"Output file '{OUTPUT_PATH}' does not exist. "
        "The task requires writing the processed CSV to this path."
    )


def test_output_file_is_readable():
    assert os.access(OUTPUT_PATH, os.R_OK), (
        f"Output file '{OUTPUT_PATH}' is not readable."
    )


def test_output_file_exact_content():
    with open(OUTPUT_PATH, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_CONTENT, (
        f"Output file content does not match expected.\n"
        f"Expected (repr): {EXPECTED_CONTENT!r}\n"
        f"Got      (repr): {actual!r}"
    )


def test_output_file_has_trailing_newline():
    with open(OUTPUT_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"Output file '{OUTPUT_PATH}' does not end with a trailing newline. "
        f"Last bytes: {content[-5:]!r}"
    )


def test_output_file_has_no_blank_lines():
    with open(OUTPUT_PATH, "r") as f:
        lines = f.readlines()
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"Output file contains blank lines at line numbers: {blank_lines}. "
        "No blank lines are allowed."
    )


def test_output_file_line_count():
    with open(OUTPUT_PATH, "r") as f:
        content = f.read()
    # Count lines as split by newline, excluding trailing empty string after final \n
    lines = content.split("\n")
    # The trailing newline means the last element after split is ''
    # wc -l counts newline characters, so 7 newlines = 7 lines
    newline_count = content.count("\n")
    assert newline_count == 7, (
        f"Output file should have 7 newline characters (7 lines per wc -l: "
        f"1 header + 6 data rows + trailing newline), but found {newline_count}."
    )


def test_output_file_header():
    with open(OUTPUT_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")
    assert first_line == EXPECTED_HEADER, (
        f"Output file header is incorrect.\n"
        f"Expected: {EXPECTED_HEADER!r}\n"
        f"Got:      {first_line!r}"
    )


def test_output_file_header_has_exactly_four_columns():
    with open(OUTPUT_PATH, "r") as f:
        header = f.readline().rstrip("\n")
    columns = header.split(",")
    assert len(columns) == 4, (
        f"Output file header should have exactly 4 columns, but found {len(columns)}: {columns}"
    )
    assert columns == ["sample_id", "feature_a", "feature_b", "label"], (
        f"Output file header columns are wrong or in wrong order.\n"
        f"Expected: ['sample_id', 'feature_a', 'feature_b', 'label']\n"
        f"Got:      {columns}"
    )


def test_output_file_data_row_count():
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    non_empty = [l for l in lines if l.strip()]
    data_rows = non_empty[1:]  # skip header
    assert len(data_rows) == 6, (
        f"Output file should have exactly 6 data rows, but found {len(data_rows)}.\n"
        f"Data rows found: {data_rows}"
    )


def test_output_file_data_rows_content():
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    non_empty = [l for l in lines if l.strip()]
    data_rows = non_empty[1:]  # skip header
    assert data_rows == EXPECTED_DATA_ROWS, (
        f"Output file data rows do not match expected.\n"
        f"Expected:\n" + "\n".join(EXPECTED_DATA_ROWS) + "\n"
        f"Got:\n" + "\n".join(data_rows)
    )


def test_output_sorted_by_sample_id_ascending():
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    non_empty = [l for l in lines if l.strip()]
    data_rows = non_empty[1:]  # skip header
    sample_ids = []
    for row in data_rows:
        parts = row.split(",")
        assert len(parts) >= 1, f"Row has no columns: {row!r}"
        try:
            sample_ids.append(int(parts[0]))
        except ValueError:
            pytest.fail(f"sample_id is not an integer: {parts[0]!r} in row {row!r}")
    assert sample_ids == sorted(sample_ids), (
        f"Data rows are not sorted by sample_id in ascending order.\n"
        f"Found order: {sample_ids}\n"
        f"Expected order: {sorted(sample_ids)}"
    )


def test_output_correct_sample_ids():
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    non_empty = [l for l in lines if l.strip()]
    data_rows = non_empty[1:]  # skip header
    found_ids = [int(row.split(",")[0]) for row in data_rows]
    expected_ids = [1, 3, 6, 8, 12, 22]
    assert found_ids == expected_ids, (
        f"sample_ids in output do not match expected.\n"
        f"Expected: {expected_ids}\n"
        f"Got:      {found_ids}"
    )


def test_output_excludes_filtered_rows():
    """Rows that failed the filter must not appear in the output."""
    excluded_ids = {5, 7, 10, 15, 19}
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    non_empty = [l for l in lines if l.strip()]
    data_rows = non_empty[1:]  # skip header
    found_ids = {int(row.split(",")[0]) for row in data_rows}
    intersection = found_ids & excluded_ids
    assert not intersection, (
        f"Output file contains rows that should have been filtered out. "
        f"Unexpected sample_ids present: {sorted(intersection)}"
    )


def test_output_excludes_unknown_labels():
    """No row with label 'unknown' should appear in the output."""
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    non_empty = [l for l in lines if l.strip()]
    data_rows = non_empty[1:]  # skip header
    unknown_rows = [row for row in data_rows if row.split(",")[-1] == "unknown"]
    assert not unknown_rows, (
        f"Output file contains rows with label 'unknown', which should be filtered out: "
        f"{unknown_rows}"
    )


def test_output_feature_values_not_reformatted():
    """Feature values must match the source exactly (no rounding/reformatting)."""
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    non_empty = [l for l in lines if l.strip()]
    data_rows = non_empty[1:]  # skip header

    # Build a dict of expected feature values by sample_id
    expected = {
        1:  ("3.400", "1.020"),
        3:  ("0.512", "1.837"),
        6:  ("1.111", "1.111"),
        8:  ("0.761", "4.112"),
        12: ("2.871", "3.142"),
        22: ("1.847", "2.930"),
    }

    for row in data_rows:
        parts = row.split(",")
        assert len(parts) == 4, (
            f"Row does not have exactly 4 columns: {row!r}"
        )
        sid = int(parts[0])
        feat_a, feat_b = parts[1], parts[2]
        exp_a, exp_b = expected[sid]
        assert feat_a == exp_a, (
            f"sample_id={sid}: feature_a value mismatch. "
            f"Expected {exp_a!r}, got {feat_a!r}"
        )
        assert feat_b == exp_b, (
            f"sample_id={sid}: feature_b value mismatch. "
            f"Expected {exp_b!r}, got {feat_b!r}"
        )


def test_raw_csv_file_unchanged():
    """The raw source file must not have been modified."""
    expected_raw = (
        "sample_id,feature_a,feature_b,quality_score,label\n"
        "3,0.512,1.837,0.91,cat\n"
        "7,1.204,0.334,0.60,dog\n"
        "12,2.871,3.142,0.88,cat\n"
        "5,0.099,2.201,0.74,dog\n"
        "19,1.553,0.778,0.77,unknown\n"
        "1,3.400,1.020,0.82,dog\n"
        "8,0.761,4.112,0.95,cat\n"
        "15,2.233,0.541,0.69,cat\n"
        "22,1.847,2.930,0.78,dog\n"
        "10,0.314,0.628,0.80,unknown\n"
        "6,1.111,1.111,0.76,cat\n"
    )
    assert os.path.isfile(RAW_CSV_PATH), (
        f"Raw CSV file '{RAW_CSV_PATH}' no longer exists."
    )
    with open(RAW_CSV_PATH, "r") as f:
        actual = f.read()
    assert actual == expected_raw, (
        f"Raw CSV file has been modified.\n"
        f"Expected (repr): {expected_raw!r}\n"
        f"Got      (repr): {actual!r}"
    )