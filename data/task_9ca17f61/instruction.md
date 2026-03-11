I'm a FinOps analyst and I need to quickly audit which cloud services are running in our environment and what their monthly costs look like. I have a CSV file at `/home/user/finops/resources.csv` that lists all provisioned cloud resources.

Can you help me produce a cost summary report? Specifically:

1. Parse `/home/user/finops/resources.csv`. The file has these columns (comma-separated, with a header row):
   - `resource_id`: unique identifier (e.g., `i-0a1b2c3d`)
   - `service`: cloud service type (e.g., `EC2`, `RDS`, `S3`)
   - `region`: AWS region (e.g., `us-east-1`)
   - `monthly_cost_usd`: a decimal number representing monthly cost in USD

2. Compute the **total monthly cost per service** by summing `monthly_cost_usd` for all rows with the same `service` value.

3. Write the results to `/home/user/finops/cost_summary.txt` in this exact format:

```
Monthly Cost Summary
====================
EC2: $<total>
RDS: $<total>
S3: $<total>
====================
Total: $<grand_total>
```

Where:
- Services are listed in **alphabetical order**
- Each `<total>` is rounded to **2 decimal places** (e.g., `$143.20`, not `$143.2` or `$143.200`)
- The grand total is also rounded to 2 decimal places
- There are no extra spaces or trailing whitespace on any line
- The file ends with a single newline character

Please write the cost summary to `/home/user/finops/cost_summary.txt`.
