# test_final_state.py

import os
import pytest

REPORT_FILE = "/home/user/iot_logs/telemetry_report.txt"

EXPECTED_CONTENT = """\
=== IoT Telemetry Frequency Report ===

[ZONE: factory]
Total events: 20
Distinct codes: 5
Top 3:
  1. ERR_SENSOR_TIMEOUT (7)
  2. INFO_HEARTBEAT (5)
  3. WARN_LOW_BATTERY (4)

[ZONE: warehouse]
Total events: 20
Distinct codes: 5
Top 3:
  1. WARN_LOW_BATTERY (7)
  2. ERR_COMM_FAILURE (5)
  3. INFO_HEARTBEAT (4)

[ZONE: outdoor]
Total events: 20
Distinct codes: 5
Top 3:
  1. WARN_TEMP_HIGH (8)
  2. ERR_COMM_FAILURE (5)
  3. INFO_HEARTBEAT (4)

[CROSS-ZONE]
Codes present in all 3 zones: ERR_COMM_FAILURE,ERR_SENSOR_TIMEOUT,INFO_HEARTBEAT,WARN_LOW_BATTERY,WARN_TEMP_HIGH
Grand total events: 60"""


def read_report():
    with open(REPORT_FILE, "r") as f:
        return f.read()


def test_report_file_exists():
    assert os.path.isfile(REPORT_FILE), (
        f"Report file {REPORT_FILE} does not exist. "
        "The task requires writing the telemetry report to this path."
    )


def test_report_file_not_empty():
    content = read_report()
    assert content.strip(), (
        f"Report file {REPORT_FILE} is empty. It should contain the telemetry report."
    )


def test_report_no_trailing_newline():
    content = read_report()
    assert not content.endswith("\n"), (
        f"Report file {REPORT_FILE} must NOT have a trailing newline at the end, "
        f"but the file ends with a newline character."
    )


def test_report_exact_content():
    content = read_report()
    assert content == EXPECTED_CONTENT, (
        f"Report file {REPORT_FILE} does not match the expected content.\n"
        f"--- EXPECTED ---\n{EXPECTED_CONTENT!r}\n"
        f"--- ACTUAL ---\n{content!r}"
    )


def test_report_header_line():
    content = read_report()
    lines = content.split("\n")
    assert lines[0] == "=== IoT Telemetry Frequency Report ===", (
        f"First line of report should be '=== IoT Telemetry Frequency Report ===' "
        f"but got: {lines[0]!r}"
    )


def test_report_factory_zone_header():
    content = read_report()
    assert "[ZONE: factory]" in content, (
        "Report is missing '[ZONE: factory]' section header."
    )


def test_report_warehouse_zone_header():
    content = read_report()
    assert "[ZONE: warehouse]" in content, (
        "Report is missing '[ZONE: warehouse]' section header."
    )


def test_report_outdoor_zone_header():
    content = read_report()
    assert "[ZONE: outdoor]" in content, (
        "Report is missing '[ZONE: outdoor]' section header."
    )


def test_report_cross_zone_header():
    content = read_report()
    assert "[CROSS-ZONE]" in content, (
        "Report is missing '[CROSS-ZONE]' section header."
    )


def test_report_factory_total_events():
    content = read_report()
    assert "Total events: 20" in content, (
        "Report should contain 'Total events: 20' for the factory zone "
        "(20 non-blank lines in zone_factory.log)."
    )


def test_report_factory_distinct_codes():
    content = read_report()
    # Check within the factory section specifically
    lines = content.split("\n")
    factory_idx = lines.index("[ZONE: factory]")
    factory_section = "\n".join(lines[factory_idx:factory_idx + 7])
    assert "Distinct codes: 5" in factory_section, (
        f"Factory zone section should have 'Distinct codes: 5', "
        f"but factory section is:\n{factory_section}"
    )


def test_report_factory_top3():
    content = read_report()
    lines = content.split("\n")
    factory_idx = lines.index("[ZONE: factory]")
    factory_section_lines = lines[factory_idx:factory_idx + 8]
    factory_section = "\n".join(factory_section_lines)

    assert "  1. ERR_SENSOR_TIMEOUT (7)" in factory_section, (
        f"Factory zone Top 3 #1 should be '  1. ERR_SENSOR_TIMEOUT (7)'. "
        f"Factory section:\n{factory_section}"
    )
    assert "  2. INFO_HEARTBEAT (5)" in factory_section, (
        f"Factory zone Top 3 #2 should be '  2. INFO_HEARTBEAT (5)'. "
        f"Factory section:\n{factory_section}"
    )
    assert "  3. WARN_LOW_BATTERY (4)" in factory_section, (
        f"Factory zone Top 3 #3 should be '  3. WARN_LOW_BATTERY (4)'. "
        f"Factory section:\n{factory_section}"
    )


def test_report_warehouse_total_events():
    content = read_report()
    lines = content.split("\n")
    warehouse_idx = lines.index("[ZONE: warehouse]")
    warehouse_section = "\n".join(lines[warehouse_idx:warehouse_idx + 7])
    assert "Total events: 20" in warehouse_section, (
        f"Warehouse zone section should have 'Total events: 20', "
        f"but warehouse section is:\n{warehouse_section}"
    )


def test_report_warehouse_distinct_codes():
    content = read_report()
    lines = content.split("\n")
    warehouse_idx = lines.index("[ZONE: warehouse]")
    warehouse_section = "\n".join(lines[warehouse_idx:warehouse_idx + 7])
    assert "Distinct codes: 5" in warehouse_section, (
        f"Warehouse zone section should have 'Distinct codes: 5', "
        f"but warehouse section is:\n{warehouse_section}"
    )


def test_report_warehouse_top3():
    content = read_report()
    lines = content.split("\n")
    warehouse_idx = lines.index("[ZONE: warehouse]")
    warehouse_section_lines = lines[warehouse_idx:warehouse_idx + 8]
    warehouse_section = "\n".join(warehouse_section_lines)

    assert "  1. WARN_LOW_BATTERY (7)" in warehouse_section, (
        f"Warehouse zone Top 3 #1 should be '  1. WARN_LOW_BATTERY (7)'. "
        f"Warehouse section:\n{warehouse_section}"
    )
    assert "  2. ERR_COMM_FAILURE (5)" in warehouse_section, (
        f"Warehouse zone Top 3 #2 should be '  2. ERR_COMM_FAILURE (5)'. "
        f"Warehouse section:\n{warehouse_section}"
    )
    assert "  3. INFO_HEARTBEAT (4)" in warehouse_section, (
        f"Warehouse zone Top 3 #3 should be '  3. INFO_HEARTBEAT (4)'. "
        f"Warehouse section:\n{warehouse_section}"
    )


def test_report_outdoor_total_events():
    content = read_report()
    lines = content.split("\n")
    outdoor_idx = lines.index("[ZONE: outdoor]")
    outdoor_section = "\n".join(lines[outdoor_idx:outdoor_idx + 7])
    assert "Total events: 20" in outdoor_section, (
        f"Outdoor zone section should have 'Total events: 20', "
        f"but outdoor section is:\n{outdoor_section}"
    )


def test_report_outdoor_distinct_codes():
    content = read_report()
    lines = content.split("\n")
    outdoor_idx = lines.index("[ZONE: outdoor]")
    outdoor_section = "\n".join(lines[outdoor_idx:outdoor_idx + 7])
    assert "Distinct codes: 5" in outdoor_section, (
        f"Outdoor zone section should have 'Distinct codes: 5', "
        f"but outdoor section is:\n{outdoor_section}"
    )


def test_report_outdoor_top3():
    content = read_report()
    lines = content.split("\n")
    outdoor_idx = lines.index("[ZONE: outdoor]")
    outdoor_section_lines = lines[outdoor_idx:outdoor_idx + 8]
    outdoor_section = "\n".join(outdoor_section_lines)

    assert "  1. WARN_TEMP_HIGH (8)" in outdoor_section, (
        f"Outdoor zone Top 3 #1 should be '  1. WARN_TEMP_HIGH (8)'. "
        f"Outdoor section:\n{outdoor_section}"
    )
    assert "  2. ERR_COMM_FAILURE (5)" in outdoor_section, (
        f"Outdoor zone Top 3 #2 should be '  2. ERR_COMM_FAILURE (5)'. "
        f"Outdoor section:\n{outdoor_section}"
    )
    assert "  3. INFO_HEARTBEAT (4)" in outdoor_section, (
        f"Outdoor zone Top 3 #3 should be '  3. INFO_HEARTBEAT (4)'. "
        f"Outdoor section:\n{outdoor_section}"
    )


def test_report_cross_zone_codes():
    content = read_report()
    expected_line = (
        "Codes present in all 3 zones: "
        "ERR_COMM_FAILURE,ERR_SENSOR_TIMEOUT,INFO_HEARTBEAT,WARN_LOW_BATTERY,WARN_TEMP_HIGH"
    )
    assert expected_line in content, (
        f"Report should contain the cross-zone codes line:\n  {expected_line!r}\n"
        f"All 5 event codes appear in all 3 zone files, sorted alphabetically, "
        f"comma-separated with no spaces."
    )


def test_report_grand_total():
    content = read_report()
    assert "Grand total events: 60" in content, (
        "Report should contain 'Grand total events: 60' "
        "(20 events per zone × 3 zones = 60 total)."
    )


def test_report_zone_order():
    """Zones must appear in order: factory, warehouse, outdoor."""
    content = read_report()
    factory_pos = content.find("[ZONE: factory]")
    warehouse_pos = content.find("[ZONE: warehouse]")
    outdoor_pos = content.find("[ZONE: outdoor]")
    cross_pos = content.find("[CROSS-ZONE]")

    assert factory_pos != -1, "Missing [ZONE: factory] section."
    assert warehouse_pos != -1, "Missing [ZONE: warehouse] section."
    assert outdoor_pos != -1, "Missing [ZONE: outdoor] section."
    assert cross_pos != -1, "Missing [CROSS-ZONE] section."

    assert factory_pos < warehouse_pos, (
        "factory zone section must appear before warehouse zone section."
    )
    assert warehouse_pos < outdoor_pos, (
        "warehouse zone section must appear before outdoor zone section."
    )
    assert outdoor_pos < cross_pos, (
        "outdoor zone section must appear before [CROSS-ZONE] section."
    )


def test_report_blank_lines_between_sections():
    """There must be a blank line between each zone section and before [CROSS-ZONE]."""
    content = read_report()
    lines = content.split("\n")

    # Find section positions
    section_headers = [
        "[ZONE: factory]",
        "[ZONE: warehouse]",
        "[ZONE: outdoor]",
        "[CROSS-ZONE]",
    ]

    header_positions = {}
    for i, line in enumerate(lines):
        for header in section_headers:
            if line == header:
                header_positions[header] = i

    for header in section_headers:
        assert header in header_positions, f"Could not find section header: {header!r}"

    # Each section header (except the first) should be preceded by a blank line
    for header in ["[ZONE: warehouse]", "[ZONE: outdoor]", "[CROSS-ZONE]"]:
        idx = header_positions[header]
        assert idx > 0 and lines[idx - 1] == "", (
            f"There should be a blank line immediately before '{header}' "
            f"(line {idx + 1}), but line {idx} is: {lines[idx - 1]!r}"
        )


def test_report_top3_indentation():
    """Top 3 entries must use exactly 2-space indentation before the number."""
    content = read_report()
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("  1. ") or line.startswith("  2. ") or line.startswith("  3. "):
            # Correct: exactly 2 spaces
            assert line[0:2] == "  " and line[2] != " ", (
                f"Line {i + 1} has incorrect indentation: {line!r}. "
                "Top 3 entries must have exactly 2 spaces before the number."
            )


def test_report_cross_zone_no_spaces_in_codes_list():
    """The codes list must be comma-separated with NO spaces."""
    content = read_report()
    for line in content.split("\n"):
        if line.startswith("Codes present in all 3 zones:"):
            codes_part = line.split(": ", 1)[1]
            if codes_part != "NONE":
                assert " " not in codes_part, (
                    f"Codes list must have NO spaces between commas, "
                    f"but got: {codes_part!r}"
                )
            break
    else:
        pytest.fail("Could not find 'Codes present in all 3 zones:' line in report.")