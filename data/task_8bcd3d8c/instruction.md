An application error log file exists at <code>/home/user/app_error.log</code>. Each line in the file represents a log event and is formatted as follows:

<pre>
[YYYY-MM-DD HH:MM:SS] LEVEL: message
</pre>

Example lines:
<pre>
[2024-06-11 10:45:23] ERROR: Failed to connect to database
[2024-06-11 10:45:24] WARN: Retrying connection
[2024-06-11 10:45:25] INFO: Connection re-established
</pre>

You are triaging a recent incident and have been asked to extract **only the timestamp and message text of lines where the log level is ERROR** to a new file at <code>/home/user/errors_extracted.log</code>.

**Required output format of each line in /home/user/errors_extracted.log:**

<pre>
YYYY-MM-DD HH:MM:SS | message
</pre>

For the above example, /home/user/errors_extracted.log would contain:
<pre>
2024-06-11 10:45:23 | Failed to connect to database
</pre>

**Perform this task by processing /home/user/app_error.log and outputting the result as described, preserving the order of ERROR log entries.** Use <code>awk</code> and/or <code>sed</code> as needed.
