I'm a capacity planner doing a quarterly backup of our application deployment directories. I need you to help me archive two project directories and then produce a concise storage report. Here's exactly what I need done:

**Existing directories to archive:**

- `/home/user/projects/webapp` — a web application directory
- `/home/user/projects/dataservice` — a data service directory

**Step 1: Create compressed archives**

Create gzip-compressed tar archives of each project directory. Place both archives in `/home/user/backups/`. The archive filenames must be:

- `webapp.tar.gz` (archive of `/home/user/projects/webapp`)
- `dataservice.tar.gz` (archive of `/home/user/projects/dataservice`)

When creating the archives, the paths inside the archive should be relative (i.e., the archive should contain `webapp/...` not `/home/user/projects/webapp/...`). You should create the archives from the parent directory `/home/user/projects/` so that this relative structure is preserved.

**Step 2: Generate a storage report**

After creating both archives, write a report file at `/home/user/backups/storage_report.txt`.

The report must have this exact format:

```
=== Backup Storage Report ===
webapp.tar.gz <SIZE_IN_BYTES> bytes
dataservice.tar.gz <SIZE_IN_BYTES> bytes
total 2 archives
```

- Line 1: the literal string `=== Backup Storage Report ===`
- Lines 2 and 3: the archive filename, a single space, the size of that archive file **in bytes** (as reported by `wc -c` or `stat --format=%s`), a single space, then the word `bytes`
- Line 4: the literal string `total 2 archives`
- `webapp.tar.gz` must appear before `dataservice.tar.gz`
- There should be no trailing spaces on any line and no blank lines anywhere in the file

The sizes must reflect the actual byte sizes of the `.tar.gz` files you created in `/home/user/backups/`.
