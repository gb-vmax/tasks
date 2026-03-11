I'm a site reliability engineer and I need help processing our weekly uptime monitoring data. We have a JSON file at `/home/user/monitoring/uptime_report.json` that contains uptime check results collected over the past week. I need to analyze this data using `jq` and produce a formatted status report.

The JSON file contains a top-level object with a `"services"` key. Each service entry has:
- `"name"`: string — the service name
- `"sla_target_pct"`: number — the required uptime percentage (e.g., 99.9)
- `"checks"`: array of objects, each with:
  - `"timestamp"`: ISO 8601 string
  - `"status"`: either `"up"` or `"down"`
  - `"response_time_ms"`: integer (only meaningful when status is `"up"`)

Please process this file and write a report to `/home/user/monitoring/sla_report.txt`. Here is exactly what the report must contain:

---

```
=== SLA COMPLIANCE REPORT ===
Generated checks per service: <N>

SERVICE SUMMARY
---------------
<service_name>
  Checks: <total> | Up: <up_count> | Down: <down_count>
  Uptime: <uptime_pct>%
  SLA Target: <sla_target_pct>%
  SLA Status: BREACH
  Avg Response (up checks): <avg_ms>ms

<service_name>
  Checks: <total> | Up: <up_count> | Down: <down_count>
  Uptime: <uptime_pct>%
  SLA Target: <sla_target_pct>%
  SLA Status: OK
  Avg Response (up checks): <avg_ms>ms

...

=== BREACH SUMMARY ===
Services in breach: <N>
<service_name>: <uptime_pct>% uptime (target: <sla_target_pct>%)
...
(if no breaches, write: "No SLA breaches detected.")

=== OVERALL STATS ===
Total services: <N>
Total checks: <N>
Global uptime: <pct>%
Slowest avg response: <service_name> (<avg_ms>ms)
```

---

Formatting rules:
- Services in the SERVICE SUMMARY section must appear in **alphabetical order by service name**.
- `<uptime_pct>` is `(up_count / total_checks) * 100`, rounded to **2 decimal places** (e.g., `98.33`).
- `SLA Status` is `BREACH` if uptime_pct is strictly less than sla_target_pct, otherwise `OK`.
- `<avg_ms>` is the average of `response_time_ms` across all checks where status is `"up"`, rounded to the **nearest integer**.
- In the BREACH SUMMARY, list breaching services in alphabetical order.
- `Global uptime` is (total up checks across all services / total checks across all services) * 100, rounded to **2 decimal places**.
- `Slowest avg response` is the service with the highest average response time (same avg_ms computation as above, rounded to nearest integer). If there's a tie, pick alphabetically first.
- `Generated checks per service: <N>` — this is the number of checks in the first service's `checks` array (they are all equal).
- There is a blank line between each service block in SERVICE SUMMARY.
- The breach list entries in BREACH SUMMARY use format: `<service_name>: <uptime_pct>% uptime (target: <sla_target_pct>%)`

You may use `jq`, `awk`, `bc`, `python3`, or any combination of standard Linux tools to compute and assemble this report.
