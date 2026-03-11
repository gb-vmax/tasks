# test_final_state.py

import os
import pytest

VIOLATIONS_PATH = "/home/user/devsecops/violations.txt"

EXPECTED_LINES = [
    "POLICY VIOLATION REPORT",
    "=======================",
    "NON-COMPLIANT ACCOUNTS (password_expires=false):",
    "",
    "svc-deploy | role=deployer | env=production",
    "svc-backup | role=backup-agent | env=staging",
    "svc-infra | role=admin | env=production",
    "",
    "Total violations: 3",
]

COMPLIANT_ACCOUNTS = ["svc-monitor", "svc-ci", "svc-audit"]


def read_violations_file():
    with open(VIOLATIONS_PATH, "r") as f:
        content = f.read()
    return content


def get_lines():
    content = read_violations_file()
    # Split on newlines; trailing newline means last element is empty string
    lines = content.split("\n")
    # The file should end with a newline, so the last element after split is ''
    return lines


def test_violations_file_exists():
    assert os.path.isfile(VIOLATIONS_PATH), (
        f"Report file '{VIOLATIONS_PATH}' does not exist. "
        "The violations report must be generated at this path."
    )


def test_violations_file_is_readable():
    assert os.access(VIOLATIONS_PATH, os.R_OK), (
        f"Report file '{VIOLATIONS_PATH}' is not readable."
    )


def test_violations_file_ends_with_newline():
    content = read_violations_file()
    assert content.endswith("\n"), (
        f"Report file '{VIOLATIONS_PATH}' must end with a trailing newline character. "
        f"Last character is: {content[-1]!r}"
    )


def test_violations_file_total_line_count():
    content = read_violations_file()
    # With trailing newline, split gives 10 elements (last is empty string)
    lines = content.split("\n")
    # 9 content lines + trailing newline = 10 elements when split
    assert len(lines) == 10, (
        f"Expected exactly 10 elements when splitting on newline (9 lines + trailing newline), "
        f"but got {len(lines)}. "
        f"Full content:\n{content!r}"
    )


def test_line_1_policy_violation_report():
    lines = get_lines()
    assert lines[0] == "POLICY VIOLATION REPORT", (
        f"Line 1 must be 'POLICY VIOLATION REPORT', "
        f"but got: {lines[0]!r}"
    )


def test_line_2_separator():
    lines = get_lines()
    assert lines[1] == "=======================", (
        f"Line 2 must be exactly 23 '=' characters ('======================='), "
        f"but got: {lines[1]!r} (length {len(lines[1])})"
    )


def test_line_2_separator_length():
    lines = get_lines()
    assert len(lines[1]) == 23, (
        f"Line 2 separator must be exactly 23 '=' characters, "
        f"but got {len(lines[1])} characters: {lines[1]!r}"
    )


def test_line_3_non_compliant_header():
    lines = get_lines()
    assert lines[2] == "NON-COMPLIANT ACCOUNTS (password_expires=false):", (
        f"Line 3 must be 'NON-COMPLIANT ACCOUNTS (password_expires=false):', "
        f"but got: {lines[2]!r}"
    )


def test_line_4_blank():
    lines = get_lines()
    assert lines[3] == "", (
        f"Line 4 must be blank (empty string), "
        f"but got: {lines[3]!r}"
    )


def test_line_5_svc_deploy():
    lines = get_lines()
    expected = "svc-deploy | role=deployer | env=production"
    assert lines[4] == expected, (
        f"Line 5 must be {expected!r}, "
        f"but got: {lines[4]!r}"
    )


def test_line_6_svc_backup():
    lines = get_lines()
    expected = "svc-backup | role=backup-agent | env=staging"
    assert lines[5] == expected, (
        f"Line 6 must be {expected!r}, "
        f"but got: {lines[5]!r}"
    )


def test_line_7_svc_infra():
    lines = get_lines()
    expected = "svc-infra | role=admin | env=production"
    assert lines[6] == expected, (
        f"Line 7 must be {expected!r}, "
        f"but got: {lines[6]!r}"
    )


def test_line_8_blank():
    lines = get_lines()
    assert lines[7] == "", (
        f"Line 8 must be blank (empty string), "
        f"but got: {lines[7]!r}"
    )


def test_line_9_total_violations():
    lines = get_lines()
    assert lines[8] == "Total violations: 3", (
        f"Line 9 must be 'Total violations: 3', "
        f"but got: {lines[8]!r}"
    )


def test_line_10_trailing_newline_empty():
    lines = get_lines()
    assert lines[9] == "", (
        f"After the trailing newline, the last split element must be empty string, "
        f"but got: {lines[9]!r}"
    )


def test_compliant_accounts_not_in_file():
    content = read_violations_file()
    for account in COMPLIANT_ACCOUNTS:
        assert account not in content, (
            f"Compliant account '{account}' (password_expires=true) must NOT appear "
            f"in the violations report, but it was found in the file."
        )


def test_exact_content_matches():
    content = read_violations_file()
    expected_content = "\n".join(EXPECTED_LINES) + "\n"
    assert content == expected_content, (
        f"File content does not exactly match expected.\n"
        f"Expected:\n{expected_content!r}\n"
        f"Got:\n{content!r}"
    )


def test_account_line_format_uses_pipe_delimiter():
    lines = get_lines()
    account_lines = [lines[4], lines[5], lines[6]]
    for line in account_lines:
        assert " | " in line, (
            f"Account line must use ' | ' (space-pipe-space) as delimiter, "
            f"but got: {line!r}"
        )
        parts = line.split(" | ")
        assert len(parts) == 3, (
            f"Account line must have exactly 3 parts separated by ' | ', "
            f"but got {len(parts)} parts in: {line!r}"
        )
        assert parts[1].startswith("role="), (
            f"Second part of account line must start with 'role=', "
            f"but got: {parts[1]!r} in line: {line!r}"
        )
        assert parts[2].startswith("env="), (
            f"Third part of account line must start with 'env=', "
            f"but got: {parts[2]!r} in line: {line!r}"
        )


def test_three_violation_accounts_present():
    lines = get_lines()
    account_lines = lines[4:7]
    account_names = [line.split(" | ")[0] for line in account_lines]
    expected_names = ["svc-deploy", "svc-backup", "svc-infra"]
    assert account_names == expected_names, (
        f"Expected non-compliant account names in order {expected_names}, "
        f"but got: {account_names}"
    )