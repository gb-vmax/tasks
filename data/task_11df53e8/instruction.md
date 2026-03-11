Hey, I need help processing a sales CSV file. I have a file at `/home/user/data/sales.csv` that contains transaction records, and I need to extract a filtered subset of rows and save them to a new file.

The CSV has these columns (with a header row):
```
transaction_id,date,region,product_code,amount,status
```

I need you to do the following:

1. From `/home/user/data/sales.csv`, extract only the rows where:
   - The `product_code` column matches the pattern `^PRD-[0-9]{3}$` (exactly "PRD-" followed by exactly 3 digits), AND
   - The `status` column is either `completed` or `refunded` (case-sensitive, exact match)

2. From those filtered rows, keep only four columns in this order: `transaction_id`, `date`, `amount`, `status`. Drop the `region` and `product_code` columns entirely.

3. Write the result to `/home/user/data/filtered_sales.csv`. The output file must include the header line `transaction_id,date,amount,status` as the first line, followed by the matching data rows in the same order they appeared in the original file.

The output file should have no trailing whitespace, no blank lines, and Unix line endings.

Can you produce `/home/user/data/filtered_sales.csv` with the correct filtered and reformatted content?
