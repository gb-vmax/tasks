Hi, I'm a FinOps analyst and I need your help reshaping a cloud cost report so it's easier to read in our billing dashboard. The report was exported from AWS Cost Explorer and the columns are in an inconvenient order.

The file is located at `/home/user/finops/aws_costs.csv`. It's a comma-separated file.

I need you to reorder the columns and output the result to `/home/user/finops/aws_costs_reordered.csv`.

**Current column order in the file:**
1. `region`
2. `service`
3. `account_id`
4. `cost_usd`
5. `usage_hours`
6. `team`

**Required column order in the output:**
1. `team`
2. `account_id`
3. `region`
4. `service`
5. `cost_usd`
6. `usage_hours`

The output file must:
- Be comma-delimited (same as the input)
- Include the header row (reordered too)
- Have no trailing spaces or extra blank lines
- Preserve every data row exactly as-is (just reordered columns — no rounding, no reformatting of values)

Please produce the reordered file at `/home/user/finops/aws_costs_reordered.csv`.
