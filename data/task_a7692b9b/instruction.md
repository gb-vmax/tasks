I'm a capacity planner and I need your help analyzing server resource usage data. We have a log file at `/home/user/capacity/server_metrics.csv` that records CPU and memory usage at 15-minute intervals. All timestamps in the log are in UTC, but our operations team works in the `America/New_York` timezone, so I need the final report to show times converted to Eastern Time.

Here's what I need you to do:

**Step 1: Inspect the data**
The file `/home/user/capacity/server_metrics.csv` has four columns (comma-separated, with a header row):
- `timestamp`: UTC timestamps in the format `YYYY-MM-DD HH:MM:SS`
- `cpu_percent`: float, CPU usage percentage (0.0–100.0)
- `mem_percent`: float, memory usage percentage (0.0–100.0)
- `server_id`: string, always `"srv-01"`

**Step 2: Convert all timestamps to America/New_York**
For each data row, convert the UTC timestamp to the local time in the `America/New_York` timezone. The data spans a period that includes a DST boundary (clocks spring forward), so some rows will be EST (UTC-5) and others will be EDT (UTC-4). You must handle this correctly.

**Step 3: Compute the following statistics using the New_York-local times**

- **Peak CPU hour**: The 1-hour window (identified by its start, on the hour) during which the average CPU usage is highest. Express the hour in New York local time, formatted as `YYYY-MM-DD HH:MM TZ` where TZ is either `EST` or `EDT`.
- **Peak memory hour**: Same as above but for memory usage.
- **Overall average CPU**: Average of all cpu_percent values across all rows, rounded to 2 decimal places.
- **Overall average memory**: Average of all mem_percent values across all rows, rounded to 2 decimal places.
- **DST transition row**: The first row (by timestamp order) whose New York local time is EDT (i.e., UTC-4). Report its New York local timestamp in the format `YYYY-MM-DD HH:MM EDT`.
- **High CPU intervals**: Count of rows where cpu_percent > 75.0.
- **High memory intervals**: Count of rows where mem_percent > 80.0.

**Step 4: Write the report**
Write the results to `/home/user/capacity/usage_report.txt` using EXACTLY this format (replace angle-bracket placeholders with computed values, and do not include the angle brackets themselves):

```
=== SERVER CAPACITY REPORT ===
Server: srv-01
Report timezone: America/New_York

--- CPU ANALYSIS ---
Overall average CPU: <value>%
Peak CPU hour: <YYYY-MM-DD HH:MM TZ>
High CPU intervals (>75%): <count>

--- MEMORY ANALYSIS ---
Overall average memory: <mem_value>%
Peak memory hour: <YYYY-MM-DD HH:MM TZ>
High memory intervals (>80%): <count>

--- DST NOTE ---
First EDT interval: <YYYY-MM-DD HH:MM EDT>
```

There must be a newline at the end of the file. Every line must match exactly, including spacing, punctuation, the `%` signs, and the section separators. Do not add any extra lines or trailing spaces.
