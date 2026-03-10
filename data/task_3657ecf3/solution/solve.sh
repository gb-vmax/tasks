#!/bin/bash
set -e
cd /home/user

ls /home/user/projects/client_alpha
find /home/user/projects/client_alpha -type f
mkdir -p /home/user/backups && tar -czf /home/user/backups/client_alpha.tar.gz -C /home/user/projects client_alpha
stat -c%s /home/user/backups/client_alpha.tar.gz
tar -tzf /home/user/backups/client_alpha.tar.gz | grep -v '/$' | grep -c '.'
printf 'archive: client_alpha.tar.gz\nsize_bytes: 392\nfiles: 4\n' > /home/user/backups/manifest.txt
cat /home/user/backups/manifest.txt
tar -tzf /home/user/backups/client_alpha.tar.gz
