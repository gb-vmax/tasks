# test_final_state.py

import os
import pytest

OUTPUT_FILE = "/home/user/tickets/import_ready.tsv"
TICKETS_DIR = "/home/user/tickets"

EXPECTED_HEADER = ["ticket_id", "customer_email", "priority", "category", "assigned_agent"]

EXPECTED_ROWS = [
    ["TKT-001", "john.doe@example.com", "high", "billing", "alice"],
    ["TKT-002", "sara.smith@example.com", "low", "network", "bob"],
    ["TKT-003", "mike.jones@example.com", "medium", "hardware", "alice"],
    ["TKT-004", "linda.wu@example.com", "high", "software", "carol"],
    ["TKT-005", "raj.patel@example.com", "low", "billing", "bob"],
]


def test_tickets_directory_exists():
    assert os.path.isdir(TICKETS_DIR), (
        f"Directory '{TICKETS_DIR}' does not exist. "
        "The tickets directory must be present."
    )


def test_output_file_exists():
    assert os.path.isfile(OUTPUT_FILE), (
        f"Output file '{OUTPUT_FILE}' does not exist. "
        "The import_ready.tsv file must be created as part of the task."
    )


def test_output_file_is_readable():
    assert os.access(OUTPUT_FILE, os.R_OK), (
        f"Output file '{OUTPUT_FILE}' is not readable."
    )


def test_output_file_line_count():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]

    assert len(non_empty_lines) == 6, (
        f"Expected exactly 6 lines (1 header + 5 data rows) in '{OUTPUT_FILE}', "
        f"but found {len(non_empty_lines)} non-empty lines."
    )


def test_output_file_header():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, (
        f"Output file '{OUTPUT_FILE}' is empty — expected at least a header line."
    )

    header_line = lines[0].rstrip()
    actual_columns = header_line.split("\t")

    assert actual_columns == EXPECTED_HEADER, (
        f"Header mismatch in '{OUTPUT_FILE}'.\n"
        f"Expected: {EXPECTED_HEADER}\n"
        f"Got:      {actual_columns}\n"
        "The header must be exactly: ticket_id<TAB>customer_email<TAB>priority<TAB>category<TAB>assigned_agent"
    )


def test_output_file_is_tab_separated():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    for i, line in enumerate(lines):
        if not line.strip():
            continue
        cols = line.split("\t")
        assert len(cols) == 5, (
            f"Line {i + 1} in '{OUTPUT_FILE}' does not have exactly 5 tab-separated columns.\n"
            f"Line content: {repr(line)}\n"
            f"Columns found: {len(cols)}\n"
            "All lines must be tab-separated with exactly 5 columns."
        )


def test_output_file_data_rows():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # Skip header line
    data_lines = [line for line in lines[1:] if line.strip()]

    assert len(data_lines) == len(EXPECTED_ROWS), (
        f"Expected {len(EXPECTED_ROWS)} data rows in '{OUTPUT_FILE}', "
        f"but found {len(data_lines)}."
    )

    for i, (actual_line, expected_row) in enumerate(zip(data_lines, EXPECTED_ROWS), start=1):
        actual_cols = actual_line.rstrip().split("\t")
        assert actual_cols == expected_row, (
            f"Row {i} mismatch in '{OUTPUT_FILE}'.\n"
            f"Expected: {expected_row}\n"
            f"Got:      {actual_cols}\n"
            "Check that columns are reordered correctly: "
            "ticket_id, customer_email, priority, category, assigned_agent."
        )


def test_output_file_no_trailing_whitespace():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    for i, line in enumerate(lines):
        if not line.strip():
            continue
        assert line == line.rstrip(), (
            f"Line {i + 1} in '{OUTPUT_FILE}' has trailing whitespace.\n"
            f"Line content: {repr(line)}\n"
            "All lines must have no trailing whitespace."
        )


def test_output_file_column_order():
    """Verify that the column order matches the required new order exactly."""
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, f"Output file '{OUTPUT_FILE}' is empty."

    header_cols = lines[0].rstrip().split("\t")

    expected_order = ["ticket_id", "customer_email", "priority", "category", "assigned_agent"]
    assert header_cols == expected_order, (
        f"Column order is incorrect in '{OUTPUT_FILE}'.\n"
        f"Expected order: {expected_order}\n"
        f"Got order:      {header_cols}\n"
        "Columns must be: ticket_id, customer_email, priority, category, assigned_agent"
    )


def test_output_file_dropped_columns():
    """Verify that created_date and status columns are not present."""
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, f"Output file '{OUTPUT_FILE}' is empty."

    header_cols = lines[0].rstrip().split("\t")

    assert "created_date" not in header_cols, (
        f"Column 'created_date' should have been dropped from '{OUTPUT_FILE}', "
        f"but it is still present in the header: {header_cols}"
    )

    assert "status" not in header_cols, (
        f"Column 'status' should have been dropped from '{OUTPUT_FILE}', "
        f"but it is still present in the header: {header_cols}"
    )


def test_output_file_exact_content():
    """Verify the complete content of the output file matches expected exactly."""
    expected_lines = [
        "ticket_id\tcustomer_email\tpriority\tcategory\tassigned_agent",
        "TKT-001\tjohn.doe@example.com\thigh\tbilling\talice",
        "TKT-002\tsara.smith@example.com\tlow\tnetwork\tbob",
        "TKT-003\tmike.jones@example.com\tmedium\thardware\talice",
        "TKT-004\tlinda.wu@example.com\thigh\tsoftware\tcarol",
        "TKT-005\traj.patel@example.com\tlow\tbilling\tbob",
    ]

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    actual_lines = [line for line in content.splitlines() if line.strip()]

    assert len(actual_lines) == len(expected_lines), (
        f"Expected {len(expected_lines)} non-empty lines in '{OUTPUT_FILE}', "
        f"but found {len(actual_lines)}."
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, expected_lines)):
        assert actual.rstrip() == expected, (
            f"Line {i + 1} content mismatch in '{OUTPUT_FILE}'.\n"
            f"Expected: {repr(expected)}\n"
            f"Got:      {repr(actual.rstrip())}"
        )


def test_original_file_unchanged():
    """Verify the original open_tickets.tsv file was not modified."""
    INPUT_FILE = "/home/user/tickets/open_tickets.tsv"

    assert os.path.isfile(INPUT_FILE), (
        f"Original file '{INPUT_FILE}' no longer exists — it should not have been deleted."
    )

    expected_header = ["ticket_id", "assigned_agent", "priority", "created_date", "category", "status", "customer_email"]

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, f"Original file '{INPUT_FILE}' is empty."

    actual_header = lines[0].rstrip().split("\t")
    assert actual_header == expected_header, (
        f"Original file '{INPUT_FILE}' header has been modified.\n"
        f"Expected: {expected_header}\n"
        f"Got:      {actual_header}\n"
        "The original file should remain unchanged."
    )