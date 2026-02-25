You are a container specialist managing microservices logs. In the directory <code>/home/user/microservices/logs/</code>, there is a log file named <code>service-api.log</code>. Your task is to analyze this log file and create a new summary file named <code>/home/user/microservices/logs/error_summary.txt</code>. 

Your summary file must meet these requirements:
- It should contain only the error lines (lines containing the keyword <code>ERROR</code> as a whole word, case-sensitive).
- Each matching line should be written as-is, in the original order.
- After listing all error lines, add a line at the end of the file in this format: <code>Total ERROR lines: X</code> where <code>X</code> is the total count of error lines found.

This will help us quickly identify and count critical issues. 

Example expected content (for illustration only, do not use this literally):
<pre>
2024-05-01 12:02:34 ERROR Failed to connect to database
2024-05-01 12:10:17 ERROR Timeout in payment service
Total ERROR lines: 2
</pre>
Make sure to keep the format exactly as described. When ready, check that <code>/home/user/microservices/logs/error_summary.txt</code> exists and matches the expected format.
