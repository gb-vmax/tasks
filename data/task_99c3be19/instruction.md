Hey, I need your help managing disk space on our server. I'm a storage admin and I've noticed that the `/home/user/data` directory is filling up fast. I need to quickly audit which subdirectories are consuming the most space so I can report it to the team.

Please do the following:

1. Use `du` to measure the disk usage of each **immediate subdirectory** inside `/home/user/data` (not recursively listing every nested folder — just the top-level subdirectories and their total sizes). Measure in **kilobytes (1K blocks)**.

2. Sort the results by size in **descending order** (largest first).

3. Write the **top 3 largest subdirectories** to a report file at `/home/user/disk_report.txt` in this exact format:

```
=== Disk Usage Report ===
1. <size>K  <path>
2. <size>K  <path>
3. <size>K  <path>
```

Where:
- `<size>` is the number of 1K blocks as reported by `du`
- `<path>` is the full absolute path to the subdirectory (e.g., `/home/user/data/logs`)
- There is exactly one tab character between `<size>K` and `<path>` on each line
- The numbering `1.`, `2.`, `3.` is followed by a single space before `<size>`

For example, a valid line would look like:
```
1. 204800K	/home/user/data/backups
```
(where the gap between `204800K` and `/home/user/data/backups` is a tab)

The report should contain exactly 4 lines total: the header line `=== Disk Usage Report ===` followed by the 3 ranked entries.

The `/home/user/data` directory already exists with subdirectories inside it. Do not modify any files inside `/home/user/data` — only create the report file at `/home/user/disk_report.txt`.
