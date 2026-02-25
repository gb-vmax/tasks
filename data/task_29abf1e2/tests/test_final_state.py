# test_final_state.py

import os
import pytest

PROFILE_LOG_PATH = "/home/user/profile.log"
HIGH_CPU_PROCESSES_PATH = "/home/user/high_cpu_processes.txt"
EXPECTED_PROFILE_LOG_CONTENT = (
    "PID: 4521, CPU: 23.1%, MEM: 125MB, CMD: myapp\n"
    "PID: 4522, CPU: 88.6%, MEM: 300MB, CMD: data-collector\n"
    "PID: 4523, CPU: 11.8%, MEM: 89MB, CMD: helper\n"
    "PID: 4524, CPU: 67.2%, MEM: 200MB, CMD: analytics\n"
    "PID: 4525, CPU: 50.0%, MEM: 230MB, CMD: renderer\n"
    "PID: 4526, CPU: 99.1%, MEM: 100MB, CMD: cruncher\n"
    "PID: 4527, CPU: 44.5%, MEM: 189MB, CMD: updater\n"
)
EXPECTED_HIGH_CPU_CONTENT = (
    "PID: 4522, CPU: 88.6%, MEM: 300MB, CMD: data-collector\n"
    "PID: 4524, CPU: 67.2%, MEM: 200MB, CMD: analytics\n"
    "PID: 4526, CPU: 99.1%, MEM: 100MB, CMD: cruncher\n"
)
EXPECTED_HIGH_CPU_LINE_COUNT = 3
EXPECTED_STDOUT = "3\n"

@pytest.mark.describe("Final state after filtering high CPU processes")
def test_high_cpu_file_exists_and_content_exact():
    """Check that /home/user/high_cpu_processes.txt exists and contains exactly the expected lines."""
    assert os.path.isfile(HIGH_CPU_PROCESSES_PATH), (
        f"Missing output file: {HIGH_CPU_PROCESSES_PATH}. "
        "You must write the filtered high-CPU processes to this exact path."
    )
    with open(HIGH_CPU_PROCESSES_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_HIGH_CPU_CONTENT, (
        f"The contents of {HIGH_CPU_PROCESSES_PATH} do not match the expected output.\n"
        "Expected:\n"
        f"{EXPECTED_HIGH_CPU_CONTENT!r}\n"
        "Found:\n"
        f"{content!r}\n"
        "Ensure only lines with CPU utilization >50% are included, "
        "with no extra whitespace or headers."
    )

def test_high_cpu_file_line_count():
    """Check that the output file contains exactly the expected number of lines."""
    with open(HIGH_CPU_PROCESSES_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) == EXPECTED_HIGH_CPU_LINE_COUNT, (
        f"{HIGH_CPU_PROCESSES_PATH} should contain exactly {EXPECTED_HIGH_CPU_LINE_COUNT} lines, "
        f"but contains {len(lines)}. Each line should correspond to a process with CPU >50%."
    )

def test_no_extra_trailing_newlines():
    """Ensure there are no extra trailing blank lines in the output file."""
    with open(HIGH_CPU_PROCESSES_PATH, "rb") as f:
        content = f.read()
    # Should end with exactly one \n and nothing after
    assert content.endswith(b"\n"), (
        f"{HIGH_CPU_PROCESSES_PATH} must end with a single newline character."
    )
    assert not content.endswith(b"\n\n"), (
        f"{HIGH_CPU_PROCESSES_PATH} must not end with multiple trailing newlines."
    )
    # Should not have any blank lines
    lines = content.decode("utf-8").splitlines()
    for i, line in enumerate(lines):
        assert line.strip() != "", (
            f"Line {i + 1} in {HIGH_CPU_PROCESSES_PATH} is blank. "
            "There must be no blank lines."
        )

def test_profile_log_is_unchanged():
    """Ensure the original input log file is unchanged after the task."""
    assert os.path.isfile(PROFILE_LOG_PATH), (
        f"The input log file {PROFILE_LOG_PATH} is missing after the task. "
        "Do not delete or modify it."
    )
    with open(PROFILE_LOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_PROFILE_LOG_CONTENT, (
        f"The contents of {PROFILE_LOG_PATH} have changed after the task.\n"
        "Expected:\n"
        f"{EXPECTED_PROFILE_LOG_CONTENT!r}\n"
        "Found:\n"
        f"{content!r}"
    )

@pytest.mark.describe("Check correct output to terminal")
def test_output_to_terminal_matches_expected(monkeypatch):
    """
    Checks that the script outputs the correct count (number of high-CPU processes) to stdout.
    This test simulates running the expected logic and verifies that the output matches.
    """
    import subprocess

    # Try to find a script that produces the output.
    # We'll look for a script in /home/user, but if not present, skip this test.
    candidate_scripts = [
        "/home/user/filter_high_cpu.py",
        "/home/user/solution.py",
        "/home/user/main.py",
        "/home/user/task.py",
        "/home/user/app.py"
    ]
    found = False
    for script in candidate_scripts:
        if os.path.isfile(script):
            found = True
            break
    if not found:
        pytest.skip("No script found to check terminal output (looked for filter_high_cpu.py, solution.py, etc.)")

    # Run the script and capture stdout.
    result = subprocess.run(
        ["python3", script],
        capture_output=True,
        encoding="utf-8"
    )
    assert result.returncode == 0, (
        f"Running {script} failed with return code {result.returncode}.\n"
        f"stderr:\n{result.stderr}"
    )
    stdout = result.stdout
    assert stdout == EXPECTED_STDOUT, (
        f"Your script should print exactly '{EXPECTED_STDOUT.strip()}' to stdout, "
        f"but printed:\n{stdout!r}\n"
        "Check that you print only the count, with no extra whitespace or lines."
    )