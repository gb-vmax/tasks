I'm a system administrator and I need to quickly identify which subdirectories under `/home/user/server_data` are consuming the most disk space. Some of those directories have grown unexpectedly large and I need a sorted report to send to my team.

Please generate a disk usage report file at `/home/user/disk_report.txt` that lists the disk usage of each **direct subdirectory** of `/home/user/server_data` (one level deep only), sorted from largest to smallest. The report should only include entries that are **50 kilobytes or larger**.

The file must have this exact format — a header line, a separator line, then one entry per qualifying subdirectory:

```
Disk Usage Report: /home/user/server_data
==========================================
<size_in_KB>K	<path>
<size_in_KB>K	<path>
...
```

Specific requirements:
- The header is exactly: `Disk Usage Report: /home/user/server_data`
- The separator is exactly 42 `=` characters on its own line.
- Each data line has the size (as reported by `du -k`, in kilobytes, followed immediately by the letter `K`), then a **tab character**, then the full absolute path to the subdirectory.
- Entries are sorted largest first (descending by size).
- Any subdirectory whose `du -k` size is less than 50 is excluded entirely.
- There should be no trailing spaces, no blank lines between entries, and no extra lines after the last entry.

For example, if `/home/user/server_data/logs` uses 128K and `/home/user/server_data/cache` uses 64K and `/home/user/server_data/tmp` uses 12K, the file should look like:

```
Disk Usage Report: /home/user/server_data
==========================================
128K	/home/user/server_data/logs
64K	/home/user/server_data/cache
```

(`tmp` is excluded because 12 < 50.)
