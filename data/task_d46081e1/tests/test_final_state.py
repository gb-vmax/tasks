# test_final_state.py

import os
import pytest

INPUT_CSV_PATH = "/home/user/app_translations.csv"
OUTPUT_CSV_PATH = "/home/user/app_translations_es.csv"

EXPECTED_INPUT_CSV_CONTENT = (
    "welcome,Welcome,Bienvenido\n"
    "goodbye,Goodbye,Adiós\n"
    "thanks,Thank you,Gracias\n"
)

EXPECTED_OUTPUT_CSV_CONTENT = (
    "welcome,Bienvenido\n"
    "goodbye,Adiós\n"
    "thanks,Gracias\n"
)

def test_input_csv_still_exists_and_unchanged():
    """
    Ensure the original input CSV still exists and has not been modified.
    """
    assert os.path.isfile(INPUT_CSV_PATH), (
        f"Expected file '{INPUT_CSV_PATH}' does not exist after task completion."
    )
    with open(INPUT_CSV_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_INPUT_CSV_CONTENT, (
        f"File '{INPUT_CSV_PATH}' was modified. It must remain unchanged after the task.\n"
        "Expected:\n"
        f"{EXPECTED_INPUT_CSV_CONTENT!r}\n"
        "Found:\n"
        f"{content!r}"
    )

def test_output_csv_exists_with_correct_content():
    """
    Validate that the output CSV exists and contains exactly the expected Spanish translations.
    """
    assert os.path.isfile(OUTPUT_CSV_PATH), (
        f"Output file '{OUTPUT_CSV_PATH}' does not exist. "
        "You must create this file with the required translations."
    )
    with open(OUTPUT_CSV_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_OUTPUT_CSV_CONTENT, (
        f"File '{OUTPUT_CSV_PATH}' does not have the correct contents.\n"
        "Expected exactly:\n"
        f"{EXPECTED_OUTPUT_CSV_CONTENT!r}\n"
        "But found:\n"
        f"{content!r}\n"
        "Check for extra/missing lines, headers, wrong order, or extra spaces."
    )

def test_output_csv_has_no_extra_lines():
    """
    Ensure there are exactly three lines in the output, no more, no less.
    """
    with open(OUTPUT_CSV_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    expected_lines = [
        "welcome,Bienvenido\n",
        "goodbye,Adiós\n",
        "thanks,Gracias\n",
    ]
    assert lines == expected_lines, (
        f"Output file '{OUTPUT_CSV_PATH}' does not have the exact expected lines.\n"
        f"Expected lines:\n{expected_lines!r}\n"
        f"Found lines:\n{lines!r}\n"
        "Check for extra lines, missing lines, or incorrect line endings."
    )

def test_output_csv_has_no_header_or_extra_spaces():
    """
    Ensure no header row and no extra spaces are present in output CSV.
    """
    with open(OUTPUT_CSV_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        assert not line.startswith("key") and not line.startswith("en") and not line.startswith("es"), (
            f"Line {i+1} in '{OUTPUT_CSV_PATH}' looks like a header: '{line.strip()}'. "
            "There should be NO header row."
        )
        # Check for extra spaces before/after comma or at line ends
        parts = line.rstrip('\n').split(',')
        assert len(parts) == 2, (
            f"Line {i+1} in '{OUTPUT_CSV_PATH}' does not have exactly one comma: '{line.strip()}'."
        )
        assert parts[0] == parts[0].strip(), (
            f"Extra spaces detected before/after key in line {i+1}: '{line.strip()}'."
        )
        assert parts[1] == parts[1].strip(), (
            f"Extra spaces detected before/after Spanish translation in line {i+1}: '{line.strip()}'."
        )

def test_console_output_matches_expected(monkeypatch, capsys):
    """
    Simulate the verification step: the agent must display the exact three lines of the output file.
    This test assumes that the agent prints these lines to the console after creating the file.
    """
    # Simulate what the agent should print
    expected_console_output = (
        "welcome,Bienvenido\n"
        "goodbye,Adiós\n"
        "thanks,Gracias\n"
    )
    # For the test, we simulate the agent printing the file contents
    with open(OUTPUT_CSV_PATH, "r", encoding="utf-8") as f:
        file_output = f.read()
    assert file_output == expected_console_output, (
        "When displaying '/home/user/app_translations_es.csv' in the terminal, "
        "the output must be exactly:\n"
        f"{expected_console_output!r}\n"
        "But found:\n"
        f"{file_output!r}\n"
        "Check for extra/missing lines, wrong order, or extra spaces."
    )