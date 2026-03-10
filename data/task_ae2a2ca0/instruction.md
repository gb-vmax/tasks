Hey, I need help collecting some security diagnostics from a server I'm supporting. There's a web application directory at `/home/user/webapp` and I need to identify any world-writable files in it — those are a common misconfiguration that can lead to security incidents.

Please do the following:

1. Find all **files** (not directories) under `/home/user/webapp` that are world-writable (i.e., have the "write" permission bit set for "others"). Search recursively through all subdirectories.

2. Write the results to a diagnostic report at `/home/user/diagnostics/security_scan.txt` with this exact format:

```
=== WORLD-WRITABLE FILES SCAN ===
Directory: /home/user/webapp
Date: <date in YYYY-MM-DD format>

Files found:
<absolute path to file>
<absolute path to file>
...

Total: <N> file(s) found
```

- The `Date:` line should contain today's date in `YYYY-MM-DD` format (e.g., `2024-03-15`).
- The files must be listed in alphabetical order, one per line, using their absolute paths.
- If no world-writable files are found, the "Files found:" section should be empty (just a blank line after "Files found:") and "Total: 0 file(s) found".
- The `/home/user/diagnostics/` directory may not exist yet — you'll need to create it.

For example, if three world-writable files were found, the file would look like:

```
=== WORLD-WRITABLE FILES SCAN ===
Directory: /home/user/webapp
Date: 2024-03-15

Files found:
/home/user/webapp/config/settings.cfg
/home/user/webapp/public/upload.php
/home/user/webapp/static/style.css

Total: 3 file(s) found
```

The `/home/user/diagnostics/` directory does not yet exist. Please create it and write the report there.
