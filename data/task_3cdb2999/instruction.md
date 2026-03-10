Hey, I need help setting up a Python environment and cleaning a dataset. I have a messy CSV file at `/home/user/data/sales_raw.csv` that needs some cleaning, and I want to keep everything isolated in a virtual environment.

Here's what I need you to do:

1. Create a Python virtual environment at `/home/user/envs/datawork` using the `venv` module.

2. Using the pip from that virtual environment (NOT any system pip), install `pandas` version `2.2.2` and `numpy` version `1.26.4`.

3. Run the script `/home/user/scripts/clean_sales.py` using the Python interpreter from that virtual environment. The script will read `/home/user/data/sales_raw.csv`, clean it, and write the result to `/home/user/data/sales_clean.csv`.

**The script logic (you do not need to write this — it already exists):**
- Drops any rows where `revenue` is missing or negative
- Strips leading/trailing whitespace from the `region` column
- Converts the `revenue` column to integers (truncating any decimals)
- Writes the cleaned data to `/home/user/data/sales_clean.csv` with no index column

**Expected output file format for `/home/user/data/sales_clean.csv`:**

The file should be a standard comma-separated CSV with a header row, and the columns in this order: `order_id`, `region`, `revenue`. Each data row should have an integer in the `revenue` column. Example of valid rows:

```
order_id,region,revenue
1001,North,4500
1002,South,3200
```

Please make sure the virtual environment is fully set up at `/home/user/envs/datawork` and the cleaned CSV is written to `/home/user/data/sales_clean.csv`.
</think>
