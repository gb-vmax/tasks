FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
install -d -m 755 /home/user/configs

cat > /home/user/configs/backup.yml <<EOF
backup_dir: /mnt/storage/backups
integrity_check_dir: /mnt/storage/integrity
retention_days: 30
EOF

cat > /home/user/configs/backup.toml <<EOF
backup_dir = "/mnt/storage/backups"
retention_days = 30

[checks]
integrity_check_dir = "/mnt/storage/integrity"
EOF

# Do NOT create /home/user/backup_integrity_locations.log

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
