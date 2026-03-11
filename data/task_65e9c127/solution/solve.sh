#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/backups
tar -czf /home/user/backups/alerts_backup.tar.gz -C /home/user/monitoring alerts
tar -tzf /home/user/backups/alerts_backup.tar.gz > /home/user/backups/alerts_manifest.txt
cat /home/user/backups/alerts_manifest.txt
