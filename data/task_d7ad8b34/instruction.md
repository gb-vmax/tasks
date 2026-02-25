You are a support engineer tasked with collecting diagnostic information from an application log file for troubleshooting purposes. The log file is located at <code>/home/user/appdata/app.log</code>. Your goal is to extract only the <b>ERROR</b> and <b>WARN</b> level log entries for the week starting from <b>2024-06-10</b> (inclusive) to <b>2024-06-16</b> (inclusive) and save these to a new file.

Log entries in <code>app.log</code> are formatted as follows (one entry per line):

<pre>
YYYY-MM-DD HH:MM:SS [LEVEL] Message text...
</pre>

Example:
<pre>
2024-06-12 09:08:16 [INFO] Application started successfully.
2024-06-12 09:25:33 [ERROR] Connection failed: timeout.
2024-06-14 18:22:01 [WARN] Disk space low.
</pre>

To accomplish this task:

1. Use suitable regular expressions to locate all lines in <code>/home/user/appdata/app.log</code> that meet <b>all</b> these criteria:
   <ul>
      <li>Date is between <code>2024-06-10</code> and <code>2024-06-16</code> (inclusive).</li>
      <li>Log level is <code>[ERROR]</code> or <code>[WARN]</code>.</li>
   </ul>
2. Write the matching log entries, in the <b>original order</b> from the source log, to a new file at <code>/home/user/diagnostics/filtered_errors_warnings.log</code>.

The format of <code>filtered_errors_warnings.log</code> should be:

<pre>
YYYY-MM-DD HH:MM:SS [LEVEL] Message text...
YYYY-MM-DD HH:MM:SS [LEVEL] Message text...
...
</pre>

No extra header, footer, or blank lines. Only the original log lines that match the filter criteria should appear.

After completing the task, verify the contents of <code>/home/user/diagnostics/filtered_errors_warnings.log</code> by outputting its contents to the terminal.

You have write access to both <code>/home/user/appdata/</code> and <code>/home/user/diagnostics/</code>.
