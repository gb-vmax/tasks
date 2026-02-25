FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
# Do NOT run the solution or create output files

# Ensure backup directory exists (should already exist, but for safety)
mkdir -p /home/user/backup

# Create the backup_report.csv file with the specified contents
cat > /home/user/backup/backup_report.csv <<EOF
backup_id,timestamp,status,checksum
01,2024-06-14T06:00:01Z,SUCCESS,ad328d766fbe
02,2024-06-14T08:30:25Z,FAILURE,09842dbeff92
03,2024-06-14T10:13:52Z,SUCCESS,ff33aabb2200
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
