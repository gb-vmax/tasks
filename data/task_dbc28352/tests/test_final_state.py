# test_final_state.py

import os
import csv
import pytest

CSV_PATH = "/home/user/devsecops/pod_configs.csv"
VIOLATIONS_PATH = "/home/user/devsecops/violations.txt"
DEVSECOPS_DIR = "/home/user/devsecops"

EXPECTED_HEADER_LINE1 = "POLICY VIOLATION REPORT: privileged=true"
EXPECTED_HEADER_LINE2 = "=" * 41
EXPECTED_VIOLATIONS = [
    "infra/privileged-agent",
    "kube-system/debug-shell",
    "monitoring/log-collector",
]

EXPECTED_CONTENT = (
    "POLICY VIOLATION REPORT: privileged=true\n"
    "=========================================\n"
    "infra/privileged-agent\n"
    "kube-system/debug-shell\n"
    "monitoring/log-collector\n"
)


def test_violations_file_exists():
    assert os.path.isfile(VIOLATIONS_PATH), (
        f"Violations report '{VIOLATIONS_PATH}' does not exist. "
        "The student must generate this file as part of the task."
    )


def test_violations_file_is_readable():
    assert os.access(VIOLATIONS_PATH, os.R_OK), (
        f"Violations report '{VIOLATIONS_PATH}' exists but is not readable."
    )


def test_violations_file_not_empty():
    size = os.path.getsize(VIOLATIONS_PATH)
    assert size > 0, (
        f"Violations report '{VIOLATIONS_PATH}' is empty. "
        "It must contain the policy violation report."
    )


def test_violations_file_first_header_line():
    with open(VIOLATIONS_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, (
        f"'{VIOLATIONS_PATH}' has no lines at all."
    )
    assert lines[0] == EXPECTED_HEADER_LINE1, (
        f"First line of '{VIOLATIONS_PATH}' is incorrect.\n"
        f"Expected: '{EXPECTED_HEADER_LINE1}'\n"
        f"Got:      '{lines[0]}'"
    )


def test_violations_file_separator_line():
    with open(VIOLATIONS_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 2, (
        f"'{VIOLATIONS_PATH}' has fewer than 2 lines; missing separator line."
    )
    assert lines[1] == EXPECTED_HEADER_LINE2, (
        f"Second line (separator) of '{VIOLATIONS_PATH}' is incorrect.\n"
        f"Expected: '{EXPECTED_HEADER_LINE2}' (41 '=' characters)\n"
        f"Got:      '{lines[1]}' (length={len(lines[1])})"
    )


def test_violations_file_separator_length():
    with open(VIOLATIONS_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 2, (
        f"'{VIOLATIONS_PATH}' has fewer than 2 lines."
    )
    sep = lines[1]
    assert len(sep) == 41, (
        f"Separator line must be exactly 41 '=' characters, "
        f"but got {len(sep)} characters: '{sep}'"
    )
    assert sep == "=" * 41, (
        f"Separator line must consist only of '=' characters, got: '{sep}'"
    )


def test_violations_file_violation_entries():
    with open(VIOLATIONS_PATH, "r") as f:
        lines = f.read().splitlines()

    # Entries start from line index 2
    assert len(lines) >= 3, (
        f"'{VIOLATIONS_PATH}' has fewer than 3 lines; no violation entries found."
    )
    actual_entries = lines[2:]

    assert actual_entries == EXPECTED_VIOLATIONS, (
        f"Violation entries in '{VIOLATIONS_PATH}' do not match expected.\n"
        f"Expected entries (sorted):\n" +
        "\n".join(EXPECTED_VIOLATIONS) +
        f"\n\nActual entries:\n" +
        "\n".join(actual_entries)
    )


def test_violations_file_entries_are_sorted():
    with open(VIOLATIONS_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 3, (
        f"'{VIOLATIONS_PATH}' has fewer than 3 lines; no violation entries to check."
    )
    actual_entries = lines[2:]
    sorted_entries = sorted(actual_entries)

    assert actual_entries == sorted_entries, (
        f"Violation entries in '{VIOLATIONS_PATH}' are not sorted alphabetically.\n"
        f"Current order:  {actual_entries}\n"
        f"Expected order: {sorted_entries}"
    )


def test_violations_file_entry_format():
    with open(VIOLATIONS_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 3, (
        f"'{VIOLATIONS_PATH}' has fewer than 3 lines."
    )
    actual_entries = lines[2:]

    for entry in actual_entries:
        assert "/" in entry, (
            f"Entry '{entry}' does not follow the '<namespace>/<pod_name>' format "
            f"(missing '/' separator)."
        )
        parts = entry.split("/")
        assert len(parts) == 2, (
            f"Entry '{entry}' does not follow the '<namespace>/<pod_name>' format "
            f"(expected exactly one '/')."
        )
        namespace, pod_name = parts
        assert namespace and pod_name, (
            f"Entry '{entry}' has an empty namespace or pod_name."
        )
        assert not entry.startswith(" "), (
            f"Entry '{entry}' has leading whitespace, which is not allowed."
        )
        assert not entry.endswith(" "), (
            f"Entry '{entry}' has trailing whitespace, which is not allowed."
        )


def test_violations_file_correct_number_of_entries():
    with open(VIOLATIONS_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 3, (
        f"'{VIOLATIONS_PATH}' has fewer than 3 lines."
    )
    actual_entries = lines[2:]
    expected_count = len(EXPECTED_VIOLATIONS)

    assert len(actual_entries) == expected_count, (
        f"Expected {expected_count} violation entries in '{VIOLATIONS_PATH}', "
        f"but found {len(actual_entries)}.\n"
        f"Entries found: {actual_entries}"
    )


def test_violations_file_exact_content():
    with open(VIOLATIONS_PATH, "r") as f:
        actual_content = f.read()

    # Normalize: ensure trailing newline for comparison
    # The expected content ends with a newline after the last entry
    assert actual_content == EXPECTED_CONTENT, (
        f"Content of '{VIOLATIONS_PATH}' does not exactly match expected.\n"
        f"Expected (repr): {repr(EXPECTED_CONTENT)}\n"
        f"Actual   (repr): {repr(actual_content)}"
    )


def test_violations_match_csv_privileged_true():
    """Cross-check: violations in report match privileged=true rows in CSV."""
    with open(CSV_PATH, "r") as f:
        reader = csv.DictReader(f)
        expected_entries = sorted(
            f"{row['namespace']}/{row['pod_name']}"
            for row in reader
            if row["privileged"].strip().lower() == "true"
        )

    with open(VIOLATIONS_PATH, "r") as f:
        lines = f.read().splitlines()

    actual_entries = lines[2:] if len(lines) >= 3 else []

    assert actual_entries == expected_entries, (
        f"Violation entries do not match privileged=true rows from '{CSV_PATH}'.\n"
        f"Expected (derived from CSV): {expected_entries}\n"
        f"Actual (in report):          {actual_entries}"
    )


def test_csv_file_unchanged():
    """Ensure the original CSV file was not modified."""
    expected_csv_content = (
        "pod_name,namespace,image,privileged,run_as_root\n"
        "api-server,production,myrepo/api:1.2,false,false\n"
        "debug-shell,kube-system,busybox:latest,true,true\n"
        "nginx-proxy,frontend,nginx:1.21,false,false\n"
        "log-collector,monitoring,fluentd:v1.14,true,false\n"
        "db-migrator,production,postgres:14,false,true\n"
        "privileged-agent,infra,agent:3.0,true,false\n"
        "cert-manager,cert-manager,quay.io/cert-manager:v1.9,false,false\n"
        "node-exporter,monitoring,prom/node-exporter:v1.3,false,false\n"
    )

    with open(CSV_PATH, "r") as f:
        actual_csv = f.read()

    # Strip trailing whitespace from each line for a lenient check
    actual_lines = actual_csv.strip().splitlines()
    expected_lines = expected_csv_content.strip().splitlines()

    assert actual_lines == expected_lines, (
        f"The CSV file '{CSV_PATH}' appears to have been modified.\n"
        f"Expected content:\n{expected_csv_content}\n"
        f"Actual content:\n{actual_csv}"
    )