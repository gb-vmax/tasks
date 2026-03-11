I'm building an automated disk-usage monitoring workflow and need a quick disk analysis script output for our project archive. We have a directory at `/home/user/archive` containing several subdirectories. I need you to analyze the disk usage of each immediate subdirectory, sort them from largest to smallest, and save the results to a report file.

Please generate a disk usage report at `/home/user/disk_report.txt`. The report must list the disk usage of each **immediate subdirectory** of `/home/user/archive` (one level deep only — do not recurse into sub-subdirectories), sorted by size in **descending order** (largest first).

The format of `/home/user/disk_report.txt` must be exactly:

```
<size_in_KB>K	<path>
<size_in_KB>K	<path>
...
```

Where each line has:
- The size expressed in **kilobytes with a capital K suffix** (e.g., `44K`)
- A **tab character** separating the size and the path
- The **full absolute path** of the subdirectory (e.g., `/home/user/archive/videos`)
- Lines sorted by numeric size, largest first

For example, if `videos` used 44K, `docs` used 28K, and `logs` used 8K, the file would contain exactly:
```
44K	/home/user/archive/videos
28K	/home/user/archive/docs
8K	/home/user/archive/logs
```

No header line, no blank lines, no trailing spaces — just the sorted data lines. The path column should use absolute paths, not relative ones.
