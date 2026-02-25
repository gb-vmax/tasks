You are simulating the initial reporting phase of a penetration test. You are given a file at /home/user/targets.txt, which contains a list of target hostnames or IP addresses, one per line, as follows:

```
web1.corp.local
192.168.10.5
dbserver.corp.local
router01
```

Your objective is to process this file and prepare a summarized vulnerability scan report.

1. For each target in the file, you must simulate a basic nmap scan by creating an entry in a new file called /home/user/vulnscan_results.txt. Each entry must have the following format (replace TARGET with the actual hostname or IP):

```
[SCAN] TARGET
Ports:
80/tcp open
443/tcp closed
22/tcp open
Vulnerabilities:
CVE-2021-1234: LOW
CVE-2019-8903: HIGH
---
```
(Each target must have a separate entry, separated by the "---" line.)

2. After generating /home/user/vulnscan_results.txt, process it to create a summary report at /home/user/report_summary.log with the following requirements:
  - Show the count of targets scanned.
  - Show the number of open ports found across all targets (i.e., count of unique "PORT/tcp open" lines).
  - For each vulnerability (e.g., CVE-2021-1234), indicate across all targets how many times it was detected, grouped by severity ("LOW", "HIGH").

The format of /home/user/report_summary.log must be exactly as follows (replace X, Y, etc.):

```
Targets scanned: X
Open ports found: Y
Vulnerability counts:
CVE-2021-1234 (LOW): Z times
CVE-2019-8903 (HIGH): W times
```

Verify your outputs match the specified formats and filenames. Create all files and directories as needed with default user permissions.
