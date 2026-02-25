You are investigating issues reported by users about failed authentication attempts on a web service. There is an application log located at /home/user/server/app.log. 

Filter this log to extract only the lines that include the phrases "authentication failed" or "invalid password" (case-insensitive match for both phrases). Create a new filtered log at /home/user/server/auth_failure.log containing these lines in the exact order found in the original log.

Each matching log entry must be copied verbatim to the corresponding output file, preserving all whitespace and formatting. 

Create a summary file named /home/user/server/auth_summary.txt that contains a single line: "Total failures: X", where X is the number of lines in auth_failure.log. This line must be the only content in auth_summary.txt.

To verify your solution, the test will check:
- Only the matching lines (case-insensitive) are present in /home/user/server/auth_failure.log, in the correct order.
- The total in /home/user/server/auth_summary.txt matches the exact count of those lines in the log.
