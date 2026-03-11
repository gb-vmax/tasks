#!/bin/bash
set -e
cd /home/user

cat /home/user/configs/app.conf
mkdir -p /home/user/configs/backups
cp /home/user/configs/app.conf /home/user/configs/backups/app.conf.bak
sed -i 's/^log_level=.*/log_level=debug/' /home/user/configs/app.conf && sed -i 's/^max_connections=.*/max_connections=150/' /home/user/configs/app.conf
cd /home/user/configs && diff -u backups/app.conf.bak app.conf > backups/changes.diff
cat /home/user/configs/backups/changes.diff
cat /home/user/configs/app.conf && echo "---" && cat /home/user/configs/backups/app.conf.bak
