You are a database reliability engineer tasked with verifying the status of recent backup operations for the "customer_data" PostgreSQL database. A script, <code>/home/user/backup_scripts/postgres_backup.sh</code>, generates daily backup logs which are stored in the directory <code>/home/user/backup_logs/</code>. Each log is named as <code>backup_YYYYMMDD.log</code>.

Your goal is to analyze the five most recent backup log files and generate a status summary report.

Each log contains multiple lines in the format:
<code>[YYYY-MM-DD HH:MM:SS] INFO: Database backup completed: customer_data (Duration: HH:MM:SS) - STATUS: SUCCESS/FAILURE</code>

Steps to complete the task:
1. Identify the five most recent <code>backup_*.log</code> files in <code>/home/user/backup_logs/</code>.
2. For each log file, extract the most recent backup status line for the "customer_data" database.
3. For each file, parse out:
    - The date and time of the entry.
    - The status of the backup (either <code>SUCCESS</code> or <code>FAILURE</code>).
    - The backup duration (as HH:MM:SS).
4. Generate a summary report file at <code>/home/user/backup_summary/backup_status_report.txt</code> with the following format (each line one backup, sorted by date from oldest to newest):
<pre>
DATE_TIME | STATUS | DURATION
2024-06-18 01:43:00 | SUCCESS | 00:12:03
2024-06-19 01:43:01 | FAILURE | 00:07:20
...
</pre>
5. Make sure the report only contains the header and the five entries in the specified format, with exact field separators (" | ") and no trailing spaces.

Ensure that the user running the commands can write to <code>/home/user/backup_summary/</code> and has read access to the logs.

Intended outcome: a readable and accurately formatted status report of the latest five "customer_data" backup attempts.
