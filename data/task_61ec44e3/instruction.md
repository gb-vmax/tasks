I'm a monitoring specialist and I have an old alert-checking script at `/home/user/monitoring/check_alerts.sh` that I need to run against a CPU usage log file. The script and log file are already set up — I just need to make the script executable and run it.

The log file is at `/home/user/monitoring/cpu_usage.log`. Each line has this format:
```
<hostname> <timestamp> <cpu_percent>
```
For example:
```
webserver01 2024-03-15T08:00:00 45.2
```

The script `check_alerts.sh` reads `cpu_usage.log` from the same directory as the script, checks each entry, and prints an alert line for any entry where the CPU percentage is **above 80.0**. Each alert line must look exactly like:
```
ALERT: <hostname> exceeded threshold at <timestamp> (CPU: <cpu_percent>%)
```

The script currently exists but is not executable. Please make it executable and run it, saving the output to `/home/user/monitoring/alerts_output.txt`.
