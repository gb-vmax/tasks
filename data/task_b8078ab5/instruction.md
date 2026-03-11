Hey, I need your help configuring some environment variables on this server. We're setting up a new application deployment and I need to add several environment variables to the system's Bash configuration file so they persist across sessions.

Please add the following environment variable definitions to the end of `/home/user/.bashrc`:

```
# App deployment config
export APP_ENV=production
export APP_PORT=8443
export APP_LOG_LEVEL=warn
export APP_MAX_WORKERS=8
export APP_DATA_DIR=/var/app/data
```

The block must be appended exactly as shown above — the comment line first, then the five `export` lines in the order listed, with no extra blank lines between them and no trailing blank line after the last export.

After adding those lines, source the updated `/home/user/.bashrc` file so the variables become active in the current session, and then write a verification snapshot to `/home/user/env_check.txt` by running:

```
env | grep "^APP_" | sort
```

and redirecting the output to `/home/user/env_check.txt`.

The file `/home/user/env_check.txt` must contain exactly these lines (in this order, since `sort` will sort them alphabetically):

```
APP_DATA_DIR=/var/app/data
APP_ENV=production
APP_LOG_LEVEL=warn
APP_MAX_WORKERS=8
APP_PORT=8443
```

To summarize the end state I need:
1. `/home/user/.bashrc` has the new block appended at the end, exactly matching the format above.
2. `/home/user/env_check.txt` exists and contains exactly those 5 lines in alphabetical order with no extra whitespace or blank lines.
