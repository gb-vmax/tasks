FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/backups

cat > /home/user/backups/backup_run.log << 'EOF'
# Backup run started 2024-11-01 02:00:00
BACKUP|JOB001|webserver01|SUCCESS|800|60
BACKUP|JOB002|dbserver01|FAILED|0|45

BACKUP|JOB003|fileserver01|SUCCESS|1523|95
# checkpoint
BACKUP|JOB004|archivehost|SUCCESS|512|30
BACKUP|JOB005|webserver02|SUCCESS|4096|210
BACKUP|JOB006|testbox|FAILED|0|12
BACKUP|JOB007|appserver03|SUCCESS|999|88
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
