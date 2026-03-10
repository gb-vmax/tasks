I'm a penetration tester preparing for an engagement and I need to verify the integrity of my toolkit before deploying it. I've had some concerns that one or more of my scanning tool binaries may have been tampered with (either corrupted or replaced by a compromised version), and I need to know exactly which ones are safe to use.

My toolkit directory is at `/home/user/pentest/tools/`. It contains the following files:

- `nmap_wrapper.sh`
- `enum_users.py`
- `port_scan.sh`
- `vuln_check.py`
- `report_gen.sh`

There is also a trusted checksums manifest at `/home/user/pentest/manifest.sha256` that contains the known-good SHA256 hashes for each of these files, in standard `sha256sum` output format (hash, two spaces, filename — no directory path, just the bare filename).

Please do the following:

1. Compute the SHA256 checksum of each file in `/home/user/pentest/tools/` and compare them against the entries in `/home/user/pentest/manifest.sha256`.

2. Write a verification report to `/home/user/pentest/integrity_report.txt` with the following exact format:

```
=== TOOLKIT INTEGRITY REPORT ===

OK: enum_users.py
OK: nmap_wrapper.sh
OK: port_scan.sh
TAMPERED: report_gen.sh
OK: vuln_check.py

VERDICT: 1 file(s) failed integrity check.
```

The files should be listed in **alphabetical order** by filename. Each line must start with either `OK: ` or `TAMPERED: ` followed by the filename (no directory path). After a blank line following the file list, the final verdict line must read `VERDICT: N file(s) failed integrity check.` where `N` is the exact count of files that did NOT match the manifest. There must be a blank line between the last file status line and the VERDICT line.

Use exactly this format — the automated test will check for precise line-by-line matches. Do not include checksums, extra whitespace, or additional commentary in the report file.
