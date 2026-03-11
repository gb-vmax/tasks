I'm setting up a monitoring alert system on our Linux server and need help organizing the directory structure, user groups, and permissions correctly — then generating an audit report so I can verify everything is configured right before we go live.

Here's what I need you to do:

---

### Step 1: Create the group and users

Create a group called `monitors` (you can let the system assign the GID automatically, but note it for later).

Create two new system users (with `--no-create-home` and `--shell /usr/sbin/nologin`):
- `alertagent` — add this user to the `monitors` group
- `logreader` — add this user to the `monitors` group

---

### Step 2: Set up the directory structure

Create the following directories:

- `/home/user/alertsys/configs` — should be owned by `alertagent:monitors`, permissions `750`
- `/home/user/alertsys/logs` — should be owned by `logreader:monitors`, permissions `770`
- `/home/user/alertsys/reports` — should be owned by `user:monitors`, permissions `775`

---

### Step 3: Place files into the directories

Create the following files with the specified contents, ownership, and permissions:

**`/home/user/alertsys/configs/threshold.conf`**
- Content (exactly):
  ```
  cpu_threshold=85
  mem_threshold=90
  disk_threshold=80
  ```
- Ownership: `alertagent:monitors`
- Permissions: `640`

**`/home/user/alertsys/logs/alert.log`**
- Content (exactly):
  ```
  2024-06-01T08:00:00Z INFO monitoring started
  2024-06-01T08:15:22Z WARN cpu usage at 87%
  2024-06-01T08:16:01Z ALERT disk usage at 83%
  ```
- Ownership: `logreader:monitors`
- Permissions: `660`

**`/home/user/alertsys/reports/daily_summary.txt`**
- Content (exactly):
  ```
  Date: 2024-06-01
  Alerts triggered: 2
  Status: review required
  ```
- Ownership: `user:monitors`
- Permissions: `664`

---

### Step 4: Generate the audit report

Create a file at `/home/user/alertsys/audit_report.txt` that documents the permissions and ownership of all three directories and all three files. The file must follow this **exact format**:

```
=== ALERTSYS PERMISSION AUDIT ===

[DIRECTORIES]
path=/home/user/alertsys/configs owner=alertagent group=monitors perms=750
path=/home/user/alertsys/logs owner=logreader group=monitors perms=770
path=/home/user/alertsys/reports owner=user group=monitors perms=775

[FILES]
path=/home/user/alertsys/configs/threshold.conf owner=alertagent group=monitors perms=640
path=/home/user/alertsys/logs/alert.log owner=logreader group=monitors perms=660
path=/home/user/alertsys/reports/daily_summary.txt owner=user group=monitors perms=664

[SUMMARY]
total_directories=3
total_files=3
group_verified=monitors
```

Rules for generating the audit report:
- The `perms` value must be the **3-digit octal** representation (e.g., `750`, not `0750` and not `-rwxr-x---`).
- The `owner` and `group` values must be the actual symbolic names (not numeric UIDs/GIDs).
- The order of lines within `[DIRECTORIES]` and `[FILES]` sections must match the order shown above exactly.
- The `group_verified` field should list the group name that all six entries share as their group owner (which is `monitors` if everything was set up correctly).
- There must be a blank line between each section header and after the `[DIRECTORIES]` block (i.e., blank line before `[FILES]`), exactly as shown above.
- The file itself should be owned by `user:user` with permissions `644`.

---

Please make sure every ownership assignment, permission, and file content is exactly as specified — the audit report will be checked automatically against the actual filesystem state.
