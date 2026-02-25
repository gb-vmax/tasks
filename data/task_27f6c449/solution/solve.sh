#!/bin/bash
set -e
cd /home/user

cp /home/user/data/customer_data.db /home/user/backups/customer_data_backup.db
sqlite3 /home/user/backups/customer_data_backup.db "SELECT name FROM sqlite_master WHERE type='table' AND name IN ('customers','orders') ORDER BY CASE name WHEN 'customers' THEN 1 WHEN 'orders' THEN 2 END;" | sed 's/^/Table: /' > /home/user/backup_logs/backup_verification.log
cat /home/user/backup_logs/backup_verification.log
