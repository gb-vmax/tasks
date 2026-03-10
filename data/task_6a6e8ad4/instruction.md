I'm a site administrator and I need to generate a quick account status report from our user database export. I have a CSV file at `/home/user/admin/users.csv` that contains user account records. Each line has the format:

```
username,email,role,status
```

The `status` field is either `active` or `inactive`. The `role` field is one of `admin`, `editor`, or `viewer`.

I need you to create a shell script at `/home/user/admin/gen_report.sh` that reads `/home/user/admin/users.csv` and writes a report to `/home/user/admin/report.txt`. Then run the script to produce the report.

The report must have this exact format:

```
=== USER ACCOUNT REPORT ===
Total users: <N>
Active: <N>
Inactive: <N>

Active admins:
  <username> (<email>)
  <username> (<email>)

Active editors:
  <username> (<email>)
  <username> (<email>)
```

Rules:
- Skip the CSV header line (`username,email,role,status`).
- "Total users" is the count of all non-header rows.
- "Active" and "Inactive" are counts of users with those statuses.
- Under "Active admins", list all users where `role=admin` AND `status=active`, sorted alphabetically by username.
- Under "Active editors", list all users where `role=editor` AND `status=active`, sorted alphabetically by username.
- Each user entry is indented with two spaces, formatted as `  <username> (<email>)`.
- If there are no active admins or no active editors, the section should still appear but with no entries beneath it.
- Do NOT include a section for viewers.
- The script must be executable (`chmod +x`).
