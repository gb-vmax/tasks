I'm a database reliability engineer and I need your help verifying the integrity of our PostgreSQL backup files before we rotate them off to cold storage. We've had incidents in the past where corrupted backups made it to the archive, so I need a verified integrity report before anything gets moved.

The backup files are stored in `/home/user/backups/pg/` and there is a pre-existing checksum manifest at `/home/user/backups/pg/checksums.sha256`. This manifest was generated when the backups were first created and contains SHA-256 hashes for each backup file.

Please verify all the backup files against the manifest, then write an integrity report to `/home/user/backups/integrity_report.txt`.

The report must have this exact format:

```
BACKUP INTEGRITY REPORT
=======================
db_primary_20240801.dump: OK
db_replica_20240801.dump: OK
db_primary_20240731.dump: FAILED
db_replica_20240731.dump: OK
=======================
PASSED: 3
FAILED: 1
STATUS: CORRUPTED
```

Specific formatting rules:
- The header is the literal string `BACKUP INTEGRITY REPORT` followed by a line of 23 `=` characters.
- Each line lists the filename (basename only, no directory path) followed by `: OK` or `: FAILED`.
- Files must be listed in the same order they appear in `checksums.sha256`.
- After the file listing, a separator line of 23 `=` characters.
- Then `PASSED: <N>` and `FAILED: <N>` counts.
- The final line is `STATUS: VERIFIED` if all files passed, or `STATUS: CORRUPTED` if any file failed.

The checksums.sha256 manifest uses standard `sha256sum` format (hash followed by two spaces followed by the filename with its path, e.g., `abc123...  /home/user/backups/pg/db_primary_20240801.dump`).

Use `sha256sum --check` or verify each file individually — whichever approach you prefer — and then produce the report file as described above.
