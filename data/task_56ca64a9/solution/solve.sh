#!/bin/bash
set -e
cd /home/user

cat /home/user/backups/backup_config.yaml
cat /home/user/backups/retention.toml
cat > /home/user/backups/backup_config.yaml << 'EOF'
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
EOF
cat > /home/user/backups/retention.toml << 'EOF'
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
EOF
cat /home/user/backups/backup_config.yaml && echo "---" && cat /home/user/backups/retention.toml
