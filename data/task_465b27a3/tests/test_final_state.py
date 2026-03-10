# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/pipeline/build_report.txt"
PIPELINE_DIR = "/home/user/pipeline"

EXPECTED_REPORT = """\
=== ANDROID BUILD REPORT ===

-- Module Summary --
core: SUCCESS (3420ms)
auth: SUCCESS (1870ms)
payments: FAILED (5210ms)
notifications: SUCCESS (980ms)
analytics: SUCCESS (2650ms)
ui-components: FAILED (4100ms)

-- Build Statistics --
Total modules: 6
Passed: 4
Failed: 2
Total build time: 18230ms
Slowest module: payments (5210ms)
Fastest module: notifications (980ms)

-- Warnings by Module --
analytics: 2 warning(s)
core: 2 warning(s)
auth: 1 warning(s)
notifications: 1 warning(s)
ui-components: 1 warning(s)

-- Errors by Module --
payments: 3 error(s)
auth: 1 error(s)
ui-components: 1 error(s)

-- Action Items --
FAILED modules: payments, ui-components
Total warnings: 7
Total errors: 5"""


def read_report():
    with open(REPORT_PATH, "r") as f:
        return f.read()


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Build report file does not exist: {REPORT_PATH}. "
        "The task requires generating the report at this path."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Build report file is not readable: {REPORT_PATH}"
    )


def test_report_exact_content():
    content = read_report()
    actual = content.strip()
    expected = EXPECTED_REPORT.strip()
    assert actual == expected, (
        f"Build report content does not exactly match expected.\n\n"
        f"=== EXPECTED ===\n{expected}\n\n"
        f"=== ACTUAL ===\n{actual}\n\n"
        f"=== DIFF (first differing line) ===\n"
        + _first_diff(expected.splitlines(), actual.splitlines())
    )


def _first_diff(expected_lines, actual_lines):
    max_lines = max(len(expected_lines), len(actual_lines))
    for i in range(max_lines):
        exp = expected_lines[i] if i < len(expected_lines) else "<missing>"
        act = actual_lines[i] if i < len(actual_lines) else "<missing>"
        if exp != act:
            return f"Line {i+1}:\n  Expected: {repr(exp)}\n  Actual:   {repr(act)}"
    return "No differences found (lengths differ?)"


def test_report_has_header():
    content = read_report()
    assert "=== ANDROID BUILD REPORT ===" in content, (
        "Report is missing the header '=== ANDROID BUILD REPORT ==='"
    )


def test_report_has_module_summary_section():
    content = read_report()
    assert "-- Module Summary --" in content, (
        "Report is missing the '-- Module Summary --' section header"
    )


def test_report_has_build_statistics_section():
    content = read_report()
    assert "-- Build Statistics --" in content, (
        "Report is missing the '-- Build Statistics --' section header"
    )


def test_report_has_warnings_section():
    content = read_report()
    assert "-- Warnings by Module --" in content, (
        "Report is missing the '-- Warnings by Module --' section header"
    )


def test_report_has_errors_section():
    content = read_report()
    assert "-- Errors by Module --" in content, (
        "Report is missing the '-- Errors by Module --' section header"
    )


def test_report_has_action_items_section():
    content = read_report()
    assert "-- Action Items --" in content, (
        "Report is missing the '-- Action Items --' section header"
    )


def test_module_summary_order_and_content():
    content = read_report()
    lines = content.splitlines()

    # Find the Module Summary section
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "-- Module Summary --":
            start = i + 1
            break
    assert start is not None, "Could not find '-- Module Summary --' in report"

    # Collect module summary lines until next section
    summary_lines = []
    for line in lines[start:]:
        if line.startswith("--") or line.startswith("==="):
            break
        if line.strip():
            summary_lines.append(line)

    expected_summary = [
        "core: SUCCESS (3420ms)",
        "auth: SUCCESS (1870ms)",
        "payments: FAILED (5210ms)",
        "notifications: SUCCESS (980ms)",
        "analytics: SUCCESS (2650ms)",
        "ui-components: FAILED (4100ms)",
    ]

    assert summary_lines == expected_summary, (
        f"Module Summary section content/order is wrong.\n"
        f"Expected:\n" + "\n".join(expected_summary) + "\n\n"
        f"Actual:\n" + "\n".join(summary_lines)
    )


def test_build_statistics_total_modules():
    content = read_report()
    assert "Total modules: 6" in content, (
        "Build Statistics: 'Total modules: 6' not found in report. "
        "There are 6 modules in the build log."
    )


def test_build_statistics_passed():
    content = read_report()
    assert "Passed: 4" in content, (
        "Build Statistics: 'Passed: 4' not found in report. "
        "4 modules had SUCCESS status."
    )


def test_build_statistics_failed():
    content = read_report()
    assert "Failed: 2" in content, (
        "Build Statistics: 'Failed: 2' not found in report. "
        "2 modules had FAILED status (payments, ui-components)."
    )


def test_build_statistics_total_build_time():
    content = read_report()
    assert "Total build time: 18230ms" in content, (
        "Build Statistics: 'Total build time: 18230ms' not found in report. "
        "Sum: 3420+1870+5210+980+2650+4100 = 18230"
    )


def test_build_statistics_slowest_module():
    content = read_report()
    assert "Slowest module: payments (5210ms)" in content, (
        "Build Statistics: 'Slowest module: payments (5210ms)' not found. "
        "payments has the highest duration_ms of 5210."
    )


def test_build_statistics_fastest_module():
    content = read_report()
    assert "Fastest module: notifications (980ms)" in content, (
        "Build Statistics: 'Fastest module: notifications (980ms)' not found. "
        "notifications has the lowest duration_ms of 980."
    )


def test_warnings_by_module_order_and_content():
    content = read_report()
    lines = content.splitlines()

    start = None
    for i, line in enumerate(lines):
        if line.strip() == "-- Warnings by Module --":
            start = i + 1
            break
    assert start is not None, "Could not find '-- Warnings by Module --' in report"

    warning_lines = []
    for line in lines[start:]:
        if line.startswith("--") or line.startswith("==="):
            break
        if line.strip():
            warning_lines.append(line)

    expected_warnings = [
        "analytics: 2 warning(s)",
        "core: 2 warning(s)",
        "auth: 1 warning(s)",
        "notifications: 1 warning(s)",
        "ui-components: 1 warning(s)",
    ]

    assert warning_lines == expected_warnings, (
        f"Warnings by Module section is wrong.\n"
        f"Expected (sorted by count desc, then alphabetically):\n"
        + "\n".join(expected_warnings) + "\n\n"
        f"Actual:\n" + "\n".join(warning_lines) + "\n\n"
        "Note: analytics and core both have 2 warnings (alphabetical order), "
        "auth/notifications/ui-components each have 1 warning (alphabetical order)."
    )


def test_errors_by_module_order_and_content():
    content = read_report()
    lines = content.splitlines()

    start = None
    for i, line in enumerate(lines):
        if line.strip() == "-- Errors by Module --":
            start = i + 1
            break
    assert start is not None, "Could not find '-- Errors by Module --' in report"

    error_lines = []
    for line in lines[start:]:
        if line.startswith("--") or line.startswith("==="):
            break
        if line.strip():
            error_lines.append(line)

    expected_errors = [
        "payments: 3 error(s)",
        "auth: 1 error(s)",
        "ui-components: 1 error(s)",
    ]

    assert error_lines == expected_errors, (
        f"Errors by Module section is wrong.\n"
        f"Expected (sorted by count desc, then alphabetically):\n"
        + "\n".join(expected_errors) + "\n\n"
        f"Actual:\n" + "\n".join(error_lines) + "\n\n"
        "Note: payments has 3 errors; auth and ui-components each have 1 error "
        "(alphabetical order for ties)."
    )


def test_action_items_failed_modules():
    content = read_report()
    assert "FAILED modules: payments, ui-components" in content, (
        "Action Items: 'FAILED modules: payments, ui-components' not found. "
        "payments appears before ui-components in the log file."
    )


def test_action_items_total_warnings():
    content = read_report()
    assert "Total warnings: 7" in content, (
        "Action Items: 'Total warnings: 7' not found. "
        "core=2, auth=1, notifications=1, analytics=2, ui-components=1 → total=7"
    )


def test_action_items_total_errors():
    content = read_report()
    assert "Total errors: 5" in content, (
        "Action Items: 'Total errors: 5' not found. "
        "auth=1, payments=3, ui-components=1 → total=5"
    )


def test_no_trailing_spaces_on_any_line():
    content = read_report()
    lines = content.splitlines()
    offending = [(i + 1, repr(line)) for i, line in enumerate(lines) if line != line.rstrip()]
    assert not offending, (
        f"Report has trailing spaces on the following lines:\n"
        + "\n".join(f"  Line {lineno}: {line}" for lineno, line in offending)
    )


def test_section_separation_blank_lines():
    """Verify there is exactly one blank line between sections."""
    content = read_report()
    lines = content.splitlines()

    section_headers = [
        "-- Module Summary --",
        "-- Build Statistics --",
        "-- Warnings by Module --",
        "-- Errors by Module --",
        "-- Action Items --",
    ]

    header_indices = []
    for i, line in enumerate(lines):
        if line.strip() in section_headers:
            header_indices.append(i)

    assert len(header_indices) == 5, (
        f"Expected 5 section headers, found {len(header_indices)}"
    )

    # Between consecutive section headers, the last non-empty line of the
    # previous section and the header of the next section should be separated
    # by exactly one blank line.
    for idx in range(1, len(header_indices)):
        prev_header = header_indices[idx - 1]
        curr_header = header_indices[idx]

        # Find the last non-blank line before curr_header
        last_content_line = None
        for j in range(curr_header - 1, prev_header, -1):
            if lines[j].strip():
                last_content_line = j
                break

        if last_content_line is not None:
            # There should be exactly one blank line between last_content_line and curr_header
            lines_between = lines[last_content_line + 1: curr_header]
            blank_count = sum(1 for l in lines_between if not l.strip())
            non_blank_between = [l for l in lines_between if l.strip()]
            assert blank_count == 1 and not non_blank_between, (
                f"Expected exactly one blank line between section ending at line "
                f"{last_content_line + 1} and section header at line {curr_header + 1}. "
                f"Found {blank_count} blank line(s) and {len(non_blank_between)} non-blank line(s) between them."
            )


def test_report_line_count():
    """The expected report has a specific number of lines."""
    content = read_report()
    actual_lines = content.strip().splitlines()
    expected_lines = EXPECTED_REPORT.strip().splitlines()
    assert len(actual_lines) == len(expected_lines), (
        f"Report has {len(actual_lines)} lines, expected {len(expected_lines)} lines.\n"
        f"Expected line count breakdown:\n"
        f"  Header: 1, blank: 1\n"
        f"  Module Summary header + 6 modules + blank: 8\n"
        f"  Build Statistics header + 6 stats + blank: 8\n"
        f"  Warnings header + 5 warnings + blank: 7\n"
        f"  Errors header + 3 errors + blank: 5\n"
        f"  Action Items header + 3 items: 4\n"
        f"  Total: {len(expected_lines)}"
    )