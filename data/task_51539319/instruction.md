I have a CSV file at `/home/user/data/sales.csv` that contains sales transaction data. The file has these columns in this order: `transaction_id`, `date`, `salesperson`, `region`, `product`, `quantity`, `unit_price`, `total`.

My reporting tool needs a simplified CSV with only three columns, and in a specific order: `date`, `salesperson`, `total`. The header row must be included. I want the output saved to `/home/user/data/sales_report.csv`.

Can you extract just those three columns (in that order: `date` first, then `salesperson`, then `total`) from the original file and write them to `/home/user/data/sales_report.csv`?

The output file should have no extra blank lines, no extra spaces, and use commas as delimiters — exactly matching the original CSV formatting style. The header row should be `date,salesperson,total` and each data row should follow the same pattern.
