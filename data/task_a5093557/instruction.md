You are a backup engineer who needs to verify the integrity of a data backup using a Python script. In the directory <code>/home/user/backup_verification</code>, there is a script called <code>check_backup.py</code> that prints "Backup OK" if the checksum of <code>backup.tar.gz</code> in the same directory matches a known value.

Before running this script, set up a Python virtual environment named <code>venv</code> inside <code>/home/user/backup_verification</code> using Python’s standard <code>venv</code> module. 

After setting up the environment:
1. Activate the virtual environment (make sure your Python prompt indicates you are inside <code>venv</code>).
2. Run <code>python check_backup.py</code>.
3. The output should be appended to a log file named <code>verify.log</code> in <code>/home/user/backup_verification</code>. Only append the line "Backup OK" to this log file, with no extra text or timestamp. The log must only contain "Backup OK" as a new line at the end of the file.

Leave all files and the <code>venv</code> directory in place for later verification.
