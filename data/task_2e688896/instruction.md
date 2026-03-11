Hey, I need some help processing a sales CSV file on my Linux machine. I have a file at `/home/user/data/sales.csv` that contains daily sales records. I need to generate a quick diagnostic summary of the data to share with my manager.

The CSV file has the following columns (with a header row):
```
date,region,product,units_sold,revenue
```

I need you to produce a summary report at `/home/user/data/sales_summary.txt`. Here's exactly what the report should contain:

```
=== SALES DATA SUMMARY ===
Total records: <N>
Total units sold: <N>
Total revenue: <N>

=== REVENUE BY REGION ===
<region>: <revenue>
<region>: <revenue>
...

=== TOP PRODUCT BY UNITS SOLD ===
<product>: <total_units>
```

A few important notes about the format:

- "Total records" should be the count of data rows only (not counting the header line).
- "Total units sold" and "Total revenue" are the sums of those columns across all rows.
- All numeric values should be plain integers (no decimal points, no commas, no dollar signs).
- In the "REVENUE BY REGION" section, list each region and its total revenue, sorted by revenue in **descending** order. Each line should be formatted as `  <region>: <revenue>` (two leading spaces before the region name).
- "TOP PRODUCT BY UNITS SOLD" should show the single product with the highest total units across all rows, formatted as `  <product>: <total_units>` (two leading spaces).
- There should be a blank line between each of the three sections (after the last line of one section and before the `===` header of the next).

The final file at `/home/user/data/sales_summary.txt` is what I need — please create it with exactly the right content.
