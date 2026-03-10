# test_final_state.py

import os
import pytest

ALERTS_PATH = "/home/user/alerts.txt"

EXPECTED_LINES = [
    "ALERT: /boot is at 85% capacity (170G used of 200G)",
    "ALERT: /data is at 90% capacity (900G used of 1.0T)",
    "ALERT: /var/log is at 98% capacity (294G used of 300G)",
    "ALERT: /home is at 80% capacity (480G used of 600G)",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES) + "\n"


def read_alerts():
    with open(ALERTS_PATH, "r") as f:
        return f.read()


def test_alerts_file_exists():
    assert os.path.isfile(ALERTS_PATH), (
        f"Output file '{ALERTS_PATH}' does not exist. "
        "The task requires creating this file with alert lines."
    )


def test_alerts_file_is_readable():
    assert os.access(ALERTS_PATH, os.R_OK), (
        f"File '{ALERTS_PATH}' exists but is not readable."
    )


def test_alerts_file_exact_content():
    content = read_alerts()
    assert content == EXPECTED_CONTENT, (
        f"Content of '{ALERTS_PATH}' does not match expected.\n"
        f"Expected (repr): {repr(EXPECTED_CONTENT)}\n"
        f"Actual   (repr): {repr(content)}"
    )


def test_alerts_file_line_count():
    content = read_alerts()
    lines = content.splitlines()
    assert len(lines) == 4, (
        f"Expected exactly 4 lines in '{ALERTS_PATH}', but found {len(lines)}.\n"
        f"Lines found: {lines}"
    )


def test_alerts_line_1_boot():
    content = read_alerts()
    lines = content.splitlines()
    expected = "ALERT: /boot is at 85% capacity (170G used of 200G)"
    assert lines[0] == expected, (
        f"Line 1 of '{ALERTS_PATH}' is incorrect.\n"
        f"Expected: {repr(expected)}\n"
        f"Actual:   {repr(lines[0])}"
    )


def test_alerts_line_2_data():
    content = read_alerts()
    lines = content.splitlines()
    expected = "ALERT: /data is at 90% capacity (900G used of 1.0T)"
    assert lines[1] == expected, (
        f"Line 2 of '{ALERTS_PATH}' is incorrect.\n"
        f"Expected: {repr(expected)}\n"
        f"Actual:   {repr(lines[1])}"
    )


def test_alerts_line_3_var_log():
    content = read_alerts()
    lines = content.splitlines()
    expected = "ALERT: /var/log is at 98% capacity (294G used of 300G)"
    assert lines[2] == expected, (
        f"Line 3 of '{ALERTS_PATH}' is incorrect.\n"
        f"Expected: {repr(expected)}\n"
        f"Actual:   {repr(lines[2])}"
    )


def test_alerts_line_4_home():
    content = read_alerts()
    lines = content.splitlines()
    expected = "ALERT: /home is at 80% capacity (480G used of 600G)"
    assert lines[3] == expected, (
        f"Line 4 of '{ALERTS_PATH}' is incorrect.\n"
        f"Expected: {repr(expected)}\n"
        f"Actual:   {repr(lines[3])}"
    )


def test_alerts_excludes_sda1_24_percent():
    content = read_alerts()
    assert "/dev/sda1" not in content, (
        f"'/dev/sda1' (24% usage) should NOT appear in '{ALERTS_PATH}' "
        "because 24% < 80%."
    )
    # Also check the mount point is not present as an alert
    assert "ALERT: / is at" not in content, (
        f"Mount point '/' (/dev/sda1, 24%) should NOT appear as an ALERT in '{ALERTS_PATH}'."
    )


def test_alerts_excludes_sdc1_27_percent():
    content = read_alerts()
    assert "/dev/sdc1" not in content, (
        f"'/dev/sdc1' (27% usage) should NOT appear in '{ALERTS_PATH}' "
        "because 27% < 80%."
    )
    assert "ALERT: /backup is at" not in content, (
        f"Mount point '/backup' (/dev/sdc1, 27%) should NOT appear as an ALERT in '{ALERTS_PATH}'."
    )


def test_alerts_excludes_sdd1_78_percent():
    content = read_alerts()
    assert "/dev/sdd1" not in content, (
        f"'/dev/sdd1' (78% usage) should NOT appear in '{ALERTS_PATH}' "
        "because 78% < 80%."
    )
    assert "ALERT: /tmp is at" not in content, (
        f"Mount point '/tmp' (/dev/sdd1, 78%) should NOT appear as an ALERT in '{ALERTS_PATH}'."
    )


def test_alerts_includes_sdd2_80_percent():
    content = read_alerts()
    assert "ALERT: /home is at 80% capacity (480G used of 600G)" in content, (
        f"'/dev/sdd2' (80% usage) MUST appear in '{ALERTS_PATH}' "
        "because 80% >= 80% (boundary condition)."
    )


def test_alerts_header_not_present():
    content = read_alerts()
    assert "Filesystem" not in content, (
        f"The header line starting with 'Filesystem' must NOT appear in '{ALERTS_PATH}'."
    )


def test_alerts_all_lines_start_with_alert_prefix():
    content = read_alerts()
    lines = content.splitlines()
    for i, line in enumerate(lines, start=1):
        assert line.startswith("ALERT: "), (
            f"Line {i} in '{ALERTS_PATH}' does not start with 'ALERT: '.\n"
            f"Line content: {repr(line)}"
        )


def test_alerts_percent_signs_preserved():
    content = read_alerts()
    lines = content.splitlines()
    for i, line in enumerate(lines, start=1):
        assert "%" in line, (
            f"Line {i} in '{ALERTS_PATH}' is missing the '%' sign.\n"
            f"Line content: {repr(line)}"
        )


def test_alerts_order_matches_input():
    content = read_alerts()
    lines = content.splitlines()
    # Verify the order: /boot, /data, /var/log, /home
    mount_points = []
    for line in lines:
        # Extract mount point from "ALERT: <mount> is at ..."
        parts = line.split()
        if len(parts) >= 2:
            mount_points.append(parts[1])
    assert mount_points == ["/boot", "/data", "/var/log", "/home"], (
        f"Lines in '{ALERTS_PATH}' are not in the correct order (matching input file order).\n"
        f"Expected mount point order: ['/boot', '/data', '/var/log', '/home']\n"
        f"Actual mount point order:   {mount_points}"
    )


def test_alerts_no_extra_blank_lines():
    content = read_alerts()
    lines = content.splitlines()
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"'{ALERTS_PATH}' contains unexpected blank lines at positions: {blank_lines}"
    )


def test_alerts_ends_with_single_newline():
    content = read_alerts()
    assert content.endswith("\n"), (
        f"'{ALERTS_PATH}' should end with a newline character."
    )
    assert not content.endswith("\n\n"), (
        f"'{ALERTS_PATH}' should not end with multiple trailing newlines."
    )