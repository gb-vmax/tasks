As a security auditor, you have been asked to review the permissions changes recorded in a sample system log file. There is a log file located at <code>/home/user/logs/auth_sample.log</code>. 

Your task is to filter this log for any lines that indicate a file or directory permission (mode) change, specifically those using the <code>chmod</code> or <code>chown</code> commands. 

Please extract and save <b>only</b> those lines containing either "<code>chmod</code>" or "<code>chown</code>" (case-sensitive, full word) in them. Save the filtered results into a new file named <code>/home/user/logs/perm_audit.log</code>.

The output format in <code>perm_audit.log</code> should be exactly the matching lines taken from <code>/home/user/logs/auth_sample.log</code> — one per line, preserving the original order and spacing.

At the end, you should have the <code>perm_audit.log</code> file containing only all lines from <code>auth_sample.log</code> that include "<code>chmod</code>" or "<code>chown</code>".
