#!/bin/bash
set -e
cd /home/user

ls /home/user/backups/pg/ && echo "---" && cat /home/user/backups/pg/checksums.sha256
sha256sum /home/user/backups/pg/db_primary_20240801.dump /home/user/backups/pg/db_replica_20240801.dump /home/user/backups/pg/db_primary_20240731.dump /home/user/backups/pg/db_replica_20240731.dump
cat > /home/user/backups/integrity_report.txt << 'EOF'
BACKUP INTEGRITY REPORT
=======================
db_primary_20240801.dump: OK
db_replica_20240801.dump: OK
db_primary_20240731.dump: FAILED
db_replica_20240731.dump: OK
=======================
PASSED: 3
FAILED: 1
STATUS: CORRUPTED
EOF
cat /home/user/backups/integrity_report.txt
