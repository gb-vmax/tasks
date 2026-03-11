# test_final_state.py

import os
import pytest

ARTIFACTS_DIR = "/home/user/artifacts"
BUILD_LOG_PATH = "/home/user/artifacts/build_log.txt"
ARTIFACT_FREQ_PATH = "/home/user/artifacts/artifact_freq.txt"
SUMMARY_PATH = "/home/user/artifacts/summary.txt"

EXPECTED_FREQ_LINES = [
    "9 libcore.so",
    "6 app-release.apk",
    "6 libutils.so",
    "5 libnetwork.so",
    "4 app-debug.apk",
]

EXPECTED_SUMMARY = (
    "Total builds: 30 | Unique artifacts: 5 | Most built: libcore.so (9 times)"
)


# --- artifact_freq.txt tests ---

def test_artifact_freq_file_exists():
    assert os.path.isfile(ARTIFACT_FREQ_PATH), (
        f"File '{ARTIFACT_FREQ_PATH}' does not exist. "
        "The frequency report file must be created by the task."
    )


def test_artifact_freq_file_is_readable():
    assert os.access(ARTIFACT_FREQ_PATH, os.R_OK), (
        f"File '{ARTIFACT_FREQ_PATH}' is not readable."
    )


def test_artifact_freq_line_count():
    with open(ARTIFACT_FREQ_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 5, (
        f"Expected exactly 5 lines in '{ARTIFACT_FREQ_PATH}', but found {len(lines)}.\n"
        f"Actual content:\n{content}"
    )


def test_artifact_freq_no_blank_lines():
    with open(ARTIFACT_FREQ_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"Found blank lines at line numbers {blank_lines} in '{ARTIFACT_FREQ_PATH}'. "
        "No blank lines are allowed."
    )


def test_artifact_freq_no_leading_spaces():
    with open(ARTIFACT_FREQ_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for i, line in enumerate(lines, 1):
        assert not line.startswith(" "), (
            f"Line {i} in '{ARTIFACT_FREQ_PATH}' has a leading space: {repr(line)}. "
            "Each line must start directly with the numeric count."
        )


def test_artifact_freq_no_trailing_whitespace():
    with open(ARTIFACT_FREQ_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for i, line in enumerate(lines, 1):
        assert line == line.rstrip(), (
            f"Line {i} in '{ARTIFACT_FREQ_PATH}' has trailing whitespace: {repr(line)}."
        )


def test_artifact_freq_exact_content():
    with open(ARTIFACT_FREQ_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert lines == EXPECTED_FREQ_LINES, (
        f"Content of '{ARTIFACT_FREQ_PATH}' does not match expected content.\n"
        f"Expected lines:\n" + "\n".join(EXPECTED_FREQ_LINES) + "\n\n"
        f"Actual lines:\n" + "\n".join(lines)
    )


def test_artifact_freq_first_line_highest_count():
    with open(ARTIFACT_FREQ_PATH, "r") as f:
        lines = f.read().splitlines()
    assert len(lines) >= 1, (
        f"'{ARTIFACT_FREQ_PATH}' is empty."
    )
    first_line = lines[0]
    assert first_line == "9 libcore.so", (
        f"First line of '{ARTIFACT_FREQ_PATH}' should be '9 libcore.so' "
        f"(highest count artifact), but got: {repr(first_line)}"
    )


def test_artifact_freq_tiebreaker_ordering():
    """app-release.apk and libutils.so both have count 6; alphabetically app-release.apk < libutils.so."""
    with open(ARTIFACT_FREQ_PATH, "r") as f:
        lines = f.read().splitlines()
    # Find lines with count 6
    count_6_lines = [line for line in lines if line.startswith("6 ")]
    assert len(count_6_lines) == 2, (
        f"Expected 2 lines with count 6 in '{ARTIFACT_FREQ_PATH}', "
        f"but found {len(count_6_lines)}: {count_6_lines}"
    )
    assert count_6_lines[0] == "6 app-release.apk", (
        f"For count=6 tiebreaker, 'app-release.apk' should come before 'libutils.so' "
        f"(alphabetical order). Got: {count_6_lines}"
    )
    assert count_6_lines[1] == "6 libutils.so", (
        f"For count=6 tiebreaker, 'libutils.so' should be second. Got: {count_6_lines}"
    )


def test_artifact_freq_descending_order():
    with open(ARTIFACT_FREQ_PATH, "r") as f:
        lines = f.read().splitlines()
    counts = []
    for i, line in enumerate(lines, 1):
        parts = line.split(" ", 1)
        assert len(parts) == 2 and parts[0].isdigit(), (
            f"Line {i} in '{ARTIFACT_FREQ_PATH}' is not in '<count> <artifact>' format: {repr(line)}"
        )
        counts.append(int(parts[0]))
    for i in range(len(counts) - 1):
        assert counts[i] >= counts[i + 1], (
            f"Lines in '{ARTIFACT_FREQ_PATH}' are not sorted in descending order by count. "
            f"Line {i+1} has count {counts[i]}, but line {i+2} has count {counts[i+1]}."
        )


def test_artifact_freq_format_each_line():
    """Each line must be exactly '<integer> <artifact_name>' with no extra spaces."""
    with open(ARTIFACT_FREQ_PATH, "r") as f:
        lines = f.read().splitlines()
    for i, line in enumerate(lines, 1):
        parts = line.split(" ", 1)
        assert len(parts) == 2, (
            f"Line {i} in '{ARTIFACT_FREQ_PATH}' does not have the format '<count> <artifact>': {repr(line)}"
        )
        count_str, artifact = parts
        assert count_str.isdigit(), (
            f"Line {i} in '{ARTIFACT_FREQ_PATH}': count '{count_str}' is not a valid integer."
        )
        assert artifact == artifact.strip(), (
            f"Line {i} in '{ARTIFACT_FREQ_PATH}': artifact name has extra whitespace: {repr(artifact)}"
        )
        assert artifact != "", (
            f"Line {i} in '{ARTIFACT_FREQ_PATH}': artifact name is empty."
        )


# --- summary.txt tests ---

def test_summary_file_exists():
    assert os.path.isfile(SUMMARY_PATH), (
        f"File '{SUMMARY_PATH}' does not exist. "
        "The summary file must be created by the task."
    )


def test_summary_file_is_readable():
    assert os.access(SUMMARY_PATH, os.R_OK), (
        f"File '{SUMMARY_PATH}' is not readable."
    )


def test_summary_exact_content():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()
    # Strip a single trailing newline if present (common for text files)
    lines = content.splitlines()
    assert len(lines) == 1, (
        f"Expected exactly 1 line in '{SUMMARY_PATH}', but found {len(lines)}.\n"
        f"Actual content: {repr(content)}"
    )
    actual_line = lines[0]
    assert actual_line == EXPECTED_SUMMARY, (
        f"Content of '{SUMMARY_PATH}' does not match expected.\n"
        f"Expected: {repr(EXPECTED_SUMMARY)}\n"
        f"Got:      {repr(actual_line)}"
    )


def test_summary_total_builds():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read().strip()
    assert "Total builds: 30" in content, (
        f"'{SUMMARY_PATH}' should contain 'Total builds: 30', but got: {repr(content)}"
    )


def test_summary_unique_artifacts():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read().strip()
    assert "Unique artifacts: 5" in content, (
        f"'{SUMMARY_PATH}' should contain 'Unique artifacts: 5', but got: {repr(content)}"
    )


def test_summary_most_built():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read().strip()
    assert "Most built: libcore.so (9 times)" in content, (
        f"'{SUMMARY_PATH}' should contain 'Most built: libcore.so (9 times)', but got: {repr(content)}"
    )


def test_summary_no_trailing_whitespace():
    with open(SUMMARY_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for i, line in enumerate(lines, 1):
        assert line == line.rstrip(), (
            f"Line {i} in '{SUMMARY_PATH}' has trailing whitespace: {repr(line)}."
        )


# --- build_log.txt integrity (ensure it was not modified) ---

def test_build_log_still_intact():
    """Ensure the original build_log.txt was not modified by the task."""
    expected_lines = [
        "libcore.so", "libutils.so", "app-release.apk", "libcore.so",
        "libnetwork.so", "app-release.apk", "libcore.so", "libutils.so",
        "libnetwork.so", "libcore.so", "app-debug.apk", "libutils.so",
        "libcore.so", "app-release.apk", "libnetwork.so", "libcore.so",
        "app-debug.apk", "libutils.so", "libcore.so", "app-release.apk",
        "libutils.so", "libcore.so", "libnetwork.so", "app-debug.apk",
        "libcore.so", "app-release.apk", "libutils.so", "libnetwork.so",
        "app-debug.apk", "app-release.apk",
    ]
    assert os.path.isfile(BUILD_LOG_PATH), (
        f"'{BUILD_LOG_PATH}' is missing — it should not have been deleted."
    )
    with open(BUILD_LOG_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    if lines and lines[-1] == "":
        lines = lines[:-1]
    assert lines == expected_lines, (
        f"'{BUILD_LOG_PATH}' was modified. "
        f"Expected 30 original lines but content has changed.\n"
        f"Got: {lines}"
    )