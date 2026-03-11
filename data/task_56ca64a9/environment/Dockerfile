FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/backups

cat > /home/user/backups/backup_config.yaml << 'EOF'
database:
  host: postgres-primary.internal
  port: 5432
  name: appdb
retention_days: 7
schedule: "0 3 * * *"
storage:
  bucket: db-backups-staging
  region: us-west-2
  encryption: true
notifications:
  email: dba-team@company.com
  on_failure: true
EOF

cat > /home/user/backups/retention.toml << 'EOF'
enabled = false
version = "2.0"

[policy.daily]
keep_days = 7
compress = true

[policy.weekly]
keep_days = 30
compress = true

[policy.monthly]
keep_days = 180
compress = false
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
