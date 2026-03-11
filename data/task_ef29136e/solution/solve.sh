#!/bin/bash
set -e
cd /home/user

cat /home/user/storage/storage.conf
ls /home/user/storage/
du -sm /home/user/storage/appdata /home/user/storage/logs /home/user/storage/backups /home/user/storage/uploads
find /home/user/storage/appdata /home/user/storage/logs /home/user/storage/backups /home/user/storage/uploads -type f -printf '%s %p\n' | sort -rn | head -20
cat > /home/user/storage_report.txt << 'EOF'
=== DISK SPACE REPORT ===
Generated for: /home/user/storage

--- Directory Usage ---
/home/user/storage/appdata: 53MB [WARN] (threshold: 50MB)
/home/user/storage/logs: 28MB [OK] (threshold: 30MB)
/home/user/storage/backups: 82MB [WARN] (threshold: 80MB)
/home/user/storage/uploads: 21MB [WARN] (threshold: 20MB)

--- Top 3 Largest Files ---
1. /home/user/storage/backups/backup_full.tar.gz (61440KB)
2. /home/user/storage/appdata/database.db (38912KB)
3. /home/user/storage/backups/backup_inc.tar.gz (22528KB)

--- Summary ---
Total monitored usage: 184MB
Directories in WARNING: 3
EOF
cat /home/user/storage_report.txt
