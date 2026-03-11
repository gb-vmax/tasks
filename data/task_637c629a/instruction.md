I'm a backup administrator and I've just discovered that some sensitive configuration files in our application directory have dangerously insecure permissions — they're world-readable, meaning any user on the system can read passwords and API keys stored in them. Before I archive these files for offsite backup, I need to fix the permissions first, then create the archive so the backup itself contains files with correct, secure permissions.

Here's what I need you to do:

**Step 1: Fix the permissions on the sensitive files**

The following files exist under `/home/user/appdata/`:
- `/home/user/appdata/db.conf` — contains database credentials. Should be readable/writable by owner only: `600`
- `/home/user/appdata/api_keys.conf` — contains API secrets. Should be readable/writable by owner only: `600`
- `/home/user/appdata/app.log` — a general application log. Should be readable/writable by owner, readable by group, no access for others: `640`

**Step 2: Create the backup archive**

Create a gzip-compressed tar archive at `/home/user/backups/appdata_backup.tar.gz` that contains all three files from `/home/user/appdata/`. The archive must preserve the file permissions you just set (tar does this by default, but make sure you're not using any flags that would strip or override permissions).

The files should be archived with relative paths so they appear inside the archive as:
- `appdata/db.conf`
- `appdata/api_keys.conf`
- `appdata/app.log`

(i.e., run tar from `/home/user` so the paths inside the archive are relative to that directory, not absolute paths starting with `/`)

**Step 3: Verify the archive**

Confirm the archive is valid and check that the permissions recorded inside it are correct by listing the verbose contents of the archive and redirecting that output to `/home/user/backups/archive_manifest.txt`.

The `/home/user/backups/archive_manifest.txt` file must contain exactly three data lines (one per file). Each line should show the permissions in the format produced by `tar -tzvf`, which looks like:

```
-rw------- user/user   <size> <date> <time> appdata/db.conf
-rw------- user/user   <size> <date> <time> appdata/api_keys.conf
-rw-r----- user/user   <size> <date> <time> appdata/app.log
```

The exact sizes, dates, and times will vary — but the permission strings and filenames must match exactly as shown above. The file owner and group will reflect the actual user running the commands (shown generically as `user/user` above). The lines may appear in any order.

Please fix the permissions, create the archive, and generate the manifest file.
