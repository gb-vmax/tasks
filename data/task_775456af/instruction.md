You are acting as a support engineer tasked with collecting diagnostics from a Linux system. There is a web server log file located at /home/user/logs/access.log.

Your tasks are as follows:

1. Use <b>awk</b> to extract all unique IP addresses from /home/user/logs/access.log and save them in sorted order (one IP per line, no duplicates, sorted in ascending order) to a new file: /home/user/diagnostics/unique_ips.txt.

2. Use <b>sed</b> to find and replace all occurrences of the HTTP status code "404" with "NOT_FOUND" <b>in place</b> (i.e., overwriting the existing file) within /home/user/logs/access.log.

3. Use <b>awk</b> again to generate a summary file at /home/user/diagnostics/http_status_count.txt that lists each unique HTTP status code (after the "404" replacements) found in /home/user/logs/access.log, along with their respective occurrence counts. The format must be: <status_code>: <count>, one per line, sorted numerically by status code (e.g., "200: 12", "301: 4", "NOT_FOUND: 5").

Ensure that intermediate and output files have the following line endings: UNIX style (LF).

Verify your results by checking the contents of:
- /home/user/diagnostics/unique_ips.txt (sorted, unique IPs, one per line)
- /home/user/logs/access.log (all 404s replaced in place with NOT_FOUND)
- /home/user/diagnostics/http_status_count.txt (status code/counts in required format, sorted numerically or alphabetically as appropriate)

Do not change or remove the original log structure except for the required modifications.
