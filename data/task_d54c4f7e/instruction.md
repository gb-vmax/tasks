I'm a configuration manager and I need your help securing a sensitive configuration file and logging the change for our audit trail.

There's a configuration file at `/home/user/configs/database.conf` that currently has overly permissive permissions. I need you to:

1. Change the permissions on `/home/user/configs/database.conf` so that the owner has read and write access, the group has read-only access, and others have no access at all. (This corresponds to mode `640`.)

2. After changing the permissions, append a single line to the audit log at `/home/user/configs/audit.log` recording this change. The line must follow this exact format:

```
PERMISSION_CHANGE: /home/user/configs/database.conf 664->640 by user
```

Where:
- `PERMISSION_CHANGE:` is the literal label
- `/home/user/configs/database.conf` is the file path
- `664->640` shows the old permissions followed by `->` followed by the new permissions (both as 3-digit octal numbers without a leading zero)
- `by user` is the literal string `by user`
- Fields are separated by single spaces
- There is no trailing whitespace on the line

The audit log already exists and may contain prior entries — do not overwrite it, only append.
