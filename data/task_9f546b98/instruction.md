I have a CSV file at `/home/user/data/sales.csv` that tracks monthly sales data for different product categories. I need you to process it and generate a summary report.

The CSV file has a header row followed by data rows in this format:
```
region,category,month,units_sold,revenue
```

I need you to do two things:

**Step 1:** Using `awk`, extract only the rows where `revenue` is greater than 5000, and write them to `/home/user/data/high_revenue.csv`. The output file should include the header row as the first line, followed by the matching data rows in their original order. Do not include the dollar sign or any other formatting — just the raw CSV data as-is.

**Step 2:** Using `sed`, transform the `high_revenue.csv` file to produce `/home/user/data/report.txt` where:
- The word `North` is replaced with `Northern`
- The word `South` is replaced with `Southern`
- The header line `region,category,month,units_sold,revenue` is replaced with `REGION,CATEGORY,MONTH,UNITS_SOLD,REVENUE` (all uppercase)

The final `/home/user/data/report.txt` should reflect both substitutions applied to the high-revenue data. The file should have no trailing newline issues — just clean lines, one per row.

Please process the file and produce both output files.
</tale>
