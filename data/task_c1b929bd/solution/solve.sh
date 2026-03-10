#!/bin/bash
set -e
cd /home/user

find /home/user/k8s/operators -type f -name "*.yaml"
mkdir -p /home/user/backups
cd /home/user/k8s && find operators -type f -name "*.yaml" | tar -czf /home/user/backups/manifests_backup.tar.gz -T -
tar -tf /home/user/backups/manifests_backup.tar.gz > /home/user/backups/manifests_backup.txt
cat /home/user/backups/manifests_backup.txt
tar -tzf /home/user/backups/manifests_backup.tar.gz && echo "Archive is valid"
