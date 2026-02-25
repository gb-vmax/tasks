# test_final_state.py

import os
import pytest

BUILD_LOGS_DIR = "/home/user/build_logs"
PIPELINE_LOG = os.path.join(BUILD_LOGS_DIR, "pipeline.log")
PIPELINE_ERRORS = os.path.join(BUILD_LOGS_DIR, "pipeline_errors.txt")
EXTRACTION_SUMMARY = os.path.join(BUILD_LOGS_DIR, "extraction_summary.txt")

EXPECTED_ERROR_LINES = [
    "[ERROR] Failed to clone repository\n",
    "[ERROR] Compilation failed due to missing dependency\n",
]

EXPECTED_PIPELINE_ERRORS_CONTENT = "".join(EXPECTED_ERROR_LINES)

EXPECTED_EXTRACTION_SUMMARY_CONTENT = (
    "Total ERROR lines extracted: 2\n"
    "First ERROR line: [ERROR] Failed to clone repository\n"
)

def test_pipeline_errors_file_exists():
    assert os.path.isfile(PIPELINE_ERRORS), (
        f"{PIPELINE_ERRORS} does not exist. "
        "You must create this file containing the lines with 'ERROR' from pipeline.log."
    )

def test_pipeline_errors_content_exact():
    with open(PIPELINE_ERRORS, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_PIPELINE_ERRORS_CONTENT, (
        f"{PIPELINE_ERRORS} does not contain the exact expected ERROR lines.\n"
        "Expected content:\n"
        f"{EXPECTED_PIPELINE_ERRORS_CONTENT!r}\n"
        "Found:\n"
        f"{content!r}\n"
        "Check that only the lines containing 'ERROR' are present, in the original order, and that there are no extra or missing lines."
    )

def test_extraction_summary_file_exists():
    assert os.path.isfile(EXTRACTION_SUMMARY), (
        f"{EXTRACTION_SUMMARY} does not exist. "
        "You must create this file summarizing the ERROR extraction."
    )

def test_extraction_summary_content_exact():
    with open(EXTRACTION_SUMMARY, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_EXTRACTION_SUMMARY_CONTENT, (
        f"{EXTRACTION_SUMMARY} does not match the expected summary format or content.\n"
        "Expected content:\n"
        f"{EXPECTED_EXTRACTION_SUMMARY_CONTENT!r}\n"
        "Found:\n"
        f"{content!r}\n"
        "Ensure the summary format, counts, and first ERROR line are exactly as specified, with no extra whitespace or lines."
    )

def test_pipeline_errors_no_extra_lines():
    """Extra robust: Ensure only the expected lines are present and no more."""
    with open(PIPELINE_ERRORS, "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert lines == EXPECTED_ERROR_LINES, (
        f"{PIPELINE_ERRORS} contains unexpected lines.\n"
        f"Expected lines:\n{EXPECTED_ERROR_LINES}\n"
        f"Found lines:\n{lines}\n"
        "Check for extra, missing, or reordered lines."
    )

def test_extraction_summary_format_and_values():
    """Extra robust: Parse summary and check values."""
    with open(EXTRACTION_SUMMARY, "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) == 2, (
        f"{EXTRACTION_SUMMARY} should have exactly 2 lines, found {len(lines)} lines."
    )
    total_line = lines[0].strip()
    first_line = lines[1].strip()

    assert total_line.startswith("Total ERROR lines extracted: "), (
        f"First line of {EXTRACTION_SUMMARY} should start with 'Total ERROR lines extracted: '.\n"
        f"Found: {total_line}"
    )
    try:
        extracted_count = int(total_line.split(": ", 1)[1])
    except Exception:
        pytest.fail(
            f"Could not parse the count from the first line of {EXTRACTION_SUMMARY}. Found: {total_line}"
        )
    assert extracted_count == len(EXPECTED_ERROR_LINES), (
        f"Summary count ({extracted_count}) does not match actual number of ERROR lines ({len(EXPECTED_ERROR_LINES)})."
    )

    assert first_line.startswith("First ERROR line: "), (
        f"Second line of {EXTRACTION_SUMMARY} should start with 'First ERROR line: '.\n"
        f"Found: {first_line}"
    )
    first_error_line = first_line[len("First ERROR line: "):]
    expected_first = EXPECTED_ERROR_LINES[0].rstrip('\n')
    assert first_error_line == expected_first, (
        f"The 'First ERROR line' in summary is incorrect.\n"
        f"Expected: {expected_first!r}\n"
        f"Found: {first_error_line!r}\n"
        "Make sure you use the exact first ERROR line as it appears in pipeline.log."
    )