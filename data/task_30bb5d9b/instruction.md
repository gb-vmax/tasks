Hey, I need your help setting up alert thresholds for our server monitoring system. I have a CSV file at `/home/user/monitoring/metrics.csv` that contains historical performance data for several servers. I need you to process this data and generate an alert configuration file that our monitoring daemon can consume.

The CSV file has these columns:
- `server`: server hostname
- `metric`: the metric name (e.g., `cpu_usage`, `mem_usage`, `disk_io`)
- `value`: a float reading

For each unique combination of `server` and `metric`, I need you to:
1. Compute the **maximum** value observed
2. Compute the **average** value observed (rounded to 2 decimal places)
3. Set the **alert threshold** to `average + 20% of (max - average)`, rounded to 2 decimal places

Then write the results to `/home/user/monitoring/alert_thresholds.cfg` in this exact format:

```
[server:metric]
max=<value>
avg=<value>
threshold=<value>

[server:metric]
max=<value>
avg=<value>
threshold=<value>
```

Rules for the output file:
- Each section header is `[<server>:<metric>]` with no spaces around the colon
- `max` should be the raw maximum value from the CSV (no rounding — preserve it as it appears, as an integer if it has no decimal part, or with its original decimal digits)
- `avg` and `threshold` are rounded to 2 decimal places
- Sections are separated by a single blank line
- Sections must be sorted first by server name alphabetically, then by metric name alphabetically within each server
- There is NO trailing blank line at the end of the file

For example, if `webserver01` had `cpu_usage` readings of 45.0, 60.0, and 75.0:
- max = 75.0
- avg = (45+60+75)/3 = 60.0
- threshold = 60.0 + 0.20*(75.0-60.0) = 60.0 + 3.0 = 63.0

The file should be written to `/home/user/monitoring/alert_thresholds.cfg`.
