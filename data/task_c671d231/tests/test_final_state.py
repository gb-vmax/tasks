# test_final_state.py

import os
import re
import pytest

LOG_FILE = "/home/user/ml_resource_snapshot.log"

@pytest.mark.describe("Final state after resource snapshot log is created")
def test_log_file_exists_and_format_is_correct():
    """
    The resource snapshot log file must exist and strictly conform to the specified format:
    - Three lines, in order:
        1. CPU Usage: X.Y%
        2. Available RAM: NNNN MB
        3. Free Disk Space in /home: M.GB GB
    - No extra lines, headers, or blank lines.
    - Correct number formatting for each field.
    - If the file previously existed, it must be overwritten (not appended to).
    """
    # 1. File exists
    assert os.path.isfile(LOG_FILE), (
        f"The log file {LOG_FILE} does not exist. "
        "You must create this file at the specified absolute path."
    )

    # 2. File contents: no blank lines, exactly 3 lines
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) == 3, (
        f"The log file must contain exactly 3 lines, but it has {len(lines)}. "
        "Check for extra lines or blank lines."
    )

    # 3. Line 1: CPU Usage: X.Y%
    cpu_line = lines[0].rstrip("\n")
    cpu_regex = r"^CPU Usage: ([0-9]+(?:\.[0-9])?)%$"
    cpu_match = re.match(cpu_regex, cpu_line)
    assert cpu_match, (
        f"Line 1 must be in the format 'CPU Usage: X.Y%'. "
        f"Found: '{cpu_line}'"
    )
    cpu_value = cpu_match.group(1)
    # Validate one decimal point
    assert '.' in cpu_value and len(cpu_value.split('.')[-1]) == 1, (
        f"CPU usage must be shown with exactly one decimal (e.g., '5.2%'). "
        f"Found: '{cpu_line}'"
    )
    try:
        cpu_float = float(cpu_value)
        assert 0.0 <= cpu_float <= 100.0, (
            f"CPU usage percentage must be between 0.0 and 100.0. Found: {cpu_float}%"
        )
    except Exception:
        pytest.fail(f"CPU usage value is not a valid float: '{cpu_value}'")

    # 4. Line 2: Available RAM: NNNN MB
    ram_line = lines[1].rstrip("\n")
    ram_regex = r"^Available RAM: ([0-9]+) MB$"
    ram_match = re.match(ram_regex, ram_line)
    assert ram_match, (
        f"Line 2 must be in the format 'Available RAM: NNNN MB'. "
        f"Found: '{ram_line}'"
    )
    ram_value = ram_match.group(1)
    try:
        ram_int = int(ram_value)
        assert ram_int > 0, (
            f"Available RAM must be a positive integer. Found: {ram_int}"
        )
    except Exception:
        pytest.fail(f"Available RAM value is not a valid integer: '{ram_value}'")

    # 5. Line 3: Free Disk Space in /home: M.GB GB
    disk_line = lines[2].rstrip("\n")
    disk_regex = r"^Free Disk Space in /home: ([0-9]+(?:\.[0-9]{2})) GB$"
    disk_match = re.match(disk_regex, disk_line)
    assert disk_match, (
        f"Line 3 must be in the format 'Free Disk Space in /home: M.GB GB'. "
        f"Found: '{disk_line}'"
    )
    disk_value = disk_match.group(1)
    # Validate two decimal places
    assert '.' in disk_value and len(disk_value.split('.')[-1]) == 2, (
        f"Disk space must be shown with exactly two decimals (e.g., '238.45 GB'). "
        f"Found: '{disk_line}'"
    )
    try:
        disk_float = float(disk_value)
        assert disk_float >= 0.0, (
            f"Free disk space must be non-negative. Found: {disk_float} GB"
        )
    except Exception:
        pytest.fail(f"Free disk space value is not a valid float: '{disk_value}'")

    # 6. No extra lines or trailing content
    assert not lines[-1].endswith('\n\n'), (
        "There must be no blank line at the end of the file."
    )