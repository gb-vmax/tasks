# test_final_state.py

import os
import re
import stat
import hashlib
import pytest

PIPELINE_DIR = "/home/user/pipeline"
PROCESS_SH = "/home/user/pipeline/process.sh"
REPORT_PATH = "/home/user/pipeline/benchmark_report.txt"

EXPECTED_PROCESS_SH_CONTENT = """\
#!/bin/bash
# Simulate a lightweight data processing step
total=0
for i in $(seq 1 5000); do
    total=$((total + i))
done
echo "processed: $total" > /dev/null
"""


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def read_report_lines():
    """Read the report file and return a list of lines (stripped of trailing newline)."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()
    return content.splitlines()


# ---------------------------------------------------------------------------
# Tests: process.sh must be unmodified
# ---------------------------------------------------------------------------

class TestProcessShUnmodified:
    def test_process_sh_exists(self):
        assert os.path.isfile(PROCESS_SH), (
            f"'{PROCESS_SH}' does not exist. The original script must still be present."
        )

    def test_process_sh_is_executable(self):
        assert os.access(PROCESS_SH, os.X_OK), (
            f"'{PROCESS_SH}' is not executable. It must remain executable."
        )

    def test_process_sh_content_unmodified(self):
        with open(PROCESS_SH, "r") as f:
            content = f.read()
        actual_lines = [line.rstrip() for line in content.splitlines()]
        expected_lines = [line.rstrip() for line in EXPECTED_PROCESS_SH_CONTENT.splitlines()]
        assert actual_lines == expected_lines, (
            f"Content of '{PROCESS_SH}' has been modified.\n"
            f"Expected:\n{EXPECTED_PROCESS_SH_CONTENT}\n"
            f"Actual:\n{content}"
        )

    def test_process_sh_checksum(self):
        with open(PROCESS_SH, "rb") as f:
            raw = f.read()
        expected_bytes = EXPECTED_PROCESS_SH_CONTENT.encode("utf-8")
        expected_hash = hashlib.sha256(expected_bytes).hexdigest()

        actual_normalized = raw.decode("utf-8").replace("\r\n", "\n")
        if not actual_normalized.endswith("\n"):
            actual_normalized += "\n"
        actual_hash = hashlib.sha256(actual_normalized.encode("utf-8")).hexdigest()

        assert actual_hash == expected_hash, (
            f"Checksum mismatch for '{PROCESS_SH}'. The file has been modified.\n"
            f"Expected sha256: {expected_hash}\n"
            f"Actual sha256:   {actual_hash}"
        )


# ---------------------------------------------------------------------------
# Tests: benchmark_report.txt existence and structure
# ---------------------------------------------------------------------------

class TestReportExists:
    def test_report_file_exists(self):
        assert os.path.isfile(REPORT_PATH), (
            f"Report file '{REPORT_PATH}' does not exist. "
            "The benchmark must be run and the report written."
        )

    def test_report_is_not_empty(self):
        assert os.path.getsize(REPORT_PATH) > 0, (
            f"Report file '{REPORT_PATH}' is empty."
        )


class TestReportLineCount:
    def test_exactly_five_lines(self):
        lines = read_report_lines()
        assert len(lines) == 5, (
            f"Report must have exactly 5 lines, but found {len(lines)}.\n"
            f"Lines: {lines}"
        )

    def test_no_trailing_blank_lines(self):
        with open(REPORT_PATH, "r") as f:
            content = f.read()
        # File should end with exactly one newline (5 newline-terminated lines)
        assert content.endswith("\n"), (
            "Report file must end with a newline character."
        )
        assert not content.endswith("\n\n"), (
            "Report file must not have trailing blank lines."
        )


# ---------------------------------------------------------------------------
# Tests: exact content of each line
# ---------------------------------------------------------------------------

class TestReportLineContent:
    def test_line1_benchmark(self):
        lines = read_report_lines()
        assert lines[0] == "benchmark: process.sh", (
            f"Line 1 must be exactly 'benchmark: process.sh', got: {lines[0]!r}"
        )

    def test_line2_runs(self):
        lines = read_report_lines()
        assert lines[1] == "runs: 10", (
            f"Line 2 must be exactly 'runs: 10', got: {lines[1]!r}"
        )

    def test_line3_min_format(self):
        lines = read_report_lines()
        pattern = r"^min: [0-9]+\.[0-9]{3}s$"
        assert re.match(pattern, lines[2]), (
            f"Line 3 must match '{pattern}', got: {lines[2]!r}"
        )

    def test_line4_max_format(self):
        lines = read_report_lines()
        pattern = r"^max: [0-9]+\.[0-9]{3}s$"
        assert re.match(pattern, lines[3]), (
            f"Line 4 must match '{pattern}', got: {lines[3]!r}"
        )

    def test_line5_avg_format(self):
        lines = read_report_lines()
        pattern = r"^avg: [0-9]+\.[0-9]{3}s$"
        assert re.match(pattern, lines[4]), (
            f"Line 5 must match '{pattern}', got: {lines[4]!r}"
        )

    def test_no_trailing_spaces_on_any_line(self):
        lines = read_report_lines()
        for i, line in enumerate(lines, start=1):
            assert line == line.rstrip(), (
                f"Line {i} has trailing whitespace: {line!r}"
            )


# ---------------------------------------------------------------------------
# Tests: numeric value semantics
# ---------------------------------------------------------------------------

def _parse_value(line_prefix, lines):
    """Extract float value from a line like 'min: 0.043s'."""
    for line in lines:
        if line.startswith(line_prefix):
            # Strip prefix and trailing 's'
            value_str = line[len(line_prefix):].rstrip("s")
            return float(value_str)
    raise ValueError(f"Could not find line starting with '{line_prefix}' in report.")


class TestReportValues:
    def test_min_greater_than_zero(self):
        lines = read_report_lines()
        min_val = _parse_value("min: ", lines)
        assert min_val > 0.0, (
            f"min value must be > 0.000s (the script must actually run), got: {min_val:.3f}s"
        )

    def test_max_greater_than_zero(self):
        lines = read_report_lines()
        max_val = _parse_value("max: ", lines)
        assert max_val > 0.0, (
            f"max value must be > 0.000s (the script must actually run), got: {max_val:.3f}s"
        )

    def test_avg_greater_than_zero(self):
        lines = read_report_lines()
        avg_val = _parse_value("avg: ", lines)
        assert avg_val > 0.0, (
            f"avg value must be > 0.000s (the script must actually run), got: {avg_val:.3f}s"
        )

    def test_min_less_than_60_seconds(self):
        lines = read_report_lines()
        min_val = _parse_value("min: ", lines)
        assert min_val < 60.0, (
            f"min value must be < 60.000s (sanity bound for trivial script), got: {min_val:.3f}s"
        )

    def test_max_less_than_60_seconds(self):
        lines = read_report_lines()
        max_val = _parse_value("max: ", lines)
        assert max_val < 60.0, (
            f"max value must be < 60.000s (sanity bound for trivial script), got: {max_val:.3f}s"
        )

    def test_avg_less_than_60_seconds(self):
        lines = read_report_lines()
        avg_val = _parse_value("avg: ", lines)
        assert avg_val < 60.0, (
            f"avg value must be < 60.000s (sanity bound for trivial script), got: {avg_val:.3f}s"
        )

    def test_min_lte_avg(self):
        lines = read_report_lines()
        min_val = _parse_value("min: ", lines)
        avg_val = _parse_value("avg: ", lines)
        assert min_val <= avg_val, (
            f"min ({min_val:.3f}s) must be <= avg ({avg_val:.3f}s). "
            "Monotonicity check failed — values may be incorrect."
        )

    def test_avg_lte_max(self):
        lines = read_report_lines()
        avg_val = _parse_value("avg: ", lines)
        max_val = _parse_value("max: ", lines)
        assert avg_val <= max_val, (
            f"avg ({avg_val:.3f}s) must be <= max ({max_val:.3f}s). "
            "Monotonicity check failed — values may be incorrect."
        )

    def test_min_lte_max(self):
        lines = read_report_lines()
        min_val = _parse_value("min: ", lines)
        max_val = _parse_value("max: ", lines)
        assert min_val <= max_val, (
            f"min ({min_val:.3f}s) must be <= max ({max_val:.3f}s). "
            "This is a fundamental invariant — values are likely incorrect."
        )

    def test_values_have_exactly_3_decimal_places(self):
        """Verify each value string has exactly 3 decimal digits."""
        lines = read_report_lines()
        for prefix in ("min: ", "max: ", "avg: "):
            for line in lines:
                if line.startswith(prefix):
                    value_str = line[len(prefix):].rstrip("s")
                    parts = value_str.split(".")
                    assert len(parts) == 2 and len(parts[1]) == 3, (
                        f"Value in '{line}' must have exactly 3 decimal places, "
                        f"got: {value_str!r}"
                    )