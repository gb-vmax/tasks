#!/bin/bash
set -e
cd /home/user

ls /home/user/configs/ && ls /home/user/backups/
tar -czf /home/user/backups/configs_backup.tar.gz -C /home/user configs/
tar -tzf /home/user/backups/configs_backup.tar.gz
sha256sum /home/user/backups/configs_backup.tar.gz > /home/user/backups/configs_backup.tar.gz.sha256
cat /home/user/backups/configs_backup.tar.gz.sha256
sha256sum --check /home/user/backups/configs_backup.tar.gz.sha256
