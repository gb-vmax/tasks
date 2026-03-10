I'm an operations engineer triaging a production incident and I need your help analyzing a server log file. The log is located at `/home/user/logs/production.log`. Each line follows this format:

```
[TIMESTAMP] [SEVERITY] [SERVICE] MESSAGE
```

Where:
- `TIMESTAMP` is in the format `2024-05-21T14:32:01`
- `SEVERITY` is one of: `INFO`, `WARN`, `ERROR`, `FATAL`
- `SERVICE` is one of: `auth-service`, `payment-service`, `api-gateway`, `db-connector`
- `MESSAGE` is free text that may contain error codes like `ERR-1042`, `ERR-2201`, etc.

I need you to produce a triage report at `/home/user/logs/triage_report.txt`. Here's exactly what the report must contain, in this precise order and format:

---

**Section 1 — Incident Window**

Scan the log for all lines with severity `ERROR` or `FATAL`. Find the earliest and latest timestamps among those lines. Write these two lines:

```
=== INCIDENT TRIAGE REPORT ===
Incident window: <earliest_timestamp> to <latest_timestamp>
```

**Section 2 — Severity Counts**

Count every log line by severity (across ALL lines, not just errors). Write a blank line, then:

```
--- Severity Breakdown ---
FATAL: <count>
ERROR: <count>
WARN: <count>
INFO: <count>
```

Always print all four severities in that order (FATAL, ERROR, WARN, INFO), even if the count is 0.

**Section 3 — Affected Services**

Among only `ERROR` and `FATAL` lines, count how many such lines each service produced. Write a blank line, then:

```
--- Affected Services (ERROR/FATAL only) ---
<service>: <count>
<service>: <count>
...
```

List only services that appear at least once in ERROR/FATAL lines. Sort by count descending. If two services have the same count, sort them alphabetically.

**Section 4 — Error Code Frequency**

Scan ALL log lines for error codes matching the pattern `ERR-\d+`. A single log line may contain at most one error code. Count how many times each distinct error code appears across all lines. Write a blank line, then:

```
--- Error Code Frequency ---
<code>: <count>
<code>: <count>
...
```

Sort by count descending. If two codes have the same count, sort numerically by the numeric portion of the code (e.g., `ERR-404` before `ERR-1042`).

**Section 5 — Critical Service Flag**

Check whether `payment-service` produced any `FATAL` lines. Write a blank line, then:

- If yes: `*** CRITICAL: payment-service has FATAL errors — escalate immediately ***`
- If no: `payment-service: no FATAL errors detected`

---

The final file `/home/user/logs/triage_report.txt` must contain exactly those five sections with no trailing spaces on any line and a single newline at the very end of the file.
