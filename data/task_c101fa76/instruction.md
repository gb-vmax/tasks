I'm a technical writer putting together a system health summary document for our ops team. I have some raw monitoring data on my machine that I need to process into a clean, formatted report. Can you help me parse and organize this data?

Here's what I have and what I need:

**Input files:**

1. `/home/user/monitoring/cpu_mem.csv` — A CSV file with per-minute snapshots of CPU and memory usage. Columns: `timestamp,cpu_percent,mem_used_mb,mem_total_mb`. The timestamp format is `YYYY-MM-DD HH:MM`.

2. `/home/user/monitoring/disk_usage.txt` — A plain-text file where each line has the format: `<mount_point> <used_gb> <total_gb>`. Fields are separated by a single space.

3. `/home/user/monitoring/processes.log` — A log file where each line records a process snapshot in this format:
   `[YYYY-MM-DD HH:MM] <process_name> <pid> <state> <cpu_pct>`
   - `<state>` is one of: `running`, `sleeping`, `zombie`
   - `<cpu_pct>` is a float

**What I need you to produce:**

Please generate a report at `/home/user/monitoring/system_health_report.txt`.

The report must have this exact format (replace placeholders with computed values):

```
=== SYSTEM HEALTH REPORT ===

-- CPU & MEMORY --
Samples: <total number of rows in cpu_mem.csv, excluding header>
CPU avg: <average cpu_percent across all samples, rounded to 1 decimal place>%
CPU max: <maximum cpu_percent across all samples, rounded to 1 decimal place>%
Memory avg usage: <average of (mem_used_mb/mem_total_mb*100) across all samples, rounded to 1 decimal place>%
Memory peak usage: <maximum of (mem_used_mb/mem_total_mb*100) across all samples, rounded to 1 decimal place>%

-- DISK USAGE --
<mount_point>: <used_gb>GB / <total_gb>GB (<percent>%)
<mount_point>: <used_gb>GB / <total_gb>GB (<percent>%)
...
(one line per mount point, sorted alphabetically by mount_point)
(percent = round(used_gb/total_gb*100, 1))

-- PROCESS SUMMARY --
Total snapshots: <total number of lines in processes.log>
Unique processes: <count of distinct process_name values>
Zombie processes: <count of lines where state == "zombie">
Top CPU process: <process_name with the highest single cpu_pct value> (<that cpu_pct value, rounded to 1 decimal>%)

-- ALERTS --
<list of alert lines, one per qualifying condition, in the order specified below>
(if no alerts, write a single line: "No alerts.")
```

**Alert rules** (check in this order, include a line for each that triggers):
1. If CPU avg exceeds 75.0%, add line: `WARN: High average CPU usage (<value>%)`
2. If CPU max exceeds 90.0%, add line: `WARN: CPU spike detected (<value>%)`
3. If any disk mount point has usage percentage >= 80.0%, add one line per such mount (sorted alphabetically by mount point): `WARN: Disk <mount_point> at <percent>% capacity`
4. If zombie process count > 0, add line: `WARN: <count> zombie process(es) detected`

For all alert values, use the same rounded-to-1-decimal values as computed in the sections above.

The output file must have a single trailing newline after the last line. There should be no trailing spaces on any line.
