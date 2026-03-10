# test_final_state.py

import os
import json
import pytest

PROVISIONING_DIR = "/home/user/provisioning"
SERVER_SPEC_PATH = "/home/user/provisioning/server_spec.json"
SCRIPT_PATH = "/home/user/provisioning/solve_provisioning.py"
PLAN_PATH = "/home/user/provisioning/provisioning_plan.txt"

EXPECTED_PLAN = """\
=== PROVISIONING PLAN ===
Budget used: $50000.00 of $50000
Rack units used: 16.67 of 42
Total vCPUs: 333.33

Allocation:
  compute-s: 0.00
  compute-m: 0.00
  compute-l: 4.17"""


def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), (
        f"Script {SCRIPT_PATH} does not exist. "
        "The student must create solve_provisioning.py."
    )


def test_script_is_readable():
    assert os.access(SCRIPT_PATH, os.R_OK), (
        f"Script {SCRIPT_PATH} is not readable."
    )


def test_script_contains_linprog():
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    assert "linprog" in content, (
        f"Script {SCRIPT_PATH} does not appear to use scipy.optimize.linprog. "
        "The task requires using linprog for the LP solver."
    )


def test_plan_file_exists():
    assert os.path.isfile(PLAN_PATH), (
        f"Output file {PLAN_PATH} does not exist. "
        "The student must run the script to produce provisioning_plan.txt."
    )


def test_plan_file_is_readable():
    assert os.access(PLAN_PATH, os.R_OK), (
        f"Output file {PLAN_PATH} is not readable."
    )


def test_plan_file_exact_content():
    with open(PLAN_PATH, "r") as f:
        content = f.read()

    # Strip trailing newline for comparison but check structure
    content_stripped = content.rstrip("\n")

    assert content_stripped == EXPECTED_PLAN, (
        f"Content of {PLAN_PATH} does not match expected.\n"
        f"Expected:\n{EXPECTED_PLAN!r}\n\n"
        f"Got:\n{content_stripped!r}"
    )


def test_plan_header_line():
    with open(PLAN_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    assert len(lines) >= 1, f"File {PLAN_PATH} is empty or has too few lines."
    assert lines[0] == "=== PROVISIONING PLAN ===", (
        f"First line of {PLAN_PATH} should be '=== PROVISIONING PLAN ===' "
        f"but got: {lines[0]!r}"
    )


def test_plan_budget_line():
    with open(PLAN_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    assert len(lines) >= 2, f"File {PLAN_PATH} has fewer than 2 lines."
    assert lines[1] == "Budget used: $50000.00 of $50000", (
        f"Second line of {PLAN_PATH} should be 'Budget used: $50000.00 of $50000' "
        f"but got: {lines[1]!r}"
    )


def test_plan_rack_units_line():
    with open(PLAN_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    assert len(lines) >= 3, f"File {PLAN_PATH} has fewer than 3 lines."
    assert lines[2] == "Rack units used: 16.67 of 42", (
        f"Third line of {PLAN_PATH} should be 'Rack units used: 16.67 of 42' "
        f"but got: {lines[2]!r}"
    )


def test_plan_total_vcpus_line():
    with open(PLAN_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    assert len(lines) >= 4, f"File {PLAN_PATH} has fewer than 4 lines."
    assert lines[3] == "Total vCPUs: 333.33", (
        f"Fourth line of {PLAN_PATH} should be 'Total vCPUs: 333.33' "
        f"but got: {lines[3]!r}"
    )


def test_plan_blank_line_after_summary():
    with open(PLAN_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    assert len(lines) >= 5, f"File {PLAN_PATH} has fewer than 5 lines."
    assert lines[4] == "", (
        f"Fifth line of {PLAN_PATH} should be blank "
        f"but got: {lines[4]!r}"
    )


def test_plan_allocation_header():
    with open(PLAN_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    assert len(lines) >= 6, f"File {PLAN_PATH} has fewer than 6 lines."
    assert lines[5] == "Allocation:", (
        f"Sixth line of {PLAN_PATH} should be 'Allocation:' "
        f"but got: {lines[5]!r}"
    )


def test_plan_compute_s_allocation():
    with open(PLAN_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    assert len(lines) >= 7, f"File {PLAN_PATH} has fewer than 7 lines."
    assert lines[6] == "  compute-s: 0.00", (
        f"Seventh line of {PLAN_PATH} should be '  compute-s: 0.00' "
        f"but got: {lines[6]!r}"
    )


def test_plan_compute_m_allocation():
    with open(PLAN_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    assert len(lines) >= 8, f"File {PLAN_PATH} has fewer than 8 lines."
    assert lines[7] == "  compute-m: 0.00", (
        f"Eighth line of {PLAN_PATH} should be '  compute-m: 0.00' "
        f"but got: {lines[7]!r}"
    )


def test_plan_compute_l_allocation():
    with open(PLAN_PATH, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    assert len(lines) >= 9, f"File {PLAN_PATH} has fewer than 9 lines."
    assert lines[8] == "  compute-l: 4.17", (
        f"Ninth line of {PLAN_PATH} should be '  compute-l: 4.17' "
        f"but got: {lines[8]!r}"
    )


def test_plan_line_count():
    with open(PLAN_PATH, "r") as f:
        content = f.read().rstrip("\n")
    lines = content.splitlines()
    assert len(lines) == 9, (
        f"Expected exactly 9 lines in {PLAN_PATH} (excluding trailing newline), "
        f"but got {len(lines)} lines."
    )


def test_plan_no_trailing_spaces():
    with open(PLAN_PATH, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(" "), (
            f"Line {i} in {PLAN_PATH} has trailing spaces: {stripped!r}"
        )


def test_server_spec_unchanged():
    """Verify that server_spec.json was not modified."""
    with open(SERVER_SPEC_PATH, "r") as f:
        data = json.load(f)

    assert data["budget"] == 50000, (
        f"server_spec.json was modified: budget changed to {data['budget']}"
    )
    assert data["rack_units"] == 42, (
        f"server_spec.json was modified: rack_units changed to {data['rack_units']}"
    )
    assert len(data["servers"]) == 3, (
        f"server_spec.json was modified: servers list length changed to {len(data['servers'])}"
    )

    expected_servers = [
        {"name": "compute-s", "cost": 3000, "ru": 1, "vcpus": 16},
        {"name": "compute-m", "cost": 6000, "ru": 2, "vcpus": 36},
        {"name": "compute-l", "cost": 12000, "ru": 4, "vcpus": 80},
    ]
    for i, (expected, actual) in enumerate(zip(expected_servers, data["servers"])):
        assert expected == actual, (
            f"server_spec.json was modified: server[{i}] changed. "
            f"Expected {expected}, got {actual}"
        )