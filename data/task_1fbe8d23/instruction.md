I need to back up information for network troubleshooting. Specifically, I'd like you to perform the following steps:

1. Run the <code>ping</code> command to test connectivity to the IP address <code>8.8.8.8</code> and collect exactly 5 pings. 
2. Save the output of this test in a text file at <code>/home/user/network/ping_output.txt</code>. 
3. Archive this file into a gzip-compressed tarball at <code>/home/user/network/backup/network_logs.tar.gz</code>. The archive should contain only <code>ping_output.txt</code> (no directory structure inside the archive).
4. Create a log file at <code>/home/user/network/backup/backup_log.txt</code> with exactly two lines: 
    - The first line should state: <code>Backup created: network_logs.tar.gz</code>
    - The second line should state the exact UTC timestamp of when the tarball was created, in ISO 8601 format (e.g., <code>2024-06-01T13:24:56Z</code>).

Make sure the contents of the log file exactly match these requirements, and confirm that only the required file is in the archive with no directory structure.
