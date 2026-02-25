You are a DevOps engineer who needs to debug issues from a complex application’s logs. These logs are stored at /home/user/logs/app.log. First, inspect the log file and filter all lines that match either of the following criteria using regular expressions:

1. Any line that starts with the word "ERROR" (case sensitive).
2. Any line that contains an IPv4 address anywhere in the line.

From these filtered lines, perform the following in parallel:

- Save all "ERROR" lines (from criterion 1) to a new file named /home/user/logs/error_lines.log.
- Save all lines that contain an IPv4 address (from criterion 2) to another file named /home/user/logs/ip_lines.log.

Additionally, count the number of lines output to each file and write a summary log at /home/user/logs/regex_summary.log with the following exact format:

error_lines.log: X lines
ip_lines.log: Y lines

Where X is replaced by the count of lines in error_lines.log and Y is replaced by the count from ip_lines.log.

Summary:

- Use only regex-based filters for the log extraction.
- Ensure parallel execution or at least one-liners for each filter.
- The summary log format and file naming must exactly match the description for verification.
