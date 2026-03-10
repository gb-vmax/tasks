I'm auditing our microservices deployment and I've found some concerning security issues in our container configuration directory. I need your help to identify and fix insecure file permissions on sensitive credential files, then produce a short audit report.

Our services are deployed with config files under `/home/user/services/`. After a rushed deployment, several files ended up with dangerously permissive settings. Here's what I need done:

**Step 1: Inspect and record the current (insecure) permissions**

Check the permissions of all files directly inside `/home/user/services/` (non-recursively — just the files at that level, not subdirectories). Use `stat` to get the octal permission of each file.

**Step 2: Fix the permissions**

- Any file whose name contains `credentials`, `secret`, or `token` should be set to `600` (owner read/write only — no access for group or others).
- Any file whose name contains `config` (but not `credentials`, `secret`, or `token`) should be set to `640` (owner read/write, group read, no access for others).
- All other files in that directory should be set to `644`.

**Step 3: Write an audit report**

Write a file at `/home/user/services/audit_report.txt` with the following exact format:

```
PERMISSION AUDIT REPORT
=======================
FILE: <filename>
  BEFORE: <octal>
  AFTER: <octal>
FILE: <filename>
  BEFORE: <octal>
  AFTER: <octal>
...
=======================
TOTAL FILES REMEDIATED: <N>
```

Requirements for the report:
- `<filename>` is just the base filename (not the full path), e.g. `db_credentials.env`
- `<octal>` is the 4-digit octal permission string as reported by `stat --format="%a"`, e.g. `644`, `777`, `600` — **do not zero-pad to 4 digits unless stat outputs it that way**
- Files should be listed in **alphabetical order** by filename
- `<N>` is the total count of files that appear in the report (i.e., all files in the directory, not counting `audit_report.txt` itself)
- Do NOT include `audit_report.txt` itself in the report entries
- The two `=======================` separator lines must be exactly 23 `=` characters each

After writing the report, verify the permissions are correctly applied by running `stat --format="%n %a"` on each file. The audit report itself (`audit_report.txt`) should be left with whatever default permissions it was created with — do not explicitly chmod it.
