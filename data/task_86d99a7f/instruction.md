You are a security engineer performing a periodic credential rotation. A sensitive application has generated an access log, <code>/home/user/security/access.log</code>, that contains multiple entries related to authentication.

Your tasks are as follows:

1. **Search and Extract Old Credentials Use**: Using a regular expression, filter all log entries where the username field is either exactly <code>alice</code> or <code>bob</code>, and where the <code>action</code> field is either <code>login</code>, <code>failed</code>, or <code>token_refresh</code>. The format for each line in the log is:

    <pre>
    DATE TIME - user:USERNAME - action:ACTION - status:STATUS - ip:IP_ADDRESS
    </pre>

    For example:

    <pre>
    2024-06-05 12:21:11 - user:alice - action:login - status:success - ip:192.168.1.15
    </pre>

2. **Write the filtered results to a new file**: Save all matching entries to the file <code>/home/user/security/old-credentials.log</code>. The output format should be **identical** to the original: one entry per line, exactly as in the original log, with no additional content.

3. **Count and Summarize**: Count the number of matching entries and write a summary file <code>/home/user/security/old-credentials-summary.txt</code> with the following _precise_ content on one line:

    <pre>
    Old credential entries: N
    </pre>

    where <code>N</code> is the total number of lines in <code>old-credentials.log</code>.

Please ensure that there are no extra spaces or blank lines in your outputs. Both result files must exist and match the specified formats exactly.
