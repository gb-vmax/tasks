FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

mkdir -p /home/user/db-backup-utility

cat > /home/user/db-backup-utility/config.yaml <<EOF
version: "2.3.4"
backup:
  path: "/var/backups"
  schedule: "daily"
EOF

cat > /home/user/db-backup-utility/CHANGELOG.md <<EOF
## [2.3.4] - 2024-05-19
### Fixed
- Restore job now handles missing file errors (Bugfix).

## [2.3.0] - 2024-04-02
### Added
- Incremental backup mode introduced.
- Settings for backup encryption.
EOF

cat > /home/user/db-backup-utility/README.md <<EOF
DB Backup Utility
=================
Simple tool for managing PostgreSQL backups.
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
