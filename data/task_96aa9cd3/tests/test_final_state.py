# test_final_state.py

import os
import pytest

TRIAGE_SUMMARY = "/home/user/oncall/triage_summary.txt"
INCIDENTS_LOG = "/home/user/oncall/incidents.log"

EXPECTED_LINES = [
    "[CRITICAL] INC-0042 | auth-service: Token validation FAILURE",
    "[HIGH] INC-0044 | api-gateway: Upstream connection TIMEOUT",
    "[CRITICAL] INC-0046 | database: Replication FAILURE detected",
    "[HIGH] INC-0047 | auth-service: Session TIMEOUT on login endpoint",
    "[CRITICAL] INC-0049 | payment-service: Payment processing FAILURE",
]

EXPECTED_CONTENT = "\n".join(EXPECTED_LINES)


def test_triage_summary_exists():
    """The triage_summary.txt file must exist at the expected path."""
    assert os.path.isfile(TRIAGE_SUMMARY), (
        f"File '{TRIAGE_SUMMARY}' does not exist. "
        "The triage summary file must be created after processing incidents.log."
    )


def test_triage_summary_is_readable():
    """The triage_summary.txt file must be readable."""
    assert os.access(TRIAGE_SUMMARY, os.R_OK), (
        f"File '{TRIAGE_SUMMARY}' exists but is not readable."
    )


def test_triage_summary_line_count():
    """The triage_summary.txt file must have exactly 5 lines (no blank lines)."""
    with open(TRIAGE_SUMMARY, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    assert len(lines) == 5, (
        f"Expected exactly 5 non-blank lines in '{TRIAGE_SUMMARY}', but found {len(lines)}.\n"
        f"Lines found:\n" + "\n".join(repr(l) for l in lines)
    )


def test_triage_summary_no_blank_lines():
    """The triage_summary.txt file must not contain any blank lines."""
    with open(TRIAGE_SUMMARY, "r") as f:
        all_lines = f.readlines()

    blank_lines = [i + 1 for i, line in enumerate(all_lines) if line.strip() == ""]
    assert not blank_lines, (
        f"Found blank lines in '{TRIAGE_SUMMARY}' at line numbers: {blank_lines}. "
        "The output must have no blank lines."
    )


def test_triage_summary_no_trailing_whitespace():
    """No line in triage_summary.txt should have trailing whitespace."""
    with open(TRIAGE_SUMMARY, "r") as f:
        lines = f.readlines()

    offending = []
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        if stripped != stripped.rstrip():
            offending.append((i, repr(stripped)))

    assert not offending, (
        f"Lines with trailing whitespace found in '{TRIAGE_SUMMARY}':\n"
        + "\n".join(f"  Line {lineno}: {content}" for lineno, content in offending)
    )


def test_triage_summary_exact_content():
    """The triage_summary.txt must contain exactly the expected content."""
    with open(TRIAGE_SUMMARY, "r") as f:
        content = f.read().rstrip("\n")

    assert content == EXPECTED_CONTENT, (
        f"Content of '{TRIAGE_SUMMARY}' does not match expected.\n"
        f"Expected:\n{EXPECTED_CONTENT}\n\n"
        f"Got:\n{content}"
    )


def test_triage_summary_each_line_matches():
    """Each line in triage_summary.txt must exactly match the expected line."""
    with open(TRIAGE_SUMMARY, "r") as f:
        actual_lines = [line.rstrip("\n") for line in f if line.strip()]

    assert len(actual_lines) == len(EXPECTED_LINES), (
        f"Expected {len(EXPECTED_LINES)} lines but got {len(actual_lines)}."
    )

    for i, (expected, actual) in enumerate(zip(EXPECTED_LINES, actual_lines), start=1):
        assert actual == expected, (
            f"Line {i} in '{TRIAGE_SUMMARY}' does not match expected.\n"
            f"  Expected: {expected!r}\n"
            f"  Got:      {actual!r}"
        )


def test_triage_summary_excludes_low_severity():
    """The triage_summary.txt must not contain any LOW severity incidents."""
    with open(TRIAGE_SUMMARY, "r") as f:
        content = f.read()

    assert "INC-0043" not in content, (
        f"INC-0043 (LOW severity) should not appear in '{TRIAGE_SUMMARY}', but it does."
    )
    assert "INC-0048" not in content, (
        f"INC-0048 (LOW severity) should not appear in '{TRIAGE_SUMMARY}', but it does."
    )
    assert "[LOW]" not in content, (
        f"'[LOW]' severity tag should not appear in '{TRIAGE_SUMMARY}', but it does."
    )


def test_triage_summary_excludes_medium_severity():
    """The triage_summary.txt must not contain any MEDIUM severity incidents."""
    with open(TRIAGE_SUMMARY, "r") as f:
        content = f.read()

    assert "INC-0045" not in content, (
        f"INC-0045 (MEDIUM severity) should not appear in '{TRIAGE_SUMMARY}', but it does."
    )
    assert "[MEDIUM]" not in content, (
        f"'[MEDIUM]' severity tag should not appear in '{TRIAGE_SUMMARY}', but it does."
    )


def test_triage_summary_failure_uppercased():
    """All occurrences of 'failure' (case-insensitive) must be replaced with 'FAILURE'."""
    with open(TRIAGE_SUMMARY, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines, start=1):
        # Check that no lowercase/mixed-case 'failure' remains
        import re
        matches = re.findall(r'(?i)failure', line)
        for match in matches:
            assert match == "FAILURE", (
                f"Line {i} in '{TRIAGE_SUMMARY}' contains '{match}' instead of 'FAILURE'.\n"
                f"  Line: {line!r}"
            )


def test_triage_summary_timeout_uppercased():
    """All occurrences of 'timeout' (case-insensitive) must be replaced with 'TIMEOUT'."""
    with open(TRIAGE_SUMMARY, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines, start=1):
        import re
        matches = re.findall(r'(?i)timeout', line)
        for match in matches:
            assert match == "TIMEOUT", (
                f"Line {i} in '{TRIAGE_SUMMARY}' contains '{match}' instead of 'TIMEOUT'.\n"
                f"  Line: {line!r}"
            )


def test_triage_summary_format_brackets():
    """Each line must start with a severity tag in square brackets like [CRITICAL] or [HIGH]."""
    with open(TRIAGE_SUMMARY, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    import re
    pattern = re.compile(r'^\[(CRITICAL|HIGH)\] ')
    for i, line in enumerate(lines, start=1):
        assert pattern.match(line), (
            f"Line {i} in '{TRIAGE_SUMMARY}' does not start with '[CRITICAL] ' or '[HIGH] '.\n"
            f"  Line: {line!r}"
        )


def test_triage_summary_format_pipe_separator():
    """Each line must contain ' | ' separating incident_id from service:message."""
    with open(TRIAGE_SUMMARY, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines, start=1):
        assert " | " in line, (
            f"Line {i} in '{TRIAGE_SUMMARY}' does not contain ' | ' separator.\n"
            f"  Line: {line!r}"
        )


def test_triage_summary_format_colon_separator():
    """Each line must contain ': ' separating service from message."""
    with open(TRIAGE_SUMMARY, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    for i, line in enumerate(lines, start=1):
        assert ": " in line, (
            f"Line {i} in '{TRIAGE_SUMMARY}' does not contain ': ' separating service from message.\n"
            f"  Line: {line!r}"
        )


def test_triage_summary_contains_all_expected_incident_ids():
    """The triage_summary.txt must contain exactly the expected incident IDs."""
    expected_ids = {"INC-0042", "INC-0044", "INC-0046", "INC-0047", "INC-0049"}

    with open(TRIAGE_SUMMARY, "r") as f:
        content = f.read()

    for inc_id in expected_ids:
        assert inc_id in content, (
            f"Expected incident ID '{inc_id}' not found in '{TRIAGE_SUMMARY}'.\n"
            f"Content:\n{content}"
        )


def test_triage_summary_order_matches_original():
    """Lines in triage_summary.txt must appear in the same order as in the original log."""
    with open(TRIAGE_SUMMARY, "r") as f:
        actual_lines = [line.rstrip("\n") for line in f if line.strip()]

    # Extract incident IDs in order from summary
    import re
    id_pattern = re.compile(r'\[(CRITICAL|HIGH)\] (INC-\d+) \|')
    actual_ids = []
    for line in actual_lines:
        m = id_pattern.match(line)
        assert m is not None, (
            f"Could not parse incident ID from line: {line!r}"
        )
        actual_ids.append(m.group(2))

    expected_ids_in_order = ["INC-0042", "INC-0044", "INC-0046", "INC-0047", "INC-0049"]

    assert actual_ids == expected_ids_in_order, (
        f"Incident IDs in '{TRIAGE_SUMMARY}' are not in the expected order.\n"
        f"Expected order: {expected_ids_in_order}\n"
        f"Actual order:   {actual_ids}"
    )


def test_incidents_log_unchanged():
    """The original incidents.log file must remain unchanged after processing."""
    expected_content = (
        "2024-06-01T08:15:00|INC-0042|CRITICAL|auth-service|Token validation failure\n"
        "2024-06-01T08:17:00|INC-0043|LOW|billing-service|Invoice render delay\n"
        "2024-06-01T08:22:00|INC-0044|HIGH|api-gateway|Upstream connection timeout\n"
        "2024-06-01T08:35:00|INC-0045|MEDIUM|cache-layer|Cache miss rate elevated\n"
        "2024-06-01T08:41:00|INC-0046|CRITICAL|database|Replication Failure detected\n"
        "2024-06-01T08:55:00|INC-0047|HIGH|auth-service|Session Timeout on login endpoint\n"
        "2024-06-01T09:03:00|INC-0048|LOW|notifier|Email queue backed up\n"
        "2024-06-01T09:10:00|INC-0049|CRITICAL|payment-service|Payment processing failure"
    )

    with open(INCIDENTS_LOG, "r") as f:
        content = f.read().rstrip("\n")

    assert content == expected_content, (
        f"The original '{INCIDENTS_LOG}' has been modified.\n"
        f"Expected:\n{expected_content}\n\n"
        f"Got:\n{content}"
    )