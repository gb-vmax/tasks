# test_final_state.py

import pytest
import os

ARTIFACT_NAMES_PATH = "/home/user/artifact_names.txt"
REPORT_PATH = "/home/user/artifacts_frequency_report.txt"

EXPECTED_REPORT_CONTENT = (
    "model_v1.pt: 4\n"
    "metrics.json: 3\n"
    "model_v2.pt: 2\n"
    "training.log: 2\n"
    "config.yaml: 1\n"
)

def test_report_file_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Expected report file '{REPORT_PATH}' was not found. "
        "Please create the file with the correct artifact frequencies."
    )

def test_report_file_content_exact():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_REPORT_CONTENT, (
        f"The contents of '{REPORT_PATH}' do not match the required final report.\n"
        "Expected (with exact order and newlines):\n"
        f"{EXPECTED_REPORT_CONTENT!r}\n"
        "But got:\n"
        f"{content!r}\n"
        "Please ensure the report format, order, and spacing are exactly as specified."
    )

def test_report_no_extra_blank_lines_or_spaces():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Check no leading/trailing blank lines
    assert lines, f"'{REPORT_PATH}' is empty. The report must contain artifact frequencies."
    assert lines[0].strip() != "", (
        f"'{REPORT_PATH}' has a blank line at the top. "
        "Remove any leading blank lines."
    )
    assert lines[-1].endswith("\n"), (
        f"The last line of '{REPORT_PATH}' does not end with a newline. "
        "Ensure each line ends with a single newline character."
    )
    # The last line should not be blank
    assert lines[-1].strip() != "", (
        f"'{REPORT_PATH}' has a blank line at the bottom. "
        "Remove any trailing blank lines."
    )
    # Check for extra spaces at line ends
    for i, line in enumerate(lines):
        assert line.rstrip("\n") == line.strip(), (
            f"Line {i+1} of '{REPORT_PATH}' has leading or trailing spaces: {repr(line)}. "
            "Each line should have no extra spaces at the start or end."
        )

def test_report_filenames_unique():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    filenames = [ln.split(":")[0] for ln in lines]
    dups = set([fn for fn in filenames if filenames.count(fn) > 1])
    assert not dups, (
        f"The report file '{REPORT_PATH}' contains duplicate filenames: {dups}. "
        "Each artifact filename should appear only once in the report."
    )

def test_report_frequencies_correct_and_sorted():
    # Truth data
    expected_freqs = [
        ("model_v1.pt", 4),
        ("metrics.json", 3),
        ("model_v2.pt", 2),
        ("training.log", 2),
        ("config.yaml", 1),
    ]
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    parsed = []
    for ln in lines:
        if ": " not in ln:
            pytest.fail(
                f"Line in '{REPORT_PATH}' is incorrectly formatted: {repr(ln)}. "
                "Each line must be '<filename>: <count>'."
            )
        filename, count_str = ln.split(": ", 1)
        try:
            count = int(count_str)
        except ValueError:
            pytest.fail(
                f"Line in '{REPORT_PATH}' has a non-integer count: {repr(ln)}. "
                "Frequencies must be integers."
            )
        parsed.append((filename, count))
    # Compare content and order
    assert parsed == expected_freqs, (
        f"Frequencies or order in '{REPORT_PATH}' are incorrect.\n"
        "Expected (in order):\n"
        f"{expected_freqs}\n"
        "But got:\n"
        f"{parsed}\n"
        "Ensure sorting by frequency descending, then alphabetically for ties."
    )

def test_report_output_printed_to_console(monkeypatch, capsys):
    """
    This test simulates the requirement that the report file's content
    be printed to the console after creation.
    Since we cannot rerun the student's code, we check that the file exists
    and that its content is exactly as expected, and demonstrate how the output
    should appear if printed to stdout.
    """
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    # Simulate print to console
    print(content, end="")  # end="" to avoid adding extra newline
    captured = capsys.readouterr()
    assert captured.out == EXPECTED_REPORT_CONTENT, (
        "The printed output to the console does not match the required report file content.\n"
        "Expected printed content:\n"
        f"{EXPECTED_REPORT_CONTENT!r}\n"
        "But got:\n"
        f"{captured.out!r}\n"
        "Ensure you print the report file's content exactly, with no extra blank lines or spaces."
    )