You are a compliance officer assigned to audit scheduled tasks and cron jobs for user accounts on a Linux system. To prepare for an audit, you need to:

1. List all user-level (non-root) cron jobs currently active on the system, specifically for the users "alice" and "bob".
2. For each user's crontab (if it exists), extract and report every scheduled command, the full timing specification (minute, hour, day of month, month, day of week), and the user for which it is set.
3. Output your findings in a detailed audit log file located at /home/user/cron_audit_report.txt.

The required output format for cron_audit_report.txt is as follows:

Each user section should begin with:  
`==== CRON JOBS FOR USER: [username] ====`

For each cron job entry, output:

```
TIMING: [minute] [hour] [day_of_month] [month] [day_of_week]
COMMAND: [full command as in crontab]
```

For example (with two jobs for user alice):

```
==== CRON JOBS FOR USER: alice ====
TIMING: 0 5 * * 1
COMMAND: /home/alice/backup.sh
TIMING: 15 14 1 * *
COMMAND: /usr/bin/python3 /home/alice/scripts/cleanup.py
```

If a user does not have any cron jobs, note it clearly with:
`No crontab for user [username]`

Ensure you check only the cron jobs specific to each user's crontab, not the system-wide /etc/crontab or cron.d directories. Your report should include both users ("alice" and "bob") in the order specified above. The formatting (including spacing and line breaks) must exactly match the given example so it can be checked automatically.
