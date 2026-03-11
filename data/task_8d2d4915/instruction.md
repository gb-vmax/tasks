I'm a DevSecOps engineer and I need your help enforcing a secrets-hygiene policy on a service configuration file. We have a raw environment config at `/home/user/services/api-gateway/config.env` that developers wrote by hand. Unfortunately, it doesn't comply with our policy standards — it contains banned variables, improperly formatted lines, and some variables need to be masked before they can be written to a policy-compliant output file.

Here's what I need you to do:

**Step 1: Inspect the source file**

Read `/home/user/services/api-gateway/config.env`. It contains lines in `KEY=VALUE` format (no spaces around `=`), blank lines, and comment lines starting with `#`.

**Step 2: Apply policy rules and write a compliant file**

Create a new file at `/home/user/services/api-gateway/config.compliant.env` by processing the source file with these rules, applied in order:

1. **Strip non-data lines**: Skip all blank lines and comment lines (lines starting with `#`).
2. **Remove banned variables**: Do not include any line where the key is `DEBUG`, `DEV_MODE`, or `LEGACY_AUTH_TOKEN`.
3. **Mask secrets**: For any key that contains the substring `SECRET`, `PASSWORD`, or `TOKEN` (case-sensitive), replace the value with exactly `***REDACTED***`.
4. **Sort the output**: Write all remaining lines sorted alphabetically by key name (A-Z).
5. **Add a policy header**: The very first line of the output file must be exactly:
   ```
   # compliant-env-v1 policy=strict
   ```
   followed by a blank line, then the sorted key=value lines.

The output file must use exactly this format — no trailing spaces, no extra blank lines between entries, a single blank line between the header comment and the first key=value line, and a newline at the end of the file.

**Step 3: Write a policy audit summary**

Create a file at `/home/user/services/api-gateway/audit.log` with a summary of what was done. The format must be exactly:

```
AUDIT: config.env policy enforcement
banned_removed: <N>
secrets_redacted: <N>
lines_written: <N>
```

Where:
- `banned_removed` is the count of lines dropped because the key was `DEBUG`, `DEV_MODE`, or `LEGACY_AUTH_TOKEN`.
- `secrets_redacted` is the count of lines where the value was replaced with `***REDACTED***`.
- `lines_written` is the count of key=value lines in the compliant file (not counting the header comment line or the blank line).

There should be a newline at the end of `audit.log` and no extra lines.
