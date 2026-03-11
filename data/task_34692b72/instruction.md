I'm a log analyst and I have an old Python script that was written to scan an Apache access log for suspicious repeated requests. The script is at `/home/user/analysis/scan_log.py` and it reads the log file at `/home/user/analysis/access.log`. I need your help running it and extracting a summary.

Here's what I need you to do:

1. Run the script `/home/user/analysis/scan_log.py`. It prints one line per suspicious entry to stdout, in the format:
   ```
   SUSPICIOUS <ip_address> <request_count> requests to <path>
   ```
   For example: `SUSPICIOUS 192.168.1.5 47 requests to /admin/login`

2. The script also prints some header/footer lines (lines that do NOT start with the word `SUSPICIOUS`). Ignore those.

3. From the suspicious entries only, count how many unique IP addresses appear. An IP address may appear more than once (for different paths), but count each distinct IP only once.

4. Write a summary file to `/home/user/analysis/report.txt` with **exactly** this format (no trailing spaces, no extra blank lines):
   ```
   Suspicious IPs found: <count>
   <ip1>
   <ip2>
   ...
   ```
   Where the IPs are listed one per line, sorted in ascending lexicographic order, after the first line. The first line must say `Suspicious IPs found: ` followed by the integer count.

For example, if the script output contained suspicious entries for IPs `10.0.0.5`, `10.0.0.2`, and `10.0.0.5` again (different path), the file should look like:
```
Suspicious IPs found: 2
10.0.0.2
10.0.0.5
```

Please run the existing script (do not modify it) and produce the `/home/user/analysis/report.txt` file with the correct content.
