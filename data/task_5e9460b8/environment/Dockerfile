FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

mkdir -p /home/user/backup

cat > /home/user/backup/settings.yaml <<EOF
integrity_check: true
backup_schedule: "daily"
compression: "gzip"
EOF

cat > /home/user/backup/settings.toml <<EOF
integrity_check = false
backup_schedule = "weekly"
compression = "bzip2"
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
