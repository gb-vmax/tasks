I'm a storage administrator and I need your help analyzing disk usage on this server and generating a disk space management report. There's a directory tree at `/home/user/storage` that simulates several application data directories. I need you to analyze the space usage and produce a structured report.

Here's what I need you to do:

**Step 1: Read the storage configuration**

There's a file at `/home/user/storage/storage.conf` that defines the monitored directories and their warning thresholds (in MB). Each non-comment line has the format:
```
<directory_path>:<warning_threshold_mb>
```
Lines beginning with `#` are comments and should be ignored.

**Step 2: Analyze each monitored directory**

For each directory listed in `storage.conf`, compute its total disk usage in MB (rounded to the nearest integer). Mark it as `WARN` if its usage meets or exceeds the threshold, or `OK` if it is below the threshold.

Use `du -sm <directory>` to get the usage in MB for each directory. The first field (the number) is the size in MB.

**Step 3: Find the top 3 largest files across all monitored directories**

Across all directories listed in `storage.conf`, find the 3 largest individual files by size. Use `find` and `du` or `stat` to get each file's size in bytes. Report the size in KB (rounded to the nearest integer).

For this step, only count regular files (not directories, symlinks, etc.).

**Step 4: Compute the aggregate total**

Sum up the disk usage (in MB) across all monitored directories and report the total.

**Step 5: Write the report**

Write the report to `/home/user/storage_report.txt` with this exact format:

```
=== DISK SPACE REPORT ===
Generated for: /home/user/storage

--- Directory Usage ---
<dir_path>: <usage_mb>MB [<STATUS>] (threshold: <threshold_mb>MB)
<dir_path>: <usage_mb>MB [<STATUS>] (threshold: <threshold_mb>MB)
...

--- Top 3 Largest Files ---
1. <absolute_file_path> (<size_kb>KB)
2. <absolute_file_path> (<size_kb>KB)
3. <absolute_file_path> (<size_kb>KB)

--- Summary ---
Total monitored usage: <total_mb>MB
Directories in WARNING: <warn_count>
```

Important formatting rules:
- The directories in the "Directory Usage" section must appear in the **same order** as they appear in `storage.conf` (top to bottom, skipping comment lines).
- The "Top 3 Largest Files" must be sorted by size **descending** (largest first). If two files have the same size in KB, sort them alphabetically by absolute path.
- `<usage_mb>` and `<threshold_mb>` are plain integers (no decimals).
- `<size_kb>` is a plain integer (no decimals).
- `<total_mb>` is the sum of all `<usage_mb>` values shown in the Directory Usage section (plain integer).
- `<warn_count>` is the count of directories with status `WARN`.
- There is exactly one blank line between each of the four sections (after the header line, after the Directory Usage block, and after the Top 3 block).

The report file should end with a newline after the last line (`Directories in WARNING: <N>`).
