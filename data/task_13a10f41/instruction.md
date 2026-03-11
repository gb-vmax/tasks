I'm a DevSecOps engineer and I need your help analyzing an audit log to enforce our "blocked source IP" policy. We've collected a raw firewall deny log at `/home/user/security/firewall_deny.log`. Each line in this file has the following space-separated format:

```
<timestamp> <action> <protocol> <source_ip> <dest_port>
```

For example:
```
2024-06-01T08:12:34 DENY TCP 192.168.1.50 443
```

I need you to produce a report at `/home/user/security/top_offenders.txt` that lists every source IP that appears in the log, along with how many times it was denied, sorted from **most frequent to least frequent**. If two IPs have the same count, sort them **numerically by IP address** (ascending).

The output file must have **exactly** this format — one line per IP, with the count and IP separated by a single space:

```
<count> <ip_address>
<count> <ip_address>
...
```

No header line, no trailing whitespace, no blank lines. Just the raw count-and-IP pairs, one per line.

After generating `top_offenders.txt`, also append a summary line to the **end** of that same file in this exact format:

```
TOTAL_DENIES: <total_number_of_log_entries>
```

Where `<total_number_of_log_entries>` is the total number of lines in the original log file (which equals the total number of deny events).

Please generate this report for me.
