I'm a backup administrator and I need to analyze disk usage across several data directories before deciding what to archive. I have four independent data directories under `/home/user/datastore`:

- `/home/user/datastore/projects`
- `/home/user/datastore/media`
- `/home/user/datastore/logs`
- `/home/user/datastore/databases`

For each of these four directories, I need you to analyze their disk usage and produce individual summary files, then combine everything into a master report. Here's exactly what I need done:

---

**Step 1: Per-directory analysis**

For each of the four directories, create a summary file inside `/home/user/backup_analysis/` named `<dirname>_summary.txt` (e.g., `projects_summary.txt`). Each summary file must have this exact format:

```
Directory: /home/user/datastore/<dirname>
Total size (bytes): <N>
File count: <N>
Largest file: <relative/path/to/file> (<N> bytes)
Smallest file: <relative/path/to/file> (<N> bytes)
```

- "Total size (bytes)" is the sum of the actual byte sizes of all regular files in the directory tree (not `du` block sizes — use `find` with `stat` or `wc -c` or similar to get exact byte counts).
- "File count" is the number of regular files (not directories or symlinks).
- "Largest file" and "Smallest file" paths are relative to the directory itself (e.g., `subdir/file.txt` not the full absolute path). If there is a tie for largest or smallest, choose the one that comes first alphabetically by relative path.

---

**Step 2: Per-directory top-3 files report**

For each directory, also create a file `/home/user/backup_analysis/<dirname>_top3.txt` listing the three largest files (by exact byte size). Format:

```
Top 3 largest files in /home/user/datastore/<dirname>:
1. <relative/path> (<N> bytes)
2. <relative/path> (<N> bytes)
3. <relative/path> (<N> bytes)
```

If the directory has fewer than 3 files, list all files (still numbered 1, 2, 3... up to however many exist). Sort by size descending; break ties alphabetically by relative path.

---

**Step 3: Master report**

Create `/home/user/backup_analysis/master_report.txt` with the following exact format:

```
=== BACKUP ANALYSIS REPORT ===
Generated from: /home/user/datastore

DIRECTORY SUMMARY (sorted by total size, largest first):
  1. <dirname>: <N> bytes (<filecount> files)
  2. <dirname>: <N> bytes (<filecount> files)
  3. <dirname>: <N> bytes (<filecount> files)
  4. <dirname>: <N> bytes (<filecount> files)

GRAND TOTAL: <N> bytes across <N> files

ARCHIVE RECOMMENDATIONS:
  Exceeds 100KB: <dirname>, <dirname>, ...  (or "None" if none qualify)
  Exceeds 50KB:  <dirname>, <dirname>, ...  (or "None" if none qualify)

LARGEST SINGLE FILE OVERALL:
  <relative-to-datastore/path> (<N> bytes)
```

Notes on the master report:
- In "DIRECTORY SUMMARY", sort directories by total byte size descending; break ties alphabetically by directory name.
- "GRAND TOTAL" is the sum of all files across all four directories.
- "Exceeds 100KB" lists directory names (not paths) whose total size exceeds 102400 bytes, sorted alphabetically.
- "Exceeds 50KB" lists directory names whose total size exceeds 51200 bytes (include those already listed in Exceeds 100KB too), sorted alphabetically.
- "LARGEST SINGLE FILE OVERALL" path is relative to `/home/user/datastore` (e.g., `projects/subdir/file.txt`).
- For ties on the largest single file, choose alphabetically first by this relative path.

---

All output files should be created in `/home/user/backup_analysis/` (create the directory if it doesn't exist). The individual summary files for all four directories can be produced in any order (they're independent), but the master report must be produced last after all individual summaries are complete.
