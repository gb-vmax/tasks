# test_final_state.py

import os
import glob
import pytest

HOME = "/home/user"
DATA_DIR = os.path.join(HOME, "data")
SALES_CSV = os.path.join(DATA_DIR, "sales.csv")
ANALYZE_PY = os.path.join(DATA_DIR, "analyze.py")
REPORT_TXT = os.path.join(DATA_DIR, "report.txt")
VENV_DIR = os.path.join(HOME, "analyst_env")

EXPECTED_REPORT = (
    "Sales Report\n"
    "============\n"
    "Total Revenue: 4522.00\n"
    "Average Revenue: 452.20\n"
    "Top Region: North\n"
    "Total Transactions: 10\n"
)


# ── Virtual environment checks ────────────────────────────────────────────────

def test_venv_directory_exists():
    assert os.path.isdir(VENV_DIR), (
        f"Virtual environment directory does not exist: {VENV_DIR}"
    )


def test_venv_python_exists():
    python_path = os.path.join(VENV_DIR, "bin", "python")
    assert os.path.isfile(python_path) or os.path.islink(python_path), (
        f"Virtual environment Python interpreter not found at: {python_path}"
    )


def test_venv_pip_exists():
    pip_path = os.path.join(VENV_DIR, "bin", "pip")
    assert os.path.isfile(pip_path) or os.path.islink(pip_path), (
        f"Virtual environment pip not found at: {pip_path}"
    )


def test_venv_pyvenv_cfg_exists():
    cfg_path = os.path.join(VENV_DIR, "pyvenv.cfg")
    assert os.path.isfile(cfg_path), (
        f"pyvenv.cfg not found at: {cfg_path} — "
        f"{VENV_DIR} may not be a valid Python venv."
    )


def test_pandas_installed_in_venv():
    pattern = os.path.join(VENV_DIR, "lib", "python*", "site-packages", "pandas")
    matches = glob.glob(pattern)
    assert matches, (
        f"pandas does not appear to be installed inside the venv.\n"
        f"Searched pattern: {pattern}\n"
        f"No matching directories found."
    )
    # At least one match must be a directory
    dirs = [m for m in matches if os.path.isdir(m)]
    assert dirs, (
        f"pandas path(s) found but none are directories: {matches}"
    )


# ── analyze.py checks ─────────────────────────────────────────────────────────

def test_analyze_py_exists():
    assert os.path.isfile(ANALYZE_PY), (
        f"Script not found: {ANALYZE_PY}"
    )


def test_analyze_py_imports_pandas():
    with open(ANALYZE_PY, "r") as f:
        source = f.read()
    uses_pandas = ("import pandas" in source) or ("from pandas" in source)
    assert uses_pandas, (
        f"{ANALYZE_PY} does not contain 'import pandas' or 'from pandas'.\n"
        f"The script must use the pandas library, not the csv stdlib module."
    )


def test_analyze_py_does_not_import_csv_only():
    """Ensure the script isn't solely relying on the stdlib csv module."""
    with open(ANALYZE_PY, "r") as f:
        source = f.read()
    uses_pandas = ("import pandas" in source) or ("from pandas" in source)
    assert uses_pandas, (
        f"{ANALYZE_PY} must import pandas. "
        f"Found source does not include a pandas import."
    )


# ── report.txt checks ─────────────────────────────────────────────────────────

def test_report_txt_exists():
    assert os.path.isfile(REPORT_TXT), (
        f"Report file not found: {REPORT_TXT}"
    )


def test_report_txt_exact_contents():
    with open(REPORT_TXT, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_REPORT, (
        f"Contents of {REPORT_TXT} do not match expected.\n\n"
        f"Expected (repr):\n{EXPECTED_REPORT!r}\n\n"
        f"Actual (repr):\n{actual!r}"
    )


def test_report_txt_ends_with_single_newline():
    with open(REPORT_TXT, "r") as f:
        actual = f.read()
    assert actual.endswith("\n"), (
        f"{REPORT_TXT} does not end with a newline character."
    )
    assert not actual.endswith("\n\n"), (
        f"{REPORT_TXT} ends with more than one newline character."
    )


def test_report_txt_no_trailing_spaces():
    with open(REPORT_TXT, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"{REPORT_TXT}: Line {i} has trailing whitespace: {line!r}"
        )


def test_report_txt_line_count():
    with open(REPORT_TXT, "r") as f:
        actual = f.read()
    lines = actual.split("\n")
    # "Sales Report\n============\n...\nTotal Transactions: 10\n"
    # split by \n gives 7 elements, last is empty string
    assert lines[-1] == "", (
        f"{REPORT_TXT} should end with a newline (last split element should be empty)."
    )
    content_lines = lines[:-1]  # exclude trailing empty
    assert len(content_lines) == 6, (
        f"{REPORT_TXT} should have exactly 6 content lines, "
        f"but found {len(content_lines)}: {content_lines}"
    )


def test_report_txt_header_line():
    with open(REPORT_TXT, "r") as f:
        lines = f.readlines()
    assert lines[0] == "Sales Report\n", (
        f"First line of {REPORT_TXT} is wrong.\n"
        f"Expected: 'Sales Report\\n'\n"
        f"Actual:   {lines[0]!r}"
    )


def test_report_txt_separator_line():
    with open(REPORT_TXT, "r") as f:
        lines = f.readlines()
    assert lines[1] == "============\n", (
        f"Second line of {REPORT_TXT} is wrong.\n"
        f"Expected: '============\\n'\n"
        f"Actual:   {lines[1]!r}"
    )


def test_report_txt_total_revenue():
    with open(REPORT_TXT, "r") as f:
        lines = f.readlines()
    assert lines[2] == "Total Revenue: 4522.00\n", (
        f"Total Revenue line is wrong.\n"
        f"Expected: 'Total Revenue: 4522.00\\n'\n"
        f"Actual:   {lines[2]!r}"
    )


def test_report_txt_average_revenue():
    with open(REPORT_TXT, "r") as f:
        lines = f.readlines()
    assert lines[3] == "Average Revenue: 452.20\n", (
        f"Average Revenue line is wrong.\n"
        f"Expected: 'Average Revenue: 452.20\\n'\n"
        f"Actual:   {lines[3]!r}"
    )


def test_report_txt_top_region():
    with open(REPORT_TXT, "r") as f:
        lines = f.readlines()
    assert lines[4] == "Top Region: North\n", (
        f"Top Region line is wrong.\n"
        f"Expected: 'Top Region: North\\n'\n"
        f"Actual:   {lines[4]!r}\n\n"
        f"Note: North and South are tied at 3 occurrences each; "
        f"alphabetically 'North' comes before 'South'."
    )


def test_report_txt_total_transactions():
    with open(REPORT_TXT, "r") as f:
        lines = f.readlines()
    assert lines[5] == "Total Transactions: 10\n", (
        f"Total Transactions line is wrong.\n"
        f"Expected: 'Total Transactions: 10\\n'\n"
        f"Actual:   {lines[5]!r}"
    )


# ── Sales CSV integrity (should remain unchanged) ─────────────────────────────

def test_sales_csv_still_intact():
    expected = (
        "region,product,revenue\n"
        "North,Widget A,450.00\n"
        "South,Widget B,320.50\n"
        "North,Widget C,890.25\n"
        "East,Widget A,215.75\n"
        "South,Widget B,540.00\n"
        "North,Widget D,125.50\n"
        "East,Widget C,678.90\n"
        "West,Widget A,310.00\n"
        "South,Widget B,430.75\n"
        "West,Widget C,560.35\n"
    )
    with open(SALES_CSV, "r") as f:
        actual = f.read()
    assert actual == expected, (
        f"The original {SALES_CSV} has been modified!\n"
        f"Expected:\n{expected!r}\n\nActual:\n{actual!r}"
    )