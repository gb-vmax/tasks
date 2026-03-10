I'm an incident responder and I've been handed a server where someone may have tampered with critical system configuration files. I have a directory of config files at `/home/user/incident/configs/` and a trusted checksum manifest at `/home/user/incident/trusted_checksums.sha256` that was generated before the suspected tampering occurred.

I need you to verify the integrity of all files in the `/home/user/incident/configs/` directory against the trusted manifest, then write a short report.

Please do the following:

1. Run `sha256sum --check` against the trusted manifest file (`/home/user/incident/trusted_checksums.sha256`), making sure to run it from the `/home/user/incident/` directory so the relative paths in the manifest resolve correctly.

2. Write a report to `/home/user/incident/integrity_report.txt` with the following **exact** format:

```
INTEGRITY CHECK REPORT
======================
FAILED: configs/<filename>
FAILED: configs/<filename>
OK: configs/<filename>
OK: configs/<filename>
OK: configs/<filename>
```

The report must:
- Start with the two header lines exactly as shown (`INTEGRITY CHECK REPORT` then `======================`).
- List every file from the manifest, one per line, prefixed with either `FAILED: ` or `OK: ` depending on whether the checksum matched.
- Sort the lines so all `FAILED:` entries appear before all `OK:` entries.
- Within each group (`FAILED` and `OK`), sort alphabetically by filename.
- Use the path exactly as it appears in the manifest (e.g., `configs/nginx.conf`), not an absolute path.

There should be no trailing whitespace on any line and no blank lines between entries.
