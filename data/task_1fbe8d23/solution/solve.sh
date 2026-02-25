#!/bin/bash
set -e
cd /home/user

ping -c 5 8.8.8.8 > /home/user/network/ping_output.txt
mkdir -p /home/user/network/backup && cd /home/user/network && tar -czf /home/user/network/backup/network_logs.tar.gz ping_output.txt
echo -e "Backup created: network_logs.tar.gz\n$(date -u +"%Y-%m-%dT%H:%M:%SZ")" > /home/user/network/backup/backup_log.txt
tar -tzf /home/user/network/backup/network_logs.tar.gz
cat /home/user/network/backup/backup_log.txt
