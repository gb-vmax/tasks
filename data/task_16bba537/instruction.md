I'm a network engineer investigating repeated connection failures on our gateway. I have a firewall deny log at `/home/user/logs/fw_deny.log` where each line represents a blocked connection attempt and looks like this:

```
2024-11-01T08:12:03 DENY src=192.168.1.45 dst=10.0.0.1 port=443 proto=TCP
```

I need to figure out which source IP addresses are responsible for the most blocked traffic. Can you help me analyze this log and produce a report showing how many times each source IP was denied?

Please extract the source IP from each log line (the value after `src=`), count how many times each IP appears, and write the results to `/home/user/logs/deny_count.txt`.

The output file must have one line per source IP in this exact format:

```
<count> <ip_address>
```

The lines must be sorted by count in **descending** order (highest count first). If two IPs have the same count, sort them in **reverse alphabetical** order (i.e., descending lexicographic order by IP string). There should be no leading spaces on any line and no blank lines in the file.

For example, if IP `10.4.1.2` was blocked 15 times and `172.16.0.8` was blocked 9 times, the file should look like:

```
15 10.4.1.2
9 172.16.0.8
```
