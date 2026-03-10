# test_final_state.py

import os
import pytest

MIGRATION_DIR = "/home/user/migration"
INVENTORY_RAW = "/home/user/migration/inventory_raw.txt"
ACTIVE_SERVICES = "/home/user/migration/active_services.txt"

EXPECTED_RAW_LINES = [
    "SERVICE=auth-service HOST=10.0.1.10 PORT=8080 STATUS=active",
    "SERVICE=billing-service HOST=10.0.1.11 PORT=8081 STATUS=inactive",
    "SERVICE=user-service HOST=10.0.1.12 PORT=8082 STATUS=active",
    "SERVICE=notification-service HOST=10.0.1.13 PORT=8083 STATUS=active",
    "SERVICE=report-service HOST=10.0.1.14 PORT=8084 STATUS=inactive",
    "SERVICE=gateway-service HOST=10.0.1.15 PORT=8085 STATUS=active",
    "SERVICE=cache-service HOST=10.0.1.16 PORT=8086 STATUS=inactive",
    "SERVICE=search-service HOST=10.0.1.17 PORT=8087 STATUS=active",
]

EXPECTED_ACTIVE_LINES = [
    "SERVICE=auth-service HOST=10.0.1.10 PORT=8080 STATUS=active",
    "SERVICE=user-service HOST=10.0.1.12 PORT=8082 STATUS=active",
    "SERVICE=notification-service HOST=10.0.1.13 PORT=8083 STATUS=active",
    "SERVICE=gateway-service HOST=10.0.1.15 PORT=8085 STATUS=active",
    "SERVICE=search-service HOST=10.0.1.17 PORT=8087 STATUS=active",
]

EXPECTED_ACTIVE_COUNT = 5
EXPECTED_SUMMARY_LINE = f"TOTAL_ACTIVE={EXPECTED_ACTIVE_COUNT}"


# ── migration directory ───────────────────────────────────────────────────────

def test_migration_directory_exists():
    assert os.path.isdir(MIGRATION_DIR), (
        f"Migration directory '{MIGRATION_DIR}' does not exist. "
        "It should have been created as part of the task."
    )


# ── inventory_raw.txt ─────────────────────────────────────────────────────────

def test_inventory_raw_exists():
    assert os.path.isfile(INVENTORY_RAW), (
        f"File '{INVENTORY_RAW}' does not exist. "
        "The legacy script output should have been redirected here."
    )


def test_inventory_raw_is_readable():
    assert os.access(INVENTORY_RAW, os.R_OK), (
        f"File '{INVENTORY_RAW}' exists but is not readable."
    )


def test_inventory_raw_line_count():
    with open(INVENTORY_RAW, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    assert len(lines) == 8, (
        f"'{INVENTORY_RAW}' should contain exactly 8 lines, "
        f"but found {len(lines)} line(s).\nContent:\n{content}"
    )


def test_inventory_raw_no_trailing_blank_line():
    with open(INVENTORY_RAW, "r") as f:
        content = f.read()
    assert not content.endswith("\n\n"), (
        f"'{INVENTORY_RAW}' has trailing blank lines. "
        "There should be no trailing blank line after the last service entry."
    )


def test_inventory_raw_exact_contents():
    with open(INVENTORY_RAW, "r") as f:
        content = f.read()
    actual_lines = content.rstrip("\n").split("\n")
    assert actual_lines == EXPECTED_RAW_LINES, (
        f"'{INVENTORY_RAW}' contents do not match expected.\n\n"
        f"Expected lines:\n" + "\n".join(EXPECTED_RAW_LINES) + "\n\n"
        f"Actual lines:\n" + "\n".join(actual_lines)
    )


def test_inventory_raw_each_line_format():
    with open(INVENTORY_RAW, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    for i, line in enumerate(lines, start=1):
        assert line.startswith("SERVICE="), (
            f"Line {i} of '{INVENTORY_RAW}' does not start with 'SERVICE=': {line!r}"
        )
        assert "HOST=" in line, (
            f"Line {i} of '{INVENTORY_RAW}' is missing 'HOST=': {line!r}"
        )
        assert "PORT=" in line, (
            f"Line {i} of '{INVENTORY_RAW}' is missing 'PORT=': {line!r}"
        )
        assert "STATUS=" in line, (
            f"Line {i} of '{INVENTORY_RAW}' is missing 'STATUS=': {line!r}"
        )


# ── active_services.txt ───────────────────────────────────────────────────────

def test_active_services_exists():
    assert os.path.isfile(ACTIVE_SERVICES), (
        f"File '{ACTIVE_SERVICES}' does not exist. "
        "Active service lines should have been extracted here."
    )


def test_active_services_is_readable():
    assert os.access(ACTIVE_SERVICES, os.R_OK), (
        f"File '{ACTIVE_SERVICES}' exists but is not readable."
    )


def test_active_services_total_line_count():
    with open(ACTIVE_SERVICES, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    expected_total = EXPECTED_ACTIVE_COUNT + 1  # service lines + summary
    assert len(lines) == expected_total, (
        f"'{ACTIVE_SERVICES}' should contain exactly {expected_total} lines "
        f"({EXPECTED_ACTIVE_COUNT} active service lines + 1 summary line), "
        f"but found {len(lines)} line(s).\nContent:\n{content}"
    )


def test_active_services_no_trailing_blank_line():
    with open(ACTIVE_SERVICES, "r") as f:
        content = f.read()
    assert not content.endswith("\n\n"), (
        f"'{ACTIVE_SERVICES}' has trailing blank lines. "
        "There should be no trailing blank line."
    )


def test_active_services_no_blank_lines_anywhere():
    with open(ACTIVE_SERVICES, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    for i, line in enumerate(lines, start=1):
        assert line.strip() != "", (
            f"Line {i} of '{ACTIVE_SERVICES}' is blank. "
            "No blank lines are allowed."
        )


def test_active_services_only_active_status_lines_before_summary():
    with open(ACTIVE_SERVICES, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    service_lines = lines[:-1]  # all but last (summary)
    for i, line in enumerate(service_lines, start=1):
        assert "STATUS=active" in line, (
            f"Line {i} of '{ACTIVE_SERVICES}' (before summary) does not contain "
            f"'STATUS=active': {line!r}. Only active service lines should appear."
        )


def test_active_services_no_inactive_lines():
    with open(ACTIVE_SERVICES, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    for i, line in enumerate(lines, start=1):
        assert "STATUS=inactive" not in line, (
            f"Line {i} of '{ACTIVE_SERVICES}' contains 'STATUS=inactive', "
            f"which should have been filtered out: {line!r}"
        )


def test_active_services_last_line_is_summary():
    with open(ACTIVE_SERVICES, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    last_line = lines[-1]
    assert last_line == EXPECTED_SUMMARY_LINE, (
        f"The last line of '{ACTIVE_SERVICES}' should be exactly "
        f"'{EXPECTED_SUMMARY_LINE}', but got: {last_line!r}"
    )


def test_active_services_summary_count_matches_active_lines():
    with open(ACTIVE_SERVICES, "r") as f:
        content = f.read()
    lines = content.rstrip("\n").split("\n")
    service_lines = lines[:-1]
    summary_line = lines[-1]
    # Parse N from TOTAL_ACTIVE=N
    assert summary_line.startswith("TOTAL_ACTIVE="), (
        f"Summary line does not start with 'TOTAL_ACTIVE=': {summary_line!r}"
    )
    try:
        reported_count = int(summary_line.split("=", 1)[1])
    except ValueError:
        pytest.fail(
            f"Could not parse integer from summary line: {summary_line!r}"
        )
    actual_service_count = len(service_lines)
    assert reported_count == actual_service_count, (
        f"Summary line reports TOTAL_ACTIVE={reported_count}, but there are "
        f"{actual_service_count} active service lines in the file."
    )
    assert reported_count == EXPECTED_ACTIVE_COUNT, (
        f"Summary line reports TOTAL_ACTIVE={reported_count}, but the expected "
        f"count is {EXPECTED_ACTIVE_COUNT}."
    )


def test_active_services_exact_contents():
    with open(ACTIVE_SERVICES, "r") as f:
        content = f.read()
    actual_lines = content.rstrip("\n").split("\n")
    expected_lines = EXPECTED_ACTIVE_LINES + [EXPECTED_SUMMARY_LINE]
    assert actual_lines == expected_lines, (
        f"'{ACTIVE_SERVICES}' contents do not match expected.\n\n"
        f"Expected lines:\n" + "\n".join(expected_lines) + "\n\n"
        f"Actual lines:\n" + "\n".join(actual_lines)
    )


def test_active_services_order_matches_raw():
    """Active lines in active_services.txt must appear in the same order as in inventory_raw.txt."""
    with open(INVENTORY_RAW, "r") as f:
        raw_content = f.read()
    with open(ACTIVE_SERVICES, "r") as f:
        active_content = f.read()

    raw_lines = raw_content.rstrip("\n").split("\n")
    active_lines = active_content.rstrip("\n").split("\n")[:-1]  # exclude summary

    raw_active_lines = [line for line in raw_lines if "STATUS=active" in line]

    assert active_lines == raw_active_lines, (
        f"Active lines in '{ACTIVE_SERVICES}' are not in the same order as "
        f"they appear in '{INVENTORY_RAW}'.\n\n"
        f"Expected order (from raw):\n" + "\n".join(raw_active_lines) + "\n\n"
        f"Actual order (in active file):\n" + "\n".join(active_lines)
    )