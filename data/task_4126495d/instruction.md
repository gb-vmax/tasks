You are a security auditor who needs to check the file permissions of all files in the directory <code>/home/user/security_audit/</code>. List the permissions, ownership, and filenames of all files (do not include directories or their contents) in that directory and save the output in a file named <code>/home/user/permission_audit_report.txt</code>. 

The report must list exactly one line per file (not directory) in the following format for each file:

<pre>
[PERMISSIONS] [OWNER] [GROUP] [FILENAME]
</pre>

- <b>[PERMISSIONS]</b> should be the full symbolic permission string (e.g., <code>-rw-r--r--</code>).
- <b>[OWNER]</b> and <b>[GROUP]</b> should be the Unix owner and group.
- <b>[FILENAME]</b> should be the file's name only, not the path.
- Only include files directly in <code>/home/user/security_audit/</code>, not subdirectories or files within subdirectories.
- The order of the lines does not matter, but there should be one line for each file.

After running the command, confirm that the <code>/home/user/permission_audit_report.txt</code> file matches the specification above.
