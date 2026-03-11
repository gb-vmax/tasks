# test_final_state.py

import os
import pytest

REPORT_PATH = "/home/user/monitoring/system_health_report.txt"

EXPECTED_CONTENT = """\
=== SYSTEM HEALTH REPORT ===

-- CPU & MEMORY --
Samples: 10
CPU avg: 68.9%
CPU max: 91.3%
Memory avg usage: 41.9%
Memory peak usage: 48.8%

-- DISK USAGE --
/: 42GB / 100GB (42.0%)
/boot: 0.4GB / 1GB (40.0%)
/home: 310GB / 400GB (77.5%)
/var: 75GB / 80GB (93.8%)

-- PROCESS SUMMARY --
Total snapshots: 11
Unique processes: 4
Zombie processes: 2
Top CPU process: python3 (91.1%)

-- ALERTS --
WARN: CPU spike detected (91.3%)
WARN: Disk /var at 93.8% capacity
WARN: 2 zombie process(es) detected
"""


def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Report file {REPORT_PATH} does not exist. "
        "The task requires generating this file."
    )


def test_report_file_is_readable():
    assert os.access(REPORT_PATH, os.R_OK), (
        f"Report file {REPORT_PATH} exists but is not readable."
    )


def read_report():
    with open(REPORT_PATH, "r") as f:
        return f.read()


def test_report_ends_with_single_newline():
    content = read_report()
    assert content.endswith("\n"), (
        f"Report file {REPORT_PATH} must end with a newline character."
    )
    assert not content.endswith("\n\n"), (
        f"Report file {REPORT_PATH} must end with exactly one trailing newline, "
        "but it ends with more than one."
    )


def test_report_no_trailing_spaces():
    content = read_report()
    lines = content.split("\n")
    # The last element after split on trailing newline will be empty string; skip it
    for i, line in enumerate(lines, start=1):
        assert line == line.rstrip(), (
            f"Line {i} in {REPORT_PATH} has trailing spaces: {line!r}"
        )


def test_report_exact_content():
    content = read_report()
    assert content == EXPECTED_CONTENT, (
        f"Report file {REPORT_PATH} content does not match expected.\n"
        f"--- EXPECTED ---\n{EXPECTED_CONTENT!r}\n"
        f"--- ACTUAL ---\n{content!r}"
    )


def test_report_header():
    content = read_report()
    lines = content.split("\n")
    assert lines[0] == "=== SYSTEM HEALTH REPORT ===", (
        f"First line of report is incorrect. Got: {lines[0]!r}, "
        "expected: '=== SYSTEM HEALTH REPORT ==='"
    )


def test_report_cpu_memory_section():
    content = read_report()
    assert "-- CPU & MEMORY --" in content, (
        "Report is missing the '-- CPU & MEMORY --' section header."
    )
    assert "Samples: 10" in content, (
        "Report CPU & Memory section: 'Samples: 10' not found. "
        "Expected 10 data rows from cpu_mem.csv."
    )
    assert "CPU avg: 68.9%" in content, (
        "Report CPU & Memory section: 'CPU avg: 68.9%' not found. "
        "Expected average CPU of 68.9%."
    )
    assert "CPU max: 91.3%" in content, (
        "Report CPU & Memory section: 'CPU max: 91.3%' not found. "
        "Expected maximum CPU of 91.3%."
    )
    assert "Memory avg usage: 41.9%" in content, (
        "Report CPU & Memory section: 'Memory avg usage: 41.9%' not found. "
        "Expected average memory usage of 41.9%."
    )
    assert "Memory peak usage: 48.8%" in content, (
        "Report CPU & Memory section: 'Memory peak usage: 48.8%' not found. "
        "Expected peak memory usage of 48.8%."
    )


def test_report_disk_usage_section():
    content = read_report()
    assert "-- DISK USAGE --" in content, (
        "Report is missing the '-- DISK USAGE --' section header."
    )
    assert "/: 42GB / 100GB (42.0%)" in content, (
        "Report Disk Usage section: '/: 42GB / 100GB (42.0%)' not found."
    )
    assert "/boot: 0.4GB / 1GB (40.0%)" in content, (
        "Report Disk Usage section: '/boot: 0.4GB / 1GB (40.0%)' not found."
    )
    assert "/home: 310GB / 400GB (77.5%)" in content, (
        "Report Disk Usage section: '/home: 310GB / 400GB (77.5%)' not found."
    )
    assert "/var: 75GB / 80GB (93.8%)" in content, (
        "Report Disk Usage section: '/var: 75GB / 80GB (93.8%)' not found."
    )


def test_report_disk_usage_sorted():
    content = read_report()
    lines = content.split("\n")
    # Find the disk section
    disk_start = None
    for i, line in enumerate(lines):
        if line == "-- DISK USAGE --":
            disk_start = i
            break
    assert disk_start is not None, "Could not find '-- DISK USAGE --' section."

    # Collect disk lines until blank line or next section
    disk_lines = []
    for line in lines[disk_start + 1:]:
        if line == "" or line.startswith("--"):
            break
        disk_lines.append(line)

    assert len(disk_lines) == 4, (
        f"Expected 4 disk usage lines, got {len(disk_lines)}: {disk_lines}"
    )

    # Extract mount points
    mount_points = []
    for line in disk_lines:
        mount = line.split(":")[0]
        mount_points.append(mount)

    assert mount_points == sorted(mount_points), (
        f"Disk mount points are not sorted alphabetically. Got: {mount_points}"
    )

    expected_mounts = ["/", "/boot", "/home", "/var"]
    assert mount_points == expected_mounts, (
        f"Disk mount points do not match expected. "
        f"Expected: {expected_mounts}, got: {mount_points}"
    )


def test_report_process_summary_section():
    content = read_report()
    assert "-- PROCESS SUMMARY --" in content, (
        "Report is missing the '-- PROCESS SUMMARY --' section header."
    )
    assert "Total snapshots: 11" in content, (
        "Report Process Summary section: 'Total snapshots: 11' not found. "
        "Expected 11 lines in processes.log."
    )
    assert "Unique processes: 4" in content, (
        "Report Process Summary section: 'Unique processes: 4' not found. "
        "Expected 4 distinct process names (nginx, postgres, python3, defunct)."
    )
    assert "Zombie processes: 2" in content, (
        "Report Process Summary section: 'Zombie processes: 2' not found. "
        "Expected 2 zombie process entries."
    )
    assert "Top CPU process: python3 (91.1%)" in content, (
        "Report Process Summary section: 'Top CPU process: python3 (91.1%)' not found. "
        "Expected python3 with highest cpu_pct of 91.1%."
    )


def test_report_alerts_section():
    content = read_report()
    assert "-- ALERTS --" in content, (
        "Report is missing the '-- ALERTS --' section header."
    )
    # CPU avg alert should NOT be present (68.9% <= 75.0%)
    assert "WARN: High average CPU usage" not in content, (
        "Report Alerts section: 'WARN: High average CPU usage' should NOT be present. "
        "CPU avg is 68.9% which does not exceed 75.0%."
    )
    # CPU max alert SHOULD be present
    assert "WARN: CPU spike detected (91.3%)" in content, (
        "Report Alerts section: 'WARN: CPU spike detected (91.3%)' not found. "
        "CPU max is 91.3% which exceeds 90.0%."
    )
    # Disk /var alert SHOULD be present
    assert "WARN: Disk /var at 93.8% capacity" in content, (
        "Report Alerts section: 'WARN: Disk /var at 93.8% capacity' not found. "
        "/var is at 93.8% which is >= 80.0%."
    )
    # /home should NOT trigger disk alert (77.5% < 80.0%)
    assert "WARN: Disk /home" not in content, (
        "Report Alerts section: 'WARN: Disk /home' should NOT be present. "
        "/home is at 77.5% which is < 80.0%."
    )
    # Zombie alert SHOULD be present
    assert "WARN: 2 zombie process(es) detected" in content, (
        "Report Alerts section: 'WARN: 2 zombie process(es) detected' not found. "
        "There are 2 zombie processes."
    )
    # No alerts line should NOT be present
    assert "No alerts." not in content, (
        "Report Alerts section: 'No alerts.' should NOT be present since there are alerts."
    )


def test_report_alerts_order():
    content = read_report()
    lines = content.split("\n")

    # Find alerts section
    alerts_start = None
    for i, line in enumerate(lines):
        if line == "-- ALERTS --":
            alerts_start = i
            break
    assert alerts_start is not None, "Could not find '-- ALERTS --' section."

    # Collect alert lines
    alert_lines = []
    for line in lines[alerts_start + 1:]:
        if line == "" or line.startswith("--"):
            break
        if line:
            alert_lines.append(line)

    assert len(alert_lines) == 3, (
        f"Expected 3 alert lines, got {len(alert_lines)}: {alert_lines}"
    )

    expected_alerts = [
        "WARN: CPU spike detected (91.3%)",
        "WARN: Disk /var at 93.8% capacity",
        "WARN: 2 zombie process(es) detected",
    ]

    for i, (actual, expected) in enumerate(zip(alert_lines, expected_alerts)):
        assert actual == expected, (
            f"Alert line {i+1}: expected {expected!r}, got {actual!r}. "
            "Alerts must appear in the specified order."
        )


def test_report_section_order():
    content = read_report()
    lines = content.split("\n")

    section_headers = [
        "=== SYSTEM HEALTH REPORT ===",
        "-- CPU & MEMORY --",
        "-- DISK USAGE --",
        "-- PROCESS SUMMARY --",
        "-- ALERTS --",
    ]

    positions = {}
    for header in section_headers:
        for i, line in enumerate(lines):
            if line == header:
                positions[header] = i
                break
        assert header in positions, (
            f"Section header {header!r} not found in report."
        )

    for i in range(len(section_headers) - 1):
        h1 = section_headers[i]
        h2 = section_headers[i + 1]
        assert positions[h1] < positions[h2], (
            f"Section {h1!r} (line {positions[h1]}) must appear before "
            f"{h2!r} (line {positions[h2]}) in the report."
        )


def test_report_line_by_line():
    content = read_report()
    actual_lines = content.split("\n")
    expected_lines = EXPECTED_CONTENT.split("\n")

    assert len(actual_lines) == len(expected_lines), (
        f"Report has {len(actual_lines)} lines (after split on newline), "
        f"expected {len(expected_lines)} lines."
    )

    for i, (actual, expected) in enumerate(zip(actual_lines, expected_lines), start=1):
        assert actual == expected, (
            f"Line {i} mismatch:\n"
            f"  Expected: {expected!r}\n"
            f"  Actual:   {actual!r}"
        )