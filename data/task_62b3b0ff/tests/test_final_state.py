# test_final_state.py

import os
import pytest

REPORT_FILE = "/home/user/registry/deprecated_report.txt"
MANIFEST_FILE = "/home/user/registry/image_manifest.tsv"

EM_DASH = "\u2014"

EXPECTED_SERVICE_LINES = [
    f"[DEPRECATED] auth-service (v2.1.0) uses debian:stretch {EM_DASH} pushed by alice",
    f"[DEPRECATED] notification-service (v4.2.0) uses debian:stretch {EM_DASH} pushed by eve",
    f"[DEPRECATED] session-service (v1.1.1) uses ubuntu:18.04 {EM_DASH} pushed by alice",
    f"[DEPRECATED] user-service (v1.0.3) uses ubuntu:18.04 {EM_DASH} pushed by bob",
]

EXPECTED_SUMMARY_LINE = "Total deprecated images: 4"

EXPECTED_CONTENT = (
    "\n".join(EXPECTED_SERVICE_LINES)
    + "\n"
    + "\n"
    + EXPECTED_SUMMARY_LINE
    + "\n"
)

NON_DEPRECATED_SERVICES = [
    "payment-service",
    "gateway-service",
    "order-service",
    "inventory-service",
]


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file '{REPORT_FILE}' does not exist. "
        "The task requires creating this file with deprecated image entries."
    )


def test_report_file_readable():
    assert os.access(REPORT_FILE, os.R_OK), (
        f"Report file '{REPORT_FILE}' is not readable. "
        "Check file permissions."
    )


def test_report_file_exact_content():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    assert content == EXPECTED_CONTENT, (
        f"Content of '{REPORT_FILE}' does not match expected.\n"
        f"Expected:\n{EXPECTED_CONTENT!r}\n"
        f"Got:\n{content!r}"
    )


def test_report_file_line_count():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) == 6, (
        f"Expected exactly 6 lines in '{REPORT_FILE}' "
        f"(4 service lines, 1 blank line, 1 summary line), "
        f"but found {len(lines)} lines.\n"
        f"Lines: {lines!r}"
    )


def test_report_service_lines_content():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    service_lines = [line.rstrip("\n") for line in lines[:4]]

    assert service_lines == EXPECTED_SERVICE_LINES, (
        f"The first 4 lines of '{REPORT_FILE}' do not match expected service lines.\n"
        f"Expected:\n{EXPECTED_SERVICE_LINES!r}\n"
        f"Got:\n{service_lines!r}"
    )


def test_report_blank_line():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) >= 5, (
        f"'{REPORT_FILE}' has fewer than 5 lines; cannot check blank line."
    )

    blank_line = lines[4].rstrip("\n")
    assert blank_line == "", (
        f"Line 5 (index 4) of '{REPORT_FILE}' should be a blank line, "
        f"but got: {blank_line!r}"
    )


def test_report_summary_line():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) >= 6, (
        f"'{REPORT_FILE}' has fewer than 6 lines; cannot check summary line."
    )

    summary_line = lines[5].rstrip("\n")
    assert summary_line == EXPECTED_SUMMARY_LINE, (
        f"Line 6 (index 5) of '{REPORT_FILE}' should be the summary line.\n"
        f"Expected: {EXPECTED_SUMMARY_LINE!r}\n"
        f"Got: {summary_line!r}"
    )


def test_report_uses_em_dash():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    assert EM_DASH in content, (
        f"'{REPORT_FILE}' does not contain the em dash character (U+2014). "
        "Make sure to use ' \u2014 ' (space, em dash, space) and not a regular hyphen."
    )

    # Also ensure no regular hyphen is used as separator (e.g., " - " pattern)
    # The format should be " — " not " - "
    service_lines_content = "\n".join(EXPECTED_SERVICE_LINES)
    for line in EXPECTED_SERVICE_LINES:
        assert line in content, (
            f"Expected line not found in report:\n{line!r}\n"
            f"Report content:\n{content!r}"
        )


def test_report_sorted_alphabetically():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    service_lines = [line.rstrip("\n") for line in lines[:4]]

    expected_order = [
        "auth-service",
        "notification-service",
        "session-service",
        "user-service",
    ]

    for i, (line, expected_service) in enumerate(zip(service_lines, expected_order)):
        assert expected_service in line, (
            f"Line {i + 1} of '{REPORT_FILE}' should contain '{expected_service}' "
            f"(sorted alphabetically), but got:\n{line!r}"
        )


def test_report_does_not_contain_non_deprecated_services():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    for service in NON_DEPRECATED_SERVICES:
        assert service not in content, (
            f"Service '{service}' should NOT appear in '{REPORT_FILE}' "
            "because it does not use a deprecated base image, "
            f"but it was found in the report."
        )


def test_report_deprecated_prefix_on_all_service_lines():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    service_lines = [line.rstrip("\n") for line in lines[:4]]

    for i, line in enumerate(service_lines):
        assert line.startswith("[DEPRECATED] "), (
            f"Line {i + 1} of '{REPORT_FILE}' should start with '[DEPRECATED] ', "
            f"but got:\n{line!r}"
        )


def test_report_format_uses_parentheses_for_tag():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    service_lines = [line.rstrip("\n") for line in lines[:4]]

    for i, line in enumerate(service_lines):
        # Check that image tag is enclosed in parentheses
        assert "(" in line and ")" in line, (
            f"Line {i + 1} of '{REPORT_FILE}' should have the image tag in parentheses, "
            f"but got:\n{line!r}"
        )


def test_report_contains_correct_count():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    assert "Total deprecated images: 4" in content, (
        f"'{REPORT_FILE}' should contain 'Total deprecated images: 4', "
        f"but it was not found.\nReport content:\n{content!r}"
    )


def test_manifest_file_still_intact():
    """Ensure the original manifest file was not modified."""
    EXPECTED_TSV_CONTENT = (
        "auth-service\tv2.1.0\tdebian:stretch\talice\t142\n"
        "payment-service\tv3.0.1\tubuntu:20.04\tcarol\t98\n"
        "user-service\tv1.0.3\tubuntu:18.04\tbob\t210\n"
        "gateway-service\tv1.5.2\talpine:3.17\tdave\t55\n"
        "notification-service\tv4.2.0\tdebian:stretch\teve\t180\n"
        "order-service\tv2.0.0\tubuntu:20.04\tfrank\t134\n"
        "session-service\tv1.1.1\tubuntu:18.04\talice\t77\n"
        "inventory-service\tv3.3.3\talpine:3.17\tcarol\t66\n"
    )

    assert os.path.isfile(MANIFEST_FILE), (
        f"Original manifest file '{MANIFEST_FILE}' is missing after task completion."
    )

    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    assert content == EXPECTED_TSV_CONTENT, (
        f"Original manifest file '{MANIFEST_FILE}' was modified during the task.\n"
        f"Expected:\n{EXPECTED_TSV_CONTENT!r}\n"
        f"Got:\n{content!r}"
    )