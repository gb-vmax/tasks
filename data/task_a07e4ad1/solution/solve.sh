#!/bin/bash
set -e
cd /home/user

ls /home/user/logs/
mkdir -p /home/user/backups
tar -czf /home/user/backups/app-jan2024.tar.gz -C /home/user/logs/ app-2024-01-*.log
cd /home/user/logs/ && tar -czf /home/user/backups/app-jan2024.tar.gz app-2024-01-*.log
tar -tzf /home/user/backups/app-jan2024.tar.gz > /home/user/backups/app-jan2024.manifest
echo "=== Archive contents ===" && tar -tzf /home/user/backups/app-jan2024.tar.gz && echo "=== Manifest file ===" && cat /home/user/backups/app-jan2024.manifest && echo "=== Excluded files check ===" && tar -tzf /home/user/backups/app-jan2024.tar.gz | grep -E "(app-2024-02|system)" || echo "No excluded files found in archive (correct!)"
tar -tzf /home/user/backups/app-jan2024.tar.gz
cat /home/user/backups/app-jan2024.manifest
