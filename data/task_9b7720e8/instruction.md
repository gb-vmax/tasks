Hey, I need your help cleaning up a training dataset before I can use it for model training. I have a raw CSV file at `/home/user/ml_project/raw_samples.csv` that was exported from our data collection pipeline, and it has some corrupted or invalid records mixed in.

The file has a header row followed by data rows with these columns:
- `sample_id`: a string identifier (must be non-empty)
- `feature1`: a float (must be between -10.0 and 10.0 inclusive)
- `feature2`: a float (must be between -10.0 and 10.0 inclusive)
- `label`: an integer, either 0 or 1

I need you to validate each data row and split it into two output files:

**Clean data → `/home/user/ml_project/clean_samples.csv`**
Write only rows that pass ALL validation checks. Include the header row as the first line. Preserve the original row values exactly as they appeared in the input (no reformatting of numbers).

**Rejected data → `/home/user/ml_project/rejected_samples.csv`**
Write rows that failed at least one check. Include a header row as the first line, with the original columns plus an additional final column called `error_reason`. Preserve the original row values exactly as they appeared. For the `error_reason` column, use these exact strings based on what failed (if multiple errors exist, report only the first that applies in this priority order):
1. `missing_field` — if any of the four fields is empty or the row has fewer than 4 fields
2. `invalid_feature1` — if `feature1` cannot be parsed as a float, or is outside [-10.0, 10.0]
3. `invalid_feature2` — if `feature2` cannot be parsed as a float, or is outside [-10.0, 10.0]
4. `invalid_label` — if `label` cannot be parsed as an integer, or is not 0 or 1

The output files must use Unix line endings. Do not include a trailing newline after the last data row.

Please process the file and create both output files.
