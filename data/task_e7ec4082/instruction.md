I'm a log analyst investigating traffic patterns in our web server logs. I have an Apache Combined Log Format access log at `/home/user/logs/access.log`. I need you to process it and produce a formatted report using awk and sed (or similar standard Unix text processing tools).

The log file uses standard Apache Combined Log Format where each line looks like:
```
<IP> - - [<timestamp>] "<METHOD> <path> <protocol>" <status> <bytes> "<referrer>" "<user-agent>"
```

**Your goal is to produce a report file at `/home/user/reports/traffic_report.txt`.**

Here is the exact format the report must follow (including blank lines and spacing):

```
=== TRAFFIC REPORT ===

--- Top 5 IPs by Request Count ---
<count> <ip>
<count> <ip>
<count> <ip>
<count> <ip>
<count> <ip>

--- Status Code Summary ---
<status>: <count> requests
<status>: <count> requests
...

--- Total Bytes Transferred by Method ---
<METHOD>: <total_bytes> bytes
<METHOD>: <total_bytes> bytes
...

--- Suspicious IPs (error rate > 50%) ---
<ip> errors=<error_count> total=<total_count>
<ip> errors=<error_count> total=<total_count>
...
```

Specific rules:

1. **Top 5 IPs by Request Count**: Count how many requests each IP address made. Print the top 5, sorted by count descending. Each line is `<count><TAB><ip>` (count and IP separated by a single tab character). If there is a tie in count, sort those tied IPs alphabetically (ascending) by IP address string.

2. **Status Code Summary**: For each HTTP status code that appears in the log, print `<status>: <count> requests`. Sort status codes numerically ascending. Include all status codes present in the log.

3. **Total Bytes Transferred by Method**: Sum the `bytes` field for each HTTP method (GET, POST, HEAD, etc.). Print `<METHOD>: <total_bytes> bytes`. Sort methods alphabetically ascending. Treat `-` in the bytes field as 0.

4. **Suspicious IPs (error rate > 50%)**: An IP is "suspicious" if more than 50% of its requests resulted in a 4xx or 5xx status code. For each such IP, print `<ip> errors=<error_count> total=<total_count>`. Only include IPs that made at least 3 requests total (to avoid noise from single-request errors). Sort suspicious IPs by error count descending; break ties alphabetically by IP ascending.

5. If there are no suspicious IPs, print `None` on a single line under that section header.

Make sure the `reports` directory exists before writing the file. The report must end with a trailing newline.

Here is an example of how the "Top 5 IPs" section should look (with fake data, not the real answer):
```
--- Top 5 IPs by Request Count ---
12	203.0.113.5
9	198.51.100.2
7	192.168.1.1
6	10.0.0.3
5	172.16.0.4
```

Note the single tab character between the count and the IP. All other separators in the report are plain spaces as shown in the format templates above.
