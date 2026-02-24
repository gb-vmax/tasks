You are a FinOps analyst tasked with optimizing monthly cloud costs. In your home directory (/home/user), you have received two files:

1. A CSV file at /home/user/cloud_costs.csv containing the following columns:
   - service_name
   - usage_hours
   - cost_usd

2. A JSON file at /home/user/services_to_optimize.json, containing an array of service names that are targeted for cost optimization.

Your objectives are:

1. Read the list of targeted services from services_to_optimize.json.
2. Filter the rows in cloud_costs.csv to include only the services whose names appear in the "services_to_optimize.json" array.
3. For each filtered service, calculate the "cost_per_hour" as cost_usd divided by usage_hours. (Be careful with the data type: cost_usd may have decimals, usage_hours is an integer. Present cost_per_hour as a float with exactly 4 decimal places, e.g., 0.1234.)
4. Create a new CSV file called /home/user/optimized_costs_report.csv with the following columns in order:
   - service_name
   - usage_hours
   - cost_usd
   - cost_per_hour

   Include the header row. The data rows should be sorted by "cost_per_hour" in descending order.

5. The output CSV must match this format exactly (comma-separated, double quotes for fields not required, header on the first row, fields as described).

6. When you are done, display only the contents of /home/user/optimized_costs_report.csv in the terminal.

Hint: Make sure that the final "cost_per_hour" values have 4 decimal places with rounding as appropriate, and that only services present in the JSON appear in the report.
