Hey, I need some help preparing a training dataset for a classification model. I have a raw CSV file at `/home/user/ml_data/raw_samples.csv` that contains sensor readings, and I need to clean and filter it before I can use it for training.

Here's what I need you to do:

1. **Filter the data**: Keep only rows where the `quality_score` column is greater than or equal to `0.75` AND the `label` column is not equal to `"unknown"`.

2. **Select and reorder columns**: From the filtered rows, keep only these four columns in this exact order: `sample_id`, `feature_a`, `feature_b`, `label`.

3. **Sort the output**: Sort the resulting rows by `sample_id` in ascending numerical order.

4. **Write the output**: Save the result to `/home/user/ml_data/training_ready.csv`. The file must:
   - Have a header row: `sample_id,feature_a,feature_b,label`
   - Have each data row as comma-separated values with no extra spaces
   - Keep `feature_a` and `feature_b` values exactly as they appear in the source (no rounding or reformatting)
   - Have a trailing newline at the end of the file (i.e., the last line ends with `\n`)
   - Have NO blank lines anywhere in the file

The output file should contain only the header plus the rows that passed both filter conditions, sorted by `sample_id`.

Can you process this and write the final file to `/home/user/ml_data/training_ready.csv`?
