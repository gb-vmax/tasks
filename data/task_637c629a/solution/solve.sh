#!/bin/bash
set -e
cd /home/user

ls -la /home/user/appdata/
chmod 600 /home/user/appdata/db.conf /home/user/appdata/api_keys.conf && chmod 640 /home/user/appdata/app.log
ls -la /home/user/appdata/
mkdir -p /home/user/backups && tar -czvf /home/user/backups/appdata_backup.tar.gz -C /home/user appdata/
tar -tzvf /home/user/backups/appdata_backup.tar.gz > /home/user/backups/archive_manifest.txt
cat /home/user/backups/archive_manifest.txt
tar -tzvf /home/user/backups/appdata_backup.tar.gz | grep -v '^d' > /home/user/backups/archive_manifest.txt
cat /home/user/backups/archive_manifest.txt
