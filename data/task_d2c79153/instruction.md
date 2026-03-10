I'm building a small utility to process a sales data file and generate a summary report. I have a pipe-delimited file at `/home/user/data/sales.psv` that contains raw sales records. I need you to process this file using `awk` and `sed` to produce a clean, formatted report.

The file has lines in this format:
```
REGION|SALESPERSON|PRODUCT|UNITS|UNIT_PRICE
```

The first line is a header and should be skipped. The data lines look like:
```
West|Alice|Widget|12|4.50
```

Here is exactly what I need you to do:

**Step 1 — Compute line totals and reformat with `awk`:**

Using `awk`, read `/home/user/data/sales.psv`, skip the header line, and for each data line compute `TOTAL = UNITS * UNIT_PRICE`. Print a new pipe-delimited line with five fields: `REGION`, `SALESPERSON`, `PRODUCT`, `UNITS`, and `TOTAL` (formatted to exactly 2 decimal places). Write the result to `/home/user/data/sales_totals.psv`.

The output should have NO header line and look like:
```
West|Alice|Widget|12|54.00
```

**Step 2 — Use `sed` to produce a human-readable report:**

Using `sed`, transform `/home/user/data/sales_totals.psv` so that each pipe-delimited line becomes a sentence in this exact format:
```
[REGION] SALESPERSON sold UNITS units of PRODUCT for $TOTAL
```

For example, the line `West|Alice|Widget|12|54.00` should become:
```
[West] Alice sold 12 units of Widget for $54.00
```

Write this output to `/home/user/data/sales_report.txt`.

**Step 3 — Append a grand total line using `awk`:**

Using `awk`, read `/home/user/data/sales_totals.psv` (NOT the report file), sum the fifth field (TOTAL) across all rows, and append a final line to `/home/user/data/sales_report.txt` in this exact format:
```
GRAND TOTAL: $<sum formatted to 2 decimal places>
```

For example, if the totals are 54.00 and 30.00, append:
```
GRAND TOTAL: $84.00
```

The final `/home/user/data/sales_report.txt` should contain one sentence per sales record (in the original file order) followed by exactly one `GRAND TOTAL:` line at the end.

Please produce exactly these two output files:
- `/home/user/data/sales_totals.psv`
- `/home/user/data/sales_report.txt`
