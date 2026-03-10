I'm a site reliability engineer and I've just audited our uptime monitoring setup at `/home/user/monitoring`. I discovered two serious security vulnerabilities that need to be fixed immediately:

1. **World-writable health check script**: The file `/home/user/monitoring/healthcheck.sh` is currently set to permissions `0777`. This is dangerous — any user on the system can modify this script, and since it runs as a cron job, a malicious user could inject arbitrary commands into it. Fix this by setting its permissions to `0750` (owner has full access, group can read and execute, others have no access).

2. **World-readable credentials file**: The file `/home/user/monitoring/config/api_credentials.conf` is currently set to permissions `0644`. This file contains sensitive API keys and should never be readable by anyone other than the owner. Fix this by setting its permissions to `0600` (owner can read and write, nobody else has any access).

After fixing both permissions issues, produce a security audit report at `/home/user/monitoring/audit_report.txt` that documents what was found and fixed.

The report must have **exactly** this format (substitute in the actual fixed permission values in octal notation):

```
=== SECURITY AUDIT REPORT ===
Date: 2024-01-15
Auditor: sre-bot

VULNERABILITIES FIXED:

[1] healthcheck.sh
    Previous permissions: 0777
    Fixed permissions: 0750
    Risk: World-writable script executed by cron - arbitrary code injection

[2] api_credentials.conf
    Previous permissions: 0644
    Fixed permissions: 0600
    Risk: World-readable credentials file - API key exposure

STATUS: RESOLVED
```

The report file itself must have permissions `0640` (owner read/write, group read-only, others no access).

Please fix the permissions and create this exact report file. I'll be verifying with `stat` and `cat` to confirm everything looks right.
