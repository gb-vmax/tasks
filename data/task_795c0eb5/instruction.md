As a data analyst, you have a CSV file located at <code>/home/user/data/sales.csv</code>. This file contains sales transactions with the columns: <code>ID</code>, <code>Date</code>, <code>Customer</code>, <code>Amount</code>. However, some rows may be malformed (such as missing columns or commas inside quoted fields breaking the format). Your task is to process this file in a way that:

1. Extracts only the rows that are well-formed and have all four columns present.
2. Writes these valid rows to a new file at <code>/home/user/data/clean_sales.csv</code> in the exact same column order as the original.
3. Logs any malformed lines that were skipped (including the full line content) into a separate plain text log file at <code>/home/user/data/sales_errors.log</code>, one per line, in the order encountered.

The output must meet the following specifications:
- <code>/home/user/data/clean_sales.csv</code> must contain the original header row, followed by only well-formed data rows.
- <code>/home/user/data/sales_errors.log</code> must contain exactly one line per malformed row (no additional output or line numbers).

Only these two output files should be changed or created. The test will automatically check that the output formats and contents match these requirements.
