I'm a data analyst and I need help setting up a Python virtual environment and processing a CSV file with it. Here's what I need done:

There's a CSV file at `/home/user/data/sales.csv` that contains sales records. I need you to:

1. Create a Python virtual environment using `venv` at `/home/user/analyst_env`.

2. Install the `pandas` package into that virtual environment (and only that virtual environment — do not use any system Python or pip).

3. Using the Python interpreter from the virtual environment at `/home/user/analyst_env`, run a Python script that reads `/home/user/data/sales.csv` and writes a summary report to `/home/user/data/report.txt`.

The script should be saved at `/home/user/data/analyze.py` and must use `pandas` to compute the following from the CSV file:

- The **total revenue** across all rows (sum of the `revenue` column), formatted as a float with exactly 2 decimal places.
- The **average revenue** per row (mean of the `revenue` column), formatted as a float with exactly 2 decimal places.
- The **top-selling region** (the value in the `region` column that appears most frequently; if tied, use the one that comes first alphabetically).
- The **number of rows** in the CSV (not counting the header).

The output file `/home/user/data/report.txt` must contain exactly the following format (with actual computed values substituted in):

```
Sales Report
============
Total Revenue: <value>
Average Revenue: <value>
Top Region: <value>
Total Transactions: <value>
```

For example, if total revenue were 1234.56, average were 411.52, top region were "North", and there were 3 rows, the file would contain:

```
Sales Report
============
Total Revenue: 1234.56
Average Revenue: 411.52
Top Region: North
Total Transactions: 3
```

There should be no trailing spaces on any line, and the file should end with a single newline character. The script must import `pandas` (not the `csv` stdlib module) — this will be verified by inspecting `analyze.py`.

Please make sure the virtual environment is fully set up at `/home/user/analyst_env`, the script is saved at `/home/user/data/analyze.py`, and the report is written to `/home/user/data/report.txt`.
