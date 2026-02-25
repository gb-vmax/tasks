You are an incident responder. You have been provided with an Apache access log located at /home/user/investigation/access.log. Identify all unique IP addresses that have accessed the server and count how many times each IP has appeared in the log. 

Produce a report at /home/user/investigation/ip_report.txt in the following format: each line should contain an IP address, followed by a space, and then the number of times it appears in the log. The lines should be sorted in descending order of the count (highest count first). If two IPs have the same count, order them lexicographically in ascending order by IP address.

Example report:
```
192.168.1.101 8
203.0.113.4 4
203.0.113.42 4
10.0.0.1 2
```

Only include valid IPv4 addresses (exclude any malformed or blank entries). Use awk and sed exclusively to process the file. Please save your results in /home/user/investigation/ip_report.txt.
