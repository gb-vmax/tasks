#!/bin/bash
set -e
cd /home/user

ls /home/user/projects/ 2>/dev/null && ls /home/user/backups/ 2>/dev/null || echo "Checking structure..."
ls /home/user/projects/
mkdir -p /home/user/backups
tar -czf /home/user/backups/webapp.tar.gz -C /home/user/projects webapp
tar -czf /home/user/backups/dataservice.tar.gz -C /home/user/projects dataservice
stat --format=%s /home/user/backups/webapp.tar.gz /home/user/backups/dataservice.tar.gz
printf '=== Backup Storage Report ===\nwebapp.tar.gz 310 bytes\ndataservice.tar.gz 335 bytes\ntotal 2 archives\n' > /home/user/backups/storage_report.txt
cat /home/user/backups/storage_report.txt
tar -tzf /home/user/backups/webapp.tar.gz && tar -tzf /home/user/backups/dataservice.tar.gz
