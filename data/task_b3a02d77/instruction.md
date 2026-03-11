You're a DevSecOps engineer enforcing a permissions policy on a server. A secrets configuration file at `/home/user/config/secrets.env` currently has overly permissive access rights — it's readable and writable by everyone. Company policy requires this file to be accessible only by its owner (read and write for owner, no permissions for group or others).

Please do the following:

1. Change the permissions on `/home/user/config/secrets.env` so that only the file owner has read and write access (mode `600`). Group and others must have zero permissions.

2. After enforcing the new permissions, produce an audit log entry at `/home/user/audit/permissions.log`. The file must contain exactly one line in this format:

```
ENFORCED 600 /home/user/config/secrets.env
```

That is: the word `ENFORCED`, a single space, the octal mode `600`, a single space, and the absolute path to the file. No trailing whitespace, no blank lines, nothing else.

The `/home/user/audit/` directory does not exist yet — you'll need to create it first.

To verify your work: running `stat -c "%a" /home/user/config/secrets.env` should output `600`, and `cat /home/user/audit/permissions.log` should output exactly the line shown above.
