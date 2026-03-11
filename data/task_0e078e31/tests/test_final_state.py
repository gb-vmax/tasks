# test_final_state.py

import hashlib
import os
import pytest

ARTIFACTS_DIR = "/home/user/artifacts"
REPORT_PATH = "/home/user/artifacts/verification_report.txt"

EXPECTED_JARS = sorted([
    "app-core-1.0.jar",
    "app-ui-2.1.jar",
    "app-utils-1.4.jar",
])

SEPARATOR = "=" * 35


def compute_sha256(filepath):
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def read_stored_sha256(sha_path):
    with open(sha_path, "rb") as f:
        return f.read().strip().decode("ascii")


def get_expected_report_lines():
    """Dynamically compute the expected report based on actual file state."""
    results = []
    passed = 0
    failed = 0

    for jar in EXPECTED_JARS:
        jar_path = os.path.join(ARTIFACTS_DIR, jar)
        sha_path = os.path.join(ARTIFACTS_DIR, jar.replace(".jar", ".sha256"))

        actual = compute_sha256(jar_path)
        stored = read_stored_sha256(sha_path)

        if actual == stored:
            status = "OK"
            passed += 1
        else:
            status = "CORRUPTED"
            failed += 1

        results.append((jar, status))

    total = len(results)
    lines = []
    lines.append("Build Artifact Verification Report")
    lines.append(SEPARATOR)
    for jar, status in results:
        lines.append(f"{jar}: {status}")
    lines.append(SEPARATOR)
    lines.append(f"Total: {total} | Passed: {passed} | Failed: {failed}")

    return lines, passed, failed, total


# ── Tests ──────────────────────────────────────────────────────────────────────

def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Verification report '{REPORT_PATH}' does not exist. "
        "The student must write the report to this path."
    )


def test_report_is_not_empty():
    size = os.path.getsize(REPORT_PATH)
    assert size > 0, (
        f"Verification report '{REPORT_PATH}' is empty (0 bytes)."
    )


def test_report_header_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 1, "Report has no lines at all."
    assert lines[0] == "Build Artifact Verification Report", (
        f"First line of report must be exactly 'Build Artifact Verification Report', "
        f"but got: {lines[0]!r}"
    )


def test_report_opening_separator():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) >= 2, "Report has fewer than 2 lines."
    assert lines[1] == SEPARATOR, (
        f"Second line of report must be exactly 35 '=' characters, "
        f"but got: {lines[1]!r} (length {len(lines[1])})"
    )


def test_report_closing_separator():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    # The closing separator is the second-to-last line
    assert len(lines) >= 6, (
        f"Report should have at least 6 lines (header, sep, 3 jar lines, sep, summary), "
        f"but only has {len(lines)}."
    )
    closing_sep_index = len(lines) - 2
    assert lines[closing_sep_index] == SEPARATOR, (
        f"Second-to-last line of report must be exactly 35 '=' characters, "
        f"but got: {lines[closing_sep_index]!r} (length {len(lines[closing_sep_index])})"
    )


def test_report_artifact_lines_sorted_alphabetically():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    # Artifact lines are between the two separators (indices 2 to len-3 inclusive)
    assert len(lines) >= 6, (
        f"Report should have at least 6 lines, but only has {len(lines)}."
    )
    artifact_lines = lines[2:-2]
    jar_names_in_report = []
    for line in artifact_lines:
        assert ": OK" in line or ": CORRUPTED" in line, (
            f"Artifact line does not match expected format '<filename>: OK' or "
            f"'<filename>: CORRUPTED': {line!r}"
        )
        jar_name = line.split(": ")[0]
        jar_names_in_report.append(jar_name)

    assert jar_names_in_report == sorted(jar_names_in_report), (
        f"Artifact lines are not sorted alphabetically. "
        f"Found order: {jar_names_in_report}, expected: {sorted(jar_names_in_report)}"
    )


def test_report_contains_all_jars():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    artifact_lines = lines[2:-2]
    jar_names_in_report = [line.split(": ")[0] for line in artifact_lines]

    assert sorted(jar_names_in_report) == EXPECTED_JARS, (
        f"Report should contain exactly these JAR files: {EXPECTED_JARS}, "
        f"but found: {sorted(jar_names_in_report)}"
    )


def test_report_no_directory_paths_in_artifact_lines():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    artifact_lines = lines[2:-2]
    for line in artifact_lines:
        assert "/" not in line, (
            f"Artifact line must contain only the filename (no directory path), "
            f"but got: {line!r}"
        )


def test_report_correct_ok_corrupted_statuses():
    """Verify each jar's status matches the actual checksum comparison."""
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    artifact_lines = lines[2:-2]
    report_statuses = {}
    for line in artifact_lines:
        parts = line.rsplit(": ", 1)
        assert len(parts) == 2, (
            f"Cannot parse artifact line: {line!r}. "
            "Expected format '<filename>: OK' or '<filename>: CORRUPTED'."
        )
        jar_name, status = parts
        report_statuses[jar_name] = status

    for jar in EXPECTED_JARS:
        jar_path = os.path.join(ARTIFACTS_DIR, jar)
        sha_path = os.path.join(ARTIFACTS_DIR, jar.replace(".jar", ".sha256"))

        actual = compute_sha256(jar_path)
        stored = read_stored_sha256(sha_path)

        expected_status = "OK" if actual == stored else "CORRUPTED"

        assert jar in report_statuses, (
            f"JAR '{jar}' not found in report artifact lines."
        )
        assert report_statuses[jar] == expected_status, (
            f"Status for '{jar}' is wrong. "
            f"Expected '{expected_status}' (actual SHA256={actual!r}, stored SHA256={stored!r}), "
            f"but report says '{report_statuses[jar]}'."
        )


def test_report_app_core_is_ok():
    """app-core-1.0.jar should be OK (checksum matches)."""
    jar_path = os.path.join(ARTIFACTS_DIR, "app-core-1.0.jar")
    sha_path = os.path.join(ARTIFACTS_DIR, "app-core-1.0.sha256")
    actual = compute_sha256(jar_path)
    stored = read_stored_sha256(sha_path)

    with open(REPORT_PATH, "r") as f:
        content = f.read()

    assert "app-core-1.0.jar: OK" in content, (
        f"Expected 'app-core-1.0.jar: OK' in report "
        f"(actual SHA256={actual!r}, stored SHA256={stored!r}), "
        f"but it was not found. Report content:\n{content}"
    )


def test_report_app_ui_is_corrupted():
    """app-ui-2.1.jar should be CORRUPTED (checksum does not match)."""
    jar_path = os.path.join(ARTIFACTS_DIR, "app-ui-2.1.jar")
    sha_path = os.path.join(ARTIFACTS_DIR, "app-ui-2.1.sha256")
    actual = compute_sha256(jar_path)
    stored = read_stored_sha256(sha_path)

    with open(REPORT_PATH, "r") as f:
        content = f.read()

    assert "app-ui-2.1.jar: CORRUPTED" in content, (
        f"Expected 'app-ui-2.1.jar: CORRUPTED' in report "
        f"(actual SHA256={actual!r}, stored SHA256={stored!r}), "
        f"but it was not found. Report content:\n{content}"
    )


def test_report_app_utils_is_ok():
    """app-utils-1.4.jar should be OK (checksum matches)."""
    jar_path = os.path.join(ARTIFACTS_DIR, "app-utils-1.4.jar")
    sha_path = os.path.join(ARTIFACTS_DIR, "app-utils-1.4.sha256")
    actual = compute_sha256(jar_path)
    stored = read_stored_sha256(sha_path)

    with open(REPORT_PATH, "r") as f:
        content = f.read()

    assert "app-utils-1.4.jar: OK" in content, (
        f"Expected 'app-utils-1.4.jar: OK' in report "
        f"(actual SHA256={actual!r}, stored SHA256={stored!r}), "
        f"but it was not found. Report content:\n{content}"
    )


def test_report_summary_line_format_and_values():
    """The summary line must match 'Total: N | Passed: P | Failed: F' with correct counts."""
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    summary_line = lines[-1]

    # Compute expected values dynamically
    passed = 0
    failed = 0
    for jar in EXPECTED_JARS:
        jar_path = os.path.join(ARTIFACTS_DIR, jar)
        sha_path = os.path.join(ARTIFACTS_DIR, jar.replace(".jar", ".sha256"))
        actual = compute_sha256(jar_path)
        stored = read_stored_sha256(sha_path)
        if actual == stored:
            passed += 1
        else:
            failed += 1

    total = len(EXPECTED_JARS)
    expected_summary = f"Total: {total} | Passed: {passed} | Failed: {failed}"

    assert summary_line == expected_summary, (
        f"Summary line is wrong. "
        f"Expected: {expected_summary!r}, "
        f"but got: {summary_line!r}"
    )


def test_report_total_count_is_3():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    summary_line = lines[-1]
    assert "Total: 3" in summary_line, (
        f"Summary line should contain 'Total: 3' (3 JAR files checked), "
        f"but got: {summary_line!r}"
    )


def test_report_passed_count_is_2():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    summary_line = lines[-1]
    assert "Passed: 2" in summary_line, (
        f"Summary line should contain 'Passed: 2' (2 files with matching checksums), "
        f"but got: {summary_line!r}"
    )


def test_report_failed_count_is_1():
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    summary_line = lines[-1]
    assert "Failed: 1" in summary_line, (
        f"Summary line should contain 'Failed: 1' (1 corrupted file), "
        f"but got: {summary_line!r}"
    )


def test_report_exact_line_count():
    """Report must have exactly 7 lines: header, sep, 3 artifact lines, sep, summary."""
    with open(REPORT_PATH, "r") as f:
        lines = f.read().splitlines()

    assert len(lines) == 7, (
        f"Report must have exactly 7 lines, but has {len(lines)}. "
        f"Lines found:\n" + "\n".join(repr(l) for l in lines)
    )


def test_report_exact_full_content():
    """The entire report content must match the expected output exactly."""
    expected_lines, _, _, _ = get_expected_report_lines()
    expected_content = "\n".join(expected_lines) + "\n"

    with open(REPORT_PATH, "r") as f:
        actual_content = f.read()

    # Also accept without trailing newline
    actual_stripped = actual_content.rstrip("\n")
    expected_stripped = "\n".join(expected_lines)

    assert actual_stripped == expected_stripped, (
        f"Report content does not match expected output.\n"
        f"Expected:\n{expected_stripped}\n\n"
        f"Actual:\n{actual_stripped}"
    )


def test_sha256_files_not_in_report():
    """The .sha256 files must NOT appear in the report artifact lines."""
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    assert ".sha256" not in content, (
        f"The report must not contain any '.sha256' file entries, "
        f"but found '.sha256' in report content:\n{content}"
    )