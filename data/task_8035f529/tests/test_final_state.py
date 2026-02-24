# test_final_state.py
import os
import pytest
import csv

HOME = "/home/user"
OPTIMIZED_COSTS_REPORT_CSV = os.path.join(HOME, "optimized_costs_report.csv")

EXPECTED_ROWS = [
    ["service_name", "usage_hours", "cost_usd", "cost_per_hour"],
    ["BigQuery", "90", "54.00", "0.6000"],
    ["Cloud-SQL", "500", "175.00", "0.3500"],
    ["Kubernetes-Engine", "300", "90.00", "0.3000"],
    ["Compute-Engine", "720", "105.60", "0.1467"],
]

EXPECTED_DISPLAY = (
    "service_name,usage_hours,cost_usd,cost_per_hour\n"
    "BigQuery,90,54.00,0.6000\n"
    "Cloud-SQL,500,175.00,0.3500\n"
    "Kubernetes-Engine,300,90.00,0.3000\n"
    "Compute-Engine,720,105.60,0.1467"
)

@pytest.mark.describe("Final OS/filesystem state after completing the FinOps CSV optimization task")
class TestFinalState:
    def test_optimized_costs_report_csv_exists(self):
        assert os.path.isfile(OPTIMIZED_COSTS_REPORT_CSV), (
            f"Missing required output file: {OPTIMIZED_COSTS_REPORT_CSV}. "
            "You must create this report file in the specified location."
        )

    def test_optimized_costs_report_csv_content_and_order(self):
        with open(OPTIMIZED_COSTS_REPORT_CSV, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            actual_rows = list(reader)
        assert actual_rows == EXPECTED_ROWS, (
            f"{OPTIMIZED_COSTS_REPORT_CSV} does not have the exact expected content, "
            "column order, row order, or formatting.\n"
            "If you see float precision or ordering issues, check your sort key and string formatting.\n"
            f"Expected rows:\n{EXPECTED_ROWS}\nActual rows:\n{actual_rows}"
        )

    def test_optimized_costs_report_csv_line_endings(self):
        with open(OPTIMIZED_COSTS_REPORT_CSV, "rb") as f:
            content = f.read()
        assert b"\r" not in content, (
            f"{OPTIMIZED_COSTS_REPORT_CSV} must use LF (\\n) line endings only (no CR or CRLF)."
        )
        # Ensure there is no trailing blank line
        if content.endswith(b"\n"):
            # Should only be one trailing LF, not two
            assert not content.endswith(b"\n\n"), (
                f"{OPTIMIZED_COSTS_REPORT_CSV} must not have a trailing blank line at the end."
            )

    def test_optimized_costs_report_csv_field_formatting(self):
        # Check that cost_per_hour is always a float with exactly 4 decimal places, as a string
        with open(OPTIMIZED_COSTS_REPORT_CSV, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cph = row["cost_per_hour"]
                # Should match: at least one digit, a decimal, exactly four digits
                import re
                assert re.fullmatch(r"\d+\.\d{4}", cph), (
                    f"cost_per_hour value '{cph}' is not formatted with exactly 4 decimal places "
                    f"in row: {row}"
                )
                # Also check that usage_hours is integer string, cost_usd is float string with 2 decimals
                assert row["usage_hours"].isdigit(), (
                    f"usage_hours '{row['usage_hours']}' is not an integer string in row: {row}"
                )
                assert re.fullmatch(r"\d+\.\d{2}", row["cost_usd"]), (
                    f"cost_usd '{row['cost_usd']}' is not formatted as a float with 2 decimal places "
                    f"in row: {row}"
                )

    def test_optimized_costs_report_csv_no_extra_rows(self):
        # Ensure no extra services are present in the report (only the 4 expected)
        with open(OPTIMIZED_COSTS_REPORT_CSV, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            service_names = [row["service_name"] for row in reader]
        expected_services = [
            "BigQuery",
            "Cloud-SQL",
            "Kubernetes-Engine",
            "Compute-Engine",
        ]
        assert service_names == expected_services, (
            f"{OPTIMIZED_COSTS_REPORT_CSV} contains unexpected services or wrong order.\n"
            f"Expected: {expected_services}\nActual: {service_names}"
        )

    def test_terminal_output_is_report_only(self, capsys):
        """
        This test assumes the student's script is named 'solution.py' and is invoked as:
        python3 /home/user/solution.py
        If the script is invoked differently in your environment, modify as needed.
        """
        import subprocess

        # Determine the script location
        solution_py = os.path.join(HOME, "solution.py")
        if not os.path.isfile(solution_py):
            pytest.skip("Cannot find /home/user/solution.py, skipping terminal output check.")

        # Run the script and capture stdout
        result = subprocess.run(
            ["python3", solution_py],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            timeout=10,
        )
        # The only output should be the CSV file's content, exactly as in the file (including line endings)
        # Read the file's content for comparison
        with open(OPTIMIZED_COSTS_REPORT_CSV, "r", encoding="utf-8") as f:
            file_content = f.read()
        output = result.stdout.strip("\r\n")
        file_content_stripped = file_content.strip("\r\n")
        assert output == file_content_stripped, (
            "Your terminal output does not exactly match the contents of "
            f"{OPTIMIZED_COSTS_REPORT_CSV}.\n"
            "You must display ONLY the report CSV file and nothing else (no extra print statements).\n"
            f"Expected output:\n{file_content_stripped!r}\nActual output:\n{output!r}"
        )
        # Also ensure nothing was sent to stderr
        assert not result.stderr.strip(), (
            "Your script produced output to stderr:\n"
            f"{result.stderr}"
        )