I'm a compliance analyst and I need to package up some audit log files for our quarterly review submission. We keep daily access logs in `/home/user/audit_logs/` and I need to bundle the ones from March 2024 into a compressed archive, then generate a table-of-contents manifest so our auditors can verify what's inside without extracting it.

Here's what I need you to do:

**Step 1: Create the archive**

Compress all files in `/home/user/audit_logs/` that match the pattern `access_2024-03-*.log` into a single gzip-compressed tar archive at `/home/user/submissions/audit_march_2024.tar.gz`. The files should be archived without the full directory path — meaning they should be stored simply as `access_2024-03-01.log`, `access_2024-03-02.log`, etc. (not as `home/user/audit_logs/access_2024-03-01.log`). You'll need to make sure the `/home/user/submissions/` directory exists first.

**Step 2: Generate the manifest**

After creating the archive, list its contents in verbose mode and write the output to `/home/user/submissions/audit_march_2024_manifest.txt`. This file must contain the exact output of `tar -tzvf` run against the archive — one line per file, showing permissions, ownership, size, date, time, and filename.

The manifest file should have exactly 5 lines (one for each of the 5 March log files that exist). No header lines, no blank lines — just the raw `tar -tzvf` output.
