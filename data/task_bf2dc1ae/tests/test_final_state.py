# test_final_state.py

import os
import pytest

CSV_PATH = "/home/user/etl/schemas/orders_pipeline.csv"
DOCS_DIR = "/home/user/etl/docs"
MD_PATH = "/home/user/etl/docs/orders_pipeline.md"
ROW_COUNT_PATH = "/home/user/etl/docs/row_count.txt"
LINT_RESULT_PATH = "/home/user/etl/docs/lint_result.txt"

EXPECTED_MD_CONTENT = """\
# orders Pipeline Documentation

## Overview

Pipeline: orders  
Source: PostgreSQL  
Destination: BigQuery  
Owner: data-eng-team  

## Schema

| Field Name | Data Type | Nullable | Description |
|---|---|---|---|
| order_id | INTEGER | NO | Unique identifier for the order |
| customer_id | INTEGER | NO | Foreign key to the customers table |
| order_date | TIMESTAMP | NO | Date and time the order was placed |
| status | STRING | NO | Current status of the order |
| total_amount | FLOAT | YES | Total monetary value of the order |
| discount_code | STRING | YES | Promotional discount code applied |

## Notes

- Schema version: 1.0
- Last updated: 2024-01-15
- Do not modify this file manually; it is generated from the schema CSV.
"""

EXPECTED_ROW_COUNT = "6"
EXPECTED_LINT_RESULT = "LINT PASSED: all 8 table lines are properly closed"


# ---------------------------------------------------------------------------
# docs directory
# ---------------------------------------------------------------------------

def test_docs_directory_exists():
    assert os.path.isdir(DOCS_DIR), (
        f"The docs directory '{DOCS_DIR}' does not exist. "
        "It must be created as part of the task."
    )


# ---------------------------------------------------------------------------
# orders_pipeline.md – existence and readability
# ---------------------------------------------------------------------------

def test_markdown_file_exists():
    assert os.path.isfile(MD_PATH), (
        f"The Markdown documentation file '{MD_PATH}' does not exist. "
        "It must be created as part of the task."
    )


def test_markdown_file_is_readable():
    assert os.access(MD_PATH, os.R_OK), (
        f"The Markdown file '{MD_PATH}' exists but is not readable."
    )


# ---------------------------------------------------------------------------
# orders_pipeline.md – exact content
# ---------------------------------------------------------------------------

def test_markdown_file_exact_content():
    with open(MD_PATH, "r") as fh:
        actual = fh.read()
    assert actual == EXPECTED_MD_CONTENT, (
        "The content of '{}' does not match the expected content.\n\n"
        "--- EXPECTED ---\n{}\n\n"
        "--- ACTUAL ---\n{}".format(MD_PATH, EXPECTED_MD_CONTENT, actual)
    )


def test_markdown_title_line():
    with open(MD_PATH, "r") as fh:
        lines = fh.readlines()
    assert lines[0].rstrip("\n") == "# orders Pipeline Documentation", (
        f"First line of '{MD_PATH}' is wrong.\n"
        f"Expected: '# orders Pipeline Documentation'\n"
        f"Got:      '{lines[0].rstrip(chr(10))}'"
    )


def test_markdown_overview_section():
    with open(MD_PATH, "r") as fh:
        content = fh.read()
    expected_block = (
        "## Overview\n\n"
        "Pipeline: orders  \n"
        "Source: PostgreSQL  \n"
        "Destination: BigQuery  \n"
        "Owner: data-eng-team  \n"
    )
    assert expected_block in content, (
        f"The Overview section in '{MD_PATH}' is missing or incorrectly formatted.\n"
        f"Expected block:\n{expected_block}"
    )


def test_markdown_schema_table_header():
    with open(MD_PATH, "r") as fh:
        content = fh.read()
    assert "| Field Name | Data Type | Nullable | Description |" in content, (
        f"The table header row '| Field Name | Data Type | Nullable | Description |' "
        f"is missing from '{MD_PATH}'."
    )
    assert "|---|---|---|---|" in content, (
        f"The table separator row '|---|---|---|---|' is missing from '{MD_PATH}'."
    )


def test_markdown_data_rows_present():
    expected_rows = [
        "| order_id | INTEGER | NO | Unique identifier for the order |",
        "| customer_id | INTEGER | NO | Foreign key to the customers table |",
        "| order_date | TIMESTAMP | NO | Date and time the order was placed |",
        "| status | STRING | NO | Current status of the order |",
        "| total_amount | FLOAT | YES | Total monetary value of the order |",
        "| discount_code | STRING | YES | Promotional discount code applied |",
    ]
    with open(MD_PATH, "r") as fh:
        content = fh.read()
    for row in expected_rows:
        assert row in content, (
            f"Expected table row not found in '{MD_PATH}':\n  {row}"
        )


def test_markdown_data_rows_order():
    expected_rows = [
        "| order_id | INTEGER | NO | Unique identifier for the order |",
        "| customer_id | INTEGER | NO | Foreign key to the customers table |",
        "| order_date | TIMESTAMP | NO | Date and time the order was placed |",
        "| status | STRING | NO | Current status of the order |",
        "| total_amount | FLOAT | YES | Total monetary value of the order |",
        "| discount_code | STRING | YES | Promotional discount code applied |",
    ]
    with open(MD_PATH, "r") as fh:
        content = fh.read()
    positions = [content.index(row) for row in expected_rows]
    assert positions == sorted(positions), (
        f"The data rows in '{MD_PATH}' are not in the expected order.\n"
        f"Expected order:\n" + "\n".join(expected_rows)
    )


def test_markdown_notes_section():
    with open(MD_PATH, "r") as fh:
        content = fh.read()
    expected_notes = (
        "## Notes\n\n"
        "- Schema version: 1.0\n"
        "- Last updated: 2024-01-15\n"
        "- Do not modify this file manually; it is generated from the schema CSV."
    )
    assert expected_notes in content, (
        f"The Notes section in '{MD_PATH}' is missing or incorrectly formatted.\n"
        f"Expected block:\n{expected_notes}"
    )


def test_markdown_blank_line_before_notes():
    with open(MD_PATH, "r") as fh:
        lines = fh.readlines()
    # Find the line index of "## Notes"
    notes_idx = None
    for i, line in enumerate(lines):
        if line.rstrip("\n") == "## Notes":
            notes_idx = i
            break
    assert notes_idx is not None, (
        f"'## Notes' heading not found in '{MD_PATH}'."
    )
    assert notes_idx >= 1 and lines[notes_idx - 1].strip() == "", (
        f"There must be a blank line immediately before '## Notes' in '{MD_PATH}'.\n"
        f"Line before '## Notes' (index {notes_idx - 1}): "
        f"'{lines[notes_idx - 1].rstrip(chr(10))}'"
    )


# ---------------------------------------------------------------------------
# row_count.txt
# ---------------------------------------------------------------------------

def test_row_count_file_exists():
    assert os.path.isfile(ROW_COUNT_PATH), (
        f"The row count file '{ROW_COUNT_PATH}' does not exist. "
        "It must be created as part of the task."
    )


def test_row_count_file_content():
    with open(ROW_COUNT_PATH, "r") as fh:
        actual = fh.read().strip()
    assert actual == EXPECTED_ROW_COUNT, (
        f"Content of '{ROW_COUNT_PATH}' is incorrect.\n"
        f"Expected: '{EXPECTED_ROW_COUNT}'\n"
        f"Got:      '{actual}'"
    )


def test_row_count_is_integer():
    with open(ROW_COUNT_PATH, "r") as fh:
        raw = fh.read().strip()
    try:
        value = int(raw)
    except ValueError:
        pytest.fail(
            f"Content of '{ROW_COUNT_PATH}' is not a valid integer: '{raw}'"
        )
    assert value == 6, (
        f"Row count in '{ROW_COUNT_PATH}' should be 6, but got {value}."
    )


# ---------------------------------------------------------------------------
# lint_result.txt
# ---------------------------------------------------------------------------

def test_lint_result_file_exists():
    assert os.path.isfile(LINT_RESULT_PATH), (
        f"The lint result file '{LINT_RESULT_PATH}' does not exist. "
        "It must be created as part of the task."
    )


def test_lint_result_file_content():
    with open(LINT_RESULT_PATH, "r") as fh:
        actual = fh.read().strip()
    assert actual == EXPECTED_LINT_RESULT, (
        f"Content of '{LINT_RESULT_PATH}' is incorrect.\n"
        f"Expected: '{EXPECTED_LINT_RESULT}'\n"
        f"Got:      '{actual}'"
    )


def test_lint_result_reports_passed():
    with open(LINT_RESULT_PATH, "r") as fh:
        actual = fh.read().strip()
    assert actual.startswith("LINT PASSED"), (
        f"Lint result in '{LINT_RESULT_PATH}' does not start with 'LINT PASSED'.\n"
        f"Got: '{actual}'"
    )


def test_lint_result_correct_line_count():
    with open(LINT_RESULT_PATH, "r") as fh:
        actual = fh.read().strip()
    assert "8" in actual, (
        f"Lint result in '{LINT_RESULT_PATH}' should reference 8 pipe-delimited lines.\n"
        f"Got: '{actual}'"
    )


# ---------------------------------------------------------------------------
# Cross-validation: pipe-delimited lines in the MD file actually pass lint
# ---------------------------------------------------------------------------

def test_all_pipe_lines_properly_closed_in_md():
    with open(MD_PATH, "r") as fh:
        lines = fh.readlines()
    pipe_lines = [ln.rstrip("\n") for ln in lines if ln.startswith("|")]
    malformed = [ln for ln in pipe_lines if not ln.endswith("|")]
    assert len(malformed) == 0, (
        f"The following lines in '{MD_PATH}' start with '|' but do NOT end with '|':\n"
        + "\n".join(f"  {ln!r}" for ln in malformed)
    )


def test_total_pipe_lines_count_in_md():
    with open(MD_PATH, "r") as fh:
        lines = fh.readlines()
    pipe_lines = [ln for ln in lines if ln.startswith("|")]
    assert len(pipe_lines) == 8, (
        f"Expected 8 lines starting with '|' in '{MD_PATH}' "
        f"(1 header + 1 separator + 6 data rows), but found {len(pipe_lines)}."
    )


# ---------------------------------------------------------------------------
# Original CSV is untouched
# ---------------------------------------------------------------------------

def test_csv_file_still_intact():
    expected_csv = (
        "field_name,data_type,nullable,description\n"
        "order_id,INTEGER,NO,Unique identifier for the order\n"
        "customer_id,INTEGER,NO,Foreign key to the customers table\n"
        "order_date,TIMESTAMP,NO,Date and time the order was placed\n"
        "status,STRING,NO,Current status of the order\n"
        "total_amount,FLOAT,YES,Total monetary value of the order\n"
        "discount_code,STRING,YES,Promotional discount code applied"
    )
    with open(CSV_PATH, "r") as fh:
        actual = fh.read().strip()
    assert actual == expected_csv.strip(), (
        f"The original CSV file '{CSV_PATH}' has been modified.\n"
        f"Expected:\n{expected_csv.strip()}\n\n"
        f"Got:\n{actual}"
    )