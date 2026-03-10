Hey, I need your help analyzing a deployment log from our latest rollout. We pushed updates to several microservices earlier today and I want to understand what happened — which services succeeded, which failed, and how long each deployment took.

The deployment log is at `/home/user/deployments/rollout_2024.log`. Each line has this format:

```
[TIMESTAMP] [LEVEL] SERVICE=<name> ACTION=<START|END> STATUS=<running|success|failed> DURATION_MS=<integer|->
```

Where:
- `TIMESTAMP` is in the format `2024-04-10T<HH:MM:SS>Z`
- `LEVEL` is one of `INFO` or `ERROR`
- `SERVICE` is the service name (e.g., `auth-service`)
- `ACTION` is either `START` (deployment beginning) or `END` (deployment finished)
- `STATUS` is `running` for START lines, `success` or `failed` for END lines
- `DURATION_MS` is `-` for START lines and an integer (milliseconds) for END lines

I need you to generate a deployment summary report at `/home/user/deployments/rollout_report.txt`. Here's exactly what the report must look like:

```
=== DEPLOYMENT ROLLOUT REPORT ===
Log file: /home/user/deployments/rollout_2024.log
Total services deployed: <N>
Successful: <N>
Failed: <N>

=== SERVICE DETAILS ===
<service-name> [SUCCESS] <duration_ms>ms
<service-name> [FAILED] <duration_ms>ms
...

=== TIMING STATISTICS ===
Fastest deployment: <service-name> (<duration_ms>ms)
Slowest deployment: <service-name> (<duration_ms>ms)
Average deployment time: <integer>ms

=== FAILED SERVICES ===
<service-name>
...
```

Formatting rules:
- In the "SERVICE DETAILS" section, list all services sorted alphabetically by service name. Each line shows the service name, its outcome in brackets (`[SUCCESS]` or `[FAILED]`), and its duration from the END line.
- "Total services deployed" is the count of unique service names that have an END line.
- In "TIMING STATISTICS", fastest and slowest are determined by the `DURATION_MS` value from END lines.
- "Average deployment time" is the mean of all END-line `DURATION_MS` values, rounded to the nearest integer.
- In "FAILED SERVICES", list only services whose END status is `failed`, one per line, sorted alphabetically. If no services failed, write `None`.
- There is exactly one blank line between each section (i.e., one blank line after the header block, one blank line after SERVICE DETAILS, one blank line after TIMING STATISTICS).
- The file must end with a newline after the last failed service (or after "None").

Please generate this report from the log file.
