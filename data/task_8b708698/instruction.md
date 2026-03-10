Hey, I need help with a quick configuration management task. I'm tracking changes between two versions of a server configuration file and need to generate a formatted change report for our ops team.

I have two config files:
- `/home/user/configs/app.conf.v1` — the old version
- `/home/user/configs/app.conf.v2` — the new version

Please compare these two files and write a change report to `/home/user/configs/changes.txt`.

The report must have this **exact** format:

```
CONFIG CHANGE REPORT
====================
REMOVED:
  - <line that was removed>
  - <line that was removed>
ADDED:
  - <line that was added>
  - <line that was added>
====================
Total changes: <N>
```

Rules for generating the report:
- The `REMOVED:` section lists every line that was in `v1` but is NOT in `v2`, one per line, each prefixed with `  - ` (two spaces, a dash, a space).
- The `ADDED:` section lists every line that is in `v2` but was NOT in `v1`, one per line, each prefixed with `  - ` (two spaces, a dash, a space).
- Lines that are identical in both files should NOT appear in any section.
- The order within each section should match the order those lines appear in their respective source file.
- `Total changes: <N>` is the sum of the number of removed lines plus the number of added lines.
- If there are no removed lines, still include the `REMOVED:` header with no entries beneath it (just an empty section before `ADDED:`).
- If there are no added lines, still include the `ADDED:` header with no entries beneath it.

The two config files already exist on the filesystem — you don't need to create them. Just read them, compute the diff, and write the report to `/home/user/configs/changes.txt`.
