I'm a monitoring specialist and I need to create a backup of our alerting configuration before we push some changes. The alert configs are stored in `/home/user/monitoring/alerts/` and I need to archive the entire directory into a single compressed tarball.

Please create a gzip-compressed tar archive of `/home/user/monitoring/alerts/` and save it to `/home/user/backups/alerts_backup.tar.gz`. The archive should preserve the directory structure, meaning when you list its contents, paths should appear as `alerts/filename` (i.e., the `alerts` directory itself should be included as the top-level entry, not just the files inside it).

After creating the archive, I also need a plain-text manifest file at `/home/user/backups/alerts_manifest.txt`. This file should list every file path contained in the archive, one per line, exactly as they appear when running `tar -tzf` on the archive — including the top-level `alerts/` directory entry itself. The lines should be in the same order that `tar -tzf` outputs them (no sorting, no modification).

The `/home/user/backups/` directory does not exist yet, so you'll need to create it first.
