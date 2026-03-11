Hey, I'm a backup operator and I need your help processing a backup log file to prepare a restore verification report. We ran a series of backups overnight and the results were written to `/home/user/backups/backup_run.log`. I need to extract specific information from this file and produce a clean report.

The log file has lines in this format:
```
BACKUP|<job_id>|<hostname>|<status>|<size_mb>|<duration_sec>
```

For example:
```
BACKUP|JOB001|webserver01|SUCCESS|2048|120
BACKUP|JOB002|dbserver01|FAILED|0|45
```

There are also comment lines starting with `#` and blank lines in the file that should be ignored.

I need you to produce a restore verification report at `/home/user/backups/restore_verification.txt`. Here is exactly what the report should look like:

```
=== RESTORE VERIFICATION REPORT ===
Successful backups eligible for restore testing:

  JOB003  fileserver01        1523 MB   ( 95 sec)
  JOB005  webserver02         4096 MB   (210 sec)

Total eligible: 2 jobs, 5619 MB
```

The specific rules are:

1. Only include jobs where status is `SUCCESS` AND size is greater than 1000 MB. These are "eligible" jobs.
2. List them in the order they appear in the log file.
3. Each eligible job line must be formatted **exactly** as two spaces of indentation, then the job ID left-aligned in a field of 7 characters, then the hostname left-aligned in a field of 20 characters, then the size right-aligned in a field of 4 characters followed by ` MB`, then two spaces, then the duration in parentheses with the seconds value right-aligned in a field of 3 characters followed by ` sec)` — like `( 95 sec)`.
4. The summary line at the bottom must say `Total eligible: N jobs, TOTAL MB` where N is the count of eligible jobs and TOTAL is the sum of their sizes in MB.
5. The header `=== RESTORE VERIFICATION REPORT ===` and the line `Successful backups eligible for restore testing:` must appear exactly as shown, followed by a blank line before the job list, and a blank line between the last job and the summary line.

Please process `/home/user/backups/backup_run.log` using awk and/or sed to produce this report at `/home/user/backups/restore_verification.txt`. The automated test will check the file character-by-character, so spacing and alignment must be exact.
