# test_final_state.py

import os
import pytest

HOME = "/home/user"
REPO_PATH = os.path.join(HOME, "target-repo")
OUTPUT_PATH = os.path.join(REPO_PATH, "submodules_list.txt")

EXPECTED_OUTPUT_LINES = [
    "path: libs/vuln-lib, url: https://github.com/example/vuln-lib.git",
    "path: utils/useful-util, url: https://github.com/example/useful-util.git",
]

def test_output_file_exists():
    assert os.path.isfile(OUTPUT_PATH), (
        f"Expected output file {OUTPUT_PATH} does not exist.\n"
        "You must create this file as part of the task."
    )

def test_output_file_not_empty():
    size = os.path.getsize(OUTPUT_PATH)
    assert size > 0, (
        f"The output file {OUTPUT_PATH} exists but is empty.\n"
        "It should contain the list of submodules in the specified format."
    )

def test_output_file_contents_exact():
    try:
        with open(OUTPUT_PATH, "r") as f:
            lines = [line.rstrip("\n") for line in f]
    except Exception as e:
        pytest.fail(f"Could not read {OUTPUT_PATH}: {e}")

    # Check for "No submodules found." case first
    if lines == ["No submodules found."]:
        pytest.fail(
            f"The output file {OUTPUT_PATH} contains 'No submodules found.', "
            "but the repository is configured with submodules in .gitmodules.\n"
            "Expected list of submodules."
        )

    # Check that the output matches the expected lines exactly
    assert lines == EXPECTED_OUTPUT_LINES, (
        f"The contents of {OUTPUT_PATH} do not match the expected output.\n"
        "Expected:\n"
        + "\n".join(EXPECTED_OUTPUT_LINES)
        + "\nActual:\n"
        + "\n".join(lines)
        + "\n"
        "Ensure each line matches exactly, with correct path, url, and no extra whitespace."
    )

def test_output_file_no_extra_lines():
    """Ensure there are exactly as many lines as expected (no extras or blank lines)."""
    with open(OUTPUT_PATH, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    assert len(lines) == len(EXPECTED_OUTPUT_LINES), (
        f"The output file {OUTPUT_PATH} should have exactly {len(EXPECTED_OUTPUT_LINES)} lines, "
        f"but it has {len(lines)}.\n"
        "Check for extra blank lines or unexpected output."
    )