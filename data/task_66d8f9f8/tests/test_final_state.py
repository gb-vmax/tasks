# test_final_state.py

import os
import pytest

OUTPUT_FILE = "/home/user/metrics/high_latency.txt"
SOURCE_FILE = "/home/user/metrics/service_latency.txt"

EXPECTED_LINES = [
    "SERVICE\tENV\tP99\tRATIO",
    "billing-service\tprod\t450\t18.0",
    "payment-service\tprod\t310\t10.3",
    "search-service\tstg\t210\t14.0",
    "auth-service\tprod\t120\t10.0",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES)


def read_output_file():
    with open(OUTPUT_FILE, "r") as f:
        return f.read()


def test_output_file_exists():
    assert os.path.isfile(OUTPUT_FILE), (
        f"Output file '{OUTPUT_FILE}' does not exist. "
        "The task requires creating this file with awk and sed transformations."
    )


def test_output_file_is_readable():
    assert os.access(OUTPUT_FILE, os.R_OK), (
        f"Output file '{OUTPUT_FILE}' exists but is not readable."
    )


def test_output_file_line_count():
    content = read_output_file()
    lines = content.strip().splitlines()
    assert len(lines) == 5, (
        f"Expected exactly 5 lines in '{OUTPUT_FILE}' (1 header + 4 data lines), "
        f"but found {len(lines)} lines.\n"
        f"Actual content:\n{content}"
    )


def test_output_file_header():
    content = read_output_file()
    first_line = content.splitlines()[0]
    expected_header = "SERVICE\tENV\tP99\tRATIO"
    assert first_line == expected_header, (
        f"Header line in '{OUTPUT_FILE}' is incorrect.\n"
        f"Expected: {repr(expected_header)}\n"
        f"Actual:   {repr(first_line)}"
    )


def test_output_file_tab_separated():
    content = read_output_file()
    lines = content.strip().splitlines()
    for i, line in enumerate(lines):
        fields = line.split("\t")
        assert len(fields) == 4, (
            f"Line {i+1} in '{OUTPUT_FILE}' does not have exactly 4 tab-separated fields.\n"
            f"Line: {repr(line)}\n"
            f"Fields found: {fields}"
        )


def test_output_file_no_production_string():
    content = read_output_file()
    assert "production" not in content, (
        f"The word 'production' still appears in '{OUTPUT_FILE}'. "
        "The sed step should have replaced 'production' with 'prod'.\n"
        f"Actual content:\n{content}"
    )


def test_output_file_no_staging_string():
    content = read_output_file()
    assert "staging" not in content, (
        f"The word 'staging' still appears in '{OUTPUT_FILE}'. "
        "The sed step should have replaced 'staging' with 'stg'.\n"
        f"Actual content:\n{content}"
    )


def test_output_file_data_line_billing_service():
    content = read_output_file()
    lines = content.strip().splitlines()
    expected_line = "billing-service\tprod\t450\t18.0"
    assert lines[1] == expected_line, (
        f"Line 2 (billing-service) in '{OUTPUT_FILE}' is incorrect.\n"
        f"Expected: {repr(expected_line)}\n"
        f"Actual:   {repr(lines[1])}"
    )


def test_output_file_data_line_payment_service():
    content = read_output_file()
    lines = content.strip().splitlines()
    expected_line = "payment-service\tprod\t310\t10.3"
    assert lines[2] == expected_line, (
        f"Line 3 (payment-service) in '{OUTPUT_FILE}' is incorrect.\n"
        f"Expected: {repr(expected_line)}\n"
        f"Actual:   {repr(lines[2])}"
    )


def test_output_file_data_line_search_service():
    content = read_output_file()
    lines = content.strip().splitlines()
    expected_line = "search-service\tstg\t210\t14.0"
    assert lines[3] == expected_line, (
        f"Line 4 (search-service) in '{OUTPUT_FILE}' is incorrect.\n"
        f"Expected: {repr(expected_line)}\n"
        f"Actual:   {repr(lines[3])}"
    )


def test_output_file_data_line_auth_service():
    content = read_output_file()
    lines = content.strip().splitlines()
    expected_line = "auth-service\tprod\t120\t10.0"
    assert lines[4] == expected_line, (
        f"Line 5 (auth-service) in '{OUTPUT_FILE}' is incorrect.\n"
        f"Expected: {repr(expected_line)}\n"
        f"Actual:   {repr(lines[4])}"
    )


def test_output_file_sorted_by_p99_descending():
    content = read_output_file()
    lines = content.strip().splitlines()
    data_lines = lines[1:]  # skip header
    p99_values = []
    for i, line in enumerate(data_lines):
        fields = line.split("\t")
        assert len(fields) == 4, (
            f"Data line {i+2} does not have 4 tab-separated fields: {repr(line)}"
        )
        try:
            p99 = int(fields[2])
        except ValueError:
            pytest.fail(
                f"P99 value on data line {i+2} is not an integer: {repr(fields[2])}\n"
                f"Line: {repr(line)}"
            )
        p99_values.append(p99)

    assert p99_values == sorted(p99_values, reverse=True), (
        f"Data lines in '{OUTPUT_FILE}' are not sorted by P99 descending.\n"
        f"P99 values found: {p99_values}\n"
        f"Expected order: {sorted(p99_values, reverse=True)}"
    )


def test_output_file_only_high_latency_services():
    """Only services with p99_ms > 100 should appear."""
    content = read_output_file()
    lines = content.strip().splitlines()
    data_lines = lines[1:]
    service_names = [line.split("\t")[0] for line in data_lines]

    # Services that should NOT appear (p99 <= 100)
    excluded_services = ["cart-service", "user-service", "notification-service"]
    for svc in excluded_services:
        assert svc not in service_names, (
            f"Service '{svc}' should NOT appear in '{OUTPUT_FILE}' "
            f"because its p99_ms is not greater than 100.\n"
            f"Services found: {service_names}"
        )

    # Services that SHOULD appear (p99 > 100)
    included_services = ["auth-service", "payment-service", "search-service", "billing-service"]
    for svc in included_services:
        assert svc in service_names, (
            f"Service '{svc}' should appear in '{OUTPUT_FILE}' "
            f"because its p99_ms is greater than 100.\n"
            f"Services found: {service_names}"
        )


def test_output_file_ratio_values():
    """Check that ratio values are correctly computed and rounded to 1 decimal place."""
    content = read_output_file()
    lines = content.strip().splitlines()
    data_lines = lines[1:]

    expected_ratios = {
        "billing-service": "18.0",
        "payment-service": "10.3",
        "search-service": "14.0",
        "auth-service": "10.0",
    }

    for line in data_lines:
        fields = line.split("\t")
        assert len(fields) == 4, f"Line does not have 4 fields: {repr(line)}"
        service = fields[0]
        ratio = fields[3]
        if service in expected_ratios:
            assert ratio == expected_ratios[service], (
                f"Ratio for '{service}' in '{OUTPUT_FILE}' is incorrect.\n"
                f"Expected: {repr(expected_ratios[service])}\n"
                f"Actual:   {repr(ratio)}"
            )


def test_output_file_exact_content():
    """Final check: the entire file content must match exactly."""
    content = read_output_file()
    actual = content.strip()
    assert actual == EXPECTED_CONTENT, (
        f"The content of '{OUTPUT_FILE}' does not match the expected output.\n"
        f"Expected:\n{EXPECTED_CONTENT}\n\n"
        f"Actual:\n{actual}\n\n"
        f"Expected (repr): {repr(EXPECTED_CONTENT)}\n"
        f"Actual   (repr): {repr(actual)}"
    )


def test_source_file_unchanged():
    """The original source file should remain unmodified."""
    expected_source = (
        "service_name|environment|p50_ms|p95_ms|p99_ms\n"
        "auth-service|production|12|45|120\n"
        "payment-service|production|30|95|310\n"
        "cart-service|staging|8|22|55\n"
        "user-service|production|20|60|95\n"
        "search-service|staging|15|80|210\n"
        "notification-service|staging|5|18|88\n"
        "billing-service|production|25|110|450"
    )
    with open(SOURCE_FILE, "r") as f:
        actual = f.read().strip()
    assert actual == expected_source, (
        f"The source file '{SOURCE_FILE}' has been modified unexpectedly.\n"
        f"Expected:\n{expected_source}\n\n"
        f"Actual:\n{actual}"
    )