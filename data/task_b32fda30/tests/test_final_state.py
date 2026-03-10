# test_final_state.py

import os
import pytest

SCHEDULE_PATH = "/home/user/k8s_optimizer/schedule.txt"
SOLVE_SCRIPT_PATH = "/home/user/k8s_optimizer/solve.py"
WORKLOADS_JSON_PATH = "/home/user/k8s_optimizer/workloads.json"
K8S_OPTIMIZER_DIR = "/home/user/k8s_optimizer"

EXPECTED_LINES = [
    "=== Kubernetes Operator Schedule ===",
    "api-server: 1 replicas",
    "worker: 5 replicas",
    "cache: 2 replicas",
    "Total throughput: 51",
    "Status: OPTIMAL",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES) + "\n"


def test_k8s_optimizer_directory_exists():
    assert os.path.isdir(K8S_OPTIMIZER_DIR), (
        f"Required directory not found: {K8S_OPTIMIZER_DIR}\n"
        "The k8s_optimizer directory must exist."
    )


def test_workloads_json_still_exists():
    assert os.path.isfile(WORKLOADS_JSON_PATH), (
        f"Required file not found: {WORKLOADS_JSON_PATH}\n"
        "The workloads.json file must still exist after the task."
    )


def test_solve_script_exists():
    assert os.path.isfile(SOLVE_SCRIPT_PATH), (
        f"Required script not found: {SOLVE_SCRIPT_PATH}\n"
        "The solve.py script must be created at this path."
    )


def test_schedule_file_exists():
    assert os.path.isfile(SCHEDULE_PATH), (
        f"Output file not found: {SCHEDULE_PATH}\n"
        "The solve.py script must be run to produce schedule.txt."
    )


def test_schedule_file_is_readable():
    assert os.access(SCHEDULE_PATH, os.R_OK), (
        f"File exists but is not readable: {SCHEDULE_PATH}"
    )


def test_schedule_file_not_empty():
    size = os.path.getsize(SCHEDULE_PATH)
    assert size > 0, (
        f"File {SCHEDULE_PATH} is empty (0 bytes). "
        "It must contain the schedule output."
    )


def test_schedule_file_exact_content():
    with open(SCHEDULE_PATH, "r") as f:
        content = f.read()
    assert content == EXPECTED_CONTENT, (
        f"File {SCHEDULE_PATH} does not have the expected content.\n"
        f"Expected:\n{repr(EXPECTED_CONTENT)}\n"
        f"Got:\n{repr(content)}"
    )


def test_schedule_file_ends_with_newline():
    with open(SCHEDULE_PATH, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        f"File {SCHEDULE_PATH} must end with a single newline character.\n"
        f"Got content ending with: {repr(content[-5:])}"
    )


def test_schedule_file_line_count():
    with open(SCHEDULE_PATH, "r") as f:
        content = f.read()
    # Split by newline; trailing newline means last element is empty string
    lines = content.split("\n")
    # Should be 6 content lines + 1 empty string from trailing newline = 7 parts
    assert len(lines) == 7, (
        f"Expected 6 content lines plus a trailing newline (7 parts when split), "
        f"but got {len(lines)} parts.\nContent: {repr(content)}"
    )
    # The last element should be empty (trailing newline)
    assert lines[-1] == "", (
        f"Expected trailing newline resulting in empty last element after split, "
        f"but got: {repr(lines[-1])}"
    )


def test_schedule_header_line():
    with open(SCHEDULE_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[0] == "=== Kubernetes Operator Schedule ===", (
        f"Line 1 (header) is wrong.\n"
        f"Expected: '=== Kubernetes Operator Schedule ==='\n"
        f"Got: {repr(lines[0])}"
    )


def test_schedule_api_server_line():
    with open(SCHEDULE_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[1] == "api-server: 1 replicas", (
        f"Line 2 (api-server) is wrong.\n"
        f"Expected: 'api-server: 1 replicas'\n"
        f"Got: {repr(lines[1])}"
    )


def test_schedule_worker_line():
    with open(SCHEDULE_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[2] == "worker: 5 replicas", (
        f"Line 3 (worker) is wrong.\n"
        f"Expected: 'worker: 5 replicas'\n"
        f"Got: {repr(lines[2])}"
    )


def test_schedule_cache_line():
    with open(SCHEDULE_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[3] == "cache: 2 replicas", (
        f"Line 4 (cache) is wrong.\n"
        f"Expected: 'cache: 2 replicas'\n"
        f"Got: {repr(lines[3])}"
    )


def test_schedule_total_throughput_line():
    with open(SCHEDULE_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[4] == "Total throughput: 51", (
        f"Line 5 (total throughput) is wrong.\n"
        f"Expected: 'Total throughput: 51'\n"
        f"Got: {repr(lines[4])}"
    )


def test_schedule_status_line():
    with open(SCHEDULE_PATH, "r") as f:
        lines = f.read().split("\n")
    assert lines[5] == "Status: OPTIMAL", (
        f"Line 6 (status) is wrong.\n"
        f"Expected: 'Status: OPTIMAL'\n"
        f"Got: {repr(lines[5])}"
    )


def test_schedule_no_trailing_spaces_on_any_line():
    with open(SCHEDULE_PATH, "r") as f:
        content = f.read()
    lines = content.split("\n")
    # Check all content lines (not the trailing empty string)
    for i, line in enumerate(lines[:-1], start=1):
        assert line == line.rstrip(), (
            f"Line {i} has trailing spaces.\n"
            f"Got: {repr(line)}"
        )


def test_schedule_throughput_is_correct_for_given_replicas():
    """Verify throughput calculation matches the replica counts."""
    with open(SCHEDULE_PATH, "r") as f:
        lines = f.read().split("\n")

    # Parse replica counts
    api_replicas = int(lines[1].split(": ")[1].split(" ")[0])
    worker_replicas = int(lines[2].split(": ")[1].split(" ")[0])
    cache_replicas = int(lines[3].split(": ")[1].split(" ")[0])
    total_throughput = int(lines[4].split(": ")[1])

    expected_throughput = 5 * api_replicas + 8 * worker_replicas + 3 * cache_replicas
    assert total_throughput == expected_throughput, (
        f"Total throughput {total_throughput} does not match computed value "
        f"5*{api_replicas} + 8*{worker_replicas} + 3*{cache_replicas} = {expected_throughput}"
    )


def test_schedule_cpu_constraint_satisfied():
    """Verify the CPU constraint is not violated."""
    with open(SCHEDULE_PATH, "r") as f:
        lines = f.read().split("\n")

    api_replicas = int(lines[1].split(": ")[1].split(" ")[0])
    worker_replicas = int(lines[2].split(": ")[1].split(" ")[0])
    cache_replicas = int(lines[3].split(": ")[1].split(" ")[0])

    cpu_used = 2 * api_replicas + 4 * worker_replicas + 1 * cache_replicas
    assert cpu_used <= 24, (
        f"CPU constraint violated: 2*{api_replicas} + 4*{worker_replicas} + 1*{cache_replicas} "
        f"= {cpu_used} > 24"
    )


def test_schedule_memory_constraint_satisfied():
    """Verify the memory constraint is not violated."""
    with open(SCHEDULE_PATH, "r") as f:
        lines = f.read().split("\n")

    api_replicas = int(lines[1].split(": ")[1].split(" ")[0])
    worker_replicas = int(lines[2].split(": ")[1].split(" ")[0])
    cache_replicas = int(lines[3].split(": ")[1].split(" ")[0])

    mem_used = 3 * api_replicas + 2 * worker_replicas + 4 * cache_replicas
    assert mem_used <= 24, (
        f"Memory constraint violated: 3*{api_replicas} + 2*{worker_replicas} + 4*{cache_replicas} "
        f"= {mem_used} > 24"
    )


def test_schedule_pod_slot_constraint_satisfied():
    """Verify the pod slot constraint is not violated."""
    with open(SCHEDULE_PATH, "r") as f:
        lines = f.read().split("\n")

    api_replicas = int(lines[1].split(": ")[1].split(" ")[0])
    worker_replicas = int(lines[2].split(": ")[1].split(" ")[0])
    cache_replicas = int(lines[3].split(": ")[1].split(" ")[0])

    total_pods = api_replicas + worker_replicas + cache_replicas
    assert total_pods <= 8, (
        f"Pod slot constraint violated: {api_replicas} + {worker_replicas} + {cache_replicas} "
        f"= {total_pods} > 8"
    )


def test_schedule_replica_bounds_satisfied():
    """Verify each workload has between 1 and 6 replicas."""
    with open(SCHEDULE_PATH, "r") as f:
        lines = f.read().split("\n")

    api_replicas = int(lines[1].split(": ")[1].split(" ")[0])
    worker_replicas = int(lines[2].split(": ")[1].split(" ")[0])
    cache_replicas = int(lines[3].split(": ")[1].split(" ")[0])

    for name, count in [("api-server", api_replicas), ("worker", worker_replicas), ("cache", cache_replicas)]:
        assert 1 <= count <= 6, (
            f"Replica bounds violated for {name}: {count} is not in [1, 6]"
        )


def test_solve_script_references_workloads_json():
    """Verify that solve.py reads from workloads.json (not hardcoded)."""
    with open(SOLVE_SCRIPT_PATH, "r") as f:
        content = f.read()
    assert "workloads.json" in content, (
        f"solve.py does not appear to reference 'workloads.json'.\n"
        "The script must read from /home/user/k8s_optimizer/workloads.json."
    )