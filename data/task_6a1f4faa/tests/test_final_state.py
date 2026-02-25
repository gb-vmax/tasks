# test_final_state.py

import os
import pytest

HOME = "/home/user"
TARGETS_TXT = os.path.join(HOME, "targets.txt")
VULNSCAN_RESULTS = os.path.join(HOME, "vulnscan_results.txt")
REPORT_SUMMARY = os.path.join(HOME, "report_summary.log")

TARGETS_CONTENT = [
    "web1.corp.local",
    "192.168.10.5",
    "dbserver.corp.local",
    "router01",
]

VULNSCAN_ENTRY = (
    "[SCAN] {target}\n"
    "Ports:\n"
    "80/tcp open\n"
    "443/tcp closed\n"
    "22/tcp open\n"
    "Vulnerabilities:\n"
    "CVE-2021-1234: LOW\n"
    "CVE-2019-8903: HIGH\n"
    "---\n"
)

VULNSCAN_EXPECTED = "".join(
    [
        VULNSCAN_ENTRY.format(target=target)
        for target in TARGETS_CONTENT
    ]
)

REPORT_SUMMARY_EXPECTED = (
    "Targets scanned: 4\n"
    "Open ports found: 2\n"
    "Vulnerability counts:\n"
    "CVE-2021-1234 (LOW): 4 times\n"
    "CVE-2019-8903 (HIGH): 4 times\n"
)

@pytest.mark.final
def test_targets_txt_still_exists_and_unchanged():
    """Check that /home/user/targets.txt still exists and is unchanged."""
    assert os.path.isfile(TARGETS_TXT), (
        f"Missing file: {TARGETS_TXT}\n"
        "The targets file must remain present after completion."
    )
    with open(TARGETS_TXT, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    assert lines == TARGETS_CONTENT, (
        f"{TARGETS_TXT} contents have changed after completion.\n"
        f"Expected:\n{TARGETS_CONTENT}\nGot:\n{lines}"
    )

@pytest.mark.final
def test_vulnscan_results_exists_and_correct():
    """Check that /home/user/vulnscan_results.txt exists and contents are exactly as required."""
    assert os.path.isfile(VULNSCAN_RESULTS), (
        f"Missing file: {VULNSCAN_RESULTS}\n"
        "You must create the vulnerability scan results file at the correct location."
    )
    with open(VULNSCAN_RESULTS, "r", encoding="utf-8") as f:
        actual = f.read()
    assert actual == VULNSCAN_EXPECTED, (
        f"{VULNSCAN_RESULTS} contents are incorrect.\n"
        "Expected exactly:\n"
        f"{VULNSCAN_EXPECTED!r}\n"
        "But got:\n"
        f"{actual!r}\n"
        "Check for missing/extra lines, whitespace, and entry formatting."
    )

@pytest.mark.final
def test_report_summary_log_exists_and_correct():
    """Check that /home/user/report_summary.log exists and contents are exactly as required."""
    assert os.path.isfile(REPORT_SUMMARY), (
        f"Missing file: {REPORT_SUMMARY}\n"
        "You must create the summary report at the correct location."
    )
    with open(REPORT_SUMMARY, "r", encoding="utf-8") as f:
        actual = f.read()
    assert actual == REPORT_SUMMARY_EXPECTED, (
        f"{REPORT_SUMMARY} contents are incorrect.\n"
        "Expected exactly:\n"
        f"{REPORT_SUMMARY_EXPECTED!r}\n"
        "But got:\n"
        f"{actual!r}\n"
        "Check target count, open port count, vulnerability counts, and formatting."
    )