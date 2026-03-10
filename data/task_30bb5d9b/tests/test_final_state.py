# test_final_state.py

import os
import pytest

ALERT_CFG = "/home/user/monitoring/alert_thresholds.cfg"
METRICS_CSV = "/home/user/monitoring/metrics.csv"

EXPECTED_CONTENT = (
    "[dbserver01:cpu_usage]\n"
    "max=55.0\n"
    "avg=45.0\n"
    "threshold=47.0\n"
    "\n"
    "[dbserver01:disk_io]\n"
    "max=200.0\n"
    "avg=160.0\n"
    "threshold=168.0\n"
    "\n"
    "[webserver01:cpu_usage]\n"
    "max=75.0\n"
    "avg=60.0\n"
    "threshold=63.0\n"
    "\n"
    "[webserver01:mem_usage]\n"
    "max=91.0\n"
    "avg=77.0\n"
    "threshold=79.8"
)


def test_alert_cfg_exists():
    assert os.path.isfile(ALERT_CFG), (
        f"Output file '{ALERT_CFG}' does not exist. "
        "The student's solution must create this file."
    )


def test_alert_cfg_is_readable():
    assert os.access(ALERT_CFG, os.R_OK), (
        f"File '{ALERT_CFG}' is not readable. "
        "Please ensure the file has appropriate read permissions."
    )


def test_alert_cfg_exact_content():
    with open(ALERT_CFG, "r") as f:
        actual = f.read()

    assert actual == EXPECTED_CONTENT, (
        f"Content of '{ALERT_CFG}' does not match expected content.\n\n"
        f"--- EXPECTED (repr) ---\n{repr(EXPECTED_CONTENT)}\n\n"
        f"--- ACTUAL (repr) ---\n{repr(actual)}\n\n"
        f"--- EXPECTED ---\n{EXPECTED_CONTENT}\n\n"
        f"--- ACTUAL ---\n{actual}"
    )


def test_alert_cfg_no_trailing_newline():
    with open(ALERT_CFG, "rb") as f:
        raw = f.read()

    assert not raw.endswith(b"\n"), (
        f"File '{ALERT_CFG}' must NOT end with a trailing newline, "
        f"but it does. Last bytes: {repr(raw[-5:])}"
    )


def test_alert_cfg_sections_present():
    with open(ALERT_CFG, "r") as f:
        content = f.read()

    expected_sections = [
        "[dbserver01:cpu_usage]",
        "[dbserver01:disk_io]",
        "[webserver01:cpu_usage]",
        "[webserver01:mem_usage]",
    ]
    for section in expected_sections:
        assert section in content, (
            f"Section header '{section}' not found in '{ALERT_CFG}'. "
            "All server:metric combinations must be present."
        )


def test_alert_cfg_section_count():
    with open(ALERT_CFG, "r") as f:
        content = f.read()

    section_count = content.count("[")
    assert section_count == 4, (
        f"Expected exactly 4 sections in '{ALERT_CFG}', "
        f"but found {section_count} opening brackets '['."
    )


def test_alert_cfg_sorted_order():
    with open(ALERT_CFG, "r") as f:
        content = f.read()

    lines = content.splitlines()
    section_lines = [line for line in lines if line.startswith("[")]

    expected_order = [
        "[dbserver01:cpu_usage]",
        "[dbserver01:disk_io]",
        "[webserver01:cpu_usage]",
        "[webserver01:mem_usage]",
    ]
    assert section_lines == expected_order, (
        f"Sections are not in the correct sorted order.\n"
        f"Expected order: {expected_order}\n"
        f"Actual order:   {section_lines}"
    )


def test_alert_cfg_dbserver01_cpu_usage_values():
    with open(ALERT_CFG, "r") as f:
        content = f.read()

    # Find the section and verify values
    assert "max=55.0" in content, (
        f"Expected 'max=55.0' for dbserver01:cpu_usage in '{ALERT_CFG}'."
    )
    assert "avg=45.0" in content, (
        f"Expected 'avg=45.0' for dbserver01:cpu_usage in '{ALERT_CFG}'."
    )
    assert "threshold=47.0" in content, (
        f"Expected 'threshold=47.0' for dbserver01:cpu_usage in '{ALERT_CFG}'."
    )


def test_alert_cfg_dbserver01_disk_io_values():
    with open(ALERT_CFG, "r") as f:
        content = f.read()

    assert "max=200.0" in content, (
        f"Expected 'max=200.0' for dbserver01:disk_io in '{ALERT_CFG}'."
    )
    assert "avg=160.0" in content, (
        f"Expected 'avg=160.0' for dbserver01:disk_io in '{ALERT_CFG}'."
    )
    assert "threshold=168.0" in content, (
        f"Expected 'threshold=168.0' for dbserver01:disk_io in '{ALERT_CFG}'."
    )


def test_alert_cfg_webserver01_cpu_usage_values():
    with open(ALERT_CFG, "r") as f:
        content = f.read()

    assert "max=75.0" in content, (
        f"Expected 'max=75.0' for webserver01:cpu_usage in '{ALERT_CFG}'."
    )
    assert "avg=60.0" in content, (
        f"Expected 'avg=60.0' for webserver01:cpu_usage in '{ALERT_CFG}'."
    )
    assert "threshold=63.0" in content, (
        f"Expected 'threshold=63.0' for webserver01:cpu_usage in '{ALERT_CFG}'."
    )


def test_alert_cfg_webserver01_mem_usage_values():
    with open(ALERT_CFG, "r") as f:
        content = f.read()

    assert "max=91.0" in content, (
        f"Expected 'max=91.0' for webserver01:mem_usage in '{ALERT_CFG}'."
    )
    assert "avg=77.0" in content, (
        f"Expected 'avg=77.0' for webserver01:mem_usage in '{ALERT_CFG}'."
    )
    assert "threshold=79.8" in content, (
        f"Expected 'threshold=79.8' for webserver01:mem_usage in '{ALERT_CFG}'."
    )


def test_alert_cfg_blank_line_between_sections():
    with open(ALERT_CFG, "r") as f:
        content = f.read()

    # There should be exactly 3 blank lines (between 4 sections)
    # A blank line is represented as \n\n in the file
    blank_line_count = content.count("\n\n")
    assert blank_line_count == 3, (
        f"Expected exactly 3 blank lines between sections in '{ALERT_CFG}', "
        f"but found {blank_line_count}. "
        "Sections must be separated by a single blank line."
    )


def test_alert_cfg_section_structure():
    """Verify each section has exactly max, avg, threshold keys in order."""
    with open(ALERT_CFG, "r") as f:
        content = f.read()

    # Split into sections by blank lines
    sections = content.split("\n\n")
    assert len(sections) == 4, (
        f"Expected 4 sections separated by blank lines, got {len(sections)}."
    )

    for section in sections:
        lines = section.splitlines()
        assert len(lines) == 4, (
            f"Each section must have exactly 4 lines (header + max + avg + threshold), "
            f"but got {len(lines)} lines in section:\n{section}"
        )
        assert lines[0].startswith("[") and lines[0].endswith("]"), (
            f"First line of section must be a header like '[server:metric]', "
            f"but got: '{lines[0]}'"
        )
        assert lines[1].startswith("max="), (
            f"Second line of section must start with 'max=', "
            f"but got: '{lines[1]}'"
        )
        assert lines[2].startswith("avg="), (
            f"Third line of section must start with 'avg=', "
            f"but got: '{lines[2]}'"
        )
        assert lines[3].startswith("threshold="), (
            f"Fourth line of section must start with 'threshold=', "
            f"but got: '{lines[3]}'"
        )


def test_alert_cfg_section_headers_format():
    """Verify section headers use [server:metric] format with no spaces."""
    with open(ALERT_CFG, "r") as f:
        lines = f.readlines()

    header_lines = [line.strip() for line in lines if line.strip().startswith("[")]
    for header in header_lines:
        assert ":" in header, (
            f"Section header '{header}' must contain a colon ':' separating server and metric."
        )
        assert " " not in header, (
            f"Section header '{header}' must not contain spaces."
        )
        # Should be [server:metric] format
        inner = header[1:-1]
        parts = inner.split(":")
        assert len(parts) == 2, (
            f"Section header '{header}' must be in format '[server:metric]' with exactly one colon."
        )


def test_metrics_csv_still_intact():
    """Ensure the original metrics.csv was not modified."""
    assert os.path.isfile(METRICS_CSV), (
        f"Original metrics CSV '{METRICS_CSV}' is missing after task completion."
    )

    with open(METRICS_CSV, "r") as f:
        first_line = f.readline().strip()

    assert first_line == "server,metric,value", (
        f"The header of '{METRICS_CSV}' appears to have been modified. "
        f"Got: '{first_line}'"
    )