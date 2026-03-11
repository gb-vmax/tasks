#!/bin/bash
set -e
cd /home/user

ls /home/user/backups/
mkdir -p /home/user/restore_test
TIMEFORMAT='%R'; { time tar -xzf /home/user/backups/nightly.tar.gz -C /home/user/restore_test/; } 2>/tmp/extract_time.txt; cat /tmp/extract_time.txt
cat /tmp/extract_time.txt | xargs printf "%.2f\n"
stat --format=%s /home/user/backups/nightly.tar.gz
find /home/user/restore_test -type f | wc -l
cd /home/user/restore_test && sha256sum --check /home/user/backups/manifest.sha256
printf '=== RESTORE TEST REPORT ===\nArchive: /home/user/backups/nightly.tar.gz\nDestination: /home/user/restore_test\nExtraction time (s): 0.02\nArchive size (bytes): 350\nFiles restored: 3\nChecksum status: OK\n' > /home/user/backups/restore_report.txt
cat /home/user/backups/restore_report.txt
