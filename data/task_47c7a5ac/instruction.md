I'm a storage administrator and I've been collecting a daily snapshot log of files on our file server. The log file is at `/home/user/storage/file_audit.log`. Each line in this file represents one file and has the following tab-separated format:

```
<size_in_bytes>\t<username>\t<file_path>
```

For example:
```
204800	alice	/data/projects/report.pdf
```

I need you to help me analyze this log to understand our disk usage patterns and produce a summary report. Here's what I need:

**Step 1: Count files per user**
Count how many files each user has. Produce an intermediate sorted list (by file count descending, then alphabetically by username for ties) and use this in the final report.

**Step 2: Count files per file extension**
Extract the file extension from each file path (the part after the last `.` in the filename, e.g., `pdf`, `txt`, `log`). Files with no extension (no `.` in the filename itself, ignoring directory components) should be counted under the label `(none)`. Count how many files have each extension, sorted by count descending, then alphabetically for ties.

**Step 3: Identify the top 3 users by file count**
From your user counts, list only the top 3.

**Step 4: Identify the top 5 extensions by file count**
From your extension counts, list only the top 5.

**Step 5: Write the final report**
Write the report to `/home/user/storage/disk_report.txt` with **exactly** this format (no trailing spaces, unix line endings):

```
=== DISK USAGE REPORT ===

-- Top 3 Users by File Count --
1. <username>: <count> files
2. <username>: <count> files
3. <username>: <count> files

-- Top 5 Extensions by File Count --
1. <ext>: <count> files
2. <ext>: <count> files
3. <ext>: <count> files
4. <ext>: <count> files
5. <ext>: <count> files

-- Summary --
Total files: <N>
Total unique users: <N>
Total unique extensions: <N>
```

Where `<ext>` is the extension label (e.g., `pdf`) or `(none)` for files without an extension.

The `Total unique extensions` count should include `(none)` if any files have no extension.

Please produce this report from the existing log file. Do not modify the original `file_audit.log`.
