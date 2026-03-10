# test_final_state.py

import os
import pytest

REPAIR_REPORT_PATH = "/home/user/observability/repair_report.txt"
OBSERVABILITY_DIR = "/home/user/observability"

EXPECTED_LINES = [
    "[NEEDS REPAIR] memory-pressure | status=error | threshold=70",
    "[NEEDS REPAIR] disk-io | status=ok | threshold=MISSING",
    "[NEEDS REPAIR] network-latency | status=error | threshold=MISSING",
    "[NEEDS REPAIR] error-budget | status=error | threshold=10",
    "[NEEDS REPAIR] pod-restarts | status=ok | threshold=MISSING",
    "",
    "Total dashboards needing repair: 5",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES)


def test_observability_directory_exists():
    assert os.path.isdir(OBSERVABILITY_DIR), (
        f"Directory '{OBSERVABILITY_DIR}' does not exist. "
        "The observability directory must be present."
    )


def test_repair_report_exists():
    assert os.path.isfile(REPAIR_REPORT_PATH), (
        f"Repair report file '{REPAIR_REPORT_PATH}' does not exist. "
        "The student must generate this file as part of the task."
    )


def test_repair_report_is_readable():
    assert os.access(REPAIR_REPORT_PATH, os.R_OK), (
        f"Repair report file '{REPAIR_REPORT_PATH}' is not readable."
    )


def test_repair_report_not_empty():
    size = os.path.getsize(REPAIR_REPORT_PATH)
    assert size > 0, (
        f"Repair report file '{REPAIR_REPORT_PATH}' is empty. "
        "It must contain the repair entries and summary."
    )


def _read_report():
    with open(REPAIR_REPORT_PATH, "r") as f:
        return f.read()


def test_repair_report_has_correct_number_of_dashboard_lines():
    content = _read_report()
    lines = content.splitlines()
    dashboard_lines = [l for l in lines if l.startswith("[NEEDS REPAIR]")]
    assert len(dashboard_lines) == 5, (
        f"Expected 5 '[NEEDS REPAIR]' lines in '{REPAIR_REPORT_PATH}', "
        f"but found {len(dashboard_lines)}.\n"
        f"Lines found: {dashboard_lines}"
    )


def test_repair_report_memory_pressure_line():
    content = _read_report()
    expected = "[NEEDS REPAIR] memory-pressure | status=error | threshold=70"
    assert expected in content, (
        f"Expected line not found in '{REPAIR_REPORT_PATH}':\n"
        f"  Expected: {expected!r}\n"
        f"  File content:\n{content}"
    )


def test_repair_report_disk_io_line():
    content = _read_report()
    expected = "[NEEDS REPAIR] disk-io | status=ok | threshold=MISSING"
    assert expected in content, (
        f"Expected line not found in '{REPAIR_REPORT_PATH}':\n"
        f"  Expected: {expected!r}\n"
        f"  File content:\n{content}"
    )


def test_repair_report_network_latency_line():
    content = _read_report()
    expected = "[NEEDS REPAIR] network-latency | status=error | threshold=MISSING"
    assert expected in content, (
        f"Expected line not found in '{REPAIR_REPORT_PATH}':\n"
        f"  Expected: {expected!r}\n"
        f"  File content:\n{content}"
    )


def test_repair_report_error_budget_line():
    content = _read_report()
    expected = "[NEEDS REPAIR] error-budget | status=error | threshold=10"
    assert expected in content, (
        f"Expected line not found in '{REPAIR_REPORT_PATH}':\n"
        f"  Expected: {expected!r}\n"
        f"  File content:\n{content}"
    )


def test_repair_report_pod_restarts_line():
    content = _read_report()
    expected = "[NEEDS REPAIR] pod-restarts | status=ok | threshold=MISSING"
    assert expected in content, (
        f"Expected line not found in '{REPAIR_REPORT_PATH}':\n"
        f"  Expected: {expected!r}\n"
        f"  File content:\n{content}"
    )


def test_repair_report_no_ok_dashboards_included():
    """Dashboards that are ok and have threshold should NOT appear in the report."""
    content = _read_report()
    for name in ["cpu-usage", "request-rate", "db-connections"]:
        assert name not in content, (
            f"Dashboard '{name}' should NOT appear in '{REPAIR_REPORT_PATH}' "
            f"because it has status=ok and a threshold present. "
            f"But it was found in the report."
        )


def test_repair_report_summary_line():
    content = _read_report()
    expected_summary = "Total dashboards needing repair: 5"
    assert expected_summary in content, (
        f"Summary line not found in '{REPAIR_REPORT_PATH}':\n"
        f"  Expected: {expected_summary!r}\n"
        f"  File content:\n{content}"
    )


def test_repair_report_order_of_entries():
    """Entries must appear in the same order as in dashboards.json."""
    content = _read_report()
    lines = content.splitlines()
    dashboard_lines = [l for l in lines if l.startswith("[NEEDS REPAIR]")]

    expected_names_in_order = [
        "memory-pressure",
        "disk-io",
        "network-latency",
        "error-budget",
        "pod-restarts",
    ]

    actual_names_in_order = []
    for line in dashboard_lines:
        # Extract name from "[NEEDS REPAIR] <name> | ..."
        parts = line.split("|")
        if parts:
            name_part = parts[0].replace("[NEEDS REPAIR]", "").strip()
            actual_names_in_order.append(name_part)

    assert actual_names_in_order == expected_names_in_order, (
        f"Dashboard entries in '{REPAIR_REPORT_PATH}' are not in the expected order.\n"
        f"  Expected order: {expected_names_in_order}\n"
        f"  Actual order:   {actual_names_in_order}"
    )


def test_repair_report_blank_line_before_summary():
    """There must be a blank line between the last dashboard entry and the summary."""
    content = _read_report()
    lines = content.splitlines()

    # Find the index of the summary line
    summary_index = None
    for i, line in enumerate(lines):
        if line.startswith("Total dashboards needing repair:"):
            summary_index = i
            break

    assert summary_index is not None, (
        f"Summary line 'Total dashboards needing repair: ...' not found in '{REPAIR_REPORT_PATH}'."
    )

    assert summary_index >= 1, (
        f"Summary line is at the very beginning of the file; expected it to be preceded by content."
    )

    preceding_line = lines[summary_index - 1]
    assert preceding_line == "", (
        f"Expected a blank line immediately before the summary line in '{REPAIR_REPORT_PATH}', "
        f"but found: {preceding_line!r}"
    )


def test_repair_report_exact_content():
    """The entire file content must match the expected output exactly (ignoring optional trailing newline)."""
    content = _read_report()
    # Strip a single trailing newline if present, since the task says "no trailing newline required"
    content_stripped = content.rstrip("\n")
    expected_stripped = EXPECTED_CONTENT.rstrip("\n")

    assert content_stripped == expected_stripped, (
        f"The content of '{REPAIR_REPORT_PATH}' does not match the expected content.\n"
        f"  Expected:\n{expected_stripped!r}\n\n"
        f"  Actual:\n{content_stripped!r}"
    )