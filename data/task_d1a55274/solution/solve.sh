#!/bin/bash
set -e
cd /home/user

find /home/user/projects/website -print | head -50
mkdir -p /home/user/backups && tar -czf /home/user/backups/website_backup.tar.gz -C /home/user/projects website
tar -tzf /home/user/backups/website_backup.tar.gz > /home/user/backups/website_backup.manifest
echo "=== Archive contents ===" && tar -tzf /home/user/backups/website_backup.tar.gz && echo "=== Manifest file ===" && cat /home/user/backups/website_backup.manifest && echo "=== File sizes ===" && ls -lh /home/user/backups/
