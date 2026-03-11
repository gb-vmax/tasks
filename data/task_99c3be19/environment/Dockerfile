FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the data directory structure
mkdir -p /home/user/data/logs
mkdir -p /home/user/data/backups
mkdir -p /home/user/data/uploads
mkdir -p /home/user/data/tmp
mkdir -p /home/user/data/configs

# Create files with specified sizes using dd
dd if=/dev/zero of=/home/user/data/backups/backup.tar bs=1M count=200 status=none
dd if=/dev/zero of=/home/user/data/logs/access.log bs=1M count=50 status=none
dd if=/dev/zero of=/home/user/data/uploads/user_uploads.bin bs=1M count=30 status=none
dd if=/dev/zero of=/home/user/data/tmp/scratch.bin bs=1M count=5 status=none
dd if=/dev/zero of=/home/user/data/configs/settings.conf bs=1M count=1 status=none

# Do NOT create /home/user/disk_report.txt — agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
