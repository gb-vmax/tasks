Hi, I'm a compliance analyst and I need your help generating a clean audit trail report from our raw system access logs. We have a CSV file at `/home/user/audit/access_log.csv` that captures all login events for the quarter.

The CSV file has these columns (with a header row):
```
timestamp,username,action,source_ip,status
```

I need you to produce a filtered audit trail at `/home/user/audit/trail_report.txt` that meets the following requirements:

**Filtering:** Only include rows where the `status` is `FAILURE`. Ignore all `SUCCESS` rows.

**Sorting:** The output entries must be sorted by `username` alphabetically (A–Z). If two entries share the same username, sort them by `timestamp` chronologically (ascending).

**Output format:** The file must start with a header line, followed by one line per matching record, and end with a summary line. Use this exact format:

```
AUDIT TRAIL - FAILED LOGIN ATTEMPTS
------------------------------------
[<timestamp>] <username> @ <source_ip>
[<timestamp>] <username> @ <source_ip>
...
------------------------------------
Total failed attempts: <N>
```

Rules:
- The separator line is exactly 36 hyphens (`-`), appearing both after the header and before the summary.
- The timestamp in each entry must be reformatted from the original `YYYY-MM-DD HH:MM:SS` format to `DD/MM/YYYY HH:MM`.  Note that seconds are dropped.
- There is no blank line between the last entry and the second separator line.
- `<N>` is the total count of `FAILURE` rows included in the report.

The file `/home/user/audit/access_log.csv` already exists with the raw data. Please generate the report at `/home/user/audit/trail_report.txt`.
