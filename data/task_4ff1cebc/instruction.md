A customer support engineer needs to collect system diagnostics for troubleshooting. Three log files, located at /home/user/logs/syslog.txt, /home/user/logs/auth.log, and /home/user/logs/kernel.log, have already been gathered in the /home/user/logs directory. 

Your task is to compress these three files into a single archive named diagnostics.tar.gz and place it in the /home/user/diagnostics directory. Make sure that only syslog.txt, auth.log, and kernel.log are included in the archive and that they appear at the root level of the archive (not inside a subdirectory). 

After creating the archive, you must verify the contents by extracting a list of files stored in the archive. Save this list to a new file named /home/user/diagnostics/diagnostics_archive_contents.txt. Each line of diagnostics_archive_contents.txt must contain the full file name as stored in the archive, specifically:
syslog.txt
auth.log
kernel.log

No extra lines or characters should be included in diagnostics_archive_contents.txt. The destination directory, /home/user/diagnostics, already exists and is writable. Ensure that the archive and the list are both created in that directory.
