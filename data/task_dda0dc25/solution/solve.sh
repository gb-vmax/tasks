#!/bin/bash
set -e
cd /home/user

ls /home/user/configs/ && ls /home/user/backups/
tar -czvf /home/user/backups/configs_v2.tar.gz -C /home/user configs/
tar -tzvf /home/user/backups/configs_v2.tar.gz > /home/user/backups/configs_v2.manifest
HASH=$(sha256sum /home/user/backups/configs_v2.tar.gz | awk '{print $1}'); SIZE=$(stat --format="%s" /home/user/backups/configs_v2.tar.gz); echo "configs_v2.tar.gz $HASH $SIZE" >> /home/user/backups/backup.log
echo "=== Manifest ===" && cat /home/user/backups/configs_v2.manifest && echo "=== Backup Log ===" && cat /home/user/backups/backup.log && echo "=== Archive test extract ===" && tar -tzvf /home/user/backups/configs_v2.tar.gz
