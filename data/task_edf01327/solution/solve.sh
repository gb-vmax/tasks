#!/bin/bash
set -e
cd /home/user

find /home/user/datastore -type f | head -50
find /home/user/datastore -type f -exec stat --format="%s %n" {} \; | sort
mkdir -p /home/user/backup_analysis
cat > /home/user/backup_analysis/projects_summary.txt << 'EOF'
Directory: /home/user/datastore/projects
Total size (bytes): 70424
File count: 5
Largest file: beta/app.py (43008 bytes)
Smallest file: alpha/README.md (512 bytes)
EOF
cat > /home/user/backup_analysis/projects_top3.txt << 'EOF'
Top 3 largest files in /home/user/datastore/projects:
1. beta/app.py (43008 bytes)
2. alpha/main.c (18200 bytes)
3. shared/utils.py (7680 bytes)
EOF
cat > /home/user/backup_analysis/media_summary.txt << 'EOF'
Directory: /home/user/datastore/media
Total size (bytes): 387072
File count: 4
Largest file: videos/clip.mp4 (204800 bytes)
Smallest file: thumbs/thumb1.png (3072 bytes)
EOF
cat > /home/user/backup_analysis/media_top3.txt << 'EOF'
Top 3 largest files in /home/user/datastore/media:
1. videos/clip.mp4 (204800 bytes)
2. images/photo1.jpg (92160 bytes)
3. images/photo2.jpg (87040 bytes)
EOF
cat > /home/user/backup_analysis/logs_summary.txt << 'EOF'
Directory: /home/user/datastore/logs
Total size (bytes): 58368
File count: 3
Largest file: app/app.log (34816 bytes)
Smallest file: app/error.log (8192 bytes)
EOF
cat > /home/user/backup_analysis/logs_top3.txt << 'EOF'
Top 3 largest files in /home/user/datastore/logs:
1. app/app.log (34816 bytes)
2. system/syslog (15360 bytes)
3. app/error.log (8192 bytes)
EOF
cat > /home/user/backup_analysis/databases_summary.txt << 'EOF'
Directory: /home/user/datastore/databases
Total size (bytes): 112640
File count: 3
Largest file: backups/db1_bak.sqlite (46080 bytes)
Smallest file: db2.sqlite (20480 bytes)
EOF
cat > /home/user/backup_analysis/databases_top3.txt << 'EOF'
Top 3 largest files in /home/user/datastore/databases:
1. backups/db1_bak.sqlite (46080 bytes)
2. db1.sqlite (46080 bytes)
3. db2.sqlite (20480 bytes)
EOF
cat > /home/user/backup_analysis/master_report.txt << 'EOF'
=== BACKUP ANALYSIS REPORT ===
Generated from: /home/user/datastore

DIRECTORY SUMMARY (sorted by total size, largest first):
  1. media: 387072 bytes (4 files)
  2. databases: 112640 bytes (3 files)
  3. projects: 70424 bytes (5 files)
  4. logs: 58368 bytes (3 files)

GRAND TOTAL: 628504 bytes across 15 files

ARCHIVE RECOMMENDATIONS:
  Exceeds 100KB: databases, media
  Exceeds 50KB:  databases, logs, media, projects

LARGEST SINGLE FILE OVERALL:
  media/videos/clip.mp4 (204800 bytes)
EOF
ls /home/user/backup_analysis/ && echo "---" && cat /home/user/backup_analysis/master_report.txt
cat /home/user/backup_analysis/projects_summary.txt && echo "---" && cat /home/user/backup_analysis/media_summary.txt && echo "---" && cat /home/user/backup_analysis/logs_summary.txt && echo "---" && cat /home/user/backup_analysis/databases_summary.txt
