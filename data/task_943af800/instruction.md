I'm a DevOps engineer trying to debug a series of service failures that happened yesterday. I have a CSV log file at `/home/user/logs/service_errors.csv` with the following columns:

```
timestamp,service,level,error_code,response_time_ms,region
```

Where:
- `timestamp`: format `YYYY-MM-DD HH:MM:SS`
- `service`: one of several service names
- `level`: `ERROR`, `WARN`, or `INFO`
- `error_code`: an integer (0 means no error)
- `response_time_ms`: integer response time
- `region`: `us-east`, `us-west`, or `eu-central`

I need you to analyze this file and produce a report at `/home/user/logs/error_report.txt`. The report must have this **exact** format (no trailing spaces, no extra blank lines):

```
=== SERVICE ERROR REPORT ===

[ERROR COUNTS BY SERVICE]
<service>: <error_count> errors (<error_pct>%)
<service>: <error_count> errors (<error_pct>%)
...

[TOP ERROR CODES]
<error_code>: <count> occurrences
<error_code>: <count> occurrences
...

[RESPONSE TIME BY REGION]
<region>: avg <avg_ms>ms, max <max_ms>ms
<region>: avg <avg_ms>ms, max <max_ms>ms
...

[HOURLY ERROR RATE]
<HH>:00 - <count> errors
<HH>:00 - <count> errors
...

[CRITICAL SERVICES]
<service> - <error_code_count> unique error codes, worst code: <most_frequent_error_code>
...
```

Here are the rules for each section:

**[ERROR COUNTS BY SERVICE]**
- Count only rows where `level` is `ERROR`.
- `error_pct` is the percentage of that service's ERROR rows out of ALL rows for that service (all levels), rounded to 1 decimal place.
- Sort by `error_count` descending. If tied, sort alphabetically by service name.

**[TOP ERROR CODES]**
- Count only rows where `error_code` is NOT 0 and `level` is `ERROR`.
- List only the top 3 error codes by occurrence count.
- Sort by count descending. If tied, sort by error_code ascending (numerically).

**[RESPONSE TIME BY REGION]**
- Include ALL rows (all levels, all services) when computing averages and maximums.
- `avg_ms` is the mean response_time_ms per region, rounded to the nearest integer.
- `max_ms` is the maximum response_time_ms per region.
- Sort regions alphabetically.

**[HOURLY ERROR RATE]**
- Count rows where `level` is `ERROR`, grouped by the hour extracted from `timestamp`.
- Only include hours that have at least 1 error.
- Sort by hour ascending (00 through 23).

**[CRITICAL SERVICES]**
- Include only services that have 3 or more distinct non-zero `error_code` values among their ERROR rows.
- `error_code_count` is the count of distinct non-zero error codes for that service's ERROR rows.
- `worst code` is the single non-zero error_code that appears most frequently in that service's ERROR rows. If tied, pick the numerically largest error_code.
- Sort by `error_code_count` descending. If tied, sort alphabetically.

Please analyze the file and write the complete report.
</think>

The intermediate computations are based on the following pre-existing file.
