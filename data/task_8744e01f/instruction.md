I'm a capacity planner and I need your help analyzing resource usage data from our servers. I have three raw metric files in `/home/user/metrics/` that were dumped from our monitoring system. They're messy and need to be cleaned up and summarized into a final capacity report. Can you process all three files, extract the stats I need, and combine everything into one report?

Here are the three files and what I need from each:

---

### File 1: `/home/user/metrics/cpu_usage.log`

This file has lines in the format `<hostname> <timestamp> <cpu_percent>`. Some lines are malformed (missing fields or non-numeric CPU values — lines where the third field is not a valid number). I need you to:

- **Ignore any malformed lines** (where the third field is missing or not a number).
- Compute the **average CPU usage** across all valid lines, rounded to 1 decimal place.
- Find the **maximum CPU usage** value (no rounding needed, just the numeric value as it appears).
- Find the **hostname with the highest average CPU usage** across all its valid readings. If there's a tie, choose the one that comes first alphabetically.

---

### File 2: `/home/user/metrics/memory_usage.log`

This file has lines in the format `<hostname> <used_mb> <total_mb>`. Some lines have a leading `#` character (comments) that must be skipped. I need you to:

- **Skip comment lines** (lines starting with `#`) and blank lines.
- Compute the **overall memory utilization percentage** as `(sum of all used_mb) / (sum of all total_mb) * 100`, rounded to 1 decimal place.
- Find the **hostname with the highest memory utilization** (used_mb/total_mb), expressed as a percentage rounded to 1 decimal place.
- Report the **total used memory** (sum of all used_mb) as an integer.

---

### File 3: `/home/user/metrics/disk_usage.log`

This file has lines in the format `<mount_point> <used_gb> <capacity_gb>` but mount point names may contain spaces (they are always in the first column and the last two columns are always numbers). Actually, to make this unambiguous, each line is space-delimited but the last two fields are always the numeric ones, and the mount point is everything before those last two fields. Some lines have the used_gb greater than capacity_gb — these are **corrupt entries and should be skipped**. I need you to:

- **Skip corrupt lines** where used_gb > capacity_gb.
- Find the **mount point with the highest usage percentage** (used_gb/capacity_gb * 100), along with that percentage rounded to 1 decimal place.
- Compute the **total capacity** (sum of all valid capacity_gb) as an integer.
- Compute the **overall disk utilization** as `(sum of valid used_gb) / (sum of valid capacity_gb) * 100`, rounded to 1 decimal place.

---

### Final Report

Please write all results to `/home/user/metrics/capacity_report.txt` in this **exact** format (replace the angle-bracket placeholders with actual values):

```
=== CAPACITY PLANNING REPORT ===

[CPU]
Average Usage: <value>%
Peak Usage: <value>%
Busiest Host: <hostname>

[MEMORY]
Overall Utilization: <value>%
Total Used: <value> MB
Most Loaded Host: <hostname> (<value>%)

[DISK]
Overall Utilization: <value>%
Total Capacity: <value> GB
Fullest Mount: <mount_point> (<value>%)

[SUMMARY]
CPU Status: <OK or WARN>
Memory Status: <OK or WARN>
Disk Status: <OK or WARN>
```

For the `[SUMMARY]` section:
- CPU Status is `WARN` if average CPU usage is above 75%, otherwise `OK`.
- Memory Status is `WARN` if overall memory utilization is above 80%, otherwise `OK`.
- Disk Status is `WARN` if overall disk utilization is above 70%, otherwise `OK`.

There should be no trailing spaces on any line. The blank lines between sections must be present exactly as shown.
