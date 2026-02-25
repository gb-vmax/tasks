You are a backup operator testing restore procedures. In your home directory (/home/user), there is a YAML file named /home/user/backup_config.yaml with the following initial contents:

---
name: daily_backup
enabled: true
paths:
  - /home/user/documents
  - /home/user/photos
retention_days: 7
---

And a TOML file named /home/user/restore_points.toml with these initial contents:

[restore1]
timestamp = "2024-05-22T10:00:00Z"
path = "/home/user/documents"
status = "valid"

[restore2]
timestamp = "2024-05-22T14:00:00Z"
path = "/home/user/photos"
status = "valid"

Perform the following actions:

1. Edit the YAML file /home/user/backup_config.yaml so that:
   - The enabled field is set to false.
   - The retention_days field is changed to 3.

2. Edit the TOML file /home/user/restore_points.toml so that:
   - The status of [restore2] is changed from "valid" to "invalid".

3. Create a log file at /home/user/restore_test.log. The log file must have exactly this format (with no surrounding extra lines):

Backup config updated: enabled false, retention_days 3
Restore2 status updated: invalid

Automated verification will check for the precise structure of the YAML and TOML files and the exact content of the log file as specified above.
