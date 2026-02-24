As a storage administrator, you are responsible for maintaining both disk space utilization and security on the server. I want you to simulate a security audit of directories containing large files. Here is what you should do:

1. In the directory <code>/home/user/storage_audit/</code>, locate all files larger than 10MB within any subdirectories and output a list of these files.
2. For each of these large files, conduct a simple scan for potential security risks by checking for the presence of the word <code>password</code> (case-insensitive) anywhere in the file contents.
3. Create a log file at <code>/home/user/storage_audit/security_scan.log</code>. For each large file found above, append a record to this log in the following precise format (one per line):

<pre>
[filename]: [status] [details]
</pre>

Where:
- <code>[filename]</code> is the full absolute path to the file.
- <code>[status]</code> is either <code>OK</code> (if <code>password</code> was NOT found) or <code>ALERT</code> (if <code>password</code> WAS found).
- <code>[details]</code> should be <code>No sensitive keywords found.</code> for <code>OK</code>, or <code>Keyword 'password' found on line X</code> for <code>ALERT</code>, replacing <code>X</code> with the first line number where <code>password</code> appeared (counting from 1).

4. The log file should have:
   - A log entry for each file that is larger than 10MB found under <code>/home/user/storage_audit/</code> (recursively).
   - No other files should appear in the log.

Be sure to use absolute paths in your log, and to ensure precise conformity to the log format for verification.
