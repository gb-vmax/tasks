I'm a compliance analyst and I need your help generating an audit trail report from our server configuration files. We have several INI-format configuration files stored in `/home/user/audit/configs/` that define security and operational settings for different services. I need you to parse these files, check them against our compliance rules, and write a formatted audit report.

Here are the configuration files you'll be working with:

- `/home/user/audit/configs/webserver.ini`
- `/home/user/audit/configs/database.ini`
- `/home/user/audit/configs/mailrelay.ini`

**Compliance Rules to Enforce:**

For every INI file, check the following keys across any section they appear in:

1. `ssl_enabled` must equal `true` — if `false` or missing, flag as **FAIL**
2. `max_connections` must be an integer ≤ 100 — if > 100 or missing, flag as **FAIL**
3. `log_level` must be one of: `warn`, `error`, `critical` — if `debug`, `info`, or any other value or missing, flag as **FAIL**
4. `auth_required` must equal `true` — if `false` or missing, flag as **FAIL**
5. `timeout_seconds` must be an integer ≤ 30 — if > 30 or missing, flag as **FAIL**

If a key is present in multiple sections of the same file, check each occurrence independently. A file PASSES a rule only if every occurrence of that key in the file is compliant. If the key is absent from the entire file, that rule is a FAIL for that file.

**Output File:**

Write the audit report to `/home/user/audit/report.txt`. The format must be exactly as follows:

```
=== COMPLIANCE AUDIT REPORT ===
Generated for: /home/user/audit/configs

--- webserver.ini ---
ssl_enabled: PASS
max_connections: FAIL
log_level: FAIL
auth_required: PASS
timeout_seconds: PASS
Status: NON-COMPLIANT

--- database.ini ---
ssl_enabled: PASS
max_connections: PASS
log_level: PASS
auth_required: FAIL
timeout_seconds: FAIL
Status: NON-COMPLIANT

--- mailrelay.ini ---
ssl_enabled: PASS
max_connections: PASS
log_level: PASS
auth_required: PASS
timeout_seconds: PASS
Status: COMPLIANT

=== SUMMARY ===
Total files checked: 3
Compliant: 1
Non-compliant: 2
Compliance rate: 33%

=== FAILED RULES ACROSS ALL FILES ===
max_connections: webserver.ini
log_level: webserver.ini
auth_required: database.ini
timeout_seconds: database.ini
```

Important formatting notes:
- Files must appear in alphabetical order: `database.ini`, `mailrelay.ini`, `webserver.ini`.
- Each file block starts with `--- filename ---` (just the filename, not the full path).
- The five rules appear in the order listed above for every file, every time.
- `Status:` is `COMPLIANT` if all 5 rules pass, otherwise `NON-COMPLIANT`.
- `Compliance rate:` is integer division (floor), expressed as a percentage with no decimal point (e.g., `33%` not `33.3%`).
- The `=== FAILED RULES ACROSS ALL FILES ===` section lists each rule that failed in at least one file, in the same order as the five rules, followed by a colon and a space, then a comma-separated list of filenames (alphabetical) where that rule failed. Rules with zero failures across all files are omitted entirely from this section.
- There is a blank line between the last file block and `=== SUMMARY ===`, and a blank line between `=== SUMMARY ===` block and `=== FAILED RULES ACROSS ALL FILES ===`.

The actual PASS/FAIL values in your output will depend on the real contents of the config files. I've described the format above using placeholder values to illustrate the structure — your report must reflect the actual values found in the config files.

Please parse those INI files, evaluate the compliance rules, and write the report to `/home/user/audit/report.txt`.
