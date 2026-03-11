I'm a backup administrator and I need to archive old log files from our application server. Can you help me set up and run a backup process on the Linux terminal?

Here's the situation: we have a directory at `/home/user/applogs` that contains log files scattered across multiple subdirectories. I need you to:

1. Find all files ending in `.log` under `/home/user/applogs` that are **larger than 10 kilobytes** and use `xargs` to copy them (preserving their names, but NOT their directory structure) all into a single flat backup directory at `/home/user/backup/archive/`.

2. Use `find` and `xargs` to compute the MD5 checksum of every `.log` file inside `/home/user/backup/archive/` and write the results to a manifest file at `/home/user/backup/manifest.txt`.

   The manifest file must be sorted alphabetically by filename (not full path) and must use this exact format — one line per file:
   ```
   <md5hash>  <filename>
   ```
   Where `<md5hash>` is the 32-character hex digest, followed by **two spaces**, followed by just the bare filename (no directory path). Example line:
   ```
   d41d8cd98f00b204e9800998ecf8427e  app.log
   ```

3. Append a final summary line at the very end of `/home/user/backup/manifest.txt` in this exact format:
   ```
   TOTAL FILES: <N>
   ```
   Where `<N>` is the count of `.log` files archived.

A few constraints:
- The backup directory `/home/user/backup/archive/` must exist before copying (create it if needed).
- Only `.log` files strictly larger than 10 KB should be copied. Files exactly 10240 bytes or smaller must NOT appear in the archive or manifest.
- The manifest lines (before the TOTAL line) must be sorted alphabetically by filename.
- Do not include any path prefix in the hash lines — just the bare filename.
- The `TOTAL FILES:` line must be the last line of the file, with no trailing newline after it.
