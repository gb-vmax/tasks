You are helping a capacity planner analyze resource usage in an organization using an SQLite database via the CLI. In your home directory (/home/user), there is a SQLite database file named /home/user/capacity_resources.db. Your task is to use only the sqlite3 CLI tool to:

1. Create a new table named 'resources' with the following schema:
   - id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
   - resource_type (TEXT)
   - resource_name (TEXT)
   - usage_percent (REAL CHECK(usage_percent >= 0 AND usage_percent <= 100))
   - analysis_date (TEXT, format 'YYYY-MM-DD')

2. Insert the following records into the 'resources' table (all on the same analysis_date: '2024-06-01'):
   - resource_type: 'CPU', resource_name: 'Server01', usage_percent: 63.5
   - resource_type: 'Memory', resource_name: 'Server01', usage_percent: 74.2
   - resource_type: 'Disk', resource_name: 'DBStorage', usage_percent: 87.9
   - resource_type: 'CPU', resource_name: 'Server02', usage_percent: 41.0

3. Create a SELECT SQL statement that retrieves, in a single query, the average usage_percent for each resource_type, and the maximum usage_percent value on '2024-06-01'. Save only the plain-text output (no headers, no column labels, no formatting other than single space separation) of this query to a file called /home/user/resource_stats.log.

   The output file, /home/user/resource_stats.log, must have exactly one line per resource_type, with each line in the format:
   <resource_type> <average_usage_percent> <max_usage_percent>
   For example:
   CPU 52.25 63.5
   Disk 87.9 87.9
   Memory 74.2 74.2

   All floats must be rounded to two decimal places.

4. When you are done, the file /home/user/resource_stats.log should exist, containing one line per resource_type. The lines can appear in any order.

Do not include any other text, explanations, or output—just the specified log file with the results.
