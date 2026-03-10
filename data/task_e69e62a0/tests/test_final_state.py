# test_final_state.py

import os
import pytest

INPUT_FILE = "/home/user/profiling/cpu_profile.tsv"
OUTPUT_FILE = "/home/user/profiling/summary.tsv"

EXPECTED_HEADER = ["function_name", "total_time_us", "self_time_us", "call_count"]

EXPECTED_ROWS = [
    ["render_frame", "1310400", "987600", "4200"],
    ["parse_input", "850500", "850500", "18900"],
    ["load_texture", "954000", "721000", "530"],
    ["update_physics", "1155000", "634000", "4200"],
    ["audio_mix", "823200", "823200", "8400"],
    ["compress_data", "882000", "441000", "210"],
]


def test_profiling_directory_exists():
    dirpath = "/home/user/profiling"
    assert os.path.isdir(dirpath), (
        f"Directory '{dirpath}' does not exist. "
        "The profiling directory must be present."
    )


def test_input_file_still_exists():
    assert os.path.isfile(INPUT_FILE), (
        f"Input file '{INPUT_FILE}' no longer exists. "
        "The original cpu_profile.tsv must not be removed or modified."
    )


def test_summary_file_exists():
    assert os.path.isfile(OUTPUT_FILE), (
        f"Output file '{OUTPUT_FILE}' does not exist. "
        "The summary.tsv must be created by the task."
    )


def test_summary_file_is_readable():
    assert os.access(OUTPUT_FILE, os.R_OK), (
        f"Output file '{OUTPUT_FILE}' is not readable."
    )


def test_summary_file_header():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, (
        f"Output file '{OUTPUT_FILE}' is empty; expected at least a header row."
    )

    header_fields = lines[0].split("\t")
    assert header_fields == EXPECTED_HEADER, (
        f"Header mismatch in '{OUTPUT_FILE}'.\n"
        f"  Expected: {EXPECTED_HEADER}\n"
        f"  Got:      {header_fields}"
    )


def test_summary_file_row_count():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    non_empty = [l for l in lines if l.strip()]

    assert len(non_empty) == 7, (
        f"Expected 7 non-empty lines (1 header + 6 data rows) in '{OUTPUT_FILE}', "
        f"but found {len(non_empty)}."
    )


def test_summary_file_data_rows():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    non_empty = [l for l in lines if l.strip()]
    data_lines = non_empty[1:]  # skip header

    assert len(data_lines) == len(EXPECTED_ROWS), (
        f"Expected {len(EXPECTED_ROWS)} data rows in '{OUTPUT_FILE}', "
        f"but found {len(data_lines)}."
    )

    for i, (actual_line, expected_fields) in enumerate(zip(data_lines, EXPECTED_ROWS), start=1):
        actual_fields = actual_line.split("\t")
        assert actual_fields == expected_fields, (
            f"Row {i} mismatch in '{OUTPUT_FILE}'.\n"
            f"  Expected fields: {expected_fields}\n"
            f"  Got fields:      {actual_fields}\n"
            f"  Raw line: {actual_line!r}"
        )


def test_summary_file_uses_tab_delimiters():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    for i, line in enumerate(lines):
        if not line.strip():
            continue
        assert "\t" in line, (
            f"Line {i+1} in '{OUTPUT_FILE}' does not contain a tab delimiter: {line!r}"
        )


def test_summary_file_no_trailing_whitespace():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    for i, line in enumerate(lines):
        assert line == line.rstrip(), (
            f"Line {i+1} in '{OUTPUT_FILE}' has trailing whitespace: {line!r}"
        )


def test_summary_file_ends_with_newline():
    with open(OUTPUT_FILE, "rb") as f:
        content = f.read()

    assert content.endswith(b"\n"), (
        f"Output file '{OUTPUT_FILE}' does not end with a newline character."
    )


def test_summary_file_no_extra_blank_lines():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    blank_lines = [i + 1 for i, l in enumerate(lines) if l.strip() == ""]

    assert len(blank_lines) == 0, (
        f"Output file '{OUTPUT_FILE}' contains unexpected blank lines at line numbers: "
        f"{blank_lines}"
    )


def test_summary_file_column_order():
    """Explicitly verify that the columns are in the correct order."""
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    non_empty = [l for l in lines if l.strip()]
    header = non_empty[0].split("\t")

    assert len(header) == 4, (
        f"Expected exactly 4 columns in header of '{OUTPUT_FILE}', "
        f"but found {len(header)}: {header}"
    )

    assert header[0] == "function_name", (
        f"Column 1 should be 'function_name', got '{header[0]}'"
    )
    assert header[1] == "total_time_us", (
        f"Column 2 should be 'total_time_us', got '{header[1]}'"
    )
    assert header[2] == "self_time_us", (
        f"Column 3 should be 'self_time_us', got '{header[2]}'"
    )
    assert header[3] == "call_count", (
        f"Column 4 should be 'call_count', got '{header[3]}'"
    )


def test_summary_file_excludes_dropped_columns():
    """Verify that 'module' and 'avg_latency_us' are not present in the output."""
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    non_empty = [l for l in lines if l.strip()]
    header = non_empty[0].split("\t")

    assert "module" not in header, (
        f"Column 'module' should have been dropped from '{OUTPUT_FILE}', "
        f"but it is still present in the header: {header}"
    )
    assert "avg_latency_us" not in header, (
        f"Column 'avg_latency_us' should have been dropped from '{OUTPUT_FILE}', "
        f"but it is still present in the header: {header}"
    )


def test_summary_file_row_order_matches_input():
    """Verify that the row order in summary.tsv matches the original cpu_profile.tsv."""
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        input_lines = f.read().splitlines()

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        output_lines = f.read().splitlines()

    input_data = [l for l in input_lines if l.strip()][1:]  # skip header
    output_data = [l for l in output_lines if l.strip()][1:]  # skip header

    input_function_names = [l.split("\t")[0] for l in input_data]
    output_function_names = [l.split("\t")[0] for l in output_data]

    assert input_function_names == output_function_names, (
        f"Row order in '{OUTPUT_FILE}' does not match '{INPUT_FILE}'.\n"
        f"  Input order:  {input_function_names}\n"
        f"  Output order: {output_function_names}"
    )


def test_summary_file_exact_content():
    """Verify the complete exact content of the summary file."""
    expected_lines = [
        "function_name\ttotal_time_us\tself_time_us\tcall_count",
        "render_frame\t1310400\t987600\t4200",
        "parse_input\t850500\t850500\t18900",
        "load_texture\t954000\t721000\t530",
        "update_physics\t1155000\t634000\t4200",
        "audio_mix\t823200\t823200\t8400",
        "compress_data\t882000\t441000\t210",
    ]
    expected_content = "\n".join(expected_lines) + "\n"

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        actual_content = f.read()

    assert actual_content == expected_content, (
        f"Content of '{OUTPUT_FILE}' does not match expected.\n"
        f"  Expected:\n{expected_content!r}\n"
        f"  Got:\n{actual_content!r}"
    )