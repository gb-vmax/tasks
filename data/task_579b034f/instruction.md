I'm a backup operator and I need to test the restore performance of a backup archive we made last night. The archive is at `/home/user/backups/nightly.tar.gz` and there's a checksum manifest at `/home/user/backups/manifest.sha256`.

Please do the following:

1. **Extract the archive** into a fresh restore directory at `/home/user/restore_test/`. Time how long the extraction takes (wall-clock seconds, rounded to two decimal places).

2. **Verify the restored files** by running `sha256sum --check` against `/home/user/backups/manifest.sha256` from within the `/home/user/restore_test/` directory. All files should pass.

3. **Write a restore report** to `/home/user/backups/restore_report.txt` with exactly this format (fill in the real values):

```
=== RESTORE TEST REPORT ===
Archive: /home/user/backups/nightly.tar.gz
Destination: /home/user/restore_test
Extraction time (s): <seconds as X.XX>
Archive size (bytes): <exact byte count from stat>
Files restored: <count of regular files under /home/user/restore_test>
Checksum status: OK
```

Important formatting rules:
- The extraction time must be formatted with exactly two decimal places (e.g., `1.47` or `12.03`), not more, not fewer.
- The archive size must be the exact byte count as reported by `stat --format=%s` on the archive file.
- "Files restored" must be the count of regular files only (use `find /home/user/restore_test -type f`).
- "Checksum status" must be `OK` if all checksums pass, or `FAIL` if any do not.
- There must be no trailing spaces on any line.
- The file must end with a single newline.

Can you run through this whole restore test and produce the report for me?
