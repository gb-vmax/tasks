# test_final_state.py

import os
import pytest

SALES_PSV = "/home/user/data/sales.psv"
SALES_TOTALS_PSV = "/home/user/data/sales_totals.psv"
SALES_REPORT_TXT = "/home/user/data/sales_report.txt"

EXPECTED_TOTALS_LINES = [
    "West|Alice|Widget|12|54.00",
    "East|Bob|Gadget|7|105.00",
    "North|Carol|Widget|3|13.50",
    "South|Dave|Doohickey|20|175.00",
    "East|Alice|Gadget|5|75.00",
]

EXPECTED_REPORT_LINES = [
    "[West] Alice sold 12 units of Widget for $54.00",
    "[East] Bob sold 7 units of Gadget for $105.00",
    "[North] Carol sold 3 units of Widget for $13.50",
    "[South] Dave sold 20 units of Doohickey for $175.00",
    "[East] Alice sold 5 units of Gadget for $75.00",
    "GRAND TOTAL: $422.50",
]


# ---------------------------------------------------------------------------
# sales_totals.psv tests
# ---------------------------------------------------------------------------

def test_sales_totals_psv_exists():
    assert os.path.isfile(SALES_TOTALS_PSV), (
        f"Expected file '{SALES_TOTALS_PSV}' does not exist. "
        "Step 1 (awk) must produce this file."
    )


def test_sales_totals_psv_is_readable():
    assert os.access(SALES_TOTALS_PSV, os.R_OK), (
        f"File '{SALES_TOTALS_PSV}' exists but is not readable."
    )


def test_sales_totals_psv_no_header():
    with open(SALES_TOTALS_PSV, "r") as f:
        first_line = f.readline().rstrip("\n")
    assert first_line != "REGION|SALESPERSON|PRODUCT|UNITS|UNIT_PRICE", (
        f"'{SALES_TOTALS_PSV}' must NOT contain a header line, "
        f"but the first line is the header: '{first_line}'"
    )


def test_sales_totals_psv_line_count():
    with open(SALES_TOTALS_PSV, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    assert len(lines) == 5, (
        f"'{SALES_TOTALS_PSV}' should have exactly 5 data lines, "
        f"found {len(lines)}."
    )


def test_sales_totals_psv_content():
    with open(SALES_TOTALS_PSV, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    assert len(lines) == len(EXPECTED_TOTALS_LINES), (
        f"'{SALES_TOTALS_PSV}' has {len(lines)} non-empty lines, "
        f"expected {len(EXPECTED_TOTALS_LINES)}."
    )

    for i, (actual, expected) in enumerate(zip(lines, EXPECTED_TOTALS_LINES), start=1):
        assert actual == expected, (
            f"Line {i} of '{SALES_TOTALS_PSV}' does not match.\n"
            f"Expected: '{expected}'\n"
            f"Actual:   '{actual}'"
        )


def test_sales_totals_psv_field_format():
    with open(SALES_TOTALS_PSV, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines, start=1):
        fields = line.split("|")
        assert len(fields) == 5, (
            f"Line {i} of '{SALES_TOTALS_PSV}' should have 5 pipe-delimited fields, "
            f"got {len(fields)}: '{line}'"
        )
        # UNITS should be an integer
        try:
            int(fields[3])
        except ValueError:
            pytest.fail(
                f"Line {i} of '{SALES_TOTALS_PSV}': UNITS field (field 4) should be "
                f"an integer, got '{fields[3]}'"
            )
        # TOTAL should be a float with 2 decimal places
        total_str = fields[4]
        try:
            float(total_str)
        except ValueError:
            pytest.fail(
                f"Line {i} of '{SALES_TOTALS_PSV}': TOTAL field (field 5) should be "
                f"a number, got '{total_str}'"
            )
        assert "." in total_str and len(total_str.split(".")[1]) == 2, (
            f"Line {i} of '{SALES_TOTALS_PSV}': TOTAL field '{total_str}' "
            "should be formatted to exactly 2 decimal places."
        )


def test_sales_totals_psv_computed_values():
    """Verify each computed TOTAL = UNITS * UNIT_PRICE matches expected values."""
    expected_totals = {
        ("West", "Alice", "Widget", "12"): "54.00",
        ("East", "Bob", "Gadget", "7"): "105.00",
        ("North", "Carol", "Widget", "3"): "13.50",
        ("South", "Dave", "Doohickey", "20"): "175.00",
        ("East", "Alice", "Gadget", "5"): "75.00",
    }

    with open(SALES_TOTALS_PSV, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines, start=1):
        fields = line.split("|")
        if len(fields) != 5:
            continue
        key = tuple(fields[:4])
        total = fields[4]
        if key in expected_totals:
            assert total == expected_totals[key], (
                f"Line {i} of '{SALES_TOTALS_PSV}': TOTAL for {key} "
                f"should be '{expected_totals[key]}', got '{total}'"
            )


# ---------------------------------------------------------------------------
# sales_report.txt tests
# ---------------------------------------------------------------------------

def test_sales_report_txt_exists():
    assert os.path.isfile(SALES_REPORT_TXT), (
        f"Expected file '{SALES_REPORT_TXT}' does not exist. "
        "Steps 2 and 3 (sed + awk) must produce this file."
    )


def test_sales_report_txt_is_readable():
    assert os.access(SALES_REPORT_TXT, os.R_OK), (
        f"File '{SALES_REPORT_TXT}' exists but is not readable."
    )


def test_sales_report_txt_line_count():
    with open(SALES_REPORT_TXT, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    assert len(lines) == 6, (
        f"'{SALES_REPORT_TXT}' should have exactly 6 lines "
        f"(5 sales sentences + 1 GRAND TOTAL line), found {len(lines)}."
    )


def test_sales_report_txt_content():
    with open(SALES_REPORT_TXT, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    assert len(lines) == len(EXPECTED_REPORT_LINES), (
        f"'{SALES_REPORT_TXT}' has {len(lines)} non-empty lines, "
        f"expected {len(EXPECTED_REPORT_LINES)}."
    )

    for i, (actual, expected) in enumerate(zip(lines, EXPECTED_REPORT_LINES), start=1):
        assert actual == expected, (
            f"Line {i} of '{SALES_REPORT_TXT}' does not match.\n"
            f"Expected: '{expected}'\n"
            f"Actual:   '{actual}'"
        )


def test_sales_report_txt_sentence_format():
    """Each of the first 5 lines must match the pattern [REGION] NAME sold N units of PRODUCT for $TOTAL"""
    import re
    pattern = re.compile(
        r'^\[.+\] .+ sold \d+ units of .+ for \$\d+\.\d{2}$'
    )
    with open(SALES_REPORT_TXT, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines[:5], start=1):
        assert pattern.match(line), (
            f"Line {i} of '{SALES_REPORT_TXT}' does not match the expected sentence format.\n"
            f"Expected format: '[REGION] SALESPERSON sold UNITS units of PRODUCT for $TOTAL'\n"
            f"Actual:          '{line}'"
        )


def test_sales_report_txt_grand_total_line():
    with open(SALES_REPORT_TXT, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    last_line = lines[-1]
    assert last_line == "GRAND TOTAL: $422.50", (
        f"Last line of '{SALES_REPORT_TXT}' should be 'GRAND TOTAL: $422.50', "
        f"got: '{last_line}'"
    )


def test_sales_report_txt_grand_total_is_last():
    with open(SALES_REPORT_TXT, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    grand_total_indices = [i for i, line in enumerate(lines) if line.startswith("GRAND TOTAL:")]
    assert len(grand_total_indices) == 1, (
        f"'{SALES_REPORT_TXT}' should contain exactly one 'GRAND TOTAL:' line, "
        f"found {len(grand_total_indices)}."
    )
    assert grand_total_indices[0] == len(lines) - 1, (
        f"'GRAND TOTAL:' line should be the last line of '{SALES_REPORT_TXT}', "
        f"but it appears at line index {grand_total_indices[0]} "
        f"(total lines: {len(lines)})."
    )


def test_sales_report_txt_order():
    """Sales sentences must appear in the same order as the original data."""
    expected_sentences = EXPECTED_REPORT_LINES[:5]

    with open(SALES_REPORT_TXT, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    actual_sentences = lines[:5]
    for i, (actual, expected) in enumerate(zip(actual_sentences, expected_sentences), start=1):
        assert actual == expected, (
            f"Sales sentence {i} in '{SALES_REPORT_TXT}' is out of order or incorrect.\n"
            f"Expected: '{expected}'\n"
            f"Actual:   '{actual}'"
        )


def test_sales_report_txt_exact_full_content():
    """Verify the complete file content matches exactly."""
    expected_content = "\n".join(EXPECTED_REPORT_LINES) + "\n"

    with open(SALES_REPORT_TXT, "r") as f:
        actual_content = f.read()

    # Normalize: strip trailing whitespace from each line, then compare
    actual_lines = [line.rstrip() for line in actual_content.splitlines()]
    expected_lines = [line.rstrip() for line in expected_content.splitlines()]

    # Remove trailing empty lines
    while actual_lines and not actual_lines[-1]:
        actual_lines.pop()
    while expected_lines and not expected_lines[-1]:
        expected_lines.pop()

    assert actual_lines == expected_lines, (
        f"Full content of '{SALES_REPORT_TXT}' does not match expected.\n"
        f"Expected lines:\n" + "\n".join(f"  {i+1}: '{l}'" for i, l in enumerate(expected_lines)) +
        f"\n\nActual lines:\n" + "\n".join(f"  {i+1}: '{l}'" for i, l in enumerate(actual_lines))
    )


# ---------------------------------------------------------------------------
# Cross-validation: totals file feeds report correctly
# ---------------------------------------------------------------------------

def test_cross_validation_totals_match_report():
    """Each line in sales_totals.psv should correspond to a sentence in sales_report.txt."""
    with open(SALES_TOTALS_PSV, "r") as f:
        total_lines = [line.rstrip("\n") for line in f if line.strip()]

    with open(SALES_REPORT_TXT, "r") as f:
        report_lines = [line.rstrip("\n") for line in f if line.strip()]

    # There should be one report sentence per total line
    report_sentences = report_lines[:-1]  # exclude GRAND TOTAL line

    assert len(total_lines) == len(report_sentences), (
        f"Number of lines in '{SALES_TOTALS_PSV}' ({len(total_lines)}) "
        f"does not match number of sentences in '{SALES_REPORT_TXT}' "
        f"({len(report_sentences)})."
    )

    for i, (total_line, sentence) in enumerate(zip(total_lines, report_sentences), start=1):
        fields = total_line.split("|")
        if len(fields) != 5:
            continue
        region, salesperson, product, units, total = fields
        expected_sentence = (
            f"[{region}] {salesperson} sold {units} units of {product} for ${total}"
        )
        assert sentence == expected_sentence, (
            f"Report sentence {i} does not match the corresponding totals line.\n"
            f"Totals line:       '{total_line}'\n"
            f"Expected sentence: '{expected_sentence}'\n"
            f"Actual sentence:   '{sentence}'"
        )