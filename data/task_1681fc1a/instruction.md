Hey, I have a CSV file of sales transactions at `/home/user/data/sales.csv` that I need to clean and summarize. The file has some bad rows — missing fields and non-numeric values in columns that should be numeric. Can you help me process it?

Here's what I need you to do:

**Step 1: Filter the CSV to keep only valid rows.**

The CSV has a header row followed by data rows with these columns (in order):
`transaction_id,product,quantity,unit_price,region`

A row is **valid** if ALL of the following are true:
- It has exactly 5 fields (no missing or extra columns)
- `quantity` is a positive integer (whole number greater than 0)
- `unit_price` is a positive number (greater than 0, can be a decimal)
- `region` is one of: `north`, `south`, `east`, `west` (case-sensitive, lowercase only)

Write all valid rows (including the header) to `/home/user/data/sales_clean.csv`, preserving the original column order and values exactly as they appear.

**Step 2: Compute a summary.**

From the cleaned data (valid rows only), calculate the **total revenue per region**, where:
`revenue = quantity * unit_price`

Write the results to `/home/user/data/sales_summary.txt` in this exact format:
```
Sales Summary
=============
east: <total>
north: <total>
south: <total>
west: <total>
Total: <grand_total>
```

The regions must be listed in alphabetical order. Each total should be a plain decimal number rounded to 2 decimal places (e.g., `1234.50`). The grand total is the sum of all regions' revenues. There should be a blank line between the `=============` line and the first region line, and no trailing blank lines at the end of the file.

For example, if `east` had one transaction of quantity 3 and unit_price 10.00, it would show `east: 30.00`.
