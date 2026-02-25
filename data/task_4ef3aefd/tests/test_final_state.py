# test_final_state.py

import os
import pytest

LOGS_DIR = '/home/user/logs'
SERVICE_STATUS_LOG = '/home/user/logs/service_status.log'
RUNNING_CONTAINERS_CSV = '/home/user/logs/running_containers.csv'

EXPECTED_CSV_LINES = [
    "api-service,micro/api:latest",
    "web-front,company/web:1.2",
    "worker,micro/worker:latest",
]

def test_logs_directory_still_exists():
    assert os.path.isdir(LOGS_DIR), (
        f"Required directory '{LOGS_DIR}' is missing after task completion."
    )

def test_service_status_log_unmodified():
    expected_content = (
        "container_id: a1b2c3; name: api-service; image: micro/api:latest; status: running\n"
        "container_id: d4e5f6; name: db-service; image: micro/db:5.6; status: stopped\n"
        "container_id: g7h8i9; name: web-front; image: company/web:1.2; status: running\n"
        "container_id: j1k2l3; name: cache; image: micro/cache:3.0; status: paused\n"
        "container_id: m4n5o6; name: worker; image: micro/worker:latest; status: running\n"
    )
    assert os.path.isfile(SERVICE_STATUS_LOG), (
        f"Required file '{SERVICE_STATUS_LOG}' is missing after task completion."
    )
    with open(SERVICE_STATUS_LOG, 'r', encoding='utf-8') as f:
        actual = f.read()
    expected = expected_content.replace('\r\n', '\n').replace('\r', '\n')
    actual = actual.replace('\r\n', '\n').replace('\r', '\n')
    assert actual == expected, (
        f"'{SERVICE_STATUS_LOG}' was modified during the task. It must remain unchanged.\n"
        "Expected content:\n"
        "----------------\n"
        f"{expected}"
        "----------------\n"
        "Actual content:\n"
        "----------------\n"
        f"{actual}"
        "----------------\n"
    )

def test_running_containers_csv_created_with_correct_content():
    assert os.path.isfile(RUNNING_CONTAINERS_CSV), (
        f"Output file '{RUNNING_CONTAINERS_CSV}' does not exist after the task."
    )
    with open(RUNNING_CONTAINERS_CSV, 'r', encoding='utf-8') as f:
        lines = f.read().replace('\r\n', '\n').replace('\r', '\n').split('\n')
    # Remove trailing empty line if present
    if lines and lines[-1] == '':
        lines = lines[:-1]
    assert lines == EXPECTED_CSV_LINES, (
        f"'{RUNNING_CONTAINERS_CSV}' does not have the expected content.\n"
        "Expected lines:\n"
        "----------------\n"
        f"{chr(10).join(EXPECTED_CSV_LINES)}\n"
        "----------------\n"
        "Actual lines:\n"
        "----------------\n"
        f"{chr(10).join(lines)}\n"
        "----------------\n"
        "Make sure there are NO extra blank lines, headers, or spaces. Each line must be '<name>,<image>' for running containers only."
    )

def test_running_containers_csv_has_no_header_or_extra_spaces():
    with open(RUNNING_CONTAINERS_CSV, 'r', encoding='utf-8') as f:
        lines = f.read().replace('\r\n', '\n').replace('\r', '\n').split('\n')
    # Remove trailing empty line if present
    if lines and lines[-1] == '':
        lines = lines[:-1]
    for idx, line in enumerate(lines):
        assert ',' in line, (
            f"Line {idx+1} in '{RUNNING_CONTAINERS_CSV}' does not contain a comma: '{line}'"
        )
        parts = line.split(',')
        assert len(parts) == 2, (
            f"Line {idx+1} in '{RUNNING_CONTAINERS_CSV}' does not have exactly one comma: '{line}'"
        )
        name, image = parts
        assert name == name.strip(), (
            f"Line {idx+1}: Container name in '{RUNNING_CONTAINERS_CSV}' has leading/trailing spaces: '{name}'"
        )
        assert image == image.strip(), (
            f"Line {idx+1}: Image in '{RUNNING_CONTAINERS_CSV}' has leading/trailing spaces: '{image}'"
        )
        assert not name.startswith(' ') and not name.endswith(' '), (
            f"Line {idx+1}: Extra spaces found around container name: '{name}'"
        )
        assert not image.startswith(' ') and not image.endswith(' '), (
            f"Line {idx+1}: Extra spaces found around image: '{image}'"
        )

def test_no_extra_files_created_in_logs_dir():
    allowed_files = {'service_status.log', 'running_containers.csv'}
    actual_files = set(
        f for f in os.listdir(LOGS_DIR)
        if os.path.isfile(os.path.join(LOGS_DIR, f))
    )
    extra_files = actual_files - allowed_files
    assert not extra_files, (
        f"Unexpected files found in '{LOGS_DIR}': {sorted(extra_files)}\n"
        "Only 'service_status.log' and 'running_containers.csv' should exist after the task."
    )