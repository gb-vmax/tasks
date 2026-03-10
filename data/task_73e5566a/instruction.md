Hey, I'm a machine learning engineer and I need your help running a quick diagnostic check on a training dataset before I start preprocessing it. The dataset is a CSV file at `/home/user/data/training_samples.csv`.

I need you to generate a diagnostic report at `/home/user/data/dataset_report.txt`. The report should give me a snapshot of the dataset's health so I can decide what cleaning steps are needed.

Please compute the following and write them to the report in **exactly** this format (including blank lines and spacing as shown):

```
=== DATASET DIAGNOSTIC REPORT ===

File: /home/user/data/training_samples.csv
Total rows (excluding header): <N>
Total columns: <N>

=== COLUMN STATS ===
<column_name>: min=<min_val>, max=<max_val>, missing=<count>
<column_name>: min=<min_val>, max=<max_val>, missing=<count>
<column_name>: min=<min_val>, max=<max_val>, missing=<count>
<column_name>: min=<min_val>, max=<max_val>, missing=<count>

=== MISSING VALUE SUMMARY ===
Total missing values: <N>
Columns with missing data: <N>
```

Important details:
- The CSV has a header row. "Total rows" should NOT count the header.
- "Total columns" is the number of column headers in the first row.
- For the COLUMN STATS section, list every column in the order they appear in the CSV.
- `min` and `max` should be computed only over non-missing numeric values, as plain integers (no decimals).
- `missing` is the count of empty fields in that column across all data rows.
- For columns where ALL values are missing, write `min=N/A, max=N/A`.
- "Total missing values" is the sum of all missing fields across all columns and rows.
- "Columns with missing data" is the count of columns that have at least one missing value.
- All numeric min/max values should be written as integers (e.g., `42` not `42.0`).
