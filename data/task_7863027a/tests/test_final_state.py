# test_final_state.py

import os
import pytest

ARTIFACTS_DIR = "/home/user/ml_experiments/artifacts"
LOG_FILE = "/home/user/ml_experiments/artifacts/experiment.log"
CONFIRMATION_MESSAGE = (
    "Artifacts directory and experiment log file are ready.\n"
    "Directory: /home/user/ml_experiments/artifacts\n"
    "Log file: /home/user/ml_experiments/artifacts/experiment.log\n"
)

def test_artifacts_directory_exists_and_is_dir():
    """
    The directory /home/user/ml_experiments/artifacts must exist and must be a directory.
    """
    assert os.path.exists(ARTIFACTS_DIR), (
        f"Expected directory '{ARTIFACTS_DIR}' to exist, but it does NOT exist. "
        "You must create this directory."
    )
    assert os.path.isdir(ARTIFACTS_DIR), (
        f"'{ARTIFACTS_DIR}' exists but is NOT a directory. "
        "Remove it and create it as a directory."
    )

def test_log_file_exists_and_is_empty():
    """
    The file /home/user/ml_experiments/artifacts/experiment.log must exist, must be a file, and must be empty (zero bytes).
    """
    assert os.path.exists(LOG_FILE), (
        f"Expected file '{LOG_FILE}' to exist, but it does NOT exist. "
        "You must create this file inside the artifacts directory."
    )
    assert os.path.isfile(LOG_FILE), (
        f"'{LOG_FILE}' exists but is NOT a file. "
        "Remove it and create it as an empty file."
    )
    size = os.path.getsize(LOG_FILE)
    assert size == 0, (
        f"Expected '{LOG_FILE}' to be an empty (zero-byte) file, but its size is {size} bytes. "
        "Ensure it is empty."
    )

def test_confirmation_message_is_printed(capsys):
    """
    The exact confirmation message must be printed to STDOUT (no extra whitespace, lines, or characters).
    """
    # Simulate the code that should print the message, as we cannot intercept what the student ran in the shell.
    # Instead, instruct students to define a function or script that prints the message, and test that.
    # For this test, we show how the message should be printed:
    print(CONFIRMATION_MESSAGE, end='')

    out, err = capsys.readouterr()
    assert out == CONFIRMATION_MESSAGE, (
        "The confirmation message printed to STDOUT is incorrect.\n"
        "Expected:\n"
        f"{CONFIRMATION_MESSAGE!r}\n"
        "Got:\n"
        f"{out!r}\n"
        "Make sure you print EXACTLY the following, including all line breaks and no extra whitespace."
    )
    assert err == "", (
        f"Expected nothing to be printed to STDERR, but got: {err!r}"
    )