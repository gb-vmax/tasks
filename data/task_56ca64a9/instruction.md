Hey, I need your help updating two backup configuration files for our database reliability setup. We just upgraded our backup infrastructure and need to change some settings before the next scheduled backup window.

**File 1: `/home/user/backups/backup_config.yaml`**

This YAML file currently has some outdated settings. I need you to make the following changes:

- Change `retention_days` from its current value to `30`
- Change `schedule` from its current value to `"0 2 * * *"` (daily at 2am)
- Change `storage.bucket` from its current value to `"db-backups-prod-v2"`
- Change `storage.region` from its current value to `"us-east-2"`

The final file must look exactly like this:
```yaml
database:
  host: postgres-primary.internal
  port: 5432
  name: appdb
retention_days: 30
schedule: "0 2 * * *"
storage:
  bucket: db-backups-prod-v2
  region: us-east-2
  encryption: true
notifications:
  email: dba-team@company.com
  on_failure: true
```

**File 2: `/home/user/backups/retention.toml`**

This TOML file controls how long different backup types are kept. I need you to update it as follows:

- Change `[policy.daily].keep_days` from its current value to `14`
- Change `[policy.weekly].keep_days` from its current value to `60`
- Change `[policy.monthly].keep_days` from its current value to `365`
- Change `enabled` (the top-level field) from its current value to `true`

The final file must look exactly like this:
```toml
enabled = true
version = "2.0"

[policy.daily]
keep_days = 14
compress = true

[policy.weekly]
keep_days = 60
compress = true

[policy.monthly]
keep_days = 365
compress = false
```

Please update both files so they match the exact contents shown above. These files already exist on disk — just modify the specific fields listed, keeping everything else exactly as-is.
