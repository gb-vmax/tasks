# test_final_state.py

import csv
import os
import subprocess
import sys
import pytest

HOME = "/home/user"
VENV_DIR = os.path.join(HOME, "envs", "datawork")
VENV_PYTHON = os.path.join(VENV_DIR, "bin", "python")
VENV_PIP = os.path.join(VENV_DIR, "bin", "pip")
CLEAN_CSV = os.path.join(HOME, "data", "sales_clean.csv")

EXPECTED_ROWS = [
    {"order_id": "1001", "region": "North", "revenue": "4500"},
    {"order_id": "1002", "region": "South", "revenue": "3200"},
    {"order_id": "1004", "region": "West",  "revenue": "1800"},
    {"order_id": "1006", "region": "South", "revenue": "9100"},
    {"order_id": "1008", "region": "West",  "revenue": "4400"},
    {"order_id": "1009", "region": "South", "revenue": "7750"},
]

EXPECTED_HEADER = ["order_id", "region", "revenue"]

EXPECTED_CLEAN_CONTENT = (
    "order_id,region,revenue\n"
    "1001,North,4500\n"
    "1002,South,3200\n"
    "1004,West,1800\n"
    "1006,South,9100\n"
    "1008,West,4400\n"
    "1009,South,7750\n"
)


# ---------------------------------------------------------------------------
# Virtual environment structure
# ---------------------------------------------------------------------------

class TestVenvExists:
    def test_venv_directory_exists(self):
        assert os.path.isdir(VENV_DIR), (
            f"Virtual environment directory '{VENV_DIR}' does not exist. "
            "Run: python3 -m venv /home/user/envs/datawork"
        )

    def test_venv_python_exists(self):
        assert os.path.isfile(VENV_PYTHON), (
            f"Python executable '{VENV_PYTHON}' not found inside the venv. "
            "The venv may not have been created correctly."
        )

    def test_venv_python_is_executable(self):
        assert os.access(VENV_PYTHON, os.X_OK), (
            f"'{VENV_PYTHON}' exists but is not executable."
        )

    def test_venv_pip_exists(self):
        assert os.path.isfile(VENV_PIP), (
            f"pip executable '{VENV_PIP}' not found inside the venv. "
            "The venv may not have been created correctly."
        )

    def test_venv_pip_is_executable(self):
        assert os.access(VENV_PIP, os.X_OK), (
            f"'{VENV_PIP}' exists but is not executable."
        )

    def test_venv_python_runs(self):
        result = subprocess.run(
            [VENV_PYTHON, "--version"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"'{VENV_PYTHON} --version' failed.\nstderr: {result.stderr}"
        )

    def test_venv_python_is_isolated(self):
        """Confirm the venv python resolves to the venv directory."""
        result = subprocess.run(
            [VENV_PYTHON, "-c", "import sys; print(sys.prefix)"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"Could not query sys.prefix from venv python.\nstderr: {result.stderr}"
        )
        prefix = result.stdout.strip()
        assert prefix == VENV_DIR, (
            f"venv python sys.prefix is '{prefix}', expected '{VENV_DIR}'. "
            "The python interpreter may not belong to the correct venv."
        )


# ---------------------------------------------------------------------------
# Package installation inside the venv
# ---------------------------------------------------------------------------

class TestPackagesInstalled:
    def _get_installed_version(self, package_name: str) -> str:
        result = subprocess.run(
            [
                VENV_PYTHON, "-c",
                f"import importlib.metadata; print(importlib.metadata.version('{package_name}'))",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"Could not determine installed version of '{package_name}' in the venv.\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}\n"
            f"Make sure '{package_name}' is installed via: "
            f"{VENV_PIP} install {package_name}"
        )
        return result.stdout.strip()

    def test_pandas_installed(self):
        version = self._get_installed_version("pandas")
        assert version == "2.2.2", (
            f"pandas version in venv is '{version}', expected '2.2.2'. "
            f"Run: {VENV_PIP} install pandas==2.2.2"
        )

    def test_numpy_installed(self):
        version = self._get_installed_version("numpy")
        assert version == "1.26.4", (
            f"numpy version in venv is '{version}', expected '1.26.4'. "
            f"Run: {VENV_PIP} install numpy==1.26.4"
        )

    def test_pandas_importable(self):
        result = subprocess.run(
            [VENV_PYTHON, "-c", "import pandas"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"pandas cannot be imported inside the venv.\nstderr: {result.stderr}"
        )

    def test_numpy_importable(self):
        result = subprocess.run(
            [VENV_PYTHON, "-c", "import numpy"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"numpy cannot be imported inside the venv.\nstderr: {result.stderr}"
        )


# ---------------------------------------------------------------------------
# Cleaned CSV existence and basic properties
# ---------------------------------------------------------------------------

class TestCleanCsvExists:
    def test_clean_csv_exists(self):
        assert os.path.isfile(CLEAN_CSV), (
            f"Cleaned CSV '{CLEAN_CSV}' does not exist. "
            "Run the cleaning script with the venv python: "
            f"{VENV_PYTHON} /home/user/scripts/clean_sales.py"
        )

    def test_clean_csv_is_readable(self):
        assert os.access(CLEAN_CSV, os.R_OK), (
            f"Cleaned CSV '{CLEAN_CSV}' exists but is not readable."
        )

    def test_clean_csv_is_not_empty(self):
        size = os.path.getsize(CLEAN_CSV)
        assert size > 0, (
            f"Cleaned CSV '{CLEAN_CSV}' is empty (0 bytes)."
        )


# ---------------------------------------------------------------------------
# Cleaned CSV content correctness
# ---------------------------------------------------------------------------

class TestCleanCsvContent:
    @pytest.fixture(autouse=True)
    def require_file(self):
        if not os.path.isfile(CLEAN_CSV):
            pytest.skip(f"'{CLEAN_CSV}' does not exist; skipping content tests.")

    def _read_csv(self):
        with open(CLEAN_CSV, newline="") as fh:
            reader = csv.DictReader(fh)
            rows = list(reader)
            fieldnames = reader.fieldnames
        return fieldnames, rows

    def test_header_columns_correct(self):
        fieldnames, _ = self._read_csv()
        assert list(fieldnames) == EXPECTED_HEADER, (
            f"CSV header is {list(fieldnames)}, expected {EXPECTED_HEADER}. "
            "Columns must be in the order: order_id, region, revenue."
        )

    def test_row_count(self):
        _, rows = self._read_csv()
        assert len(rows) == len(EXPECTED_ROWS), (
            f"CSV has {len(rows)} data rows, expected {len(EXPECTED_ROWS)}. "
            "Rows with missing or negative revenue should be dropped."
        )

    def test_no_index_column(self):
        """Ensure the file was written with index=False (no unnamed index col)."""
        fieldnames, _ = self._read_csv()
        for col in fieldnames:
            assert not col.startswith("Unnamed"), (
                f"Found an index column '{col}' in the CSV. "
                "Write the CSV with: df.to_csv(..., index=False)"
            )

    def test_order_ids_correct(self):
        _, rows = self._read_csv()
        actual_ids = [r["order_id"] for r in rows]
        expected_ids = [r["order_id"] for r in EXPECTED_ROWS]
        assert actual_ids == expected_ids, (
            f"order_id values are {actual_ids}, expected {expected_ids}. "
            "Check which rows are dropped (missing or negative revenue)."
        )

    def test_regions_correct(self):
        _, rows = self._read_csv()
        actual_regions = [r["region"] for r in rows]
        expected_regions = [r["region"] for r in EXPECTED_ROWS]
        assert actual_regions == expected_regions, (
            f"region values are {actual_regions}, expected {expected_regions}. "
            "Make sure leading/trailing whitespace is stripped from the region column."
        )

    def test_revenue_values_are_integers(self):
        _, rows = self._read_csv()
        for row in rows:
            val = row["revenue"]
            assert val.lstrip("-").isdigit(), (
                f"revenue value '{val}' for order_id={row['order_id']} "
                "is not an integer string. Revenue must be converted to int "
                "(truncating decimals)."
            )

    def test_revenue_values_correct(self):
        _, rows = self._read_csv()
        actual_revenues = [r["revenue"] for r in rows]
        expected_revenues = [r["revenue"] for r in EXPECTED_ROWS]
        assert actual_revenues == expected_revenues, (
            f"revenue values are {actual_revenues}, expected {expected_revenues}. "
            "Check that decimals are truncated (cast to int) and that negative "
            "revenue rows are removed."
        )

    def test_no_negative_revenue(self):
        _, rows = self._read_csv()
        for row in rows:
            try:
                rev = int(row["revenue"])
            except ValueError:
                pytest.fail(
                    f"revenue '{row['revenue']}' for order_id={row['order_id']} "
                    "cannot be parsed as an integer."
                )
            assert rev >= 0, (
                f"Row with order_id={row['order_id']} has negative revenue {rev}. "
                "Rows with negative revenue must be dropped."
            )

    def test_no_missing_revenue(self):
        _, rows = self._read_csv()
        for row in rows:
            assert row["revenue"].strip() != "", (
                f"Row with order_id={row['order_id']} has an empty revenue value. "
                "Rows with missing revenue must be dropped."
            )

    def test_exact_file_content(self):
        with open(CLEAN_CSV, newline="") as fh:
            actual = fh.read()
        assert actual == EXPECTED_CLEAN_CONTENT, (
            f"Exact file content of '{CLEAN_CSV}' does not match expected.\n\n"
            f"Expected:\n{EXPECTED_CLEAN_CONTENT!r}\n\n"
            f"Got:\n{actual!r}"
        )

    def test_region_no_leading_trailing_whitespace(self):
        _, rows = self._read_csv()
        for row in rows:
            region = row["region"]
            assert region == region.strip(), (
                f"Region '{region}' for order_id={row['order_id']} has "
                "leading or trailing whitespace. Strip the region column."
            )