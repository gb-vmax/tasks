I'm a deployment engineer and I just unpacked a release tarball onto our staging server. I've discovered that the deployment package at `/home/user/deploy` has some serious security vulnerabilities in the file permissions — several sensitive files are world-writable or have way too open permissions. I need you to lock these down before we proceed with the rollout.

Here's what I know about the files in `/home/user/deploy`:

- `start.sh` — the main startup script. It's currently world-writable, which means any user on the system could tamper with it. It should be executable by the owner and group, but NOT writable or readable by others. The correct permission should be `750`.
- `config/db.conf` — the database configuration file containing credentials. Right now it's readable by everyone. It should only be readable and writable by the owner, with no permissions for group or others. The correct permission should be `600`.
- `config/app.conf` — the general application config. It's currently world-writable. It should be readable and writable by owner, readable by group, and have no permissions for others. The correct permission should be `640`.
- `logs/` — the logs directory. It's currently world-writable (sticky bit is not set). It should be writable only by owner, readable and executable by group, and have no permissions for others. The correct permission should be `750`.

Please fix all four of these permission issues. After you're done, I want you to record the audit results in a file at `/home/user/deploy/security_audit.txt`. The file should contain exactly the following content (use `ls -la` style permission strings):

```
DEPLOYMENT SECURITY AUDIT
=========================
start.sh: -rwxr-x---
config/db.conf: -rw-------
config/app.conf: -rw-r-----
logs/: drwxr-x---
STATUS: SECURED
```

The file paths in the audit should be relative (not absolute), and the permission strings should match exactly what `ls -l` would display for those files. There should be no trailing spaces on any line. The final line must be `STATUS: SECURED` with no blank line after it.
