# test_final_state.py

import os
import re
import pytest

ETL_DIR = '/home/user/etl_legacy'
RUN_ETL = os.path.join(ETL_DIR, 'run_etl.py')
SALES_RAW = os.path.join(ETL_DIR, 'sales_raw.csv')
SALES_PROCESSED = os.path.join(ETL_DIR, 'sales_processed.csv')
ETL_LOG = os.path.join(ETL_DIR, 'etl_run.log')

SALES_PROCESSED_EXPECTED = (
    "product,amount,date,processed\n"
    "Widget,100,2023-01-05,yes\n"
    "Gadget,150,2023-01-06,yes\n"
)
ETL_LOG_SECOND_LINE = "ETL run completed successfully."

@pytest.mark.describe("Final OS/filesystem state after ETL has run")
def test_sales_processed_csv_exists_and_contents():
    assert os.path.isfile(SALES_PROCESSED), (
        f"The output CSV '{SALES_PROCESSED}' is missing.\n"
        "You must run the ETL script so that this file is created."
    )
    with open(SALES_PROCESSED, 'r', encoding='utf-8') as f:
        contents = f.read()
    assert contents == SALES_PROCESSED_EXPECTED, (
        f"The contents of '{SALES_PROCESSED}' do not match the expected output.\n"
        "Expected:\n" +
        SALES_PROCESSED_EXPECTED +
        "But got:\n" +
        contents
    )

def test_etl_run_log_exists_and_format():
    assert os.path.isfile(ETL_LOG), (
        f"The log file '{ETL_LOG}' is missing.\n"
        "You must create this file after running the ETL script."
    )
    with open(ETL_LOG, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    assert len(lines) == 2, (
        f"The log file '{ETL_LOG}' must contain exactly 2 lines.\n"
        f"Found {len(lines)} lines."
    )
    timestamp = lines[0].rstrip('\n')
    message = lines[1].rstrip('\n')

    # ISO 8601 timestamp: e.g. 2024-07-01T09:32:00 (no timezone, no microseconds)
    iso8601_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$'
    assert re.match(iso8601_regex, timestamp), (
        f"The first line of '{ETL_LOG}' must be an ISO 8601 timestamp (YYYY-MM-DDTHH:MM:SS).\n"
        f"Found: {timestamp}"
    )
    assert message == ETL_LOG_SECOND_LINE, (
        f"The second line of '{ETL_LOG}' must be exactly:\n"
        f"{ETL_LOG_SECOND_LINE}\n"
        f"But found:\n"
        f"{message}"
    )

def test_no_unexpected_files_created():
    expected_files = {
        "run_etl.py",
        "sales_raw.csv",
        "sales_processed.csv",
        "etl_run.log",
    }
    found_files = set(os.listdir(ETL_DIR))
    unexpected = found_files - expected_files
    assert not unexpected, (
        f"Unexpected files found in '{ETL_DIR}': {sorted(unexpected)}\n"
        "Only these files should exist after the task: "
        + ", ".join(sorted(expected_files))
    )

def test_run_etl_py_unchanged():
    # Confirm the ETL script was not modified
    expected = (
        "import csv\n"
        "\n"
        "with open('sales_raw.csv', newline='') as infile, open('sales_processed.csv', 'w', newline='') as outfile:\n"
        "    reader = csv.DictReader(infile)\n"
        "    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames + ['processed'])\n"
        "    writer.writeheader()\n"
        "    for row in reader:\n"
        "        row['processed'] = 'yes'\n"
        "        writer.writerow(row)\n"
    )
    with open(RUN_ETL, 'r', encoding='utf-8') as f:
        contents = f.read()
    assert contents == expected, (
        f"The ETL script '{RUN_ETL}' was modified. It must remain exactly as originally provided."
    )

def test_sales_raw_csv_unchanged():
    # Confirm the input file was not modified
    expected = (
        "product,amount,date\n"
        "Widget,100,2023-01-05\n"
        "Gadget,150,2023-01-06\n"
    )
    with open(SALES_RAW, 'r', encoding='utf-8') as f:
        contents = f.read()
    assert contents == expected, (
        f"The input file '{SALES_RAW}' was modified. It must remain exactly as originally provided."
    )