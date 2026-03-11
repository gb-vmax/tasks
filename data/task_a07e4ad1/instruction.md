Hey, I need your help archiving some old log files on our server before we rotate them out. I'm debugging an intermittent issue and need to preserve specific logs for later analysis.

Here's the situation: there are log files in `/home/user/logs/` directory. I need you to create a compressed tarball of only the files that match the pattern `app-2024-01-*.log` (January 2024 logs), then verify the archive was created correctly.

**Step 1:** Create a gzip-compressed tar archive at `/home/user/backups/app-jan2024.tar.gz` containing all files from `/home/user/logs/` that match the pattern `app-2024-01-*.log`. The files should be archived with their bare filenames only (no directory path prefix inside the archive — so `app-2024-01-01.log`, not `home/user/logs/app-2024-01-01.log`).

**Step 2:** Write a manifest file at `/home/user/backups/app-jan2024.manifest` that lists the contents of the archive. The manifest must be produced by running `tar -tzf` on the archive you created. The file should contain exactly the filenames inside the archive, one per line, in the order they appear in the archive, with no extra formatting or headers — just the raw output of `tar -tzf /home/user/backups/app-jan2024.tar.gz` redirected into the file.

The `/home/user/backups/` directory does not exist yet — you will need to create it.

Make sure the archive does NOT include any files that don't match the January 2024 pattern (e.g., `app-2024-02-01.log` or `system.log` should be excluded).
