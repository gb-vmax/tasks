I'm an edge computing engineer preparing firmware configurations and deployment scripts for a fleet of IoT devices. Before pushing to production, I need to run a security audit on the deployment bundle located at `/home/user/iot_deploy/`. Help me scan this directory for common IoT security issues and generate a report.

The deployment bundle contains device configuration files, a startup script, and service definitions. I need you to scan for the following security issues and write a final report to `/home/user/iot_deploy/security_report.txt`.

Here is what I need scanned and reported:

---

### 1. Hardcoded Credentials Scan

Search all files under `/home/user/iot_deploy/` recursively for lines matching any of these patterns (case-insensitive):
- Lines containing `password=` (with anything after the `=`)
- Lines containing `api_key=` (with anything after the `=`)
- Lines containing `secret=` (with anything after the `=`)
- Lines containing `token=` (with anything after the `=`)

For each match, record the filename (basename only, not the full path), the line number, and the full matching line (trimmed of leading/trailing whitespace). Do not include lines that are comments (i.e., where the first non-whitespace character is `#`). Do not scan the `security_report.txt` file itself.

---

### 2. Dangerous File Permissions Audit

Check the permissions of these specific files:
- `/home/user/iot_deploy/startup.sh`
- `/home/user/iot_deploy/configs/device.conf`
- `/home/user/iot_deploy/configs/mqtt.conf`
- `/home/user/iot_deploy/services/watchdog.service`

For each file, record whether it is **UNSAFE** or **OK**. A file is UNSAFE if it is world-writable (i.e., the "others write" permission bit is set — mode bit `o+w`). Otherwise it is OK.

---

### 3. Insecure Protocol Detection

Search all files under `/home/user/iot_deploy/` recursively for lines (non-comment, first non-whitespace character is not `#`) that reference insecure protocols. Flag any line containing any of these strings (case-insensitive):
- `telnet`
- `ftp://`
- `http://` (but NOT `https://`)

Record the filename (basename only), line number, and the full matching line (trimmed). Do not scan `security_report.txt` itself.

---

### 4. Write the Security Report

Write the file `/home/user/iot_deploy/security_report.txt` with **exactly** this format (replace bracketed placeholders with actual values):

```
=== IOT SECURITY AUDIT REPORT ===
Scanned directory: /home/user/iot_deploy

--- SECTION 1: HARDCODED CREDENTIALS ---
Total findings: <N>
[filename]:[line_number]: [matched_line]
[filename]:[line_number]: [matched_line]
...

--- SECTION 2: FILE PERMISSION AUDIT ---
startup.sh: <OK|UNSAFE>
device.conf: <OK|UNSAFE>
mqtt.conf: <OK|UNSAFE>
watchdog.service: <OK|UNSAFE>
Total unsafe files: <N>

--- SECTION 3: INSECURE PROTOCOLS ---
Total findings: <N>
[filename]:[line_number]: [matched_line]
[filename]:[line_number]: [matched_line]
...

--- SUMMARY ---
Total issues found: <N>
Risk level: <LOW|MEDIUM|HIGH|CRITICAL>
```

Rules for the report:
- In Sections 1 and 3, list findings sorted by filename (alphabetically by basename), then by line number ascending within each file.
- The `Total issues found` in the SUMMARY is the sum of: (number of credential findings) + (number of unsafe files) + (number of insecure protocol findings).
- Risk level is determined by total issues: 0 = LOW, 1–3 = MEDIUM, 4–7 = HIGH, 8 or more = CRITICAL.
- If a section has zero findings, still print `Total findings: 0` (for sections 1 and 3) with no finding lines below it.
- Each finding line must be in the format `filename:line_number: matched_line` — note the space after the second colon.
- The matched_line should be the actual content of the line with leading and trailing whitespace stripped.

---

The files already exist in `/home/user/iot_deploy/`. I just need you to perform the scans and generate the report file exactly as specified above.
