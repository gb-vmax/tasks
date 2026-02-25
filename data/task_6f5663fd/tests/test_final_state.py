# test_final_state.py

import os
import stat
import pytest

HOME = "/home/user"
DATA_DIR = os.path.join(HOME, "data")
SCRIPTS_DIR = os.path.join(HOME, "scripts")
RAW_TEXT = os.path.join(DATA_DIR, "raw_text.txt")
PREPARED_TEXT = os.path.join(DATA_DIR, "prepared_text.txt")
PREPARE_SCRIPT = os.path.join(SCRIPTS_DIR, "prepare_data.sh")

EXPECTED_RAW_TEXT = (
    "The Quick brown Fox  \n"
    "  jumps Over the Lazy Dog  \n"
    "\n"
    "\n"
    "HELLO WORLD  \n"
    "  data science is Awesome     \n"
    "\n"
)

# Note: There are 7 lines in the input (6 newlines, so 7 lines), so output should also have 7 lines
EXPECTED_PREPARED_TEXT = (
    "the quick brown fox\n"
    "jumps over the lazy dog\n"
    "\n"
    "\n"
    "hello world\n"
    "data science is awesome\n"
    "\n"
)

def test_data_directory_exists():
    assert os.path.isdir(DATA_DIR), (
        f"Required data directory '{DATA_DIR}' does not exist. Please create it."
    )

def test_scripts_directory_exists():
    assert os.path.isdir(SCRIPTS_DIR), (
        f"Required scripts directory '{SCRIPTS_DIR}' does not exist. Please create it."
    )

def test_raw_text_file_exists_and_unchanged():
    assert os.path.isfile(RAW_TEXT), (
        f"Raw text file '{RAW_TEXT}' does not exist. It must remain present after processing."
    )
    try:
        with open(RAW_TEXT, "r", encoding="utf-8") as f:
            actual = f.read()
    except Exception as e:
        pytest.fail(f"Could not read '{RAW_TEXT}': {e}")

    assert actual == EXPECTED_RAW_TEXT, (
        f"'{RAW_TEXT}' contents have changed after running the script.\n"
        "Expected:\n"
        "---\n"
        f"{EXPECTED_RAW_TEXT}---\n"
        "Actual:\n"
        "---\n"
        f"{actual}---\n"
        "The raw text file must NOT be modified by the script."
    )

def test_prepare_data_script_exists_and_executable():
    assert os.path.isfile(PREPARE_SCRIPT), (
        f"Required script '{PREPARE_SCRIPT}' does not exist."
    )
    st = os.stat(PREPARE_SCRIPT)
    is_executable = bool(st.st_mode & stat.S_IXUSR)
    assert is_executable, (
        f"Script '{PREPARE_SCRIPT}' exists but is not executable by the user. "
        "Please ensure it has execute permissions (e.g., chmod u+x)."
    )

def test_prepared_text_file_exists_and_correct():
    assert os.path.isfile(PREPARED_TEXT), (
        f"Output file '{PREPARED_TEXT}' does not exist. The script did not create it."
    )
    try:
        with open(PREPARED_TEXT, "r", encoding="utf-8") as f:
            actual = f.read()
    except Exception as e:
        pytest.fail(f"Could not read '{PREPARED_TEXT}': {e}")

    assert actual == EXPECTED_PREPARED_TEXT, (
        f"'{PREPARED_TEXT}' has incorrect contents after running the script.\n"
        "Expected:\n"
        "---\n"
        f"{EXPECTED_PREPARED_TEXT}---\n"
        "Actual:\n"
        "---\n"
        f"{actual}---\n"
        "Please ensure the output matches the required transformation exactly, including blanks and trailing newlines."
    )

def test_data_directory_listing_final_state():
    expected = {"raw_text.txt", "prepared_text.txt"}
    actual = set(os.listdir(DATA_DIR))
    missing = expected - actual
    extra = actual - expected
    assert expected <= actual, (
        f"Data directory '{DATA_DIR}' is missing required files: {missing}. "
        f"Found: {actual}"
    )
    assert not extra, (
        f"Data directory '{DATA_DIR}' contains unexpected files: {extra}. "
        f"Expected only: {expected}"
    )

def test_scripts_directory_listing_final_state():
    expected = {"prepare_data.sh"}
    actual = set(os.listdir(SCRIPTS_DIR))
    missing = expected - actual
    extra = actual - expected
    assert expected <= actual, (
        f"Scripts directory '{SCRIPTS_DIR}' is missing required script(s): {missing}. "
        f"Found: {actual}"
    )
    assert not extra, (
        f"Scripts directory '{SCRIPTS_DIR}' contains unexpected files: {extra}. "
        f"Expected only: {expected}"
    )

def test_prepared_text_lines_match_input_count():
    """Ensure the output file has the same number of lines (including blanks) as the input."""
    with open(RAW_TEXT, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()
    with open(PREPARED_TEXT, "r", encoding="utf-8") as f:
        prepared_lines = f.readlines()
    assert len(prepared_lines) == len(raw_lines), (
        f"Output file '{PREPARED_TEXT}' has {len(prepared_lines)} lines, "
        f"but input '{RAW_TEXT}' has {len(raw_lines)} lines. "
        "The output must preserve the exact number of lines, including blanks."
    )

def test_prepared_text_transformation_per_line():
    """Check each line is lowercased, trimmed, blank lines preserved."""
    with open(RAW_TEXT, "r", encoding="utf-8") as fin:
        raw_lines = fin.readlines()
    with open(PREPARED_TEXT, "r", encoding="utf-8") as fout:
        prepared_lines = fout.readlines()

    assert len(raw_lines) == len(prepared_lines), (
        f"Line count mismatch: input has {len(raw_lines)} lines, but output has {len(prepared_lines)} lines."
    )

    for i, (raw, prepared) in enumerate(zip(raw_lines, prepared_lines)):
        # Remove trailing newline for comparison, but remember it must be present in the file
        raw_no_nl = raw.rstrip('\n')
        prepared_no_nl = prepared.rstrip('\n')
        if raw_no_nl.strip() == "":
            # Blank or whitespace-only line in input: output should be blank line
            assert prepared_no_nl == "", (
                f"Line {i+1} in '{PREPARED_TEXT}' should be blank because line {i+1} in '{RAW_TEXT}' is blank or whitespace.\n"
                f"Input line: {repr(raw_no_nl)}\nOutput line: {repr(prepared_no_nl)}"
            )
        else:
            expected_line = raw_no_nl.strip().lower()
            assert prepared_no_nl == expected_line, (
                f"Line {i+1} in '{PREPARED_TEXT}' incorrect.\n"
                f"Expected: {repr(expected_line)}\nActual:   {repr(prepared_no_nl)}\n"
                f"Input line: {repr(raw_no_nl)}"
            )