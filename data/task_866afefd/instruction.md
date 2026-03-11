I'm a DevSecOps engineer and I need your help enforcing a password policy audit on our service account configuration file. We have a JSON file at `/home/user/devsecops/accounts.json` that lists service accounts and their configuration. My job is to extract only the non-compliant accounts (those where `"password_expires": false`) and write a policy violation report.

Please produce a report file at `/home/user/devsecops/violations.txt` that lists non-compliant accounts in the following exact format:

```
POLICY VIOLATION REPORT
=======================
NON-COMPLIANT ACCOUNTS (password_expires=false):

<account_name> | role=<role> | env=<env>
<account_name> | role=<role> | env=<env>
...

Total violations: <N>
```

Requirements:
- List accounts in the order they appear in the source JSON file (do not sort them).
- Only include accounts where `"password_expires"` is `false` (boolean, not the string "false").
- The header lines must match exactly, including the `=` separator line being exactly 23 `=` characters.
- Each account line uses ` | ` (space-pipe-space) as the delimiter.
- The `Total violations:` line at the bottom must reflect the exact count of listed accounts.
- There must be a blank line between the header block and the first account line, and another blank line between the last account line and the `Total violations:` line.

The source file `/home/user/devsecops/accounts.json` already exists on the system. Please generate the report from it.
