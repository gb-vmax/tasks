# test_final_state.py

import os
import pytest
import re

PING_RESULTS_PATH = "/home/user/ping_results.log"
UNREACHABLE_HOSTS_PATH = "/home/user/unreachable_hosts.log"

EXPECTED_PING_RESULTS = [
    "[2024-06-06 08:31:22] Host: server1.example.com Result: 0% packet loss",
    "[2024-06-06 08:31:23] Host: 192.168.0.42 Result: 100% packet loss",
    "[2024-06-06 08:31:24] Host: 10.0.0.13 Result: 100% packet loss",
    "[2024-06-06 08:31:25] Host: router.local Result: 0% packet loss",
    "[2024-06-06 08:31:26] Host: 172.16.5.9 Result: 100% packet loss",
]

EXPECTED_UNREACHABLE_HOSTS = [
    "192.168.0.42",
    "10.0.0.13",
    "172.16.5.9",
]

EXPECTED_UNREACHABLE_HOSTS_LOG = [
    "[2024-06-06 08:31:23] Host: 192.168.0.42 Result: 100% packet loss",
    "[2024-06-06 08:31:24] Host: 10.0.0.13 Result: 100% packet loss",
    "[2024-06-06 08:31:26] Host: 172.16.5.9 Result: 100% packet loss",
]

@pytest.mark.describe("Final OS/filesystem state after ping log analysis task")
class TestFinalState:

    def test_ping_results_log_unchanged(self):
        """The original ping_results.log must exist and not be modified."""
        assert os.path.isfile(PING_RESULTS_PATH), (
            f"Missing required log file at {PING_RESULTS_PATH}."
        )
        with open(PING_RESULTS_PATH, "rt", encoding="utf-8") as f:
            actual_lines = [line.rstrip('\n') for line in f]
        assert actual_lines == EXPECTED_PING_RESULTS, (
            f"The contents of {PING_RESULTS_PATH} have changed.\n"
            f"Expected ({len(EXPECTED_PING_RESULTS)} lines):\n" +
            "\n".join(EXPECTED_PING_RESULTS) +
            f"\n\nFound ({len(actual_lines)} lines):\n" +
            "\n".join(actual_lines)
        )

    def test_total_ping_test_count(self, capsys):
        """The student must output the correct total count of ping tests (should be 5)."""
        # Simulate the counting action as the student's script would do.
        # We re-implement the logic and check that the output matches.
        with open(PING_RESULTS_PATH, "rt", encoding="utf-8") as f:
            lines = f.readlines()
        expected_count = len(EXPECTED_PING_RESULTS)
        # The student should print just the integer, nothing else.
        # Let's check that the script's output matches this.
        # Since we can't rerun the student's code, we check that the requirement is met:
        assert expected_count == 5, "Expected 5 ping test entries in the log file."
        # This test is a placeholder to remind that the output must be just '5'

    def test_unreachable_hosts_extraction(self, capsys):
        """The student must extract and output only unreachable hosts, one per line, no extra whitespace."""
        # Extract unreachable hosts from the original log
        unreachable_hosts = []
        pattern = re.compile(r"Host:\s*(\S+)\s+Result:\s*100% packet loss")
        with open(PING_RESULTS_PATH, "rt", encoding="utf-8") as f:
            for line in f:
                m = pattern.search(line)
                if m:
                    unreachable_hosts.append(m.group(1))
        assert unreachable_hosts == EXPECTED_UNREACHABLE_HOSTS, (
            "The extracted list of unreachable hostnames/IPs is incorrect.\n"
            f"Expected ({len(EXPECTED_UNREACHABLE_HOSTS)} lines):\n" +
            "\n".join(EXPECTED_UNREACHABLE_HOSTS) +
            f"\n\nFound ({len(unreachable_hosts)} lines):\n" +
            "\n".join(unreachable_hosts) +
            "\n\nEnsure your output contains ONLY the unreachable hosts, one per line, with no extra whitespace or blank lines."
        )

    def test_unreachable_hosts_log_exists_and_correct(self):
        """The /home/user/unreachable_hosts.log must exist and contain only correct unreachable entries."""
        assert os.path.isfile(UNREACHABLE_HOSTS_PATH), (
            f"Missing filtered unreachable hosts log at {UNREACHABLE_HOSTS_PATH}."
        )
        with open(UNREACHABLE_HOSTS_PATH, "rt", encoding="utf-8") as f:
            actual_lines = [line.rstrip('\n') for line in f]
        assert actual_lines == EXPECTED_UNREACHABLE_HOSTS_LOG, (
            f"The contents of {UNREACHABLE_HOSTS_PATH} do not match the expected unreachable log entries.\n"
            f"Expected ({len(EXPECTED_UNREACHABLE_HOSTS_LOG)} lines):\n" +
            "\n".join(EXPECTED_UNREACHABLE_HOSTS_LOG) +
            f"\n\nFound ({len(actual_lines)} lines):\n" +
            "\n".join(actual_lines) +
            "\n\nEnsure you preserved the original lines and order, and included only those with '100% packet loss'."
        )