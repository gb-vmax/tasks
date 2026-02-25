# test_final_state.py
#
# Pytest suite to validate the final state after the solver benchmarking pipeline is complete.
# This checks the /home/user/outputs/ directory for correct files, content, and naming,
# and ensures strict compliance with the requested output and format.

import os
import pytest

HOME = "/home/user"
SOLVERS = ["solverX", "solverY"]
PROBLEMS = ["problemA", "problemB"]
OUTPUTS_DIR = os.path.join(HOME, "outputs")

EXPECTED_OUTPUT_FILES = [
    f"{solver}_{problem}.out"
    for problem in PROBLEMS
    for solver in SOLVERS
]
EXPECTED_BENCHMARK_LOG = "benchmark.log"
ALL_EXPECTED_FILES = set(EXPECTED_OUTPUT_FILES + [EXPECTED_BENCHMARK_LOG])

# Truth: expected content for each .out file
EXPECTED_FILE_CONTENTS = {
    "solverX_problemA.out": "solution of solverX on problemA",
    "solverY_problemA.out": "solution of solverY on problemA",
    "solverX_problemB.out": "solution of solverX on problemB",
    "solverY_problemB.out": "solution of solverY on problemB",
}
# Truth: expected content of benchmark.log
EXPECTED_BENCHMARK_LOG_CONTENT = """BENCHMARK RESULTS

Input File: problemA.dat
solverX output: solverX_problemA.out
solverY output: solverY_problemA.out

Input File: problemB.dat
solverX output: solverX_problemB.out
solverY output: solverY_problemB.out
"""

@pytest.mark.describe("Final state: All outputs produced, named, and formatted correctly")
class TestFinalState:

    def test_outputs_dir_exists(self):
        assert os.path.isdir(OUTPUTS_DIR), (
            f"Directory '{OUTPUTS_DIR}' does not exist. "
            "You must create it to store all output files."
        )

    def test_outputs_dir_contains_only_expected_files(self):
        files = sorted(os.listdir(OUTPUTS_DIR))
        expected_files = sorted(ALL_EXPECTED_FILES)
        assert files == expected_files, (
            f"Directory '{OUTPUTS_DIR}' contains unexpected files.\n"
            f"Expected only: {expected_files}\n"
            f"Found: {files}\n"
            "Remove any old or extra files from the outputs directory."
        )

    @pytest.mark.parametrize("filename,expected_content", EXPECTED_FILE_CONTENTS.items())
    def test_output_file_content(self, filename, expected_content):
        path = os.path.join(OUTPUTS_DIR, filename)
        assert os.path.isfile(path), (
            f"Expected output file '{path}' does not exist."
        )
        with open(path, "r") as f:
            content = f.read().strip()
        assert content == expected_content, (
            f"File '{path}' has incorrect content.\n"
            f"Expected: {expected_content!r}\n"
            f"Got: {content!r}"
        )

    def test_benchmark_log_exists(self):
        path = os.path.join(OUTPUTS_DIR, EXPECTED_BENCHMARK_LOG)
        assert os.path.isfile(path), (
            f"Benchmark log file '{path}' is missing."
        )

    def test_benchmark_log_content_exact(self):
        path = os.path.join(OUTPUTS_DIR, EXPECTED_BENCHMARK_LOG)
        with open(path, "r") as f:
            content = f.read()
        # Check for exact content including blank lines and order
        if content != EXPECTED_BENCHMARK_LOG_CONTENT:
            # Show a diff-style message
            import difflib
            diff = "\n".join(
                difflib.unified_diff(
                    EXPECTED_BENCHMARK_LOG_CONTENT.splitlines(),
                    content.splitlines(),
                    fromfile="expected",
                    tofile="found",
                    lineterm=""
                )
            )
            pytest.fail(
                f"benchmark.log content does not match the required format. "
                f"See diff below:\n{diff}"
            )

    def test_no_extra_files_in_outputs(self):
        """
        Double-check: No hidden or stray files (e.g. .DS_Store, backup files, temp files)
        """
        files = set(os.listdir(OUTPUTS_DIR))
        extras = files - ALL_EXPECTED_FILES
        assert not extras, (
            f"Found extra files in '{OUTPUTS_DIR}': {sorted(extras)}. "
            "Only the specified output and log files should be present."
        )