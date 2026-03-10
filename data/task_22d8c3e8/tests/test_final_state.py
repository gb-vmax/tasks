# test_final_state.py

import os
import pytest

INFRA_DIR = "/home/user/infra"
SERVERS_CSV_PATH = "/home/user/infra/servers.csv"
PROVISION_TARGETS_PATH = "/home/user/infra/provision_targets.ini"

EXPECTED_CONTENT = "[provision_targets]\nweb-prod-01\ndb-prod-01\ncache-prod-01\nworker-prod-01"

EXPECTED_LINES = [
    "[provision_targets]",
    "web-prod-01",
    "db-prod-01",
    "cache-prod-01",
    "worker-prod-01",
]


def test_provision_targets_file_exists():
    assert os.path.isfile(PROVISION_TARGETS_PATH), (
        f"Output file '{PROVISION_TARGETS_PATH}' does not exist. "
        "The task requires generating this Ansible inventory file."
    )


def test_provision_targets_file_is_readable():
    assert os.access(PROVISION_TARGETS_PATH, os.R_OK), (
        f"Output file '{PROVISION_TARGETS_PATH}' exists but is not readable."
    )


def test_provision_targets_first_line_is_header():
    with open(PROVISION_TARGETS_PATH, "r") as f:
        first_line = f.readline()
    # Strip only the newline, not spaces (to catch trailing space issues)
    first_line_stripped = first_line.rstrip("\n").rstrip("\r")
    assert first_line_stripped == "[provision_targets]", (
        f"The first line of '{PROVISION_TARGETS_PATH}' must be exactly '[provision_targets]', "
        f"but got: '{first_line_stripped}'"
    )


def test_provision_targets_line_count():
    with open(PROVISION_TARGETS_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 5, (
        f"Expected exactly 5 lines in '{PROVISION_TARGETS_PATH}' "
        f"(1 header + 4 hostnames), but found {len(lines)} lines.\n"
        f"File content:\n{content}"
    )


def test_provision_targets_exact_content():
    with open(PROVISION_TARGETS_PATH, "r") as f:
        content = f.read()
    # Normalize: strip trailing newline if present (one trailing newline is acceptable)
    # but the content itself must match exactly
    normalized = content.rstrip("\n").rstrip("\r")
    assert normalized == EXPECTED_CONTENT, (
        f"Content of '{PROVISION_TARGETS_PATH}' does not match expected.\n"
        f"Expected:\n{EXPECTED_CONTENT}\n\n"
        f"Got (repr):\n{repr(content)}"
    )


def test_provision_targets_no_blank_lines():
    with open(PROVISION_TARGETS_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"Found blank lines at line numbers {blank_lines} in '{PROVISION_TARGETS_PATH}'. "
        "The file must contain no blank lines."
    )


def test_provision_targets_no_trailing_spaces():
    with open(PROVISION_TARGETS_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    lines_with_trailing_spaces = [
        (i + 1, repr(line)) for i, line in enumerate(lines) if line != line.rstrip()
    ]
    assert not lines_with_trailing_spaces, (
        f"Found trailing spaces in '{PROVISION_TARGETS_PATH}' on lines: "
        f"{lines_with_trailing_spaces}"
    )


def test_provision_targets_hostnames_correct():
    with open(PROVISION_TARGETS_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    # Skip header line
    hostnames = lines[1:]
    expected_hostnames = ["web-prod-01", "db-prod-01", "cache-prod-01", "worker-prod-01"]
    assert hostnames == expected_hostnames, (
        f"Hostnames in '{PROVISION_TARGETS_PATH}' do not match expected.\n"
        f"Expected hostnames (in order): {expected_hostnames}\n"
        f"Got hostnames: {hostnames}"
    )


def test_provision_targets_hostnames_order():
    """Hostnames must appear in the same order as in the CSV."""
    with open(PROVISION_TARGETS_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    hostnames = lines[1:]  # skip header

    expected_order = ["web-prod-01", "db-prod-01", "cache-prod-01", "worker-prod-01"]
    assert hostnames == expected_order, (
        f"Hostnames are not in the correct order (must match CSV top-to-bottom order).\n"
        f"Expected order: {expected_order}\n"
        f"Got: {hostnames}"
    )


def test_provision_targets_excludes_non_prod():
    with open(PROVISION_TARGETS_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    hostnames = lines[1:]

    non_prod_hosts = ["app-staging-01", "db-staging-01"]
    for host in non_prod_hosts:
        assert host not in hostnames, (
            f"Hostname '{host}' should NOT be in '{PROVISION_TARGETS_PATH}' "
            f"because it is in the 'staging' environment, not 'prod'."
        )


def test_provision_targets_excludes_non_unprovisioned():
    with open(PROVISION_TARGETS_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    hostnames = lines[1:]

    non_unprovisioned_hosts = ["web-prod-02", "app-prod-01", "lb-prod-01"]
    for host in non_unprovisioned_hosts:
        assert host not in hostnames, (
            f"Hostname '{host}' should NOT be in '{PROVISION_TARGETS_PATH}' "
            f"because its status is not 'unprovisioned'."
        )


def test_provision_targets_contains_all_expected_hostnames():
    with open(PROVISION_TARGETS_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    hostnames = lines[1:]

    expected_hostnames = ["web-prod-01", "db-prod-01", "cache-prod-01", "worker-prod-01"]
    for host in expected_hostnames:
        assert host in hostnames, (
            f"Hostname '{host}' is missing from '{PROVISION_TARGETS_PATH}'. "
            f"It should be included because it is in 'prod' environment with 'unprovisioned' status."
        )


def test_servers_csv_unchanged():
    """The original servers.csv should not have been modified."""
    expected_csv = (
        "hostname,ip_address,environment,status,role\n"
        "web-prod-01,10.0.1.10,prod,unprovisioned,webserver\n"
        "web-prod-02,10.0.1.11,prod,running,webserver\n"
        "db-prod-01,10.0.2.10,prod,unprovisioned,database\n"
        "app-staging-01,10.0.3.10,staging,unprovisioned,appserver\n"
        "app-prod-01,10.0.1.20,prod,running,appserver\n"
        "cache-prod-01,10.0.1.30,prod,unprovisioned,cache\n"
        "db-staging-01,10.0.3.20,staging,unprovisioned,database\n"
        "lb-prod-01,10.0.1.5,prod,stopped,loadbalancer\n"
        "worker-prod-01,10.0.1.40,prod,unprovisioned,worker"
    )
    assert os.path.isfile(SERVERS_CSV_PATH), (
        f"Original CSV file '{SERVERS_CSV_PATH}' is missing."
    )
    with open(SERVERS_CSV_PATH, "r") as f:
        content = f.read().strip()
    assert content == expected_csv.strip(), (
        f"The original '{SERVERS_CSV_PATH}' has been modified unexpectedly.\n"
        f"Expected:\n{expected_csv.strip()}\n\nGot:\n{content}"
    )