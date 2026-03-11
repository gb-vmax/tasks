Hey, I need help resolving a batch of IT support tickets on our file server. There's a shared directory at `/home/user/fileserver` that's gotten messy — there are stale temp files, overly permissive scripts, and old reports that need to be archived. I need you to clean it all up and produce an audit log. Here's what needs to happen:

---

**Step 1: Remove stale temporary files**

Find all files under `/home/user/fileserver` (recursively) that match the pattern `*.tmp` AND were last modified more than 2 days ago. Delete them using `find` with `xargs`. Do not delete `.tmp` files modified within the last 2 days.

---

**Step 2: Fix insecure script permissions**

Find all files under `/home/user/fileserver` (recursively) that have the extension `.sh` and are currently world-writable (i.e., have permission bit `o+w` set). Use `find` and `xargs` to remove the world-writable bit from all of them (use `chmod o-w`). Do not touch `.sh` files that are not world-writable.

---

**Step 3: Archive old report files**

Find all files under `/home/user/fileserver` (recursively) that match `*.report` AND were last modified more than 2 days ago. Move all of them (using `find` and `xargs`) into the directory `/home/user/fileserver/archive/`. The archive directory already exists. Do not move `.report` files modified within the last 2 days.

---

**Step 4: Generate an audit log**

After completing steps 1–3, generate an audit log at `/home/user/audit.log`. The file must be produced using `find` commands and contain the following sections in this exact order, with these exact headers:

```
=== REMAINING TMP FILES ===
<list of .tmp files still present under /home/user/fileserver, one absolute path per line, sorted>

=== FIXED SCRIPTS ===
<list of .sh files under /home/user/fileserver that are NOT world-writable, one absolute path per line, sorted>

=== ARCHIVED REPORTS ===
<list of .report files under /home/user/fileserver/archive/, one absolute path per line, sorted>
```

Each section header must appear exactly as shown (including the `===` delimiters and spacing). Each section's file list should be sorted lexicographically (use `sort`). If a section has no files, print the header and leave the list empty (no blank line, just the next header immediately after).

For example, if there are no remaining `.tmp` files, the output would be:
```
=== REMAINING TMP FILES ===
=== FIXED SCRIPTS ===
...
```

---

The directory structure under `/home/user/fileserver` currently looks like this (don't worry about memorizing it — just use the right `find` predicates and it will all work out). The `archive/` subdirectory exists and is empty. Make sure every `find | xargs` pipeline handles filenames safely (use `-print0` and `-0` or equivalent).
