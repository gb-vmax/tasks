I'm a compliance officer auditing a Linux server and I need to generate a quick report of all non-system (human) user accounts on the machine. These are accounts with a UID of 1000 or greater — the standard range for regular user accounts on Linux systems.

Please read `/etc/passwd` and produce a formatted audit report at `/home/user/audit/user_accounts.txt`.

The report must have this exact format:

```
=== USER ACCOUNT AUDIT REPORT ===
Generated from: /etc/passwd

Non-system accounts (UID >= 1000):
  <username> | UID: <uid> | Home: <home_dir> | Shell: <shell>
  <username> | UID: <uid> | Home: <home_dir> | Shell: <shell>
  ...

Total non-system accounts: <N>
```

Specific requirements:
- The accounts must be sorted in ascending order by UID.
- Each account line must be indented with exactly two spaces.
- Fields must be separated by ` | ` (space, pipe, space).
- The `Shell` field should show the full path as it appears in `/etc/passwd`.
- Exclude the `nobody` account (UID 65534) if present — this is a special pseudo-user, not a real account.
- The directory `/home/user/audit/` may not exist yet; create it if needed.
- Do not include any blank lines between the account entries.
