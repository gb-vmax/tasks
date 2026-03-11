# test_final_state.py

import os
import pytest

AUTH_LOG_PATH = "/home/user/security/auth.log"
KEY_FREQUENCY_PATH = "/home/user/security/key_frequency.txt"
SECURITY_DIR = "/home/user/security"

EXPECTED_FREQUENCY_CONTENTS = "7 key_gamma\n6 key_alpha\n4 key_beta\n3 key_delta\n"

EXPECTED_LINES = [
    "7 key_gamma",
    "6 key_alpha",
    "4 key_beta",
    "3 key_delta",
]


def test_security_directory_exists():
    assert os.path.isdir(SECURITY_DIR), (
        f"Directory '{SECURITY_DIR}' does not exist. "
        "The /home/user/security/ directory must exist."
    )


def test_auth_log_still_exists():
    assert os.path.isfile(AUTH_LOG_PATH), (
        f"File '{AUTH_LOG_PATH}' does not exist. "
        "The original auth.log file must still be present after the task."
    )


def test_key_frequency_file_exists():
    assert os.path.isfile(KEY_FREQUENCY_PATH), (
        f"File '{KEY_FREQUENCY_PATH}' does not exist. "
        "The student must create this file as part of the task."
    )


def test_key_frequency_file_is_readable():
    assert os.access(KEY_FREQUENCY_PATH, os.R_OK), (
        f"File '{KEY_FREQUENCY_PATH}' is not readable."
    )


def test_key_frequency_file_exact_contents():
    with open(KEY_FREQUENCY_PATH, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_FREQUENCY_CONTENTS, (
        f"Contents of '{KEY_FREQUENCY_PATH}' do not match expected.\n"
        f"Expected (repr): {repr(EXPECTED_FREQUENCY_CONTENTS)}\n"
        f"Actual   (repr): {repr(actual)}"
    )


def test_key_frequency_line_count():
    with open(KEY_FREQUENCY_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    non_blank = [l for l in lines if l.strip()]
    assert len(non_blank) == 4, (
        f"Expected exactly 4 non-blank lines in '{KEY_FREQUENCY_PATH}', "
        f"got {len(non_blank)}.\nLines: {non_blank}"
    )


def test_key_frequency_no_blank_lines():
    with open(KEY_FREQUENCY_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    blank_lines = [i + 1 for i, l in enumerate(lines) if not l.strip()]
    assert len(blank_lines) == 0, (
        f"Found blank lines in '{KEY_FREQUENCY_PATH}' at line numbers: {blank_lines}. "
        "There must be no blank lines in the output file."
    )


def test_key_frequency_no_leading_spaces():
    with open(KEY_FREQUENCY_PATH, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for i, line in enumerate(lines, start=1):
        if line.strip():
            assert not line.startswith(" "), (
                f"Line {i} in '{KEY_FREQUENCY_PATH}' has leading spaces: {repr(line)}. "
                "No leading spaces are allowed."
            )


def test_key_frequency_line_format():
    with open(KEY_FREQUENCY_PATH, "r") as f:
        content = f.read()
    lines = [l for l in content.splitlines() if l.strip()]
    for i, line in enumerate(lines, start=1):
        parts = line.split()
        assert len(parts) == 2, (
            f"Line {i} in '{KEY_FREQUENCY_PATH}' does not have exactly 2 fields: {repr(line)}. "
            "Each line must be in the format '<count> <key_name>'."
        )
        count_str, key_name = parts
        assert count_str.isdigit(), (
            f"Line {i} in '{KEY_FREQUENCY_PATH}' has a non-integer count field: {repr(count_str)}. "
            "The first field must be an integer count."
        )
        assert key_name.startswith("key_"), (
            f"Line {i} in '{KEY_FREQUENCY_PATH}' has unexpected key format: {repr(key_name)}. "
            "Expected key to start with 'key_'."
        )


def test_key_frequency_correct_counts():
    with open(KEY_FREQUENCY_PATH, "r") as f:
        content = f.read()
    lines = [l for l in content.splitlines() if l.strip()]
    actual_counts = {}
    for line in lines:
        parts = line.split()
        count, key = int(parts[0]), parts[1]
        actual_counts[key] = count

    expected_counts = {
        "key_gamma": 7,
        "key_alpha": 6,
        "key_beta": 4,
        "key_delta": 3,
    }
    assert actual_counts == expected_counts, (
        f"Key counts in '{KEY_FREQUENCY_PATH}' do not match expected.\n"
        f"Expected: {expected_counts}\n"
        f"Actual:   {actual_counts}"
    )


def test_key_frequency_correct_order():
    with open(KEY_FREQUENCY_PATH, "r") as f:
        content = f.read()
    lines = [l for l in content.splitlines() if l.strip()]
    actual_lines = [l.strip() for l in lines]
    assert actual_lines == EXPECTED_LINES, (
        f"Lines in '{KEY_FREQUENCY_PATH}' are not in the correct order.\n"
        f"Expected order:\n" + "\n".join(EXPECTED_LINES) + "\n"
        f"Actual order:\n" + "\n".join(actual_lines)
    )


def test_key_frequency_descending_count_order():
    with open(KEY_FREQUENCY_PATH, "r") as f:
        content = f.read()
    lines = [l for l in content.splitlines() if l.strip()]
    counts = [int(l.split()[0]) for l in lines]
    for i in range(len(counts) - 1):
        assert counts[i] >= counts[i + 1], (
            f"Lines in '{KEY_FREQUENCY_PATH}' are not sorted by descending count. "
            f"Count at line {i + 1} ({counts[i]}) is less than count at line {i + 2} ({counts[i + 1]})."
        )


def test_key_frequency_tie_breaking_reverse_alphabetical():
    """
    For keys with the same count, they must appear in reverse alphabetical order.
    In this dataset there are no ties, but we verify the general ordering rule
    is consistent with what we expect.
    """
    with open(KEY_FREQUENCY_PATH, "r") as f:
        content = f.read()
    lines = [l for l in content.splitlines() if l.strip()]
    parsed = [(int(l.split()[0]), l.split()[1]) for l in lines]

    # Group by count and check reverse alphabetical within each group
    from itertools import groupby
    for count, group in groupby(parsed, key=lambda x: x[0]):
        keys_in_group = [item[1] for item in group]
        expected_order = sorted(keys_in_group, reverse=True)
        assert keys_in_group == expected_order, (
            f"Keys with count {count} in '{KEY_FREQUENCY_PATH}' are not in reverse alphabetical order.\n"
            f"Expected: {expected_order}\n"
            f"Actual:   {keys_in_group}"
        )


def test_key_frequency_all_keys_present():
    with open(KEY_FREQUENCY_PATH, "r") as f:
        content = f.read()
    lines = [l for l in content.splitlines() if l.strip()]
    keys_in_file = {l.split()[1] for l in lines}
    expected_keys = {"key_alpha", "key_gamma", "key_beta", "key_delta"}
    missing = expected_keys - keys_in_file
    extra = keys_in_file - expected_keys
    assert not missing, (
        f"The following keys are missing from '{KEY_FREQUENCY_PATH}': {missing}"
    )
    assert not extra, (
        f"The following unexpected keys are present in '{KEY_FREQUENCY_PATH}': {extra}"
    )


def test_key_frequency_newline_terminated():
    with open(KEY_FREQUENCY_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"File '{KEY_FREQUENCY_PATH}' is not newline-terminated. "
        f"Last bytes: {repr(content[-5:])}"
    )


def test_auth_log_unchanged():
    """Verify the original auth.log was not modified during the task."""
    EXPECTED_LOG_CONTENTS = (
        "2024-05-01T08:00:01Z SUCCESS key_alpha\n"
        "2024-05-01T08:00:05Z FAILED key_beta\n"
        "2024-05-01T08:00:09Z SUCCESS key_gamma\n"
        "2024-05-01T08:01:00Z SUCCESS key_alpha\n"
        "2024-05-01T08:01:15Z FAILED key_delta\n"
        "2024-05-01T08:01:22Z SUCCESS key_gamma\n"
        "2024-05-01T08:02:00Z FAILED key_alpha\n"
        "2024-05-01T08:02:10Z SUCCESS key_beta\n"
        "2024-05-01T08:02:45Z SUCCESS key_gamma\n"
        "2024-05-01T08:03:00Z SUCCESS key_delta\n"
        "2024-05-01T08:03:12Z FAILED key_gamma\n"
        "2024-05-01T08:03:30Z SUCCESS key_alpha\n"
        "2024-05-01T08:04:00Z SUCCESS key_gamma\n"
        "2024-05-01T08:04:22Z FAILED key_beta\n"
        "2024-05-01T08:05:00Z SUCCESS key_delta\n"
        "2024-05-01T08:05:10Z SUCCESS key_gamma\n"
        "2024-05-01T08:05:45Z SUCCESS key_alpha\n"
        "2024-05-01T08:06:00Z FAILED key_gamma\n"
        "2024-05-01T08:06:15Z SUCCESS key_beta\n"
        "2024-05-01T08:06:45Z SUCCESS key_alpha"
    )
    with open(AUTH_LOG_PATH, "r") as f:
        actual = f.read().rstrip("\n")
    expected = EXPECTED_LOG_CONTENTS.rstrip("\n")
    assert actual == expected, (
        f"Contents of '{AUTH_LOG_PATH}' were modified during the task.\n"
        f"Expected:\n{expected}\n\n"
        f"Actual:\n{actual}"
    )