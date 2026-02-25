FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
# Do NOT run the solution or create output files

cat > /home/user/backup_config.yaml <<'EOF'
---
name: daily_backup
enabled: true
paths:
  - /home/user/documents
  - /home/user/photos
retention_days: 7
---
EOF

cat > /home/user/restore_points.toml <<'EOF'
[restore1]
timestamp = "2024-05-22T10:00:00Z"
path = "/home/user/documents"
status = "valid"

[restore2]
timestamp = "2024-05-22T14:00:00Z"
path = "/home/user/photos"
status = "valid"
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
