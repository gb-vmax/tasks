I'm managing configuration files for a small service and I need your help creating a proper backup and change-tracking workflow. Here's what I need you to do:

I have an existing configuration file at `/home/user/configs/app.conf`. I need you to:

1. **Create a backup directory** at `/home/user/configs/backups/` if it doesn't already exist.

2. **Copy the current `app.conf` to the backup directory** with the filename `app.conf.bak`. The backup should be an exact copy of the original file.

3. **Modify the original `/home/user/configs/app.conf`** by making the following two changes:
   - Find the line that starts with `log_level=` and change its value to `debug`
   - Find the line that starts with `max_connections=` and change its value to `150`
   - Leave all other lines exactly as they are.

4. **Generate a diff report** showing what changed between the backup and the modified config. Save this diff output to `/home/user/configs/backups/changes.diff`. The diff should be produced using the unified diff format (`diff -u`), with the first file argument being the backup (`app.conf.bak`) and the second being the modified original (`app.conf`). The paths shown in the diff header should be exactly `backups/app.conf.bak` and `app.conf` — meaning you should run the diff command from inside `/home/user/configs/` so the relative paths appear that way.

The final state should be:
- `/home/user/configs/app.conf` — the modified config file with updated `log_level` and `max_connections`
- `/home/user/configs/backups/app.conf.bak` — the original unmodified config file
- `/home/user/configs/backups/changes.diff` — the unified diff output, saved as a plain text file

Please make sure the diff file is not empty and accurately reflects only the two lines that changed.
