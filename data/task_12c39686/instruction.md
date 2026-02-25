As a performance engineer, your goal is to synchronize local application profiling data from your machine to a simulated "remote" backup directory within the local filesystem (since actual SSH access is not available). 

1. The profiling data is located in <b>/home/user/app_profile/results/</b> and contains several files with the <b>.prof</b> extension. Before synchronization, make sure all file names, sizes (in bytes), and last modification timestamps (in UTC, ISO 8601 format, e.g., <i>2024-06-15T14:25:36Z</i>) in this directory are recorded.
2. The "remote" backup target is <b>/home/user/remote_server/backup/results/</b>. 
3. Synchronize all <b>.prof</b> files so that the target directory matches the source directory exactly – any extraneous <b>.prof</b> files in the backup target that do not exist in the source are to be deleted, and all differences in content or timestamp are to be updated.
4. After synchronization, create a log file at <b>/home/user/sync_report.log</b> with the following format:
   - The first section is titled <b>[BEFORE]</b> and lists each file present in the source directory before sync: each line must be formatted as <b>{filename} {size_bytes} {mtime_utc}</b>, one per line.
   - The second section is titled <b>[SYNC OPERATIONS]</b> and must log each file operation taken, one per line, in the format: <b>COPIED {filename}</b> if a file was copied to the target, <b>UPDATED {filename}</b> if a file was updated, <b>DELETED {filename}</b> if a file at the target was deleted. No line if no action for that file.
   - The third section is titled <b>[AFTER]</b> and lists the files in the target directory after sync, using the same line format as the <b>[BEFORE]</b> section.

<b>Example structure of the log file:</b>
<pre>
[BEFORE]
cpu.prof 24576 2024-06-15T14:25:36Z
mem.prof 16832 2024-06-15T14:21:00Z

[SYNC OPERATIONS]
COPIED cpu.prof
DELETED old.prof

[AFTER]
cpu.prof 24576 2024-06-15T14:25:36Z
mem.prof 16832 2024-06-15T14:21:00Z
</pre>

Ensure the log reflects exactly what synchronization actions were performed. The entries in each section must be sorted alphabetically by filename.
