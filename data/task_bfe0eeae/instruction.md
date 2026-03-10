I'm a compliance analyst and I need to generate a standardized audit trail entry for a security event log. The requirement is that all audit entries must be timestamped in **UTC** and formatted according to the **en_US.UTF-8** locale. I need your help setting the correct environment and writing a properly formatted audit log entry.

Here's what needs to be done:

**Step 1: Write a shell script**

Create a shell script at `/home/user/audit/gen_audit_entry.sh` that does the following when executed:

- Sets the `TZ` environment variable to `UTC` and the `LANG` environment variable to `en_US.UTF-8` for the duration of the script.
- Generates a single audit log line and **appends** it to `/home/user/audit/audit_trail.log`.
- The log line must follow this exact format (pipe-delimited):

```
<timestamp>|COMPLIANCE|INFO|Audit trail initialized|TZ=UTC|LANG=en_US.UTF-8
```

Where `<timestamp>` is the current date and time in this exact format: `%Y-%m-%dT%H:%M:%SZ` (e.g., `2024-03-15T09:00:00Z`), generated using the `date` command with `TZ=UTC` explicitly set.

**Step 2: Run the script**

Execute the script. After execution, `/home/user/audit/audit_trail.log` must exist and contain exactly one line matching the format above.

**Verification requirements:**

The automated test will check:
1. The file `/home/user/audit/gen_audit_entry.sh` exists and is executable.
2. The file `/home/user/audit/audit_trail.log` exists and contains exactly **one line**.
3. That line matches the regex pattern: `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\|COMPLIANCE\|INFO\|Audit trail initialized\|TZ=UTC\|LANG=en_US\.UTF-8$`
4. The timestamp in the log entry uses a `Z` suffix (indicating UTC), not a numeric offset like `+0000`.

Please create the `/home/user/audit/` directory if it doesn't exist, write the script, make it executable, and run it.
