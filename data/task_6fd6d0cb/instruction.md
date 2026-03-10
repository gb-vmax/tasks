I'm a deployment engineer who just ran a batch of rolling updates across multiple services, and I need to generate a post-deployment health report from the deployment logs before the team stand-up. The raw log file is at `/home/user/deploys/deployment.log`.

Each line in the log file has this format:
```
[TIMESTAMP] SERVICE=<name> VERSION=<ver> STATUS=<DEPLOYED|FAILED|ROLLED_BACK> DURATION=<seconds>s REGION=<region>
```

For example:
```
[2024-06-10T08:15:30Z] SERVICE=auth-service VERSION=2.4.1 STATUS=DEPLOYED DURATION=42s REGION=us-east
```

I need you to analyze this log and produce a report at `/home/user/deploys/deploy_report.txt`. Here's the exact format the report must follow:

```
=== DEPLOYMENT HEALTH REPORT ===
Generated: 2024-06-10

Total deployments: <N>
Successful: <N>
Failed/Rolled back: <N>
Overall success rate: <percentage>%

=== PER-SERVICE SUMMARY ===
<service_name>: <success_count>/<total_count> succeeded, avg duration <avg_seconds>s
<service_name>: <success_count>/<total_count> succeeded, avg duration <avg_seconds>s
...

=== REGIONAL BREAKDOWN ===
<region>: <success_count>/<total_count> deployments succeeded
<region>: <success_count>/<total_count> deployments succeeded
...

=== ALERTS ===
DEGRADED SERVICES (success rate < 100%):
  <service_name>: <success_rate>% success rate
  ...
SLOWEST DEPLOYMENT: <service_name> v<version> in <region> took <duration>s
FASTEST DEPLOYMENT: <service_name> v<version> in <region> took <duration>s
```

Important formatting rules:
- The date on the "Generated:" line must be `2024-06-10` exactly (hardcoded from the log data, not today's date).
- "Failed/Rolled back" counts both `FAILED` and `ROLLED_BACK` statuses together.
- "Overall success rate" is calculated as `(Successful / Total) * 100`, rounded to one decimal place (e.g., `83.3%`).
- In the "PER-SERVICE SUMMARY" section, services must be listed in **alphabetical order**. The `avg duration` must be rounded to the nearest integer.
- In the "REGIONAL BREAKDOWN" section, regions must be listed in **alphabetical order**.
- In the "ALERTS" section, "DEGRADED SERVICES" are any services where at least one deployment did NOT have `STATUS=DEPLOYED`. List them alphabetically by service name. The success rate shown is `(service_successful / service_total) * 100`, rounded to one decimal place.
- For "SLOWEST DEPLOYMENT" and "FASTEST DEPLOYMENT", in case of a tie on duration, pick the one that appears **last** in the log file.
- If there are no degraded services, write `  (none)` under that heading.
- DEPLOYED counts as successful. FAILED and ROLLED_BACK both count as not successful.

Please analyze `/home/user/deploys/deployment.log` and create the report at `/home/user/deploys/deploy_report.txt`.
