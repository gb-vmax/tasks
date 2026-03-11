I'm a capacity planner and I need your help running an existing resource usage analysis script and capturing its output in a specific format.

There's a Python script at `/home/user/capacity/analyze_usage.py` that reads a CSV file of server resource snapshots and prints usage statistics to stdout. The CSV file is at `/home/user/capacity/server_metrics.csv`.

Run the script like this:

```
python3 /home/user/capacity/analyze_usage.py /home/user/capacity/server_metrics.csv
```

The script will print several lines to stdout. I need you to capture only specific parts of that output and write a clean summary report to `/home/user/capacity/report.txt`.

The report must have this exact format — no extra blank lines, no extra spaces, every line exactly as shown:

```
=== Capacity Report ===
Hosts analyzed: <N>
CPU avg: <value>%
MEM avg: <value>%
DISK avg: <value>%
High CPU hosts (>80%): <comma-separated hostnames, sorted alphabetically, or "none">
High MEM hosts (>80%): <comma-separated hostnames, sorted alphabetically, or "none">
```

Where:
- `<N>` is the integer number of unique hosts in the dataset
- `<value>` for CPU, MEM, and DISK averages are the values printed by the script, rounded to one decimal place
- "High CPU hosts" and "High MEM hosts" are the hostnames the script prints, sorted alphabetically and joined with ", " (comma space). If the script prints "none" for that category, write "none".

The script prints its output in a human-readable block — you'll need to parse specific lines from it to extract the numbers and hostnames, then write the report in the exact format above.

Please produce the file `/home/user/capacity/report.txt` with the correct content.
