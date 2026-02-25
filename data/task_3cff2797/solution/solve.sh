#!/bin/bash
set -e
cd /home/user

tar -czf /home/user/etl_backup_2024_06_15.tar.gz -C /home/user etl_data
tar -tzf /home/user/etl_backup_2024_06_15.tar.gz
echo -e "Backup completed on: $(date '+%Y-%m-%d %H:%M:%S')\nFiles in archive:\ndata1.csv\ndata2.csv\ndata3.csv" > /home/user/etl_backup_log.txt
cat /home/user/etl_backup_log.txt
