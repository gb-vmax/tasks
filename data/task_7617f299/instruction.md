I'm a compliance analyst and I need to generate an audit trail report from our server's authentication log. The log file is located at `/home/user/logs/auth.log`. I need you to analyze it and produce a formatted report at `/home/user/reports/audit_report.txt`.

The auth log uses standard syslog format. Each line looks something like this:

```
Mar 15 09:23:41 webserver sshd[12345]: Failed password for alice from 192.168.1.10 port 54321 ssh2
Mar 15 09:24:02 webserver sshd[12346]: Failed password for invalid user bob from 10.0.0.5 port 43210 ssh2
Mar 15 09:25:10 webserver sshd[12347]: Accepted password for carol from 192.168.1.20 port 33333 ssh2
```

Please produce the report at `/home/user/reports/audit_report.txt`. The `reports` directory may not exist yet — create it if needed.

The report must have this **exact** format:

```
=== FAILED LOGIN AUDIT REPORT ===
Log file: /home/user/logs/auth.log
Total failed attempts: <N>

Failed attempts per user (descending):
  <username>: <count>
  <username>: <count>
  ...

Users with 3 or more failed attempts (HIGH RISK):
  <username>
  ...
```

Important formatting rules:
- "Total failed attempts" must be the total count of all `Failed password` lines in the log.
- The "Failed attempts per user" section lists every user who had at least one failed login, sorted by count descending. If two users have the same count, sort them alphabetically by username.
- Each entry in that section is two spaces of indentation, followed by the username, a colon, a space, and the count.
- The "HIGH RISK" section lists only users with 3 or more failed attempts, sorted alphabetically. Each name is indented with two spaces.
- If there are no high-risk users, write `  (none)` (two spaces then the word in parentheses) for that section.
- A "user" is the username that appears after `Failed password for` or `Failed password for invalid user` — strip the `invalid user` prefix so only the bare username remains.
