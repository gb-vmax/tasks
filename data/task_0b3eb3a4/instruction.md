You are a machine learning engineer preparing a CSV dataset for model training. In the directory <code>/home/user/data_pipeline/</code>, you will find a file called <code>raw_customers.csv</code>. This file may contain blank lines and some rows in which the <code>age</code> field is missing or not a number.

Your task is to perform the following data-cleaning step:

1. Create a new file named <code>cleaned_customers.csv</code> in the same directory (<code>/home/user/data_pipeline/</code>).
2. Copy over the header line as-is.
3. For all following rows, only include:
     - Rows that are NOT blank.
     - Rows where the <code>age</code> field exists and is a non-empty integer (no decimals, not missing or blank, and no non-numeric strings).
4. For rows that do not meet these criteria (i.e., blank row or invalid/missing <code>age</code>), skip them BUT log the skipped line (entire raw line, unmodified) into a file <code>error_rows.log</code> in the same directory.

The output <code>cleaned_customers.csv</code> must preserve the original column ordering and contain only valid, cleaned rows (plus the header). The <code>error_rows.log</code> must contain each skipped raw line (including blank lines), as-is, in the order encountered in <code>raw_customers.csv</code>; do not include headers.

Both output files will be checked for correctness, so make sure the formatting (commas, new lines, and order) is strictly correct and consistent with the above requirements.
