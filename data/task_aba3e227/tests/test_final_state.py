# test_final_state.py

import os
import stat
import pytest

TO_MIGRATE_PATH = "/home/user/cloud/to_migrate.csv"
MANIFEST_PATH = "/home/user/cloud/migration_manifest.txt"

EXPECTED_TO_MIGRATE = """service_name,region,tier,monthly_cost_usd,replicas
auth-service,us-east-1,production,1200,3
billing-api,us-east-1,production,2400,5
search-service,us-east-1,production,3100,4
data-pipeline,us-east-1,production,4500,6
queue-worker,us-east-1,production,750,2"""

EXPECTED_MANIFEST = """MIGRATION MANIFEST: us-east-1 -> eu-west-2
----------------------------------------
[SERVICE] auth-service | replicas=3 | est_cost=$1200
[SERVICE] billing-api | replicas=5 | est_cost=$2400
[SERVICE] search-service | replicas=4 | est_cost=$3100
[SERVICE] data-pipeline | replicas=6 | est_cost=$4500
[SERVICE] queue-worker | replicas=2 | est_cost=$750
----------------------------------------
Total services: 5
Total monthly cost: $11950"""


# ── to_migrate.csv tests ──────────────────────────────────────────────────────

def test_to_migrate_csv_exists():
    assert os.path.isfile(TO_MIGRATE_PATH), (
        f"File '{TO_MIGRATE_PATH}' does not exist. "
        "Step 1 requires creating to_migrate.csv with filtered services."
    )


def test_to_migrate_csv_header():
    with open(TO_MIGRATE_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")
    expected_header = "service_name,region,tier,monthly_cost_usd,replicas"
    assert first_line == expected_header, (
        f"Header of '{TO_MIGRATE_PATH}' is incorrect.\n"
        f"Expected: '{expected_header}'\n"
        f"Got:      '{first_line}'"
    )


def test_to_migrate_csv_row_count():
    with open(TO_MIGRATE_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    # 1 header + 5 data rows
    assert len(lines) == 6, (
        f"Expected 6 lines (1 header + 5 data rows) in '{TO_MIGRATE_PATH}', "
        f"but found {len(lines)} lines."
    )


def test_to_migrate_csv_contains_correct_services():
    with open(TO_MIGRATE_PATH, "r") as f:
        content = f.read()
    required = [
        "auth-service,us-east-1,production,1200,3",
        "billing-api,us-east-1,production,2400,5",
        "search-service,us-east-1,production,3100,4",
        "data-pipeline,us-east-1,production,4500,6",
        "queue-worker,us-east-1,production,750,2",
    ]
    for line in required:
        assert line in content, (
            f"Required service line '{line}' not found in '{TO_MIGRATE_PATH}'."
        )


def test_to_migrate_csv_excludes_wrong_services():
    with open(TO_MIGRATE_PATH, "r") as f:
        content = f.read()
    excluded = [
        "logging-agent",
        "notification-svc",
        "image-processor",
        "cache-cluster",
        "gateway-api",
    ]
    for svc in excluded:
        assert svc not in content, (
            f"Service '{svc}' should NOT appear in '{TO_MIGRATE_PATH}' "
            "(it does not meet the us-east-1 + production criteria)."
        )


def test_to_migrate_csv_order():
    with open(TO_MIGRATE_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    # Skip header
    data_lines = lines[1:]
    expected_order = [
        "auth-service,us-east-1,production,1200,3",
        "billing-api,us-east-1,production,2400,5",
        "search-service,us-east-1,production,3100,4",
        "data-pipeline,us-east-1,production,4500,6",
        "queue-worker,us-east-1,production,750,2",
    ]
    assert data_lines == expected_order, (
        f"Data rows in '{TO_MIGRATE_PATH}' are not in the expected order.\n"
        f"Expected:\n" + "\n".join(expected_order) + "\n\n"
        f"Got:\n" + "\n".join(data_lines)
    )


def test_to_migrate_csv_exact_content():
    with open(TO_MIGRATE_PATH, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_TO_MIGRATE, (
        f"Content of '{TO_MIGRATE_PATH}' does not match expected.\n"
        f"Expected:\n{EXPECTED_TO_MIGRATE}\n\n"
        f"Got:\n{content}"
    )


def test_to_migrate_csv_no_trailing_spaces():
    with open(TO_MIGRATE_PATH, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} in '{TO_MIGRATE_PATH}' has trailing whitespace: {repr(line)}"
        )


# ── migration_manifest.txt tests ─────────────────────────────────────────────

def test_manifest_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"File '{MANIFEST_PATH}' does not exist. "
        "Step 2 requires creating migration_manifest.txt."
    )


def test_manifest_exact_content():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read().rstrip("\n")
    assert content == EXPECTED_MANIFEST, (
        f"Content of '{MANIFEST_PATH}' does not match expected.\n"
        f"Expected:\n{EXPECTED_MANIFEST}\n\n"
        f"Got:\n{content}"
    )


def test_manifest_header_line():
    with open(MANIFEST_PATH, "r") as f:
        first_line = f.readline().rstrip("\n")
    expected = "MIGRATION MANIFEST: us-east-1 -> eu-west-2"
    assert first_line == expected, (
        f"First line of '{MANIFEST_PATH}' is incorrect.\n"
        f"Expected: '{expected}'\n"
        f"Got:      '{first_line}'"
    )


def test_manifest_separator_lines():
    with open(MANIFEST_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip() or line == "\n"]
    separator = "-" * 40
    # Second line should be separator
    assert lines[1] == separator, (
        f"Line 2 of '{MANIFEST_PATH}' should be 40 dashes.\n"
        f"Expected: '{separator}'\n"
        f"Got:      '{lines[1]}'"
    )
    # The separator after services should be at index 7 (0-based: header, sep, 5 services, sep)
    assert lines[7] == separator, (
        f"The closing separator line in '{MANIFEST_PATH}' should be 40 dashes.\n"
        f"Expected: '{separator}'\n"
        f"Got:      '{lines[7]}'"
    )


def test_manifest_service_lines():
    with open(MANIFEST_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    # Service lines are at indices 2-6
    expected_service_lines = [
        "[SERVICE] auth-service | replicas=3 | est_cost=$1200",
        "[SERVICE] billing-api | replicas=5 | est_cost=$2400",
        "[SERVICE] search-service | replicas=4 | est_cost=$3100",
        "[SERVICE] data-pipeline | replicas=6 | est_cost=$4500",
        "[SERVICE] queue-worker | replicas=2 | est_cost=$750",
    ]
    service_lines = lines[2:7]
    assert service_lines == expected_service_lines, (
        f"Service lines in '{MANIFEST_PATH}' are incorrect.\n"
        f"Expected:\n" + "\n".join(expected_service_lines) + "\n\n"
        f"Got:\n" + "\n".join(service_lines)
    )


def test_manifest_total_services_line():
    with open(MANIFEST_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    # Total services line is at index 8
    expected = "Total services: 5"
    assert lines[8] == expected, (
        f"'Total services' line in '{MANIFEST_PATH}' is incorrect.\n"
        f"Expected: '{expected}'\n"
        f"Got:      '{lines[8]}'"
    )


def test_manifest_total_cost_line():
    with open(MANIFEST_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    # Total monthly cost line is at index 9
    expected = "Total monthly cost: $11950"
    assert lines[9] == expected, (
        f"'Total monthly cost' line in '{MANIFEST_PATH}' is incorrect.\n"
        f"Expected: '{expected}'\n"
        f"Got:      '{lines[9]}'"
    )


def test_manifest_line_count():
    with open(MANIFEST_PATH, "r") as f:
        lines = [line for line in f if line.rstrip("\n") or False]
    # Count non-empty lines: header + sep + 5 services + sep + total_services + total_cost = 10
    non_empty = [l for l in lines if l.strip()]
    assert len(non_empty) == 10, (
        f"Expected 10 non-empty lines in '{MANIFEST_PATH}', found {len(non_empty)}."
    )


def test_manifest_no_trailing_spaces():
    with open(MANIFEST_PATH, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"Line {i} in '{MANIFEST_PATH}' has trailing whitespace: {repr(line)}"
        )


def test_manifest_no_decimal_costs():
    with open(MANIFEST_PATH, "r") as f:
        content = f.read()
    import re
    # Ensure no decimal points appear in cost values
    decimal_costs = re.findall(r'\$[\d]+\.[\d]+', content)
    assert not decimal_costs, (
        f"Cost values in '{MANIFEST_PATH}' should be plain integers (no decimals). "
        f"Found: {decimal_costs}"
    )


# ── permissions tests ─────────────────────────────────────────────────────────

def test_manifest_permissions():
    st = os.stat(MANIFEST_PATH)
    mode = stat.S_IMODE(st.st_mode)
    expected_mode = 0o644
    assert mode == expected_mode, (
        f"Permissions on '{MANIFEST_PATH}' are incorrect.\n"
        f"Expected: {oct(expected_mode)} (rw-r--r--)\n"
        f"Got:      {oct(mode)}"
    )


def test_manifest_owner_readable():
    st = os.stat(MANIFEST_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert mode & stat.S_IRUSR, (
        f"'{MANIFEST_PATH}' should be readable by owner (bit S_IRUSR)."
    )


def test_manifest_owner_writable():
    st = os.stat(MANIFEST_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert mode & stat.S_IWUSR, (
        f"'{MANIFEST_PATH}' should be writable by owner (bit S_IWUSR)."
    )


def test_manifest_not_owner_executable():
    st = os.stat(MANIFEST_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert not (mode & stat.S_IXUSR), (
        f"'{MANIFEST_PATH}' should NOT be executable by owner (bit S_IXUSR)."
    )


def test_manifest_group_readable():
    st = os.stat(MANIFEST_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert mode & stat.S_IRGRP, (
        f"'{MANIFEST_PATH}' should be readable by group (bit S_IRGRP)."
    )


def test_manifest_group_not_writable():
    st = os.stat(MANIFEST_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert not (mode & stat.S_IWGRP), (
        f"'{MANIFEST_PATH}' should NOT be writable by group (bit S_IWGRP)."
    )


def test_manifest_others_readable():
    st = os.stat(MANIFEST_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert mode & stat.S_IROTH, (
        f"'{MANIFEST_PATH}' should be readable by others (bit S_IROTH)."
    )


def test_manifest_others_not_writable():
    st = os.stat(MANIFEST_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert not (mode & stat.S_IWOTH), (
        f"'{MANIFEST_PATH}' should NOT be writable by others (bit S_IWOTH)."
    )


def test_manifest_others_not_executable():
    st = os.stat(MANIFEST_PATH)
    mode = stat.S_IMODE(st.st_mode)
    assert not (mode & stat.S_IXOTH), (
        f"'{MANIFEST_PATH}' should NOT be executable by others (bit S_IXOTH)."
    )