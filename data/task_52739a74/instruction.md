Hey, I need your help analyzing some API diagnostic data I collected during a load test. I've got several files in `/home/user/api_diagnostics/` that capture different aspects of system behavior during the test window, and I need to combine them into a single report.

Here's what's in the directory:

- `/home/user/api_diagnostics/auth_events.log` — log of authentication events, one per line
- `/home/user/api_diagnostics/latency_samples.csv` — CSV of per-request latency measurements
- `/home/user/api_diagnostics/error_counts.tsv` — tab-separated error counts per endpoint per minute
- `/home/user/api_diagnostics/system_metrics.log` — CPU and memory snapshots during the test

I need you to analyze all four files independently and then combine the results into a single report at `/home/user/api_diagnostics/diagnostic_report.txt`.

---

**From `auth_events.log`:**

Each line has the format: `[TIMESTAMP] [LEVEL] [EVENT_TYPE] user=<username> result=<OK|FAIL>`

Count the following:
- Total authentication events
- Total successful auths (`result=OK`)
- Total failed auths (`result=FAIL`)
- The username with the most FAIL events (and how many they had)

---

**From `latency_samples.csv`:**

The CSV has a header row, then rows with columns: `request_id,endpoint,latency_ms,status_code`

Compute:
- The overall minimum, maximum, and mean latency across all rows (mean rounded to 1 decimal place)
- The endpoint with the highest mean latency (average across all its rows, rounded to 1 decimal place)
- The count of requests with `status_code` of 200

---

**From `error_counts.tsv`:**

Each row (no header): `<minute_timestamp>\t<endpoint>\t<error_count>`

Compute:
- Total error count across all rows
- The endpoint that accumulated the most errors in total (sum across all minutes)
- The minute timestamp with the highest single error_count value (if tie, pick the earliest lexicographically)

---

**From `system_metrics.log`:**

Each line has the format: `TIMESTAMP cpu_pct=<float> mem_pct=<float>`

Compute:
- Peak CPU percentage (highest value seen)
- Peak memory percentage (highest value seen)
- Number of samples where cpu_pct exceeded 80.0

---

**Output format:**

Write the results to `/home/user/api_diagnostics/diagnostic_report.txt` with EXACTLY this format (replace angle-bracket placeholders with computed values):

```
=== API DIAGNOSTIC REPORT ===

--- AUTH EVENTS ---
Total events: <N>
Successful: <N>
Failed: <N>
Top failing user: <username> (<N> failures)

--- LATENCY (ms) ---
Min: <N>
Max: <N>
Mean: <N.N>
Slowest endpoint: <endpoint> (avg <N.N>ms)
HTTP 200 count: <N>

--- ERROR COUNTS ---
Total errors: <N>
Most errors endpoint: <endpoint> (<N> errors)
Worst minute: <timestamp> (<N> errors)

--- SYSTEM METRICS ---
Peak CPU: <N.N>%
Peak Memory: <N.N>%
High CPU samples (>80%): <N>
```

Use exactly one space after the colon on each line. No trailing spaces. Preserve the section headers and separator lines exactly as shown.
