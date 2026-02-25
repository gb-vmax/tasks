# test_final_state.py

import os
import stat
import pytest

DATA_DIR = "/home/user/data"
CSV_PATH = os.path.join(DATA_DIR, "sales_data.csv")
SCRIPT_PATH = os.path.join(DATA_DIR, "summarize_sales.sh")
SUMMARY_PATH = os.path.join(DATA_DIR, "sales_summary.txt")

EXPECTED_SUM = 500
EXPECTED_OUTPUT_LINE = f"Total Sales Amount: {EXPECTED_SUM}\n"

@pytest.mark.describe("Final filesystem and script state after task completion")
class TestFinalState:
    def test_data_directory_still_exists(self):
        assert os.path.isdir(DATA_DIR), (
            f"Required directory '{DATA_DIR}' is missing. "
            "It should still exist after completing the task."
        )

    def test_sales_data_csv_untouched(self):
        """Ensure the input CSV is unchanged."""
        expected_lines = [
            "Product,Date,Amount\n",
            "Widget A,2023-06-01,120\n",
            "Widget B,2023-06-02,130\n",
            "Widget C,2023-06-03,150\n",
            "Widget A,2023-06-04,100\n",
        ]
        assert os.path.isfile(CSV_PATH), f"'{CSV_PATH}' is missing after the task."
        with open(CSV_PATH, "r", encoding="utf-8") as f:
            content = f.readlines()
        assert content == expected_lines, (
            f"'{CSV_PATH}' contents were modified. Expected:\n"
            + "".join(expected_lines)
            + "But got:\n"
            + "".join(content)
        )

    def test_summarize_sales_sh_exists_and_executable(self):
        assert os.path.isfile(SCRIPT_PATH), (
            f"Script '{SCRIPT_PATH}' does not exist. "
            "You must create this script in the required location."
        )
        st = os.stat(SCRIPT_PATH)
        is_executable = bool(st.st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
        assert is_executable, (
            f"Script '{SCRIPT_PATH}' is not executable. "
            "You must run 'chmod +x' on the script."
        )

    def test_summarize_sales_sh_content_valid(self):
        """Check script content for correct logic and absolute paths."""
        with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        assert lines, (
            f"Script '{SCRIPT_PATH}' is empty. "
            "It must contain shell code that performs the required operations."
        )
        header = lines[0].strip()
        assert header.startswith("#!"), (
            f"Script '{SCRIPT_PATH}' must start with a shebang line (e.g. '#!/bin/bash')."
        )
        script_str = "".join(lines)
        # Check for absolute paths
        assert "/home/user/data/sales_data.csv" in script_str, (
            f"Script '{SCRIPT_PATH}' must use the absolute path to 'sales_data.csv'."
        )
        assert "/home/user/data/sales_summary.txt" in script_str, (
            f"Script '{SCRIPT_PATH}' must use the absolute path to 'sales_summary.txt'."
        )
        # Check for column summing (e.g., awk, cut, etc.)
        has_awk_sum = ("awk" in script_str and ("sum" in script_str or "SUM" in script_str or "+=" in script_str))
        assert has_awk_sum, (
            f"Script '{SCRIPT_PATH}' does not appear to sum the 'Amount' column using 'awk' or similar. "
            "You must use shell logic to sum the third column of the CSV."
        )
        # Check that both output to terminal and file (tee or echo ... > or awk ... >)
        outputs_to_file = (
            ">" in script_str or
            "tee" in script_str or
            ">>" in script_str
        )
        assert outputs_to_file, (
            f"Script '{SCRIPT_PATH}' does not appear to write the output to '{SUMMARY_PATH}'."
        )
        # Check that output is also printed to the terminal (echo or print or tee)
        outputs_to_terminal = (
            "echo" in script_str or
            "tee" in script_str or
            "awk" in script_str
        )
        assert outputs_to_terminal, (
            f"Script '{SCRIPT_PATH}' does not appear to print the result to the terminal."
        )

    def test_sales_summary_txt_exists_and_content(self):
        assert os.path.isfile(SUMMARY_PATH), (
            f"Summary file '{SUMMARY_PATH}' does not exist. "
            "You must create this file with the required output."
        )
        with open(SUMMARY_PATH, "r", encoding="utf-8") as f:
            content = f.readlines()
        assert content == [EXPECTED_OUTPUT_LINE], (
            f"'{SUMMARY_PATH}' contents are incorrect.\n"
            f"Expected:\n{EXPECTED_OUTPUT_LINE}But got:\n{''.join(content)}"
        )

    def test_sales_summary_txt_is_writable(self):
        assert os.access(SUMMARY_PATH, os.W_OK), (
            f"File '{SUMMARY_PATH}' is not writable by the user."
        )

    def test_no_extra_files_in_data_directory(self):
        expected_files = {"sales_data.csv", "summarize_sales.sh", "sales_summary.txt"}
        found = set(os.listdir(DATA_DIR))
        extra = found - expected_files
        assert not extra, (
            f"Unexpected files or directories found in '{DATA_DIR}': {extra}. "
            "Only 'sales_data.csv', 'summarize_sales.sh', and 'sales_summary.txt' should exist."
        )

    def test_script_produces_correct_terminal_output(self, capfd):
        """
        Run the script and check that the output matches the expected result.
        Note: This test runs the script with the current Python user.
        """
        import subprocess

        # Run the script, capture output
        try:
            result = subprocess.run(
                [SCRIPT_PATH],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
        except Exception as e:
            pytest.fail(
                f"Error running '{SCRIPT_PATH}': {e}\n"
                f"stderr: {getattr(e, 'stderr', '')}"
            )
        # The output should be exactly the expected line (with or without trailing newline)
        out = result.stdout
        out_lines = out.splitlines()
        assert out_lines, (
            f"The script '{SCRIPT_PATH}' did not print any output to the terminal."
        )
        assert out_lines[0] == EXPECTED_OUTPUT_LINE.strip(), (
            f"Terminal output is incorrect.\n"
            f"Expected:\n{EXPECTED_OUTPUT_LINE.strip()}\n"
            f"But got:\n{out_lines[0]}"
        )
        # Optionally, check that there is no extra output
        if len(out_lines) > 1:
            assert all(line.strip() == "" for line in out_lines[1:]), (
                f"Script '{SCRIPT_PATH}' printed extra lines to the terminal:\n"
                + "\n".join(out_lines[1:])
            )
        # Also check that no error was printed
        assert result.stderr.strip() == "", (
            f"Script '{SCRIPT_PATH}' printed error output:\n{result.stderr}"
        )